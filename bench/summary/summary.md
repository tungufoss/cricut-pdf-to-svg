# Benchmark summary

12 templates, 13 pages, 3 conditions, 8 methods.

## Mean per method and condition

| method | condition | raster_iou | chamfer_mm | F1_closed | F2_dim_mm | F3_macro_f1 | F4_duplicate_contours | F5_match_diff_mm | controls |
|---|---|---|---|---|---|---|---|---|---|
| A-contours | clean-300 | 0.7590 | 0.0231 | 0.8610 | 0.359 | 0.785 | 0.538 | 1.52e-01 | 3920 |
| B-potrace | clean-300 | 0.7270 | 0.0133 | 0.8160 | 0.474 | 0.702 | 0.729 | 1.22e-01 | 9990 |
| C-centerline | clean-300 | 0.6780 | 0.0208 | 0.0438 | 2.020 | 0.842 | 0.000 | 2.60e-01 | 2620 |
| T-folds-as-cuts | clean-300 | 0.4580 | 0.2990 | 1.0000 | 0.000 | 0.350 | 0.000 | 4.02e-05 |  149 |
| T-jitter-0.4mm | clean-300 | 0.2720 | 0.3480 | 1.0000 | 0.339 | 0.999 | 0.000 | 3.50e-01 |  149 |
| T-open-gap | clean-300 | 0.4580 | 0.2990 | 0.0000 | NA | 1.000 | 0.000 | 4.02e-05 |  155 |
| T-oracle | clean-300 | 0.4580 | 0.2990 | 1.0000 | 0.000 | 1.000 | 0.000 | 4.02e-05 |  149 |
| T-scale-2pct | clean-300 | 0.0498 | 1.0400 | 0.8430 | 1.100 | 0.250 | 0.000 | 2.08e-05 |  149 |
| A-contours | poor-100 | 0.6280 | 0.1500 | 0.9790 | 0.543 | 0.729 | 0.779 | 3.89e-01 | 2220 |
| B-potrace | poor-100 | 0.6340 | 0.0584 | 0.9290 | 0.705 | 0.663 | 0.459 | 2.79e-01 | 6780 |
| C-centerline | poor-100 | 0.5540 | 0.0929 | 0.0566 | 2.200 | 0.766 | 0.000 | 4.82e-01 | 1580 |
| T-folds-as-cuts | poor-100 | 0.3920 | 0.3310 | 1.0000 | 0.000 | 0.350 | 0.000 | 4.02e-05 |  149 |
| T-jitter-0.4mm | poor-100 | 0.3580 | 0.3520 | 1.0000 | 0.306 | 1.000 | 0.000 | 3.32e-01 |  149 |
| T-open-gap | poor-100 | 0.3930 | 0.3310 | 0.0000 | NA | 1.000 | 0.000 | 4.02e-05 |  155 |
| T-oracle | poor-100 | 0.3920 | 0.3310 | 1.0000 | 0.000 | 1.000 | 0.000 | 4.02e-05 |  149 |
| T-scale-2pct | poor-100 | 0.1130 | 0.9010 | 0.8430 | 1.100 | 0.250 | 0.000 | 2.08e-05 |  149 |
| A-contours | scan-150 | 0.5940 | 0.1660 | 1.0000 | 0.349 | 0.807 | 0.873 | 2.21e-01 | 2660 |
| B-potrace | scan-150 | 0.6150 | 0.0410 | 0.9470 | 0.659 | 0.705 | 0.737 | 1.83e-01 | 8120 |
| C-centerline | scan-150 | 0.6600 | 0.0443 | 0.0385 | 0.206 | 0.809 | 0.000 | 3.54e-01 | 1870 |
| T-folds-as-cuts | scan-150 | 0.4410 | 0.3180 | 1.0000 | 0.000 | 0.350 | 0.000 | 4.02e-05 |  149 |
| T-jitter-0.4mm | scan-150 | 0.3080 | 0.3620 | 1.0000 | 0.261 | 0.999 | 0.000 | 3.73e-01 |  149 |
| T-open-gap | scan-150 | 0.4410 | 0.3180 | 0.0000 | NA | 1.000 | 0.000 | 4.02e-05 |  155 |
| T-oracle | scan-150 | 0.4410 | 0.3180 | 1.0000 | 0.000 | 1.000 | 0.000 | 4.02e-05 |  149 |
| T-scale-2pct | scan-150 | 0.0628 | 1.0200 | 0.8430 | 1.100 | 0.250 | 0.000 | 2.08e-05 |  149 |

## Spearman correlation, visual vs fabrication metrics

| group | fabrication | raster_iou | chamfer_mm | hausdorff95_mm |
|---|---|---|---|---|
| existing methods | F1_closed |  0.02220 |  0.1570 |  0.1170 |
| existing methods | F2_dim_mm | -0.01780 |  0.0609 |  0.1430 |
| existing methods | F3_macro_f1 |  0.28400 | -0.2190 | -0.2870 |
| existing methods | F4_duplicate_contours |  0.00970 |  0.0947 |  0.0817 |
| existing methods | F4_extra_contours |  0.07620 |  0.0945 |  0.1150 |
| existing methods | F4_fragments_per_fold |  0.28100 | -0.3290 | -0.3230 |
| existing methods | F5_match_diff_mm | -0.36200 |  0.5450 |  0.5600 |
| perturbed truth | F1_closed |  0.00884 | -0.1010 | -0.0325 |
| perturbed truth | F2_dim_mm | -0.86900 |  0.6830 |  0.3290 |
| perturbed truth | F3_macro_f1 |  0.53700 | -0.4900 | -0.2370 |
| perturbed truth | F4_duplicate_contours | NA | NA | NA |
| perturbed truth | F4_extra_contours | -0.16200 |  0.1610 |  0.0859 |
| perturbed truth | F4_fragments_per_fold | NA | NA | NA |
| perturbed truth | F5_match_diff_mm | -0.38800 | -0.0160 | -0.1530 |
