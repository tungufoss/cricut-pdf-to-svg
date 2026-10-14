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
    fold_min_ink: float = 0.6       # share of a fold line that must be printed dashes
    fold_extend_mm: float = 6.0     # folds stretched further than this to reach the cut are flagged
    outline_tolerance_px: float = 1.5
    notch_mm: float = 6.0           # longest bump (a number touching the cut) straightened away
    notch_depth_mm: float = 2.0     # deepest such bump
    corner_mm: float = 1.2          # cut edges shorter than this between long edges are rounded corners


def _intersect(p0, p1, p2, p3):
    """Intersection of the infinite lines p0-p1 and p2-p3, or None if parallel."""
    d1, d2 = p1 - p0, p3 - p2
    denom = d1[0] * d2[1] - d1[1] * d2[0]
    if abs(denom) < 1e-9:
        return None
    t = ((p2[0] - p0[0]) * d2[1] - (p2[1] - p0[1]) * d2[0]) / denom
    return p0 + d1 * t


def _angle(u, v) -> float:
    """Unsigned angle between two direction vectors, in radians."""
    cos = float(u @ v) / max(np.linalg.norm(u) * np.linalg.norm(v), 1e-9)
    return math.acos(max(-1.0, min(1.0, cos)))


def _kernel(size: int) -> np.ndarray:
    return np.ones((max(1, size), max(1, size)), np.uint8)


