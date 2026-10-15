# Bowser

1570 printed numbers on 178 pieces. 565 numbers form a clean pair (one plain edge, one tab, lengths within 1 mm); 440 labels need a look.

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
| numbers | 1570 read, 388 uncertain (orange in the SVG) |
| pieces to check | 160 marked ⚠ in Inkscape |
| paper colour | footers disagree with the YAML: pages 14–23 say beige (YAML: yellow); page 24 says white (YAML: black) |
| nesting on sheets | not started |

## Edge numbers

| status | labels | meaning |
|---|---:|---|
| ok | 1130 | partner found, one tab and one plain edge, same length |
| length mismatch | 180 | partner found but the marked lines differ in length: misread number or traced line |
| unpaired | 72 | no other copy of this number: likely misread |
| extra copy: likely misread | 60 | number read more than twice; the other copies already form a clean pair |
| line not found | 60 | no cut edge or fold next to the number |
| no tab | 34 | neither copy sits on a tab fold |
| both tabs | 28 | both copies sit on a tab fold |
| printed 3 times | 6 | number read more than twice: some are misread |

## Pages

| page | config material | footer says | pieces | ok | check |
|---|---|---|---:|---:|---:|
| 04 | red | red | 8 | 55 | 20 |
| 05 | red | red | 8 | 52 | 23 |
| 06 | red | red | 6 | 44 | 14 |
| 07 | red | red | 10 | 55 | 21 |
| 08 | red | red | 6 | 41 | 15 |
| 09 | red | red | 7 | 29 | 29 |
| 10 | red | red | 7 | 44 | 10 |
| 11 | green | green | 11 | 53 | 37 |
| 12 | green | green | 11 | 56 | 34 |
| 13 | green | green | 4 | 24 | 6 |
| 14 | yellow | beige ⚠ | 10 | 73 | 19 |
| 15 | yellow | beige ⚠ | 10 | 70 | 22 |
| 16 | yellow | beige ⚠ | 10 | 58 | 33 |
| 17 | yellow | beige ⚠ | 10 | 55 | 36 |
| 18 | yellow | beige ⚠ | 8 | 61 | 21 |
| 19 | yellow | beige ⚠ | 8 | 53 | 29 |
| 20 | yellow | beige ⚠ | 8 | 66 | 10 |
| 21 | yellow | beige ⚠ | 8 | 64 | 12 |
| 22 | yellow | beige ⚠ | 6 | 47 | 11 |
| 23 | yellow | beige ⚠ | 6 | 54 | 4 |
| 24 | black | white ⚠ | 16 | 76 | 34 |

## Pieces to check

Pieces listed by how many of their numbers need a look.

