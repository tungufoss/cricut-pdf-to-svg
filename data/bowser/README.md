# Bowser

1573 printed numbers on 178 pieces. 769 numbers form a clean pair (one plain edge, one tab, lengths within 1 mm); 35 labels need a look.

Conversion status (2026-10-16), written by `make`. Edit the YAML, not this file.

## Files

| file | what | in git |
|---|---|---|
| `bowser.pdf` | source template | no, personal use only |
| `bowser.yaml` | pages per cardstock, fold styles, sheet size | yes |
| `bowser.svg` | Inkscape review file, one row of pages per cardstock | no, traced pattern |
| `previews/` | rendered PDF pages, the SVG's faint Source layer | no |
| `bowser-edges.csv` | every printed edge number with its line and partner | yes |
| `bowser-misreads.csv` | unpaired numbers matched by length to a look-alike number | yes |
| `README.md` | this status page | yes |

## Status

| stage | result |
|---|---|
| pages | 21 converted |
| pieces | 178 cut outlines, corners joined by straight edges |
| folds | 1543, 0 stretched far to reach the cut |
| numbers | 1573 read, 127 uncertain (orange in the SVG) |
| pieces to check | 82 marked ⚠ in Inkscape |
| paper colour | footers disagree with the YAML: pages 14–23 say beige (YAML: yellow); page 24 says white (YAML: black) |
| nesting on sheets | not started |

## Edge numbers

| status | labels | meaning |
|---|---:|---|
| ok | 1538 | partner found, one tab and one plain edge, same length |
| unpaired | 18 | no other copy of this number: likely misread |
| extra copy: likely misread | 12 | number read more than twice; the other copies already form a clean pair |
| printed 3 times | 3 | number read more than twice: some are misread |
| length mismatch | 2 | partner found but the marked lines differ in length: misread number or traced line |

## Pages

| page | config material | footer says | pieces | ok | check |
|---|---|---|---:|---:|---:|
| 04 | red | red | 8 | 74 | 1 |
| 05 | red | red | 8 | 74 | 1 |
| 06 | red | red | 6 | 57 | 2 |
| 07 | red | red | 10 | 73 | 3 |
| 08 | red | red | 6 | 54 | 2 |
| 09 | red | red | 7 | 52 | 6 |
| 10 | red | red | 7 | 53 | 1 |
| 11 | green | green | 11 | 87 | 3 |
| 12 | green | green | 11 | 85 | 5 |
| 13 | green | green | 4 | 29 | 1 |
| 14 | yellow | beige ⚠ | 10 | 92 | 0 |
| 15 | yellow | beige ⚠ | 10 | 90 | 2 |
| 16 | yellow | beige ⚠ | 10 | 92 | 1 |
| 17 | yellow | beige ⚠ | 10 | 91 | 2 |
| 18 | yellow | beige ⚠ | 8 | 82 | 0 |
| 19 | yellow | beige ⚠ | 8 | 81 | 1 |
| 20 | yellow | beige ⚠ | 8 | 76 | 0 |
| 21 | yellow | beige ⚠ | 8 | 76 | 0 |
| 22 | yellow | beige ⚠ | 6 | 58 | 0 |
| 23 | yellow | beige ⚠ | 6 | 58 | 0 |
| 24 | black | white ⚠ | 16 | 104 | 4 |

## Pieces to check

Pieces listed by how many of their numbers need a look.

