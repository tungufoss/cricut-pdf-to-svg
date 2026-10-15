# Bowser

1570 printed numbers on 178 pieces. 621 numbers form a clean pair (one plain edge, one tab, lengths within 1 mm); 328 labels need a look.

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
| numbers | 1570 read, 287 uncertain (orange in the SVG) |
| pieces to check | 144 marked ⚠ in Inkscape |
| paper colour | footers disagree with the YAML: pages 14–23 say beige (YAML: yellow); page 24 says white (YAML: black) |
| nesting on sheets | not started |

## Edge numbers

| status | labels | meaning |
|---|---:|---|
| ok | 1242 | partner found, one tab and one plain edge, same length |
| length mismatch | 144 | partner found but the marked lines differ in length: misread number or traced line |
| line not found | 64 | no cut edge or fold next to the number |
| unpaired | 51 | no other copy of this number: likely misread |
| extra copy: likely misread | 38 | number read more than twice; the other copies already form a clean pair |
| both tabs | 16 | both copies sit on a tab fold |
| no tab | 12 | neither copy sits on a tab fold |
| printed 3 times | 3 | number read more than twice: some are misread |

## Pages

| page | config material | footer says | pieces | ok | check |
|---|---|---|---:|---:|---:|
| 04 | red | red | 8 | 61 | 14 |
| 05 | red | red | 8 | 55 | 20 |
| 06 | red | red | 6 | 46 | 12 |
| 07 | red | red | 10 | 56 | 20 |
| 08 | red | red | 6 | 46 | 10 |
| 09 | red | red | 7 | 37 | 21 |
| 10 | red | red | 7 | 49 | 5 |
| 11 | green | green | 11 | 61 | 29 |
| 12 | green | green | 11 | 59 | 31 |
| 13 | green | green | 4 | 24 | 6 |
| 14 | yellow | beige ⚠ | 10 | 83 | 9 |
| 15 | yellow | beige ⚠ | 10 | 77 | 15 |
| 16 | yellow | beige ⚠ | 10 | 65 | 26 |
| 17 | yellow | beige ⚠ | 10 | 63 | 28 |
| 18 | yellow | beige ⚠ | 8 | 65 | 17 |
| 19 | yellow | beige ⚠ | 8 | 62 | 20 |
| 20 | yellow | beige ⚠ | 8 | 68 | 8 |
| 21 | yellow | beige ⚠ | 8 | 73 | 3 |
| 22 | yellow | beige ⚠ | 6 | 58 | 0 |
| 23 | yellow | beige ⚠ | 6 | 54 | 4 |
| 24 | black | white ⚠ | 16 | 80 | 30 |

## Pieces to check

Pieces listed by how many of their numbers need a look.

