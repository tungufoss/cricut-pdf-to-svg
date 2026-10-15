# Papercraft PDF -> Inkscape review SVG.
# Each model keeps everything in data/<project>/: PDF, YAML, SVG, edge table and README.
#   make            convert every page in the manifest into data/<project>/<project>.svg
#   make page PAGE=4  convert one page into output/<project>/page-4/ (quick check while tuning)
#   make install    install Python dependencies (Poppler's pdftoppm comes from the OS)
#   make clean      remove generated files (keeps the PDF and YAML)

PYTHON  ?= python3
CONFIG  ?= data/bowser/bowser.yaml
PROJECT ?= $(basename $(notdir $(CONFIG)))
OUT     ?= $(patsubst %/,%,$(dir $(CONFIG)))
DPI     ?= 180
SOURCES := $(wildcard src/lowpoly_pdf_to_svg/*.py)
CONVERT  = $(PYTHON) -m src.lowpoly_pdf_to_svg --config $(CONFIG) --output $(OUT) --dpi $(DPI)

.PHONY: all page install clean

all: $(OUT)/$(PROJECT).svg

$(OUT)/$(PROJECT).svg: $(CONFIG) $(SOURCES)
	$(CONVERT)

page:
	@test -n "$(PAGE)" || { echo "usage: make page PAGE=4"; exit 2; }
	$(CONVERT) --page $(PAGE) --output output/$(PROJECT)/page-$(PAGE)

install:
	$(PYTHON) -m pip install -r requirements.txt

clean:
	rm -rf $(OUT)/previews $(OUT)/$(PROJECT).svg $(OUT)/$(PROJECT)-edges.csv $(OUT)/README.md output/$(PROJECT)

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
