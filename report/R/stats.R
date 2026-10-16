#!/usr/bin/env Rscript
# Summary statistics for the public site: `make report-data` runs
#   Rscript report/R/stats.R data/<project> report/data/<project>
# It reads a model's own tables (edges, corrections, misreads, mirrors, checks, 3D glue) and
# writes only counts and binned distributions, so report/data/ holds no traced geometry and no
# per-edge rows. A 3D preview render (fold3d.png), when present, is copied as the one
# static image. Review what it wrote before committing it.

suppressPackageStartupMessages({
  library(dplyr)
  library(purrr)
  library(readr)
  library(tibble)
  library(tidyr)
  library(yaml)
})

args <- commandArgs(trailingOnly = TRUE)
src <- args[1]
dest <- args[2]
project <- basename(normalizePath(src))
dir.create(dest, recursive = TRUE, showWarnings = FALSE)

read_if <- function(name) {
  path <- file.path(src, paste0(name, ".csv"))
  if (file.exists(path)) read_csv(path, col_types = cols(.default = col_character()), na = c("", "NA"))
}
num <- function(x) suppressWarnings(as.numeric(x))
put <- function(df, name) write_csv(df, file.path(dest, paste0(name, ".csv")), na = "")

edges <- read_if("edge-numbers")
if (is.null(edges)) stop("no edge-numbers.csv in ", src)
corrections <- read_if("number-corrections")
misreads <- read_if("number-misreads")
mirrors <- read_if("mirror-mismatches")
checks <- read_if("trace-faults")
glue <- read_if("fold3d-glue")
pieces_fix <- read_if("piece-edits")
lines_fix <- read_if("number-lines")

edges <- edges |>
  mutate(page = as.integer(substr(piece, 7, 8)),
         verdict = if_else(status == "ok", "matching", "needs work"))

# Cardstock per page, from the manifest
manifest <- read_yaml(file.path(src, paste0(project, ".yaml")))
cardstock <- map_dfr(manifest$materials, \(m) tibble(page = as.integer(m$pages), cardstock = m$name))

edges |> count(status, verdict) |> put("status")

edges |>
  count(page, verdict) |>
  complete(page, verdict = c("matching", "needs work"), fill = list(n = 0)) |>
  pivot_wider(names_from = verdict, values_from = n) |>
  left_join(cardstock, by = "page") |>
  transmute(page, cardstock, matching, needs_work = `needs work`) |>
  put("pages")

# The numbers that still need a look, by page and reason
edges |>
  filter(verdict == "needs work") |>
  count(page, status) |>
  put("open")

# Where each final reading came from: the readers, the program, or a person
empty <- tibble(piece = character(), x_mm = character(), y_mm = character())
applied <- if (is.null(misreads)) mutate(empty, why = character()) else filter(misreads, sure == "applied")
hand <- if (is.null(corrections)) mutate(empty, read = character(), number = character()) else corrections
edges |>
  left_join(transmute(hand, piece, x_mm, y_mm, hand_read = read, hand_number = number),
            by = c("piece", "x_mm", "y_mm")) |>
  left_join(transmute(applied, piece, x_mm, y_mm, auto = TRUE), by = c("piece", "x_mm", "y_mm")) |>
  mutate(source = case_when(
    !is.na(hand_number) & hand_read == hand_number ~ "person confirmed",
    !is.na(hand_number) | corrected %in% "yes" ~ "person changed",
    !is.na(auto) ~ "fixed by the program",
    ocr_trusted == "yes" ~ "readers sure",
    TRUE ~ "readers unsure"),
    outcome = if_else(status == "ok", "pairs (ok)", "still open")) |>
  count(source, outcome) |>
  put("provenance")

tally <- function(x) if (length(x) == 0) "none" else paste(names(table(x)), table(x), collapse = ", ")
closed <- if (!is.null(glue)) filter(glue, grepl("closes", status))
by_mirror <- sum(grepl("^mirror", applied$why))
numbers <- list(
  project = project,
  numbers = nrow(edges),
  pieces = n_distinct(edges$piece),
  pages = n_distinct(edges$page),
  matching = sum(edges$verdict == "matching"),
  needs_work = sum(edges$verdict == "needs work"),
  ocr_sure = sum(edges$ocr_trusted == "yes"),
  auto_fixed = nrow(applied),
  auto_lookalike = nrow(applied) - by_mirror,
  auto_mirror = by_mirror,
  mirror_lines = if (is.null(mirrors)) 0L else nrow(mirrors),
  mirror_exact = if (is.null(mirrors)) 0L else sum(mirrors$mirror == "exact"),
  mirror_differ = if (is.null(mirrors)) 0L else sum(mirrors$check != "ok"),
  trace_faults = if (is.null(checks)) 0L else nrow(checks),
  cards_answered = nrow(hand),
  cards_changed = sum(hand$read != hand$number),
  piece_edits = if (is.null(pieces_fix)) 0L else nrow(pieces_fix),
  piece_edits_by_action = tally(pieces_fix$action),
  lines_drawn = if (is.null(lines_fix)) 0L else nrow(lines_fix),
  lines_by_kind = tally(lines_fix$kind),
  glue_total = if (is.null(glue)) NA else nrow(glue),
  glue_closes = if (is.null(glue)) NA else nrow(closed),
  glue_median_gap_mm = if (is.null(glue)) NA else round(median(num(closed$gap_mm), na.rm = TRUE), 2)
)
tibble(key = names(numbers), value = map_chr(numbers, \(v) if (is.na(v)) NA_character_ else as.character(v))) |>
  put("numbers")

if (!is.null(glue)) {
  glue |> count(status) |> put("glue-status")
  # Gap histogram in log10 bins of 0.2 (gaps below 0.05 mm count as 0.05)
  glue |>
    filter(!is.na(gap_mm)) |>
    mutate(gap_bin = floor(log10(pmax(num(gap_mm), 0.05)) * 5) / 5) |>
    count(gap_bin, status) |>
    put("glue-gaps")
}

render <- file.path(src, "fold3d.png")
if (file.exists(render)) file.copy(render, file.path(dest, basename(render)), overwrite = TRUE)
message("wrote summary statistics for ", project, " to ", dest)
