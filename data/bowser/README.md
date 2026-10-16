# Bowser

1573 printed numbers on 178 pieces. 756 numbers form a clean pair (one plain edge, one tab, lengths within 1 mm); 61 labels need a look.

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
| numbers | 1573 read, 150 uncertain (orange in the SVG) |
| pieces to check | 95 marked ⚠ in Inkscape |
| paper colour | footers disagree with the YAML: pages 14–23 say beige (YAML: yellow); page 24 says white (YAML: black) |
| nesting on sheets | not started |

## Edge numbers

| status | labels | meaning |
|---|---:|---|
| ok | 1512 | partner found, one tab and one plain edge, same length |
| unpaired | 24 | no other copy of this number: likely misread |
| extra copy: likely misread | 16 | number read more than twice; the other copies already form a clean pair |
| length mismatch | 12 | partner found but the marked lines differ in length: misread number or traced line |
| both tabs | 6 | both copies sit on a tab fold |
| printed 3 times | 3 | number read more than twice: some are misread |

## Pages

| page | config material | footer says | pieces | ok | check |
|---|---|---|---:|---:|---:|
| 04 | red | red | 8 | 73 | 2 |
| 05 | red | red | 8 | 74 | 1 |
| 06 | red | red | 6 | 53 | 6 |
| 07 | red | red | 10 | 71 | 5 |
| 08 | red | red | 6 | 52 | 4 |
| 09 | red | red | 7 | 52 | 6 |
| 10 | red | red | 7 | 52 | 2 |
| 11 | green | green | 11 | 85 | 5 |
| 12 | green | green | 11 | 84 | 6 |
| 13 | green | green | 4 | 29 | 1 |
| 14 | yellow | beige ⚠ | 10 | 90 | 2 |
| 15 | yellow | beige ⚠ | 10 | 90 | 2 |
| 16 | yellow | beige ⚠ | 10 | 88 | 5 |
| 17 | yellow | beige ⚠ | 10 | 90 | 3 |
| 18 | yellow | beige ⚠ | 8 | 81 | 1 |
| 19 | yellow | beige ⚠ | 8 | 81 | 1 |
| 20 | yellow | beige ⚠ | 8 | 74 | 2 |
| 21 | yellow | beige ⚠ | 8 | 76 | 0 |
| 22 | yellow | beige ⚠ | 6 | 56 | 2 |
| 23 | yellow | beige ⚠ | 6 | 58 | 0 |
| 24 | black | white ⚠ | 16 | 103 | 5 |

## Pieces to check

Pieces listed by how many of their numbers need a look.

