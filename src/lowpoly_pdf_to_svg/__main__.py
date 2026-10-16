"""Convert the pages listed in a project manifest into Inkscape review SVGs."""

from __future__ import annotations

import argparse
import csv
import math
import datetime
import pickle
import shutil
import sys
from pathlib import Path

from .config import Project
from .checks import TraceChecks
from .corrections import FOLD_MM, Correction, Corrections, LineFixes, PieceFixes
from .detect import PageDetector
from .edges import EdgeTable
from .ocr import EdgeNumberReader, read_paper
from .render import PageRenderer
from .svg import InkscapeSvgWriter
from .symmetry import Symmetry


def main() -> int:
    parser = argparse.ArgumentParser(description="Trace papercraft PDF pages into Cricut-oriented SVGs.")
    parser.add_argument("--config", type=Path, default=Path("data/bowser/bowser.yaml"), help="project YAML manifest")
    parser.add_argument("--output", type=Path, help="output directory (default: the YAML's folder)")
    parser.add_argument("--dpi", type=int, default=180, help="PDF render resolution (default: 180)")
    parser.add_argument("--page", type=int, action="append", help="convert only this 1-based page; repeatable")
    parser.add_argument("--redo", type=int, nargs="*", metavar="PAGE",
                        help="trace only these pages again and reuse the saved trace of every other page "
                             "(no pages: just redraw the SVG and redo the edge check)")
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
    cache = output / "cache"
    saved = {}
    if args.redo is not None:
        saved = {number: cache / f"page-{number:02d}.pickle" for number, _ in pages if number not in args.redo}
        missing = [str(n) for n, path in saved.items() if not path.is_file()]
        if missing:
            parser.error(f"no saved trace for page(s) {', '.join(missing)}; run a full make first")
    renderer = PageRenderer(project.pdf, args.dpi, renderer_path)
    detector = PageDetector(folds=project.folds)
    results, fresh = [], []
    for number, material in pages:
        if number in saved:
            with saved[number].open("rb") as handle:
                page, layout = pickle.load(handle)
            results.append((page, layout, material))
            continue
        stem = f"{project.name}-page-{number:02d}-{material.id}"
        page = renderer.render(number, output / "previews" / f"{stem}.png")
        layout = detector.detect(page, material.id)
        layout.paper = read_paper(layout.footer)
        if layout.paper and layout.paper not in (material.id, material.name.lower()):
            print(f"warning: page {number} says 'print on {layout.paper} paper' but the config says {material.id}",
                  file=sys.stderr)
        results.append((page, layout, material))
        fresh.append(results[-1])
        print(f"page {number:02d} ({material.id}): {len(results[-1][1].pieces)} pieces", flush=True)

    reader = EdgeNumberReader()
    if not reader.available:
        print("warning: tesseract was not found, so edge numbers are left as '?'", file=sys.stderr)
    corrections = Corrections.load(output / f"{project.name}-corrections.csv")
    new_labels = [label for _, layout, _ in fresh for piece in layout.pieces for label in piece.labels]
    known = corrections.match([(layout, page.mm_per_px) for page, layout, _ in fresh])
    print(f"reading {len(new_labels)} edge numbers ({len(known)} corrected by hand teach the reader) ...", flush=True)
    reader.read_all(new_labels, known)
    cache.mkdir(parents=True, exist_ok=True)
    for page, layout, _ in fresh:
        with (cache / f"page-{layout.page:02d}.pickle").open("wb") as handle:
            pickle.dump((page, layout), handle)
    if corrections.rows:
        applied, missed = corrections.apply([(layout, page.mm_per_px) for page, layout, _ in results])
        print(f"applied {applied} hand corrections" + (f", {len(missed)} matched no number: "
              + ", ".join(f"{c.piece} {c.read}->{c.number}" for c in missed) if missed else ""))
    # Folds added or dropped and corners moved on the piece review, then every piece tidied (near points
    # merged, overlapping lines split); numbers on changed pieces look for their line again.
    piece_fixes = PieceFixes.load(output / f"{project.name}-pieces.csv")
    page_of = {piece.id: page for page, layout, _ in results for piece in layout.pieces}
    changed, missed = piece_fixes.apply([(layout, page.mm_per_px) for page, layout, _ in results],
                                        lambda piece, a, b: detector.fold_kind(page_of[piece], a, b))
    # Corners the folded 3D model says are slightly off (written by the 3D thread); a corner Helga
    # moved by hand keeps her position.
    nudges = PieceFixes.load(output / f"{project.name}-3d-moves.csv")
    if nudges.rows:
        hand = [(r.piece, p) for r in piece_fixes.rows if r.action == "move" for p in (r.a, r.b)]
        nudges.rows = [r for r in nudges.rows
                       if not any(piece == r.piece and math.dist(p, r.a) <= FOLD_MM for piece, p in hand)]
        nudged, unmatched = nudges.apply([(layout, page.mm_per_px) for page, layout, _ in results])
        changed |= nudged
        print(f"moved {len(nudges.rows) - len(unmatched)} corners on {len(nudged)} pieces from the 3D fold"
              + (f", {len(unmatched)} matched no corner" if unmatched else ""))
    for page, layout, _ in results:
        for piece in layout.pieces:
            if piece.id in changed:
                for label in piece.labels:
                    detector._mark_edge(label, piece, 1 / page.mm_per_px)
    print(f"changed {len(changed)} pieces by hand or from the 3D fold (folds, corners)" + (f", {len(missed)} rows matched no fold or corner" if missed else ""))
    lines = LineFixes.load(output / f"{project.name}-lines.csv")
    if lines.rows:
        applied, missed = lines.apply([(layout, page.mm_per_px) for page, layout, _ in results])
        print(f"applied {applied} hand-drawn lines" + (f", {len(missed)} matched no number" if missed else ""))
    # Clear-cut misreads are fixed without asking; the rest wait for the number check page.
    measured = [(layout, page.mm_per_px) for page, layout, _ in results]
    first = EdgeTable()
    for layout, mm in measured:
        first.add(layout, mm)
    sure = [m for m in first.misreads() if m["sure"] == "yes"]
    Corrections([Correction(m["piece"], float(m["x_mm"]), float(m["y_mm"]), m["read"], m["suggested"])
                 for m in sure], by_hand=False).apply(measured)
    print(f"fixed {len(sure)} clear-cut misreads without asking")
    # Mirror twins predict numbers from the clean pairs on the other side of the model.
    symmetry = Symmetry(measured)
    second = EdgeTable()
    for layout, mm in measured:
        second.add(layout, mm)
    predicted = symmetry.predictions(second.records())
    mirrored = [m for m in predicted if m["sure"] == "yes"]
    Corrections([Correction(m["piece"], float(m["x_mm"]), float(m["y_mm"]), m["read"], m["suggested"])
                 for m in mirrored], by_hand=False).apply(measured)
    print(f"{len(symmetry.twins)} mirror twins; fixed {len(mirrored)} numbers from their twins without asking")
    sure += mirrored
    labels = [label for _, layout, _ in results for piece in layout.pieces for label in piece.labels]

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
    for layout, mm in measured:
        table.add(layout, mm)
    checks = TraceChecks(measured)
    checks.scale(table.records())
    table.checks = checks
    found = checks.write(output / f"{project.name}-checks.csv")
    print(f"Wrote {output / (project.name + '-checks.csv')}: "
          + (", ".join(f"{n} {c}" for c, n in found.most_common()) or "no trace faults"))
    edges = output / f"{project.name}-edges.csv"
    statuses = table.write(edges)
    records = table.records()
    asked = symmetry.predictions(records)
    misreads = table.write_misreads(output / f"{project.name}-misreads.csv",
                                    applied=[dict(m, sure="applied") for m in sure], extra=asked)
    mirrors = output / f"{project.name}-mirrors.csv"
    off = symmetry.write(mirrors, records)
    print(f"Wrote {mirrors}: {off} lines differ in length from their mirror line")
    # a fold Helga removed by hand is not suggested again from the twin
    dropped = [(r.piece, r.a, r.b) for r in piece_fixes.rows if r.action == "drop"]
    undone = lambda g: any(piece == g["piece"] and min(
        math.dist(a, (g["ax_mm"], g["ay_mm"])) + math.dist(b, (g["bx_mm"], g["by_mm"])),
        math.dist(b, (g["ax_mm"], g["ay_mm"])) + math.dist(a, (g["bx_mm"], g["by_mm"]))) <= 4.0
        for piece, a, b in dropped)
    gaps = [g for g in symmetry.fold_gaps() if not (g["issue"] == "missing" and undone(g))]
    with (output / f"{project.name}-mirror-folds.csv").open("w", newline="", encoding="utf-8") as handle:
        table_out = csv.DictWriter(handle, ["piece", "twin", "issue", "kind", "ax_mm", "ay_mm", "bx_mm", "by_mm"])
        table_out.writeheader()
        table_out.writerows(gaps)
    missing = [g for g in gaps if g["issue"] == "missing"]
    print(f"Wrote {output / (project.name + '-mirror-folds.csv')}: {len(missing)} folds whose mirror twin has them "
          f"on {len({g['piece'] for g in missing})} pieces, {len(gaps) - len(missing)} mirror folds in another style")
    print(f"Wrote {output / (project.name + '-misreads.csv')}: {len(misreads)} likely misreads left to check")
    table.write_report(output / "README.md", project.name, datetime.date.today().isoformat(), applied=len(sure),
                       symmetry=(symmetry, off))
    print(f"Wrote {edges}: " + ", ".join(f"{n} {s}" for s, n in statuses.most_common()))
    target = output / f"{project.name}.svg"
    writer.write(target)
    print(f"Wrote {len(pages)} page(s) to {target}. {len(flagged)} piece(s) flagged for review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
