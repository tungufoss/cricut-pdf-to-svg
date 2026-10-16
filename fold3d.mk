# Fold the traced pattern back into the 3D model (prototype, src/lowpoly_pdf_to_svg/fold3d.py).
#   make -f fold3d.mk          data/<project>/fold3d.obj (+ .mtl), fold3d.png preview,
#                              fold3d-glue.csv: every glued edge, its gap in the folded model and status,
#                              fold3d-baseline.csv: triangles and corners against the YAML `reference:`,
#                              fold3d-moves.csv: corners 0.2-1 mm off as `move` rows (piece-edits.csv columns)
#                              and fold3d-inspect.csv: pieces to look at by eye (corner >1 mm off, glue open)
#   make -f fold3d.mk install  extra Python dependencies (scipy, shapely, matplotlib)
# Needs data/<project>/<project>.svg from a full `make` first.

PYTHON  ?= python3
CONFIG  ?= data/example/example.yaml
PROJECT ?= $(basename $(notdir $(CONFIG)))
OUT     ?= $(patsubst %/,%,$(dir $(CONFIG)))

.PHONY: fold3d install
fold3d: $(OUT)/fold3d.obj

$(OUT)/fold3d.obj: $(OUT)/$(PROJECT).svg src/lowpoly_pdf_to_svg/fold3d.py
	$(PYTHON) -m src.lowpoly_pdf_to_svg.fold3d --config $(CONFIG)

install:
	$(PYTHON) -m pip install -r requirements-fold3d.txt
