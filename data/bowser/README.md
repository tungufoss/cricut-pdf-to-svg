# Bowser

1570 printed numbers on 178 pieces. 433 numbers form a clean pair (one plain edge, one tab, lengths within 1 mm); 704 labels need a look.

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
| numbers | 1570 read, 699 uncertain (orange in the SVG) |
| pieces to check | 175 marked ⚠ in Inkscape |
| paper colour | footers disagree with the YAML: pages 14–23 say beige (YAML: yellow); page 24 says white (YAML: black) |
| nesting on sheets | not started |

## Edge numbers

| status | labels | meaning |
|---|---:|---|
| ok | 866 | partner found, one tab and one plain edge, same length |
| length mismatch | 218 | partner found but the marked lines differ in length: misread number or traced line |
| unpaired | 124 | no other copy of this number: likely misread |
| extra copy: likely misread | 97 | number read more than twice; the other copies already form a clean pair |
| both tabs | 86 | both copies sit on a tab fold |
| no tab | 72 | neither copy sits on a tab fold |
| line not found | 56 | no cut edge or fold next to the number |
| printed 3 times | 51 | number read more than twice: some are misread |

## Pages

| page | config material | footer says | pieces | ok | check |
|---|---|---|---:|---:|---:|
| 04 | red | red | 8 | 50 | 25 |
| 05 | red | red | 8 | 39 | 36 |
| 06 | red | red | 6 | 30 | 28 |
| 07 | red | red | 10 | 40 | 36 |
| 08 | red | red | 6 | 33 | 23 |
| 09 | red | red | 7 | 25 | 33 |
| 10 | red | red | 7 | 31 | 23 |
| 11 | green | green | 11 | 48 | 42 |
| 12 | green | green | 11 | 44 | 46 |
| 13 | green | green | 4 | 21 | 9 |
| 14 | yellow | beige ⚠ | 10 | 56 | 36 |
| 15 | yellow | beige ⚠ | 10 | 49 | 43 |
| 16 | yellow | beige ⚠ | 10 | 39 | 52 |
| 17 | yellow | beige ⚠ | 10 | 52 | 39 |
| 18 | yellow | beige ⚠ | 8 | 43 | 39 |
| 19 | yellow | beige ⚠ | 8 | 44 | 38 |
| 20 | yellow | beige ⚠ | 8 | 48 | 28 |
| 21 | yellow | beige ⚠ | 8 | 56 | 20 |
| 22 | yellow | beige ⚠ | 6 | 25 | 33 |
| 23 | yellow | beige ⚠ | 6 | 39 | 19 |
| 24 | black | white ⚠ | 16 | 54 | 56 |

## Pieces to check

Pieces listed by how many of their numbers need a look.

