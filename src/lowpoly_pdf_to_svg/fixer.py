"""Data for the number check page: data/<project>/<project>-check.json.

    python -m src.lowpoly_pdf_to_svg.fixer --config data/bowser/bowser.yaml

One card per number that did not pair up: the PDF patch around it beside the patch
around its partner (the suggested look-alike, or the copy it was paired with).
app/number-check.html opens a model folder, shows the cards, and Save writes
<project>-corrections.csv back into the folder; the next build applies it. The JSON
embeds scan patches, so it stays local (gitignored).
"""

from __future__ import annotations

import argparse
import base64
import csv
import io
import json
import pickle
import sys
from pathlib import Path

from PIL import Image

CROP_MM = 36.0        # smallest patch; grows to hold the whole line the number marks
MARGIN_MM = 10.0      # room past the line's ends, where the true corner may lie
MAX_MM = 120.0
FOLDED_MM = 0.6       # a 3D-model pair matches a card when its line length agrees this closely
SIZE_PX = 360         # patches are scaled to this so long lines do not bloat the JSON


class CheckData:
    def __init__(self, folder: Path, project: str, dpi: int):
        self.folder, self.project = folder, project
        self.mm_per_px = 25.4 / dpi
        self.edges = list(csv.DictReader((folder / f"{project}-edges.csv").open(encoding="utf-8")))
        self.misreads = list(csv.DictReader((folder / f"{project}-misreads.csv").open(encoding="utf-8")))
        self.pages: dict[str, Image.Image] = {}
        self.lines = {(r["piece"], r["x_mm"], r["y_mm"]): [float(v) for v in r.get("line_mm", "").split()]
                      for r in self.edges}
        self.checks = {(r["piece"], r["x_mm"], r["y_mm"]): r.get("checks", "") for r in self.edges}
        self.traces = self._traces()
        self.folded = self._folded()

    def _folded(self) -> dict[frozenset, list[tuple[float, str]]]:
        """Second opinion from the folded 3D model (<project>-3d-glue.csv, written by the 3D
        reconstruction): pairs of an open edge and an open tab of the same length that meet once
        folded. Keyed by the two pieces; reads can differ between builds, so a pair is matched
        to a card by its pieces and line length."""
        found: dict[frozenset, list[tuple[float, str]]] = {}
        for path in (self.folder / f"{self.project}-3d-glue.csv", self.folder / "3d" / f"{self.project}-3d-glue.csv"):
            if path.is_file():
                for r in csv.DictReader(path.open(encoding="utf-8")):
                    if r["status"].startswith("proposed"):
                        found.setdefault(frozenset({r["piece"], r["tab_piece"]}), []).append((float(r["length_mm"]), r["status"]))
                break
        return found

    def _folded_status(self, m: dict) -> str:
        length = (float(m["length_mm"]) + float(m["partner_length_mm"])) / 2
        return next((status for mm, status in self.folded.get(frozenset({m["piece"], m["partner_piece"]}), [])
                     if abs(mm - length) <= FOLDED_MM), "")

    def _traces(self) -> dict[str, dict]:
        """Traced outline corners and folds per piece, in page mm, from the build cache."""
        traces = {}
        for path in sorted((self.folder / "cache").glob("page-*.pickle")):
            with path.open("rb") as handle:
                page, layout = pickle.load(handle)
            mm = page.mm_per_px
            for piece in layout.pieces:
                traces[piece.id] = {
                    "outline": [[round(x * mm, 2), round(y * mm, 2)] for x, y in piece.outline],
                    "folds": [[round(f.a[0] * mm, 2), round(f.a[1] * mm, 2), round(f.b[0] * mm, 2), round(f.b[1] * mm, 2)]
                              for f in piece.folds]}
        return traces

    def cards(self) -> list[dict]:
        cards, covered = [], set()
        # Hand corrections that still do not pair: the correction, its partner or the line is off.
        for r in self.edges:
            if r.get("corrected") != "yes" or r["status"] == "ok":
                continue
            copies = [r] + [o for o in self.edges if o is not r and o["number"] == r["number"]][:2]
            covered.update((o["piece"], o["x_mm"], o["y_mm"]) for o in copies)
            cards.append({"kind": "doubt", "suggested": "", "why": r["status"],
                          "panels": [self._panel(o["piece"], o["x_mm"], o["y_mm"], o["number"], o["side"], o["length_mm"])
                                     for o in copies]})
        for m in self.misreads:
            this = self._panel(m["piece"], m["x_mm"], m["y_mm"], m["read"], m["side"], m["length_mm"])
            other = self._panel(m["partner_piece"], m["partner_x_mm"], m["partner_y_mm"], m["suggested"],
                                m["partner_side"], m["partner_length_mm"])
            covered.update({(m["piece"], m["x_mm"], m["y_mm"]), (m["partner_piece"], m["partner_x_mm"], m["partner_y_mm"])})
            kind = "auto" if m.get("sure") == "applied" else "suggested"
            folded = self._folded_status(m)
            cards.append({"kind": kind, "suggested": m["suggested"], "why": m["why"], "panels": [this, other],
                          "folded": folded})
        for r in self.edges:
            if r["status"] == "ok" or (r["piece"], r["x_mm"], r["y_mm"]) in covered:
                continue
            panels = [self._panel(r["piece"], r["x_mm"], r["y_mm"], r["number"], r["side"], r["length_mm"])]
            partner = next((o for o in self.edges if o is not r and o["number"] == r["number"]
                            and o["piece"] == r["partner_piece"] and o["side"] == r["partner_side"]), None)
            if partner:
                panels.append(self._panel(partner["piece"], partner["x_mm"], partner["y_mm"], partner["number"],
                                          partner["side"], partner["length_mm"]))
            cards.append({"kind": "open", "suggested": "", "why": r["status"], "panels": panels})
        return cards

    def _panel(self, piece: str, x: str, y: str, number: str, side: str, length: str) -> dict:
        line = self.lines.get((piece, x, y), [])
        image, box = self._crop(piece, float(x), float(y), line)
        return {"piece": piece, "x": x, "y": y, "read": number, "side": side, "length": length,
                "image": image, "box": box, "line": line, "checks": self.checks.get((piece, x, y), "")}

    def _crop(self, piece: str, x_mm: float, y_mm: float, line: list[float]) -> tuple[str, list[float]]:
        """Plain scan patch around the number, wide enough to show the whole line it marks,
        and its box on the page [left, top, side] in mm; the page draws the trace on top."""
        page = piece.split("-")[1]
        if page not in self.pages:
            found = sorted((self.folder / "previews").glob(f"{self.project}-page-{page}-*.png"))
            self.pages[page] = Image.open(found[0]).convert("L") if found else Image.new("L", (10, 10), 255)
        xs, ys = [x_mm] + line[0::2], [y_mm] + line[1::2]
        cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
        side = min(MAX_MM, max(CROP_MM, max(xs) - min(xs) + 2 * MARGIN_MM, max(ys) - min(ys) + 2 * MARGIN_MM))
        left, top = cx - side / 2, cy - side / 2
        px = lambda mm: round(mm / self.mm_per_px)
        crop = self.pages[page].crop((px(left), px(top), px(left) + px(side), px(top) + px(side)))
        crop = crop.resize((SIZE_PX, SIZE_PX), Image.LANCZOS)
        buffer = io.BytesIO()
        crop.save(buffer, "JPEG", quality=80)
        box = [round(px(left) * self.mm_per_px, 3), round(px(top) * self.mm_per_px, 3), round(px(side) * self.mm_per_px, 3)]
        return "data:image/jpeg;base64," + base64.b64encode(buffer.getvalue()).decode("ascii"), box

    def write(self, path: Path) -> int:
        cards = self.cards()
        used = {p["piece"] for c in cards for p in c["panels"]}
        traces = {k: v for k, v in self.traces.items() if k in used}
        path.write_text(json.dumps({"project": self.project, "cards": cards, "traces": traces}), encoding="utf-8")
        return len(cards)




def main() -> int:
    parser = argparse.ArgumentParser(description="Write the number check data for app/number-check.html.")
    parser.add_argument("--config", type=Path, default=Path("data/bowser/bowser.yaml"), help="project YAML manifest")
    parser.add_argument("--dpi", type=int, default=180, help="resolution the previews were rendered at")
    args = parser.parse_args()
    folder, project = args.config.parent, args.config.stem
    try:
        count = CheckData(folder, project, args.dpi).write(folder / f"{project}-check.json")
    except OSError as error:
        parser.error(str(error))
    print(f"Wrote {folder / (project + '-check.json')} with {count} numbers to check; "
          "open app/number-check.html and pick the folder")
    return 0


if __name__ == "__main__":
    sys.exit(main())
