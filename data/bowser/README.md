# Bowser

1570 printed numbers on 178 pieces. 666 numbers form a clean pair (one plain edge, one tab, lengths within 1 mm); 238 labels need a look.

Conversion status (2026-10-15), written by `make`. Edit the YAML, not this file.

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
| numbers | 1570 read, 272 uncertain (orange in the SVG) |
| pieces to check | 139 marked ⚠ in Inkscape |
| paper colour | footers disagree with the YAML: pages 14–23 say beige (YAML: yellow); page 24 says white (YAML: black) |
| nesting on sheets | not started |

## Edge numbers

| status | labels | meaning |
|---|---:|---|
| ok | 1332 | partner found, one tab and one plain edge, same length |
| length mismatch | 64 | partner found but the marked lines differ in length: misread number or traced line |
| line not found | 60 | no cut edge or fold next to the number |
| unpaired | 54 | no other copy of this number: likely misread |
| extra copy: likely misread | 34 | number read more than twice; the other copies already form a clean pair |
| no tab | 14 | neither copy sits on a tab fold |
| both tabs | 12 | both copies sit on a tab fold |

## Pages

| page | config material | footer says | pieces | ok | check |
|---|---|---|---:|---:|---:|
| 04 | red | red | 8 | 65 | 10 |
| 05 | red | red | 8 | 66 | 9 |
| 06 | red | red | 6 | 49 | 9 |
| 07 | red | red | 10 | 66 | 10 |
| 08 | red | red | 6 | 48 | 8 |
| 09 | red | red | 7 | 44 | 14 |
| 10 | red | red | 7 | 49 | 5 |
| 11 | green | green | 11 | 66 | 24 |
| 12 | green | green | 11 | 64 | 26 |
| 13 | green | green | 4 | 25 | 5 |
| 14 | yellow | beige ⚠ | 10 | 86 | 6 |
| 15 | yellow | beige ⚠ | 10 | 78 | 14 |
| 16 | yellow | beige ⚠ | 10 | 72 | 19 |
| 17 | yellow | beige ⚠ | 10 | 70 | 21 |
| 18 | yellow | beige ⚠ | 8 | 71 | 11 |
| 19 | yellow | beige ⚠ | 8 | 67 | 15 |
| 20 | yellow | beige ⚠ | 8 | 73 | 3 |
| 21 | yellow | beige ⚠ | 8 | 75 | 1 |
| 22 | yellow | beige ⚠ | 6 | 58 | 0 |
| 23 | yellow | beige ⚠ | 6 | 54 | 4 |
| 24 | black | white ⚠ | 16 | 86 | 24 |

## Pieces to check

Pieces listed by how many of their numbers need a look.