| piece | ok | check | numbers to check |
|---|---:|---:|---|
| piece-12-04 | 1 | 9 | 5 (unpaired), 6 (unpaired), 7 (line not found), 014 (unpaired), 17 (extra copy: likely misread), 61 (line not found), 420 (line not found), 593 (line not found), 742 (length mismatch) |
| piece-12-06 | 0 | 8 | 040 (line not found), 511 (length mismatch), 546 (no tab), 593 (line not found), 594 (unpaired), 645 (no tab), 695 (both tabs), 898 (line not found) |
| piece-09-03 | 1 | 8 | 658 (both tabs), 658 (both tabs), 660 (length mismatch), 668 (extra copy: likely misread), 677 (length mismatch), 678 (no tab), 883 (no tab), 887 (both tabs) |
| piece-05-01 | 5 | 7 | 10 (printed 3 times), 46 (both tabs), 46 (both tabs), 47 (line not found), 51 (length mismatch), 55 (unpaired), 925 (unpaired) |
| piece-11-05 | 3 | 7 | 58 (line not found), 770 (line not found), 777 (line not found), 778 (printed 3 times), 779 (unpaired), 781 (length mismatch), 793 (unpaired) |
| piece-19-04 | 7 | 7 | 398 (length mismatch), 400 (line not found), 454 (line not found), 457 (line not found), 460 (length mismatch), 461 (length mismatch), 469 (length mismatch) |
| piece-16-10 | 1 | 6 | 060 (unpaired), 283 (length mismatch), 381 (length mismatch), 385 (length mismatch), 844 (unpaired), 848 (unpaired) |
| piece-18-06 | 5 | 6 | 67 (extra copy: likely misread), 78 (no tab), 90 (line not found), 93 (length mismatch), 100 (extra copy: likely misread), 136 (line not found) |
| piece-24-05 | 0 | 6 | 261 (length mismatch), 281 (length mismatch), 282 (both tabs), 283 (length mismatch), 364 (length mismatch), 370 (length mismatch) |
| piece-17-01 | 3 | 6 | 706 (extra copy: likely misread), 723 (unpaired), 726 (line not found), 727 (length mismatch), 729 (length mismatch), 734 (length mismatch) |
| piece-11-02 | 4 | 5 | 000 (unpaired), 10 (printed 3 times), 11 (line not found), 040 (line not found), 48 (extra copy: likely misread) |
| piece-11-04 | 8 | 5 | 11 (line not found), 745 (line not found), 766 (both tabs), 770 (line not found), 778 (printed 3 times) |
| piece-17-09 | 2 | 5 | 95 (line not found), 655 (unpaired), 729 (length mismatch), 734 (length mismatch), 976 (unpaired) |
| piece-11-06 | 3 | 5 | 147 (length mismatch), 757 (length mismatch), 764 (extra copy: likely misread), 777 (line not found), 790 (unpaired) |
| piece-16-03 | 9 | 5 | 370 (length mismatch), 372 (length mismatch), 386 (length mismatch), 869 (extra copy: likely misread), 883 (no tab) |
| piece-04-06 | 3 | 5 | 570 (length mismatch), 577 (length mismatch), 578 (extra copy: likely misread), 645 (no tab), 676 (both tabs) |
| piece-09-04 | 4 | 5 | 259 (extra copy: likely misread), 298 (length mismatch), 300 (length mismatch), 302 (extra copy: likely misread), 323 (length mismatch) |
| piece-16-02 | 4 | 5 | 262 (no tab), 378 (unpaired), 379 (line not found), 381 (length mismatch), 385 (length mismatch) |
| piece-07-01 | 5 | 5 | 273 (both tabs), 392 (length mismatch), 618 (length mismatch), 619 (length mismatch), 672 (unpaired) |
| piece-04-07 | 4 | 5 | 395 (length mismatch), 420 (line not found), 422 (extra copy: likely misread), 731 (no tab), 784 (unpaired) |
| piece-19-07 | 6 | 5 | 454 (line not found), 460 (length mismatch), 462 (extra copy: likely misread), 466 (extra copy: likely misread), 496 (line not found) |
| piece-17-04 | 10 | 5 | 469 (length mismatch), 508 (unpaired), 546 (no tab), 708 (unpaired), 714 (line not found) |
| piece-12-05 | 9 | 4 | 4 (extra copy: likely misread), 7 (line not found), 742 (length mismatch), 745 (line not found) |
| piece-05-02 | 3 | 4 | 10 (printed 3 times), 45 (length mismatch), 47 (line not found), 51 (length mismatch) |
| piece-11-03 | 5 | 4 | 13 (length mismatch), 41 (length mismatch), 414 (extra copy: likely misread), 786 (length mismatch) |
| piece-06-03 | 7 | 4 | 33 (length mismatch), 34 (unpaired), 316 (length mismatch), 386 (length mismatch) |
| piece-07-07 | 6 | 4 | 272 (length mismatch), 273 (both tabs), 274 (length mismatch), 318 (unpaired) |
| piece-24-12 | 4 | 4 | 43 (no tab), 145 (length mismatch), 457 (line not found), 866 (no tab) |
| piece-16-04 | 11 | 4 | 181 (length mismatch), 286 (no tab), 364 (length mismatch), 379 (line not found) |
| piece-16-09 | 8 | 4 | 186 (extra copy: likely misread), 192 (length mismatch), 195 (length mismatch), 494 (extra copy: likely misread) |
| piece-14-06 | 10 | 4 | 171 (length mismatch), 175 (unpaired), 181 (length mismatch), 698 (length mismatch) |
| piece-12-07 | 3 | 4 | 545 (unpaired), 548 (line not found), 595 (no tab), 648 (extra copy: likely misread) |
| piece-17-05 | 8 | 4 | 470 (length mismatch), 556 (length mismatch), 562 (unpaired), 613 (extra copy: likely misread) |
| piece-24-01 | 2 | 4 | 276 (extra copy: likely misread), 277 (length mismatch), 278 (unpaired), 280 (length mismatch) |
| piece-08-05 | 5 | 4 | 305 (both tabs), 312 (length mismatch), 314 (length mismatch), 326 (extra copy: likely misread) |
| piece-17-03 | 10 | 4 | 716 (length mismatch), 718 (length mismatch), 726 (line not found), 732 (unpaired) |
| piece-19-01 | 4 | 4 | 397 (line not found), 398 (length mismatch), 400 (line not found), 898 (line not found) |
| piece-21-03 | 6 | 4 | 464 (extra copy: likely misread), 476 (extra copy: likely misread), 477 (length mismatch), 482 (unpaired) |
| piece-15-02 | 5 | 4 | 511 (length mismatch), 596 (no tab), 608 (length mismatch), 714 (line not found) |
| piece-17-10 | 8 | 4 | 537 (unpaired), 548 (line not found), 551 (length mismatch), 552 (both tabs) |
| piece-13-03 | 6 | 4 | 538 (unpaired), 687 (length mismatch), 695 (both tabs), 768 (no tab) |
| piece-07-03 | 5 | 4 | 556 (length mismatch), 651 (length mismatch), 652 (length mismatch), 653 (length mismatch) |
| piece-09-02 | 4 | 4 | 652 (length mismatch), 676 (both tabs), 677 (length mismatch), 909 (unpaired) |
| piece-24-03 | 4 | 3 | 13 (length mismatch), 755 (extra copy: likely misread), 789 (unpaired) |
| piece-11-07 | 4 | 3 | 751 (unpaired), 757 (length mismatch), 760 (extra copy: likely misread) |
| piece-24-15 | 5 | 3 | 14 (extra copy: likely misread), 215 (unpaired), 216 (extra copy: likely misread) |
| piece-18-03 | 11 | 3 | 20 (extra copy: likely misread), 90 (line not found), 95 (line not found) |
| piece-06-06 | 6 | 3 | 272 (length mismatch), 316 (length mismatch), 414 (extra copy: likely misread) |
| piece-05-03 | 9 | 3 | 54 (length mismatch), 58 (line not found), 81 (extra copy: likely misread) |
| piece-05-05 | 7 | 3 | 40 (length mismatch), 41 (length mismatch), 61 (line not found) |
| piece-05-07 | 6 | 3 | 40 (length mismatch), 778 (printed 3 times), 792 (unpaired) |
| piece-18-07 | 8 | 3 | 106 (line not found), 189 (length mismatch), 195 (length mismatch) |
| piece-18-04 | 5 | 3 | 188 (extra copy: likely misread), 189 (length mismatch), 192 (length mismatch) |
| piece-15-06 | 8 | 3 | 564 (line not found), 636 (length mismatch), 662 (length mismatch) |
| piece-14-03 | 5 | 3 | 290 (unpaired), 292 (length mismatch), 768 (no tab) |
| piece-12-09 | 4 | 3 | 261 (length mismatch), 292 (length mismatch), 577 (length mismatch) |
| piece-16-07 | 3 | 3 | 277 (length mismatch), 372 (length mismatch), 376 (unpaired) |
| piece-15-01 | 5 | 3 | 280 (length mismatch), 836 (unpaired), 887 (both tabs) |
| piece-09-05 | 5 | 3 | 286 (no tab), 300 (length mismatch), 323 (length mismatch) |
| piece-10-05 | 5 | 3 | 298 (length mismatch), 328 (length mismatch), 752 (extra copy: likely misread) |
| piece-08-04 | 8 | 3 | 328 (length mismatch), 639 (extra copy: likely misread), 885 (unpaired) |
| piece-08-02 | 6 | 3 | 678 (no tab), 860 (unpaired), 862 (no tab) |
| piece-09-07 | 5 | 3 | 312 (length mismatch), 314 (length mismatch), 335 (length mismatch) |
| piece-08-01 | 8 | 3 | 335 (length mismatch), 588 (unpaired), 802 (length mismatch) |
| piece-24-16 | 4 | 3 | 571 (length mismatch), 571 (length mismatch), 576 (line not found) |
| piece-06-04 | 8 | 3 | 368 (both tabs), 380 (extra copy: likely misread), 392 (length mismatch) |
| piece-17-07 | 3 | 3 | 629 (length mismatch), 730 (unpaired), 944 (line not found) |
| piece-19-08 | 8 | 3 | 477 (length mismatch), 481 (length mismatch), 496 (line not found) |
| piece-21-01 | 8 | 3 | 461 (length mismatch), 479 (unpaired), 484 (unpaired) |
| piece-19-06 | 8 | 3 | 448 (extra copy: likely misread), 470 (length mismatch), 555 (length mismatch) |
| piece-19-03 | 5 | 3 | 539 (length mismatch), 549 (unpaired), 551 (length mismatch) |
| piece-19-02 | 3 | 3 | 507 (extra copy: likely misread), 539 (length mismatch), 636 (length mismatch) |
| piece-22-05 | 8 | 3 | 509 (extra copy: likely misread), 560 (no tab), 576 (line not found) |
| piece-15-10 | 8 | 3 | 527 (length mismatch), 534 (unpaired), 559 (unpaired) |
| piece-15-08 | 11 | 3 | 527 (length mismatch), 536 (both tabs), 634 (extra copy: likely misread) |
| piece-09-06 | 5 | 3 | 628 (extra copy: likely misread), 651 (length mismatch), 681 (unpaired) |
| piece-24-06 | 3 | 3 | 631 (unpaired), 718 (length mismatch), 727 (length mismatch) |
| piece-09-01 | 5 | 3 | 657 (length mismatch), 683 (unpaired), 862 (no tab) |
| piece-17-06 | 1 | 3 | 735 (line not found), 944 (line not found), 989 (unpaired) |
| piece-11-01 | 4 | 2 | 00 (unpaired), 33 (length mismatch) |
| piece-22-01 | 9 | 2 | 536 (both tabs), 560 (no tab) |
| piece-22-04 | 7 | 2 | 575 (unpaired), 589 (unpaired) |
| piece-20-06 | 10 | 2 | 76 (both tabs), 76 (both tabs) |
| piece-20-07 | 7 | 2 | 66 (length mismatch), 93 (length mismatch) |
| piece-11-09 | 5 | 2 | 43 (no tab), 224 (length mismatch) |
| piece-14-05 | 3 | 2 | 15 (no tab), 137 (length mismatch) |
| piece-11-10 | 6 | 2 | 184 (extra copy: likely misread), 766 (both tabs) |
| piece-05-04 | 7 | 2 | 54 (length mismatch), 66 (length mismatch) |
| piece-21-06 | 10 | 2 | 45 (length mismatch), 78 (no tab) |
| piece-24-04 | 6 | 2 | 786 (length mismatch), 794 (unpaired) |
| piece-20-08 | 4 | 2 | 67 (extra copy: likely misread), 68 (length mismatch) |
| piece-18-05 | 11 | 2 | 106 (line not found), 109 (unpaired) |
| piece-04-02 | 10 | 2 | 073 (unpaired), 412 (length mismatch) |
| piece-18-08 | 9 | 2 | 118 (length mismatch), 136 (line not found) |
| piece-18-01 | 6 | 2 | 88 (extra copy: likely misread), 397 (line not found) |
| piece-20-02 | 8 | 2 | 118 (length mismatch), 129 (length mismatch) |
| piece-14-08 | 8 | 2 | 176 (extra copy: likely misread), 209 (unpaired) |
| piece-14-01 | 7 | 2 | 145 (length mismatch), 147 (length mismatch) |
| piece-04-01 | 5 | 2 | 406 (extra copy: likely misread), 456 (extra copy: likely misread) |
| piece-04-03 | 10 | 2 | 281 (length mismatch), 406 (extra copy: likely misread) |
| piece-16-05 | 10 | 2 | 161 (length mismatch), 334 (extra copy: likely misread) |
| piece-14-10 | 9 | 2 | 161 (length mismatch), 171 (length mismatch) |
| piece-14-07 | 9 | 2 | 208 (extra copy: likely misread), 564 (line not found) |
| piece-24-07 | 6 | 2 | 781 (length mismatch), 785 (unpaired) |
| piece-11-11 | 4 | 2 | 339 (unpaired), 762 (unpaired) |
| piece-23-03 | 7 | 2 | 229 (length mismatch), 957 (unpaired) |
| piece-12-08 | 5 | 2 | 308 (length mismatch), 659 (no tab) |
| piece-04-04 | 7 | 2 | 262 (no tab), 412 (length mismatch) |
| piece-07-10 | 4 | 2 | 265 (length mismatch), 274 (length mismatch) |
| piece-06-05 | 7 | 2 | 466 (extra copy: likely misread), 618 (length mismatch) |
| piece-10-02 | 5 | 2 | 341 (line not found), 697 (unpaired) |
| piece-16-06 | 2 | 2 | 341 (line not found), 735 (line not found) |
| piece-21-07 | 7 | 2 | 435 (unpaired), 452 (unpaired) |
| piece-15-09 | 8 | 2 | 616 (extra copy: likely misread), 659 (no tab) |
| piece-15-07 | 8 | 2 | 552 (both tabs), 629 (length mismatch) |
| piece-22-03 | 8 | 2 | 596 (no tab), 608 (length mismatch) |
| piece-07-02 | 4 | 2 | 619 (length mismatch), 685 (extra copy: likely misread) |
| piece-07-04 | 4 | 2 | 653 (length mismatch), 660 (length mismatch) |
| piece-24-02 | 4 | 2 | 623 (extra copy: likely misread), 731 (no tab) |
| piece-10-04 | 5 | 2 | 657 (length mismatch), 698 (length mismatch) |
| piece-22-06 | 9 | 1 | 009 (extra copy: likely misread) |
| piece-16-01 | 4 | 1 | 15 (no tab) |
| piece-07-09 | 5 | 1 | 802 (length mismatch) |
| piece-05-06 | 7 | 1 | 224 (length mismatch) |
| piece-06-02 | 8 | 1 | 866 (no tab) |
| piece-12-01 | 5 | 1 | 308 (length mismatch) |
| piece-06-01 | 8 | 1 | 555 (length mismatch) |
| piece-20-03 | 10 | 1 | 68 (length mismatch) |
| piece-10-07 | 6 | 1 | 359 (unpaired) |
| piece-10-03 | 8 | 1 | 368 (both tabs) |
| piece-20-04 | 9 | 1 | 129 (length mismatch) |
| piece-14-04 | 6 | 1 | 137 (length mismatch) |
| piece-14-02 | 6 | 1 | 282 (both tabs) |
| piece-12-03 | 8 | 1 | 408 (unpaired) |
| piece-16-08 | 6 | 1 | 716 (length mismatch) |
| piece-24-08 | 5 | 1 | 288 (extra copy: likely misread) |
| piece-13-02 | 9 | 1 | 999 (both tabs) |
| piece-04-05 | 9 | 1 | 395 (length mismatch) |
| piece-17-02 | 4 | 1 | 613 (extra copy: likely misread) |
| piece-23-01 | 10 | 1 | 235 (unpaired) |
| piece-23-05 | 10 | 1 | 229 (length mismatch) |
| piece-04-08 | 7 | 1 | 578 (extra copy: likely misread) |
| piece-12-10 | 7 | 1 | 846 (unpaired) |
| piece-07-08 | 6 | 1 | 265 (length mismatch) |
| piece-08-06 | 7 | 1 | 305 (both tabs) |
| piece-13-04 | 4 | 1 | 687 (length mismatch) |
| piece-10-01 | 8 | 1 | 570 (length mismatch) |
| piece-21-05 | 4 | 1 | 481 (length mismatch) |
| piece-19-05 | 12 | 1 | 483 (extra copy: likely misread) |
| piece-24-09 | 6 | 1 | 750 (unpaired) |
| piece-15-04 | 6 | 1 | 616 (extra copy: likely misread) |
| piece-15-03 | 6 | 1 | 637 (unpaired) |
| piece-17-08 | 6 | 1 | 999 (both tabs) |
| piece-12-11 | 5 | 1 | 595 (no tab) |
| piece-22-02 | 6 | 1 | 580 (extra copy: likely misread) |
| piece-08-03 | 7 | 1 | 662 (length mismatch) |