| piece | ok | check | numbers to check |
|---|---:|---:|---|
| piece-12-04 | 1 | 9 | 5 (unpaired), 6 (line not found), 7 (line not found), 014 (unpaired), 17 (extra copy: likely misread), 61 (line not found), 420 (line not found), 693 (length mismatch), 742 (length mismatch) |
| piece-12-06 | 1 | 7 | 040 (line not found), 511 (length mismatch), 546 (unpaired), 593 (line not found), 594 (unpaired), 595 (length mismatch), 645 (unpaired) |
| piece-11-05 | 4 | 6 | 58 (line not found), 770 (line not found), 777 (line not found), 778 (line not found), 781 (length mismatch), 793 (unpaired) |
| piece-16-10 | 1 | 6 | 066 (unpaired), 68 (line not found), 283 (length mismatch), 381 (length mismatch), 385 (length mismatch), 448 (extra copy: likely misread) |
| piece-17-01 | 3 | 6 | 706 (extra copy: likely misread), 723 (unpaired), 726 (line not found), 727 (length mismatch), 729 (length mismatch), 734 (length mismatch) |
| piece-11-02 | 4 | 5 | 000 (unpaired), 10 (length mismatch), 11 (line not found), 040 (line not found), 48 (extra copy: likely misread) |
| piece-05-01 | 7 | 5 | 10 (length mismatch), 46 (length mismatch), 47 (line not found), 51 (length mismatch), 57 (unpaired) |
| piece-17-09 | 2 | 5 | 15 (line not found), 95 (line not found), 655 (unpaired), 729 (length mismatch), 734 (length mismatch) |
| piece-19-04 | 9 | 5 | 398 (length mismatch), 400 (line not found), 454 (line not found), 457 (line not found), 460 (length mismatch) |
| piece-16-03 | 9 | 5 | 370 (length mismatch), 372 (length mismatch), 386 (printed 3 times), 869 (extra copy: likely misread), 883 (no tab) |
| piece-24-05 | 1 | 5 | 261 (extra copy: likely misread), 281 (both tabs), 283 (length mismatch), 370 (length mismatch), 384 (unpaired) |
| piece-07-01 | 5 | 5 | 273 (both tabs), 392 (length mismatch), 618 (length mismatch), 619 (length mismatch), 672 (unpaired) |
| piece-04-07 | 4 | 5 | 395 (length mismatch), 420 (line not found), 422 (extra copy: likely misread), 731 (no tab), 784 (unpaired) |
| piece-09-03 | 4 | 5 | 658 (length mismatch), 660 (length mismatch), 668 (both tabs), 677 (length mismatch), 883 (no tab) |
| piece-12-05 | 9 | 4 | 4 (unpaired), 7 (line not found), 742 (length mismatch), 745 (line not found) |
| piece-11-03 | 5 | 4 | 13 (line not found), 41 (length mismatch), 414 (extra copy: likely misread), 786 (length mismatch) |
| piece-06-03 | 7 | 4 | 33 (length mismatch), 34 (unpaired), 316 (length mismatch), 386 (printed 3 times) |
| piece-07-07 | 6 | 4 | 272 (length mismatch), 273 (both tabs), 274 (length mismatch), 318 (unpaired) |
| piece-05-03 | 8 | 4 | 54 (length mismatch), 58 (line not found), 81 (extra copy: likely misread), 87 (unpaired) |
| piece-18-06 | 7 | 4 | 67 (extra copy: likely misread), 90 (line not found), 93 (length mismatch), 136 (line not found) |
| piece-11-06 | 4 | 4 | 147 (length mismatch), 757 (length mismatch), 777 (line not found), 790 (unpaired) |
| piece-15-06 | 7 | 4 | 206 (length mismatch), 564 (line not found), 580 (extra copy: likely misread), 582 (extra copy: likely misread) |
| piece-12-07 | 3 | 4 | 208 (length mismatch), 545 (unpaired), 548 (line not found), 695 (length mismatch) |
| piece-16-02 | 5 | 4 | 378 (unpaired), 379 (line not found), 381 (length mismatch), 385 (length mismatch) |
| piece-08-05 | 5 | 4 | 305 (both tabs), 312 (length mismatch), 314 (length mismatch), 326 (extra copy: likely misread) |
| piece-17-03 | 10 | 4 | 716 (length mismatch), 718 (length mismatch), 726 (line not found), 732 (unpaired) |
| piece-19-01 | 4 | 4 | 397 (line not found), 398 (length mismatch), 400 (line not found), 898 (unpaired) |
| piece-19-07 | 7 | 4 | 454 (line not found), 460 (length mismatch), 462 (extra copy: likely misread), 496 (line not found) |
| piece-13-03 | 6 | 4 | 648 (extra copy: likely misread), 687 (length mismatch), 695 (length mismatch), 698 (both tabs) |
| piece-07-03 | 5 | 4 | 555 (both tabs), 651 (length mismatch), 652 (length mismatch), 653 (length mismatch) |
| piece-05-02 | 4 | 3 | 6 (line not found), 47 (line not found), 51 (length mismatch) |
| piece-11-04 | 10 | 3 | 11 (line not found), 745 (line not found), 770 (line not found) |
| piece-06-06 | 6 | 3 | 13 (line not found), 272 (length mismatch), 316 (length mismatch) |
| piece-24-03 | 4 | 3 | 18 (extra copy: likely misread), 755 (extra copy: likely misread), 789 (unpaired) |
| piece-05-05 | 7 | 3 | 40 (length mismatch), 41 (length mismatch), 61 (line not found) |
| piece-05-07 | 6 | 3 | 40 (length mismatch), 778 (line not found), 792 (unpaired) |
| piece-24-12 | 5 | 3 | 044 (unpaired), 457 (line not found), 662 (extra copy: likely misread) |
| piece-24-15 | 5 | 3 | 46 (length mismatch), 216 (length mismatch), 216 (length mismatch) |
| piece-18-07 | 8 | 3 | 106 (line not found), 189 (length mismatch), 195 (length mismatch) |
| piece-18-04 | 5 | 3 | 189 (length mismatch), 192 (unpaired), 482 (no tab) |
| piece-16-07 | 3 | 3 | 277 (length mismatch), 372 (length mismatch), 376 (unpaired) |
| piece-09-06 | 5 | 3 | 281 (both tabs), 651 (length mismatch), 999 (length mismatch) |
| piece-09-05 | 5 | 3 | 286 (no tab), 300 (length mismatch), 323 (length mismatch) |
| piece-09-04 | 6 | 3 | 300 (length mismatch), 323 (length mismatch), 562 (both tabs) |
| piece-09-07 | 5 | 3 | 312 (length mismatch), 314 (length mismatch), 325 (unpaired) |
| piece-24-16 | 4 | 3 | 571 (length mismatch), 571 (length mismatch), 576 (extra copy: likely misread) |
| piece-06-04 | 8 | 3 | 380 (extra copy: likely misread), 386 (printed 3 times), 392 (length mismatch) |
| piece-17-07 | 3 | 3 | 444 (extra copy: likely misread), 629 (unpaired), 730 (unpaired) |
| piece-17-06 | 1 | 3 | 628 (extra copy: likely misread), 735 (line not found), 944 (unpaired) |
| piece-24-06 | 3 | 3 | 631 (unpaired), 718 (length mismatch), 727 (length mismatch) |
| piece-09-02 | 5 | 3 | 652 (length mismatch), 658 (length mismatch), 677 (length mismatch) |
| piece-11-01 | 4 | 2 | 00 (unpaired), 33 (length mismatch) |
| piece-04-02 | 10 | 2 | 03 (unpaired), 412 (length mismatch) |
| piece-20-07 | 7 | 2 | 66 (extra copy: likely misread), 93 (length mismatch) |
| piece-11-07 | 5 | 2 | 757 (length mismatch), 760 (extra copy: likely misread) |
| piece-24-04 | 6 | 2 | 786 (length mismatch), 794 (unpaired) |
| piece-18-03 | 12 | 2 | 90 (line not found), 95 (line not found) |
| piece-20-08 | 4 | 2 | 67 (extra copy: likely misread), 68 (line not found) |
| piece-18-08 | 9 | 2 | 118 (length mismatch), 136 (line not found) |
| piece-20-02 | 8 | 2 | 118 (length mismatch), 129 (length mismatch) |
| piece-16-04 | 13 | 2 | 286 (no tab), 379 (line not found) |
| piece-16-09 | 10 | 2 | 182 (both tabs), 195 (length mismatch) |
| piece-14-06 | 12 | 2 | 171 (length mismatch), 369 (unpaired) |
| piece-14-07 | 9 | 2 | 208 (length mismatch), 564 (line not found) |
| piece-24-07 | 6 | 2 | 781 (length mismatch), 785 (unpaired) |
| piece-23-03 | 7 | 2 | 229 (length mismatch), 235 (unpaired) |
| piece-12-08 | 5 | 2 | 308 (length mismatch), 659 (no tab) |
| piece-04-06 | 6 | 2 | 570 (length mismatch), 577 (length mismatch) |
| piece-17-05 | 10 | 2 | 470 (length mismatch), 556 (no tab) |
| piece-07-10 | 4 | 2 | 265 (length mismatch), 274 (length mismatch) |
| piece-24-01 | 4 | 2 | 277 (length mismatch), 280 (unpaired) |
| piece-10-05 | 6 | 2 | 328 (length mismatch), 752 (extra copy: likely misread) |
| piece-08-04 | 9 | 2 | 328 (length mismatch), 689 (unpaired) |
| piece-08-02 | 7 | 2 | 668 (both tabs), 860 (unpaired) |
| piece-06-05 | 7 | 2 | 618 (length mismatch), 947 (unpaired) |
| piece-13-04 | 3 | 2 | 593 (line not found), 687 (length mismatch) |
| piece-16-06 | 2 | 2 | 341 (line not found), 735 (line not found) |
| piece-19-08 | 9 | 2 | 477 (length mismatch), 496 (line not found) |
| piece-19-06 | 9 | 2 | 470 (length mismatch), 556 (no tab) |
| piece-19-03 | 6 | 2 | 539 (length mismatch), 551 (length mismatch) |
| piece-21-03 | 8 | 2 | 477 (length mismatch), 482 (no tab) |
| piece-15-02 | 7 | 2 | 511 (length mismatch), 714 (line not found) |
| piece-15-07 | 8 | 2 | 562 (both tabs), 580 (extra copy: likely misread) |
| piece-17-04 | 13 | 2 | 708 (unpaired), 714 (line not found) |
| piece-15-10 | 9 | 2 | 527 (length mismatch), 659 (no tab) |
| piece-17-10 | 10 | 2 | 551 (length mismatch), 555 (both tabs) |
| piece-15-08 | 12 | 2 | 527 (length mismatch), 536 (unpaired) |
| piece-12-11 | 4 | 2 | 548 (line not found), 595 (length mismatch) |
| piece-07-02 | 4 | 2 | 619 (length mismatch), 685 (unpaired) |
| piece-07-04 | 4 | 2 | 653 (length mismatch), 660 (length mismatch) |
| piece-24-02 | 4 | 2 | 623 (extra copy: likely misread), 731 (no tab) |
| piece-11-09 | 6 | 1 | 224 (length mismatch) |
| piece-16-01 | 4 | 1 | 15 (line not found) |
| piece-05-06 | 7 | 1 | 224 (length mismatch) |
| piece-11-10 | 7 | 1 | 768 (extra copy: likely misread) |
| piece-05-04 | 8 | 1 | 54 (length mismatch) |
| piece-12-01 | 5 | 1 | 308 (length mismatch) |
| piece-18-01 | 7 | 1 | 397 (line not found) |
| piece-18-05 | 12 | 1 | 106 (line not found) |
| piece-20-03 | 10 | 1 | 85 (extra copy: likely misread) |
| piece-18-02 | 5 | 1 | 182 (both tabs) |
| piece-20-04 | 9 | 1 | 129 (length mismatch) |
| piece-14-04 | 6 | 1 | 137 (length mismatch) |
| piece-14-05 | 4 | 1 | 137 (length mismatch) |
| piece-14-01 | 8 | 1 | 147 (length mismatch) |
| piece-04-01 | 6 | 1 | 456 (extra copy: likely misread) |
| piece-04-03 | 11 | 1 | 406 (extra copy: likely misread) |
| piece-14-10 | 10 | 1 | 171 (length mismatch) |
| piece-16-08 | 6 | 1 | 716 (length mismatch) |
| piece-24-08 | 5 | 1 | 288 (extra copy: likely misread) |
| piece-12-02 | 8 | 1 | 206 (length mismatch) |
| piece-04-05 | 9 | 1 | 395 (length mismatch) |
| piece-14-03 | 7 | 1 | 290 (unpaired) |
| piece-11-11 | 5 | 1 | 762 (unpaired) |
| piece-23-01 | 10 | 1 | 997 (unpaired) |
| piece-23-05 | 10 | 1 | 229 (length mismatch) |
| piece-04-08 | 7 | 1 | 578 (extra copy: likely misread) |
| piece-12-09 | 6 | 1 | 577 (length mismatch) |
| piece-15-01 | 7 | 1 | 260 (extra copy: likely misread) |
| piece-04-04 | 8 | 1 | 412 (length mismatch) |
| piece-07-08 | 6 | 1 | 265 (length mismatch) |
| piece-08-06 | 7 | 1 | 305 (both tabs) |
| piece-08-01 | 10 | 1 | 588 (extra copy: likely misread) |
| piece-10-02 | 6 | 1 | 341 (line not found) |
| piece-10-01 | 8 | 1 | 570 (length mismatch) |
| piece-21-07 | 8 | 1 | 452 (unpaired) |
| piece-24-09 | 6 | 1 | 750 (unpaired) |
| piece-15-04 | 6 | 1 | 616 (extra copy: likely misread) |
| piece-15-09 | 9 | 1 | 616 (extra copy: likely misread) |
| piece-17-08 | 6 | 1 | 999 (length mismatch) |
| piece-19-02 | 5 | 1 | 539 (length mismatch) |
| piece-09-01 | 7 | 1 | 693 (length mismatch) |
| piece-10-04 | 6 | 1 | 698 (both tabs) |

