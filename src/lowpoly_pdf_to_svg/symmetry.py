"""Stage 2d: use the model's left-right symmetry to check numbers and traced lines.

Most pieces have a mirror twin, cut from the same cardstock. Twins are found by their numbered lines: walking
round one piece, the lengths of its marked lines (cut edges and tab folds) read the
same as its twin's walked the other way. That pairs every numbered line with its
mirror line, which gives two checks:

* a line and its mirror line should be the same length; when not, one was traced off;
* glue pairs mirror too. If line a on piece A glues to piece C, then a's mirror line on
  A's twin glues to C's twin, at the mirror of C's line. So the number on that line
  is predicted from the clean pair on the other side.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from .model import Label, PageLayout

LENGTH_MM = 1.0       # mirror lines agree within this
MAX_OFF = 0.2         # share of lines allowed to disagree for two pieces to count as twins


@dataclass
class Twin:
    a: str
    b: str
    lines: list[tuple[Label, Label]]   # each numbered line of a with its mirror line on b
    off: int                           # lines whose lengths disagree


class Symmetry:
    def __init__(self, layouts: list[tuple[PageLayout, float]]):
        self.mm, self.material = {}, {}
        self.lines: dict[str, list[Label]] = {}
        for layout, mm in layouts:
            for piece in layout.pieces:
                centre = np.array(piece.outline, float).mean(axis=0)
                marked = [l for l in piece.labels if l.edge is not None]
                marked.sort(key=lambda l: np.arctan2(l.center[1] - centre[1], l.center[0] - centre[0]))
                self.lines[piece.id], self.mm[piece.id] = marked, mm
                self.material[piece.id] = piece.material
        self.twins = self._pair()
        self.twin_of = {t.a: t.b for t in self.twins} | {t.b: t.a for t in self.twins}
        self.mirror_line = {id(x): (t.b, y) for t in self.twins for x, y in t.lines}
        self.mirror_line |= {id(y): (t.a, x) for t in self.twins for x, y in t.lines}

    def _lengths(self, piece: str) -> np.ndarray:
        return np.array([l.edge_length * self.mm[piece] for l in self.lines[piece]])

    def _align(self, a: str, b: str) -> tuple[int, float, int] | None:
        """Best turn of b walked backwards against a: (lines off, mean difference, shift)."""
        la, lb = self._lengths(a), self._lengths(b)[::-1]
        if len(la) != len(lb) or len(la) < 3:
            return None
        return min((int((np.abs(la - np.roll(lb, k)) > LENGTH_MM).sum()), float(np.abs(la - np.roll(lb, k)).mean()), k)
                   for k in range(len(lb)))

    def _pair(self) -> list[Twin]:
        ids = sorted(self.lines)
        found = []
        for i, a in enumerate(ids):
            for b in ids[i + 1:]:
                if self.material[a] != self.material[b]:  # a twin is cut from the same cardstock
                    continue
                fit = self._align(a, b)
                if fit and fit[0] <= max(1, int(MAX_OFF * len(self.lines[a]))):
                    found.append((fit[0] / len(self.lines[a]), fit[1], a, b, fit))
        twins, taken = [], set()
        for _, _, a, b, (off, _, shift) in sorted(found):
            if a in taken or b in taken:
                continue
            taken |= {a, b}
            backwards = self.lines[b][::-1]
            turned = backwards[-shift:] + backwards[:-shift] if shift else backwards
            twins.append(Twin(a, b, list(zip(self.lines[a], turned)), off))
        return twins

    def predictions(self, records: list[dict]) -> list[dict]:
        """Numbers that do not pair up, with the number their twin's clean pair predicts."""
        by_label = {id(r["_row"].label): r for r in records}
        by_number: dict[str, list[dict]] = {}
        for r in records:
            by_number.setdefault(r["number"], []).append(r)
        found = []
        for r in records:
            if r["status"] == "ok" or id(r["_row"].label) not in self.mirror_line:
                continue
            twin, mirror = self.mirror_line[id(r["_row"].label)]
            source = by_label.get(id(mirror))
            # The twin's line must be cleanly paired with a piece that has its own twin.
            if not source or source["status"] != "ok" or source["partner_piece"] not in self.twin_of:
                continue
            partner = next((o for o in by_number[source["number"]] if o is not source and o["piece"] == source["partner_piece"]), None)
            if not partner or id(partner["_row"].label) not in self.mirror_line:
                continue
            target_piece, target = self.mirror_line[id(partner["_row"].label)]
            if target_piece == source["piece"] or target is r["_row"].label:
                continue
            expected = by_label.get(id(target))
            if not expected or expected["number"] == r["number"]:
                continue
            # Sure when the predicted number is the only other copy of what the target line says,
            # sits on the other side, and its line has this line's length.
            number = expected["number"]
            copies = by_number.get(number, [])
            sure = (len(copies) == 1 and copies[0] is expected and expected["side"] in ("edge", "tab")
                    and r["side"] in ("edge", "tab") and expected["side"] != r["side"]
                    and abs(r["_row"].length_mm - expected["_row"].length_mm) <= LENGTH_MM)
            found.append({"piece": r["piece"], "x_mm": r["x_mm"], "y_mm": r["y_mm"], "side": r["side"],
                          "length_mm": r["length_mm"], "read": r["number"], "ocr_conf": r["ocr_conf"],
                          "suggested": number, "partner_piece": expected["piece"], "partner_x_mm": expected["x_mm"],
                          "partner_y_mm": expected["y_mm"], "partner_side": expected["side"],
                          "partner_length_mm": expected["length_mm"],
                          "length_diff_mm": f"{abs(r['_row'].length_mm - expected['_row'].length_mm):.1f}",
                          "why": f"mirror: twin {twin} pairs {source['number']} with {source['partner_piece']}",
                          "sure": "yes" if sure else "no"})
        return found

    def write(self, path: Path, records: list[dict]) -> int:
        """Every numbered line beside its mirror line; returns how many disagree in length."""
        by_label = {id(r["_row"].label): r for r in records}
        off = 0
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["piece", "number", "side", "length_mm", "twin", "twin_number", "twin_side",
                             "twin_length_mm", "length_diff_mm", "check"])
            for t in self.twins:
                for x, y in t.lines:
                    rx, ry = by_label.get(id(x)), by_label.get(id(y))
                    if not rx or not ry:
                        continue
                    diff = abs(rx["_row"].length_mm - ry["_row"].length_mm)
                    off += diff > LENGTH_MM
                    writer.writerow([t.a, rx["number"], rx["side"], rx["length_mm"], t.b, ry["number"], ry["side"],
                                     ry["length_mm"], f"{diff:.1f}", "traced line differs" if diff > LENGTH_MM else "ok"])
        return off
