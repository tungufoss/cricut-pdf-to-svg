# Bowser

1575 printed numbers on 178 pieces. 719 numbers form a clean pair (one plain edge, one tab, lengths within 1 mm); 137 labels need a look.

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
| folds | 1496, 13 stretched far to reach the cut |
| numbers | 1575 read, 221 uncertain (orange in the SVG) |
| pieces to check | 122 marked ⚠ in Inkscape |
| paper colour | footers disagree with the YAML: pages 14–23 say beige (YAML: yellow); page 24 says white (YAML: black) |
| nesting on sheets | not started |

## Edge numbers

| status | labels | meaning |
|---|---:|---|
| ok | 1438 | partner found, one tab and one plain edge, same length |
| unpaired | 41 | no other copy of this number: likely misread |
| no tab | 40 | neither copy sits on a tab fold |
| extra copy: likely misread | 23 | number read more than twice; the other copies already form a clean pair |
| length mismatch | 18 | partner found but the marked lines differ in length: misread number or traced line |
| both tabs | 8 | both copies sit on a tab fold |
| line not found | 4 | no cut edge or fold next to the number |
| printed 3 times | 3 | number read more than twice: some are misread |

## Pages

| page | config material | footer says | pieces | ok | check |
|---|---|---|---:|---:|---:|
| 04 | red | red | 8 | 71 | 4 |
| 05 | red | red | 8 | 72 | 3 |
| 06 | red | red | 6 | 51 | 8 |
| 07 | red | red | 10 | 71 | 5 |
| 08 | red | red | 6 | 50 | 6 |
| 09 | red | red | 7 | 50 | 8 |
| 10 | red | red | 7 | 51 | 3 |
| 11 | green | green | 11 | 80 | 10 |
| 12 | green | green | 11 | 75 | 15 |
| 13 | green | green | 4 | 28 | 2 |
| 14 | yellow | beige ⚠ | 10 | 87 | 5 |
| 15 | yellow | beige ⚠ | 10 | 80 | 12 |
| 16 | yellow | beige ⚠ | 10 | 78 | 15 |
| 17 | yellow | beige ⚠ | 10 | 85 | 8 |
| 18 | yellow | beige ⚠ | 8 | 73 | 9 |
| 19 | yellow | beige ⚠ | 8 | 70 | 12 |
| 20 | yellow | beige ⚠ | 8 | 75 | 1 |
| 21 | yellow | beige ⚠ | 8 | 76 | 0 |
| 22 | yellow | beige ⚠ | 6 | 58 | 0 |
| 23 | yellow | beige ⚠ | 6 | 56 | 2 |
| 24 | black | white ⚠ | 16 | 101 | 9 |

## Pieces to check

Pieces listed by how many of their numbers need a look.

