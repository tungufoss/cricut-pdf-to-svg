"""Stage 2d: use the model's left-right symmetry to check numbers and traced lines.

Most pieces have a mirror twin, cut from the same cardstock. Twins are found by their
numbered lines: walking round one piece, the lengths of its marked lines (cut edges and
tab folds) read the same as its twin's walked the other way, with gaps where a number
found no line. An exact mirror also matches outline for outline, tabs included; a mirror
variation has the same body with its glue tabs on other edges. That pairs every numbered line with its
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
NEAR_MM = 3.0         # a line this close to its mirror line is still the same line, traced off
MIN_SHARE = 0.7       # share of lines that must agree for two pieces to count as twins
EXACT_MM = 1.0        # outlines this close (RMS, tabs included) make an exact mirror
SAMPLES = 96          # outline points compared for exact mirrors


@dataclass
class Twin:
    a: str
    b: str
    lines: list[tuple[Label, Label]]   # numbered lines of a with their mirror lines on b
    off: int                           # paired lines whose lengths disagree
    exact: bool                        # whole outline mirrors, tabs included; else tabs differ


class Symmetry:
    def __init__(self, layouts: list[tuple[PageLayout, float]]):
        self.mm, self.material, self.outline = {}, {}, {}
        self.lines: dict[str, list[Label]] = {}
        for layout, mm in layouts:
            for piece in layout.pieces:
                outline = np.array(piece.outline, float)
                marked = [l for l in piece.labels if l.edge is not None]
                marked.sort(key=lambda l: _along(outline, np.mean(l.edge, axis=0)))
                self.lines[piece.id], self.mm[piece.id] = marked, mm
                self.material[piece.id] = piece.material
                self.outline[piece.id] = outline * mm
        self.twins = self._pair()
        self.twin_of = {t.a: t.b for t in self.twins} | {t.b: t.a for t in self.twins}
        self.mirror_line = {id(x): (t.b, y) for t in self.twins for x, y in t.lines}
        self.mirror_line |= {id(y): (t.a, x) for t in self.twins for x, y in t.lines}

    def _lengths(self, piece: str) -> np.ndarray:
        return np.array([l.edge_length * self.mm[piece] for l in self.lines[piece]])

    def _align(self, a: str, b: str) -> tuple[float, list[tuple[int, int]]] | None:
        """Walk a forwards and b backwards round the outline and line up their numbered
        lines, allowing gaps where a number found no line. Returns (share of lines that
        agree, index pairs) for the best starting point."""
        la, lb = self._lengths(a), self._lengths(b)[::-1]
        if min(len(la), len(lb)) < 3:
            return None
        best = None
        for k in range(len(lb)):
            score, pairs = _sequence(la, np.roll(lb, k))
            agree = sum(abs(la[i] - np.roll(lb, k)[j]) <= LENGTH_MM for i, j in pairs)
            share = agree / max(len(la), len(lb))
            if best is None or (share, score) > best[:2]:
                best = (share, score, [(i, (len(lb) - 1 - (j - k) % len(lb))) for i, j in pairs])
        return best[0], best[2]

    def _exact(self, a: str, b: str) -> bool:
        """Do the outlines, tabs included, mirror each other?"""
        pa, pb = _resample(self.outline[a]), _resample(self.outline[b])[::-1] * [-1, 1]
        for k in range(SAMPLES):
            u, _, vt = np.linalg.svd(np.roll(pb, k, axis=0).T @ pa)
            rotation = u @ np.diag([1, np.sign(np.linalg.det(u @ vt))]) @ vt
            if np.sqrt(((np.roll(pb, k, axis=0) @ rotation - pa) ** 2).sum(1).mean()) <= EXACT_MM:
                return True
        return False

    def _pair(self) -> list[Twin]:
        ids = sorted(self.lines)
        size = {i: _perimeter(self.outline[i]) for i in ids}
        found = []
        for i, a in enumerate(ids):
            for b in ids[i + 1:]:
                # A twin is cut from the same cardstock and is about the same size.
                if self.material[a] != self.material[b] or abs(size[a] - size[b]) > 0.25 * size[a]:
                    continue
                fit = self._align(a, b)
                if fit and fit[0] >= MIN_SHARE:
                    found.append((fit[0], a, b, fit[1]))
        twins, taken = [], set()
        for share, a, b, pairs in sorted(found, key=lambda f: -f[0]):
            if a in taken or b in taken:
                continue
            taken |= {a, b}
            lines = [(self.lines[a][i], self.lines[b][j]) for i, j in pairs]
            off = sum(abs(x.edge_length * self.mm[a] - y.edge_length * self.mm[b]) > LENGTH_MM for x, y in lines)
            twins.append(Twin(a, b, lines, off, self._exact(a, b)))
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
            writer.writerow(["piece", "twin", "mirror", "number", "side", "length_mm", "twin_number", "twin_side",
                             "twin_length_mm", "length_diff_mm", "check"])
            for t in self.twins:
                for x, y in t.lines:
                    rx, ry = by_label.get(id(x)), by_label.get(id(y))
                    if not rx or not ry:
                        continue
                    diff = abs(rx["_row"].length_mm - ry["_row"].length_mm)
                    off += diff > LENGTH_MM
                    writer.writerow([t.a, t.b, "exact" if t.exact else "variation", rx["number"], rx["side"],
                                     rx["length_mm"], ry["number"], ry["side"],
                                     ry["length_mm"], f"{diff:.1f}", "traced line differs" if diff > LENGTH_MM else "ok"])
        return off


def _sequence(a: np.ndarray, b: np.ndarray) -> tuple[float, list[tuple[int, int]]]:
    """Line up two runs of line lengths in order, skipping lines on either side.
    Agreeing lengths score 2, lengths within NEAR_MM score 1 (same line, traced off)."""
    n, m = len(a), len(b)
    score = np.zeros((n + 1, m + 1))
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d = abs(a[i - 1] - b[j - 1])
            gain = 2 if d <= LENGTH_MM else 1 if d <= NEAR_MM else -np.inf
            score[i, j] = max(score[i - 1, j], score[i, j - 1], score[i - 1, j - 1] + gain)
    pairs, i, j = [], n, m
    while i and j:
        if score[i, j] == score[i - 1, j]:
            i -= 1
        elif score[i, j] == score[i, j - 1]:
            j -= 1
        else:
            pairs.append((i - 1, j - 1))
            i, j = i - 1, j - 1
    return float(score[n, m]), pairs[::-1]


def _along(outline: np.ndarray, point: np.ndarray) -> float:
    """Distance along the outline to the spot nearest `point`."""
    closed = np.vstack([outline, outline[:1]])
    best, walked, at = np.inf, 0.0, 0.0
    for p, q in zip(closed, closed[1:]):
        seg = q - p
        length = float(np.hypot(*seg))
        t = 0.0 if length == 0 else float(np.clip(np.dot(point - p, seg) / length ** 2, 0, 1))
        d = float(np.hypot(*(p + t * seg - point)))
        if d < best:
            best, at = d, walked + t * length
        walked += length
    return at


def _perimeter(outline: np.ndarray) -> float:
    return float(np.hypot(*np.diff(np.vstack([outline, outline[:1]]), axis=0).T).sum())


def _resample(outline: np.ndarray) -> np.ndarray:
    closed = np.vstack([outline, outline[:1]])
    walked = np.r_[0, np.cumsum(np.hypot(*np.diff(closed, axis=0).T))]
    t = np.linspace(0, walked[-1], SAMPLES, endpoint=False)
    points = np.c_[np.interp(t, walked, closed[:, 0]), np.interp(t, walked, closed[:, 1])]
    return points - points.mean(axis=0)
