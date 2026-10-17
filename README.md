# Low Poly PDF to SVG

Turns low poly papercraft PDF templates into one Inkscape SVG, ready for review and Cricut Design Space: every piece is a group with its cut outline, score lines for folds and pen-drawn edge numbers, tagged with its cardstock colour.

```sh
make install   # Python deps; also needs Poppler (pdftoppm) and Tesseract
make           # data/example/example.pdf -> data/example/example.svg (a synthetic template)
make CONFIG=/path/to/data/<model>/<model>.yaml   # your own template
make report    # results site in report/_site (needs Quarto and R with tidyverse, xml2, DT)
```

Your own source PDFs stay local and are not committed; only the synthetic example is.

Everything else, from the pipeline stages and reviewing in Inkscape to sheet-by-sheet results and the glue-pair check, is on the project site: <https://tungufoss.github.io/lowpoly-pdf-to-svg/> (built from `report/`).

## Folded model and 2D/3D mapping

After tracing a project SVG, generate its folded OBJ and viewer data with:

```sh
make -f fold3d.mk CONFIG=data/<project>/<project>.yaml
```

The target writes `fold3d.obj` and `fold3d.mtl`, a PNG preview, glue and inspection CSV files,
and `fold3d.json`. The JSON is the correspondence data for `app/fold3d-viewer.html`: each entry
in `faces` has an `id` such as `piece-04-01/0`, its SVG piece ID, the folded OBJ vertex indices
(`v`), and the same face corners in the SVG's flat document coordinates (`flat`, in millimetres).
Each OBJ face is emitted in this same piece and face order. The viewer uses that shared identity to
highlight the matching piece in both views; `glues` carries the paired edge numbers and folded gap
status. This JSON is generated from the traced SVG and folded geometry, so regenerate it whenever
the source SVG or fold corrections change.

To inspect the correspondence locally, run `make -f fold3d.mk view` after the fold finishes and
open the URL printed by Make. The viewer is static HTML and needs no server-side component.

## Credit

The Bowser papercraft mask is by [Sweets The Cat](https://sweetsthecat.itch.io/), free for personal use; this repository does not redistribute the PDF. 3D model on [Sketchfab](https://sketchfab.com/3d-models/papercraft-bowser-mask-92627b8a93c941b89dad9f6ab62a8fe9).

![Bowser papercraft mask preview](assets/bowser-preview.png)