| piece | ok | check | numbers to check |
|---|---:|---:|---|
| piece-12-04 | 1 | 9 | 3 (unpaired), 5 (unpaired), 6 (unpaired), 7 (line not found), 014 (unpaired), 17 (extra copy: likely misread), 420 (line not found), 693 (length mismatch), 742 (length mismatch) |
| piece-11-05 | 4 | 6 | 58 (line not found), 770 (line not found), 777 (line not found), 778 (line not found), 781 (length mismatch), 793 (unpaired) |
| piece-12-06 | 3 | 5 | 040 (line not found), 546 (unpaired), 593 (line not found), 594 (unpaired), 645 (unpaired) |
| piece-11-02 | 5 | 4 | 000 (unpaired), 11 (line not found), 040 (line not found), 48 (no tab) |
| piece-12-05 | 9 | 4 | 4 (unpaired), 7 (line not found), 742 (length mismatch), 745 (line not found) |
| piece-16-10 | 3 | 4 | 48 (no tab), 68 (extra copy: likely misread), 283 (length mismatch), 448 (extra copy: likely misread) |
| piece-19-04 | 10 | 4 | 398 (line not found), 400 (line not found), 454 (line not found), 457 (line not found) |
| piece-16-03 | 10 | 4 | 372 (length mismatch), 386 (extra copy: likely misread), 869 (extra copy: likely misread), 883 (no tab) |
| piece-15-06 | 7 | 4 | 206 (length mismatch), 564 (line not found), 580 (extra copy: likely misread), 582 (extra copy: likely misread) |
| piece-24-05 | 2 | 4 | 261 (extra copy: likely misread), 281 (unpaired), 283 (length mismatch), 384 (unpaired) |
| piece-17-03 | 10 | 4 | 716 (length mismatch), 718 (length mismatch), 726 (line not found), 732 (unpaired) |
| piece-04-07 | 5 | 4 | 420 (line not found), 422 (extra copy: likely misread), 731 (no tab), 784 (unpaired) |
| piece-19-01 | 4 | 4 | 397 (line not found), 398 (line not found), 399 (unpaired), 400 (line not found) |
| piece-11-04 | 10 | 3 | 11 (line not found), 745 (line not found), 770 (line not found) |
| piece-11-03 | 6 | 3 | 13 (line not found), 15 (line not found), 786 (length mismatch) |
| piece-06-06 | 6 | 3 | 13 (line not found), 272 (length mismatch), 316 (length mismatch) |
| piece-24-15 | 5 | 3 | 14 (extra copy: likely misread), 216 (length mismatch), 216 (length mismatch) |
| piece-24-03 | 4 | 3 | 18 (extra copy: likely misread), 755 (extra copy: likely misread), 789 (unpaired) |
| piece-06-03 | 8 | 3 | 33 (length mismatch), 34 (unpaired), 316 (length mismatch) |
| piece-07-07 | 7 | 3 | 272 (length mismatch), 273 (both tabs), 318 (unpaired) |
| piece-24-12 | 5 | 3 | 044 (unpaired), 457 (line not found), 662 (extra copy: likely misread) |
| piece-17-09 | 4 | 3 | 95 (line not found), 655 (unpaired), 976 (unpaired) |
| piece-11-06 | 5 | 3 | 757 (length mismatch), 777 (line not found), 790 (unpaired) |
| piece-12-07 | 4 | 3 | 208 (length mismatch), 545 (unpaired), 548 (line not found) |
| piece-09-04 | 6 | 3 | 259 (extra copy: likely misread), 300 (length mismatch), 562 (both tabs) |
| piece-07-01 | 7 | 3 | 273 (both tabs), 618 (length mismatch), 672 (unpaired) |
| piece-08-05 | 6 | 3 | 305 (both tabs), 312 (length mismatch), 326 (extra copy: likely misread) |
| piece-13-03 | 7 | 3 | 648 (extra copy: likely misread), 687 (length mismatch), 698 (both tabs) |
| piece-17-06 | 1 | 3 | 628 (extra copy: likely misread), 735 (line not found), 944 (unpaired) |
| piece-09-03 | 6 | 3 | 658 (length mismatch), 883 (no tab), 887 (unpaired) |
| piece-17-01 | 6 | 3 | 706 (extra copy: likely misread), 723 (unpaired), 726 (line not found) |
| piece-11-01 | 4 | 2 | 00 (unpaired), 33 (length mismatch) |
| piece-05-02 | 5 | 2 | 9 (unpaired), 47 (line not found) |
| piece-05-01 | 10 | 2 | 46 (extra copy: likely misread), 47 (line not found) |
| piece-11-07 | 5 | 2 | 757 (length mismatch), 760 (extra copy: likely misread) |
| piece-05-03 | 10 | 2 | 58 (line not found), 81 (extra copy: likely misread) |
| piece-05-07 | 7 | 2 | 778 (line not found), 792 (unpaired) |
| piece-24-04 | 6 | 2 | 786 (length mismatch), 794 (unpaired) |
| piece-18-03 | 12 | 2 | 90 (line not found), 95 (line not found) |
| piece-18-06 | 9 | 2 | 90 (line not found), 136 (line not found) |
| piece-16-04 | 13 | 2 | 286 (no tab), 379 (line not found) |
| piece-04-03 | 10 | 2 | 406 (length mismatch), 456 (extra copy: likely misread) |
| piece-14-07 | 9 | 2 | 208 (length mismatch), 564 (line not found) |
| piece-18-04 | 6 | 2 | 192 (unpaired), 482 (no tab) |
| piece-24-07 | 6 | 2 | 781 (length mismatch), 785 (unpaired) |
| piece-23-03 | 7 | 2 | 229 (length mismatch), 235 (unpaired) |
| piece-16-07 | 4 | 2 | 372 (length mismatch), 376 (unpaired) |
| piece-16-02 | 7 | 2 | 378 (unpaired), 379 (line not found) |
| piece-09-05 | 6 | 2 | 286 (no tab), 300 (length mismatch) |
| piece-08-04 | 9 | 2 | 328 (length mismatch), 689 (no tab) |
| piece-09-07 | 6 | 2 | 312 (length mismatch), 325 (unpaired) |
| piece-06-05 | 7 | 2 | 618 (length mismatch), 947 (unpaired) |
| piece-10-05 | 6 | 2 | 328 (length mismatch), 689 (no tab) |
| piece-13-04 | 3 | 2 | 593 (line not found), 687 (length mismatch) |
| piece-16-06 | 2 | 2 | 341 (line not found), 735 (line not found) |
| piece-17-07 | 4 | 2 | 444 (extra copy: likely misread), 730 (unpaired) |
| piece-19-07 | 9 | 2 | 454 (line not found), 496 (line not found) |
| piece-17-04 | 13 | 2 | 708 (unpaired), 714 (line not found) |
| piece-19-03 | 6 | 2 | 539 (length mismatch), 551 (length mismatch) |
| piece-15-07 | 8 | 2 | 562 (both tabs), 580 (extra copy: likely misread) |
| piece-15-10 | 9 | 2 | 527 (length mismatch), 536 (unpaired) |
| piece-17-10 | 10 | 2 | 551 (length mismatch), 555 (both tabs) |
| piece-15-08 | 12 | 2 | 527 (length mismatch), 939 (unpaired) |
| piece-24-06 | 4 | 2 | 631 (unpaired), 718 (length mismatch) |
| piece-09-01 | 6 | 2 | 657 (unpaired), 693 (length mismatch) |
| piece-04-02 | 11 | 1 | 03 (unpaired) |
| piece-16-01 | 4 | 1 | 15 (line not found) |
| piece-11-10 | 7 | 1 | 768 (extra copy: likely misread) |
| piece-12-01 | 5 | 1 | 308 (length mismatch) |
| piece-05-05 | 9 | 1 | 61 (unpaired) |
| piece-18-01 | 7 | 1 | 397 (line not found) |
| piece-18-05 | 12 | 1 | 106 (line not found) |
| piece-18-08 | 10 | 1 | 136 (line not found) |
| piece-20-03 | 10 | 1 | 85 (extra copy: likely misread) |
| piece-18-07 | 10 | 1 | 106 (line not found) |
| piece-18-02 | 5 | 1 | 182 (both tabs) |
| piece-20-02 | 9 | 1 | 129 (length mismatch) |
| piece-20-04 | 9 | 1 | 129 (length mismatch) |
| piece-14-04 | 6 | 1 | 137 (length mismatch) |
| piece-14-05 | 4 | 1 | 137 (length mismatch) |
| piece-12-03 | 8 | 1 | 406 (length mismatch) |
| piece-04-01 | 6 | 1 | 405 (unpaired) |
| piece-16-08 | 6 | 1 | 716 (length mismatch) |
| piece-16-09 | 11 | 1 | 182 (both tabs) |
| piece-14-06 | 13 | 1 | 369 (unpaired) |
| piece-24-08 | 5 | 1 | 288 (extra copy: likely misread) |
| piece-12-02 | 8 | 1 | 206 (length mismatch) |
| piece-14-03 | 7 | 1 | 290 (unpaired) |
| piece-23-01 | 10 | 1 | 997 (unpaired) |
| piece-23-05 | 10 | 1 | 229 (length mismatch) |
| piece-12-08 | 6 | 1 | 308 (length mismatch) |
| piece-04-06 | 7 | 1 | 570 (length mismatch) |
| piece-04-08 | 7 | 1 | 578 (extra copy: likely misread) |
| piece-15-01 | 7 | 1 | 260 (extra copy: likely misread) |
| piece-17-05 | 11 | 1 | 556 (no tab) |
| piece-07-10 | 5 | 1 | 265 (length mismatch) |
| piece-07-08 | 6 | 1 | 265 (length mismatch) |
| piece-24-01 | 5 | 1 | 280 (unpaired) |
| piece-08-06 | 7 | 1 | 305 (both tabs) |
| piece-08-02 | 8 | 1 | 668 (unpaired) |
| piece-08-01 | 10 | 1 | 588 (extra copy: likely misread) |
| piece-10-02 | 6 | 1 | 341 (line not found) |
| piece-10-01 | 8 | 1 | 570 (length mismatch) |
| piece-24-16 | 6 | 1 | 576 (extra copy: likely misread) |
| piece-06-04 | 10 | 1 | 380 (extra copy: likely misread) |
| piece-19-08 | 10 | 1 | 496 (line not found) |
| piece-19-06 | 10 | 1 | 556 (no tab) |
| piece-21-03 | 9 | 1 | 482 (no tab) |
| piece-24-09 | 6 | 1 | 750 (unpaired) |
| piece-15-04 | 6 | 1 | 616 (extra copy: likely misread) |
| piece-15-02 | 8 | 1 | 714 (line not found) |
| piece-15-09 | 9 | 1 | 616 (extra copy: likely misread) |
| piece-17-08 | 6 | 1 | 999 (length mismatch) |
| piece-19-02 | 5 | 1 | 539 (length mismatch) |
| piece-12-11 | 5 | 1 | 548 (line not found) |
| piece-07-03 | 8 | 1 | 555 (both tabs) |
| piece-07-02 | 5 | 1 | 685 (unpaired) |
| piece-24-02 | 5 | 1 | 731 (no tab) |
| piece-09-06 | 7 | 1 | 999 (length mismatch) |
| piece-09-02 | 7 | 1 | 658 (length mismatch) |
| piece-10-04 | 6 | 1 | 698 (both tabs) |

