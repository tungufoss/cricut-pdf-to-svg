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
# HÍ palette, as in styles/hi-site.scss (honnun.hi.is)
HI <- c(blue = "#10099F", teal = "#2DD2C0", yellow = "#FAC55B", orange = "#FFA05F",
        red = "#FC8484", pink = "#d61f69", green = "#00FFBA", dark = "#0A0668", grey = "#5D6872")
VERDICT_COLOURS <- c(matching = HI[["blue"]], `needs work` = HI[["orange"]])
scale_colour_hi <- function(...) scale_colour_manual(values = unname(HI), ...)
scale_fill_hi <- function(...) scale_fill_manual(values = unname(HI), ...)
theme_hi <- function(...) {
  theme_minimal(...) +
    theme(text = element_text(colour = "#262626"), plot.title = element_text(colour = HI[["blue"]]),
          strip.text = element_text(colour = HI[["blue"]], face = "bold"), legend.position = "top")
}