## Hand corrections that still do not pair

472 numbers were set by hand; 122 of them still do not form a clean pair, so the correction, its partner or the traced line is likely off. They come first on the check page.

| piece | number | side | mm | status | partner | partner mm |
|---|---|---|---:|---|---|---:|
| piece-12-05 | 4 | tab | 15.8 | unpaired |   |  |
| piece-12-04 | 5 | none | 0.0 | unpaired |   |  |
| piece-05-02 | 6 | none | 0.0 | line not found | piece-12-04 none | 0.0 |
| piece-12-04 | 6 | none | 0.0 | line not found | piece-05-02 none | 0.0 |
| piece-12-04 | 7 | none | 0.0 | line not found | piece-12-05 none | 0.0 |
| piece-12-05 | 7 | none | 0.0 | line not found | piece-12-04 none | 0.0 |
| piece-05-01 | 10 | edge | 91.1 | length mismatch | piece-11-02 tab | 37.8 |
| piece-11-02 | 10 | tab | 37.8 | length mismatch | piece-05-01 edge | 91.1 |
| piece-11-02 | 11 | tab | 15.6 | line not found | piece-11-04 none | 0.0 |
| piece-11-04 | 11 | none | 0.0 | line not found | piece-11-02 tab | 15.6 |
| piece-11-03 | 13 | tab | 31.0 | line not found | piece-06-06 none | 0.0 |
| piece-16-01 | 15 | edge | 51.9 | line not found | piece-17-09 none | 0.0 |
| piece-24-03 | 18 | edge | 56.4 | extra copy: likely misread |   |  |
| piece-06-03 | 33 | tab | 34.2 | length mismatch | piece-11-01 edge | 31.1 |
| piece-11-01 | 33 | edge | 31.1 | length mismatch | piece-06-03 tab | 34.2 |
| piece-06-03 | 34 | none | 0.0 | unpaired |   |  |
| piece-05-05 | 40 | tab | 31.0 | length mismatch | piece-05-07 edge | 38.9 |
| piece-05-07 | 40 | edge | 38.9 | length mismatch | piece-05-05 tab | 31.0 |
| piece-05-05 | 41 | tab | 20.6 | length mismatch | piece-11-03 edge | 43.6 |
| piece-11-03 | 41 | edge | 43.6 | length mismatch | piece-05-05 tab | 20.6 |
| piece-05-01 | 47 | tab | 29.2 | line not found | piece-05-02 none | 0.0 |
| piece-05-02 | 47 | none | 0.0 | line not found | piece-05-01 tab | 29.2 |
| piece-11-02 | 48 | edge | 23.9 | extra copy: likely misread |   |  |
| piece-05-01 | 51 | edge | 91.1 | length mismatch | piece-05-02 tab | 54.2 |
| piece-05-02 | 51 | tab | 54.2 | length mismatch | piece-05-01 edge | 91.1 |
| piece-05-03 | 54 | edge | 35.0 | length mismatch | piece-05-04 tab | 26.8 |
| piece-05-04 | 54 | tab | 26.8 | length mismatch | piece-05-03 edge | 35.0 |
| piece-05-03 | 58 | none | 0.0 | line not found | piece-11-05 edge | 17.8 |
| piece-11-05 | 58 | edge | 17.8 | line not found | piece-05-03 none | 0.0 |
| piece-05-05 | 61 | edge | 27.7 | line not found | piece-12-04 none | 0.0 |
| piece-20-07 | 66 | edge | 38.9 | extra copy: likely misread |   |  |
| piece-18-06 | 67 | edge | 30.9 | extra copy: likely misread |   |  |
| piece-20-08 | 67 | tab | 31.1 | extra copy: likely misread |   |  |
| piece-20-08 | 68 | tab | 38.9 | line not found | piece-16-10 none | 0.0 |
| piece-05-03 | 81 | none | 0.0 | extra copy: likely misread |   |  |
| piece-20-03 | 85 | edge | 23.4 | extra copy: likely misread |   |  |
| piece-05-03 | 87 | tab | 50.9 | unpaired |   |  |
| piece-18-03 | 95 | tab | 23.5 | line not found | piece-17-09 none | 0.0 |
| piece-18-05 | 106 | none | 0.0 | line not found | piece-18-07 edge | 17.0 |
| piece-18-07 | 106 | edge | 17.0 | line not found | piece-18-05 none | 0.0 |
| piece-18-08 | 118 | edge | 53.6 | length mismatch | piece-20-02 tab | 45.9 |
| piece-20-02 | 118 | tab | 45.9 | length mismatch | piece-18-08 edge | 53.6 |
| piece-20-02 | 129 | edge | 19.0 | length mismatch | piece-20-04 tab | 20.2 |
| piece-18-06 | 136 | edge | 17.9 | line not found | piece-18-08 none | 0.0 |
| piece-18-08 | 136 | none | 0.0 | line not found | piece-18-06 edge | 17.9 |
| piece-14-04 | 137 | edge | 20.9 | length mismatch | piece-14-05 tab | 33.9 |
| piece-14-05 | 137 | tab | 33.9 | length mismatch | piece-14-04 edge | 20.9 |
| piece-11-06 | 147 | edge | 38.4 | length mismatch | piece-14-01 tab | 72.0 |
| piece-14-01 | 147 | tab | 72.0 | length mismatch | piece-11-06 edge | 38.4 |
| piece-14-06 | 171 | edge | 59.6 | length mismatch | piece-14-10 tab | 51.5 |
| piece-14-10 | 171 | tab | 51.5 | length mismatch | piece-14-06 edge | 59.6 |
| piece-18-04 | 189 | tab | 42.5 | length mismatch | piece-18-07 edge | 93.7 |
| piece-18-07 | 189 | edge | 93.7 | length mismatch | piece-18-04 tab | 42.5 |
| piece-18-04 | 192 | edge | 37.0 | unpaired |   |  |
| piece-16-09 | 195 | tab | 51.3 | length mismatch | piece-18-07 edge | 93.7 |
| piece-18-07 | 195 | edge | 93.7 | length mismatch | piece-16-09 tab | 51.3 |
| piece-15-06 | 206 | edge | 17.6 | length mismatch | piece-12-02 tab | 14.8 |
| piece-14-07 | 208 | tab | 17.9 | length mismatch | piece-12-07 edge | 14.8 |
| piece-24-15 | 216 | edge | 23.6 | length mismatch | piece-24-15 tab | 25.7 |
| piece-05-06 | 224 | tab | 47.9 | length mismatch | piece-11-09 edge | 54.9 |
| piece-11-09 | 224 | edge | 54.9 | length mismatch | piece-05-06 tab | 47.9 |
| piece-23-03 | 229 | edge | 35.1 | length mismatch | piece-23-05 tab | 37.0 |
| piece-23-05 | 229 | tab | 37.0 | length mismatch | piece-23-03 edge | 35.1 |
| piece-24-05 | 261 | edge | 18.7 | extra copy: likely misread |   |  |
| piece-07-08 | 265 | edge | 36.2 | length mismatch | piece-07-10 tab | 37.7 |
| piece-06-06 | 272 | edge | 20.8 | length mismatch | piece-07-07 tab | 29.0 |
| piece-07-07 | 272 | tab | 29.0 | length mismatch | piece-06-06 edge | 20.8 |
| piece-07-01 | 273 | tab | 29.0 | both tabs | piece-07-07 tab | 29.0 |
| piece-07-07 | 273 | tab | 29.0 | both tabs | piece-07-01 tab | 29.0 |
| piece-07-07 | 274 | tab | 125.5 | length mismatch | piece-07-10 edge | 61.1 |
| piece-07-10 | 274 | edge | 61.1 | length mismatch | piece-07-07 tab | 125.5 |
| piece-16-07 | 277 | edge | 32.2 | length mismatch | piece-24-01 tab | 24.0 |
| piece-24-01 | 277 | tab | 24.0 | length mismatch | piece-16-07 edge | 32.2 |
| piece-24-01 | 280 | tab | 21.4 | unpaired |   |  |
| piece-16-10 | 283 | edge | 17.2 | length mismatch | piece-24-05 tab | 18.3 |
| piece-24-05 | 283 | tab | 18.3 | length mismatch | piece-16-10 edge | 17.2 |
| piece-16-04 | 286 | edge | 13.8 | no tab | piece-09-05 edge | 62.9 |
| piece-24-08 | 288 | tab | 13.3 | extra copy: likely misread |   |  |
| piece-09-04 | 300 | tab | 43.0 | length mismatch | piece-09-05 edge | 60.4 |
| piece-09-05 | 300 | edge | 60.4 | length mismatch | piece-09-04 tab | 43.0 |
| piece-08-05 | 305 | tab | 54.2 | both tabs | piece-08-06 tab | 29.7 |
| piece-08-06 | 305 | tab | 29.7 | both tabs | piece-08-05 tab | 54.2 |
| piece-12-01 | 308 | tab | 42.2 | length mismatch | piece-12-08 edge | 39.9 |
| piece-12-08 | 308 | edge | 39.9 | length mismatch | piece-12-01 tab | 42.2 |
| piece-08-05 | 312 | tab | 54.2 | length mismatch | piece-09-07 edge | 25.8 |
| piece-09-07 | 312 | edge | 25.8 | length mismatch | piece-08-05 tab | 54.2 |
| piece-08-05 | 314 | tab | 14.9 | length mismatch | piece-09-07 edge | 22.9 |
| piece-09-07 | 314 | edge | 22.9 | length mismatch | piece-08-05 tab | 14.9 |
| piece-06-03 | 316 | edge | 37.3 | length mismatch | piece-06-06 tab | 38.3 |
| piece-06-06 | 316 | tab | 38.3 | length mismatch | piece-06-03 edge | 37.3 |
| piece-07-07 | 318 | edge | 37.4 | unpaired |   |  |
| piece-09-04 | 323 | edge | 56.1 | length mismatch | piece-09-05 tab | 50.6 |
| piece-09-05 | 323 | tab | 50.6 | length mismatch | piece-09-04 edge | 56.1 |
| piece-08-04 | 328 | edge | 26.3 | length mismatch | piece-10-05 tab | 25.1 |
| piece-10-05 | 328 | tab | 25.1 | length mismatch | piece-08-04 edge | 26.3 |
| piece-10-02 | 341 | none | 0.0 | line not found | piece-16-06 edge | 58.4 |
| piece-16-06 | 341 | edge | 58.4 | line not found | piece-10-02 none | 0.0 |
| piece-16-07 | 376 | tab | 26.2 | unpaired |   |  |
| piece-16-10 | 381 | tab | 18.0 | length mismatch | piece-16-02 edge | 41.1 |
| piece-06-03 | 386 | edge | 54.8 | printed 3 times |   |  |
| piece-07-01 | 392 | edge | 42.9 | length mismatch | piece-06-04 tab | 40.2 |
| piece-04-04 | 412 | tab | 26.7 | length mismatch | piece-04-02 edge | 35.0 |
| piece-04-07 | 422 | tab | 28.9 | extra copy: likely misread |   |  |
| piece-24-12 | 457 | none | 0.0 | line not found | piece-19-04 tab | 23.9 |
| piece-21-03 | 482 | edge | 28.0 | no tab | piece-18-04 edge | 37.4 |
| piece-17-05 | 556 | edge | 29.0 | no tab | piece-19-06 edge | 49.1 |
| piece-15-07 | 562 | tab | 17.9 | both tabs | piece-09-04 tab | 51.8 |
| piece-15-06 | 580 | edge | 18.8 | extra copy: likely misread |   |  |
| piece-15-07 | 580 | tab | 18.7 | extra copy: likely misread |   |  |
| piece-15-06 | 582 | edge | 18.5 | extra copy: likely misread |   |  |
| piece-07-01 | 618 | tab | 29.0 | length mismatch | piece-06-05 edge | 12.9 |
| piece-09-02 | 658 | edge | 60.9 | length mismatch | piece-09-03 tab | 42.8 |
| piece-13-04 | 687 | tab | 43.0 | length mismatch | piece-13-03 edge | 40.7 |
| piece-17-01 | 706 | edge | 17.7 | extra copy: likely misread |   |  |
| piece-17-03 | 716 | tab | 22.6 | length mismatch | piece-16-08 edge | 40.0 |
| piece-17-09 | 729 | tab | 17.9 | length mismatch | piece-17-01 edge | 41.1 |
| piece-24-07 | 785 | edge | 23.2 | unpaired |   |  |
| piece-24-04 | 786 | tab | 24.1 | length mismatch | piece-11-03 edge | 43.6 |
| piece-24-03 | 789 | edge | 18.1 | unpaired |   |  |
| piece-11-06 | 790 | edge | 24.2 | unpaired |   |  |
| piece-05-07 | 792 | edge | 24.3 | unpaired |   |  |
| piece-23-01 | 997 | edge | 36.8 | unpaired |   |  |

