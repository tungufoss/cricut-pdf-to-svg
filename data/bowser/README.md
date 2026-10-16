# Bowser

1574 printed numbers on 178 pieces. 733 numbers form a clean pair (one plain edge, one tab, lengths within 1 mm); 108 labels need a look.

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
| folds | 1538, 0 stretched far to reach the cut |
| numbers | 1574 read, 185 uncertain (orange in the SVG) |
| pieces to check | 109 marked ⚠ in Inkscape |
| paper colour | footers disagree with the YAML: pages 14–23 say beige (YAML: yellow); page 24 says white (YAML: black) |
| nesting on sheets | not started |

## Edge numbers

| status | labels | meaning |
|---|---:|---|
| ok | 1466 | partner found, one tab and one plain edge, same length |
| unpaired | 32 | no other copy of this number: likely misread |
| no tab | 32 | neither copy sits on a tab fold |
| length mismatch | 18 | partner found but the marked lines differ in length: misread number or traced line |
| extra copy: likely misread | 17 | number read more than twice; the other copies already form a clean pair |
| both tabs | 6 | both copies sit on a tab fold |
| printed 3 times | 3 | number read more than twice: some are misread |

## Pages

| page | config material | footer says | pieces | ok | check |
|---|---|---|---:|---:|---:|
| 04 | red | red | 8 | 70 | 5 |
| 05 | red | red | 8 | 72 | 3 |
| 06 | red | red | 6 | 53 | 6 |
| 07 | red | red | 10 | 71 | 5 |
| 08 | red | red | 6 | 52 | 4 |
| 09 | red | red | 7 | 50 | 8 |
| 10 | red | red | 7 | 52 | 2 |
| 11 | green | green | 11 | 83 | 7 |
| 12 | green | green | 11 | 76 | 14 |
| 13 | green | green | 4 | 28 | 2 |
| 14 | yellow | beige ⚠ | 10 | 89 | 3 |
| 15 | yellow | beige ⚠ | 10 | 89 | 3 |
| 16 | yellow | beige ⚠ | 10 | 82 | 11 |
| 17 | yellow | beige ⚠ | 10 | 86 | 7 |
| 18 | yellow | beige ⚠ | 8 | 74 | 8 |
| 19 | yellow | beige ⚠ | 8 | 72 | 10 |
| 20 | yellow | beige ⚠ | 8 | 76 | 0 |
| 21 | yellow | beige ⚠ | 8 | 76 | 0 |
| 22 | yellow | beige ⚠ | 6 | 56 | 2 |
| 23 | yellow | beige ⚠ | 6 | 58 | 0 |
| 24 | black | white ⚠ | 16 | 101 | 8 |

## Pieces to check

Pieces listed by how many of their numbers need a look.

