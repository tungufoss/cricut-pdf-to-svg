"""Item model shared by detection, Inkscape review files and (later) nesting.

All geometry is in page pixels at the render resolution; writers convert to millimetres.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

import numpy as np

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
    """A printed edge number: where it sits, which way it reads, and what it says."""
    box: tuple[int, int, int, int]       # x, y, w, h
    center: Point
    angle: float                          # degrees clockwise that turn upright text into place
    height: float                         # digit height in px
    ink: np.ndarray = field(repr=False)   # white-on-black crop used for reading
    text: str = ""
    confident: bool = False              # both readers agreed, or Tesseract was sure
    paired: bool = False                 # the same number is printed exactly twice
    edge: tuple[Point, Point] | None = None  # the cut edge or tab fold this number marks
    tab: bool = False                    # edge is a glue-tab fold, so this side carries the tab

    @property
    def edge_length(self) -> float:
        """Length in px of the marked line; 0 when no line was found."""
        if self.edge is None:
            return 0.0
        (ax, ay), (bx, by) = self.edge
        return float(np.hypot(bx - ax, by - ay))

    @property
    def trusted(self) -> bool:
        return self.confident and self.paired


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
        return any(not fold.snapped for fold in self.folds) or any(not l.trusted for l in self.labels)


@dataclass
class PageLayout:
    """Everything detected on one page. `stray` holds artwork outside every piece."""
    page: int
    material: str
    pieces: list[Piece]
    stray_labels: list[Label] = field(default_factory=list)   # credits and instructions
    stray_lines: list[list[Point]] = field(default_factory=list)
    footer: np.ndarray | None = field(default=None, repr=False)  # right-margin strip: credit and paper note
    paper: str = ""                      # cardstock named in the footer, e.g. "beige"