## Mirror twins

The model is symmetric: 76 pairs of pieces are mirror images (152 of 178 pieces), found by the lengths of their numbered lines: 7 exact mirrors (outline and tabs match) and 69 mirror variations (same body, tabs on other edges). Of their {paired} mirrored lines, {off} differ in length from their mirror line by more than 1 mm, so one of the two was traced off (`bowser-mirrors.csv`). A twin's clean glue pair also predicts the number on the mirror line; those predictions are applied when clear-cut, and otherwise go to the check page with `mirror` as the reason.


## Likely misreads

43 clear-cut misreads were fixed without asking (marked `applied` in `bowser-misreads.csv`). 32 more numbers that did not pair up sit on a line of the same length as another unpaired number on the other side (edge against tab), and the two numbers look alike. Check them with `make fix` and `app/number-check.html`.

| piece | side | mm | read | suggested | partner | partner mm | why |
|---|---|---:|---|---|---|---:|---|
| piece-05-01 | edge | 50.9 | 57 | 87 | piece-05-03 tab | 50.9 | one digit differs |
| piece-09-03 | tab | 61.8 | 668 | 659 | piece-12-08 edge | 61.8 | OCR's other reading |
| piece-09-06 | edge | 46.8 | 999 | 668 | piece-08-02 tab | 46.8 | OCR's other reading |
| piece-15-01 | edge | 30.9 | 260 | 290 | piece-14-03 tab | 30.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-20-07 | edge | 38.9 | 66 | 68 | piece-20-08 tab | 38.9 | OCR's other reading; the read number already pairs elsewhere |
| piece-04-08 | edge | 27.4 | 578 | 570 | piece-04-06 tab | 27.5 | OCR's other reading; the read number already pairs elsewhere |
| piece-08-04 | edge | 26.3 | 328 | 376 | piece-16-07 tab | 26.2 | OCR's other reading |
| piece-08-05 | edge | 46.6 | 326 | 325 | piece-09-07 tab | 46.7 | OCR's other reading; the read number already pairs elsewhere |
| piece-11-03 | tab | 31.0 | 13 | 33 | piece-11-01 edge | 31.1 | one digit differs |
| piece-12-07 | edge | 14.8 | 208 | 206 | piece-12-02 tab | 14.8 | OCR's other reading |
| piece-12-11 | edge | 50.7 | 595 | 695 | piece-13-03 tab | 50.8 | OCR's other reading |
| piece-13-03 | tab | 54.3 | 698 | 593 | piece-13-04 edge | 54.2 | OCR's other reading |
| piece-13-03 | edge | 51.6 | 648 | 548 | piece-12-11 tab | 51.7 | OCR's other reading; the read number already pairs elsewhere |
| piece-17-06 | edge | 59.2 | 628 | 698 | piece-10-04 tab | 59.3 | one digit differs; the read number already pairs elsewhere |
| piece-20-03 | edge | 23.4 | 85 | 385 | piece-16-10 tab | 23.3 | a digit dropped or added; the read number already pairs elsewhere |
| piece-08-01 | tab | 23.6 | 588 | 689 | piece-08-04 edge | 23.4 | OCR's other reading; the read number already pairs elsewhere |
| piece-15-07 | tab | 18.7 | 580 | 582 | piece-15-06 edge | 18.5 | OCR's other reading; the read number already pairs elsewhere |
| piece-16-03 | tab | 44.6 | 869 | 369 | piece-14-06 edge | 44.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-18-02 | tab | 37.2 | 182 | 192 | piece-18-04 edge | 37.0 | OCR's other reading |
| piece-11-02 | edge | 23.9 | 48 | 95 | piece-18-03 tab | 23.5 | OCR's other reading; the read number already pairs elsewhere |
| piece-15-06 | edge | 17.6 | 206 | 208 | piece-14-07 tab | 17.9 | OCR's other reading |
| piece-15-10 | edge | 51.6 | 659 | 652 | piece-07-03 tab | 51.9 | one digit differs |
| piece-17-09 | tab | 17.9 | 729 | 789 | piece-24-03 edge | 18.1 | one digit differs |
| piece-06-04 | tab | 43.2 | 386 | 786 | piece-11-03 edge | 43.6 | one digit differs |
| piece-24-08 | tab | 13.3 | 288 | 286 | piece-16-04 edge | 13.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-23-03 | tab | 36.8 | 235 | 265 | piece-07-08 edge | 36.2 | OCR's other reading |
| piece-24-05 | edge | 18.7 | 261 | 381 | piece-16-10 tab | 18.0 | OCR's other reading; the read number already pairs elsewhere |
| piece-04-07 | tab | 28.9 | 422 | 482 | piece-21-03 edge | 28.0 | one digit differs; the read number already pairs elsewhere |
| piece-06-06 | tab | 38.3 | 316 | 318 | piece-07-07 edge | 37.4 | OCR's other reading |
| piece-09-07 | edge | 25.8 | 312 | 412 | piece-04-04 tab | 26.7 | one digit differs |
| piece-24-07 | edge | 23.2 | 785 | 786 | piece-24-04 tab | 24.1 | OCR's other reading |
| piece-24-15 | edge | 23.6 | 216 | 716 | piece-17-03 tab | 22.6 | OCR's other reading |

Full tables: `bowser-edges.csv`, `bowser-misreads.csv`.