| piece | ok | check | numbers to check |
|---|---:|---:|---|
| piece-12-04 | 5 | 5 | 2 (unpaired), 5 (unpaired), 6 (unpaired), 420 (no tab), 593 (printed 3 times) |
| piece-12-06 | 4 | 4 | 545 (no tab), 546 (unpaired), 593 (printed 3 times), 594 (unpaired) |
| piece-11-05 | 7 | 3 | 58 (no tab), 791 (unpaired), 793 (unpaired) |
| piece-19-04 | 11 | 3 | 398 (no tab), 400 (no tab), 454 (no tab) |
| piece-16-10 | 6 | 3 | 368 (unpaired), 378 (length mismatch), 383 (no tab) |
| piece-19-01 | 5 | 3 | 397 (no tab), 398 (no tab), 400 (no tab) |
| piece-09-01 | 5 | 3 | 657 (unpaired), 683 (unpaired), 685 (length mismatch) |
| piece-06-03 | 9 | 2 | 316 (length mismatch), 386 (length mismatch) |
| piece-18-06 | 9 | 2 | 90 (no tab), 136 (no tab) |
| piece-16-04 | 13 | 2 | 286 (length mismatch), 379 (no tab) |
| piece-16-03 | 12 | 2 | 383 (no tab), 386 (length mismatch) |
| piece-14-07 | 9 | 2 | 260 (extra copy: likely misread), 564 (no tab) |
| piece-12-07 | 5 | 2 | 545 (no tab), 548 (unpaired) |
| piece-09-04 | 7 | 2 | 259 (extra copy: likely misread), 286 (length mismatch) |
| piece-24-05 | 4 | 2 | 261 (extra copy: likely misread), 281 (unpaired) |
| piece-07-01 | 8 | 2 | 273 (both tabs), 672 (unpaired) |
| piece-16-02 | 7 | 2 | 378 (length mismatch), 379 (no tab) |
| piece-04-07 | 7 | 2 | 420 (no tab), 784 (unpaired) |
| piece-19-07 | 9 | 2 | 454 (no tab), 496 (no tab) |
| piece-09-03 | 7 | 2 | 885 (no tab), 887 (unpaired) |
| piece-04-02 | 11 | 1 | 03 (unpaired) |
| piece-11-02 | 8 | 1 | 9 (unpaired) |
| piece-11-03 | 8 | 1 | 14 (both tabs) |
| piece-24-03 | 6 | 1 | 789 (unpaired) |
| piece-11-07 | 6 | 1 | 14 (both tabs) |
| piece-05-02 | 6 | 1 | 040 (unpaired) |
| piece-06-02 | 8 | 1 | 865 (unpaired) |
| piece-06-01 | 8 | 1 | 356 (extra copy: likely misread) |
| piece-06-06 | 9 | 1 | 316 (length mismatch) |
| piece-07-07 | 9 | 1 | 273 (both tabs) |
| piece-05-03 | 11 | 1 | 58 (no tab) |
| piece-05-07 | 8 | 1 | 792 (unpaired) |
| piece-24-04 | 7 | 1 | 794 (unpaired) |
| piece-18-01 | 7 | 1 | 397 (no tab) |
| piece-18-03 | 13 | 1 | 90 (no tab) |
| piece-18-05 | 12 | 1 | 106 (no tab) |
| piece-18-08 | 10 | 1 | 136 (no tab) |
| piece-18-07 | 10 | 1 | 106 (no tab) |
| piece-11-06 | 7 | 1 | 790 (unpaired) |
| piece-12-03 | 8 | 1 | 406 (unpaired) |
| piece-04-03 | 11 | 1 | 456 (extra copy: likely misread) |
| piece-16-09 | 11 | 1 | 162 (extra copy: likely misread) |
| piece-24-08 | 5 | 1 | 268 (extra copy: likely misread) |
| piece-18-04 | 7 | 1 | 192 (unpaired) |
| piece-24-07 | 7 | 1 | 785 (unpaired) |
| piece-15-06 | 10 | 1 | 564 (no tab) |
| piece-04-06 | 7 | 1 | 848 (unpaired) |
| piece-12-10 | 7 | 1 | 645 (unpaired) |
| piece-17-05 | 11 | 1 | 556 (length mismatch) |
| piece-16-07 | 5 | 1 | 376 (unpaired) |
| piece-14-03 | 7 | 1 | 280 (extra copy: likely misread) |
| piece-08-05 | 8 | 1 | 305 (both tabs) |
| piece-09-05 | 7 | 1 | 295 (extra copy: likely misread) |
| piece-08-06 | 7 | 1 | 305 (both tabs) |
| piece-08-04 | 10 | 1 | 698 (length mismatch) |
| piece-10-05 | 7 | 1 | 885 (no tab) |
| piece-13-04 | 4 | 1 | 593 (printed 3 times) |
| piece-08-01 | 10 | 1 | 588 (extra copy: likely misread) |
| piece-06-04 | 10 | 1 | 369 (unpaired) |
| piece-17-03 | 13 | 1 | 732 (no tab) |
| piece-17-07 | 5 | 1 | 730 (unpaired) |
| piece-24-12 | 7 | 1 | 445 (extra copy: likely misread) |
| piece-19-08 | 10 | 1 | 496 (no tab) |
| piece-19-03 | 7 | 1 | 551 (length mismatch) |
| piece-24-09 | 6 | 1 | 786 (extra copy: likely misread) |
| piece-15-10 | 10 | 1 | 527 (length mismatch) |
| piece-17-08 | 6 | 1 | 999 (unpaired) |
| piece-17-10 | 11 | 1 | 551 (length mismatch) |
| piece-15-08 | 13 | 1 | 527 (length mismatch) |
| piece-13-03 | 9 | 1 | 648 (extra copy: likely misread) |
| piece-07-03 | 8 | 1 | 556 (length mismatch) |
| piece-12-11 | 5 | 1 | 648 (extra copy: likely misread) |
| piece-22-02 | 6 | 1 | 580 (extra copy: likely misread) |
| piece-22-01 | 10 | 1 | 680 (extra copy: likely misread) |
| piece-07-02 | 5 | 1 | 685 (length mismatch) |
| piece-17-09 | 8 | 1 | 732 (no tab) |
| piece-17-06 | 3 | 1 | 628 (extra copy: likely misread) |
| piece-10-04 | 6 | 1 | 698 (length mismatch) |

