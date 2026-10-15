"""Convert the pages listed in a project manifest into Inkscape review SVGs."""

from __future__ import annotations

import argparse
import datetime
import shutil
import sys
from pathlib import Path

from .config import Project
from .detect import PageDetector
from .edges import EdgeTable
from .ocr import EdgeNumberReader, read_paper
from .render import PageRenderer
from .svg import InkscapeSvgWriter


def main() -> int:
    parser = argparse.ArgumentParser(description="Trace papercraft PDF pages into Cricut-oriented SVGs.")
    parser.add_argument("--config", type=Path, default=Path("data/bowser/bowser.yaml"), help="project YAML manifest")
    parser.add_argument("--output", type=Path, help="output directory (default: the YAML's folder)")
    parser.add_argument("--dpi", type=int, default=180, help="PDF render resolution (default: 180)")
    parser.add_argument("--page", type=int, action="append", help="convert only this 1-based page; repeatable")
    parser.add_argument("--pdftoppm", default="pdftoppm", help="Poppler pdftoppm executable")
    args = parser.parse_args()

    try:
        project = Project.load(args.config)
        pages = project.pages()
    except ValueError as error:
        parser.error(str(error))
    if not project.pdf.is_file():
        parser.error(f"PDF not found: {project.pdf}")
    renderer_path = shutil.which(args.pdftoppm) or (args.pdftoppm if Path(args.pdftoppm).is_file() else None)
    if not renderer_path:
        parser.error("pdftoppm was not found; install Poppler or pass --pdftoppm")
    if args.page:
        missing = set(args.page) - {page for page, _ in pages}
        if missing:
            parser.error(f"page(s) not assigned to a material: {', '.join(map(str, sorted(missing)))}")
        pages = [(page, material) for page, material in pages if page in args.page]

    output = args.output or args.config.parent
    renderer = PageRenderer(project.pdf, args.dpi, renderer_path)
    detector = PageDetector(folds=project.folds)
    results = []
    for number, material in pages:
        stem = f"{project.name}-page-{number:02d}-{material.id}"
        page = renderer.render(number, output / "previews" / f"{stem}.png")
        layout = detector.detect(page, material.id)
        layout.paper = read_paper(layout.footer)
        if layout.paper and layout.paper not in (material.id, material.name.lower()):
            print(f"warning: page {number} says 'print on {layout.paper} paper' but the config says {material.id}",
                  file=sys.stderr)
        results.append((page, layout, material))
        print(f"page {number:02d} ({material.id}): {len(results[-1][1].pieces)} pieces", flush=True)

    reader = EdgeNumberReader()
    if not reader.available:
        print("warning: tesseract was not found, so edge numbers are left as '?'", file=sys.stderr)
    labels = [label for _, layout, _ in results for piece in layout.pieces for label in piece.labels]
    print(f"reading {len(labels)} edge numbers ...", flush=True)
    reader.read_all(labels)

    writer = InkscapeSvgWriter(f"{project.name.title()} papercraft")
    for page, layout, material in results:
        writer.add(page, layout, material)
    folds = [f for _, layout, _ in results for p in layout.pieces for f in p.folds]
    flagged = [p.id for _, layout, _ in results for p in layout.pieces if p.needs_review]
    unsure = sum(not label.trusted for label in labels)
    print(f"{len(folds)} folds ({sum(not f.snapped for f in folds)} stretched far to reach the cut), "
          f"{len(labels)} numbers ({unsure} uncertain).")
    if flagged:
        print(f"check: {', '.join(flagged)}")
    table = EdgeTable()
    for page, layout, _ in results:
        table.add(layout, page.mm_per_px)
    edges = output / f"{project.name}-edges.csv"
    statuses = table.write(edges)
    table.write_report(output / "README.md", project.name, datetime.date.today().isoformat())
    print(f"Wrote {edges}: " + ", ".join(f"{n} {s}" for s, n in statuses.most_common()))
    target = output / f"{project.name}.svg"
    writer.write(target)
    print(f"Wrote {len(pages)} page(s) to {target}. {len(flagged)} piece(s) flagged for review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