| piece | ok | check | numbers to check |
|---|---:|---:|---|
| piece-12-04 | 4 | 6 | 5 (unpaired), 6 (unpaired), 014 (unpaired), 420 (no tab), 693 (length mismatch), 742 (length mismatch) |
| piece-12-06 | 4 | 4 | 546 (unpaired), 593 (no tab), 594 (unpaired), 645 (unpaired) |
| piece-19-04 | 10 | 4 | 398 (no tab), 400 (no tab), 454 (no tab), 791 (no tab) |
| piece-16-03 | 10 | 4 | 372 (length mismatch), 383 (no tab), 386 (extra copy: likely misread), 869 (extra copy: likely misread) |
| piece-16-10 | 6 | 3 | 48 (no tab), 368 (unpaired), 383 (no tab) |
| piece-11-05 | 7 | 3 | 58 (no tab), 791 (no tab), 793 (unpaired) |
| piece-15-06 | 8 | 3 | 564 (no tab), 580 (extra copy: likely misread), 582 (extra copy: likely misread) |
| piece-19-01 | 5 | 3 | 397 (no tab), 398 (no tab), 400 (no tab) |
| piece-11-02 | 7 | 2 | 00 (unpaired), 48 (no tab) |
| piece-24-03 | 5 | 2 | 755 (extra copy: likely misread), 789 (unpaired) |
| piece-11-07 | 5 | 2 | 14 (printed 3 times), 760 (extra copy: likely misread) |
| piece-06-03 | 9 | 2 | 34 (line not found), 316 (length mismatch) |
| piece-06-06 | 8 | 2 | 34 (line not found), 316 (length mismatch) |
| piece-18-03 | 12 | 2 | 90 (no tab), 95 (unpaired) |
| piece-18-06 | 9 | 2 | 90 (no tab), 136 (no tab) |
| piece-16-04 | 13 | 2 | 286 (no tab), 379 (no tab) |
| piece-12-07 | 5 | 2 | 545 (unpaired), 548 (length mismatch) |
| piece-09-04 | 7 | 2 | 259 (extra copy: likely misread), 562 (both tabs) |
| piece-07-01 | 8 | 2 | 273 (both tabs), 672 (unpaired) |
| piece-16-07 | 4 | 2 | 372 (length mismatch), 376 (unpaired) |
| piece-16-02 | 7 | 2 | 378 (unpaired), 379 (no tab) |
| piece-08-05 | 7 | 2 | 305 (both tabs), 326 (extra copy: likely misread) |
| piece-04-07 | 7 | 2 | 420 (no tab), 784 (unpaired) |
| piece-24-12 | 6 | 2 | 445 (extra copy: likely misread), 701 (unpaired) |
| piece-19-07 | 9 | 2 | 454 (no tab), 496 (no tab) |
| piece-15-07 | 8 | 2 | 562 (both tabs), 580 (extra copy: likely misread) |
| piece-15-10 | 9 | 2 | 527 (length mismatch), 536 (unpaired) |
| piece-17-10 | 10 | 2 | 551 (length mismatch), 555 (both tabs) |
| piece-15-08 | 12 | 2 | 527 (length mismatch), 939 (unpaired) |
| piece-09-01 | 6 | 2 | 657 (unpaired), 693 (length mismatch) |
| piece-11-01 | 5 | 1 | 000 (unpaired) |
| piece-04-02 | 11 | 1 | 03 (unpaired) |
| piece-12-05 | 12 | 1 | 742 (length mismatch) |
| piece-05-01 | 11 | 1 | 46 (extra copy: likely misread) |
| piece-11-03 | 8 | 1 | 14 (printed 3 times) |
| piece-24-15 | 7 | 1 | 14 (printed 3 times) |
| piece-06-02 | 8 | 1 | 865 (unpaired) |
| piece-06-01 | 8 | 1 | 356 (extra copy: likely misread) |
| piece-07-07 | 9 | 1 | 273 (both tabs) |
| piece-05-03 | 11 | 1 | 58 (no tab) |
| piece-05-07 | 8 | 1 | 792 (unpaired) |
| piece-24-04 | 7 | 1 | 794 (unpaired) |
| piece-18-01 | 7 | 1 | 397 (no tab) |
| piece-18-05 | 12 | 1 | 106 (no tab) |
| piece-18-08 | 10 | 1 | 136 (no tab) |
| piece-20-03 | 10 | 1 | 85 (extra copy: likely misread) |
| piece-18-07 | 10 | 1 | 106 (no tab) |
| piece-14-04 | 6 | 1 | 137 (length mismatch) |
| piece-14-05 | 4 | 1 | 137 (length mismatch) |
| piece-11-06 | 7 | 1 | 790 (unpaired) |
| piece-12-03 | 8 | 1 | 406 (unpaired) |
| piece-04-03 | 11 | 1 | 456 (extra copy: likely misread) |
| piece-16-09 | 11 | 1 | 162 (extra copy: likely misread) |
| piece-14-06 | 13 | 1 | 369 (unpaired) |
| piece-14-07 | 10 | 1 | 564 (no tab) |
| piece-24-08 | 5 | 1 | 288 (extra copy: likely misread) |
| piece-18-04 | 7 | 1 | 192 (unpaired) |
| piece-24-07 | 7 | 1 | 785 (unpaired) |
| piece-14-03 | 7 | 1 | 290 (unpaired) |
| piece-23-01 | 10 | 1 | 997 (unpaired) |
| piece-23-03 | 8 | 1 | 235 (unpaired) |
| piece-15-01 | 7 | 1 | 260 (extra copy: likely misread) |
| piece-17-05 | 11 | 1 | 556 (no tab) |
| piece-09-05 | 7 | 1 | 286 (no tab) |
| piece-08-06 | 7 | 1 | 305 (both tabs) |
| piece-08-04 | 10 | 1 | 689 (no tab) |
| piece-08-02 | 8 | 1 | 668 (unpaired) |
| piece-09-07 | 7 | 1 | 325 (unpaired) |
| piece-06-05 | 8 | 1 | 947 (unpaired) |
| piece-10-05 | 7 | 1 | 689 (no tab) |
| piece-13-04 | 4 | 1 | 593 (no tab) |
| piece-08-01 | 10 | 1 | 588 (extra copy: likely misread) |
| piece-10-02 | 6 | 1 | 341 (line not found) |
| piece-16-06 | 3 | 1 | 341 (line not found) |
| piece-06-04 | 10 | 1 | 380 (extra copy: likely misread) |
| piece-17-03 | 13 | 1 | 732 (no tab) |
| piece-17-07 | 5 | 1 | 730 (unpaired) |
| piece-19-08 | 10 | 1 | 496 (no tab) |
| piece-19-06 | 10 | 1 | 556 (no tab) |
| piece-19-03 | 7 | 1 | 551 (length mismatch) |
| piece-24-09 | 6 | 1 | 750 (unpaired) |
| piece-15-04 | 6 | 1 | 616 (extra copy: likely misread) |
| piece-15-09 | 9 | 1 | 616 (extra copy: likely misread) |
| piece-17-08 | 6 | 1 | 999 (length mismatch) |
| piece-13-03 | 9 | 1 | 648 (extra copy: likely misread) |
| piece-12-11 | 5 | 1 | 548 (length mismatch) |
| piece-07-03 | 8 | 1 | 555 (both tabs) |
| piece-07-02 | 5 | 1 | 685 (unpaired) |
| piece-17-09 | 8 | 1 | 732 (no tab) |
| piece-17-06 | 3 | 1 | 628 (extra copy: likely misread) |
| piece-09-06 | 7 | 1 | 999 (length mismatch) |
| piece-09-03 | 8 | 1 | 887 (unpaired) |
| piece-10-04 | 6 | 1 | 698 (unpaired) |

