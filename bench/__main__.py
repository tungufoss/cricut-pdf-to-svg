"""Run the benchmark: every method on every page and condition, one tidy CSV out.

    python -m bench --data bench/out --out bench/results.csv

Rows: template, page, condition, method, metric, value. Predicted SVGs are written next
to the rasters (<template>/<condition>/<method>/page-NN.svg) for inspection.
"""

from __future__ import annotations

import argparse
import csv
import sys
import time
from pathlib import Path

import cv2

from .baselines import METHODS
from .classify import SharedClassifier
from .metrics import Evaluator
from .model import Page
from .perturb import VARIANTS
from .synth import CONDITIONS


def run(data: Path, out: Path, methods: list[str] | None) -> int:
    rows = 0
    with out.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["template", "page", "condition", "method", "metric", "value"])
        for truth_file in sorted(data.glob("*/page-*.json")):
            truth = Page.from_json(truth_file)
            for cond in CONDITIONS:
                raster = truth_file.parent / cond.name / truth_file.with_suffix(".png").name
                if not raster.exists():
                    continue
                gray = cv2.imread(str(raster), cv2.IMREAD_GRAYSCALE)
                evaluator = Evaluator(truth, gray, cond.dpi)
                classifier = SharedClassifier(gray, cond.dpi)
                preds = [(m.name, lambda m=m: m(gray, cond.dpi)) for m in METHODS]
                preds += [(v.name, lambda v=v: v(truth)) for v in VARIANTS]
                for name, make in preds:
                    if methods and name not in methods:
                        continue
                    start = time.time()
                    raw = make()
                    pred = classifier(raw)
                    folder = raster.parent / name
                    folder.mkdir(exist_ok=True)
                    (folder / truth_file.with_suffix(".svg").name).write_text(pred.to_svg(truth.width_mm, truth.height_mm))
                    scores = evaluator.evaluate(pred, raw)
                    scores["seconds"] = round(time.time() - start, 2)
                    for metric, value in scores.items():
                        writer.writerow([truth.template, truth.page, cond.name, name, metric, f"{value:.6g}"])
                        rows += 1
                    print(f"{truth.template} p{truth.page} {cond.name} {name}: "
                          f"IoU {scores['raster_iou']:.3f}  closed {scores['F1_closed']:.2f}  "
                          f"cut/fold F1 {scores['F3_macro_f1']:.2f}", file=sys.stderr)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--data", type=Path, default=Path("bench/out"))
    parser.add_argument("--out", type=Path, default=Path("bench/results.csv"))
    parser.add_argument("--methods", nargs="*", help="only these methods (default: all)")
    args = parser.parse_args()
    print(f"{run(args.data, args.out, args.methods)} rows in {args.out}")


if __name__ == "__main__":
    main()
