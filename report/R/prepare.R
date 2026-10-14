#!/usr/bin/env Rscript
# Quarto pre-render step: gather the conversion results the report shows into generated/.
#
#   generated/sheets/<project>-page-PP.svg   one sheet of the review SVG (pieces only),
#                                             edge numbers ringed green (ok) or red (needs work)
#   generated/sheets/<project>-page-PP-<material>.png   the rendered PDF page, from previews/
#   generated/sheets.csv                     one row per sheet, read by sheets.qmd
#   generated/edges.csv, summary.md          the pipeline's edge table and summary, as is
#
# Inputs come from REPORT_OUT (default ../output/bowser); `make report` sets it.

suppressPackageStartupMessages(library(xml2))
source("R/edges.R")

out <- Sys.getenv("REPORT_OUT", "../output/bowser")
project <- Sys.getenv("REPORT_PROJECT", basename(out))
gen <- "generated"
svg_path <- file.path(out, paste0(project, ".svg"))
edges_path <- file.path(out, paste0(project, "-edges.csv"))
stopifnot("run `make` first: review SVG not found" = file.exists(svg_path))

unlink(gen, recursive = TRUE)
dir.create(file.path(gen, "sheets"), recursive = TRUE)

NS <- c(svg = "http://www.w3.org/2000/svg",
        inkscape = "http://www.inkscape.org/namespaces/inkscape",
        sodipodi = "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd")
RING <- c(matching = "#1a9e8f", `needs work` = "#d61f69")

edges <- if (file.exists(edges_path)) read_edges(edges_path) else NULL
if (!is.null(edges)) invisible(file.copy(edges_path, file.path(gen, "edges.csv")))
summary_md <- file.path(out, paste0(project, "-report.md"))
if (file.exists(summary_md)) invisible(file.copy(summary_md, file.path(gen, "summary.md")))

# Sheet geometry comes from the Inkscape pages in the review SVG (all in mm).
pages <- read_xml(svg_path) |>
  xml_find_all("//inkscape:page", NS) |>
  map(xml_attrs) |>
  map_dfr(as_tibble_row) |>
  transmute(page = as.integer(str_extract(id, "\\d+")),
            label = str_remove(label, "^Page \\d+ \\S+ "),
            across(c(x, y, width, height), as.numeric))

# Cut one sheet out of the review SVG: keep its own pieces, drop the source and review layers,
# and crop the viewBox to the page. Edge numbers are ringed at their page position.
write_sheet <- function(page, x, width, height, ...) {
  doc <- read_xml(svg_path)
  xml_find_all(doc, "/svg:svg/*[not(self::svg:title) and not(@id='pieces')]", NS) |> xml_remove()
  xml_find_all(doc, sprintf("//svg:g[@data-material and not(starts-with(@id, 'piece-%02d-'))]", page), NS) |>
    xml_remove()
  root <- xml_root(doc)
  xml_set_attr(root, "width", sprintf("%.3fmm", width))
  xml_set_attr(root, "height", sprintf("%.3fmm", height))
  xml_set_attr(root, "viewBox", sprintf("%.3f 0 %.3f %.3f", x, width, height))
  xml_add_child(root, "rect", x = x, y = 0, width = width, height = height, fill = "#ffffff", .where = 0)

  if (!is.null(edges)) {
    rings <- xml_add_child(root, "g", id = "edge-rings", style = "fill:none;stroke-width:0.6")
    edges |>
      filter(page == !!page) |>
      pwalk(function(x_mm, y_mm, verdict, number, status, ...) {
        ring <- xml_add_child(rings, "circle", cx = sprintf("%.2f", x + x_mm), cy = sprintf("%.2f", y_mm),
                              r = "4.5", stroke = RING[[verdict]])
        xml_add_child(ring, "title", paste0(number, ": ", status))
      })
  }
  file <- file.path(gen, "sheets", sprintf("%s-page-%02d.svg", project, page))
  write_xml(doc, file)
  file
}

sources <- list.files(file.path(out, "previews"), pattern = "\\.png$", full.names = TRUE)
source_for <- function(page) {
  hit <- str_subset(sources, sprintf("-page-%02d-", page))
  if (length(hit) == 0) return(NA_character_)
  dest <- file.path(gen, "sheets", basename(hit[1]))
  file.copy(hit[1], dest)
  dest
}

counts <- if (is.null(edges)) tibble(page = integer()) else
  edges |> count(page, verdict) |> pivot_wider(names_from = verdict, values_from = n, values_fill = 0)

sheets <- pages |>
  mutate(after = pmap_chr(pages, write_sheet),
         before = map_chr(page, source_for)) |>
  left_join(counts, by = "page")

write_csv(sheets, file.path(gen, "sheets.csv"))
message(sprintf("prepared %d sheets in %s", nrow(sheets), gen))
