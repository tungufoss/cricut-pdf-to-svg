"""Synthetic papercraft templates with exact vector ground truth.

A random low-poly convex solid is unfolded into nets: faces are laid flat across shared
edges breadth-first, and a face that would overlap its net (or make it larger than the
printable page) starts a new piece. Edges joined inside a net become folds; every other
mesh edge appears twice as a cut edge, both copies carry the same printed number, and one
copy gets a glue tab whose base is then a fold. Pieces are packed onto A4 pages and drawn
at high resolution in the template's line style; degradations (resolution, blur, JPEG,
noise) are applied afterwards so every condition shares the same truth.

    python -m bench.synth --out bench/out --templates 6 --seed 1
"""

from __future__ import annotations

import argparse
import io
import math
import random
from collections import deque
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from scipy.spatial import ConvexHull
from shapely import affinity
from shapely.geometry import Polygon
from shapely.ops import unary_union

from .model import Edge, Label, Page, Piece

A4 = (210.0, 297.0)
MARGIN, GAP = 10.0, 5.0
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
DRAW_DPI = 600


@dataclass
class Style:
    """How one template is drawn; varies between templates like real designers do."""
    cut_mm: float = 0.3
    fold_mm: float = 0.25
    dash: tuple[float, ...] = (2.0, 1.0)     # on, off (mm); four values = dash-dot
    label_mm: float = 2.5

    @classmethod
    def random(cls, rng: random.Random) -> "Style":
        dash = rng.choice([(2.0, 1.0), (1.5, 1.5), (3.0, 1.0), (2.5, 0.8, 0.4, 0.8)])
        return cls(cut_mm=rng.uniform(0.2, 0.45), fold_mm=rng.uniform(0.15, 0.35), dash=dash,
                   label_mm=rng.uniform(2.0, 3.2))


@dataclass
class Degradation:
    name: str
    dpi: int = 300
    blur_px: float = 0.0
    jpeg: int | None = None
    noise: float = 0.0


CONDITIONS = [
    Degradation("clean-300", 300),
    Degradation("scan-150", 150, blur_px=0.6, jpeg=75, noise=6.0),
    Degradation("poor-100", 100, blur_px=0.8, jpeg=50, noise=10.0),
]


