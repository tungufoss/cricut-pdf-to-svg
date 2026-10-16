# Fold the traced pattern back into the 3D model (prototype, src/lowpoly_pdf_to_svg/fold3d.py).
#   make -f fold3d.mk          data/<project>/<project>-3d.obj (+ .mtl), -3d.png preview,
#                              -3d-glue.csv: every glued edge, its gap in the folded model and status,
#                              and -3d-baseline.csv: triangles and corners against the YAML `reference:`
#   make -f fold3d.mk install  extra Python dependencies (scipy, shapely, matplotlib)
# Needs data/<project>/<project>.svg from a full `make` first.

PYTHON  ?= python3
CONFIG  ?= data/bowser/bowser.yaml
PROJECT ?= $(basename $(notdir $(CONFIG)))
OUT     ?= $(patsubst %/,%,$(dir $(CONFIG)))

.PHONY: fold3d install
fold3d: $(OUT)/$(PROJECT)-3d.obj

$(OUT)/$(PROJECT)-3d.obj: $(OUT)/$(PROJECT).svg src/lowpoly_pdf_to_svg/fold3d.py
	$(PYTHON) -m src.lowpoly_pdf_to_svg.fold3d --config $(CONFIG)

install:
	$(PYTHON) -m pip install -r requirements-fold3d.txt
