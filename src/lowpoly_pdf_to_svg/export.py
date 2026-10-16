"""Export: the last step, turning the finished review SVG into a cut-ready file.

    python -m src.lowpoly_pdf_to_svg.export --config data/bowser/bowser.yaml

reads data/bowser/bowser.svg and bowser-edges.csv (both as left by make, make fix and
the piece review) and writes

* data/bowser/bowser-export.svg: the Pieces layer only (Source and Review dropped),
  every piece filled with its cardstock colour, and every edge number replaced by a
  short label such as 2A. Two edges that glue together share a label, and no other
  edge has it, so the PDF's three-digit numbers become two characters for the
  Cricut pen. Layers and the per-piece Cut, Score and Draw groups stay as they are.
* data/bowser/bowser-labels.csv: which PDF number and which edges each label stands
  for, so a label traces back to the template.

The review SVG, the check page and the fix loop keep the PDF numbers; only this file
is renumbered. Labels are handed out in PDF-number order from an alphabet without
look-alikes (0/O, 1/I, Q, and 6/9 since labels sit at any angle), all of one width:
two characters for up to 900 glue pairs, three beyond that.
"""

from __future__ import annotations

import argparse
import csv
import math
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from itertools import islice, product
from pathlib import Path

import yaml

SVG, INKSCAPE = "http://www.w3.org/2000/svg", "http://www.inkscape.org/namespaces/inkscape"
for prefix, uri in (("", SVG), ("xlink", "http://www.w3.org/1999/xlink"), ("inkscape", INKSCAPE),
                    ("sodipodi", "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd")):
    ET.register_namespace(prefix, uri)
LABEL = f"{{{INKSCAPE}}}label"

# Cardstock colours used when the YAML material has no `color:`.
DEFAULT_COLORS = {"red": "#c62828", "green": "#2e7d32", "yellow": "#f9d71c", "black": "#212121",
                  "white": "#ffffff", "beige": "#e8d9b5", "blue": "#1565c0", "orange": "#ef6c00",
                  "brown": "#6d4c41", "grey": "#9e9e9e", "gray": "#9e9e9e", "pink": "#f48fb1",
                  "purple": "#6a1b9a"}
FALLBACK_COLOR = "#cccccc"


class LabelAlphabet:
    """Short labels of one width, at least two characters (2A, not A next to 2A), as few
    characters as the number of glue pairs allows."""

    # No 0/O, 1/I or Q (look alike) and no 6/9 (labels sit at any angle).
    SYMBOLS = "1234578ABCDEFGHJKLMNPRSTUVWXYZ"

    def __init__(self, symbols: str = SYMBOLS, shortest: int = 2):
        self.symbols, self.shortest = symbols, shortest

    def take(self, count: int) -> list[str]:
        width = self.shortest
        while len(self.symbols) ** width < count:
            width += 1
        return ["".join(chars) for chars in islice(product(self.symbols, repeat=width), count)]


@dataclass
class Edge:
    """One printed number on one piece, as a row of the edge table."""

    number: str
    piece: str
    x_mm: float  # page coordinates, as in the edge table
    y_mm: float
    partner: str
    status: str


@dataclass
class GluePair:
    """The edges that share one label: normally a tab and the edge it glues to."""

    number: str
    edges: list[Edge] = field(default_factory=list)
    label: str = ""

    @property
    def status(self) -> str:
        return self.edges[0].status if self.edges else "no edge row"


class GluePairs:
    """Groups the edge table into glue pairs and gives each pair its short label."""

    def __init__(self, edges: list[Edge]):
        pairs: dict[tuple, GluePair] = {}
        for index, edge in enumerate(edges):
            key = ((edge.number, *sorted((edge.piece, edge.partner))) if edge.partner
                   else (edge.number, edge.piece, index))
            pairs.setdefault(key, GluePair(edge.number)).edges.append(edge)
        self.pairs = sorted(pairs.values(), key=lambda p: (_numeric(p.number), p.edges[0].piece))
        self._orphans: dict[str, GluePair] = {}

    @classmethod
    def read(cls, path: Path) -> "GluePairs":
        with path.open(newline="", encoding="utf-8") as handle:
            return cls([Edge(row["number"], row["piece"], float(row["x_mm"]), float(row["y_mm"]),
                             row["partner_piece"], row["status"]) for row in csv.DictReader(handle)])

    def find(self, piece: str, number: str, x_mm: float, y_mm: float, used: set[int]) -> GluePair:
        """The pair of the nearest unused edge row with this piece and number; a number with
        no row gets a pair of its own, shared by every other such copy of that number."""
        best, distance = None, math.inf
        for pair in self.pairs:
            for edge in pair.edges:
                if edge.piece == piece and edge.number == number and id(edge) not in used:
                    d = math.hypot(edge.x_mm - x_mm, edge.y_mm - y_mm)
                    if d < distance:
                        best, distance = (pair, edge), d
        if best:
            used.add(id(best[1]))
            return best[0]
        return self._orphans.setdefault(number, GluePair(number))

    def assign(self, alphabet: LabelAlphabet) -> None:
        everything = self.pairs + sorted(self._orphans.values(), key=lambda p: _numeric(p.number))
        for pair, label in zip(everything, alphabet.take(len(everything))):
            pair.label = label

    def write(self, path: Path) -> None:
        everything = self.pairs + list(self._orphans.values())
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["label", "pdf_number", "status", "pieces"])
            for pair in sorted(everything, key=lambda p: (len(p.label), p.label)):
                writer.writerow([pair.label, pair.number, pair.status, " ".join(e.piece for e in pair.edges)])


