# Paper 1 analysis: do conventional vectorization metrics agree with fabrication-aware ones?
#   Rscript bench/analysis.R bench/results.csv bench/summary
# Writes methods.csv (mean per method and condition), correlations.csv (Spearman between
# every visual and every fabrication metric over method x page x condition) and summary.md.

suppressPackageStartupMessages({
  library(dplyr)
  library(tidyr)
  library(readr)
})

args <- commandArgs(trailingOnly = TRUE)
input <- if (length(args) >= 1) args[1] else "bench/results.csv"
outdir <- if (length(args) >= 2) args[2] else "bench/summary"
dir.create(outdir, showWarnings = FALSE, recursive = TRUE)

visual <- c("raster_iou", "chamfer_mm", "hausdorff95_mm")
fabrication <- c("F1_closed", "F2_dim_mm", "F3_macro_f1", "F4_duplicate_contours",
                 "F4_extra_contours", "F4_fragments_per_fold", "F5_match_diff_mm")
complexity <- c("paths", "controls", "svg_bytes")

results <- read_csv(input, show_col_types = FALSE)

wide <- results |>
  pivot_wider(names_from = metric, values_from = value)

methods <- results |>
  filter(metric %in% c(visual, fabrication, complexity)) |>
  group_by(method, condition, metric) |>
  summarise(mean = mean(value, na.rm = TRUE), .groups = "drop") |>
  pivot_wider(names_from = metric, values_from = mean) |>
  select(method, condition, any_of(c(visual, fabrication, complexity))) |>
  arrange(condition, method)
write_csv(methods, file.path(outdir, "methods.csv"))

correlations <- expand_grid(visual = visual, fabrication = fabrication) |>
  rowwise() |>
  mutate(
    n = sum(complete.cases(wide[[visual]], wide[[fabrication]])),
    spearman = suppressWarnings(cor(wide[[visual]], wide[[fabrication]],
                                    method = "spearman", use = "complete.obs"))
  ) |>
  ungroup()
write_csv(correlations, file.path(outdir, "correlations.csv"))

fmt <- function(df) {
  df <- mutate(df, across(where(is.numeric), \(x) signif(x, 3)))
  header <- paste0("| ", paste(names(df), collapse = " | "), " |")
  rule <- paste0("|", paste(rep("---", ncol(df)), collapse = "|"), "|")
  rows <- apply(df, 1, \(r) paste0("| ", paste(r, collapse = " | "), " |"))
  c(header, rule, rows)
}

lines <- c(
  "# Benchmark summary", "",
  sprintf("%d templates, %d pages, %d conditions, %d methods.",
          n_distinct(results$template), n_distinct(paste(results$template, results$page)),
          n_distinct(results$condition), n_distinct(results$method)), "",
  "## Mean per method and condition", "",
  fmt(select(methods, method, condition, raster_iou, chamfer_mm, F1_closed, F2_dim_mm,
             F3_macro_f1, F4_duplicate_contours, F5_match_diff_mm, controls)), "",
  "## Spearman correlation, visual vs fabrication metrics", "",
  fmt(correlations |> select(visual, fabrication, spearman) |>
        pivot_wider(names_from = visual, values_from = spearman))
)
writeLines(lines, file.path(outdir, "summary.md"))
cat(sprintf("wrote %s\n", outdir))