## Hand corrections that still do not pair

381 numbers were set by hand; 99 of them still do not form a clean pair, so the correction, its partner or the traced line is likely off. They come first on the check page.

| piece | number | side | mm | status | partner | partner mm |
|---|---|---|---:|---|---|---:|
| piece-12-05 | 4 | tab | 15.8 | extra copy: likely misread |   |  |
| piece-12-04 | 5 | none | 0.0 | unpaired |   |  |
| piece-12-04 | 6 | none | 0.0 | unpaired |   |  |
| piece-12-04 | 7 | none | 0.0 | line not found | piece-12-05 none | 0.0 |
| piece-12-05 | 7 | none | 0.0 | line not found | piece-12-04 none | 0.0 |
| piece-11-02 | 10 | tab | 37.8 | printed 3 times |   |  |
| piece-11-04 | 11 | none | 0.0 | line not found | piece-11-02 tab | 15.6 |
| piece-11-03 | 13 | tab | 31.0 | length mismatch | piece-24-03 edge | 56.4 |
| piece-24-03 | 13 | edge | 56.4 | length mismatch | piece-11-03 tab | 31.0 |
| piece-16-01 | 15 | edge | 51.9 | no tab | piece-14-05 edge | 26.0 |
| piece-06-03 | 33 | tab | 34.2 | length mismatch | piece-11-01 edge | 31.1 |
| piece-11-01 | 33 | edge | 31.1 | length mismatch | piece-06-03 tab | 34.2 |
| piece-06-03 | 34 | none | 0.0 | unpaired |   |  |
| piece-05-05 | 40 | tab | 31.0 | length mismatch | piece-05-07 edge | 38.9 |
| piece-05-05 | 41 | tab | 20.6 | length mismatch | piece-11-03 edge | 43.6 |
| piece-11-03 | 41 | edge | 43.6 | length mismatch | piece-05-05 tab | 20.6 |
| piece-11-09 | 43 | edge | 26.2 | no tab | piece-24-12 edge | 15.3 |
| piece-05-01 | 47 | tab | 29.2 | line not found | piece-05-02 none | 0.0 |
| piece-05-02 | 47 | none | 0.0 | line not found | piece-05-01 tab | 29.2 |
| piece-05-01 | 51 | edge | 91.1 | length mismatch | piece-05-02 tab | 54.2 |
| piece-05-02 | 51 | tab | 54.2 | length mismatch | piece-05-01 edge | 91.1 |
| piece-05-03 | 54 | edge | 35.0 | length mismatch | piece-05-04 tab | 26.8 |
| piece-05-04 | 54 | tab | 26.8 | length mismatch | piece-05-03 edge | 35.0 |
| piece-05-03 | 58 | none | 0.0 | line not found | piece-11-05 edge | 17.8 |
| piece-11-05 | 58 | edge | 17.8 | line not found | piece-05-03 none | 0.0 |
| piece-05-05 | 61 | edge | 27.7 | line not found | piece-12-04 none | 0.0 |
| piece-18-06 | 67 | edge | 30.9 | extra copy: likely misread |   |  |
| piece-20-08 | 67 | tab | 31.1 | extra copy: likely misread |   |  |
| piece-05-03 | 81 | none | 0.0 | extra copy: likely misread |   |  |
| piece-18-01 | 88 | edge | 9.5 | extra copy: likely misread |   |  |
| piece-18-05 | 106 | none | 0.0 | line not found | piece-18-07 edge | 17.0 |
| piece-18-07 | 106 | edge | 17.0 | line not found | piece-18-05 none | 0.0 |
| piece-18-08 | 118 | edge | 53.6 | length mismatch | piece-20-02 tab | 45.9 |
| piece-20-02 | 118 | tab | 45.9 | length mismatch | piece-18-08 edge | 53.6 |
| piece-20-02 | 129 | edge | 19.0 | length mismatch | piece-20-04 tab | 20.2 |
| piece-18-06 | 136 | edge | 17.9 | line not found | piece-18-08 none | 0.0 |
| piece-18-08 | 136 | none | 0.0 | line not found | piece-18-06 edge | 17.9 |
| piece-14-04 | 137 | edge | 20.9 | length mismatch | piece-14-05 tab | 33.9 |
| piece-14-05 | 137 | tab | 33.9 | length mismatch | piece-14-04 edge | 20.9 |
| piece-14-01 | 145 | tab | 26.0 | length mismatch | piece-24-12 edge | 14.1 |
| piece-11-06 | 147 | edge | 38.4 | length mismatch | piece-14-01 tab | 72.0 |
| piece-14-01 | 147 | tab | 72.0 | length mismatch | piece-11-06 edge | 38.4 |
| piece-14-06 | 171 | edge | 59.6 | length mismatch | piece-14-10 tab | 51.5 |
| piece-14-10 | 171 | tab | 51.5 | length mismatch | piece-14-06 edge | 59.6 |
| piece-14-06 | 175 | tab | 20.4 | unpaired |   |  |
| piece-16-09 | 186 | edge | 24.8 | extra copy: likely misread |   |  |
| piece-18-04 | 189 | tab | 42.5 | length mismatch | piece-18-07 edge | 93.7 |
| piece-18-07 | 189 | edge | 93.7 | length mismatch | piece-18-04 tab | 42.5 |
| piece-18-04 | 192 | edge | 37.0 | length mismatch | piece-16-09 tab | 39.7 |
| piece-16-09 | 195 | tab | 51.3 | length mismatch | piece-18-07 edge | 93.7 |
| piece-18-07 | 195 | edge | 93.7 | length mismatch | piece-16-09 tab | 51.3 |
| piece-24-15 | 215 | tab | 26.5 | unpaired |   |  |
| piece-05-06 | 224 | tab | 47.9 | length mismatch | piece-11-09 edge | 54.9 |
| piece-11-09 | 224 | edge | 54.9 | length mismatch | piece-05-06 tab | 47.9 |
| piece-23-03 | 229 | edge | 35.1 | length mismatch | piece-23-05 tab | 37.0 |
| piece-23-05 | 229 | tab | 37.0 | length mismatch | piece-23-03 edge | 35.1 |
| piece-23-01 | 235 | edge | 36.8 | unpaired |   |  |
| piece-24-05 | 261 | edge | 18.7 | length mismatch | piece-12-09 tab | 25.9 |
| piece-07-08 | 265 | edge | 36.2 | length mismatch | piece-07-10 tab | 37.7 |
| piece-06-06 | 272 | edge | 20.8 | length mismatch | piece-07-07 tab | 29.0 |
| piece-07-07 | 272 | tab | 29.0 | length mismatch | piece-06-06 edge | 20.8 |
| piece-07-01 | 273 | tab | 29.0 | both tabs | piece-07-07 tab | 29.0 |
| piece-07-07 | 273 | tab | 29.0 | both tabs | piece-07-01 tab | 29.0 |
| piece-07-07 | 274 | tab | 125.5 | length mismatch | piece-07-10 edge | 61.1 |
| piece-07-10 | 274 | edge | 61.1 | length mismatch | piece-07-07 tab | 125.5 |
| piece-16-07 | 277 | edge | 32.2 | length mismatch | piece-24-01 tab | 24.0 |
| piece-24-01 | 277 | tab | 24.0 | length mismatch | piece-16-07 edge | 32.2 |
| piece-24-01 | 280 | tab | 21.4 | length mismatch | piece-15-01 edge | 30.9 |
| piece-16-10 | 283 | edge | 17.2 | length mismatch | piece-24-05 tab | 18.3 |
| piece-24-05 | 283 | tab | 18.3 | length mismatch | piece-16-10 edge | 17.2 |
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
| piece-09-04 | 323 | edge | 56.1 | length mismatch | piece-09-05 tab | 50.6 |
| piece-09-05 | 323 | tab | 50.6 | length mismatch | piece-09-04 edge | 56.1 |
| piece-08-04 | 328 | edge | 26.3 | length mismatch | piece-10-05 tab | 25.1 |
| piece-10-05 | 328 | tab | 25.1 | length mismatch | piece-08-04 edge | 26.3 |
| piece-10-02 | 341 | none | 0.0 | line not found | piece-16-06 edge | 58.4 |
| piece-16-06 | 341 | edge | 58.4 | line not found | piece-10-02 none | 0.0 |
| piece-16-07 | 376 | tab | 26.2 | unpaired |   |  |
| piece-06-03 | 386 | edge | 54.8 | length mismatch | piece-16-03 tab | 22.4 |
| piece-24-12 | 457 | none | 0.0 | line not found | piece-19-04 tab | 23.9 |
| piece-22-02 | 580 | tab | 46.0 | extra copy: likely misread |   |  |
| piece-17-01 | 706 | edge | 17.7 | extra copy: likely misread |   |  |
| piece-11-04 | 766 | tab | 26.6 | both tabs | piece-11-10 tab | 40.0 |
| piece-14-03 | 768 | edge | 26.4 | no tab | piece-13-03 edge | 61.5 |
| piece-11-05 | 779 | tab | 12.9 | unpaired |   |  |
| piece-24-04 | 786 | tab | 24.1 | length mismatch | piece-11-03 edge | 43.6 |
| piece-11-06 | 790 | edge | 24.2 | unpaired |   |  |
| piece-05-07 | 792 | edge | 24.3 | unpaired |   |  |

