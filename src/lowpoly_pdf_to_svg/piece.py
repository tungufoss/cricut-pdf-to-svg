"""Debug view of one piece: cut it out of the project SVG, lay it over its scan, and
colour each edge number by how its glue pair checked out.

    python -m src.lowpoly_pdf_to_svg.piece --config data/bowser/bowser.yaml piece-05-08

writes data/bowser/pieces/piece-05-08.svg (open it in a browser or Inkscape) and
piece-05-08.md (the piece's rows of the edge table, with each partner).
"""

from __future__ import annotations

import argparse
import base64
import csv
import io
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image

SVG, XLINK, INKSCAPE = "http://www.w3.org/2000/svg", "http://www.w3.org/1999/xlink", "http://www.inkscape.org/namespaces/inkscape"
for prefix, uri in (("", SVG), ("xlink", XLINK), ("inkscape", INKSCAPE),
                    ("sodipodi", "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd")):
    ET.register_namespace(prefix, uri)

STATUS_FILL = {"ok": "#1b8a3a", "length mismatch": "#e65100"}  # anything else is red
OTHER_FILL = "#c62828"
MARGIN_MM = 6.0


class PieceView:
    def __init__(self, svg: Path, edges: Path):
        self.svg_path = svg
        self.tree = ET.parse(svg)
        self.rows = list(csv.DictReader(edges.open(encoding="utf-8")))

    def write(self, piece_id: str, directory: Path) -> tuple[Path, Path]:
        root = self.tree.getroot()
        group = root.find(f".//{{{SVG}}}g[@id='{piece_id}']")
        if group is None:
            raise ValueError(f"{piece_id} is not in {self.svg_path}")
        page = piece_id.split("-")[1]
        image = root.find(f".//{{{SVG}}}image[@id='source-{page}']")
        x0, y0, x1, y1 = self._bounds(group)
        x0, y0, x1, y1 = x0 - MARGIN_MM, y0 - MARGIN_MM, x1 + MARGIN_MM, y1 + MARGIN_MM
        rows = [r for r in self.rows if r["piece"] == piece_id]
        self._colour_numbers(group, rows)

        directory.mkdir(parents=True, exist_ok=True)
        out = ET.Element(f"{{{SVG}}}svg", {"width": f"{x1 - x0:.2f}mm", "height": f"{y1 - y0:.2f}mm",
                                           "viewBox": f"{x0:.3f} {y0:.3f} {x1 - x0:.3f} {y1 - y0:.3f}"})
        ET.SubElement(out, f"{{{SVG}}}rect", {"x": f"{x0:.3f}", "y": f"{y0:.3f}", "width": f"{x1 - x0:.3f}",
                                              "height": f"{y1 - y0:.3f}", "fill": "#ffffff"})
        if image is not None:
            self._scan(out, image, (x0, y0, x1, y1))
        out.append(group)
        svg_out = directory / f"{piece_id}.svg"
        ET.ElementTree(out).write(svg_out, encoding="utf-8", xml_declaration=True)

        md_out = directory / f"{piece_id}.md"
        md_out.write_text(self._table(piece_id, rows), encoding="utf-8")
        return svg_out, md_out

    def _scan(self, out: ET.Element, image: ET.Element, box: tuple[float, float, float, float]) -> None:
        """Embed the piece's patch of the page scan, so the file opens anywhere on its own."""
        png = self.svg_path.parent / image.get(f"{{{XLINK}}}href", "")
        if not png.is_file():
            return
        ix, iy, iw, ih = (float(image.get(k)) for k in ("x", "y", "width", "height"))
        with Image.open(png) as page:
            sx, sy = page.width / iw, page.height / ih
            x0, y0 = max(box[0], ix), max(box[1], iy)
            x1, y1 = min(box[2], ix + iw), min(box[3], iy + ih)
            crop = page.crop((round((x0 - ix) * sx), round((y0 - iy) * sy), round((x1 - ix) * sx), round((y1 - iy) * sy)))
            buffer = io.BytesIO()
            crop.save(buffer, "PNG")
        ET.SubElement(out, f"{{{SVG}}}image", {
            f"{{{XLINK}}}href": "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode("ascii"),
            "x": f"{x0:.3f}", "y": f"{y0:.3f}", "width": f"{x1 - x0:.3f}", "height": f"{y1 - y0:.3f}",
            "preserveAspectRatio": "none", "opacity": "0.5"})

    @staticmethod
    def _bounds(group: ET.Element) -> tuple[float, float, float, float]:
        numbers = [float(v) for path in group.iter(f"{{{SVG}}}path")
                   for v in re.findall(r"-?\d+(?:\.\d+)?", path.get("d", ""))]
        xs, ys = numbers[0::2], numbers[1::2]
        return min(xs), min(ys), max(xs), max(ys)

    @staticmethod
    def _colour_numbers(group: ET.Element, rows: list[dict]) -> None:
        status = {r["number"]: r["status"] for r in rows}
        for text in group.iter(f"{{{SVG}}}text"):
            text.set("fill", STATUS_FILL.get(status.get(text.text or "", ""), OTHER_FILL))
            text.set("data-status", status.get(text.text or "", "not in table"))

    @staticmethod
    def _table(piece_id: str, rows: list[dict]) -> str:
        lines = [f"# {piece_id}", "",
                 "Numbers: green = clean pair, orange = length mismatch, red = anything else.", "",
                 "| number | side | length mm | partner | partner side | partner mm | status |",
                 "|---|---|---:|---|---|---:|---|"]
        for r in sorted(rows, key=lambda r: (r["status"] != "ok", r["number"])):
            lines.append(f"| {r['number']} | {r['side']} | {r['length_mm']} | {r['partner_piece']} | "
                         f"{r['partner_side']} | {r['partner_length_mm']} | {r['status']} |")
        return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Write a debug SVG and table for one piece.")
    parser.add_argument("piece", help="piece id, such as piece-05-08")
    parser.add_argument("--config", type=Path, default=Path("data/bowser/bowser.yaml"), help="project YAML manifest")
    args = parser.parse_args()
    folder, project = args.config.parent, args.config.stem
    try:
        svg, md = PieceView(folder / f"{project}.svg", folder / f"{project}-edges.csv").write(args.piece, folder / "pieces")
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(f"Wrote {svg} and {md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
