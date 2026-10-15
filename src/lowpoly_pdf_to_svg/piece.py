"""Debug view of one piece: cut it out of the project SVG, lay it over its scan, and
colour each edge number by how its glue pair checked out.

    python -m src.lowpoly_pdf_to_svg.piece --config data/bowser/bowser.yaml piece-05-08

writes data/bowser/pieces/piece-05-08.svg (open it in a browser or Inkscape),
piece-05-08.md (the piece's rows of the edge table, with each partner), and
data/bowser/review.png (the PDF patch and the trace side by side).

"""

from __future__ import annotations

import argparse
import base64
import csv
import io
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

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
        scan = self._scan(out, image, (x0, y0, x1, y1)) if image is not None else None
        out.append(group)
        svg_out = directory / f"{piece_id}.svg"
        ET.ElementTree(out).write(svg_out, encoding="utf-8", xml_declaration=True)

        ReviewImage(group, (x0, y0, x1, y1), scan).write(directory.parent / "review.png", piece_id)
        md_out = directory / f"{piece_id}.md"
        md_out.write_text(self._table(piece_id, rows), encoding="utf-8")
        return svg_out, md_out

    def number(self, number: str, path: Path) -> int:
        """Every piece carrying this number, PDF beside trace, the number circled, stacked in one PNG."""
        root = self.tree.getroot()
        rows = [r for r in self.rows if r["number"] == number]
        if not rows:
            raise ValueError(f"number {number} is not in the edge table")
        images = []
        for piece_id in dict.fromkeys(r["piece"] for r in rows):
            group = root.find(f".//{{{SVG}}}g[@id='{piece_id}']")
            image = root.find(f".//{{{SVG}}}image[@id='source-{piece_id.split('-')[1]}']")
            x0, y0, x1, y1 = self._bounds(group)
            box = (x0 - MARGIN_MM, y0 - MARGIN_MM, x1 + MARGIN_MM, y1 + MARGIN_MM)
            self._colour_numbers(group, [r for r in self.rows if r["piece"] == piece_id])
            scan = self._scan(ET.Element("scratch"), image, box) if image is not None else None
            marks = [(float(t.get("x")), float(t.get("y"))) for t in group.iter(f"{{{SVG}}}text") if t.text == number]
            notes = "; ".join(f"{r['side']} {r['length_mm']} mm, {r['status']}" for r in rows if r["piece"] == piece_id)
            images.append(ReviewImage(group, box, scan).render(f"{piece_id} ({notes})", marks))
        sheet = Image.new("RGB", (max(i.width for i in images), sum(i.height + 20 for i in images)), "white")
        y = 0
        for image in images:
            sheet.paste(image, (0, y))
            y += image.height
            ImageDraw.Draw(sheet).line([(0, y + 10), (sheet.width, y + 10)], fill=(120, 120, 120), width=3)
            y += 20
        sheet.save(path)
        return len(images)

    def _scan(self, out: ET.Element, image: ET.Element, box: tuple[float, float, float, float]):
        """Embed the piece's patch of the page scan, so the file opens anywhere on its own."""
        png = self.svg_path.parent / image.get(f"{{{XLINK}}}href", "")
        if not png.is_file():
            return None
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
        return crop, (x0, y0, x1, y1)

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