## Hand corrections that still do not pair

542 numbers were set by hand; 53 of them still do not form a clean pair, so the correction, its partner or the traced line is likely off. They come first on the check page.

| piece | number | side | mm | status | partner | partner mm |
|---|---|---|---:|---|---|---:|
| piece-12-04 | 2 | tab | 15.2 | unpaired |   |  |
| piece-12-04 | 5 | tab | 16.8 | unpaired |   |  |
| piece-12-04 | 6 | tab | 17.8 | unpaired |   |  |
| piece-05-02 | 040 | edge | 42.4 | unpaired |   |  |
| piece-05-03 | 58 | edge | 17.8 | no tab | piece-11-05 edge | 17.8 |
| piece-11-05 | 58 | edge | 17.8 | no tab | piece-05-03 edge | 17.8 |
| piece-18-05 | 106 | edge | 17.0 | no tab | piece-18-07 edge | 17.0 |
| piece-18-07 | 106 | edge | 17.0 | no tab | piece-18-05 edge | 17.0 |
| piece-18-06 | 136 | edge | 17.8 | no tab | piece-18-08 edge | 17.5 |
| piece-18-08 | 136 | edge | 17.5 | no tab | piece-18-06 edge | 17.8 |
| piece-18-04 | 192 | edge | 39.5 | unpaired |   |  |
| piece-24-05 | 261 | edge | 32.6 | extra copy: likely misread |   |  |
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
| piece-16-10 | 368 | edge | 22.6 | unpaired |   |  |
| piece-16-07 | 376 | tab | 26.2 | unpaired |   |  |
| piece-16-10 | 378 | edge | 26.3 | length mismatch | piece-16-02 tab | 27.8 |
| piece-16-02 | 379 | edge | 17.9 | no tab | piece-16-04 edge | 17.6 |
| piece-16-04 | 379 | edge | 17.6 | no tab | piece-16-02 edge | 17.9 |
| piece-16-10 | 383 | edge | 22.5 | no tab | piece-16-03 edge | 22.5 |
| piece-06-03 | 386 | edge | 42.5 | length mismatch | piece-16-03 tab | 22.4 |
| piece-18-01 | 397 | edge | 8.0 | no tab | piece-19-01 edge | 8.0 |
| piece-19-01 | 397 | edge | 8.0 | no tab | piece-18-01 edge | 8.0 |
| piece-19-04 | 398 | edge | 9.6 | no tab | piece-19-01 edge | 9.4 |
| piece-04-07 | 420 | edge | 11.3 | no tab | piece-12-04 edge | 11.3 |
| piece-12-04 | 420 | edge | 11.3 | no tab | piece-04-07 edge | 11.3 |
| piece-19-04 | 454 | edge | 10.8 | no tab | piece-19-07 edge | 10.6 |
| piece-19-07 | 454 | edge | 10.6 | no tab | piece-19-04 edge | 10.8 |
| piece-12-06 | 545 | edge | 8.9 | no tab | piece-12-07 edge | 8.8 |
| piece-12-06 | 546 | edge | 17.1 | unpaired |   |  |
| piece-17-05 | 556 | edge | 31.2 | length mismatch | piece-07-03 tab | 71.3 |
| piece-22-02 | 580 | tab | 46.0 | extra copy: likely misread |   |  |
| piece-12-04 | 593 | edge | 12.4 | printed 3 times |   |  |
| piece-12-06 | 593 | edge | 10.8 | printed 3 times |   |  |
| piece-12-06 | 594 | tab | 24.1 | unpaired |   |  |
| piece-12-11 | 648 | tab | 51.7 | extra copy: likely misread |   |  |
| piece-09-01 | 657 | edge | 42.3 | unpaired |   |  |
| piece-22-01 | 680 | edge | 46.0 | extra copy: likely misread |   |  |
| piece-09-01 | 683 | tab | 55.2 | unpaired |   |  |
| piece-09-01 | 685 | tab | 54.1 | length mismatch | piece-07-02 edge | 70.6 |
| piece-24-07 | 785 | edge | 15.4 | unpaired |   |  |
| piece-24-03 | 789 | edge | 18.1 | unpaired |   |  |
| piece-11-06 | 790 | edge | 24.2 | unpaired |   |  |
| piece-11-05 | 791 | edge | 15.8 | unpaired |   |  |
| piece-05-07 | 792 | edge | 24.3 | unpaired |   |  |

