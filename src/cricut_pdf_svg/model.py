"""Item model shared by detection, Inkscape review files and (later) nesting.

All geometry is in page pixels at the render resolution; writers convert to millimetres.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

Point = tuple[float, float]  # (x, y)


class FoldKind(str, Enum):
    # Pepakura convention used by this template: dash-dot = mountain, dashed = valley.
    MOUNTAIN = "mountain"
    VALLEY = "valley"


@dataclass
class Fold:
    a: Point
    b: Point
    kind: FoldKind
    snapped: bool = True     # both ends landed on a cut vertex or another fold's end


@dataclass
class Label:
    """A printed edge number, kept as centerline strokes for the Cricut pen."""
    box: tuple[int, int, int, int]       # x, y, w, h
    strokes: list[list[Point]]


@dataclass
class Piece:
    id: str
    material: str
    outline: list[Point]                  # closed cut polygon
    holes: list[list[Point]] = field(default_factory=list)  # closed cut polygons inside it
    folds: list[Fold] = field(default_factory=list)
    labels: list[Label] = field(default_factory=list)

    @property
    def needs_review(self) -> bool:
        return any(not fold.snapped for fold in self.folds)


@dataclass
class PageLayout:
    """Everything detected on one page. `stray` holds artwork outside every piece."""
    page: int
    material: str
    pieces: list[Piece]
    stray_labels: list[Label] = field(default_factory=list)
    stray_lines: list[list[Point]] = field(default_factory=list)
