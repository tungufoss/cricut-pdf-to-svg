# Fabrication-aware vectorization benchmark (paper 1)

Does a vectorization that looks right also cut and fold right? This folder scores existing
raster-to-vector methods two ways on papercraft templates with exact ground truth:
conventional visual metrics against the raster, and fabrication metrics against the vector
truth. Research plan and paper skeleton: `research/` in the project files; issues #7, #10
and #11 (label `paper-1`).

```sh
make bench          # synthetic templates, every method, bench/results.csv
make bench-report   # R summary: bench/summary/{methods,correlations}.csv, summary.md
```

## Stages

| module | what |
|---|---|
| `model.py` | ground truth (`Page` > `Piece` > outline, folds, edges with `matches`, labels; mm) and predictions (untyped or typed polylines) |
| `synth.py` | random low-poly solids unfolded into nets, glue tabs, numbered edge pairs, A4 pages; drawn at 600 dpi in a per-template line style, then degraded to the conditions `clean-300`, `scan-150` (blur, JPEG 75, noise), `poor-100` |
| `baselines.py` | A `A-contours` (Otsu, OpenCV contours, Douglas–Peucker), B `B-potrace` (Potrace via potracer), C `C-centerline` (Zhang–Suen thinning, chains, Douglas–Peucker) |
| `classify.py` | shared cut/fold classifier: solid ink under a segment is a cut, broken ink a fold; applied to every untyped method alike |
| `perturb.py` | ground truth as a method (`T-oracle`) and damaged copies: 2 % scale, 0.4 mm vertex jitter, outlines left open by 0.6 mm, folds typed as cuts |
| `metrics.py` | visual: raster IoU, chamfer and Hausdorff (mm), complexity; fabrication F1–F5 (below) |
| `analysis.R` | tidyverse summary and Spearman correlations, visual vs fabrication |

## Fabrication metrics

| id | metric | meaning |
|---|---|---|
| F1 | `F1_closed` | share of pieces with a closed cut contour matching the piece (IoU ≥ 0.8) |
| F2 | `F2_dim_mm`, `F2_dim_rel` | error of matched pieces' box sides |
| F3 | `F3_cut_*`, `F3_fold_*`, `F3_macro_f1` | per-class precision, recall, F1 at 0.5 mm |
| F4 | `F4_duplicate_contours`, `F4_extra_contours`, `F4_cut_paths_per_piece`, `F4_fragments_per_fold`, `F4_folds_missing` | cutting a piece twice, stray contours (numbers traced as cuts), broken outlines and folds |
| F5 | `F5_match_diff_mm`, `F5_match_over_0.5mm`, `F5_edge_length_err_mm`, `F5_pairs_unmeasurable` | length difference between the two copies of each glued edge, measured between predicted vertices near the true edge ends |
| F6 | `paths`, `nodes`, `controls`, `svg_bytes` | complexity (also the conventional complexity measure) |

Visual metrics use each method's raw output; fabrication metrics use it after the shared
classifier. Typed methods (the `T-` variants, later our own pipeline) skip the classifier.

## Known limits

- Ground truth is synthetic: convex solids, triangles only, one fold style per template,
  labels may overlap on thin faces. Real templates (Bowser and permissively licensed ones)
  come next (#11).
- The oracle draws folds solid and has no printed numbers, so its visual scores are low by
  construction; that gap is itself part of the argument.
- Our pipeline (baseline D) reads PDFs through its YAML manifest and is not wired in yet.
- No technical-drawing method with learned components yet (#7); C is the classical
  centreline approach.