## Hand corrections that still do not pair

495 numbers were set by hand; 96 of them still do not form a clean pair, so the correction, its partner or the traced line is likely off. They come first on the check page.

| piece | number | side | mm | status | partner | partner mm |
|---|---|---|---:|---|---|---:|
| piece-12-04 | 3 | none | 0.0 | unpaired |   |  |
| piece-12-05 | 4 | tab | 15.8 | unpaired |   |  |
| piece-12-04 | 5 | none | 0.0 | unpaired |   |  |
| piece-12-04 | 6 | none | 0.0 | unpaired |   |  |
| piece-12-04 | 7 | none | 0.0 | line not found | piece-12-05 none | 0.0 |
| piece-12-05 | 7 | none | 0.0 | line not found | piece-12-04 none | 0.0 |
| piece-05-02 | 9 | none | 0.0 | unpaired |   |  |
| piece-11-02 | 11 | tab | 15.6 | line not found | piece-11-04 none | 0.0 |
| piece-11-04 | 11 | none | 0.0 | line not found | piece-11-02 tab | 15.6 |
| piece-11-03 | 13 | tab | 31.0 | line not found | piece-06-06 none | 0.0 |
| piece-11-03 | 15 | none | 0.0 | line not found | piece-16-01 edge | 51.9 |
| piece-16-01 | 15 | edge | 51.9 | line not found | piece-11-03 none | 0.0 |
| piece-24-03 | 18 | edge | 29.7 | extra copy: likely misread |   |  |
| piece-06-03 | 33 | tab | 34.2 | length mismatch | piece-11-01 edge | 31.1 |
| piece-11-01 | 33 | edge | 31.1 | length mismatch | piece-06-03 tab | 34.2 |
| piece-06-03 | 34 | none | 0.0 | unpaired |   |  |
| piece-05-01 | 47 | tab | 29.2 | line not found | piece-05-02 none | 0.0 |
| piece-05-02 | 47 | none | 0.0 | line not found | piece-05-01 tab | 29.2 |
| piece-11-02 | 48 | edge | 23.9 | no tab | piece-16-10 edge | 13.2 |
| piece-05-03 | 58 | none | 0.0 | line not found | piece-11-05 edge | 17.8 |
| piece-11-05 | 58 | edge | 17.8 | line not found | piece-05-03 none | 0.0 |
| piece-05-05 | 61 | edge | 27.7 | unpaired |   |  |
| piece-05-03 | 81 | none | 0.0 | extra copy: likely misread |   |  |
| piece-20-03 | 85 | edge | 23.4 | extra copy: likely misread |   |  |
| piece-18-03 | 95 | tab | 23.5 | line not found | piece-17-09 none | 0.0 |
| piece-18-05 | 106 | none | 0.0 | line not found | piece-18-07 edge | 17.0 |
| piece-18-07 | 106 | edge | 17.0 | line not found | piece-18-05 none | 0.0 |
| piece-20-02 | 129 | edge | 19.0 | length mismatch | piece-20-04 tab | 20.2 |
| piece-18-06 | 136 | edge | 17.9 | line not found | piece-18-08 none | 0.0 |
| piece-18-08 | 136 | none | 0.0 | line not found | piece-18-06 edge | 17.9 |
| piece-14-04 | 137 | edge | 20.9 | length mismatch | piece-14-05 tab | 33.9 |
| piece-14-05 | 137 | tab | 33.9 | length mismatch | piece-14-04 edge | 20.9 |
| piece-18-04 | 192 | edge | 37.0 | unpaired |   |  |
| piece-15-06 | 206 | edge | 17.6 | length mismatch | piece-12-02 tab | 14.8 |
| piece-14-07 | 208 | tab | 17.9 | length mismatch | piece-12-07 edge | 14.8 |
| piece-24-15 | 216 | edge | 23.6 | length mismatch | piece-24-15 tab | 25.7 |
| piece-23-03 | 229 | edge | 35.1 | length mismatch | piece-23-05 tab | 37.0 |
| piece-23-05 | 229 | tab | 37.0 | length mismatch | piece-23-03 edge | 35.1 |
| piece-24-05 | 261 | edge | 18.7 | extra copy: likely misread |   |  |
| piece-07-08 | 265 | edge | 36.2 | length mismatch | piece-07-10 tab | 37.7 |
| piece-06-06 | 272 | edge | 12.9 | length mismatch | piece-07-07 tab | 29.0 |
| piece-07-07 | 272 | tab | 29.0 | length mismatch | piece-06-06 edge | 12.9 |
| piece-07-01 | 273 | tab | 29.0 | both tabs | piece-07-07 tab | 29.0 |
| piece-07-07 | 273 | tab | 29.0 | both tabs | piece-07-01 tab | 29.0 |
| piece-24-01 | 280 | tab | 21.4 | unpaired |   |  |
| piece-16-10 | 283 | edge | 17.2 | length mismatch | piece-24-05 tab | 18.3 |
| piece-24-05 | 283 | tab | 18.3 | length mismatch | piece-16-10 edge | 17.2 |
| piece-16-04 | 286 | edge | 13.8 | no tab | piece-09-05 edge | 51.3 |
| piece-24-08 | 288 | tab | 13.3 | extra copy: likely misread |   |  |
| piece-09-04 | 300 | tab | 43.0 | length mismatch | piece-09-05 edge | 40.3 |
| piece-09-05 | 300 | edge | 40.3 | length mismatch | piece-09-04 tab | 43.0 |
| piece-08-05 | 305 | tab | 54.2 | both tabs | piece-08-06 tab | 29.7 |
| piece-08-06 | 305 | tab | 29.7 | both tabs | piece-08-05 tab | 54.2 |
| piece-12-01 | 308 | tab | 42.2 | length mismatch | piece-12-08 edge | 39.9 |
| piece-12-08 | 308 | edge | 39.9 | length mismatch | piece-12-01 tab | 42.2 |
| piece-08-05 | 312 | tab | 54.2 | length mismatch | piece-09-07 edge | 25.8 |
| piece-09-07 | 312 | edge | 25.8 | length mismatch | piece-08-05 tab | 54.2 |
| piece-06-03 | 316 | edge | 37.3 | length mismatch | piece-06-06 tab | 38.3 |
| piece-06-06 | 316 | tab | 38.3 | length mismatch | piece-06-03 edge | 37.3 |
| piece-07-07 | 318 | edge | 37.4 | unpaired |   |  |
| piece-08-04 | 328 | edge | 26.3 | length mismatch | piece-10-05 tab | 25.1 |
| piece-10-05 | 328 | tab | 25.1 | length mismatch | piece-08-04 edge | 26.3 |
| piece-10-02 | 341 | none | 0.0 | line not found | piece-16-06 edge | 58.4 |
| piece-16-06 | 341 | edge | 58.4 | line not found | piece-10-02 none | 0.0 |
| piece-16-07 | 376 | tab | 26.2 | unpaired |   |  |
| piece-16-02 | 379 | none | 0.0 | line not found | piece-16-04 edge | 17.6 |
| piece-16-04 | 379 | edge | 17.6 | line not found | piece-16-02 none | 0.0 |
| piece-18-01 | 397 | edge | 8.0 | line not found | piece-19-01 none | 0.0 |
| piece-19-01 | 397 | none | 0.0 | line not found | piece-18-01 edge | 8.0 |
| piece-19-04 | 398 | edge | 9.6 | line not found | piece-19-01 none | 0.0 |
| piece-19-01 | 399 | tab | 14.2 | unpaired |   |  |
| piece-04-01 | 405 | edge | 29.4 | unpaired |   |  |
| piece-04-07 | 420 | none | 0.0 | line not found | piece-12-04 edge | 11.3 |
| piece-12-04 | 420 | edge | 11.3 | line not found | piece-04-07 none | 0.0 |
| piece-04-07 | 422 | tab | 28.9 | extra copy: likely misread |   |  |
| piece-19-04 | 454 | none | 0.0 | line not found | piece-19-07 edge | 10.7 |
| piece-19-07 | 454 | edge | 10.7 | line not found | piece-19-04 none | 0.0 |
| piece-24-12 | 457 | none | 0.0 | line not found | piece-19-04 tab | 23.9 |
| piece-21-03 | 482 | edge | 28.0 | no tab | piece-18-04 edge | 37.4 |
| piece-17-05 | 556 | edge | 29.0 | no tab | piece-19-06 edge | 49.1 |
| piece-15-07 | 562 | tab | 17.9 | both tabs | piece-09-04 tab | 51.8 |
| piece-15-06 | 580 | edge | 18.8 | extra copy: likely misread |   |  |
| piece-15-07 | 580 | tab | 18.7 | extra copy: likely misread |   |  |
| piece-15-06 | 582 | edge | 18.5 | extra copy: likely misread |   |  |
| piece-07-01 | 618 | tab | 29.0 | length mismatch | piece-06-05 edge | 12.9 |
| piece-09-01 | 657 | edge | 42.3 | unpaired |   |  |
| piece-09-02 | 658 | edge | 40.6 | length mismatch | piece-09-03 tab | 42.8 |
| piece-13-04 | 687 | tab | 43.0 | length mismatch | piece-13-03 edge | 40.7 |
| piece-17-01 | 706 | edge | 17.7 | extra copy: likely misread |   |  |
| piece-17-03 | 716 | tab | 22.6 | length mismatch | piece-16-08 edge | 40.0 |
| piece-24-07 | 785 | edge | 15.4 | unpaired |   |  |
| piece-24-04 | 786 | tab | 24.1 | length mismatch | piece-11-03 edge | 23.0 |
| piece-24-03 | 789 | edge | 18.1 | unpaired |   |  |
| piece-11-06 | 790 | edge | 24.2 | unpaired |   |  |
| piece-05-07 | 792 | edge | 24.3 | unpaired |   |  |
| piece-23-01 | 997 | edge | 36.8 | unpaired |   |  |

