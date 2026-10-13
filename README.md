# Cricut PDF to SVG

A tool for turning papercraft PDF templates into grouped, Cricut-ready SVG layouts. The repository is in the planning stage; the converter and nesting workflow are not implemented yet.

## Intended workflow

- Convert PDF pages into usable vector paths, including paths traced from raster artwork where needed.
- Keep each paper piece as a movable item group with a cardstock color attribute.
- Separate operations inside each group: solid cut paths, dashed score paths for folds, and pen-drawn number labels that match assembly edges.
- Nest whole item groups by cardstock color onto configured sheets, initially 12 × 12 inch or A4, while reducing waste and preventing overlap.
- Export SVGs organized by material and sheet for review and Cricut Design Space.

Cricut Design Space imports SVG vectors as Cut by default. After import, assign the fold layer to Score and the number layer to Draw/Pen, then attach them to the matching cut pieces. See [Cricut's SVG upload guide](https://help.cricut.com/hc/en-us/articles/360009556313-How-to-upload-images-into-Design-Space) and [operation guide](https://help.cricut.com/hc/en-us/articles/26922998476183-Design-Space-Selecting-Operation).

See PLAN.md for the proposed development stages.

## Bowser papercraft credit

The Bowser papercraft mask was created by Sweets The Cat (also credited as Papercraft Cat) as a Halloween project. The creator's Sketchfab model page says the free template was available through the creator's itch.io papercraft shop. Sketchfab is the model reference; itch.io is the creator's stated distribution source. Paperzone VN hosts a community repost with a ZIP attachment and is a mirror, not the original creator source.

- Creator shop: [Sweets The Cat on itch.io](https://sweetsthecat.itch.io/)
- Interactive 3D model: [Papercraft Bowser Mask by Sweets The Cat on Sketchfab](https://sketchfab.com/3d-models/papercraft-bowser-mask-92627b8a93c941b89dad9f6ab62a8fe9)
- Community mirror/download thread: [Paperzone VN](https://paperzonevn.com/bowser-mask.t13095/)

GitHub's README renderer does not display the interactive Sketchfab iframe, so the model is linked above. An embedded viewer would need a separate HTML page hosted with GitHub Pages.

The creator described the template as free for personal use. This repository does not include or redistribute the PDF. Check the creator's current terms before using or sharing derived files.

## Bowser papercraft example

![Bowser papercraft mask preview](assets/bowser-preview.png)