class PageDetector:
    def __init__(self, settings: DetectorSettings | None = None):
        self.s = settings or DetectorSettings()

    def detect(self, page: PageImage, material: str) -> PageLayout:
        px = self.px = 1.0 / page.mm_per_px
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
            piece.folds = self._folds(dash & inside, (dash | glyph) & inside, outline, px)
            owner[region > 0] = len(pieces) + 1
            pieces.append(piece)

        layout = PageLayout(page.number, material, pieces)
        for label in self._labels(gray, text_core, glyph, px):
            x, y, w, h = label.box
            hit = owner[y + h // 2, x + w // 2] or self._nearest_piece(pieces, label.center, 2 * px)
            (pieces[hit - 1].labels if hit else layout.stray_labels).append(label)
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
            polygon = cv2.approxPolyDP(contour, self.s.outline_tolerance_px, True)[:, 0, :].astype(np.float64)
            polygons.append(self._sharpen(self._straighten(polygon)).astype(np.float32).reshape(-1, 1, 2))
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

    def _straighten(self, polygon: np.ndarray) -> np.ndarray:
        """Remove small bumps where a printed number touches a straight cut line.

        A run of vertices is dropped when the edges on either side of it are in line
        with each other, the run is short, and it strays only a little from the
        straight line that replaces it.
        """
        reach, depth, bend = self.s.notch_mm * self.px, self.s.notch_depth_mm * self.px, math.radians(8)
        changed = True
        while changed and len(polygon) > 4:
            changed = False
            n = len(polygon)
            for i in range(n):
                for span in range(2, 6):  # vertices i+1 .. i+span-1 form the bump
                    j = (i + span) % n
                    if span >= n - 1:
                        break
                    a, b = polygon[i], polygon[j]
                    chord = b - a
                    length = np.linalg.norm(chord)
                    if length == 0 or length > reach:
                        continue
                    before, after = a - polygon[(i - 1) % n], polygon[(j + 1) % n] - b
                    if min(np.linalg.norm(before), np.linalg.norm(after)) < length:
                        continue
                    if _angle(before, chord) > bend or _angle(chord, after) > bend:
                        continue
                    inner = polygon[[(i + k) % n for k in range(1, span)]]
                    normal = np.array([-chord[1], chord[0]]) / length
                    if np.abs((inner - a) @ normal).max() > depth:
                        continue
                    keep = [k for k in range(n) if (k - i) % n == 0 or (k - i) % n >= span]
                    polygon = polygon[keep]
                    changed = True
                    break
                if changed:
                    break
        return polygon

    def _sharpen(self, polygon: np.ndarray) -> np.ndarray:
        """Restore corners that tracing rounded off: a short edge between two long ones
        is replaced by the point where the long edges meet."""
        short = self.s.corner_mm * self.px
        changed = True
        while changed and len(polygon) > 3:
            changed = False
            n = len(polygon)
            for i in range(n):
                p0, p1, p2, p3 = (polygon[(i + k) % n] for k in (-1, 0, 1, 2))
                edge = np.linalg.norm(p2 - p1)
                if edge >= short or min(np.linalg.norm(p1 - p0), np.linalg.norm(p3 - p2)) < 2 * edge:
                    continue
                corner = _intersect(p0, p1, p2, p3)
                if corner is None or np.linalg.norm(corner - (p1 + p2) / 2) > 2 * short:
                    continue
                polygon = np.delete(polygon, [(i + 1) % n], axis=0)
                polygon[i if (i + 1) % n else i - 1] = corner
                changed = True
                break
        return polygon

    # -- folds ------------------------------------------------------------------

    def _folds(self, dashes: np.ndarray, support: np.ndarray, outline: list[Point], px: float) -> list[Fold]:
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
        merged = [self._refit(dashes, a, b) for a, b in merged]
        folds = [Fold(a, b, self._fold_kind(dashes, a, b, px)) for a, b in merged]
        # Numbers printed on a fold interrupt its dashes, so they count as support.
        return self._span_piece(folds, polygon, support, px)

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
    def _refit(dashes: np.ndarray, a: Point, b: Point, band: float = 3.0) -> tuple[Point, Point]:
        """Least-squares line through the dash pixels near a Hough segment (Hough is quantised)."""
        ys, xs = np.nonzero(dashes)
        points = np.column_stack([xs, ys]).astype(np.float64)
        p, q = np.asarray(a), np.asarray(b)
        length = np.linalg.norm(q - p)
        if length == 0:
            return a, b
        u = (q - p) / length
        offsets = points - p
        along, across = offsets @ u, offsets @ np.array([-u[1], u[0]])
        near = points[(np.abs(across) <= band) & (along >= -band) & (along <= length + band)]
        if len(near) < 10:
            return a, b
        vx, vy, x0, y0 = cv2.fitLine(near.astype(np.float32), cv2.DIST_HUBER, 0, 0.01, 0.01).ravel()
        d, origin = np.array([vx, vy]), np.array([x0, y0])
        if d @ u < 0:
            d = -d
        ts = (near - origin) @ d
        return tuple(origin + d * ts.min()), tuple(origin + d * ts.max())

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

    def _span_piece(self, folds: list[Fold], polygon: np.ndarray, support: np.ndarray, px: float) -> list[Fold]:
        """Stretch every fold into one straight line from cut edge to cut edge.

        Each fold is extended from its midpoint in both directions to the first cut
        edge it meets, and each end snaps to a cut corner when one is close. A stretched
        line must still be mostly dashes, which rejects Hough lines that cut across a fan
        of folds. Folds that end up on the same pair of edge points are one fold seen twice.
        """
        evidence = cv2.dilate(support, _kernel(5))
        vertices = polygon[:, 0, :].astype(float)
        reach, extend = self.s.snap_mm * px, self.s.fold_extend_mm * px
        spans: list[tuple[Fold, float]] = []
        for fold in folds:
            a, b = np.asarray(fold.a), np.asarray(fold.b)
            mid, length = (a + b) / 2, np.linalg.norm(b - a)
            if length == 0 or cv2.pointPolygonTest(polygon, (float(mid[0]), float(mid[1])), False) <= 0:
                continue
            u = (b - a) / length
            # Crossings inside the detected dashes are corners the fold merely passes near.
            hits = [t for t in self._crossings(mid, u, vertices, reach) if abs(t) >= length / 2 - reach]
            ahead, behind = [t for t in hits if t > 0], [t for t in hits if t < 0]
            if not ahead or not behind:
                continue
            start, end = mid + u * max(behind), mid + u * min(ahead)
            if self._coverage(evidence, start, end) < self.s.fold_min_ink:
                continue
            ends = []
            for point in (start, end):
                distances = np.linalg.norm(vertices - point, axis=1)
                nearest = int(np.argmin(distances))
                ends.append(vertices[nearest] if distances[nearest] <= reach else point)
            stretched = max(abs(max(behind)), min(ahead)) - length / 2
            span = Fold(tuple(ends[0]), tuple(ends[1]), fold.kind, snapped=stretched <= extend)
            if math.dist(span.a, span.b) >= self.s.fold_min_mm * px:
                spans.append((span, length))
        # Keep the best-supported copy of each fold.
        kept: list[tuple[Fold, float]] = []
        for span, support in sorted(spans, key=lambda item: -item[1]):
            same = any(
                (math.dist(span.a, k.a) <= reach and math.dist(span.b, k.b) <= reach)
                or (math.dist(span.a, k.b) <= reach and math.dist(span.b, k.a) <= reach)
                for k, _ in kept)
            if not same:
                kept.append((span, support))
        return [span for span, _ in kept]

    @staticmethod
    def _coverage(mask: np.ndarray, a, b) -> float:
        """Share of the line a-b (ends excluded) that lies on mask pixels."""
        steps = max(2, int(math.dist(a, b)))
        xs = np.linspace(a[0], b[0], steps)[1:-1].round().astype(int).clip(0, mask.shape[1] - 1)
        ys = np.linspace(a[1], b[1], steps)[1:-1].round().astype(int).clip(0, mask.shape[0] - 1)
        return float(mask[ys, xs].mean()) if len(xs) else 0.0

    @staticmethod
    def _crossings(origin: np.ndarray, u: np.ndarray, vertices: np.ndarray, corner_reach: float) -> list[float]:
        """Distances along origin + t*u at which the line crosses the outline."""
        hits = []
        for p, q in zip(vertices, np.roll(vertices, -1, axis=0)):
            edge = q - p
            denom = u[0] * edge[1] - u[1] * edge[0]
            if abs(denom) < 1e-9:
                continue
            offset = p - origin
            t = (offset[0] * edge[1] - offset[1] * edge[0]) / denom
            s = (offset[0] * u[1] - offset[1] * u[0]) / denom
            if 0 <= s <= 1:
                hits.append(float(t))
        # A fold that ends on a corner can slip between its two edges; count corners near the line.
        offsets = vertices - origin
        across = np.abs(offsets @ np.array([-u[1], u[0]]))
        hits.extend(float(t) for t in (offsets @ u)[across <= corner_reach])
        return hits

    # -- labels -----------------------------------------------------------------

    def _labels(self, gray: np.ndarray, text_core: np.ndarray, glyph: np.ndarray, px: float):
        """Group glyphs into numbers; keep each one's crop, centre, direction and size."""
        grouped = cv2.dilate(glyph, _kernel(round(px)))
        count, groups, stats, _ = cv2.connectedComponentsWithStats(grouped, connectivity=8)
        for i in range(1, count):
            x, y, w, h, _ = stats[i]
            mask = groups[y:y + h, x:x + w] == i
            ys, xs = np.nonzero(mask & text_core[y:y + h, x:x + w])
            if len(xs) < 5:
                continue
            (cx, cy), (rw, rh), angle = cv2.minAreaRect(np.column_stack([xs, ys]).astype(np.float32))
            if rw < rh:  # make the long side the reading direction
                angle, rw, rh = angle + 90, rh, rw
            ink = np.where(mask, 255 - gray[y:y + h, x:x + w], 0).clip(0, 255).astype(np.uint8)
            yield Label((int(x), int(y), int(w), int(h)), (float(cx + x), float(cy + y)), float(angle), float(rh), ink)

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
