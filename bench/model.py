"""Ground truth and predictions for the fabrication-aware vectorization benchmark.

Everything is in millimetres on the page, origin top left, y down. A ground-truth page
is a list of pieces; each piece has its cut outline (glue tabs included), its fold lines,
its printed edge numbers and the edges those numbers mark, with the edge each one glues to.
A prediction is a flat list of polylines, the common denominator of every vectorizer:
methods that know cut from fold set `kind`, the others leave it empty for the shared
classifier (classify.py) to fill in.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path

Point = tuple[float, float]

CUT, FOLD = "cut", "fold"


@dataclass
class Edge:
    """A printed-number edge: the segment the number marks and the edge it glues to."""
    id: str                  # "P03:E05"
    a: Point
    b: Point
    label: str
    matches: str             # id of the partner edge
    tab: bool                # this side carries the glue tab, so the segment is a fold

    @property
    def length(self) -> float:
        return ((self.b[0] - self.a[0]) ** 2 + (self.b[1] - self.a[1]) ** 2) ** 0.5


@dataclass
class Label:
    text: str
    center: Point
    angle: float             # degrees, text baseline direction
    height: float            # mm


@dataclass
class Piece:
    id: str
    outline: list[Point]                     # closed cut polygon, tabs included
    folds: list[tuple[Point, Point]] = field(default_factory=list)
    edges: list[Edge] = field(default_factory=list)
    labels: list[Label] = field(default_factory=list)
    holes: list[list[Point]] = field(default_factory=list)


@dataclass
class Page:
    """One template page with its exact vector truth."""
    template: str
    page: int
    width_mm: float
    height_mm: float
    pieces: list[Piece]
    style: dict = field(default_factory=dict)   # line widths, dash pattern, font size

    def to_json(self, path: Path) -> None:
        path.write_text(json.dumps(asdict(self), indent=1))

    @classmethod
    def from_json(cls, path: Path) -> "Page":
        raw = json.loads(path.read_text())
        pieces = []
        for p in raw.pop("pieces"):
            pieces.append(Piece(
                id=p["id"], outline=[tuple(q) for q in p["outline"]],
                folds=[(tuple(a), tuple(b)) for a, b in p["folds"]],
                edges=[Edge(**{**e, "a": tuple(e["a"]), "b": tuple(e["b"])}) for e in p["edges"]],
                labels=[Label(**{**l, "center": tuple(l["center"])}) for l in p["labels"]],
                holes=[[tuple(q) for q in h] for h in p["holes"]]))
        return cls(pieces=pieces, **raw)

    def cut_paths(self) -> list[list[Point]]:
        """Every closed cut contour, first point repeated at the end."""
        return [ring + ring[:1] for piece in self.pieces for ring in [piece.outline, *piece.holes]]

    def fold_paths(self) -> list[list[Point]]:
        return [[a, b] for piece in self.pieces for a, b in piece.folds]

    def to_svg(self) -> str:
        """Ground-truth SVG: one group per piece with cut, fold and label groups."""
        def poly(points, closed):
            d = "M " + " L ".join(f"{x:.3f} {y:.3f}" for x, y in points)
            return f'<path d="{d}{" Z" if closed else ""}"/>'
        out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width_mm}mm" height="{self.height_mm}mm" '
               f'viewBox="0 0 {self.width_mm} {self.height_mm}" fill="none" stroke="black" stroke-width="0.3">']
        for piece in self.pieces:
            out.append(f'<g id="{piece.id}">')
            out.append('<g class="cut">' + "".join(poly(r, True) for r in [piece.outline, *piece.holes]) + "</g>")
            out.append('<g class="fold" stroke-dasharray="2 1">' + "".join(poly([a, b], False) for a, b in piece.folds) + "</g>")
            out.append('<g class="labels" stroke="none" fill="black">' + "".join(
                f'<text x="{l.center[0]:.3f}" y="{l.center[1]:.3f}" font-size="{l.height:.2f}" text-anchor="middle" '
                f'dominant-baseline="central" transform="rotate({l.angle:.2f} {l.center[0]:.3f} {l.center[1]:.3f})">{l.text}</text>'
                for l in piece.labels) + "</g>")
            out.append("</g>")
        out.append("</svg>")
        return "\n".join(out)


@dataclass
class Polyline:
    """One predicted polyline in mm. `controls` counts Bezier control points before flattening."""
    points: list[Point]
    closed: bool
    kind: str | None = None
    controls: int = 0


@dataclass
class Prediction:
    method: str
    paths: list[Polyline]
    svg_bytes: int = 0
    filled: bool = True          # paths outline ink regions (True) or are centrelines (False)

    def segments(self, kind: str | None = None):
        """(a, b, kind) for every straight piece of every path, optionally one kind only."""
        for path in self.paths:
            pts = path.points + (path.points[:1] if path.closed else [])
            for a, b in zip(pts, pts[1:]):
                if kind is None or path.kind == kind:
                    yield a, b, path.kind

    def to_svg(self, width_mm: float, height_mm: float) -> str:
        out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width_mm}mm" height="{height_mm}mm" '
               f'viewBox="0 0 {width_mm} {height_mm}" fill="none" stroke="black" stroke-width="0.3">']
        for path in self.paths:
            d = "M " + " L ".join(f"{x:.3f} {y:.3f}" for x, y in path.points)
            dash = ' stroke-dasharray="2 1"' if path.kind == FOLD else ""
            out.append(f'<path d="{d}{" Z" if path.closed else ""}"{dash}/>')
        out.append("</svg>")
        return "\n".join(out)