## Mirror twins

The model is symmetric: 82 pairs of pieces are mirror images (164 of 178 pieces), found by the lengths of their numbered lines: 7 exact mirrors (outline and tabs match) and 75 mirror variations (same body, tabs on other edges). Of their {paired} mirrored lines, {off} differ in length from their mirror line by more than 1 mm, so one of the two was traced off (`bowser-mirrors.csv`). A twin's clean glue pair also predicts the number on the mirror line; those predictions are applied when clear-cut, and otherwise go to the check page with `mirror` as the reason.


## Likely misreads

47 clear-cut misreads were fixed without asking (marked `applied` in `bowser-misreads.csv`). 30 more numbers that did not pair up sit on a line of the same length as another unpaired number on the other side (edge against tab), and the two numbers look alike. Check them with `make fix` and `app/number-check.html`.

| piece | side | mm | read | suggested | partner | partner mm | why |
|---|---|---:|---|---|---|---:|---|
| piece-04-03 | tab | 29.4 | 406 | 405 | piece-04-01 edge | 29.4 | OCR's other reading |
| piece-09-06 | edge | 46.8 | 999 | 668 | piece-08-02 tab | 46.8 | OCR's other reading |
| piece-15-01 | edge | 30.9 | 260 | 290 | piece-14-03 tab | 30.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-04-08 | edge | 27.4 | 578 | 570 | piece-04-06 tab | 27.5 | OCR's other reading; the read number already pairs elsewhere |
| piece-08-04 | edge | 26.3 | 328 | 376 | piece-16-07 tab | 26.2 | OCR's other reading |
| piece-08-05 | edge | 46.6 | 326 | 325 | piece-09-07 tab | 46.7 | OCR's other reading; the read number already pairs elsewhere |
| piece-11-03 | tab | 31.0 | 13 | 33 | piece-11-01 edge | 31.1 | one digit differs |
| piece-12-07 | edge | 14.8 | 208 | 206 | piece-12-02 tab | 14.8 | OCR's other reading |
| piece-13-03 | tab | 54.3 | 698 | 593 | piece-13-04 edge | 54.2 | OCR's other reading |
| piece-13-03 | edge | 51.6 | 648 | 548 | piece-12-11 tab | 51.7 | OCR's other reading; the read number already pairs elsewhere |
| piece-17-06 | edge | 59.2 | 628 | 698 | piece-10-04 tab | 59.3 | one digit differs; the read number already pairs elsewhere |
| piece-04-07 | edge | 32.5 | 731 | 281 | piece-24-05 tab | 32.6 | OCR's other reading |
| piece-08-01 | tab | 23.6 | 588 | 689 | piece-08-04 edge | 23.4 | OCR's other reading; the read number already pairs elsewhere |
| piece-16-03 | tab | 44.6 | 869 | 369 | piece-14-06 edge | 44.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-18-02 | tab | 37.2 | 182 | 192 | piece-18-04 edge | 37.0 | OCR's other reading |
| piece-04-03 | tab | 37.6 | 456 | 406 | piece-12-03 edge | 37.9 | OCR's other reading; the read number already pairs elsewhere |
| piece-11-02 | edge | 23.9 | 48 | 95 | piece-18-03 tab | 23.5 | OCR's other reading |
| piece-15-06 | edge | 17.6 | 206 | 208 | piece-14-07 tab | 17.9 | OCR's other reading |
| piece-09-05 | edge | 51.3 | 286 | 562 | piece-09-04 tab | 51.8 | OCR's other reading |
| piece-24-08 | tab | 13.3 | 288 | 286 | piece-16-04 edge | 13.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-15-06 | edge | 18.5 | 582 | 562 | piece-15-07 tab | 17.9 | OCR's other reading; the read number already pairs elsewhere |
| piece-16-03 | tab | 22.4 | 386 | 786 | piece-11-03 edge | 23.0 | one digit differs; the read number already pairs elsewhere |
| piece-23-03 | tab | 36.8 | 235 | 265 | piece-07-08 edge | 36.2 | OCR's other reading |
| piece-04-07 | edge | 23.4 | 784 | 786 | piece-24-04 tab | 24.1 | OCR's other reading |
| piece-09-01 | edge | 42.3 | 657 | 687 | piece-13-04 tab | 43.0 | OCR's other reading |
| piece-24-03 | edge | 29.7 | 18 | 618 | piece-07-01 tab | 29.0 | a digit dropped or added; the read number already pairs elsewhere |
| piece-04-07 | tab | 28.9 | 422 | 482 | piece-21-03 edge | 28.0 | one digit differs; the read number already pairs elsewhere |
| piece-15-07 | tab | 18.7 | 580 | 58 | piece-11-05 edge | 17.8 | a digit dropped or added; the read number already pairs elsewhere |
| piece-06-06 | tab | 38.3 | 316 | 318 | piece-07-07 edge | 37.4 | OCR's other reading |
| piece-24-15 | edge | 23.6 | 216 | 716 | piece-17-03 tab | 22.6 | OCR's other reading |

Full tables: `bowser-edges.csv`, `bowser-misreads.csv`.
