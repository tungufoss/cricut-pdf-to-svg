# Papercraft PDF -> Inkscape review SVG.
# Each model keeps everything in data/<project>/: PDF, YAML, SVG, edge table and README.
#   make            convert every page in the manifest into data/<project>/<project>.svg
#   make page PAGE=4  convert one page into output/<project>/page-4/ (quick check while tuning)
#   make piece PIECE=piece-05-08  one piece over its scan, numbers coloured by pair check,
#                   in data/<project>/pieces/ (needs a full `make` first)
#   make redo PAGES="5 11"  trace only those pages again, reuse the saved trace of the rest;
#                    make redo with no PAGES only redraws the SVG and redoes the edge check (seconds)
#   make number NUMBER=20  every piece carrying that number, PDF beside trace, in data/<project>/review.png
#   make fix        data/<project>/<project>-check.json for app/number-check.html: check each unpaired number
#                   against the scan, accept or type the right one; Save writes <project>-corrections.csv
#   make install    install Python dependencies (Poppler's pdftoppm comes from the OS)
#   make clean      remove generated files (keeps the PDF and YAML)

PYTHON  ?= python3
CONFIG  ?= data/bowser/bowser.yaml
PROJECT ?= $(basename $(notdir $(CONFIG)))
OUT     ?= $(patsubst %/,%,$(dir $(CONFIG)))
DPI     ?= 180
SOURCES := $(wildcard src/lowpoly_pdf_to_svg/*.py)
CONVERT  = $(PYTHON) -m src.lowpoly_pdf_to_svg --config $(CONFIG) --output $(OUT) --dpi $(DPI)

.PHONY: all page redo piece number fix install clean

all: $(OUT)/$(PROJECT).svg

$(OUT)/$(PROJECT).svg: $(CONFIG) $(SOURCES) $(wildcard $(OUT)/$(PROJECT)-corrections.csv $(OUT)/$(PROJECT)-lines.csv $(OUT)/$(PROJECT)-pieces.csv)
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
	@test -f $(OUT)/$(PROJECT)-misreads.csv || { echo "run make first"; exit 2; }
	$(PYTHON) -m src.lowpoly_pdf_to_svg.fixer --config $(CONFIG) --dpi $(DPI)

install:
	$(PYTHON) -m pip install -r requirements.txt

clean:
	rm -rf $(OUT)/previews $(OUT)/$(PROJECT).svg $(OUT)/$(PROJECT)-edges.csv $(OUT)/$(PROJECT)-misreads.csv $(OUT)/README.md $(OUT)/pieces $(OUT)/cache $(OUT)/review.png $(OUT)/$(PROJECT)-check.json output/$(PROJECT)

# Results site (Quarto website in report/, R with tidyverse, xml2 and DT).
#   make report     render report/_site/index.html from the current output
.PHONY: report
report: $(OUT)/$(PROJECT).svg
	LC_ALL=C.UTF-8 REPORT_OUT=$(abspath $(OUT)) REPORT_PROJECT=$(PROJECT) quarto render report
#   make preview    serve it on localhost and re-render on save
.PHONY: preview
preview: $(OUT)/$(PROJECT).svg
	LC_ALL=C.UTF-8 REPORT_OUT=$(abspath $(OUT)) REPORT_PROJECT=$(PROJECT) quarto preview report
#   make report-data  copy the edge table and summary into report/data/ for GitHub Pages
#                     (the SVG and scans stay local: the pattern is free for personal use only)
.PHONY: report-data
report-data: $(OUT)/$(PROJECT).svg
	mkdir -p report/data/$(PROJECT)
	cp $(OUT)/$(PROJECT)-edges.csv report/data/$(PROJECT)/
	cp $(OUT)/README.md report/data/$(PROJECT)/$(PROJECT)-report.md
