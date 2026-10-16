"""Stage 2e: self-checks on the traced geometry that need no ground truth.

The fabrication benchmark (bench/metrics.py, F4/F5) scores a trace against a known
template. Without one, the same faults still show in the trace itself:

* junctions: a fold runs from cut to cut and meets it at a corner. A fold end that stops
  short of the cut, or meets it between two corners, marks a missing or misplaced corner,
  so the cut edges on either side read too long or too short;
* corners: the printed cut runs on straight past a traced corner, so the corner was
  clipped and the true one lies further out;
* contours: a piece traced twice (one outline inside another of the same size), or a
  tiny outline with no folds and no numbers (a number or a mark traced as a cut);
* scale: on a page whose glued pairs read systematically longer or shorter than their
  partners elsewhere, every length there is off.

Each fault is kept with where it is, so an unsolved number can be told which faults touch
its line: data/<project>/trace-faults.csv lists them all, and the edges table carries
the ones at each number's line in its `checks` column.
"""

from __future__ import annotations

import collections
import csv
from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np

from .model import PageLayout

JUNCTION_MM = 0.5      # a fold end this close to the cut meets it
CORNER_MM = 0.6        # ... and this close to an outline corner meets it at the corner
TOUCH_MM = 1.5         # a fault this close to a number's line end touches that line
TINY_MM2 = 30.0        # smaller outlines with no folds or numbers are stray marks
SCALE_MM = 0.3         # median pair difference on a page beyond this is a scale fault
SCALE_PAIRS = 5        # pairs a page needs before its scale is judged


@dataclass
class Fault:
    page: int
    piece: str          # empty for a page-wide fault
    check: str
    x_mm: float
    y_mm: float
    detail: str


class TraceChecks:
    def __init__(self, layouts: list[tuple[PageLayout, float]]):
        self.layouts = layouts
        self.faults: list[Fault] = []
        for layout, mm in layouts:
            self._junctions(layout, mm)
            self._contours(layout, mm)

    def _junctions(self, layout: PageLayout, mm: float) -> None:
        for piece in layout.pieces:
            outline = np.asarray(piece.outline, np.float32).reshape(-1, 1, 2)
            corners = outline[:, 0, :].astype(float)
            ends = [np.asarray(p, float) for f in piece.folds for p in (f.a, f.b)]
            for i, end in enumerate(ends):
                to_cut = abs(cv2.pointPolygonTest(outline, (float(end[0]), float(end[1])), True)) * mm
                to_corner = float(np.min(np.linalg.norm(corners - end, axis=1))) * mm
                # Folds that fan out from one point inside the piece meet each other, not the cut.
                to_fold = min((float(np.linalg.norm(o - end)) * mm for j, o in enumerate(ends) if j // 2 != i // 2),
                              default=np.inf)
                x, y = end * mm
                if to_cut > JUNCTION_MM and to_fold > JUNCTION_MM:
                    self.faults.append(Fault(layout.page, piece.id, "fold end off the cut", x, y,
                                             f"stops {to_cut:.1f} mm from the cut"))
                elif to_cut <= JUNCTION_MM and to_corner > CORNER_MM:
                    self.faults.append(Fault(layout.page, piece.id, "fold meets the cut between corners", x, y,
                                             f"{to_corner:.1f} mm from the nearest corner"))
            for (x, y), run in getattr(piece, "ink_past", []):
                self.faults.append(Fault(layout.page, piece.id, "cut runs past the corner", x * mm, y * mm,
                                         f"printed cut goes on {run:.1f} mm"))

    def _contours(self, layout: PageLayout, mm: float) -> None:
        polygons = [np.asarray(p.outline, np.float32).reshape(-1, 1, 2) for p in layout.pieces]
        areas = [cv2.contourArea(p) * mm * mm for p in polygons]
        for i, piece in enumerate(layout.pieces):
            centre = polygons[i][:, 0, :].mean(axis=0) * mm
            if areas[i] < TINY_MM2 and not piece.folds and not piece.labels:
                self.faults.append(Fault(layout.page, piece.id, "extra contour", *centre,
                                         f"{areas[i]:.0f} mm² with no folds or numbers"))
            for j, other in enumerate(layout.pieces):
                probe = tuple(float(v) for v in polygons[i][:, 0, :].mean(axis=0))
                if j != i and 0.8 <= areas[i] / max(areas[j], 1e-9) <= 1.25 and areas[i] <= areas[j] \
                        and cv2.pointPolygonTest(polygons[j], probe, False) > 0:
                    self.faults.append(Fault(layout.page, piece.id, "duplicate contour", *centre,
                                             f"inside {other.id} of about the same size"))

    def scale(self, records: list[dict]) -> None:
        """Pages whose numbered lines read systematically longer or shorter than their partners."""
        diffs = collections.defaultdict(list)
        for r in records:
            if r["partner_piece"] and r["side"] in ("edge", "tab") and r["partner_side"] in ("edge", "tab") \
                    and r["partner_piece"][6:8] != r["piece"][6:8]:
                diff = float(r["length_mm"]) - float(r["partner_length_mm"])
                if abs(diff) <= 3.0:
                    diffs[int(r["piece"][6:8])].append(diff)
        for page, values in sorted(diffs.items()):
            bias = float(np.median(values))
            if len(values) >= SCALE_PAIRS and abs(bias) > SCALE_MM:
                self.faults.append(Fault(page, "", "scale", 0.0, 0.0,
                                         f"lines read {bias:+.1f} mm against their partners ({len(values)} pairs)"))

    def at(self, record: dict) -> list[str]:
        """Faults that touch this number's line: at either end of it, on its piece, or on its page."""
        found = []
        line = [float(v) for v in record.get("line_mm", "").split()]
        ends = [np.array(line[:2]), np.array(line[2:])] if len(line) == 4 else []
        page = int(record["piece"][6:8])
        for f in self.faults:
            if f.piece == "" and f.page == page:
                found.append(f"{f.check}: {f.detail}")
            elif f.piece == record["piece"]:
                if f.check in ("extra contour", "duplicate contour"):
                    found.append(f"{f.check}: {f.detail}")
                elif any(np.linalg.norm(e - (f.x_mm, f.y_mm)) <= TOUCH_MM for e in ends):
                    found.append(f"{f.check} at this line's end: {f.detail}")
        return list(dict.fromkeys(found))

    def write(self, path: Path) -> collections.Counter:
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["page", "piece", "check", "x_mm", "y_mm", "detail"])
            for f in self.faults:
                writer.writerow([f.page, f.piece, f.check, f"{f.x_mm:.1f}", f"{f.y_mm:.1f}", f.detail])
        return collections.Counter(f.check for f in self.faults)
