# Repository Guidelines

## Project Structure & Workflow

This project converts paper craft PDFs into Cricut-ready SVGs. The current root asset, bowser.pdf, is a design input. The planned workflow converts PDF pages to SVG, associates each paper piece with a cardstock color, and nests pieces to reduce waste on available 12 × 12 inch or A4 sheets. Each movable item group keeps its operations together: solid cut paths, dashed fold paths for Cricut scoring, and number labels drawn with Cricut pen. The cardstock color is an attribute of the item group, allowing groups made from the same material to be packed together. Keep source PDFs separate from generated SVGs and document directories added as the project grows.

## Build, Test, and Development

`make` converts every page in `data/bowser.yaml` into one Inkscape review file, `output/bowser/bowser.svg`; `make page PAGE=4` converts a single page for quick checks. The Python package in `src/lowpoly_pdf_to_svg/` keeps each stage (manifest, render, detect, model, SVG writer) in its own module. Preserve source PDFs and make SVGs reproducible. Start by checking a small input.

## Coding and Naming

Use descriptive lowercase kebab-case filenames, such as bowser-page-01.svg. Keep PDF conversion, operation classification, item grouping, color assignment, and sheet nesting as inspectable workflow stages. Make units explicit and record whether a sheet uses 12 × 12 inch or A4 dimensions.

## Quality Checks

There is no automated test suite yet. Check that each SVG opens, has correct physical dimensions, and preserves the source artwork. Confirm each item remains a single movable group with distinct cut, dashed score, and pen-label operations; its number labels match the intended folds or piece; and its cardstock color is retained. Check that same-color groups fit the selected sheet without overlap or clipping, and compare the result with the PDF before cutting.

## Commits and Pull Requests

No commit convention or pull request template is established. Use short imperative subjects, such as Add PDF to SVG conversion. Pull requests should describe the workflow stage changed, affected files, validation performed, and include an SVG or nesting preview when useful.

## Configuration and Safety

Keep original PDFs and reproducible conversion settings. Avoid committing temporary exports, caches, or private data embedded in source documents.