## Likely misreads

27 clear-cut misreads were fixed without asking (marked `applied` in `bowser-misreads.csv`). 79 more numbers that did not pair up sit on a line of the same length as another unpaired number on the other side (edge against tab), and the two numbers look alike. Check them with `make fix` and `app/number-check.html`.

| piece | side | mm | read | suggested | partner | partner mm | why |
|---|---|---:|---|---|---|---:|---|
| piece-04-06 | tab | 44.3 | 578 | 576 | piece-22-05 edge | 44.3 | OCR's other reading; the read number already pairs elsewhere |
| piece-05-01 | edge | 28.4 | 55 | 66 | piece-05-04 tab | 28.4 | OCR's other reading |
| piece-08-01 | tab | 26.3 | 802 | 862 | piece-09-01 edge | 26.3 | one digit differs |
| piece-08-02 | edge | 29.7 | 862 | 662 | piece-08-03 tab | 29.6 | OCR's other reading |
| piece-09-01 | tab | 55.2 | 683 | 883 | piece-09-03 edge | 55.3 | OCR's other reading |
| piece-09-03 | tab | 61.8 | 668 | 659 | piece-12-08 edge | 61.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-10-07 | edge | 49.6 | 359 | 368 | piece-10-03 tab | 49.6 | OCR's other reading |
| piece-14-03 | edge | 25.6 | 292 | 282 | piece-14-02 tab | 25.6 | OCR's other reading |
| piece-15-01 | edge | 30.9 | 280 | 290 | piece-14-03 tab | 30.8 | OCR's other reading |
| piece-16-08 | edge | 40.0 | 716 | 766 | piece-11-10 tab | 40.0 | one digit differs |
| piece-17-05 | edge | 28.6 | 562 | 552 | piece-17-10 tab | 28.5 | OCR's other reading |
| piece-19-03 | edge | 23.1 | 549 | 548 | piece-17-10 tab | 23.2 | OCR's other reading |
| piece-19-08 | edge | 24.4 | 481 | 461 | piece-19-04 tab | 24.4 | OCR's other reading |
| piece-20-06 | tab | 20.6 | 76 | 78 | piece-21-06 edge | 20.6 | OCR's other reading |
| piece-20-07 | edge | 38.9 | 66 | 68 | piece-20-08 tab | 38.9 | OCR's other reading |
| piece-21-01 | edge | 28.8 | 461 | 481 | piece-21-05 tab | 28.7 | OCR's other reading |
| piece-21-03 | tab | 34.8 | 476 | 479 | piece-21-01 edge | 34.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-22-04 | tab | 38.6 | 589 | 560 | piece-22-05 edge | 38.7 | OCR's other reading |
| piece-23-03 | tab | 36.8 | 957 | 235 | piece-23-01 edge | 36.8 | OCR's other reading |
| piece-04-06 | tab | 44.8 | 676 | 575 | piece-22-04 edge | 44.9 | OCR's other reading |
| piece-04-08 | edge | 27.4 | 578 | 570 | piece-04-06 tab | 27.5 | OCR's other reading; the read number already pairs elsewhere |
| piece-08-04 | edge | 26.3 | 328 | 376 | piece-16-07 tab | 26.2 | OCR's other reading |
| piece-08-04 | tab | 75.6 | 639 | 339 | piece-11-11 edge | 75.7 | OCR's other reading; the read number already pairs elsewhere |
| piece-08-05 | edge | 46.6 | 326 | 335 | piece-09-07 tab | 46.7 | OCR's other reading; the read number already pairs elsewhere |
| piece-09-04 | tab | 42.1 | 259 | 298 | piece-10-05 edge | 42.3 | OCR's other reading; the read number already pairs elsewhere |
| piece-11-03 | tab | 31.0 | 13 | 33 | piece-11-01 edge | 31.1 | one digit differs |
| piece-11-04 | tab | 26.6 | 766 | 768 | piece-14-03 edge | 26.4 | OCR's other reading |
| piece-12-07 | tab | 29.1 | 648 | 546 | piece-17-04 edge | 29.0 | OCR's other reading; the read number already pairs elsewhere |
| piece-12-11 | edge | 50.7 | 595 | 695 | piece-13-03 tab | 50.8 | OCR's other reading |
| piece-14-07 | tab | 14.6 | 208 | 209 | piece-14-08 edge | 14.6 | OCR's other reading; the read number already pairs elsewhere |
| piece-19-02 | tab | 30.9 | 507 | 537 | piece-17-10 edge | 31.0 | one digit differs; the read number already pairs elsewhere |
| piece-19-07 | edge | 25.6 | 466 | 483 | piece-19-05 tab | 25.7 | OCR's other reading; the read number already pairs elsewhere |
| piece-20-06 | tab | 38.1 | 76 | 78 | piece-18-06 edge | 38.2 | OCR's other reading |
| piece-21-03 | edge | 39.1 | 464 | 462 | piece-19-07 tab | 39.0 | one digit differs; the read number already pairs elsewhere |
| piece-22-02 | tab | 46.0 | 580 | 560 | piece-22-01 edge | 46.0 | one digit differs; the read number already pairs elsewhere |
| piece-10-04 | tab | 35.0 | 657 | 697 | piece-10-02 edge | 34.8 | one digit differs |
| piece-11-04 | edge | 12.7 | 778 | 779 | piece-11-05 tab | 12.9 | OCR's other reading |
| piece-11-10 | edge | 38.6 | 184 | 484 | piece-21-01 tab | 38.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-12-09 | tab | 43.2 | 292 | 392 | piece-07-01 edge | 42.9 | OCR's other reading |
| piece-12-10 | tab | 50.4 | 846 | 645 | piece-04-06 edge | 50.2 | OCR's other reading |
| piece-13-03 | edge | 54.3 | 538 | 636 | piece-19-02 tab | 54.5 | OCR's other reading |
| piece-15-02 | tab | 15.0 | 608 | 508 | piece-17-04 edge | 14.8 | OCR's other reading |
| piece-18-06 | edge | 40.6 | 100 | 109 | piece-18-05 tab | 40.8 | one digit differs; the read number already pairs elsewhere |
| piece-04-01 | tab | 42.9 | 406 | 408 | piece-12-03 edge | 43.3 | OCR's other reading; the read number already pairs elsewhere |
| piece-08-04 | tab | 35.6 | 885 | 335 | piece-08-01 edge | 35.3 | OCR's other reading |
| piece-09-06 | tab | 25.3 | 628 | 678 | piece-08-02 edge | 25.6 | OCR's other reading; the read number already pairs elsewhere |
| piece-11-02 | edge | 23.9 | 48 | 95 | piece-18-03 tab | 23.5 | OCR's other reading; the read number already pairs elsewhere |
| piece-11-06 | edge | 23.8 | 764 | 161 | piece-16-05 tab | 23.5 | OCR's other reading; the read number already pairs elsewhere |
| piece-14-08 | edge | 20.1 | 176 | 175 | piece-14-06 tab | 20.4 | OCR's other reading; the read number already pairs elsewhere |
| piece-15-03 | edge | 22.7 | 637 | 887 | piece-15-01 tab | 23.1 | OCR's other reading |
| piece-15-09 | edge | 23.6 | 659 | 629 | piece-15-07 tab | 23.2 | OCR's other reading |
| piece-16-05 | edge | 29.9 | 334 | 364 | piece-16-04 tab | 29.7 | one digit differs; the read number already pairs elsewhere |
| piece-18-04 | tab | 25.1 | 188 | 186 | piece-16-09 edge | 24.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-24-01 | edge | 37.4 | 276 | 278 | piece-24-01 tab | 37.7 | OCR's other reading; the read number already pairs elsewhere |
| piece-24-03 | edge | 18.1 | 789 | 729 | piece-17-09 tab | 17.9 | one digit differs |
| piece-04-03 | edge | 26.3 | 281 | 261 | piece-12-09 tab | 25.9 | OCR's other reading |
| piece-09-02 | edge | 60.9 | 909 | 999 | piece-13-02 tab | 61.4 | one digit differs |
| piece-09-03 | edge | 40.7 | 678 | 676 | piece-09-02 tab | 41.1 | OCR's other reading |
| piece-09-04 | tab | 30.5 | 302 | 802 | piece-07-09 edge | 30.2 | OCR's other reading; the read number already pairs elsewhere |
| piece-15-01 | tab | 32.2 | 836 | 636 | piece-15-06 edge | 32.6 | OCR's other reading |
| piece-12-05 | tab | 15.8 | 4 | 43 | piece-24-12 edge | 15.3 | a digit dropped or added; the read number already pairs elsewhere |
| piece-14-05 | edge | 26.0 | 15 | 215 | piece-24-15 tab | 26.5 | a digit dropped or added |
| piece-24-08 | tab | 13.3 | 288 | 286 | piece-16-04 edge | 13.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-12-06 | tab | 43.5 | 898 | 596 | piece-15-02 edge | 42.9 | OCR's other reading |
| piece-14-10 | edge | 42.3 | 161 | 181 | piece-14-06 tab | 41.8 | OCR's other reading |
| piece-15-06 | edge | 18.5 | 662 | 552 | piece-15-07 tab | 17.9 | OCR's other reading |
| piece-16-02 | edge | 20.6 | 262 | 282 | piece-24-05 tab | 20.0 | OCR's other reading |
| piece-21-06 | tab | 39.5 | 45 | 40 | piece-05-07 edge | 38.9 | OCR's other reading |
| piece-05-01 | tab | 41.4 | 46 | 45 | piece-05-02 edge | 40.7 | one digit differs |
| piece-09-01 | edge | 42.3 | 657 | 687 | piece-13-04 tab | 43.0 | OCR's other reading |
| piece-16-10 | tab | 18.0 | 381 | 261 | piece-24-05 edge | 18.7 | OCR's other reading |
| piece-15-08 | tab | 32.6 | 634 | 534 | piece-15-10 edge | 31.7 | OCR's other reading; the read number already pairs elsewhere |
| piece-04-07 | tab | 28.9 | 422 | 482 | piece-21-03 edge | 28.0 | one digit differs; the read number already pairs elsewhere |
| piece-17-05 | edge | 29.0 | 556 | 536 | piece-22-01 tab | 28.1 | one digit differs |
| piece-04-04 | tab | 26.7 | 412 | 312 | piece-09-07 edge | 25.8 | one digit differs |
| piece-07-01 | tab | 29.0 | 618 | 608 | piece-22-03 edge | 28.0 | one digit differs |
| piece-07-07 | edge | 37.4 | 318 | 316 | piece-06-06 tab | 38.3 | OCR's other reading |
| piece-24-07 | edge | 23.2 | 785 | 786 | piece-24-04 tab | 24.1 | OCR's other reading |
| piece-24-15 | edge | 23.6 | 216 | 716 | piece-17-03 tab | 22.6 | OCR's other reading; the read number already pairs elsewhere |

Full tables: `bowser-edges.csv`, `bowser-misreads.csv`.