## Hand corrections that still do not pair

501 numbers were set by hand; 47 of them still do not form a clean pair, so the correction, its partner or the traced line is likely off. They come first on the check page.

| piece | number | side | mm | status | partner | partner mm |
|---|---|---|---:|---|---|---:|
| piece-12-04 | 5 | tab | 16.8 | unpaired |   |  |
| piece-12-04 | 6 | tab | 17.8 | unpaired |   |  |
| piece-06-03 | 34 | none | 0.0 | line not found | piece-06-06 edge | 34.7 |
| piece-11-02 | 48 | edge | 23.9 | no tab | piece-16-10 edge | 26.3 |
| piece-05-03 | 58 | edge | 17.8 | no tab | piece-11-05 edge | 17.8 |
| piece-11-05 | 58 | edge | 17.8 | no tab | piece-05-03 edge | 17.8 |
| piece-20-03 | 85 | edge | 23.4 | extra copy: likely misread |   |  |
| piece-18-03 | 95 | tab | 23.5 | unpaired |   |  |
| piece-18-05 | 106 | edge | 17.0 | no tab | piece-18-07 edge | 17.0 |
| piece-18-07 | 106 | edge | 17.0 | no tab | piece-18-05 edge | 17.0 |
| piece-18-06 | 136 | edge | 17.7 | no tab | piece-18-08 edge | 17.5 |
| piece-18-08 | 136 | edge | 17.5 | no tab | piece-18-06 edge | 17.7 |
| piece-14-04 | 137 | edge | 27.1 | length mismatch | piece-14-05 tab | 33.9 |
| piece-14-05 | 137 | tab | 33.9 | length mismatch | piece-14-04 edge | 27.1 |
| piece-18-04 | 192 | edge | 39.5 | unpaired |   |  |
| piece-07-01 | 273 | tab | 17.1 | both tabs | piece-07-07 tab | 17.0 |
| piece-07-07 | 273 | tab | 17.0 | both tabs | piece-07-01 tab | 17.1 |
| piece-16-04 | 286 | edge | 13.8 | no tab | piece-09-05 edge | 51.3 |
| piece-24-08 | 288 | tab | 13.3 | extra copy: likely misread |   |  |
| piece-08-05 | 305 | tab | 29.7 | both tabs | piece-08-06 tab | 29.7 |
| piece-08-06 | 305 | tab | 29.7 | both tabs | piece-08-05 tab | 29.7 |
| piece-06-03 | 316 | edge | 37.3 | length mismatch | piece-06-06 tab | 38.3 |
| piece-06-06 | 316 | tab | 38.3 | length mismatch | piece-06-03 edge | 37.3 |
| piece-10-02 | 341 | none | 0.0 | line not found | piece-16-06 edge | 58.4 |
| piece-16-06 | 341 | edge | 58.4 | line not found | piece-10-02 none | 0.0 |
| piece-16-07 | 376 | tab | 26.2 | unpaired |   |  |
| piece-16-02 | 379 | edge | 17.9 | no tab | piece-16-04 edge | 17.6 |
| piece-16-04 | 379 | edge | 17.6 | no tab | piece-16-02 edge | 17.9 |
| piece-18-01 | 397 | edge | 8.0 | no tab | piece-19-01 edge | 8.0 |
| piece-19-01 | 397 | edge | 8.0 | no tab | piece-18-01 edge | 8.0 |
| piece-19-04 | 398 | edge | 9.6 | no tab | piece-19-01 edge | 9.4 |
| piece-04-07 | 420 | edge | 11.8 | no tab | piece-12-04 edge | 11.3 |
| piece-12-04 | 420 | edge | 11.3 | no tab | piece-04-07 edge | 11.8 |
| piece-19-04 | 454 | edge | 10.8 | no tab | piece-19-07 edge | 10.6 |
| piece-19-07 | 454 | edge | 10.6 | no tab | piece-19-04 edge | 10.8 |
| piece-17-05 | 556 | edge | 31.2 | no tab | piece-19-06 edge | 51.3 |
| piece-15-07 | 562 | tab | 19.1 | both tabs | piece-09-04 tab | 51.8 |
| piece-15-06 | 580 | edge | 18.8 | extra copy: likely misread |   |  |
| piece-15-07 | 580 | tab | 18.7 | extra copy: likely misread |   |  |
| piece-15-06 | 582 | edge | 18.5 | extra copy: likely misread |   |  |
| piece-09-01 | 657 | edge | 42.3 | unpaired |   |  |
| piece-24-07 | 785 | edge | 15.4 | unpaired |   |  |
| piece-24-03 | 789 | edge | 18.1 | unpaired |   |  |
| piece-11-06 | 790 | edge | 24.2 | unpaired |   |  |
| piece-11-05 | 791 | edge | 13.6 | no tab | piece-19-04 edge | 23.3 |
| piece-05-07 | 792 | edge | 24.3 | unpaired |   |  |
| piece-23-01 | 997 | edge | 36.8 | unpaired |   |  |

