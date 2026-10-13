# Development Plan

## Goal

Turn papercraft PDFs into Cricut-ready, material-aware SVG sheets. The first release targets raster pattern PDFs like the Bowser example and uses automatic detection followed by human review and correction.

## Proposed product direction

Use a local-first tool with a visual review step. A command-line-only utility would be faster to build but awkward for correcting traced paths and matching edge numbers. A hosted web app would make sharing easier but would require uploading source PDFs. A local interface keeps source files on the user's computer and supports the correction workflow this project needs. Choose the exact UI and processing stack after a small prototype.

## User workflow

1. Open a PDF and choose the paper sheet size, starting with 12 × 12 inch and A4.
2. Render pages at their physical dimensions and detect likely cut boundaries, dashed fold lines, and printed edge numbers.
3. Review and correct detected geometry and labels. Confirm which paths and edge numbers belong to each item.
4. Group each item's cut, fold, and number layers together; assign the cardstock color to the item group.
5. Arrange whole item groups by color on sheets. Permit rotation where configured, keep spacing between parts, and reject layouts that clip or overlap.
6. Export one SVG per material and sheet, with real-world dimensions and named groups for items and Cricut operations.
7. Import into Design Space, assign Score to fold paths and Draw/Pen to number labels, then attach those operations to their corresponding cut pieces.

## Delivery stages

### 1. Sample-page prototype

Use a user-downloaded copy of the Bowser PDF locally, not in the repository. Confirm page rendering, physical scale, image quality, and detection quality on one pattern page. Test solid boundaries, dashed folds, and rotated edge numbers. Establish how uncertain detections are flagged for review.

### 2. Detection and correction

Build the review flow for editing cut contours and fold paths, correcting or pairing printed edge numbers, grouping paths into items, and assigning cardstock colors. Keep the detected result editable until the user approves it.

### 3. Item model and sheet nesting

Represent every piece as one movable group with cut geometry, fold geometry, pen labels, stable identifiers, and a material/color attribute. Add sheet selection, margins, part spacing, optional rotation, and a 2D nesting step that minimizes unused area without overlap or clipping.

### 4. Cricut SVG export

Write SVGs with explicit physical dimensions and separate named groups for cut, score, and draw operations within each item group. Export by cardstock color and selected sheet size. Preserve numbering and item grouping. Since Design Space imports SVG vectors as Cut by default, document and streamline the required Score/Draw assignment and Attach steps.

### 5. Validation and release

Check output dimensions and path bounds, warn about unsupported SVG features or excessive path counts, and compare SVG previews with source pages. Test imports in Design Space and make a physical sample cut before calling the workflow ready.

## Acceptance outcomes

- A raster PDF can be opened and converted into editable cut, fold, and pen-label paths.
- Users can correct automatic detection before export.
- Every item stays grouped with its matching fold and number paths and retains its cardstock color.
- Same-color item groups fit the chosen 12 × 12 inch or A4 sheet without overlap or clipping.
- SVG scale and geometry match the source PDF, and Cricut operation layers remain easy to identify and assign.

## Risks and boundaries

- Raster quality, skew, compression, and similar line styles may make automatic detection uncertain; the review step is required.
- Number recognition and matching may need user correction, especially for rotated text and repeated edge IDs.
- The initial goal is a local workflow for raster pattern PDFs. Hosted processing, automatic attribution of colors from arbitrary instructions, and perfect one-click Cricut operation assignment are not assumed.
- The Bowser PDF is not stored in this repository. Obtain it from the creator's source or the clearly labeled community mirror in README.md, and follow the creator's current terms.
