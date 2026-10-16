"""Stage 2b': edge numbers fixed by hand.

data/<project>/<project>-corrections.csv lists, per number, the piece, where the
number sits on its page (mm) and what it should say. The fix page (`make fix`)
writes this file; every build applies it after OCR, so a number corrected once
stays corrected. A row is matched to the label of that piece nearest its position.
"""

from __future__ import annotations

import collections
import csv
from dataclasses import dataclass
from pathlib import Path

from .model import PageLayout

MATCH_MM = 2.0
NOT_A_NUMBER = "x"     # the number check page's answer for marks that are no number (a fan of fold ends)
COLUMNS = ["piece", "x_mm", "y_mm", "read", "number"]


@dataclass
class Correction:
    piece: str
    x_mm: float
    y_mm: float
    read: str
    number: str


class Corrections:
    def __init__(self, rows: list[Correction], by_hand: bool = True):
        self.rows, self.by_hand = rows, by_hand

    @classmethod
    def load(cls, path: Path) -> "Corrections":
        if not path.is_file():
            return cls([])
        with path.open(encoding="utf-8", newline="") as handle:
            return cls([Correction(r["piece"], float(r["x_mm"]), float(r["y_mm"]), r.get("read", ""), r["number"].strip())
                        for r in csv.DictReader(handle) if r.get("number", "").strip()])

    def match(self, layouts: list[tuple[PageLayout, float]]) -> dict[int, str]:
        """id(label) -> corrected text, for the labels these corrections point at."""
        found = {}
        pieces = {piece.id: (piece, mm) for layout, mm in layouts for piece in layout.pieces}
        for row in self.rows:
            label = self._nearest(pieces, row)
            if label is not None and row.number != NOT_A_NUMBER:
                found[id(label)] = row.number
        return found

    @staticmethod
    def _nearest(pieces, row: Correction):
        piece, mm = pieces.get(row.piece, (None, 0.0))
        if piece is None or not piece.labels:
            return None
        distance = lambda l: (l.center[0] * mm - row.x_mm) ** 2 + (l.center[1] * mm - row.y_mm) ** 2
        label = min(piece.labels, key=distance)
        return label if distance(label) <= MATCH_MM ** 2 else None

    def apply(self, layouts: list[tuple[PageLayout, float]]) -> tuple[int, list[Correction]]:
        """Set each corrected label's text; returns (applied, rows that matched no label)."""
        pieces = {piece.id: (piece, mm) for layout, mm in layouts for piece in layout.pieces}
        applied, missed = 0, []
        for row in self.rows:
            label = self._nearest(pieces, row)
            if label is None:
                missed.append(row)
                continue
            if row.number == NOT_A_NUMBER:
                pieces[row.piece][0].labels.remove(label)
                applied += 1
                continue
            label.text, label.confident, label.conf = row.number, True, 100.0
            label.corrected = label.corrected or self.by_hand
            applied += 1
        if applied:
            counts = collections.Counter(l.text for layout, _ in layouts for p in layout.pieces for l in p.labels)
            for layout, _ in layouts:
                for p in layout.pieces:
                    for label in p.labels:
                        label.paired = counts[label.text] == 2
        return applied, missed


LINE_COLUMNS = ["piece", "x_mm", "y_mm", "number", "kind", "ax_mm", "ay_mm", "bx_mm", "by_mm"]


@dataclass
class LineFix:
    """The line a number marks, drawn by hand on the number check page: two points on the page (mm),
    and whether it is a cut edge or a fold (a fold means this side carries the glue tab)."""
    piece: str
    x_mm: float
    y_mm: float
    kind: str
    a: tuple[float, float]
    b: tuple[float, float]


class LineFixes:
    """data/<project>/<project>-lines.csv: hand-drawn lines that replace what tracing found for a number."""

    def __init__(self, rows: list[LineFix]):
        self.rows = rows

    @classmethod
    def load(cls, path: Path) -> "LineFixes":
        if not path.is_file():
            return cls([])
        with path.open(encoding="utf-8", newline="") as handle:
            return cls([LineFix(r["piece"], float(r["x_mm"]), float(r["y_mm"]), r["kind"],
                                (float(r["ax_mm"]), float(r["ay_mm"])), (float(r["bx_mm"]), float(r["by_mm"])))
                        for r in csv.DictReader(handle) if r.get("kind") in ("cut", "fold")])

    def apply(self, layouts: list[tuple[PageLayout, float]]) -> tuple[int, list[LineFix]]:
        """Set each matched label's line; returns (applied, rows that matched no label)."""
        pieces = {piece.id: (piece, mm) for layout, mm in layouts for piece in layout.pieces}
        applied, missed = 0, []
        for row in self.rows:
            label = Corrections._nearest(pieces, row)
            if label is None:
                missed.append(row)
                continue
            mm = pieces[row.piece][1]
            label.edge = ((row.a[0] / mm, row.a[1] / mm), (row.b[0] / mm, row.b[1] / mm))
            label.tab = row.kind == "fold"
            applied += 1
        return applied, missed
