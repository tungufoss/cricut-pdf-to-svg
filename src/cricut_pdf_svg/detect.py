"""Stage 2: find pieces, folds and edge numbers on a rendered pattern page.

The template prints three kinds of ink, which this detector separates:

* solid grey cut lines, long connected strokes that enclose each piece;
* dashed (valley) and dash-dot (mountain) grey fold lines, many short strokes;
* black edge numbers, the darkest pixels on the page.

Piece interiors are the background areas fully enclosed by cut lines. Anything that
is not inside a piece (credits, instructions, an outline with a gap) is kept as
stray artwork so it shows up on the Review layer instead of silently disappearing.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import cv2
import numpy as np

from .model import Fold, FoldKind, Label, PageLayout, Piece, Point
from .render import PageImage
from .skeleton import paths_from_skeleton, simplify, thin


@dataclass
class DetectorSettings:
    ink_threshold: int = 235        # grey level below which a pixel is printed line art
    text_threshold: int = 110       # edge numbers are printed black, cut/fold lines grey
    solid_min_mm: float = 4.3       # strokes longer than this are cut lines, shorter are dashes
    gap_close_mm: float = 0.7       # bridge small breaks in cut lines
    min_piece_mm2: float = 30.0
    fold_min_mm: float = 2.8
    fold_gap_mm: float = 2.0        # longest gap between two dashes of the same fold
    fold_join_mm: float = 8.0       # longest gap joining collinear fold pieces (a number printed on a fold)
    snap_mm: float = 1.5            # fold ends closer than this to a cut vertex/edge snap to it
    fold_extend_mm: float = 4.0     # a fold may be lengthened or trimmed this much to meet the cut line
    outline_tolerance_px: float = 1.5


def _kernel(size: int) -> np.ndarray:
    return np.ones((max(1, size), max(1, size)), np.uint8)


class PageDetector:
    def __init__(self, settings: DetectorSettings | None = None):
        self.s = settings or DetectorSettings()

    def detect(self, page: PageImage, material: str) -> PageLayout:
        px = 1.0 / page.mm_per_px
        rgb = page.rgb.astype(np.int32)
        r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
        gray = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.int32)
        # Red instructions ("Print on red paper") are not part of any piece.
        red = (r > g * 1.3) & (r > b * 1.2) & (r > 100)
        ink = ((gray < self.s.ink_threshold) & ~red).astype(np.uint8)
        text_core = (gray < self.s.text_threshold) & ~red

        count, labels, stats, _ = cv2.connectedComponentsWithStats(ink, connectivity=8)
        darkest = np.full(count, 255, np.int32)
        np.minimum.at(darkest, labels.ravel(), gray.ravel())
        extent = np.maximum(stats[:, cv2.CC_STAT_WIDTH], stats[:, cv2.CC_STAT_HEIGHT])
        is_long = extent > self.s.solid_min_mm * px
        is_long[0] = False
        is_glyph = ~is_long & (darkest < self.s.text_threshold)
        is_glyph[0] = False

        solid = is_long[labels].astype(np.uint8)
        glyph = (is_glyph[labels] | text_core).astype(np.uint8)
        dash = (ink.astype(bool) & ~is_long[labels] & ~glyph.astype(bool)).astype(np.uint8)

        regions = self._piece_regions(solid, glyph, px)
        outlines, holes = self._outlines(regions)
        pieces: list[Piece] = []
        owner = np.zeros(gray.shape, np.int32)  # 1-based piece index per pixel
        for index, (region, outline) in enumerate(zip(regions, outlines)):
            if outline is None:
                continue
            piece = Piece(f"piece-{page.number:02d}-{len(pieces) + 1:02d}", material, outline)
            piece.holes = holes[index]
            inside = cv2.erode(region, _kernel(5))
            piece.folds = self._folds(dash & inside, outline, px)
            owner[region > 0] = len(pieces) + 1
            pieces.append(piece)

        layout = PageLayout(page.number, material, pieces)
        for box, strokes in self._labels(gray, red, glyph, px):
            x, y, w, h = box
            hit = owner[y + h // 2, x + w // 2] or self._nearest_piece(pieces, (x + w / 2, y + h / 2), 2 * px)
            target = pieces[hit - 1].labels if hit else layout.stray_labels
            target.append(Label(box, strokes))
        covered = cv2.dilate((owner > 0).astype(np.uint8), _kernel(7))
        stray = ((solid | dash) & (covered == 0)).astype(bool)
        layout.stray_lines = self._centerlines(stray, min_length=int(px))
        return layout

    @staticmethod
    def _nearest_piece(pieces: list[Piece], point: Point, reach: float) -> int:
        """1-based index of a piece whose cut line passes within `reach` of point, else 0."""
        for index, piece in enumerate(pieces, start=1):
            polygon = np.asarray(piece.outline, np.float32).reshape(-1, 1, 2)
            if cv2.pointPolygonTest(polygon, point, True) >= -reach:
                return index
        return 0

    # -- pieces -----------------------------------------------------------------

    def _piece_regions(self, solid: np.ndarray, glyph: np.ndarray, px: float) -> list[np.ndarray]:
        closed = cv2.morphologyEx(solid, cv2.MORPH_CLOSE, _kernel(round(self.s.gap_close_mm * px)))
        height, width = closed.shape
        count, background, stats, _ = cv2.connectedComponentsWithStats(1 - closed, connectivity=4)
        # Numbers printed against a cut line would otherwise leave a notch in the piece.
        fill_in = cv2.dilate(glyph, _kernel(3))
        regions = []
        for i in range(1, count):
            x, y, w, h, area = stats[i]
            touches_border = x == 0 or y == 0 or x + w == width or y + h == height
            if touches_border or area < self.s.min_piece_mm2 * px * px:
                continue
            inner = (background == i).astype(np.uint8)
            inner |= fill_in & cv2.dilate(inner, _kernel(9))
            inner = cv2.morphologyEx(inner, cv2.MORPH_CLOSE, _kernel(5))
            # Grow from the inner edge of the cut line to its centre.
            regions.append(cv2.dilate(inner, _kernel(5)))
        return regions

    def _outlines(self, regions: list[np.ndarray]):
        """Outer cut polygon per region; regions enclosed by another piece become its holes."""
        polygons = []
        for region in regions:
            contours, _ = cv2.findContours(cv2.erode(region, _kernel(3)), cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)
            contour = max(contours, key=cv2.contourArea)
            polygons.append(cv2.approxPolyDP(contour, self.s.outline_tolerance_px, True))
        outlines: list[list[Point] | None] = []
        holes: list[list[list[Point]]] = [[] for _ in regions]
        for i, polygon in enumerate(polygons):
            probe = tuple(float(v) for v in polygon[0][0])
            parent = next((j for j, other in enumerate(polygons)
                           if j != i and cv2.contourArea(other) > cv2.contourArea(polygon)
                           and cv2.pointPolygonTest(other, probe, False) > 0), None)
            points = [(float(x), float(y)) for x, y in polygon[:, 0, :]]
            if parent is None:
                outlines.append(points)
            else:
                holes[parent].append(points)
                outlines.append(None)
        return outlines, holes

    # -- folds ------------------------------------------------------------------

    def _folds(self, dashes: np.ndarray, outline: list[Point], px: float) -> list[Fold]:
        found = cv2.HoughLinesP(dashes * 255, 1, np.pi / 720, 12,
                                minLineLength=self.s.fold_min_mm * px,
                                maxLineGap=self.s.fold_gap_mm * px)
        segments = [] if found is None else found.reshape(-1, 4).astype(float).tolist()
        merged = self._merge_collinear(segments, gap=self.s.fold_join_mm * px)
        while True:  # merging can make two longer pieces collinear neighbours
            again = self._merge_collinear([[*a, *b] for a, b in merged], gap=self.s.fold_join_mm * px)
            if len(again) == len(merged):
                break
            merged = again
        polygon = np.asarray(outline, np.float32).reshape(-1, 1, 2)
        # Antialiased cut lines next to numbers can look like dashes; a real fold never runs along the cut.
        merged = [(a, b) for a, b in merged if not self._along_outline(polygon, a, b, 2.5)]
        folds = [Fold(a, b, self._fold_kind(dashes, a, b, px)) for a, b in merged]
        self._snap(folds, polygon, self.s.snap_mm * px, self.s.fold_extend_mm * px)
        return folds

    @staticmethod
    def _merge_collinear(segments, gap: float, tolerance: float = 3.0):
        segments = sorted(segments, key=lambda s: -math.hypot(s[2] - s[0], s[3] - s[1]))
        merged: list[list[np.ndarray]] = []
        for x1, y1, x2, y2 in segments:
            p, q = np.array([x1, y1]), np.array([x2, y2])
            for line in merged:
                a, b = line
                length = np.linalg.norm(b - a)
                u = (b - a) / length
                normal = np.array([-u[1], u[0]])
                if abs((p - a) @ normal) > tolerance or abs((q - a) @ normal) > tolerance:
                    continue
                lo, hi = sorted(((p - a) @ u, (q - a) @ u))
                if lo < length + gap and hi > -gap:
                    line[0], line[1] = a + u * min(0.0, lo), a + u * max(length, hi)
                    break
            else:
                merged.append([p, q])
        return [(tuple(a), tuple(b)) for a, b in merged]

    @staticmethod
    def _along_outline(polygon: np.ndarray, a: Point, b: Point, distance: float) -> bool:
        samples = np.linspace(a, b, 9)[1:-1]
        near = [abs(cv2.pointPolygonTest(polygon, (float(x), float(y)), True)) <= distance for x, y in samples]
        return sum(near) > len(near) / 2

    @staticmethod
    def _fold_kind(dashes: np.ndarray, a: Point, b: Point, px: float) -> FoldKind:
        """Dash-dot lines contain short 'dot' runs between the dashes."""
        tolerant = cv2.dilate(dashes, _kernel(3))
        length = math.dist(a, b)
        steps = max(2, int(length * 2))
        xs = np.linspace(a[0], b[0], steps).round().astype(int).clip(0, dashes.shape[1] - 1)
        ys = np.linspace(a[1], b[1], steps).round().astype(int).clip(0, dashes.shape[0] - 1)
        samples = tolerant[ys, xs].astype(np.int8)
        edges = np.flatnonzero(np.diff(np.concatenate(([0], samples, [0]))))
        runs = (edges[1::2] - edges[::2]) / 2.0          # run lengths in pixels
        interior = runs[1:-1] if len(runs) > 2 else runs  # end runs are often clipped
        # At 180 dpi a valley dash measures ~11 px; a mountain dash-dot alternates
        # ~19 px dashes with ~7 px runs where the dot merges with its neighbour.
        long = int((interior >= 15 * px / 7.09).sum())
        return FoldKind.MOUNTAIN if long >= max(1, 0.25 * len(interior)) else FoldKind.VALLEY

    @staticmethod
    def _snap(folds: list[Fold], polygon: np.ndarray, reach: float, extend: float) -> None:
        vertices = polygon[:, 0, :].astype(float)
        ends = [(fold, which) for fold in folds for which in ("a", "b")]
        settled: dict[tuple[int, str], bool] = {}
        for fold, which in ends:
            point = np.asarray(getattr(fold, which))
            other = np.asarray(fold.b if which == "a" else fold.a)
            corner = PageDetector._vertex_on_line(other, point, vertices, reach, extend)
            if corner is not None:
                setattr(fold, which, tuple(corner))
                settled[(id(fold), which)] = True
                continue
            hit = PageDetector._ray_to_outline(other, point, vertices, extend)
            if hit is not None:
                point = hit
            distances = np.linalg.norm(vertices - point, axis=1)
            nearest = int(np.argmin(distances))
            if distances[nearest] <= reach:
                setattr(fold, which, tuple(vertices[nearest]))
                settled[(id(fold), which)] = True
            elif abs(cv2.pointPolygonTest(polygon, (float(point[0]), float(point[1])), True)) <= reach:
                setattr(fold, which, tuple(point))
                settled[(id(fold), which)] = True
        # Interior vertices: several fold ends meeting inside the piece.
        loose = [(f, w) for f, w in ends if not settled.get((id(f), w))]
        for fold, which in loose:
            point = np.asarray(getattr(fold, which))
            partners = [(f, w) for f, w in ends if f is not fold
                        and math.dist(getattr(f, w), point) <= reach * 2]
            if len(partners) >= 2:
                group = [(fold, which)] + partners
                centre = tuple(np.mean([getattr(f, w) for f, w in group], axis=0))
                for f, w in group:
                    setattr(f, w, centre)
                    settled[(id(f), w)] = True
        for fold in folds:
            fold.snapped = settled.get((id(fold), "a"), False) and settled.get((id(fold), "b"), False)

    @staticmethod
    def _vertex_on_line(start: np.ndarray, end: np.ndarray, vertices: np.ndarray, reach: float, extend: float):
        """The cut vertex the fold start->end points at, if one lies near its end."""
        length = np.linalg.norm(end - start)
        if length == 0:
            return None
        u = (end - start) / length
        offsets = vertices - start
        along = offsets @ u
        across = np.abs(offsets @ np.array([-u[1], u[0]]))
        candidates = np.flatnonzero((across <= reach) & (np.abs(along - length) <= extend))
        if not len(candidates):
            return None
        return vertices[candidates[np.argmin(np.abs(along[candidates] - length))]]

    @staticmethod
    def _ray_to_outline(start: np.ndarray, end: np.ndarray, vertices: np.ndarray, extend: float):
        """Where the line start->end crosses the outline nearest to `end`, within `extend` px."""
        direction = end - start
        length = np.linalg.norm(direction)
        if length == 0:
            return None
        u = direction / length
        best = None
        for p, q in zip(vertices, np.roll(vertices, -1, axis=0)):
            edge = q - p
            denom = u[0] * edge[1] - u[1] * edge[0]
            if abs(denom) < 1e-9:
                continue
            offset = p - start
            t = (offset[0] * edge[1] - offset[1] * edge[0]) / denom   # along the fold
            s = (offset[0] * u[1] - offset[1] * u[0]) / denom          # along the edge
            if 0 <= s <= 1 and abs(t - length) <= extend and (best is None or abs(t - length) < abs(best - length)):
                best = t
        return None if best is None else start + u * best

    # -- labels -----------------------------------------------------------------

    def _labels(self, gray: np.ndarray, red: np.ndarray, glyph: np.ndarray, px: float):
        """Group glyphs into numbers and trace each one's centerline for the pen."""
        grouped = cv2.dilate(glyph, _kernel(round(px)))
        count, groups, stats, _ = cv2.connectedComponentsWithStats(grouped, connectivity=8)
        strokes_mask = (gray < 150) & ~red
        for i in range(1, count):
            x, y, w, h, _ = stats[i]
            mask = (groups[y:y + h, x:x + w] == i) & strokes_mask[y:y + h, x:x + w] & (glyph[y:y + h, x:x + w] > 0)
            strokes = self._centerlines(mask, min_length=2, offset=(x, y))
            if strokes:
                yield (int(x), int(y), int(w), int(h)), strokes

    @staticmethod
    def _centerlines(mask: np.ndarray, min_length: int, offset: tuple[int, int] = (0, 0)) -> list[list[Point]]:
        if not mask.any():
            return []
        ox, oy = offset
        lines = []
        for chain, _ in paths_from_skeleton(thin(mask), min_length=min_length):
            points = simplify(chain, tolerance=0.6)
            if len(points) >= 2:
                lines.append([(float(x + ox), float(y + oy)) for y, x in points])
        return lines