| piece | ok | check | numbers to check |
|---|---:|---:|---|
| piece-12-04 | 6 | 4 | 2 (unpaired), 03 (unpaired), 5 (unpaired), 593 (printed 3 times) |
| piece-12-06 | 6 | 2 | 593 (printed 3 times), 594 (unpaired) |
| piece-06-03 | 9 | 2 | 316 (length mismatch), 386 (unpaired) |
| piece-11-05 | 8 | 2 | 791 (unpaired), 793 (unpaired) |
| piece-09-04 | 7 | 2 | 259 (extra copy: likely misread), 286 (length mismatch) |
| piece-07-01 | 8 | 2 | 273 (both tabs), 672 (unpaired) |
| piece-09-01 | 6 | 2 | 657 (unpaired), 683 (unpaired) |
| piece-17-06 | 3 | 1 | 628 (extra copy: likely misread) |
| piece-17-07 | 5 | 1 | 730 (unpaired) |
| piece-04-02 | 11 | 1 | 6 (unpaired) |
| piece-11-03 | 8 | 1 | 14 (both tabs) |
| piece-24-03 | 6 | 1 | 789 (unpaired) |
| piece-11-07 | 6 | 1 | 14 (both tabs) |
| piece-06-02 | 8 | 1 | 865 (unpaired) |
| piece-06-01 | 8 | 1 | 356 (extra copy: likely misread) |
| piece-06-06 | 9 | 1 | 316 (length mismatch) |
| piece-07-07 | 9 | 1 | 273 (both tabs) |
| piece-05-07 | 8 | 1 | 792 (unpaired) |
| piece-24-04 | 7 | 1 | 794 (unpaired) |
| piece-20-07 | 8 | 1 | 80 (extra copy: likely misread) |
| piece-20-06 | 11 | 1 | 80 (extra copy: likely misread) |
| piece-16-04 | 14 | 1 | 286 (length mismatch) |
| piece-11-06 | 7 | 1 | 790 (unpaired) |
| piece-16-09 | 11 | 1 | 162 (extra copy: likely misread) |
| piece-14-07 | 10 | 1 | 260 (extra copy: likely misread) |
| piece-24-08 | 5 | 1 | 268 (extra copy: likely misread) |
| piece-18-04 | 7 | 1 | 192 (unpaired) |
| piece-24-07 | 7 | 1 | 785 (unpaired) |
| piece-16-07 | 5 | 1 | 376 (unpaired) |
| piece-14-03 | 7 | 1 | 280 (extra copy: likely misread) |
| piece-16-10 | 8 | 1 | 378 (length mismatch) |
| piece-16-02 | 8 | 1 | 378 (length mismatch) |
| piece-08-05 | 8 | 1 | 305 (both tabs) |
| piece-09-05 | 7 | 1 | 295 (extra copy: likely misread) |
| piece-08-06 | 7 | 1 | 305 (both tabs) |
| piece-08-04 | 10 | 1 | 698 (length mismatch) |
| piece-10-05 | 7 | 1 | 885 (unpaired) |
| piece-13-04 | 4 | 1 | 593 (printed 3 times) |
| piece-08-01 | 10 | 1 | 588 (extra copy: likely misread) |
| piece-06-04 | 10 | 1 | 369 (extra copy: likely misread) |
| piece-04-07 | 8 | 1 | 784 (unpaired) |
| piece-19-03 | 7 | 1 | 551 (length mismatch) |
| piece-24-09 | 6 | 1 | 786 (extra copy: likely misread) |
| piece-15-10 | 10 | 1 | 527 (length mismatch) |
| piece-17-10 | 11 | 1 | 551 (length mismatch) |
| piece-15-08 | 13 | 1 | 527 (length mismatch) |
| piece-07-03 | 8 | 1 | 556 (unpaired) |
| piece-22-02 | 6 | 1 | 580 (extra copy: likely misread) |
| piece-22-01 | 10 | 1 | 680 (extra copy: likely misread) |
| piece-07-02 | 5 | 1 | 685 (extra copy: likely misread) |
| piece-09-03 | 8 | 1 | 887 (unpaired) |
| piece-10-04 | 6 | 1 | 698 (length mismatch) |

## Hand corrections that still do not pair

623 numbers were set by hand; 33 of them still do not form a clean pair, so the correction, its partner or the traced line is likely off. They come first on the check page.

