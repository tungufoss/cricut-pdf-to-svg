# Fold the traced pattern back into the 3D model (prototype, src/lowpoly_pdf_to_svg/fold3d.py).
#   make -f fold3d.mk          data/<project>/<project>-3d.obj (+ .mtl), -3d.png preview,
#                              -3d-glue.csv: every glued edge, its gap in the folded model and status,
#                              -3d-baseline.csv: triangles and corners against the YAML `reference:`,
#                              -3d-moves.csv: corners 0.2-1 mm off as `move` rows (bowser-pieces.csv columns)
#                              and -3d-inspect.csv: pieces to look at by eye (corner >1 mm off, glue open)
#                              and -3d.json for the viewer
#   make -f fold3d.mk view     serve app/fold3d-viewer.html on localhost: the glued model beside the
#                              pattern, click a face in either to find it in the other (local only)
#   make -f fold3d.mk install  extra Python dependencies (scipy, shapely, matplotlib)
# Needs data/<project>/<project>.svg from a full `make` first.

PYTHON  ?= python3
CONFIG  ?= data/bowser/bowser.yaml
PROJECT ?= $(basename $(notdir $(CONFIG)))
OUT     ?= $(patsubst %/,%,$(dir $(CONFIG)))

PORT    ?= 8000

.PHONY: fold3d install view
fold3d: $(OUT)/$(PROJECT)-3d.obj

$(OUT)/$(PROJECT)-3d.obj: $(OUT)/$(PROJECT).svg src/lowpoly_pdf_to_svg/fold3d.py
	$(PYTHON) -m src.lowpoly_pdf_to_svg.fold3d --config $(CONFIG)

install:
	$(PYTHON) -m pip install -r requirements-fold3d.txt

view:   # no rebuild: the fold takes about half an hour, run `make -f fold3d.mk` first
	@echo "Open http://localhost:$(PORT)/app/fold3d-viewer.html?json=../$(OUT)/$(PROJECT)-3d.json&svg=../$(OUT)/$(PROJECT).svg"
	$(PYTHON) -m http.server $(PORT) --bind 127.0.0.1
