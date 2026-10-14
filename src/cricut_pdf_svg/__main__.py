"""Convert the pages listed in a project manifest into Inkscape review SVGs."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from .config import Project
from .detect import PageDetector
from .render import PageRenderer
from .svg import InkscapeSvgWriter


def main() -> int:
    parser = argparse.ArgumentParser(description="Trace papercraft PDF pages into Cricut-oriented SVGs.")
    parser.add_argument("--config", type=Path, default=Path("data/bowser.yaml"), help="project YAML manifest")
    parser.add_argument("--output", type=Path, help="output directory (default: output/<project>)")
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

    output = args.output or Path("output") / project.name
    renderer = PageRenderer(project.pdf, args.dpi, renderer_path)
    detector = PageDetector()
    writer = InkscapeSvgWriter(f"{project.name.title()} papercraft")
    flagged = 0
    for number, material in pages:
        stem = f"{project.name}-page-{number:02d}-{material.id}"
        page = renderer.render(number, output / "previews" / f"{stem}.png")
        layout = detector.detect(page, material.id)
        writer.add(page, layout, material)
        folds = sum(len(p.folds) for p in layout.pieces)
        labels = sum(len(p.labels) for p in layout.pieces)
        review = [p.id for p in layout.pieces if p.needs_review]
        flagged += len(review)
        note = f"; check folds on {', '.join(review)}" if review else ""
        print(f"page {number:02d} ({material.id}): {len(layout.pieces)} pieces, {folds} folds, "
              f"{labels} numbers, {len(layout.stray_lines)} stray lines{note}")
    target = output / f"{project.name}.svg"
    writer.write(target)
    print(f"Wrote {len(pages)} page(s) to {target}. {flagged} piece(s) flagged for review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
