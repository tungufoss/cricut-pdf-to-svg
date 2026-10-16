"""Stage 2c: list every edge number with the line it marks, paired with its partner.

Each number is printed twice: once on the piece edge that is glued (no tab) and
once on the fold of the glue tab it is glued to. Both marked lines should be the
same length, so a length mismatch or two tabs/no tabs points at a misread number
or a mis-traced line.
"""

from __future__ import annotations

import collections
import csv
from dataclasses import dataclass
from pathlib import Path

from .model import Label, PageLayout

LENGTH_TOLERANCE_MM = 1.0
SURE_MM = 0.3         # a suggested fix this close in length, and otherwise clear-cut, is applied without asking
SURE_CONF = 80.0      # Tesseract confidence below which a read counts as shaky


@dataclass
class EdgeRow:
    piece: str
    label: Label
    mm_per_px: float

    @property
    def length_mm(self) -> float:
        return self.label.edge_length * self.mm_per_px

    @property
    def side(self) -> str:
        if self.label.edge is None:
            return "none"
        return "tab" if self.label.tab else "edge"


class EdgeTable:
    COLUMNS = ["number", "piece", "side", "length_mm", "x_mm", "y_mm", "ocr_trusted", "ocr_conf", "ocr_alternatives", "corrected",
               "partner_piece", "partner_side", "partner_length_mm", "length_diff_mm", "status", "line_mm", "checks"]

    def __init__(self):
        self.rows: list[EdgeRow] = []
        self.layouts: list[PageLayout] = []
        self.checks = None  # TraceChecks: faults in the trace that touch each unsolved number's line

    def add(self, layout: PageLayout, mm_per_px: float) -> None:
        self.layouts.append(layout)
        self.rows.extend(EdgeRow(piece.id, label, mm_per_px) for piece in layout.pieces for label in piece.labels)

    def records(self) -> list[dict]:
        by_number = collections.defaultdict(list)
        for row in self.rows:
            by_number[row.label.text].append(row)
        partners = self._partners(by_number)
        records = []
        for row in self.rows:
            others = [o for o in by_number[row.label.text] if o is not row]
            partner = others[0] if len(others) == 1 else partners.get(id(row))
            records.append({
                "_row": row,
                "number": row.label.text,
                "piece": row.piece,
                "side": row.side,
                "length_mm": f"{row.length_mm:.1f}",
                "x_mm": f"{row.label.center[0] * row.mm_per_px:.1f}",
                "y_mm": f"{row.label.center[1] * row.mm_per_px:.1f}",
                "ocr_trusted": "yes" if row.label.trusted else "no",
                "ocr_conf": f"{row.label.conf:.0f}",
                "ocr_alternatives": " ".join(row.label.alternatives),
                "corrected": "yes" if row.label.corrected else "",
                "partner_piece": partner.piece if partner else "",
                "partner_side": partner.side if partner else "",
                "partner_length_mm": f"{partner.length_mm:.1f}" if partner else "",
                "length_diff_mm": f"{abs(row.length_mm - partner.length_mm):.1f}" if partner else "",
                "line_mm": " ".join(f"{v * row.mm_per_px:.1f}" for p in row.label.edge for v in p) if row.label.edge else "",
                "status": ("extra copy: likely misread" if len(others) > 1 and partner is None and
                           any(id(o) in partners for o in others) else self._status(row, partner, len(others))),
            })
        if self.checks is not None:
            for r in records:
                r["checks"] = "; ".join(self.checks.at(r)) if r["status"] != "ok" else ""
        return sorted(records, key=lambda r: (int(r["number"]) if r["number"].isdigit() else 10**6, r["piece"]))

    @staticmethod
    def _partners(by_number: dict[str, list[EdgeRow]]) -> dict[int, EdgeRow]:
        """For a number read more than twice, the plain edge and tab whose lengths agree
        best are the real pair; the other copies are misreads of some other number."""
        partners: dict[int, EdgeRow] = {}
        for rows in by_number.values():
            if len(rows) < 3:
                continue
            pairs = [(abs(a.length_mm - b.length_mm), a, b) for a in rows for b in rows
                     if a.side == "edge" and b.side == "tab"]
            if pairs:
                diff, a, b = min(pairs, key=lambda p: p[0])
                if diff <= LENGTH_TOLERANCE_MM:
                    partners[id(a)], partners[id(b)] = b, a
        return partners

    @staticmethod
    def _status(row: EdgeRow, partner: EdgeRow | None, others: int) -> str:
        if partner is None:
            return "unpaired" if others == 0 else f"printed {others + 1} times"
        if "none" in (row.side, partner.side):
            return "line not found"
        if row.side == partner.side:
            return "both tabs" if row.label.tab else "no tab"
        if abs(row.length_mm - partner.length_mm) > LENGTH_TOLERANCE_MM:
            return "length mismatch"
        return "ok"

    def write(self, path: Path) -> collections.Counter:
        records = self.records()
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, self.COLUMNS, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(records)
        return collections.Counter(r["status"] for r in records)

    def misreads(self, records: list[dict] | None = None) -> list[dict]:
        """Numbers that did not pair up, matched to an unpaired line of the same length on
        the other side (edge against tab) whose number is a likely misreading of it."""
        records = records if records is not None else self.records()
        clean = {r["number"] for r in records if r["status"] == "ok"}
        open_rows = [r for r in records if r["status"] != "ok" and r["side"] in ("edge", "tab")]
        found, used = [], set()
        pairs = []
        for i, a in enumerate(open_rows):
            for b in open_rows[i + 1:]:
                if a["side"] == b["side"] or a["number"] == b["number"]:
                    continue
                diff = abs(a["_row"].length_mm - b["_row"].length_mm)
                if diff > LENGTH_TOLERANCE_MM:
                    continue
                evidence = _similar(a, b)
                if evidence:
                    pairs.append((evidence[0], diff, a, b, evidence[1]))
        options = collections.Counter(id(r) for _, _, a, b, _ in pairs for r in (a, b))
        for rank, diff, a, b, why in sorted(pairs, key=lambda p: (p[0], p[1])):
            if id(a) in used or id(b) in used:
                continue
            used.update((id(a), id(b)))
            # Fix the copy whose number already has a clean pair elsewhere, else the less certain read.
            if (a["number"] in clean) != (b["number"] in clean):
                wrong, right = (a, b) if a["number"] in clean else (b, a)
            else:
                wrong, right = (a, b) if a["_row"].label.conf <= b["_row"].label.conf else (b, a)
            found.append({"piece": wrong["piece"], "x_mm": wrong["x_mm"], "y_mm": wrong["y_mm"],
                          "side": wrong["side"], "length_mm": wrong["length_mm"],
                          "read": wrong["number"], "ocr_conf": wrong["ocr_conf"], "suggested": right["number"],
                          "partner_piece": right["piece"], "partner_x_mm": right["x_mm"],
                          "partner_y_mm": right["y_mm"], "partner_side": right["side"],
                          "partner_length_mm": right["length_mm"], "length_diff_mm": f"{diff:.1f}",
                          "why": why + ("; the read number already pairs elsewhere" if wrong["number"] in clean else ""),
                          "sure": "yes" if self._sure(rank, diff, options[id(a)], options[id(b)], wrong, right, clean) else "no"})
        return sorted(found, key=lambda f: (float(f["length_diff_mm"]), f["piece"]))

    @staticmethod
    def _sure(rank: int, diff: float, options_a: int, options_b: int, wrong: dict, right: dict, clean: set) -> bool:
        """Clear-cut enough to apply without asking: OCR itself offered the suggested number,
        the lines agree within SURE_MM, neither copy has another candidate, and either the read
        number already pairs elsewhere or the copy to fix was read with low confidence, and the
        suggested number has no clean pair yet."""
        return (rank == 0 and diff <= SURE_MM and options_a == options_b == 1 and right["number"] not in clean and
                (wrong["number"] in clean or wrong["_row"].label.conf < SURE_CONF <= right["_row"].label.conf))

    def write_misreads(self, path: Path, applied: list[dict] = (), extra: list[dict] = ()) -> list[dict]:
        """Open suggestions, after the ones already applied (sure = "applied"). `extra` adds
        suggestions from other evidence (mirror twins) for numbers not already suggested."""
        found = self.misreads()
        listed = {(f["piece"], f["x_mm"], f["y_mm"]) for f in found}
        found += [f for f in extra if (f["piece"], f["x_mm"], f["y_mm"]) not in listed]
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, MISREAD_COLUMNS, extrasaction="ignore")
            writer.writeheader()
            writer.writerows([*applied, *found])
        return found

    def write_report(self, path: Path, project: str, generated: str = "", applied: int = 0, symmetry=None) -> None:
        """The model folder's README: what is in it, how far the conversion got, and
        which edge pairs agree and which need a look."""
        records = self.records()
        statuses = collections.Counter(r["status"] for r in records)
        pairs = {r["number"] for r in records if r["status"] == "ok"}
        by_page = collections.defaultdict(collections.Counter)
        for r in records:
            by_page[r["piece"][6:8]]["ok" if r["status"] == "ok" else "check"] += 1
        layouts = self.layouts
        pieces = [p for l in layouts for p in l.pieces]
        folds = [f for p in pieces for f in p.folds]
        labels = [label for p in pieces for label in p.labels]
        mismatched = [l for l in layouts if l.paper and l.paper != l.material]
        lines = [f"# {project.title()}", "",
                 f"{len(records)} printed numbers on {sum(len(l.pieces) for l in self.layouts)} pieces. "
                 f"{len(pairs)} numbers form a clean pair (one plain edge, one tab, lengths within "
                 f"{LENGTH_TOLERANCE_MM:g} mm); {sum(n for s, n in statuses.items() if s != 'ok')} labels need a look.", "",
                 f"Conversion status{f' ({generated})' if generated else ''}, written by `make`. "
                 "Edit the YAML, not this file.", "",
                 "## Files", "",
                 "| file | what | in git |", "|---|---|---|",
                 f"| `{project}.pdf` | source template | no, personal use only |",
                 f"| `{project}.yaml` | pages per cardstock, fold styles, sheet size | yes |",
                 f"| `{project}.svg` | Inkscape review file, one row of pages per cardstock | no, traced pattern |",
                 "| `previews/` | rendered PDF pages, the SVG's faint Source layer | no |",
                 f"| `edge-numbers.csv` | every printed edge number with its line and partner | yes |",
                 f"| `number-misreads.csv` | unpaired numbers matched by length to a look-alike number | yes |",
                 "| `README.md` | this status page | yes |", "",
                 "## Status", "",
                 "| stage | result |", "|---|---|",
                 f"| pages | {len(layouts)} converted |",
                 f"| pieces | {len(pieces)} cut outlines, corners joined by straight edges |",
                 f"| folds | {len(folds)}, {sum(not f.snapped for f in folds)} stretched far to reach the cut |",
                 f"| numbers | {len(labels)} read, {sum(not l.trusted for l in labels)} uncertain (orange in the SVG) |",
                 f"| pieces to check | {sum(p.needs_review for p in pieces)} marked ⚠ in Inkscape |",
                 "| paper colour | " + ("footers agree with the YAML" if not mismatched else
                                       "footers disagree with the YAML: " + _paper_note(mismatched)) + " |",
                 "| nesting on sheets | not started |", "",
                 "## Edge numbers", "",
                 "| status | labels | meaning |", "|---|---:|---|"]
        meaning = {"ok": "partner found, one tab and one plain edge, same length",
                   "length mismatch": "partner found but the marked lines differ in length: misread number or traced line",
                   "both tabs": "both copies sit on a tab fold", "no tab": "neither copy sits on a tab fold",
                   "unpaired": "no other copy of this number: likely misread",
                   "line not found": "no cut edge or fold next to the number",
                   "extra copy: likely misread": "number read more than twice; the other copies already form a clean pair"}
        for status, count in statuses.most_common():
            lines.append(f"| {status} | {count} | {meaning.get(status, 'number read more than twice: some are misread')} |")
        lines += ["", "## Pages", "", "| page | config material | footer says | pieces | ok | check |", "|---|---|---|---:|---:|---:|"]
        for layout in self.layouts:
            page = f"{layout.page:02d}"
            note = layout.paper or "?"
            flag = "" if not layout.paper or layout.paper == layout.material else " ⚠"
            lines.append(f"| {page} | {layout.material} | {note}{flag} | {len(layout.pieces)} | "
                         f"{by_page[page]['ok']} | {by_page[page]['check']} |")
        lines += ["", "## Pieces to check", "", "Pieces listed by how many of their numbers need a look.", "",
                  "| piece | ok | check | numbers to check |", "|---|---:|---:|---|"]
        per_piece = collections.defaultdict(list)
        for r in records:
            per_piece[r["piece"]].append(r)
        ranked = sorted(per_piece.items(), key=lambda item: -sum(r["status"] != "ok" for r in item[1]))
        for piece, rows in ranked:
            bad = [r for r in rows if r["status"] != "ok"]
            if bad:
                listed = ", ".join(f"{r['number']} ({r['status']})" for r in bad)
                lines.append(f"| {piece} | {len(rows) - len(bad)} | {len(bad)} | {listed} |")
        doubtful = [r for r in records if r["corrected"] and r["status"] != "ok"]
        corrected = sum(1 for r in records if r["corrected"])
        lines += ["", "## Hand corrections that still do not pair", "",
                  f"{corrected} numbers were set by hand; {len(doubtful)} of them still do not form a clean pair, "
                  "so the correction, its partner or the traced line is likely off. They come first on the check page.", "",
                  "| piece | number | side | mm | status | partner | partner mm |", "|---|---|---|---:|---|---|---:|"]
        for r in doubtful:
            lines.append(f"| {r['piece']} | {r['number']} | {r['side']} | {r['length_mm']} | {r['status']} | "
                         f"{r['partner_piece']} {r['partner_side']} | {r['partner_length_mm']} |")
        if symmetry:
            mirror, off = symmetry
            paired = sum(len(t.lines) for t in mirror.twins)
            lines += ["", "## Mirror twins", "",
                      f"The model is symmetric: {len(mirror.twins)} pairs of pieces are mirror images "
                      f"({2 * len(mirror.twins)} of {sum(len(l.pieces) for l in self.layouts)} pieces), found by the "
                      f"lengths of their numbered lines: {sum(t.exact for t in mirror.twins)} exact mirrors (outline and "
                      f"tabs match) and {sum(not t.exact for t in mirror.twins)} mirror variations (same body, tabs on "
                      "other edges). Of their {paired} mirrored lines, {off} differ in length from "
                      f"their mirror line by more than 1 mm, so one of the two was traced off (`mirror-mismatches.csv`). "
                      "A twin's clean glue pair also predicts the number on the mirror line; those predictions are "
                      "applied when clear-cut, and otherwise go to the check page with `mirror` as the reason.", ""]
        found = self.misreads(records)
        lines += ["", "## Likely misreads", "",
                  f"{applied} clear-cut misreads were fixed without asking (marked `applied` in "
                  f"`number-misreads.csv`). {len(found)} more numbers that did not pair up sit on a line of the "
                  "same length as another unpaired number on the other side (edge against tab), and the two numbers "
                  "look alike. Check them with `make fix` and `app/number-check.html`.", "",
                  "| piece | side | mm | read | suggested | partner | partner mm | why |", "|---|---|---:|---|---|---|---:|---|"]
        for f in found:
            lines.append(f"| {f['piece']} | {f['side']} | {f['length_mm']} | {f['read']} | {f['suggested']} | "
                         f"{f['partner_piece']} {f['partner_side']} | {f['partner_length_mm']} | {f['why']} |")
        lines += ["", f"Full tables: `edge-numbers.csv`, `number-misreads.csv`.", ""]
        path.write_text("\n".join(lines), encoding="utf-8")