| piece | ok | check | numbers to check |
|---|---:|---:|---|
| piece-12-04 | 1 | 9 | 04 (line not found), 04 (line not found), 11 (line not found), 40 (printed 3 times), 90 (unpaired), 94 (extra copy: likely misread), 420 (line not found), 593 (line not found), 742 (length mismatch) |
| piece-05-01 | 3 | 9 | 10 (line not found), 46 (printed 3 times), 46 (printed 3 times), 47 (unpaired), 48 (length mismatch), 58 (printed 3 times), 61 (no tab), 87 (no tab), 411 (extra copy: likely misread) |
| piece-16-04 | 6 | 9 | 158 (no tab), 164 (extra copy: likely misread), 181 (extra copy: likely misread), 286 (length mismatch), 364 (length mismatch), 366 (length mismatch), 379 (line not found), 383 (unpaired), 886 (both tabs) |
| piece-12-06 | 0 | 8 | 00 (line not found), 504 (length mismatch), 511 (length mismatch), 545 (line not found), 548 (line not found), 585 (both tabs), 593 (line not found), 896 (both tabs) |
| piece-12-05 | 5 | 8 | 011 (unpaired), 161 (length mismatch), 177 (extra copy: likely misread), 742 (length mismatch), 745 (line not found), 748 (extra copy: likely misread), 769 (length mismatch), 830 (no tab) |
| piece-19-04 | 6 | 8 | 98 (printed 3 times), 398 (length mismatch), 400 (printed 3 times), 450 (both tabs), 454 (line not found), 457 (unpaired), 469 (length mismatch), 483 (extra copy: likely misread) |
| piece-18-03 | 7 | 7 | 08 (line not found), 67 (printed 3 times), 95 (unpaired), 98 (printed 3 times), 101 (unpaired), 136 (printed 3 times), 736 (no tab) |
| piece-05-03 | 5 | 7 | 32 (no tab), 51 (both tabs), 58 (printed 3 times), 58 (printed 3 times), 64 (length mismatch), 80 (length mismatch), 115 (line not found) |
| piece-11-05 | 3 | 7 | 66 (no tab), 119 (length mismatch), 770 (line not found), 777 (line not found), 778 (printed 3 times), 791 (unpaired), 793 (unpaired) |
| piece-15-06 | 4 | 7 | 206 (extra copy: likely misread), 566 (length mismatch), 568 (both tabs), 584 (line not found), 636 (unpaired), 660 (no tab), 999 (both tabs) |
| piece-04-07 | 2 | 7 | 303 (extra copy: likely misread), 395 (length mismatch), 420 (line not found), 422 (extra copy: likely misread), 731 (no tab), 780 (length mismatch), 784 (no tab) |
| piece-22-01 | 5 | 6 | 562 (no tab), 590 (length mismatch), 608 (length mismatch), 629 (length mismatch), 806 (length mismatch), 909 (unpaired) |
| piece-22-04 | 3 | 6 | 502 (both tabs), 564 (no tab), 581 (no tab), 589 (both tabs), 590 (length mismatch), 591 (unpaired) |
| piece-24-12 | 2 | 6 | 14 (extra copy: likely misread), 399 (length mismatch), 430 (extra copy: likely misread), 465 (length mismatch), 703 (no tab), 709 (both tabs) |
| piece-22-02 | 1 | 6 | 019 (unpaired), 390 (no tab), 512 (both tabs), 568 (both tabs), 581 (no tab), 881 (unpaired) |
| piece-20-01 | 7 | 6 | 57 (length mismatch), 63 (extra copy: likely misread), 78 (extra copy: likely misread), 81 (length mismatch), 86 (both tabs), 86 (both tabs) |
| piece-18-08 | 5 | 6 | 61 (no tab), 97 (unpaired), 104 (extra copy: likely misread), 115 (line not found), 136 (printed 3 times), 435 (length mismatch) |
| piece-24-05 | 0 | 6 | 061 (unpaired), 281 (both tabs), 282 (extra copy: likely misread), 283 (length mismatch), 370 (length mismatch), 384 (unpaired) |
| piece-11-04 | 7 | 6 | 77 (extra copy: likely misread), 745 (line not found), 768 (length mismatch), 769 (length mismatch), 770 (line not found), 778 (printed 3 times) |
| piece-20-02 | 4 | 6 | 118 (printed 3 times), 118 (printed 3 times), 118 (printed 3 times), 125 (unpaired), 126 (extra copy: likely misread), 145 (both tabs) |
| piece-16-10 | 1 | 6 | 141 (extra copy: likely misread), 283 (length mismatch), 361 (extra copy: likely misread), 385 (length mismatch), 497 (extra copy: likely misread), 648 (extra copy: likely misread) |
| piece-16-05 | 6 | 6 | 161 (length mismatch), 163 (both tabs), 182 (both tabs), 196 (no tab), 197 (length mismatch), 354 (extra copy: likely misread) |
| piece-16-09 | 6 | 6 | 162 (printed 3 times), 183 (no tab), 184 (extra copy: likely misread), 195 (length mismatch), 196 (no tab), 197 (length mismatch) |
| piece-14-06 | 8 | 6 | 171 (length mismatch), 175 (unpaired), 178 (extra copy: likely misread), 187 (extra copy: likely misread), 189 (length mismatch), 348 (no tab) |
| piece-16-03 | 8 | 6 | 368 (length mismatch), 369 (both tabs), 370 (length mismatch), 372 (length mismatch), 388 (length mismatch), 571 (printed 3 times) |
| piece-07-01 | 4 | 6 | 273 (both tabs), 392 (length mismatch), 572 (no tab), 618 (length mismatch), 619 (length mismatch), 821 (unpaired) |
| piece-15-01 | 2 | 6 | 288 (printed 3 times), 683 (length mismatch), 836 (unpaired), 840 (length mismatch), 842 (unpaired), 887 (unpaired) |
| piece-08-02 | 3 | 6 | 676 (length mismatch), 860 (unpaired), 862 (unpaired), 865 (both tabs), 866 (extra copy: likely misread), 867 (both tabs) |
| piece-09-03 | 3 | 6 | 353 (extra copy: likely misread), 573 (length mismatch), 577 (length mismatch), 658 (length mismatch), 680 (both tabs), 883 (length mismatch) |
| piece-06-04 | 5 | 6 | 369 (both tabs), 380 (extra copy: likely misread), 381 (unpaired), 386 (length mismatch), 388 (length mismatch), 392 (length mismatch) |
| piece-17-03 | 8 | 6 | 530 (length mismatch), 716 (length mismatch), 718 (length mismatch), 726 (line not found), 732 (unpaired), 830 (no tab) |
| piece-15-02 | 3 | 6 | 503 (unpaired), 504 (length mismatch), 511 (length mismatch), 596 (unpaired), 714 (line not found), 843 (unpaired) |
| piece-22-05 | 5 | 6 | 584 (line not found), 585 (both tabs), 592 (unpaired), 600 (length mismatch), 649 (length mismatch), 808 (length mismatch) |
| piece-09-01 | 2 | 6 | 634 (extra copy: likely misread), 640 (no tab), 653 (unpaired), 657 (no tab), 682 (length mismatch), 802 (no tab) |
| piece-09-02 | 2 | 6 | 652 (unpaired), 656 (length mismatch), 658 (length mismatch), 676 (length mismatch), 677 (length mismatch), 689 (no tab) |
| piece-17-01 | 3 | 6 | 708 (line not found), 723 (unpaired), 726 (line not found), 727 (length mismatch), 729 (length mismatch), 734 (length mismatch) |
| piece-11-02 | 4 | 5 | 00 (line not found), 010 (unpaired), 11 (line not found), 48 (length mismatch), 70 (extra copy: likely misread) |
| piece-18-06 | 6 | 5 | 2 (unpaired), 08 (line not found), 87 (no tab), 93 (length mismatch), 136 (printed 3 times) |
| piece-04-02 | 7 | 5 | 03 (unpaired), 396 (line not found), 412 (printed 3 times), 418 (extra copy: likely misread), 419 (line not found) |
| piece-20-06 | 7 | 5 | 09 (unpaired), 66 (no tab), 67 (printed 3 times), 79 (unpaired), 83 (unpaired) |
| piece-17-09 | 2 | 5 | 15 (line not found), 415 (unpaired), 655 (unpaired), 729 (length mismatch), 734 (length mismatch) |
| piece-23-03 | 4 | 5 | 022 (unpaired), 236 (length mismatch), 237 (both tabs), 239 (both tabs), 867 (both tabs) |
| piece-06-03 | 6 | 5 | 33 (length mismatch), 34 (line not found), 82 (extra copy: likely misread), 316 (length mismatch), 368 (length mismatch) |
| piece-06-06 | 4 | 5 | 32 (no tab), 272 (length mismatch), 316 (length mismatch), 419 (line not found), 689 (no tab) |
| piece-07-07 | 5 | 5 | 272 (length mismatch), 273 (both tabs), 274 (length mismatch), 278 (both tabs), 318 (length mismatch) |
| piece-05-05 | 5 | 5 | 40 (printed 3 times), 41 (length mismatch), 59 (length mismatch), 69 (both tabs), 81 (length mismatch) |
| piece-05-07 | 4 | 5 | 40 (printed 3 times), 64 (length mismatch), 68 (extra copy: likely misread), 192 (no tab), 778 (printed 3 times) |
| piece-24-16 | 2 | 5 | 59 (length mismatch), 462 (length mismatch), 571 (printed 3 times), 571 (printed 3 times), 576 (extra copy: likely misread) |
| piece-08-03 | 3 | 5 | 064 (unpaired), 662 (both tabs), 666 (unpaired), 868 (length mismatch), 883 (length mismatch) |
| piece-21-03 | 5 | 5 | 078 (unpaired), 476 (length mismatch), 477 (length mismatch), 482 (length mismatch), 490 (unpaired) |
| piece-18-01 | 3 | 5 | 88 (extra copy: likely misread), 346 (length mismatch), 397 (line not found), 738 (printed 3 times), 739 (both tabs) |
| piece-11-06 | 3 | 5 | 147 (length mismatch), 757 (length mismatch), 760 (printed 3 times), 777 (line not found), 781 (length mismatch) |
| piece-14-10 | 6 | 5 | 167 (both tabs), 169 (length mismatch), 171 (length mismatch), 185 (no tab), 360 (extra copy: likely misread) |
| piece-18-04 | 3 | 5 | 162 (printed 3 times), 185 (no tab), 188 (extra copy: likely misread), 189 (length mismatch), 192 (no tab) |
| piece-14-07 | 6 | 5 | 208 (extra copy: likely misread), 260 (extra copy: likely misread), 564 (no tab), 566 (length mismatch), 668 (no tab) |
| piece-23-05 | 6 | 5 | 200 (extra copy: likely misread), 210 (unpaired), 228 (unpaired), 237 (both tabs), 239 (both tabs) |
| piece-14-03 | 3 | 5 | 260 (extra copy: likely misread), 269 (both tabs), 286 (length mismatch), 640 (no tab), 768 (length mismatch) |
| piece-16-02 | 4 | 5 | 262 (extra copy: likely misread), 364 (length mismatch), 376 (both tabs), 379 (line not found), 385 (length mismatch) |
| piece-06-05 | 4 | 5 | 366 (length mismatch), 521 (extra copy: likely misread), 618 (length mismatch), 669 (both tabs), 847 (unpaired) |
| piece-08-01 | 6 | 5 | 663 (no tab), 669 (both tabs), 688 (both tabs), 882 (length mismatch), 882 (length mismatch) |
| piece-10-01 | 4 | 5 | 348 (no tab), 352 (extra copy: likely misread), 570 (extra copy: likely misread), 706 (extra copy: likely misread), 880 (unpaired) |
| piece-19-07 | 6 | 5 | 450 (both tabs), 454 (line not found), 462 (length mismatch), 481 (extra copy: likely misread), 496 (line not found) |
| piece-19-05 | 8 | 5 | 461 (extra copy: likely misread), 465 (length mismatch), 482 (length mismatch), 487 (length mismatch), 560 (unpaired) |
| piece-17-04 | 10 | 5 | 489 (length mismatch), 612 (extra copy: likely misread), 708 (line not found), 709 (both tabs), 714 (line not found) |
| piece-22-03 | 5 | 5 | 588 (unpaired), 604 (unpaired), 608 (length mismatch), 806 (length mismatch), 808 (length mismatch) |
| piece-24-06 | 1 | 5 | 631 (unpaired), 632 (both tabs), 682 (length mismatch), 718 (length mismatch), 727 (length mismatch) |
| piece-09-06 | 3 | 5 | 651 (length mismatch), 668 (no tab), 678 (unpaired), 680 (both tabs), 681 (unpaired) |
| piece-05-02 | 3 | 4 | 10 (line not found), 12 (extra copy: likely misread), 45 (length mismatch), 51 (both tabs) |
| piece-11-03 | 5 | 4 | 13 (length mismatch), 41 (length mismatch), 414 (extra copy: likely misread), 786 (no tab) |
| piece-16-01 | 1 | 4 | 15 (line not found), 159 (both tabs), 183 (no tab), 365 (unpaired) |
| piece-24-15 | 4 | 4 | 19 (extra copy: likely misread), 106 (printed 3 times), 215 (unpaired), 216 (extra copy: likely misread) |
| piece-06-01 | 5 | 4 | 20 (extra copy: likely misread), 28 (length mismatch), 355 (unpaired), 391 (unpaired) |
| piece-05-04 | 5 | 4 | 46 (printed 3 times), 53 (both tabs), 54 (length mismatch), 60 (length mismatch) |
| piece-24-04 | 4 | 4 | 54 (length mismatch), 99 (unpaired), 766 (unpaired), 794 (unpaired) |
| piece-11-11 | 2 | 4 | 57 (length mismatch), 760 (printed 3 times), 761 (both tabs), 762 (unpaired) |
| piece-22-06 | 6 | 4 | 60 (length mismatch), 565 (printed 3 times), 589 (both tabs), 605 (unpaired) |
| piece-24-07 | 4 | 4 | 082 (unpaired), 498 (no tab), 781 (length mismatch), 783 (unpaired) |
| piece-18-05 | 9 | 4 | 89 (no tab), 92 (unpaired), 105 (unpaired), 106 (printed 3 times) |
| piece-18-07 | 7 | 4 | 106 (printed 3 times), 169 (length mismatch), 195 (length mismatch), 363 (unpaired) |
| piece-13-02 | 6 | 4 | 758 (extra copy: likely misread), 784 (no tab), 787 (extra copy: likely misread), 992 (unpaired) |
| piece-04-05 | 6 | 4 | 395 (length mismatch), 398 (length mismatch), 416 (extra copy: likely misread), 896 (both tabs) |
| piece-12-07 | 3 | 4 | 545 (line not found), 548 (line not found), 695 (extra copy: likely misread), 840 (length mismatch) |
| piece-12-10 | 4 | 4 | 558 (no tab), 572 (no tab), 646 (extra copy: likely misread), 844 (length mismatch) |
| piece-07-06 | 5 | 4 | 265 (length mismatch), 287 (extra copy: likely misread), 296 (extra copy: likely misread), 827 (unpaired) |
| piece-07-10 | 2 | 4 | 274 (length mismatch), 295 (length mismatch), 295 (length mismatch), 657 (no tab) |
| piece-07-08 | 3 | 4 | 265 (length mismatch), 269 (both tabs), 297 (unpaired), 626 (extra copy: likely misread) |
| piece-24-01 | 2 | 4 | 276 (extra copy: likely misread), 277 (length mismatch), 278 (both tabs), 280 (unpaired) |
| piece-16-07 | 2 | 4 | 277 (length mismatch), 372 (length mismatch), 376 (both tabs), 736 (no tab) |
| piece-09-04 | 5 | 4 | 298 (length mismatch), 300 (length mismatch), 302 (unpaired), 323 (length mismatch) |
| piece-10-05 | 4 | 4 | 299 (unpaired), 328 (length mismatch), 338 (extra copy: likely misread), 752 (extra copy: likely misread) |
| piece-19-01 | 4 | 4 | 396 (line not found), 397 (line not found), 399 (length mismatch), 400 (printed 3 times) |
| piece-21-02 | 9 | 4 | 430 (extra copy: likely misread), 445 (unpaired), 466 (extra copy: likely misread), 483 (extra copy: likely misread) |
| piece-19-08 | 7 | 4 | 438 (unpaired), 477 (length mismatch), 493 (unpaired), 496 (line not found) |
| piece-19-06 | 7 | 4 | 448 (extra copy: likely misread), 456 (extra copy: likely misread), 470 (length mismatch), 665 (unpaired) |
| piece-19-03 | 4 | 4 | 539 (unpaired), 551 (no tab), 643 (both tabs), 644 (length mismatch) |
| piece-24-09 | 3 | 4 | 486 (both tabs), 499 (unpaired), 600 (length mismatch), 750 (length mismatch) |
| piece-15-04 | 3 | 4 | 505 (unpaired), 515 (unpaired), 544 (unpaired), 562 (no tab) |
| piece-15-07 | 6 | 4 | 559 (length mismatch), 561 (both tabs), 565 (printed 3 times), 580 (both tabs) |
| piece-19-02 | 2 | 4 | 507 (extra copy: likely misread), 538 (length mismatch), 844 (length mismatch), 886 (both tabs) |
| piece-15-03 | 3 | 4 | 551 (no tab), 637 (unpaired), 642 (unpaired), 643 (both tabs) |
| piece-17-10 | 8 | 4 | 513 (unpaired), 537 (no tab), 561 (both tabs), 565 (printed 3 times) |
| piece-15-08 | 10 | 4 | 527 (length mismatch), 536 (unpaired), 580 (both tabs), 632 (both tabs) |
| piece-13-03 | 6 | 4 | 538 (length mismatch), 644 (length mismatch), 687 (length mismatch), 786 (no tab) |
| piece-07-03 | 5 | 4 | 651 (length mismatch), 662 (both tabs), 853 (unpaired), 865 (both tabs) |
| piece-10-04 | 3 | 4 | 688 (both tabs), 703 (no tab), 818 (unpaired), 889 (length mismatch) |
| piece-11-09 | 4 | 3 | 43 (unpaired), 168 (extra copy: likely misread), 224 (length mismatch) |
| piece-24-03 | 4 | 3 | 13 (length mismatch), 750 (length mismatch), 789 (unpaired) |
| piece-11-07 | 4 | 3 | 757 (length mismatch), 760 (printed 3 times), 761 (both tabs) |
| piece-11-10 | 5 | 3 | 184 (extra copy: likely misread), 739 (both tabs), 780 (length mismatch) |
| piece-06-02 | 6 | 3 | 26 (extra copy: likely misread), 29 (unpaired), 386 (length mismatch) |
| piece-23-01 | 8 | 3 | 30 (extra copy: likely misread), 231 (unpaired), 236 (length mismatch) |
| piece-10-06 | 4 | 3 | 34 (line not found), 446 (no tab), 716 (length mismatch) |
| piece-10-07 | 4 | 3 | 046 (unpaired), 89 (no tab), 859 (no tab) |
| piece-20-03 | 8 | 3 | 116 (no tab), 119 (length mismatch), 126 (extra copy: likely misread) |
| piece-15-05 | 2 | 3 | 109 (extra copy: likely misread), 502 (both tabs), 805 (unpaired) |
| piece-18-02 | 3 | 3 | 163 (both tabs), 182 (both tabs), 186 (both tabs) |
| piece-20-04 | 7 | 3 | 129 (unpaired), 469 (length mismatch), 487 (length mismatch) |
| piece-21-04 | 7 | 3 | 476 (length mismatch), 481 (extra copy: likely misread), 489 (length mismatch) |
| piece-14-01 | 6 | 3 | 145 (both tabs), 147 (length mismatch), 298 (length mismatch) |
| piece-14-09 | 7 | 3 | 154 (both tabs), 159 (both tabs), 190 (extra copy: likely misread) |
| piece-14-02 | 4 | 3 | 281 (both tabs), 288 (printed 3 times), 293 (unpaired) |
| piece-12-03 | 6 | 3 | 154 (both tabs), 406 (extra copy: likely misread), 746 (unpaired) |
| piece-16-08 | 4 | 3 | 162 (printed 3 times), 167 (both tabs), 186 (both tabs) |
| piece-24-08 | 3 | 3 | 179 (unpaired), 288 (printed 3 times), 371 (unpaired) |
| piece-04-08 | 5 | 3 | 522 (extra copy: likely misread), 573 (length mismatch), 683 (length mismatch) |
| piece-17-05 | 9 | 3 | 470 (length mismatch), 558 (no tab), 613 (extra copy: likely misread) |
| piece-08-05 | 6 | 3 | 305 (both tabs), 312 (length mismatch), 314 (length mismatch) |
| piece-09-05 | 5 | 3 | 296 (extra copy: likely misread), 300 (length mismatch), 323 (length mismatch) |
| piece-08-04 | 8 | 3 | 318 (length mismatch), 328 (length mismatch), 889 (length mismatch) |
| piece-09-07 | 5 | 3 | 312 (length mismatch), 314 (length mismatch), 327 (unpaired) |
| piece-16-06 | 1 | 3 | 341 (line not found), 735 (line not found), 738 (printed 3 times) |
| piece-17-07 | 3 | 3 | 629 (length mismatch), 730 (unpaired), 944 (line not found) |
| piece-21-01 | 8 | 3 | 463 (unpaired), 473 (extra copy: likely misread), 486 (both tabs) |
| piece-15-10 | 8 | 3 | 527 (length mismatch), 537 (no tab), 559 (length mismatch) |
| piece-24-02 | 3 | 3 | 530 (length mismatch), 623 (extra copy: likely misread), 731 (no tab) |
| piece-07-02 | 3 | 3 | 619 (length mismatch), 624 (unpaired), 685 (extra copy: likely misread) |
| piece-12-11 | 3 | 3 | 649 (length mismatch), 848 (unpaired), 873 (unpaired) |
| piece-17-06 | 1 | 3 | 735 (line not found), 944 (line not found), 959 (unpaired) |
| piece-11-01 | 4 | 2 | 000 (unpaired), 33 (length mismatch) |
| piece-07-09 | 4 | 2 | 275 (unpaired), 802 (no tab) |
| piece-14-05 | 3 | 2 | 18 (extra copy: likely misread), 137 (length mismatch) |
| piece-05-06 | 6 | 2 | 224 (length mismatch), 234 (extra copy: likely misread) |
| piece-12-01 | 4 | 2 | 308 (length mismatch), 390 (no tab) |
| piece-23-02 | 5 | 2 | 27 (extra copy: likely misread), 250 (unpaired) |
| piece-12-09 | 5 | 2 | 28 (length mismatch), 677 (length mismatch) |
| piece-21-06 | 10 | 2 | 45 (length mismatch), 446 (no tab) |
| piece-20-08 | 4 | 2 | 53 (both tabs), 67 (printed 3 times) |
| piece-20-07 | 7 | 2 | 80 (length mismatch), 93 (length mismatch) |
| piece-24-11 | 5 | 2 | 98 (printed 3 times), 738 (printed 3 times) |
| piece-10-03 | 7 | 2 | 362 (unpaired), 868 (length mismatch) |
| piece-14-04 | 5 | 2 | 137 (length mismatch), 158 (no tab) |
| piece-14-08 | 8 | 2 | 178 (extra copy: likely misread), 291 (unpaired) |
| piece-04-03 | 10 | 2 | 403 (unpaired), 406 (extra copy: likely misread) |
| piece-12-02 | 7 | 2 | 258 (unpaired), 498 (no tab) |
| piece-17-02 | 3 | 2 | 512 (both tabs), 613 (extra copy: likely misread) |
| piece-23-06 | 8 | 2 | 226 (extra copy: likely misread), 248 (extra copy: likely misread) |
| piece-23-04 | 8 | 2 | 251 (unpaired), 346 (length mismatch) |
| piece-04-04 | 7 | 2 | 412 (printed 3 times), 412 (printed 3 times) |
| piece-07-05 | 5 | 2 | 625 (unpaired), 824 (unpaired) |
| piece-10-02 | 5 | 2 | 341 (line not found), 697 (unpaired) |
| piece-24-13 | 5 | 2 | 448 (extra copy: likely misread), 459 (unpaired) |
| piece-21-07 | 7 | 2 | 435 (length mismatch), 452 (unpaired) |
| piece-15-09 | 8 | 2 | 616 (extra copy: likely misread), 859 (no tab) |
| piece-17-08 | 5 | 2 | 656 (length mismatch), 999 (both tabs) |
| piece-07-04 | 4 | 2 | 660 (no tab), 663 (no tab) |
| piece-24-14 | 6 | 1 | 69 (both tabs) |
| piece-20-05 | 4 | 1 | 116 (no tab) |
| piece-04-01 | 6 | 1 | 400 (printed 3 times) |
| piece-12-08 | 6 | 1 | 308 (length mismatch) |
| piece-04-06 | 7 | 1 | 577 (length mismatch) |
| piece-08-06 | 7 | 1 | 305 (both tabs) |
| piece-13-04 | 4 | 1 | 687 (length mismatch) |
| piece-21-08 | 5 | 1 | 467 (unpaired) |