class CardstockColors:
    """Fill colour per material id: the YAML `color:` if given, else a named default."""

    def __init__(self, config: Path):
        raw = yaml.safe_load(config.read_text(encoding="utf-8"))
        self.colors = {str(m["id"]): str(m.get("color") or DEFAULT_COLORS.get(str(m["id"]).lower(), FALLBACK_COLOR))
                       for m in raw["materials"]}

    def __getitem__(self, material: str) -> str:
        return self.colors.get(material, FALLBACK_COLOR)


class ExportWriter:
    """Rewrites the review SVG into the export SVG."""

    PIECE_ID = re.compile(r"piece-(\d+)-\d+$")

    def __init__(self, pairs: GluePairs, colors: CardstockColors, alphabet: LabelAlphabet = LabelAlphabet()):
        self.pairs, self.colors, self.alphabet = pairs, colors, alphabet

    def export(self, source: Path, target: Path) -> dict[str, int]:
        tree = ET.parse(source)
        root = tree.getroot()
        for layer in [g for g in root.findall(f"{{{SVG}}}g") if g.get("id") in ("source", "review")]:
            root.remove(layer)
        title = root.find(f"{{{SVG}}}title")
        if title is not None:
            title.text = f"{title.text} (export)"
        offsets = {page.get("id"): (float(page.get("x")), float(page.get("y")))
                   for page in root.iter(f"{{{INKSCAPE}}}page")}

        texts, used = [], set()
        pieces = [g for g in root.iter(f"{{{SVG}}}g") if g.get("data-material") is not None]
        for piece in pieces:
            self._fill(piece)
            match = self.PIECE_ID.match(piece.get("id", ""))
            ox, oy = offsets.get(f"page-{int(match.group(1)):02d}", (0.0, 0.0)) if match else (0.0, 0.0)
            for text in piece.iter(f"{{{SVG}}}text"):
                number = (text.text or "").strip()
                pair = self.pairs.find(piece.get("id"), number,
                                       float(text.get("x")) - ox, float(text.get("y")) - oy, used)
                texts.append((text, pair))
        self.pairs.assign(self.alphabet)
        for text, pair in texts:
            text.set("data-pdf-number", text.text or "")
            text.text = pair.label
            for attribute in ("fill", "data-review"):  # the review's orange "unsure" mark
                text.attrib.pop(attribute, None)

        ET.indent(tree, space="")
        target.parent.mkdir(parents=True, exist_ok=True)
        tree.write(target, encoding="UTF-8", xml_declaration=True)
        return {"pieces": len(pieces), "labels": len(texts),
                "pairs": len({id(pair) for _, pair in texts}),
                "longest": max((len(pair.label) for _, pair in texts), default=0)}

    def _fill(self, piece: ET.Element) -> None:
        """Fill the piece with its cardstock: outline and holes become one even-odd path,
        so holes stay open, and the numbers turn white on a dark card to stay readable."""
        color = self.colors[piece.get("data-material")]
        piece.set(LABEL, piece.get(LABEL, "").split(" ⚠")[0])
        for group in piece.iter(f"{{{SVG}}}g"):
            operation = group.get("data-operation")
            if operation == "cut":
                paths = group.findall(f"{{{SVG}}}path")
                if paths:
                    paths[0].set("d", " ".join(p.get("d") for p in paths))
                    for extra in paths[1:]:
                        group.remove(extra)
                group.set("style", _style(group.get("style", ""), fill=color, **{"fill-rule": "evenodd"}))
            elif operation == "draw" and _luminance(color) < 0.35:
                group.set("style", _style(group.get("style", ""), fill="#ffffff"))


def _style(style: str, **changes: str) -> str:
    items = dict(part.split(":", 1) for part in style.split(";") if ":" in part)
    items.update(changes)
    return ";".join(f"{key}:{value}" for key, value in items.items())


def _luminance(color: str) -> float:
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", color):
        return 1.0
    r, g, b = (int(color[i:i + 2], 16) / 255 for i in (1, 3, 5))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _numeric(number: str) -> tuple[int, str]:
    return (int(number), number) if number.isdigit() else (sys.maxsize, number)


def main() -> int:
    parser = argparse.ArgumentParser(description="Write the cut-ready export SVG with short edge labels and cardstock fills.")
    parser.add_argument("--config", type=Path, default=Path("data/bowser/bowser.yaml"), help="project YAML manifest")
    parser.add_argument("--output", type=Path, help="model folder (default: the YAML's folder)")
    args = parser.parse_args()
    folder = args.output or args.config.parent
    project = args.config.stem
    source, edges = folder / f"{project}.svg", folder / f"{project}-edges.csv"
    for path in (source, edges):
        if not path.is_file():
            parser.error(f"{path} not found; run make first")
    pairs = GluePairs.read(edges)
    target = folder / f"{project}-export.svg"
    counts = ExportWriter(pairs, CardstockColors(args.config)).export(source, target)
    pairs.write(folder / f"{project}-labels.csv")
    print(f"{target}: {counts['pieces']} pieces filled, {counts['labels']} numbers -> "
          f"{counts['pairs']} labels of at most {counts['longest']} characters; "
          f"key in {folder / f'{project}-labels.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