## Mirror twins

The model is symmetric: 89 pairs of pieces are mirror images (178 of 178 pieces), found by the lengths of their numbered lines: 7 exact mirrors (outline and tabs match) and 82 mirror variations (same body, tabs on other edges). Of their {paired} mirrored lines, {off} differ in length from their mirror line by more than 1 mm, so one of the two was traced off (`bowser-mirrors.csv`). A twin's clean glue pair also predicts the number on the mirror line; those predictions are applied when clear-cut, and otherwise go to the check page with `mirror` as the reason.


## Likely misreads

59 clear-cut misreads were fixed without asking (marked `applied` in `bowser-misreads.csv`). 20 more numbers that did not pair up sit on a line of the same length as another unpaired number on the other side (edge against tab), and the two numbers look alike. Check them with `make fix` and `app/number-check.html`.

| piece | side | mm | read | suggested | partner | partner mm | why |
|---|---|---:|---|---|---|---:|---|
| piece-09-06 | edge | 46.8 | 999 | 668 | piece-08-02 tab | 46.8 | OCR's other reading |
| piece-11-01 | edge | 50.4 | 000 | 00 | piece-11-02 tab | 50.5 | a digit dropped or added |
| piece-15-01 | edge | 30.9 | 260 | 290 | piece-14-03 tab | 30.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-17-10 | tab | 51.3 | 555 | 556 | piece-19-06 edge | 51.3 | OCR's other reading |
| piece-24-12 | tab | 23.3 | 701 | 791 | piece-19-04 edge | 23.3 | OCR's other reading |
| piece-08-05 | edge | 46.6 | 326 | 325 | piece-09-07 tab | 46.7 | OCR's other reading; the read number already pairs elsewhere |
| piece-13-03 | edge | 51.6 | 648 | 548 | piece-12-11 tab | 51.7 | OCR's other reading; the read number already pairs elsewhere |
| piece-17-06 | edge | 59.2 | 628 | 698 | piece-10-04 tab | 59.3 | one digit differs; the read number already pairs elsewhere |
| piece-08-01 | tab | 23.6 | 588 | 689 | piece-08-04 edge | 23.4 | OCR's other reading; the read number already pairs elsewhere |
| piece-16-03 | tab | 22.4 | 386 | 368 | piece-16-10 edge | 22.6 | OCR's other reading; the read number already pairs elsewhere |
| piece-16-03 | tab | 44.6 | 869 | 369 | piece-14-06 edge | 44.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-16-09 | tab | 39.7 | 162 | 192 | piece-18-04 edge | 39.5 | one digit differs; the read number already pairs elsewhere |
| piece-17-08 | tab | 31.4 | 999 | 556 | piece-17-05 edge | 31.2 | OCR's other reading |
| piece-04-03 | tab | 37.6 | 456 | 406 | piece-12-03 edge | 37.9 | OCR's other reading; the read number already pairs elsewhere |
| piece-11-02 | edge | 23.9 | 48 | 95 | piece-18-03 tab | 23.5 | OCR's other reading |
| piece-09-05 | edge | 51.3 | 286 | 562 | piece-09-04 tab | 51.8 | OCR's other reading |
| piece-24-08 | tab | 13.3 | 288 | 286 | piece-16-04 edge | 13.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-15-06 | edge | 18.5 | 582 | 562 | piece-15-07 tab | 19.1 | OCR's other reading; the read number already pairs elsewhere |
| piece-12-04 | tab | 16.8 | 5 | 58 | piece-11-05 edge | 17.8 | a digit dropped or added |
| piece-15-07 | tab | 18.7 | 580 | 58 | piece-05-03 edge | 17.8 | a digit dropped or added; the read number already pairs elsewhere |

Full tables: `bowser-edges.csv`, `bowser-misreads.csv`.
