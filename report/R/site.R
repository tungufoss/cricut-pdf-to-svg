# Readers for the committed summary statistics in report/data/<project>/ (written by
# R/stats.R through `make report-data`). The public site is built from these alone.

suppressPackageStartupMessages({
  library(dplyr)
  library(forcats)
  library(ggplot2)
  library(readr)
  library(stringr)
  library(tibble)
  library(tidyr)
})

site_project <- function() {
  p <- Sys.getenv("REPORT_PROJECT")
  if (nzchar(p)) return(p)
  dirs <- list.dirs("data", full.names = FALSE, recursive = FALSE)
  if (length(dirs)) dirs[1] else NA_character_
}
PROJECT <- site_project()
STATS <- file.path("data", PROJECT)

stat_table <- function(name) {
  path <- file.path(STATS, paste0(name, ".csv"))
  if (!is.na(PROJECT) && file.exists(path)) read_csv(path, show_col_types = FALSE, na = "")
}
NUMBERS <- stat_table("numbers")
stat <- function(key) {
  if (is.null(NUMBERS)) return(NA)
  v <- NUMBERS$value[NUMBERS$key == key]
  if (length(v) == 0 || is.na(v)) return(NA)
  n <- suppressWarnings(as.numeric(v))
  if (is.na(n)) v else n
}
VERDICT_COLOURS <- c(matching = "#1a9e8f", `needs work` = "#d61f69")