class Solid:
    """Random convex low-poly solid: triangles with outward winding."""

    def __init__(self, rng: np.random.Generator, faces: int):
        n = max(8, faces // 2 + 2)                        # a hull of n points has 2n-4 triangles
        points = rng.normal(size=(n, 3))
        points /= np.linalg.norm(points, axis=1, keepdims=True)
        points *= rng.uniform(0.6, 1.4, size=3)           # squash into an ellipsoid
        hull = ConvexHull(points)
        self.v = points
        centre = points.mean(axis=0)
        tris = []
        for a, b, c in hull.simplices:
            normal = np.cross(points[b] - points[a], points[c] - points[a])
            tris.append((a, b, c) if normal @ (points[a] - centre) > 0 else (a, c, b))
        self.faces = tris
        self.edge_faces: dict[tuple[int, int], list[int]] = {}
        for f, tri in enumerate(tris):
            for i in range(3):
                key = tuple(sorted((tri[i], tri[(i + 1) % 3])))
                self.edge_faces.setdefault(key, []).append(f)

    def neighbours(self, f: int):
        tri = self.faces[f]
        for i in range(3):
            key = tuple(sorted((tri[i], tri[(i + 1) % 3])))
            for g in self.edge_faces[key]:
                if g != f:
                    yield g, key

    def mean_edge(self) -> float:
        return float(np.mean([np.linalg.norm(self.v[a] - self.v[b]) for a, b in self.edge_faces]))


class Unfolder:
    """Greedy breadth-first unfolding of a solid into non-overlapping nets that fit a page."""

    def __init__(self, solid: Solid, scale: float, rng: random.Random, max_faces: int):
        self.s, self.scale, self.rng, self.max_faces = solid, scale, rng, max_faces
        self.limit = (A4[0] - 2 * MARGIN - 2 * GAP, A4[1] - 2 * MARGIN - 2 * GAP)

    def _length(self, i: int, j: int) -> float:
        return float(np.linalg.norm(self.s.v[i] - self.s.v[j])) * self.scale

    def _root(self, f: int) -> dict[int, np.ndarray]:
        a, b, c = self.s.faces[f]
        ab, ac, bc = self._length(a, b), self._length(a, c), self._length(b, c)
        x = (ab ** 2 + ac ** 2 - bc ** 2) / (2 * ab)
        return {a: np.array([0.0, 0.0]), b: np.array([ab, 0.0]), c: np.array([x, math.sqrt(max(ac ** 2 - x ** 2, 0.0))])}

    def _across(self, placed: dict[int, np.ndarray], f: int, key: tuple[int, int]) -> dict[int, np.ndarray]:
        """Lay face f flat across the edge `key` it shares with an already placed face."""
        i, j = key
        k = next(v for v in self.s.faces[f] if v not in key)
        pi, pj = placed[i], placed[j]
        other = next(p for v, p in placed.items() if v not in key)
        d = np.linalg.norm(pj - pi)
        u = (pj - pi) / d
        n = np.array([-u[1], u[0]])
        if (other - pi) @ n > 0:
            n = -n                                         # put the new face on the far side
        ri, rj = self._length(i, k), self._length(j, k)
        x = (ri ** 2 - rj ** 2 + d ** 2) / (2 * d)
        y = math.sqrt(max(ri ** 2 - x ** 2, 0.0))
        return {i: pi, j: pj, k: pi + u * x + n * y}

    def nets(self):
        """Yield (face placements, joined edges) per net."""
        unplaced = set(range(len(self.s.faces)))
        while unplaced:
            root = min(unplaced)
            placement = {root: self._root(root)}
            shape = Polygon([placement[root][v] for v in self.s.faces[root]])
            joined: list[tuple[int, int, tuple[int, int]]] = []
            unplaced.discard(root)
            queue = deque((g, root, key) for g, key in self.s.neighbours(root))
            while queue and len(placement) < self.max_faces:
                f, g, key = queue.popleft()
                if f not in unplaced:
                    continue
                pos = self._across(placement[g], f, key)
                tri = Polygon([pos[v] for v in self.s.faces[f]])
                if tri.intersection(shape).area > 1e-6:
                    continue
                grown = shape.union(tri)
                w, h = self._extent(grown)
                if w > self.limit[0] or h > self.limit[1]:
                    continue
                placement[f], shape = pos, grown
                joined.append((f, g, key))
                unplaced.discard(f)
                queue.extend((h_, f, k) for h_, k in self.s.neighbours(f) if h_ in unplaced)
            yield placement, joined

    @staticmethod
    def _extent(shape) -> tuple[float, float]:
        """Width and height of the smallest rotated box, long side vertical (A4 portrait)."""
        box = shape.minimum_rotated_rectangle
        xs, ys = box.exterior.coords.xy
        sides = sorted([math.dist((xs[0], ys[0]), (xs[1], ys[1])), math.dist((xs[1], ys[1]), (xs[2], ys[2]))])
        return sides[0], sides[1]


class TemplateGenerator:
    """Builds the pages of one synthetic template and their ground truth."""

    def __init__(self, name: str, seed: int):
        self.name = name
        self.rng = random.Random(seed)
        self.style = Style.random(self.rng)
        solid = Solid(np.random.default_rng(seed), faces=self.rng.randrange(14, 44, 2))
        target_edge = self.rng.uniform(18.0, 40.0)
        self.unfolder = Unfolder(solid, target_edge / solid.mean_edge(), self.rng, max_faces=self.rng.randint(3, 10))
        self.solid = solid

    def build(self) -> list[Page]:
        nets = list(self.unfolder.nets())
        tree = {key for _, joined in nets for _, _, key in joined}
        where: dict[tuple[int, int], list[tuple[int, int]]] = {}   # mesh edge -> (net, face) holding a cut copy
        for n, (placement, _) in enumerate(nets):
            for f in placement:
                for _, key in self.solid.neighbours(f):
                    if key not in tree:
                        where.setdefault(key, []).append((n, f))
        numbers = self.rng.sample(range(1, 400), len(where))
        shapes = []
        for n, (placement, joined) in enumerate(nets):
            tris = [Polygon([placement[f][v] for v in self.solid.faces[f]]) for f in placement]
            folds = [tuple(map(tuple, (placement[f][key[0]], placement[f][key[1]]))) for f, _, key in joined]
            shapes.append({"tris": tris, "body": unary_union(tris), "folds": folds, "tabs": [], "cuts": []})
        for (key, copies), number in zip(sorted(where.items()), numbers):
            sides = []
            for n, f in copies:
                pos = nets[n][0][f]
                k = next(v for v in self.solid.faces[f] if v not in key)
                sides.append((n, f, pos[key[0]], pos[key[1]], pos[k]))
            tab_side = self._place_tab(shapes, sides)
            for idx, (n, f, a, b, inner) in enumerate(sides):
                other = sides[1 - idx]
                shapes[n]["cuts"].append(dict(a=tuple(a), b=tuple(b), inner=inner, label=str(number),
                                              tab=idx == tab_side, partner=(other[0], tuple(other[2]), tuple(other[3]))))
        return self._layout(shapes)

    def _place_tab(self, shapes, sides) -> int | None:
        order = [0, 1] if self.rng.random() < 0.5 else [1, 0]
        for idx in order:
            n, f, a, b, inner = sides[idx]
            tab = self._tab(a, b, inner)
            s = shapes[n]
            if tab.intersection(s["body"]).area > 1e-6 or any(tab.intersection(t).area > 1e-6 for t in s["tabs"]):
                continue
            s["tabs"].append(tab)
            s["folds"].append((tuple(a), tuple(b)))
            return idx
        return None

    @staticmethod
    def _tab(a, b, inner) -> Polygon:
        a, b = np.asarray(a), np.asarray(b)
        length = np.linalg.norm(b - a)
        u = (b - a) / length
        n = np.array([-u[1], u[0]])
        if (np.asarray(inner) - a) @ n > 0:
            n = -n
        h = min(6.0, 0.3 * length)
        inset = min(h, 0.3 * length)
        return Polygon([a, b, b + n * h - u * inset, a + n * h + u * inset])

    def _layout(self, shapes) -> list[Page]:
        """Rotate each net to its smallest box, then shelf-pack them onto A4 pages."""
        placed = []
        for n, s in enumerate(shapes):
            outline = unary_union([s["body"], *s["tabs"]])
            box = outline.minimum_rotated_rectangle
            xs, ys = box.exterior.coords.xy
            angle = math.degrees(math.atan2(ys[1] - ys[0], xs[1] - xs[0]))
            rotated = affinity.rotate(outline, -angle, origin=(0, 0))
            minx, miny, maxx, maxy = rotated.bounds
            if maxx - minx > maxy - miny:
                angle += 90
                rotated = affinity.rotate(outline, -angle, origin=(0, 0))
                minx, miny, maxx, maxy = rotated.bounds
            placed.append((n, angle, minx, miny, maxx - minx, maxy - miny))
        placed.sort(key=lambda p: -p[5])
        pages: list[list] = [[]]
        x, y, shelf = MARGIN, MARGIN, 0.0
        for n, angle, minx, miny, w, h in placed:
            if x + w > A4[0] - MARGIN:
                x, y, shelf = MARGIN, y + shelf + GAP, 0.0
            if y + h > A4[1] - MARGIN:
                pages.append([])
                x, y, shelf = MARGIN, MARGIN, 0.0
            pages[-1].append((n, angle, x - minx, y - miny))
            x, shelf = x + w + GAP, max(shelf, h)
        transform = {n: (page, angle, dx, dy) for page, items in enumerate(pages) for n, angle, dx, dy in items}

        def move(n, point):
            page, angle, dx, dy = transform[n]
            t = math.radians(-angle)
            px, py = point
            return (round(px * math.cos(t) - py * math.sin(t) + dx, 4), round(px * math.sin(t) + py * math.cos(t) + dy, 4))

        result = [Page(self.name, p + 1, A4[0], A4[1], [], style=self.style.__dict__) for p in range(len(pages))]
        for n, s in enumerate(shapes):
            pid = f"P{n + 1:02d}"
            outline = unary_union([s["body"], *s["tabs"]])
            piece = Piece(pid, [move(n, q) for q in list(outline.exterior.coords)[:-1]],
                          folds=[(move(n, a), move(n, b)) for a, b in s["folds"]],
                          holes=[[move(n, q) for q in list(r.coords)[:-1]] for r in outline.interiors])
            for c in s["cuts"]:
                piece.edges.append(Edge(id="", a=move(n, c["a"]), b=move(n, c["b"]), label=c["label"],
                                        matches="", tab=c["tab"]))
                piece.labels.append(self._label(move(n, c["a"]), move(n, c["b"]), move(n, tuple(c["inner"])), c["label"]))
            for i, e in enumerate(piece.edges):
                e.id = f"{pid}:E{i + 1:02d}"
            result[transform[n][0]].pieces.append(piece)
        by_label = {}
        for page in result:
            for piece in page.pieces:
                for e in piece.edges:
                    by_label.setdefault(e.label, []).append(e)
        for pair in by_label.values():
            if len(pair) == 2:
                pair[0].matches, pair[1].matches = pair[1].id, pair[0].id
        return result

    def _label(self, a, b, inner, text) -> Label:
        a, b, inner = map(np.asarray, (a, b, inner))
        length = np.linalg.norm(b - a)
        u = (b - a) / length
        n = np.array([-u[1], u[0]])
        if (inner - a) @ n < 0:
            n = -n                                         # n points into the face
        height = min(self.style.label_mm, 0.2 * length)
        centre = (a + b) / 2 + n * (0.9 * height + 0.6)
        angle = math.degrees(math.atan2(u[1], u[0]))
        if angle > 90:
            angle -= 180
        elif angle <= -90:
            angle += 180
        return Label(text, (round(float(centre[0]), 4), round(float(centre[1]), 4)), round(angle, 3), round(height, 3))


class Renderer:
    """Draws a ground-truth page as a printed template, then degrades it."""

    def __init__(self, page: Page):
        self.page = page
        self.style = Style(**{**page.style, "dash": tuple(page.style["dash"])})

    def draw(self) -> Image.Image:
        k = DRAW_DPI / 25.4
        img = Image.new("L", (round(self.page.width_mm * k), round(self.page.height_mm * k)), 255)
        d = ImageDraw.Draw(img)
        cut_w, fold_w = max(1, round(self.style.cut_mm * k)), max(1, round(self.style.fold_mm * k))
        for piece in self.page.pieces:
            for ring in [piece.outline, *piece.holes]:
                d.line([(x * k, y * k) for x, y in ring + ring[:1]], fill=0, width=cut_w, joint="curve")
            for a, b in piece.folds:
                self._dashed(d, a, b, k, fold_w)
            for label in piece.labels:
                self._text(img, label, k)
        return img

    def _dashed(self, d, a, b, k, width):
        a, b = np.asarray(a), np.asarray(b)
        length = np.linalg.norm(b - a)
        u = (b - a) / length
        pattern, t, i = self.style.dash, 0.0, 0
        # Real templates keep the dashes clear of the cut corners.
        t = 0.5 * pattern[1]
        while t < length:
            on = pattern[i % len(pattern)]
            if i % 2 == 0:
                p, q = a + u * t, a + u * min(t + on, length - 0.3)
                if np.linalg.norm(q - p) > 0:
                    d.line([tuple(p * k), tuple(q * k)], fill=0, width=width)
            t += on
            i += 1

    @staticmethod
    def _text(img, label, k):
        font = ImageFont.truetype(FONT, max(6, round(label.height * k * 1.35)))
        left, top, right, bottom = font.getbbox(label.text)
        tile = Image.new("L", (right - left + 4, bottom - top + 4), 0)
        ImageDraw.Draw(tile).text((2 - left, 2 - top), label.text, fill=255, font=font)
        tile = tile.rotate(-label.angle, expand=True, resample=Image.BICUBIC)
        cx, cy = label.center[0] * k, label.center[1] * k
        img.paste(0, (round(cx - tile.width / 2), round(cy - tile.height / 2)), tile)

    @staticmethod
    def degrade(img: Image.Image, cond: Degradation, seed: int) -> Image.Image:
        scale = cond.dpi / DRAW_DPI
        out = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
        if cond.blur_px:
            out = out.filter(ImageFilter.GaussianBlur(cond.blur_px))
        if cond.noise:
            arr = np.asarray(out, np.float32) + np.random.default_rng(seed).normal(0, cond.noise, (out.height, out.width))
            out = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
        if cond.jpeg:
            buf = io.BytesIO()
            out.save(buf, "JPEG", quality=cond.jpeg)
            out = Image.open(io.BytesIO(buf.getvalue())).convert("L")
        return out


def generate(out: Path, templates: int, seed: int) -> list[Path]:
    """Write <out>/<template>/page-NN.json|svg and <out>/<template>/<condition>/page-NN.png."""
    written = []
    for t in range(templates):
        name = f"synth-{seed:02d}-{t + 1:02d}"
        folder = out / name
        folder.mkdir(parents=True, exist_ok=True)
        for page in TemplateGenerator(name, seed * 1000 + t).build():
            stem = f"page-{page.page:02d}"
            page.to_json(folder / f"{stem}.json")
            (folder / f"{stem}.svg").write_text(page.to_svg())
            clean = Renderer(page).draw()
            for cond in CONDITIONS:
                (folder / cond.name).mkdir(exist_ok=True)
                Renderer.degrade(clean, cond, seed * 1000 + t).save(folder / cond.name / f"{stem}.png", dpi=(cond.dpi, cond.dpi))
            written.append(folder / f"{stem}.json")
    return written


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", type=Path, default=Path("bench/out"))
    parser.add_argument("--templates", type=int, default=6)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()
    pages = generate(args.out, args.templates, args.seed)
    print(f"{len(pages)} pages in {args.out}")


if __name__ == "__main__":
    main()