class ReviewImage:
    """Side by side PNG: the piece's patch of the PDF page, and the trace drawn on white."""

    SCALE = 10.0                 # px per mm
    HEADER = 70                  # px for the title and captions
    STYLE = {"cut": ((0, 0, 0), None), "mountain": ((31, 95, 191), (25, 8, 4, 8)), "valley": ((46, 139, 87), (15, 10))}

    def __init__(self, group: ET.Element, box: tuple[float, float, float, float], scan, scale: float = SCALE):
        self.group, self.box, self.scan, self.SCALE = group, box, scan, scale

    def write(self, path: Path, title: str) -> None:
        self.render(title).save(path)

    def render(self, title: str, marks: list[tuple[float, float]] = ()) -> Image.Image:
        """PDF patch left, trace right; each mark (a number's position, in mm) circled on both."""
        x0, y0, x1, y1 = self.box
        w, h = round((x1 - x0) * self.SCALE), round((y1 - y0) * self.SCALE)
        font = _font(22)
        sheet = Image.new("RGB", (max(2 * w + 30, round(font.getlength(title)) + 20), h + self.HEADER), "white")
        draw = ImageDraw.Draw(sheet)
        draw.text((10, 6), title, fill="black", font=font)
        draw.text((10, 38), "PDF", fill=(90, 90, 90), font=font)
        draw.text((w + 40, 38), "traced", fill=(90, 90, 90), font=font)
        if self.scan is not None:
            crop, (cx0, cy0, cx1, cy1) = self.scan
            size = (round((cx1 - cx0) * self.SCALE), round((cy1 - cy0) * self.SCALE))
            sheet.paste(crop.convert("RGB").resize(size, Image.LANCZOS),
                        (round((cx0 - x0) * self.SCALE), self.HEADER + round((cy0 - y0) * self.SCALE)))
        trace = Image.new("RGB", (w, h), "white")
        self._draw(trace, x0, y0)
        sheet.paste(trace, (w + 30, self.HEADER))
        draw.line([(w + 15, self.HEADER), (w + 15, h + self.HEADER)], fill=(200, 200, 200), width=2)
        r = 4 * self.SCALE
        for mx, my in marks:
            cx, cy = (mx - x0) * self.SCALE, self.HEADER + (my - y0) * self.SCALE
            for left in (0, w + 30):
                draw.ellipse([left + cx - r, cy - r, left + cx + r, cy + r], outline=(230, 0, 180), width=4)
        return sheet

    def _draw(self, image, x0: float, y0: float) -> None:
        draw = ImageDraw.Draw(image)
        to_px = lambda x, y: ((x - x0) * self.SCALE, (y - y0) * self.SCALE)
        for sub in self.group.iter(f"{{{SVG}}}g"):
            kind = sub.get("data-fold") or sub.get("data-operation")
            if kind not in self.STYLE:
                continue
            colour, dash = self.STYLE[kind]
            for path in sub.findall(f"{{{SVG}}}path"):
                values = [float(v) for v in re.findall(r"-?\d+(?:\.\d+)?", path.get("d", ""))]
                points = [to_px(x, y) for x, y in zip(values[0::2], values[1::2])]
                if path.get("d", "").rstrip().endswith("Z"):
                    points.append(points[0])
                for a, b in zip(points, points[1:]):
                    _dashed(draw, a, b, colour, dash, 3 if kind == "cut" else 2)
        for text in self.group.iter(f"{{{SVG}}}text"):
            cx, cy = to_px(float(text.get("x")), float(text.get("y")))
            angle = float(re.search(r"rotate\(([-\d.]+)", text.get("transform", "rotate(0")).group(1))
            size = max(10, round(float(text.get("font-size", "2")) * self.SCALE))
            font = _font(size)
            label = text.text or ""
            left, top, right, bottom = font.getbbox(label)
            stamp = Image.new("RGBA", (right - left + 4, bottom - top + 4), (0, 0, 0, 0))
            ImageDraw.Draw(stamp).text((2 - left, 2 - top), label, fill=text.get("fill", "#8e24aa"), font=font)
            stamp = stamp.rotate(-angle, expand=True, resample=Image.BICUBIC)
            image.paste(stamp, (round(cx - stamp.width / 2), round(cy - stamp.height / 2)), stamp)


def _dashed(draw, a, b, colour, dash, width) -> None:
    if not dash:
        draw.line([a, b], fill=colour, width=width)
        return
    length = math.dist(a, b)
    if length == 0:
        return
    ux, uy = (b[0] - a[0]) / length, (b[1] - a[1]) / length
    at, k = 0.0, 0
    while at < length:
        run = dash[k % len(dash)]
        if k % 2 == 0:
            end = min(at + run, length)
            draw.line([(a[0] + ux * at, a[1] + uy * at), (a[0] + ux * end, a[1] + uy * end)], fill=colour, width=width)
        at += run
        k += 1


def _font(size: int):
    for name in ("arialbd.ttf", "DejaVuSans-Bold.ttf", "Arial Bold.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def main() -> int:
    parser = argparse.ArgumentParser(description="Write a debug SVG and table for one piece.")
    parser.add_argument("piece", nargs="?", help="piece id, such as piece-05-08")
    parser.add_argument("--number", help="write review.png with every piece carrying this number instead")
    parser.add_argument("--config", type=Path, default=Path("data/bowser/bowser.yaml"), help="project YAML manifest")
    args = parser.parse_args()
    folder, project = args.config.parent, args.config.stem
    if not (args.piece or args.number):
        parser.error("give a piece id or --number")
    try:
        view = PieceView(folder / f"{project}.svg", folder / f"{project}-edges.csv")
        if args.number:
            count = view.number(args.number, folder / "review.png")
            print(f"Wrote {folder / 'review.png'} with the {count} pieces carrying {args.number}")
            return 0
        svg, md = view.write(args.piece, folder / "pieces")
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(f"Wrote {svg}, {md} and {folder / 'review.png'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