## Mirror twins

The model is symmetric: 89 pairs of pieces are mirror images (178 of 178 pieces), found by the lengths of their numbered lines: 7 exact mirrors (outline and tabs match) and 82 mirror variations (same body, tabs on other edges). Of their {paired} mirrored lines, {off} differ in length from their mirror line by more than 1 mm, so one of the two was traced off (`bowser-mirrors.csv`). A twin's clean glue pair also predicts the number on the mirror line; those predictions are applied when clear-cut, and otherwise go to the check page with `mirror` as the reason.


## Likely misreads

55 clear-cut misreads were fixed without asking (marked `applied` in `bowser-misreads.csv`). 15 more numbers that did not pair up sit on a line of the same length as another unpaired number on the other side (edge against tab), and the two numbers look alike. Check them with `make fix` and `app/number-check.html`.

| piece | side | mm | read | suggested | partner | partner mm | why |
|---|---|---:|---|---|---|---:|---|
| piece-16-07 | tab | 26.2 | 376 | 378 | piece-16-10 edge | 26.3 | OCR's other reading |
| piece-24-05 | edge | 32.6 | 261 | 281 | piece-24-05 tab | 32.6 | OCR's other reading; the read number already pairs elsewhere |
| piece-10-05 | edge | 42.3 | 885 | 887 | piece-09-03 tab | 42.2 | one digit differs |
| piece-17-06 | edge | 59.2 | 628 | 698 | piece-10-04 tab | 59.3 | one digit differs; the read number already pairs elsewhere |
| piece-22-02 | tab | 46.0 | 580 | 680 | piece-22-01 edge | 46.0 | OCR's other reading; the read number already pairs elsewhere |
| piece-09-03 | edge | 53.9 | 885 | 685 | piece-09-01 tab | 54.1 | OCR's other reading |
| piece-14-03 | edge | 32.6 | 280 | 260 | piece-14-07 tab | 32.5 | one digit differs; the read number already pairs elsewhere |
| piece-16-03 | tab | 22.4 | 386 | 368 | piece-16-10 edge | 22.6 | OCR's other reading |
| piece-16-09 | tab | 39.7 | 162 | 192 | piece-18-04 edge | 39.5 | one digit differs; the read number already pairs elsewhere |
| piece-17-08 | tab | 31.4 | 999 | 556 | piece-17-05 edge | 31.2 | OCR's other reading |
| piece-04-03 | tab | 37.6 | 456 | 406 | piece-12-03 edge | 37.9 | OCR's other reading; the read number already pairs elsewhere |
| piece-09-05 | edge | 51.3 | 295 | 286 | piece-09-04 tab | 51.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-24-08 | tab | 13.3 | 268 | 286 | piece-16-04 edge | 13.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-06-04 | tab | 43.2 | 369 | 386 | piece-06-03 edge | 42.5 | OCR's other reading |
| piece-12-04 | tab | 16.8 | 5 | 58 | piece-11-05 edge | 17.8 | a digit dropped or added |

Full tables: `bowser-edges.csv`, `bowser-misreads.csv`.
