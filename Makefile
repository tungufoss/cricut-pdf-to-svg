# Papercraft PDF -> Inkscape review SVG.
# Each model keeps everything in data/<project>/: PDF, YAML, SVG, edge table and README.
#   make            convert every page in the manifest into data/<project>/<project>.svg
#   make page PAGE=4  convert one page into output/<project>/page-4/ (quick check while tuning)
#   make piece PIECE=piece-05-08  one piece over its scan, numbers coloured by pair check,
#                   in data/<project>/pieces/ (needs a full `make` first)
#   make redo PAGES="5 11"  trace only those pages again, reuse the saved trace of the rest;
#                    make redo with no PAGES only redraws the SVG and redoes the edge check (seconds)
#   make number NUMBER=20  every piece carrying that number, PDF beside trace, in data/<project>/review.png
#   make fix        data/<project>/check-page.json for app/number-check.html: check each unpaired number
#                   against the scan, accept or type the right one; Save writes number-corrections.csv
#   make install    install Python dependencies (Poppler's pdftoppm comes from the OS)
#   make example    regenerate data/example/example.pdf from bench/synth.py (needs scipy, shapely, cairosvg)
#   make clean      remove generated files (keeps the PDF and YAML)

PYTHON  ?= python3
# The public repository ships a synthetic example; a real model lives in its own folder (or
# repository) and is passed in, e.g. make CONFIG=/path/to/data/<model>/<model>.yaml
CONFIG  ?= data/example/example.yaml
PROJECT ?= $(basename $(notdir $(CONFIG)))
OUT     ?= $(patsubst %/,%,$(dir $(CONFIG)))
DPI     ?= 180
SOURCES := $(wildcard src/lowpoly_pdf_to_svg/*.py)
CONVERT  = $(PYTHON) -m src.lowpoly_pdf_to_svg --config $(CONFIG) --output $(OUT) --dpi $(DPI)

.PHONY: all page redo piece number fix example install clean

all: $(OUT)/$(PROJECT).svg

$(OUT)/$(PROJECT).svg: $(CONFIG) $(SOURCES) $(wildcard $(OUT)/number-corrections.csv $(OUT)/number-lines.csv $(OUT)/piece-edits.csv $(OUT)/fold3d-moves.csv)
	$(CONVERT)

page:
	@test -n "$(PAGE)" || { echo "usage: make page PAGE=4"; exit 2; }
	$(CONVERT) --page $(PAGE) --output output/$(PROJECT)/page-$(PAGE)

redo:
	@test -d $(OUT)/cache || { echo "run make first"; exit 2; }
	$(CONVERT) --redo $(PAGES)

piece:
	@test -n "$(PIECE)" || { echo "usage: make piece PIECE=piece-05-08"; exit 2; }
	@test -f $(OUT)/$(PROJECT).svg || { echo "run make first"; exit 2; }
	$(PYTHON) -m src.lowpoly_pdf_to_svg.piece --config $(CONFIG) $(PIECE)

number:
	@test -n "$(NUMBER)" || { echo "usage: make number NUMBER=20"; exit 2; }
	@test -f $(OUT)/$(PROJECT).svg || { echo "run make first"; exit 2; }
	$(PYTHON) -m src.lowpoly_pdf_to_svg.piece --config $(CONFIG) --number $(NUMBER)

fix:
	@test -f $(OUT)/number-misreads.csv || { echo "run make first"; exit 2; }
	$(PYTHON) -m src.lowpoly_pdf_to_svg.fixer --config $(CONFIG) --dpi $(DPI)

# A synthetic template with exact ground truth: one A4 page, cut lines grey like the real
# templates (the reader tells numbers from lines by darkness), numbers black.
EXAMPLE_SEED ?= 7
example:
	$(PYTHON) -m bench.synth --out output/example --templates 1 --seed $(EXAMPLE_SEED)
	$(PYTHON) -c "import cairosvg, pathlib; s = pathlib.Path('output/example/synth-$(shell printf %02d $(EXAMPLE_SEED))-01/page-01.svg'); \
	  cairosvg.svg2pdf(bytestring=s.read_text().replace('stroke=\"black\"', 'stroke=\"#7f7f7f\"', 1).encode(), write_to='data/example/example.pdf')"

install:
	$(PYTHON) -m pip install -r requirements.txt

clean:
	rm -rf $(OUT)/previews $(OUT)/$(PROJECT).svg $(OUT)/edge-numbers.csv $(OUT)/number-misreads.csv $(OUT)/README.md $(OUT)/pieces $(OUT)/cache $(OUT)/review.png $(OUT)/check-page.json output/$(PROJECT)

# Results site (Quarto website in report/, R with tidyverse, xml2 and DT).
#   make report     render report/_site/index.html from the current output
.PHONY: report
report: $(OUT)/$(PROJECT).svg
	LC_ALL=C.UTF-8 REPORT_OUT=$(abspath $(OUT)) REPORT_PROJECT=$(PROJECT) quarto render report
#   make preview    serve it on localhost and re-render on save
.PHONY: preview
preview: $(OUT)/$(PROJECT).svg
	LC_ALL=C.UTF-8 REPORT_OUT=$(abspath $(OUT)) REPORT_PROJECT=$(PROJECT) quarto preview report

# Paper 1 benchmark (bench/): synthetic templates with exact ground truth, existing
# vectorizers, shared cut/fold classifier, conventional and fabrication-aware metrics.
#   make bench-data   synthetic templates and degraded rasters in bench/out/
#   make bench        every method on every page and condition -> bench/results.csv
#   make bench-report summary tables and correlations (R, tidyverse) -> bench/summary/
BENCH_TEMPLATES ?= 12
BENCH_SEED      ?= 1
.PHONY: bench-data bench bench-report
bench-data:
	$(PYTHON) -m bench.synth --out bench/out --templates $(BENCH_TEMPLATES) --seed $(BENCH_SEED)
bench: bench-data
	$(PYTHON) -m bench --data bench/out --out bench/results.csv
bench-report:
	Rscript bench/analysis.R bench/results.csv bench/summary

# Paper 1 (Quarto article in paper/, quarto-hi template). Not part of the public site.
#   make paper      render paper/_output/index.html and index.pdf (quarto-hi article look)
.PHONY: paper
paper:
	cd paper && LC_ALL=C.UTF-8 quarto render   # from paper/ so font-paths: fonts resolves
