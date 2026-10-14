# Papercraft PDF -> Inkscape review SVG.
#   make            convert every page in the manifest into output/<project>/<project>.svg
#   make page PAGE=4  convert one page (quick check while tuning detection)
#   make install    install Python dependencies (Poppler's pdftoppm comes from the OS)
#   make clean      remove generated output

PYTHON  ?= python3
CONFIG  ?= data/bowser.yaml
PROJECT ?= $(basename $(notdir $(CONFIG)))
OUT     ?= output/$(PROJECT)
DPI     ?= 180
SOURCES := $(wildcard src/lowpoly_pdf_to_svg/*.py)
CONVERT  = $(PYTHON) -m src.lowpoly_pdf_to_svg --config $(CONFIG) --output $(OUT) --dpi $(DPI)

.PHONY: all page install clean

all: $(OUT)/$(PROJECT).svg

$(OUT)/$(PROJECT).svg: $(CONFIG) $(SOURCES)
	$(CONVERT)

page:
	@test -n "$(PAGE)" || { echo "usage: make page PAGE=4"; exit 2; }
	$(CONVERT) --page $(PAGE) --output $(OUT)/page-$(PAGE)

install:
	$(PYTHON) -m pip install -r requirements.txt

clean:
	rm -rf $(OUT)