| piece | number | side | mm | status | partner | partner mm |
|---|---|---|---:|---|---|---:|
| piece-12-04 | 2 | tab | 15.2 | unpaired |   |  |
| piece-12-04 | 03 | tab | 17.8 | unpaired |   |  |
| piece-12-04 | 5 | tab | 16.8 | unpaired |   |  |
| piece-11-03 | 14 | tab | 9.6 | both tabs | piece-11-07 tab | 9.6 |
| piece-11-07 | 14 | tab | 9.6 | both tabs | piece-11-03 tab | 9.6 |
| piece-20-06 | 80 | tab | 32.2 | extra copy: likely misread |   |  |
| piece-20-07 | 80 | edge | 32.3 | extra copy: likely misread |   |  |
| piece-18-04 | 192 | edge | 39.5 | unpaired |   |  |
| piece-24-08 | 268 | tab | 13.3 | extra copy: likely misread |   |  |
| piece-07-01 | 273 | tab | 17.1 | both tabs | piece-07-07 tab | 17.0 |
| piece-07-07 | 273 | tab | 17.0 | both tabs | piece-07-01 tab | 17.1 |
| piece-09-04 | 286 | tab | 51.8 | length mismatch | piece-16-04 edge | 13.8 |
| piece-16-04 | 286 | edge | 13.8 | length mismatch | piece-09-04 tab | 51.8 |
| piece-09-05 | 295 | edge | 51.3 | extra copy: likely misread |   |  |
| piece-08-05 | 305 | tab | 29.7 | both tabs | piece-08-06 tab | 29.7 |
| piece-08-06 | 305 | tab | 29.7 | both tabs | piece-08-05 tab | 29.7 |
| piece-06-03 | 316 | edge | 37.3 | length mismatch | piece-06-06 tab | 38.3 |
| piece-06-06 | 316 | tab | 38.3 | length mismatch | piece-06-03 edge | 37.3 |
| piece-16-07 | 376 | tab | 26.2 | unpaired |   |  |
| piece-16-10 | 378 | edge | 26.3 | length mismatch | piece-16-02 tab | 27.8 |
| piece-06-03 | 386 | edge | 42.5 | unpaired |   |  |
| piece-22-02 | 580 | tab | 46.0 | extra copy: likely misread |   |  |
| piece-12-04 | 593 | edge | 12.4 | printed 3 times |   |  |
| piece-12-06 | 593 | edge | 10.8 | printed 3 times |   |  |
| piece-12-06 | 594 | tab | 24.1 | unpaired |   |  |
| piece-09-01 | 657 | edge | 42.3 | unpaired |   |  |
| piece-22-01 | 680 | edge | 46.0 | extra copy: likely misread |   |  |
| piece-09-01 | 683 | tab | 55.2 | unpaired |   |  |
| piece-24-07 | 785 | edge | 15.4 | unpaired |   |  |
| piece-24-03 | 789 | edge | 18.1 | unpaired |   |  |
| piece-11-06 | 790 | edge | 24.2 | unpaired |   |  |
| piece-11-05 | 791 | edge | 15.8 | unpaired |   |  |
| piece-05-07 | 792 | edge | 24.3 | unpaired |   |  |

## Mirror twins

The model is symmetric: 89 pairs of pieces are mirror images (178 of 178 pieces), found by the lengths of their numbered lines: 6 exact mirrors (outline and tabs match) and 83 mirror variations (same body, tabs on other edges). Of their {paired} mirrored lines, {off} differ in length from their mirror line by more than 1 mm, so one of the two was traced off (`bowser-mirrors.csv`). A twin's clean glue pair also predicts the number on the mirror line; those predictions are applied when clear-cut, and otherwise go to the check page with `mirror` as the reason.


## Likely misreads

8 clear-cut misreads were fixed without asking (marked `applied` in `bowser-misreads.csv`). 10 more numbers that did not pair up sit on a line of the same length as another unpaired number on the other side (edge against tab), and the two numbers look alike. Check them with `make fix` and `app/number-check.html`.

| piece | side | mm | read | suggested | partner | partner mm | why |
|---|---|---:|---|---|---|---:|---|
| piece-16-07 | tab | 26.2 | 376 | 378 | piece-16-10 edge | 26.3 | OCR's other reading |
| piece-10-05 | edge | 42.3 | 885 | 887 | piece-09-03 tab | 42.2 | one digit differs |
| piece-17-06 | edge | 59.2 | 628 | 698 | piece-10-04 tab | 59.3 | one digit differs; the read number already pairs elsewhere |
| piece-22-02 | tab | 46.0 | 580 | 680 | piece-22-01 edge | 46.0 | OCR's other reading; the read number already pairs elsewhere |
| piece-14-03 | edge | 32.6 | 280 | 260 | piece-14-07 tab | 32.5 | one digit differs; the read number already pairs elsewhere |
| piece-16-09 | tab | 39.7 | 162 | 192 | piece-18-04 edge | 39.5 | one digit differs; the read number already pairs elsewhere |
| piece-09-05 | edge | 51.3 | 295 | 286 | piece-09-04 tab | 51.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-24-08 | tab | 13.3 | 268 | 286 | piece-16-04 edge | 13.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-06-04 | tab | 43.2 | 369 | 386 | piece-06-03 edge | 42.5 | OCR's other reading; the read number already pairs elsewhere |
| piece-12-04 | tab | 16.8 | 5 | 6 | piece-04-02 edge | 17.7 | one digit differs |

Full tables: `bowser-edges.csv`, `bowser-misreads.csv`.
