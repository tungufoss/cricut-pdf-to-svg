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
    COLUMNS = ["number", "piece", "side", "length_mm", "x_mm", "y_mm", "ocr_trusted",
               "partner_piece", "partner_side", "partner_length_mm", "length_diff_mm", "status"]

    def __init__(self):
        self.rows: list[EdgeRow] = []
        self.layouts: list[PageLayout] = []

    def add(self, layout: PageLayout, mm_per_px: float) -> None:
        self.layouts.append(layout)
        self.rows.extend(EdgeRow(piece.id, label, mm_per_px) for piece in layout.pieces for label in piece.labels)

    def records(self) -> list[dict]:
        by_number = collections.defaultdict(list)
        for row in self.rows:
            by_number[row.label.text].append(row)
        records = []
        for row in self.rows:
            others = [o for o in by_number[row.label.text] if o is not row]
            partner = others[0] if len(others) == 1 else None
            records.append({
                "number": row.label.text,
                "piece": row.piece,
                "side": row.side,
                "length_mm": f"{row.length_mm:.1f}",
                "x_mm": f"{row.label.center[0] * row.mm_per_px:.1f}",
                "y_mm": f"{row.label.center[1] * row.mm_per_px:.1f}",
                "ocr_trusted": "yes" if row.label.trusted else "no",
                "partner_piece": partner.piece if partner else "",
                "partner_side": partner.side if partner else "",
                "partner_length_mm": f"{partner.length_mm:.1f}" if partner else "",
                "length_diff_mm": f"{abs(row.length_mm - partner.length_mm):.1f}" if partner else "",
                "status": self._status(row, partner, len(others)),
            })
        return sorted(records, key=lambda r: (int(r["number"]) if r["number"].isdigit() else 10**6, r["piece"]))

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
            writer = csv.DictWriter(handle, self.COLUMNS)
            writer.writeheader()
            writer.writerows(records)
        return collections.Counter(r["status"] for r in records)

    def write_report(self, path: Path, title: str) -> None:
        """A short Markdown summary: which edge pairs agree and which need a look."""
        records = self.records()
        statuses = collections.Counter(r["status"] for r in records)
        pairs = {r["number"] for r in records if r["status"] == "ok"}
        by_page = collections.defaultdict(collections.Counter)
        for r in records:
            by_page[r["piece"][6:8]]["ok" if r["status"] == "ok" else "check"] += 1
        lines = [f"# {title}: edge number report", "",
                 f"{len(records)} printed numbers on {sum(len(l.pieces) for l in self.layouts)} pieces. "
                 f"{len(pairs)} numbers form a clean pair (one plain edge, one tab, lengths within "
                 f"{LENGTH_TOLERANCE_MM:g} mm); {sum(n for s, n in statuses.items() if s != 'ok')} labels need a look.", "",
                 "## Status", "", "| status | labels | meaning |", "|---|---:|---|"]
        meaning = {"ok": "partner found, one tab and one plain edge, same length",
                   "length mismatch": "partner found but the marked lines differ in length: misread number or traced line",
                   "both tabs": "both copies sit on a tab fold", "no tab": "neither copy sits on a tab fold",
                   "unpaired": "no other copy of this number: likely misread",
                   "line not found": "no cut edge or fold next to the number"}
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
        lines += ["", f"Full table: `{path.stem.replace('-report', '')}-edges.csv`.", ""]
        path.write_text("\n".join(lines), encoding="utf-8")