| piece | ok | check | numbers to check |
|---|---:|---:|---|
| piece-12-04 | 7 | 3 | 2 (unpaired), 5 (unpaired), 593 (printed 3 times) |
| piece-12-06 | 6 | 2 | 593 (printed 3 times), 594 (unpaired) |
| piece-11-05 | 8 | 2 | 791 (unpaired), 793 (unpaired) |
| piece-09-04 | 7 | 2 | 286 (extra copy: likely misread), 289 (extra copy: likely misread) |
| piece-09-01 | 6 | 2 | 657 (unpaired), 683 (unpaired) |
| piece-17-07 | 5 | 1 | 730 (unpaired) |
| piece-24-03 | 6 | 1 | 789 (unpaired) |
| piece-06-03 | 10 | 1 | 386 (unpaired) |
| piece-05-07 | 8 | 1 | 792 (unpaired) |
| piece-24-04 | 7 | 1 | 794 (unpaired) |
| piece-11-06 | 7 | 1 | 790 (unpaired) |
| piece-24-07 | 7 | 1 | 785 (unpaired) |
| piece-15-06 | 10 | 1 | 580 (extra copy: likely misread) |
| piece-07-01 | 9 | 1 | 672 (unpaired) |
| piece-16-02 | 8 | 1 | 378 (unpaired) |
| piece-10-05 | 7 | 1 | 289 (extra copy: likely misread) |
| piece-09-05 | 7 | 1 | 296 (extra copy: likely misread) |
| piece-08-04 | 10 | 1 | 698 (extra copy: likely misread) |
| piece-13-04 | 4 | 1 | 593 (printed 3 times) |
| piece-08-01 | 10 | 1 | 588 (extra copy: likely misread) |
| piece-06-04 | 10 | 1 | 369 (extra copy: likely misread) |
| piece-04-07 | 8 | 1 | 784 (unpaired) |
| piece-19-03 | 7 | 1 | 551 (length mismatch) |
| piece-24-09 | 6 | 1 | 786 (extra copy: likely misread) |
| piece-15-07 | 9 | 1 | 580 (extra copy: likely misread) |
| piece-17-10 | 11 | 1 | 551 (length mismatch) |
| piece-07-03 | 8 | 1 | 556 (extra copy: likely misread) |
| piece-07-02 | 5 | 1 | 685 (extra copy: likely misread) |
| piece-09-03 | 8 | 1 | 887 (unpaired) |

## Hand corrections that still do not pair

641 numbers were set by hand; 19 of them still do not form a clean pair, so the correction, its partner or the traced line is likely off. They come first on the check page.

| piece | number | side | mm | status | partner | partner mm |
|---|---|---|---:|---|---|---:|
| piece-12-04 | 2 | tab | 15.2 | unpaired |   |  |
| piece-12-04 | 5 | tab | 16.8 | unpaired |   |  |
| piece-09-04 | 286 | tab | 51.8 | extra copy: likely misread |   |  |
| piece-09-04 | 289 | tab | 42.1 | extra copy: likely misread |   |  |
| piece-10-05 | 289 | edge | 42.3 | extra copy: likely misread |   |  |
| piece-09-05 | 296 | edge | 51.3 | extra copy: likely misread |   |  |
| piece-06-03 | 386 | edge | 42.5 | unpaired |   |  |
| piece-15-06 | 580 | edge | 18.8 | extra copy: likely misread |   |  |
| piece-15-07 | 580 | tab | 18.7 | extra copy: likely misread |   |  |
| piece-12-04 | 593 | edge | 12.4 | printed 3 times |   |  |
| piece-12-06 | 593 | edge | 10.8 | printed 3 times |   |  |
| piece-12-06 | 594 | tab | 24.1 | unpaired |   |  |
| piece-09-01 | 657 | edge | 42.3 | unpaired |   |  |
| piece-09-01 | 683 | tab | 55.2 | unpaired |   |  |
| piece-24-07 | 785 | edge | 15.4 | unpaired |   |  |
| piece-24-03 | 789 | edge | 18.1 | unpaired |   |  |
| piece-11-06 | 790 | edge | 24.2 | unpaired |   |  |
| piece-11-05 | 791 | edge | 15.8 | unpaired |   |  |
| piece-05-07 | 792 | edge | 24.3 | unpaired |   |  |

## Mirror twins

The model is symmetric: 89 pairs of pieces are mirror images (178 of 178 pieces), found by the lengths of their numbered lines: 6 exact mirrors (outline and tabs match) and 83 mirror variations (same body, tabs on other edges). Of their {paired} mirrored lines, {off} differ in length from their mirror line by more than 1 mm, so one of the two was traced off (`bowser-mirrors.csv`). A twin's clean glue pair also predicts the number on the mirror line; those predictions are applied when clear-cut, and otherwise go to the check page with `mirror` as the reason.


## Likely misreads

1 clear-cut misreads were fixed without asking (marked `applied` in `bowser-misreads.csv`). 2 more numbers that did not pair up sit on a line of the same length as another unpaired number on the other side (edge against tab), and the two numbers look alike. Check them with `make fix` and `app/number-check.html`.

| piece | side | mm | read | suggested | partner | partner mm | why |
|---|---|---:|---|---|---|---:|---|
| piece-09-04 | tab | 51.8 | 286 | 296 | piece-09-05 edge | 51.3 | OCR's other reading; the read number already pairs elsewhere |
| piece-06-04 | tab | 43.2 | 369 | 386 | piece-06-03 edge | 42.5 | OCR's other reading; the read number already pairs elsewhere |

Full tables: `bowser-edges.csv`, `bowser-misreads.csv`.
