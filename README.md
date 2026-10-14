# Cricut PDF to SVG

A local tool for converting papercraft PDF pages into Cricut-oriented SVG paths. The first Bowser converter is implemented; visual correction, piece grouping, and sheet nesting remain future work.

## Convert the Bowser template

The source PDF is kept locally at `data/bowser.pdf` and is ignored by Git. The manifest at `data/bowser.yaml` maps its pages to cardstock materials. Install Python 3.10 or newer and Poppler (`pdftoppm`), then from the repository root run:

```powershell
python -m pip install -r requirements.txt
python -m src.cricut_pdf_svg --config data/bowser.yaml
```

The converter writes one SVG for each page assigned in the manifest under `output/bowser/`, plus rendered review images under `output/bowser/previews/`. SVGs use the PDF page's original physical size (US Letter for this source) and contain named Cut, Score, and Draw groups. The Draw group is empty because the edge numbers need recognition and matching; add or correct them manually before cutting. The fold classification is heuristic and must also be reviewed against the preview.

To convert just one page while reviewing the output:

```powershell
python -m src.cricut_pdf_svg --config data/bowser.yaml --page 4
```

If Poppler is not on `PATH`, pass its executable explicitly with `--pdftoppm C:\path\to\pdftoppm.exe`. The exporter preserves source-page scale; it does not yet regroup individual pieces or nest them onto the manifest's A4 sheet. Before cutting, compare every SVG with its preview, confirm the Cut and Score paths, add the edge-number Draw paths, then set Cricut operations and attach each item's operations in Design Space.

## Intended workflow

- Convert PDF pages into usable vector paths, including paths traced from raster artwork where needed.
- Keep each paper piece as a movable item group with a cardstock color attribute.
- Separate operations inside each group: solid cut paths, dashed score paths for folds, and pen-drawn number labels that match assembly edges.
- Nest whole item groups by cardstock color onto configured sheets, initially 12 × 12 inch or A4, while reducing waste and preventing overlap.
- Export SVGs organized by material and sheet for review and Cricut Design Space.

Cricut Design Space imports SVG vectors as Cut by default. After import, assign the fold layer to Score and the number layer to Draw/Pen, then attach them to the matching cut pieces. See [Cricut's SVG upload guide](https://help.cricut.com/hc/en-us/articles/360009556313-How-to-upload-images-into-Design-Space) and [operation guide](https://help.cricut.com/hc/en-us/articles/26922998476183-Design-Space-Selecting-Operation).

See PLAN.md for the remaining development stages.

## Bowser papercraft credit

The Bowser papercraft mask was created by Sweets The Cat (also credited as Papercraft Cat) as a Halloween project. The creator's Sketchfab model page says the free template was available through the creator's itch.io papercraft shop. Sketchfab is the model reference; itch.io is the creator's stated distribution source. Paperzone VN hosts a community repost with a ZIP attachment and is a mirror, not the original creator source.

- Creator shop: [Sweets The Cat on itch.io](https://sweetsthecat.itch.io/)
- Interactive 3D model: [Papercraft Bowser Mask by Sweets The Cat on Sketchfab](https://sketchfab.com/3d-models/papercraft-bowser-mask-92627b8a93c941b89dad9f6ab62a8fe9)
- Community mirror/download thread: [Paperzone VN](https://paperzonevn.com/bowser-mask.t13095/)

GitHub's README renderer does not display the interactive Sketchfab iframe, so the model is linked above. An embedded viewer would need a separate HTML page hosted with GitHub Pages.

The creator described the template as free for personal use. This repository does not include or redistribute the PDF. Check the creator's current terms before using or sharing derived files.

## Bowser papercraft example

![Bowser papercraft mask preview](assets/bowser-preview.png)