MISREAD_COLUMNS = ["piece", "x_mm", "y_mm", "side", "length_mm", "read", "ocr_conf", "suggested",
                   "partner_piece", "partner_x_mm", "partner_y_mm", "partner_side", "partner_length_mm", "length_diff_mm", "why", "sure"]


def _similar(a: dict, b: dict) -> tuple[int, str] | None:
    """How alike two read numbers are, as (rank, reason), lower rank is stronger; None if unalike."""
    x, y = a["number"], b["number"]
    if y in a["_row"].label.alternatives or x in b["_row"].label.alternatives:
        return 0, "OCR's other reading"
    if len(x) == len(y) and sum(c != d for c, d in zip(x, y)) == 1:
        return 1, "one digit differs"
    if abs(len(x) - len(y)) == 1 and (x in y or y in x):
        return 2, "a digit dropped or added"
    return None


def _paper_note(layouts: list[PageLayout]) -> str:
    """'pages 14-23 say beige (YAML: yellow); page 24 says white (YAML: black)'"""
    groups: dict[tuple[str, str], list[int]] = {}
    for layout in layouts:
        groups.setdefault((layout.paper, layout.material), []).append(layout.page)
    notes = []
    for (paper, material), pages in groups.items():
        where = f"page {pages[0]}" if len(pages) == 1 else (
            f"pages {pages[0]}–{pages[-1]}" if pages[-1] - pages[0] == len(pages) - 1 else "pages " + ", ".join(map(str, pages)))
        notes.append(f"{where} say{'s' if len(pages) == 1 else ''} {paper} (YAML: {material})")
    return "; ".join(notes)
