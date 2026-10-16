# Shared helpers for reading the pipeline's edge table (data/<project>/edge-numbers.csv).
# One row per printed edge number; `status` is decided by the pipeline, the report only groups it.

suppressPackageStartupMessages({
  library(dplyr)
  library(forcats)
  library(ggplot2)
  library(purrr)
  library(readr)
  library(stringr)
  library(tibble)
  library(tidyr)
})

# "ok" means the number was found on two pieces whose glue edges match.
# Everything else is a reason to look at the piece again.
STATUS_LEVELS <- c("ok", "length mismatch", "both tabs", "no tab", "unpaired",
                   "line not found", "printed 3 times", "printed 4 times")

read_edges <- function(path) {
  read_csv(path, col_types = cols(number = col_character(), .default = col_guess()),
           na = c("", "NA")) |>
    mutate(
      page = as.integer(str_sub(piece, 7, 8)),
      ocr_trusted = ocr_trusted == "yes",
      status = fct_relevel(factor(status), intersect(STATUS_LEVELS, unique(status))),
      verdict = if_else(status == "ok", "matching", "needs work")
    )
}

# One row per glue pair: the two printed edges of a number side by side.
# Numbers without a partner (unpaired, printed 3+ times) keep an empty B side.
glue_pairs <- function(edges) {
  paired <- edges |>
    filter(!is.na(partner_piece), piece < partner_piece | (piece == partner_piece & side <= partner_side)) |>
    distinct(number, piece, partner_piece, .keep_all = TRUE)
  single <- edges |> filter(is.na(partner_piece))
  bind_rows(paired, single) |>
    transmute(number, verdict, status,
              piece_a = piece, side_a = side, length_a = length_mm,
              piece_b = partner_piece, side_b = partner_side, length_b = partner_length_mm,
              diff_mm = length_diff_mm,
              ocr_a = if_else(ocr_trusted, "read", "unsure")) |>
    arrange(verdict != "needs work", status, suppressWarnings(as.integer(number)), number)
}
