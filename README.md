# Low Poly PDF to SVG

Turns low poly papercraft PDF templates into one Inkscape SVG, ready for review and Cricut Design Space: every piece is a group with its cut outline, score lines for folds and pen-drawn edge numbers, tagged with its cardstock colour.

```sh
make install   # Python deps; also needs Poppler (pdftoppm) and Tesseract
make           # data/bowser/bowser.pdf -> data/bowser/bowser.svg
make report    # results site in report/_site (needs Quarto and R with tidyverse, xml2, DT)
```

The source PDF stays local in `data/` and is not committed.

Everything else, from the pipeline stages and reviewing in Inkscape to sheet-by-sheet results and the glue-pair check, is on the project site: <https://tungufoss.github.io/lowpoly-pdf-to-svg/> (built from `report/`).

## Credit

The Bowser papercraft mask is by [Sweets The Cat](https://sweetsthecat.itch.io/), free for personal use; this repository does not redistribute the PDF. 3D model on [Sketchfab](https://sketchfab.com/3d-models/papercraft-bowser-mask-92627b8a93c941b89dad9f6ab62a8fe9).

![Bowser papercraft mask preview](assets/bowser-preview.png)