## Likely misreads

43 clear-cut misreads were fixed without asking (marked `applied` in `bowser-misreads.csv`). 194 more numbers that did not pair up sit on a line of the same length as another unpaired number on the other side (edge against tab), and the two numbers look alike. Check them with `make fix` and `app/number-check.html`.

| piece | side | mm | read | suggested | partner | partner mm | why |
|---|---|---:|---|---|---|---:|---|
| piece-04-04 | edge | 59.3 | 412 | 419 | piece-04-02 tab | 59.3 | OCR's other reading |
| piece-05-03 | tab | 34.3 | 58 | 59 | piece-05-05 edge | 34.3 | OCR's other reading |
| piece-05-04 | edge | 35.2 | 46 | 48 | piece-05-01 tab | 35.2 | OCR's other reading |
| piece-05-04 | edge | 27.5 | 60 | 80 | piece-05-03 tab | 27.5 | OCR's other reading |
| piece-06-01 | edge | 62.8 | 20 | 29 | piece-06-02 tab | 62.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-07-05 | tab | 40.7 | 824 | 624 | piece-07-02 edge | 40.7 | OCR's other reading |
| piece-07-07 | tab | 47.7 | 278 | 275 | piece-07-09 edge | 47.7 | one digit differs |
| piece-08-01 | edge | 17.4 | 882 | 682 | piece-09-01 tab | 17.4 | OCR's other reading |
| piece-08-01 | tab | 23.6 | 669 | 859 | piece-15-09 edge | 23.6 | OCR's other reading |
| piece-08-01 | tab | 26.3 | 882 | 802 | piece-09-01 edge | 26.3 | one digit differs |
| piece-08-02 | edge | 29.7 | 862 | 662 | piece-08-03 tab | 29.6 | OCR's other reading |
| piece-08-02 | tab | 46.8 | 866 | 668 | piece-09-06 edge | 46.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-10-01 | edge | 29.1 | 352 | 362 | piece-10-03 tab | 29.1 | OCR's other reading; the read number already pairs elsewhere |
| piece-11-10 | tab | 38.8 | 780 | 760 | piece-11-11 edge | 38.8 | OCR's other reading |
| piece-12-05 | edge | 15.6 | 161 | 154 | piece-12-03 tab | 15.6 | OCR's other reading |
| piece-12-10 | tab | 38.8 | 646 | 848 | piece-12-11 edge | 38.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-12-11 | edge | 58.9 | 873 | 573 | piece-04-08 tab | 58.9 | OCR's other reading |
| piece-14-01 | edge | 18.4 | 298 | 293 | piece-14-02 tab | 18.4 | OCR's other reading |
| piece-14-02 | edge | 24.1 | 288 | 269 | piece-14-03 tab | 24.1 | OCR's other reading |
| piece-14-02 | tab | 18.6 | 281 | 291 | piece-14-08 edge | 18.6 | OCR's other reading |
| piece-14-03 | tab | 24.3 | 286 | 288 | piece-15-01 edge | 24.3 | OCR's other reading |
| piece-14-07 | edge | 23.0 | 566 | 568 | piece-15-06 tab | 23.0 | OCR's other reading |
| piece-14-07 | edge | 24.5 | 668 | 566 | piece-15-06 tab | 24.6 | OCR's other reading |
| piece-14-08 | edge | 20.1 | 178 | 129 | piece-20-04 tab | 20.2 | OCR's other reading; the read number already pairs elsewhere |
| piece-15-02 | edge | 18.4 | 843 | 643 | piece-15-03 tab | 18.4 | OCR's other reading |
| piece-15-02 | edge | 31.4 | 504 | 544 | piece-15-04 tab | 31.4 | one digit differs |
| piece-15-03 | tab | 25.7 | 642 | 842 | piece-15-01 edge | 25.6 | OCR's other reading |
| piece-16-01 | edge | 33.0 | 183 | 163 | piece-16-05 tab | 33.1 | OCR's other reading |
| piece-16-05 | edge | 31.1 | 196 | 186 | piece-16-08 tab | 31.1 | OCR's other reading |
| piece-16-08 | tab | 25.2 | 167 | 197 | piece-16-09 edge | 25.2 | OCR's other reading |
| piece-17-03 | edge | 33.8 | 530 | 580 | piece-15-08 tab | 33.8 | OCR's other reading |
| piece-17-08 | tab | 40.0 | 656 | 558 | piece-12-10 edge | 39.9 | OCR's other reading |
| piece-18-04 | edge | 36.6 | 185 | 186 | piece-18-02 tab | 36.6 | OCR's other reading |
| piece-18-08 | edge | 29.9 | 61 | 81 | piece-20-01 tab | 30.0 | OCR's other reading |
| piece-19-02 | edge | 36.6 | 844 | 644 | piece-19-03 tab | 36.6 | one digit differs |
| piece-19-04 | edge | 33.8 | 483 | 493 | piece-19-08 tab | 33.9 | OCR's other reading; the read number already pairs elsewhere |
| piece-19-05 | tab | 26.3 | 482 | 462 | piece-24-16 edge | 26.3 | OCR's other reading |
| piece-19-05 | edge | 23.6 | 560 | 59 | piece-24-16 tab | 23.6 | OCR's other reading |
| piece-20-01 | tab | 23.3 | 86 | 98 | piece-24-11 edge | 23.3 | OCR's other reading |
| piece-20-01 | tab | 21.4 | 57 | 67 | piece-20-06 edge | 21.3 | one digit differs |
| piece-20-03 | edge | 34.8 | 119 | 118 | piece-20-02 tab | 34.8 | OCR's other reading |
| piece-21-03 | tab | 20.1 | 078 | 476 | piece-21-04 edge | 20.1 | OCR's other reading |
| piece-21-03 | tab | 34.8 | 476 | 470 | piece-17-05 edge | 34.7 | one digit differs |
| piece-21-04 | tab | 24.8 | 481 | 487 | piece-20-04 edge | 24.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-22-02 | edge | 45.9 | 581 | 591 | piece-22-04 tab | 45.9 | OCR's other reading |
| piece-22-02 | edge | 44.1 | 390 | 590 | piece-22-04 tab | 44.1 | OCR's other reading |
| piece-22-04 | tab | 43.9 | 502 | 592 | piece-22-05 edge | 43.9 | OCR's other reading |
| piece-22-04 | edge | 37.1 | 564 | 584 | piece-22-05 tab | 37.2 | OCR's other reading |
| piece-22-06 | tab | 30.7 | 60 | 600 | piece-22-05 edge | 30.7 | OCR's other reading |
| piece-24-07 | tab | 25.4 | 082 | 780 | piece-04-07 edge | 25.4 | OCR's other reading |
| piece-24-08 | edge | 13.0 | 371 | 571 | piece-16-03 tab | 13.0 | OCR's other reading |
| piece-24-09 | tab | 30.9 | 499 | 498 | piece-12-02 edge | 31.0 | OCR's other reading |
| piece-24-13 | edge | 36.3 | 459 | 450 | piece-19-07 tab | 36.3 | OCR's other reading |
| piece-04-08 | edge | 44.6 | 683 | 568 | piece-22-02 tab | 44.5 | OCR's other reading |
| piece-04-08 | tab | 50.2 | 522 | 572 | piece-12-10 edge | 50.2 | OCR's other reading; the read number already pairs elsewhere |
| piece-05-04 | tab | 42.8 | 53 | 58 | piece-05-01 edge | 42.7 | OCR's other reading |
| piece-05-07 | tab | 25.5 | 68 | 99 | piece-24-04 edge | 25.3 | OCR's other reading; the read number already pairs elsewhere |
| piece-06-01 | edge | 42.1 | 391 | 381 | piece-06-04 tab | 42.1 | OCR's other reading |
| piece-06-05 | edge | 46.4 | 366 | 388 | piece-06-04 tab | 46.3 | OCR's other reading |
| piece-06-05 | edge | 33.1 | 521 | 821 | piece-07-01 tab | 33.0 | one digit differs; the read number already pairs elsewhere |
| piece-06-06 | edge | 30.8 | 689 | 669 | piece-06-05 tab | 30.7 | OCR's other reading |
| piece-07-06 | tab | 52.0 | 287 | 297 | piece-07-08 edge | 51.9 | OCR's other reading; the read number already pairs elsewhere |
| piece-07-08 | edge | 39.4 | 626 | 625 | piece-07-05 tab | 39.5 | OCR's other reading; the read number already pairs elsewhere |
| piece-07-10 | edge | 40.7 | 657 | 269 | piece-07-08 tab | 40.7 | OCR's other reading |
| piece-07-10 | edge | 47.8 | 295 | 265 | piece-07-06 tab | 47.7 | OCR's other reading |
| piece-08-03 | edge | 48.0 | 868 | 865 | piece-08-02 tab | 48.1 | OCR's other reading |
| piece-08-04 | edge | 26.3 | 328 | 376 | piece-16-07 tab | 26.2 | OCR's other reading |
| piece-09-02 | edge | 44.3 | 689 | 680 | piece-09-06 tab | 44.2 | OCR's other reading |
| piece-10-01 | tab | 49.6 | 706 | 716 | piece-10-06 edge | 49.6 | one digit differs; the read number already pairs elsewhere |
| piece-10-01 | edge | 100.0 | 880 | 889 | piece-10-04 tab | 99.9 | one digit differs |
| piece-10-05 | edge | 42.3 | 299 | 298 | piece-09-04 tab | 42.1 | OCR's other reading |
| piece-10-05 | edge | 17.4 | 338 | 318 | piece-08-04 tab | 17.3 | one digit differs; the read number already pairs elsewhere |
| piece-10-06 | tab | 74.5 | 34 | 348 | piece-10-01 edge | 74.4 | a digit dropped or added |
| piece-11-01 | edge | 31.1 | 33 | 13 | piece-11-03 tab | 31.0 | one digit differs |
| piece-11-04 | tab | 26.6 | 769 | 768 | piece-14-03 edge | 26.4 | one digit differs |
| piece-12-01 | edge | 34.3 | 390 | 369 | piece-06-04 tab | 34.4 | OCR's other reading |
| piece-12-05 | tab | 30.5 | 748 | 746 | piece-12-03 edge | 30.6 | OCR's other reading; the read number already pairs elsewhere |
| piece-12-10 | tab | 42.3 | 844 | 644 | piece-13-03 edge | 42.4 | OCR's other reading |
| piece-12-11 | tab | 56.0 | 649 | 640 | piece-09-01 edge | 56.0 | OCR's other reading |
| piece-13-02 | edge | 50.7 | 784 | 761 | piece-11-11 tab | 50.8 | OCR's other reading |
| piece-13-02 | tab | 51.6 | 787 | 57 | piece-11-11 edge | 51.7 | OCR's other reading; the read number already pairs elsewhere |
| piece-14-06 | edge | 30.3 | 187 | 167 | piece-14-10 tab | 30.4 | OCR's other reading; the read number already pairs elsewhere |
| piece-14-09 | tab | 30.7 | 190 | 185 | piece-14-10 edge | 30.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-14-09 | tab | 44.6 | 159 | 158 | piece-14-04 edge | 44.5 | one digit differs |
| piece-15-01 | tab | 18.6 | 840 | 640 | piece-14-03 edge | 18.7 | OCR's other reading |
| piece-15-04 | edge | 33.9 | 562 | 502 | piece-15-05 tab | 33.8 | OCR's other reading |
| piece-15-05 | edge | 45.3 | 805 | 505 | piece-15-04 tab | 45.2 | one digit differs |
| piece-15-07 | edge | 14.7 | 565 | 999 | piece-15-06 tab | 14.6 | OCR's other reading |
| piece-15-07 | tab | 18.7 | 580 | 660 | piece-15-06 edge | 18.8 | OCR's other reading |
| piece-16-01 | tab | 22.1 | 159 | 158 | piece-16-04 edge | 22.2 | one digit differs |
| piece-16-03 | tab | 22.4 | 368 | 388 | piece-16-03 edge | 22.5 | OCR's other reading |
| piece-16-04 | tab | 27.2 | 886 | 365 | piece-16-01 edge | 27.3 | OCR's other reading |
| piece-16-08 | edge | 35.3 | 162 | 182 | piece-16-05 tab | 35.1 | OCR's other reading |
| piece-17-04 | tab | 37.8 | 709 | 703 | piece-10-04 edge | 37.9 | OCR's other reading |
| piece-18-02 | tab | 30.9 | 163 | 183 | piece-16-09 edge | 31.0 | OCR's other reading |
| piece-18-03 | tab | 26.0 | 95 | 98 | piece-19-04 edge | 25.8 | OCR's other reading |
| piece-18-05 | tab | 26.1 | 105 | 106 | piece-24-15 edge | 26.0 | OCR's other reading |
| piece-18-05 | edge | 25.7 | 92 | 2 | piece-18-06 tab | 25.6 | OCR's other reading |
| piece-19-03 | tab | 30.6 | 643 | 513 | piece-17-10 edge | 30.5 | OCR's other reading |
| piece-19-05 | edge | 42.1 | 461 | 481 | piece-19-07 tab | 42.1 | OCR's other reading; the read number already pairs elsewhere |
| piece-20-01 | tab | 32.3 | 86 | 80 | piece-20-07 edge | 32.3 | OCR's other reading |
| piece-20-01 | edge | 37.5 | 78 | 79 | piece-20-06 tab | 37.4 | OCR's other reading; the read number already pairs elsewhere |
| piece-20-08 | tab | 31.1 | 67 | 87 | piece-18-06 edge | 30.9 | OCR's other reading |
| piece-21-02 | tab | 21.3 | 445 | 446 | piece-21-06 edge | 21.2 | OCR's other reading |
| piece-21-02 | edge | 42.4 | 483 | 463 | piece-21-01 tab | 42.3 | OCR's other reading; the read number already pairs elsewhere |
| piece-21-02 | edge | 16.2 | 466 | 486 | piece-21-01 tab | 16.3 | OCR's other reading; the read number already pairs elsewhere |
| piece-21-02 | tab | 29.9 | 430 | 438 | piece-19-08 edge | 29.9 | one digit differs; the read number already pairs elsewhere |
| piece-21-04 | tab | 40.9 | 489 | 469 | piece-20-04 edge | 41.0 | OCR's other reading |
| piece-21-08 | edge | 23.1 | 467 | 487 | piece-19-05 tab | 23.3 | OCR's other reading |
| piece-22-01 | tab | 37.6 | 608 | 808 | piece-22-05 edge | 37.6 | OCR's other reading |
| piece-22-01 | edge | 32.2 | 806 | 808 | piece-22-03 tab | 32.3 | OCR's other reading |
| piece-22-01 | edge | 42.2 | 562 | 512 | piece-22-02 tab | 42.1 | one digit differs |
| piece-22-02 | tab | 39.5 | 881 | 581 | piece-22-04 edge | 39.5 | OCR's other reading |
| piece-22-06 | edge | 34.8 | 605 | 806 | piece-22-03 tab | 34.9 | OCR's other reading |
| piece-23-02 | edge | 44.1 | 27 | 237 | piece-23-03 tab | 44.0 | OCR's other reading; the read number already pairs elsewhere |
| piece-23-06 | edge | 23.3 | 226 | 228 | piece-23-05 tab | 23.3 | OCR's other reading; the read number already pairs elsewhere |
| piece-23-06 | edge | 30.4 | 248 | 346 | piece-23-04 tab | 30.3 | OCR's other reading; the read number already pairs elsewhere |
| piece-24-02 | tab | 20.4 | 530 | 830 | piece-17-03 edge | 20.5 | one digit differs |
| piece-24-04 | edge | 32.3 | 54 | 64 | piece-05-07 tab | 32.3 | OCR's other reading |
| piece-24-04 | tab | 24.1 | 766 | 760 | piece-11-06 edge | 24.2 | OCR's other reading |
| piece-24-09 | tab | 43.1 | 600 | 840 | piece-12-07 edge | 43.2 | OCR's other reading |
| piece-24-13 | tab | 18.9 | 448 | 446 | piece-10-06 edge | 18.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-04-02 | tab | 45.9 | 418 | 416 | piece-04-05 edge | 46.1 | OCR's other reading; the read number already pairs elsewhere |
| piece-04-05 | tab | 27.8 | 896 | 396 | piece-04-02 edge | 27.6 | OCR's other reading |
| piece-06-03 | tab | 46.3 | 82 | 32 | piece-06-06 edge | 46.5 | OCR's other reading; the read number already pairs elsewhere |
| piece-06-03 | edge | 54.8 | 368 | 886 | piece-19-02 tab | 54.5 | OCR's other reading |
| piece-07-06 | edge | 40.6 | 827 | 327 | piece-09-07 tab | 40.8 | OCR's other reading |
| piece-08-03 | edge | 58.3 | 666 | 688 | piece-08-01 tab | 58.1 | OCR's other reading |
| piece-12-05 | edge | 13.1 | 769 | 768 | piece-11-04 tab | 12.9 | OCR's other reading |
| piece-14-07 | tab | 17.9 | 208 | 708 | piece-17-01 edge | 17.7 | OCR's other reading; the read number already pairs elsewhere |
| piece-14-10 | edge | 36.2 | 360 | 366 | piece-16-04 tab | 36.4 | OCR's other reading; the read number already pairs elsewhere |
| piece-15-05 | tab | 26.4 | 109 | 909 | piece-22-01 edge | 26.2 | one digit differs; the read number already pairs elsewhere |
| piece-16-04 | edge | 29.9 | 164 | 154 | piece-14-09 tab | 30.1 | OCR's other reading; the read number already pairs elsewhere |
| piece-16-04 | tab | 19.4 | 383 | 363 | piece-18-07 edge | 19.6 | OCR's other reading |
| piece-17-04 | edge | 27.2 | 612 | 512 | piece-17-02 tab | 27.3 | OCR's other reading; the read number already pairs elsewhere |
| piece-18-01 | tab | 23.3 | 739 | 738 | piece-24-11 edge | 23.1 | OCR's other reading |
| piece-18-02 | tab | 37.2 | 182 | 192 | piece-18-04 edge | 37.0 | OCR's other reading |
| piece-18-03 | tab | 30.1 | 67 | 97 | piece-18-08 edge | 30.0 | one digit differs |
| piece-18-08 | edge | 14.6 | 104 | 101 | piece-18-03 tab | 14.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-20-01 | tab | 22.8 | 63 | 83 | piece-20-06 edge | 22.6 | OCR's other reading; the read number already pairs elsewhere |
| piece-20-02 | tab | 24.9 | 118 | 116 | piece-20-03 edge | 24.7 | OCR's other reading |
| piece-20-03 | tab | 23.3 | 126 | 125 | piece-20-02 edge | 23.1 | OCR's other reading; the read number already pairs elsewhere |
| piece-22-06 | edge | 29.8 | 565 | 585 | piece-22-05 tab | 30.0 | OCR's other reading |
| piece-22-06 | tab | 30.1 | 589 | 588 | piece-22-03 edge | 29.9 | one digit differs |
| piece-23-01 | edge | 36.8 | 236 | 239 | piece-23-05 tab | 37.0 | one digit differs |
| piece-23-04 | edge | 34.5 | 251 | 231 | piece-23-01 tab | 34.6 | one digit differs |
| piece-24-06 | tab | 32.7 | 632 | 682 | piece-24-06 edge | 32.5 | OCR's other reading |
| piece-24-12 | tab | 50.7 | 709 | 703 | piece-24-12 edge | 50.6 | OCR's other reading |
| piece-24-14 | tab | 25.9 | 69 | 89 | piece-10-07 edge | 25.7 | OCR's other reading |
| piece-05-06 | edge | 44.1 | 234 | 237 | piece-23-05 tab | 44.5 | OCR's other reading; the read number already pairs elsewhere |
| piece-06-02 | tab | 49.1 | 26 | 28 | piece-06-01 edge | 48.8 | OCR's other reading; the read number already pairs elsewhere |
| piece-08-03 | tab | 27.0 | 883 | 663 | piece-08-01 edge | 27.3 | OCR's other reading |
| piece-09-02 | tab | 50.6 | 677 | 87 | piece-05-01 edge | 50.9 | OCR's other reading |
| piece-09-06 | tab | 25.3 | 678 | 676 | piece-08-02 edge | 25.6 | OCR's other reading |
| piece-13-02 | edge | 42.3 | 758 | 750 | piece-24-03 tab | 42.0 | one digit differs; the read number already pairs elsewhere |
| piece-15-03 | edge | 22.7 | 637 | 887 | piece-15-01 tab | 23.1 | OCR's other reading |
| piece-15-09 | tab | 42.1 | 616 | 515 | piece-15-04 edge | 42.3 | OCR's other reading; the read number already pairs elsewhere |
| piece-16-05 | edge | 29.9 | 354 | 364 | piece-16-04 tab | 29.7 | one digit differs; the read number already pairs elsewhere |
| piece-18-01 | tab | 33.0 | 738 | 736 | piece-18-03 edge | 32.8 | OCR's other reading |
| piece-19-06 | edge | 35.8 | 456 | 465 | piece-19-05 tab | 36.0 | OCR's other reading; the read number already pairs elsewhere |
| piece-24-01 | edge | 37.4 | 276 | 278 | piece-24-01 tab | 37.7 | OCR's other reading; the read number already pairs elsewhere |
| piece-24-03 | edge | 18.1 | 789 | 729 | piece-17-09 tab | 17.9 | one digit differs |
| piece-24-09 | tab | 53.2 | 486 | 498 | piece-24-07 edge | 52.8 | OCR's other reading |
| piece-06-04 | tab | 43.2 | 386 | 786 | piece-11-03 edge | 43.6 | one digit differs |
| piece-09-04 | tab | 30.5 | 302 | 802 | piece-07-09 edge | 30.2 | OCR's other reading |
| piece-12-09 | tab | 42.5 | 28 | 258 | piece-12-02 edge | 42.8 | OCR's other reading |
| piece-14-06 | tab | 19.4 | 178 | 179 | piece-24-08 edge | 19.9 | OCR's other reading; the read number already pairs elsewhere |
| piece-15-01 | tab | 32.2 | 836 | 636 | piece-15-06 edge | 32.6 | OCR's other reading |
| piece-15-03 | edge | 27.9 | 551 | 561 | piece-15-07 tab | 28.3 | OCR's other reading |
| piece-05-01 | tab | 24.4 | 46 | 48 | piece-11-02 edge | 23.9 | OCR's other reading |
| piece-10-07 | tab | 63.7 | 046 | 346 | piece-18-01 edge | 63.2 | OCR's other reading |
| piece-11-07 | tab | 23.3 | 761 | 781 | piece-11-06 edge | 23.8 | OCR's other reading |
| piece-14-06 | edge | 32.1 | 189 | 169 | piece-14-10 tab | 31.5 | OCR's other reading |
| piece-16-04 | edge | 13.8 | 286 | 288 | piece-24-08 tab | 13.3 | OCR's other reading |
| piece-19-04 | tab | 17.5 | 450 | 750 | piece-24-09 edge | 18.1 | one digit differs |
| piece-12-06 | tab | 43.5 | 896 | 596 | piece-15-02 edge | 42.9 | one digit differs |
| piece-14-07 | edge | 10.2 | 564 | 98 | piece-18-03 tab | 9.6 | OCR's other reading |
| piece-16-02 | edge | 20.6 | 262 | 282 | piece-24-05 tab | 20.0 | OCR's other reading; the read number already pairs elsewhere |
| piece-16-04 | edge | 24.0 | 181 | 161 | piece-16-05 tab | 23.5 | OCR's other reading; the read number already pairs elsewhere |
| piece-21-06 | tab | 39.5 | 45 | 40 | piece-05-07 edge | 38.9 | one digit differs |
| piece-05-01 | tab | 41.4 | 46 | 45 | piece-05-02 edge | 40.7 | OCR's other reading |
| piece-09-01 | edge | 42.3 | 657 | 687 | piece-13-04 tab | 43.0 | OCR's other reading |
| piece-16-06 | tab | 42.0 | 738 | 736 | piece-16-07 edge | 41.3 | OCR's other reading |
| piece-19-02 | tab | 30.9 | 507 | 537 | piece-15-10 edge | 30.2 | one digit differs; the read number already pairs elsewhere |
| piece-20-05 | edge | 24.6 | 116 | 145 | piece-20-02 tab | 25.3 | OCR's other reading |
| piece-15-08 | tab | 30.2 | 632 | 537 | piece-17-10 edge | 31.0 | OCR's other reading |
| piece-04-01 | edge | 40.4 | 400 | 403 | piece-04-03 tab | 41.3 | OCR's other reading |
| piece-04-07 | tab | 28.9 | 422 | 482 | piece-21-03 edge | 28.0 | one digit differs; the read number already pairs elsewhere |
| piece-14-05 | edge | 26.0 | 18 | 188 | piece-18-04 tab | 25.1 | a digit dropped or added; the read number already pairs elsewhere |
| piece-07-01 | tab | 29.0 | 618 | 608 | piece-22-03 edge | 28.0 | one digit differs |
| piece-07-07 | edge | 37.4 | 318 | 316 | piece-06-06 tab | 38.3 | OCR's other reading |
| piece-09-07 | edge | 25.8 | 312 | 412 | piece-04-04 tab | 26.7 | one digit differs |
| piece-16-10 | tab | 18.0 | 361 | 384 | piece-24-05 edge | 18.9 | OCR's other reading; the read number already pairs elsewhere |
| piece-24-15 | edge | 23.6 | 216 | 716 | piece-17-03 tab | 22.6 | OCR's other reading; the read number already pairs elsewhere |

Full tables: `bowser-edges.csv`, `bowser-misreads.csv`.
