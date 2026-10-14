# Cricut PDF to SVG

A local tool for converting papercraft PDF pages into Cricut-oriented SVG paths. It detects every piece, its mountain and valley folds and its edge numbers, and writes the whole template as one Inkscape file for review. Sheet nesting is future work.

## Convert the Bowser template

The source PDF is kept locally at `data/bowser.pdf` and is ignored by Git. The manifest at `data/bowser.yaml` maps its pages to cardstock materials. Install Python 3.10 or newer and Poppler (`pdftoppm`), then from the repository root run:

```sh
make install
make                 # all pages -> output/bowser/bowser.svg
make page PAGE=4     # one page -> output/bowser/page-4/bowser.svg
```

Without `make`, run the same steps directly:

```sh
python -m pip install -r requirements.txt
python -m src.cricut_pdf_svg --config data/bowser.yaml
python -m src.cricut_pdf_svg --config data/bowser.yaml --page 4 --output output/bowser/page-4
```

If Poppler is not on `PATH`, add `--pdftoppm C:\path\to\pdftoppm.exe`.

## Pipeline

Each stage is a class in `src/cricut_pdf_svg/`:

| Stage | Module | What it does |
| --- | --- | --- |
| Manifest | `config.py` | Reads the YAML: source PDF, sheet size, pages per cardstock. |
| Render | `render.py` | Renders each page with `pdftoppm` at 180 dpi; the PNG is kept in `output/<project>/previews/`. |
| Detect | `detect.py` | Separates grey cut lines, dashed folds and black edge numbers. Piece interiors are areas enclosed by cut lines; folds are found with a Hough transform, joined across numbers printed on them, classified as mountain (dash-dot) or valley (dashed), and snapped to the cut vertices they end on. Numbers are traced to single centerlines for the Cricut pen. |
| Model | `model.py` | `Piece`, `Fold`, `Label` and `PageLayout`, in page pixels. |
| Write | `svg.py` | One Inkscape SVG for the whole project, in millimetres. |

## Reviewing in Inkscape

`bowser.svg` needs Inkscape 1.2 or newer. Every PDF page is an Inkscape page laid out left to right at its true size (US Letter for this source). The layers are:

- **Source**: the rendered scans, locked and faint, to compare traces against.
- **Pieces**, with one sublayer per cardstock: each piece is one group named like `piece-04-03`, holding its `Cut` outline, `Score` folds (`Mountain folds` dash-dot blue, `Valley folds` dashed green) and `Draw` edge numbers. The group carries `data-material` for later nesting.
- **Review** (hidden): artwork outside every piece, such as credits, instructions or an outline the detector could not close. Move anything that belongs to a piece into it.

Pieces whose folds could not be tied to a cut vertex are labelled `⚠ check folds` and the fold path has `data-review="unsnapped"`. Search for them with Edit > Find. Before uploading to Design Space, delete the Source and Review layers, then assign Score to the fold paths and Draw/Pen to the number paths and attach them to each cut outline.

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
