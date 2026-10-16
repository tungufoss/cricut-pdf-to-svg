# Example

56 printed numbers on 11 pieces. 7 numbers form a clean pair (one plain edge, one tab, lengths within 1 mm); 42 labels need a look.

Conversion status (2026-10-16), written by `make`. Edit the YAML, not this file.

## Files

| file | what | in git |
|---|---|---|
| `example.pdf` | source template | no, personal use only |
| `example.yaml` | pages per cardstock, fold styles, sheet size | yes |
| `example.svg` | Inkscape review file, one row of pages per cardstock | no, traced pattern |
| `previews/` | rendered PDF pages, the SVG's faint Source layer | no |
| `example-edges.csv` | every printed edge number with its line and partner | yes |
| `example-misreads.csv` | unpaired numbers matched by length to a look-alike number | yes |
| `README.md` | this status page | yes |

## Status

| stage | result |
|---|---|
| pages | 1 converted |
| pieces | 11 cut outlines, corners joined by straight edges |
| folds | 42, 0 stretched far to reach the cut |
| numbers | 56 read, 30 uncertain (orange in the SVG) |
| pieces to check | 10 marked ⚠ in Inkscape |
| paper colour | footers agree with the YAML |
| nesting on sheets | not started |

## Edge numbers

| status | labels | meaning |
|---|---:|---|
| unpaired | 24 | no other copy of this number: likely misread |
| ok | 14 | partner found, one tab and one plain edge, same length |
| line not found | 8 | no cut edge or fold next to the number |
| length mismatch | 6 | partner found but the marked lines differ in length: misread number or traced line |
| both tabs | 4 | both copies sit on a tab fold |

## Pages

| page | config material | footer says | pieces | ok | check |
|---|---|---|---:|---:|---:|
| 01 | white | ? | 11 | 14 | 42 |

## Pieces to check

Pieces listed by how many of their numbers need a look.

| piece | ok | check | numbers to check |
|---|---:|---:|---|
| piece-01-03 | 1 | 6 | 14 (length mismatch), 31 (length mismatch), 37 (unpaired), 47 (unpaired), 106 (unpaired), 292 (both tabs) |
| piece-01-04 | 1 | 6 | 93 (unpaired), 239 (unpaired), 292 (both tabs), 300 (line not found), 307 (unpaired), 447 (unpaired) |
| piece-01-06 | 0 | 5 | 02 (unpaired), 194 (unpaired), 198 (unpaired), 236 (unpaired), 771 (line not found) |
| piece-01-02 | 2 | 4 | 13 (unpaired), 17 (length mismatch), 31 (length mismatch), 64 (both tabs) |
| piece-01-05 | 2 | 4 | 15 (unpaired), 64 (both tabs), 117 (unpaired), 300 (line not found) |
| piece-01-01 | 3 | 4 | 39 (unpaired), 41 (unpaired), 295 (line not found), 395 (line not found) |
| piece-01-07 | 2 | 4 | 49 (unpaired), 195 (unpaired), 295 (line not found), 771 (line not found) |
| piece-01-08 | 0 | 4 | 97 (unpaired), 153 (unpaired), 247 (unpaired), 278 (unpaired) |
| piece-01-09 | 1 | 3 | 14 (length mismatch), 17 (length mismatch), 131 (unpaired) |
| piece-01-10 | 1 | 1 | 395 (line not found) |
| piece-01-11 | 1 | 1 | 433 (unpaired) |

## Hand corrections that still do not pair

0 numbers were set by hand; 0 of them still do not form a clean pair, so the correction, its partner or the traced line is likely off. They come first on the check page.

| piece | number | side | mm | status | partner | partner mm |
|---|---|---|---:|---|---|---:|

## Mirror twins

The model is symmetric: 0 pairs of pieces are mirror images (0 of 11 pieces), found by the lengths of their numbered lines: 0 exact mirrors (outline and tabs match) and 0 mirror variations (same body, tabs on other edges). Of their {paired} mirrored lines, {off} differ in length from their mirror line by more than 1 mm, so one of the two was traced off (`example-mirrors.csv`). A twin's clean glue pair also predicts the number on the mirror line; those predictions are applied when clear-cut, and otherwise go to the check page with `mirror` as the reason.


## Likely misreads

1 clear-cut misreads were fixed without asking (marked `applied` in `example-misreads.csv`). 3 more numbers that did not pair up sit on a line of the same length as another unpaired number on the other side (edge against tab), and the two numbers look alike. Check them with `make fix` and `app/number-check.html`.

| piece | side | mm | read | suggested | partner | partner mm | why |
|---|---|---:|---|---|---|---:|---|
| piece-01-02 | tab | 19.6 | 13 | 17 | piece-01-09 edge | 19.5 | one digit differs |
| piece-01-01 | tab | 19.6 | 41 | 47 | piece-01-03 edge | 19.8 | one digit differs |
| piece-01-07 | edge | 17.0 | 195 | 198 | piece-01-06 tab | 17.2 | one digit differs |

Full tables: `example-edges.csv`, `example-misreads.csv`.
