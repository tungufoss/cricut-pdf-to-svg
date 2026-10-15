# Bowser

1570 printed numbers on 178 pieces. 328 numbers form a clean pair (one plain edge, one tab, lengths within 1 mm); 914 labels need a look.

Conversion status (2026-10-15), written by `make`. Edit the YAML, not this file.

## Files

| file | what | in git |
|---|---|---|
| `bowser.pdf` | source template | no, personal use only |
| `bowser.yaml` | pages per cardstock, fold styles, sheet size | yes |
| `bowser.svg` | Inkscape review file, one row of pages per cardstock | no, traced pattern |
| `previews/` | rendered PDF pages, the SVG's faint Source layer | no |
| `bowser-edges.csv` | every printed edge number with its line and partner | yes |
| `README.md` | this status page | yes |

## Status

| stage | result |
|---|---|
| pages | 21 converted |
| pieces | 178 cut outlines, corners joined by straight edges |
| folds | 1496, 13 stretched far to reach the cut |
| numbers | 1570 read, 685 uncertain (orange in the SVG) |
| pieces to check | 174 marked ⚠ in Inkscape |
| paper colour | footers disagree with the YAML: pages 14–23 say beige (YAML: yellow); page 24 says white (YAML: black) |
| nesting on sheets | not started |

## Edge numbers

| status | labels | meaning |
|---|---:|---|
| ok | 656 | partner found, one tab and one plain edge, same length |
| length mismatch | 264 | partner found but the marked lines differ in length: misread number or traced line |
| printed 3 times | 237 | number read more than twice: some are misread |
| unpaired | 119 | no other copy of this number: likely misread |
| both tabs | 106 | both copies sit on a tab fold |
| no tab | 98 | neither copy sits on a tab fold |
| line not found | 58 | no cut edge or fold next to the number |
| printed 4 times | 32 | number read more than twice: some are misread |

## Pages

| page | config material | footer says | pieces | ok | check |
|---|---|---|---:|---:|---:|
| 04 | red | red | 8 | 28 | 47 |
| 05 | red | red | 8 | 33 | 42 |
| 06 | red | red | 6 | 25 | 33 |
| 07 | red | red | 10 | 31 | 45 |
| 08 | red | red | 6 | 26 | 30 |
| 09 | red | red | 7 | 20 | 38 |
| 10 | red | red | 7 | 26 | 28 |
| 11 | green | green | 11 | 34 | 56 |
| 12 | green | green | 11 | 34 | 56 |
| 13 | green | green | 4 | 17 | 13 |
| 14 | yellow | beige ⚠ | 10 | 40 | 52 |
| 15 | yellow | beige ⚠ | 10 | 45 | 47 |
| 16 | yellow | beige ⚠ | 10 | 30 | 61 |
| 17 | yellow | beige ⚠ | 10 | 44 | 47 |
| 18 | yellow | beige ⚠ | 8 | 29 | 53 |
| 19 | yellow | beige ⚠ | 8 | 30 | 52 |
| 20 | yellow | beige ⚠ | 8 | 33 | 43 |
| 21 | yellow | beige ⚠ | 8 | 45 | 31 |
| 22 | yellow | beige ⚠ | 6 | 20 | 38 |
| 23 | yellow | beige ⚠ | 6 | 33 | 25 |
| 24 | black | white ⚠ | 16 | 33 | 77 |

## Pieces to check

Pieces listed by how many of their numbers need a look.

| piece | ok | check | numbers to check |
|---|---:|---:|---|
| piece-19-04 | 4 | 10 | 98 (printed 3 times), 398 (length mismatch), 400 (printed 3 times), 450 (both tabs), 454 (line not found), 456 (printed 3 times), 457 (unpaired), 461 (printed 3 times), 469 (length mismatch), 483 (printed 4 times) |
| piece-16-04 | 5 | 10 | 158 (no tab), 164 (no tab), 178 (printed 4 times), 181 (printed 3 times), 286 (length mismatch), 364 (length mismatch), 366 (length mismatch), 379 (line not found), 383 (unpaired), 886 (both tabs) |
| piece-04-02 | 3 | 9 | 03 (unpaired), 396 (line not found), 411 (printed 3 times), 412 (printed 3 times), 414 (printed 3 times), 418 (printed 3 times), 418 (printed 3 times), 419 (line not found), 445 (both tabs) |
| piece-12-04 | 1 | 9 | 04 (line not found), 04 (line not found), 11 (line not found), 40 (printed 3 times), 90 (unpaired), 94 (line not found), 420 (printed 3 times), 593 (line not found), 742 (length mismatch) |
| piece-05-01 | 3 | 9 | 10 (line not found), 46 (printed 3 times), 46 (printed 3 times), 47 (unpaired), 48 (length mismatch), 58 (printed 3 times), 61 (no tab), 87 (no tab), 411 (printed 3 times) |
| piece-20-01 | 4 | 9 | 57 (length mismatch), 63 (printed 3 times), 78 (printed 3 times), 81 (length mismatch), 82 (printed 3 times), 84 (printed 3 times), 86 (both tabs), 86 (both tabs), 126 (printed 3 times) |
| piece-16-09 | 3 | 9 | 162 (printed 3 times), 164 (no tab), 183 (no tab), 188 (printed 3 times), 190 (printed 3 times), 195 (length mismatch), 196 (no tab), 197 (length mismatch), 494 (printed 3 times) |
| piece-14-06 | 5 | 9 | 171 (length mismatch), 175 (unpaired), 177 (printed 3 times), 178 (printed 4 times), 178 (printed 4 times), 181 (printed 3 times), 187 (printed 3 times), 189 (length mismatch), 348 (no tab) |
| piece-19-05 | 4 | 9 | 461 (printed 3 times), 465 (length mismatch), 466 (length mismatch), 473 (printed 3 times), 482 (length mismatch), 483 (printed 4 times), 484 (printed 3 times), 487 (length mismatch), 560 (unpaired) |
| piece-12-06 | 0 | 8 | 00 (line not found), 504 (length mismatch), 511 (length mismatch), 545 (line not found), 548 (line not found), 585 (both tabs), 593 (line not found), 896 (both tabs) |
| piece-22-01 | 3 | 8 | 4 (unpaired), 012 (unpaired), 562 (no tab), 590 (length mismatch), 608 (length mismatch), 629 (length mismatch), 806 (length mismatch), 909 (unpaired) |
| piece-18-03 | 6 | 8 | 08 (line not found), 67 (printed 3 times), 95 (unpaired), 98 (printed 3 times), 101 (unpaired), 136 (printed 3 times), 353 (length mismatch), 736 (no tab) |
| piece-20-06 | 4 | 8 | 09 (unpaired), 66 (no tab), 67 (printed 3 times), 70 (printed 3 times), 77 (printed 3 times), 78 (printed 3 times), 79 (length mismatch), 83 (unpaired) |
| piece-12-05 | 5 | 8 | 011 (unpaired), 161 (length mismatch), 177 (printed 3 times), 742 (length mismatch), 745 (line not found), 748 (printed 3 times), 769 (length mismatch), 830 (no tab) |
| piece-11-03 | 1 | 8 | 12 (printed 3 times), 13 (length mismatch), 14 (printed 3 times), 41 (length mismatch), 414 (printed 3 times), 748 (printed 3 times), 752 (printed 3 times), 786 (no tab) |
| piece-18-05 | 5 | 8 | 84 (printed 3 times), 89 (no tab), 92 (unpaired), 104 (printed 3 times), 105 (unpaired), 106 (printed 3 times), 108 (printed 3 times), 109 (both tabs) |
| piece-18-04 | 0 | 8 | 162 (printed 3 times), 185 (no tab), 187 (printed 3 times), 188 (printed 3 times), 188 (printed 3 times), 189 (length mismatch), 190 (printed 3 times), 192 (no tab) |
| piece-16-03 | 6 | 8 | 177 (printed 3 times), 368 (length mismatch), 369 (both tabs), 370 (length mismatch), 372 (length mismatch), 388 (length mismatch), 571 (printed 3 times), 880 (no tab) |
| piece-07-01 | 2 | 8 | 273 (both tabs), 392 (length mismatch), 572 (no tab), 616 (length mismatch), 618 (length mismatch), 619 (length mismatch), 626 (no tab), 821 (unpaired) |
| piece-17-04 | 7 | 8 | 489 (length mismatch), 522 (printed 3 times), 546 (unpaired), 612 (no tab), 634 (length mismatch), 708 (line not found), 709 (both tabs), 714 (line not found) |
| piece-18-06 | 4 | 7 | 2 (unpaired), 08 (line not found), 87 (no tab), 93 (length mismatch), 94 (line not found), 108 (printed 3 times), 136 (printed 3 times) |
| piece-23-03 | 2 | 7 | 022 (unpaired), 226 (printed 3 times), 234 (no tab), 236 (length mismatch), 237 (both tabs), 239 (both tabs), 867 (both tabs) |
| piece-06-03 | 4 | 7 | 27 (printed 3 times), 30 (printed 3 times), 33 (length mismatch), 34 (line not found), 82 (printed 3 times), 316 (length mismatch), 368 (length mismatch) |
| piece-05-03 | 5 | 7 | 32 (no tab), 51 (both tabs), 58 (printed 3 times), 58 (printed 3 times), 64 (length mismatch), 80 (length mismatch), 115 (line not found) |
| piece-05-07 | 2 | 7 | 40 (printed 3 times), 63 (printed 3 times), 64 (length mismatch), 68 (length mismatch), 192 (no tab), 778 (printed 3 times), 787 (printed 3 times) |
| piece-11-05 | 3 | 7 | 66 (no tab), 119 (length mismatch), 770 (line not found), 777 (line not found), 778 (printed 3 times), 791 (unpaired), 793 (unpaired) |
| piece-16-05 | 5 | 7 | 161 (length mismatch), 163 (both tabs), 182 (both tabs), 196 (no tab), 197 (length mismatch), 354 (length mismatch), 764 (printed 3 times) |
| piece-14-10 | 4 | 7 | 167 (both tabs), 168 (printed 3 times), 169 (length mismatch), 171 (length mismatch), 181 (printed 3 times), 185 (no tab), 360 (printed 3 times) |
| piece-15-06 | 4 | 7 | 206 (printed 3 times), 566 (length mismatch), 568 (both tabs), 584 (line not found), 636 (length mismatch), 660 (no tab), 999 (both tabs) |
| piece-14-03 | 1 | 7 | 210 (no tab), 269 (both tabs), 286 (length mismatch), 287 (printed 3 times), 292 (unpaired), 640 (no tab), 768 (length mismatch) |
| piece-04-07 | 2 | 7 | 303 (printed 3 times), 395 (length mismatch), 420 (printed 3 times), 422 (printed 3 times), 731 (no tab), 780 (length mismatch), 784 (no tab) |
| piece-08-02 | 2 | 7 | 666 (length mismatch), 676 (length mismatch), 860 (unpaired), 862 (unpaired), 865 (both tabs), 866 (length mismatch), 867 (both tabs) |
| piece-09-03 | 2 | 7 | 353 (length mismatch), 573 (length mismatch), 577 (length mismatch), 658 (length mismatch), 665 (no tab), 680 (both tabs), 883 (length mismatch) |
| piece-17-03 | 7 | 7 | 530 (length mismatch), 633 (printed 3 times), 716 (length mismatch), 718 (length mismatch), 726 (line not found), 732 (unpaired), 830 (no tab) |
| piece-19-07 | 4 | 7 | 450 (both tabs), 454 (line not found), 462 (length mismatch), 481 (printed 4 times), 483 (printed 4 times), 488 (printed 3 times), 496 (line not found) |
| piece-19-06 | 4 | 7 | 448 (printed 3 times), 456 (printed 3 times), 464 (no tab), 470 (length mismatch), 473 (printed 3 times), 665 (no tab), 705 (unpaired) |
| piece-22-04 | 2 | 7 | 502 (both tabs), 564 (no tab), 581 (no tab), 588 (length mismatch), 589 (both tabs), 590 (length mismatch), 591 (unpaired) |
| piece-22-05 | 4 | 7 | 576 (line not found), 584 (line not found), 585 (both tabs), 592 (unpaired), 600 (length mismatch), 649 (length mismatch), 808 (length mismatch) |
| piece-09-01 | 1 | 7 | 634 (length mismatch), 640 (no tab), 653 (unpaired), 657 (no tab), 682 (length mismatch), 685 (length mismatch), 802 (no tab) |
| piece-11-02 | 3 | 6 | 00 (line not found), 010 (unpaired), 11 (line not found), 26 (printed 3 times), 48 (length mismatch), 70 (printed 3 times) |
| piece-24-12 | 2 | 6 | 14 (printed 3 times), 399 (length mismatch), 430 (printed 3 times), 465 (length mismatch), 703 (no tab), 709 (both tabs) |
| piece-22-02 | 1 | 6 | 019 (unpaired), 390 (no tab), 512 (both tabs), 568 (both tabs), 581 (no tab), 881 (unpaired) |
| piece-24-15 | 2 | 6 | 19 (length mismatch), 106 (printed 3 times), 215 (unpaired), 216 (printed 3 times), 216 (printed 3 times), 381 (length mismatch) |
| piece-06-06 | 3 | 6 | 32 (no tab), 272 (length mismatch), 276 (printed 3 times), 316 (length mismatch), 419 (line not found), 689 (no tab) |
| piece-07-07 | 4 | 6 | 272 (length mismatch), 273 (both tabs), 274 (length mismatch), 276 (printed 3 times), 278 (both tabs), 318 (length mismatch) |
| piece-05-05 | 4 | 6 | 40 (printed 3 times), 41 (length mismatch), 59 (length mismatch), 63 (printed 3 times), 69 (both tabs), 81 (length mismatch) |
| piece-18-08 | 5 | 6 | 61 (no tab), 97 (unpaired), 104 (printed 3 times), 115 (line not found), 136 (printed 3 times), 435 (length mismatch) |
| piece-24-05 | 0 | 6 | 061 (unpaired), 281 (both tabs), 282 (both tabs), 283 (length mismatch), 370 (length mismatch), 384 (unpaired) |
| piece-20-07 | 3 | 6 | 68 (length mismatch), 70 (printed 3 times), 77 (printed 3 times), 80 (length mismatch), 93 (length mismatch), 430 (printed 3 times) |
| piece-11-04 | 7 | 6 | 77 (printed 3 times), 745 (line not found), 768 (length mismatch), 769 (length mismatch), 770 (line not found), 778 (printed 3 times) |
| piece-21-03 | 4 | 6 | 078 (unpaired), 476 (length mismatch), 477 (length mismatch), 482 (length mismatch), 484 (printed 3 times), 490 (unpaired) |
| piece-20-03 | 5 | 6 | 82 (printed 3 times), 84 (printed 3 times), 116 (no tab), 119 (length mismatch), 126 (printed 3 times), 128 (printed 3 times) |
| piece-18-01 | 2 | 6 | 88 (printed 4 times), 346 (length mismatch), 397 (line not found), 738 (printed 3 times), 739 (both tabs), 854 (unpaired) |
| piece-24-11 | 1 | 6 | 98 (printed 3 times), 352 (printed 3 times), 352 (printed 3 times), 354 (length mismatch), 738 (printed 3 times), 853 (both tabs) |
| piece-20-02 | 4 | 6 | 118 (printed 3 times), 118 (printed 3 times), 118 (printed 3 times), 125 (unpaired), 126 (printed 3 times), 145 (both tabs) |
| piece-21-04 | 4 | 6 | 128 (printed 3 times), 476 (length mismatch), 481 (printed 4 times), 488 (printed 3 times), 489 (length mismatch), 494 (printed 3 times) |
| piece-16-10 | 1 | 6 | 141 (printed 3 times), 283 (length mismatch), 361 (both tabs), 385 (length mismatch), 497 (no tab), 648 (printed 4 times) |
| piece-04-03 | 6 | 6 | 403 (unpaired), 406 (printed 4 times), 406 (printed 4 times), 407 (printed 3 times), 408 (printed 3 times), 416 (no tab) |
| piece-14-07 | 5 | 6 | 208 (both tabs), 208 (both tabs), 260 (both tabs), 564 (no tab), 566 (length mismatch), 668 (no tab) |
| piece-23-05 | 5 | 6 | 200 (printed 3 times), 210 (no tab), 228 (unpaired), 237 (both tabs), 239 (both tabs), 284 (printed 3 times) |
| piece-04-05 | 4 | 6 | 395 (length mismatch), 398 (length mismatch), 414 (printed 3 times), 416 (no tab), 418 (printed 3 times), 896 (both tabs) |
| piece-12-07 | 1 | 6 | 206 (printed 3 times), 545 (line not found), 548 (line not found), 648 (printed 4 times), 695 (length mismatch), 840 (length mismatch) |
| piece-16-02 | 3 | 6 | 262 (printed 3 times), 364 (length mismatch), 376 (both tabs), 379 (line not found), 380 (both tabs), 385 (length mismatch) |
| piece-17-05 | 6 | 6 | 280 (length mismatch), 470 (length mismatch), 522 (printed 3 times), 558 (no tab), 613 (no tab), 624 (length mismatch) |
| piece-15-01 | 2 | 6 | 288 (printed 3 times), 683 (length mismatch), 836 (unpaired), 840 (length mismatch), 842 (unpaired), 887 (unpaired) |
| piece-08-05 | 3 | 6 | 303 (printed 3 times), 305 (both tabs), 312 (length mismatch), 314 (length mismatch), 325 (printed 3 times), 866 (length mismatch) |
| piece-08-01 | 5 | 6 | 325 (printed 3 times), 663 (no tab), 669 (both tabs), 688 (both tabs), 882 (length mismatch), 882 (length mismatch) |
| piece-13-02 | 4 | 6 | 464 (no tab), 758 (printed 3 times), 764 (printed 3 times), 784 (no tab), 787 (printed 3 times), 992 (unpaired) |
| piece-10-01 | 3 | 6 | 348 (no tab), 352 (printed 3 times), 570 (length mismatch), 706 (both tabs), 706 (both tabs), 880 (no tab) |
| piece-06-04 | 5 | 6 | 369 (both tabs), 380 (both tabs), 381 (length mismatch), 386 (length mismatch), 388 (length mismatch), 392 (length mismatch) |
| piece-19-08 | 5 | 6 | 438 (unpaired), 461 (printed 3 times), 477 (length mismatch), 493 (unpaired), 494 (printed 3 times), 496 (line not found) |
| piece-15-02 | 3 | 6 | 503 (unpaired), 504 (length mismatch), 511 (length mismatch), 596 (unpaired), 714 (line not found), 843 (unpaired) |
| piece-15-08 | 8 | 6 | 527 (length mismatch), 533 (unpaired), 536 (unpaired), 580 (both tabs), 632 (both tabs), 633 (printed 3 times) |
| piece-13-03 | 4 | 6 | 538 (length mismatch), 644 (length mismatch), 648 (printed 4 times), 687 (length mismatch), 695 (length mismatch), 786 (no tab) |
| piece-09-02 | 2 | 6 | 652 (unpaired), 656 (length mismatch), 658 (length mismatch), 676 (length mismatch), 677 (length mismatch), 689 (no tab) |
| piece-17-01 | 3 | 6 | 708 (line not found), 723 (unpaired), 726 (line not found), 727 (length mismatch), 729 (length mismatch), 734 (length mismatch) |
| piece-05-02 | 2 | 5 | 10 (line not found), 12 (printed 3 times), 18 (printed 3 times), 45 (length mismatch), 51 (both tabs) |
| piece-11-07 | 2 | 5 | 14 (printed 3 times), 752 (printed 3 times), 757 (length mismatch), 760 (printed 3 times), 761 (both tabs) |
| piece-17-09 | 2 | 5 | 15 (line not found), 415 (unpaired), 655 (unpaired), 729 (length mismatch), 734 (length mismatch) |
| piece-11-10 | 3 | 5 | 184 (length mismatch), 739 (both tabs), 758 (printed 3 times), 764 (printed 3 times), 780 (length mismatch) |
| piece-06-02 | 4 | 5 | 26 (printed 3 times), 27 (printed 3 times), 29 (unpaired), 30 (printed 3 times), 386 (length mismatch) |
| piece-24-04 | 3 | 5 | 54 (length mismatch), 99 (unpaired), 766 (unpaired), 787 (printed 3 times), 794 (unpaired) |
| piece-24-16 | 2 | 5 | 59 (length mismatch), 462 (length mismatch), 571 (printed 3 times), 571 (printed 3 times), 576 (line not found) |
| piece-22-06 | 5 | 5 | 60 (length mismatch), 565 (printed 3 times), 578 (printed 4 times), 589 (both tabs), 605 (no tab) |
| piece-08-03 | 3 | 5 | 064 (unpaired), 662 (both tabs), 666 (length mismatch), 868 (length mismatch), 883 (length mismatch) |
| piece-24-07 | 3 | 5 | 082 (unpaired), 422 (printed 3 times), 498 (no tab), 781 (length mismatch), 783 (unpaired) |
| piece-18-07 | 6 | 5 | 106 (printed 3 times), 108 (printed 3 times), 169 (length mismatch), 195 (length mismatch), 363 (unpaired) |
| piece-18-02 | 1 | 5 | 163 (both tabs), 182 (both tabs), 184 (length mismatch), 186 (both tabs), 187 (printed 3 times) |
| piece-14-09 | 5 | 5 | 141 (printed 3 times), 154 (both tabs), 159 (both tabs), 168 (printed 3 times), 190 (printed 3 times) |
| piece-14-02 | 2 | 5 | 281 (both tabs), 282 (both tabs), 287 (printed 3 times), 288 (printed 3 times), 293 (unpaired) |
| piece-11-06 | 3 | 5 | 147 (length mismatch), 757 (length mismatch), 760 (printed 3 times), 777 (line not found), 781 (length mismatch) |
| piece-04-01 | 2 | 5 | 400 (printed 3 times), 406 (printed 4 times), 407 (printed 3 times), 408 (printed 3 times), 409 (unpaired) |
| piece-24-08 | 1 | 5 | 179 (unpaired), 284 (printed 3 times), 284 (printed 3 times), 288 (printed 3 times), 371 (unpaired) |
| piece-04-06 | 3 | 5 | 570 (length mismatch), 577 (length mismatch), 578 (printed 4 times), 578 (printed 4 times), 646 (length mismatch) |
| piece-04-08 | 3 | 5 | 522 (printed 3 times), 573 (length mismatch), 578 (printed 4 times), 612 (no tab), 683 (length mismatch) |
| piece-12-10 | 3 | 5 | 558 (no tab), 572 (no tab), 646 (length mismatch), 844 (length mismatch), 848 (length mismatch) |
| piece-07-08 | 2 | 5 | 265 (length mismatch), 269 (both tabs), 297 (unpaired), 623 (printed 3 times), 626 (no tab) |
| piece-07-05 | 2 | 5 | 613 (no tab), 623 (printed 3 times), 625 (unpaired), 628 (printed 3 times), 824 (unpaired) |
| piece-09-04 | 4 | 5 | 296 (printed 4 times), 298 (length mismatch), 300 (length mismatch), 302 (unpaired), 323 (length mismatch) |
| piece-06-05 | 4 | 5 | 366 (length mismatch), 521 (no tab), 618 (length mismatch), 669 (both tabs), 847 (unpaired) |
| piece-19-01 | 3 | 5 | 396 (line not found), 397 (line not found), 399 (length mismatch), 400 (printed 3 times), 456 (printed 3 times) |
| piece-24-09 | 2 | 5 | 407 (printed 3 times), 486 (both tabs), 499 (unpaired), 600 (length mismatch), 750 (length mismatch) |
| piece-21-01 | 6 | 5 | 463 (unpaired), 473 (printed 3 times), 481 (printed 4 times), 484 (printed 3 times), 486 (both tabs) |
| piece-15-04 | 2 | 5 | 505 (unpaired), 507 (printed 3 times), 515 (unpaired), 544 (unpaired), 562 (no tab) |
| piece-15-07 | 5 | 5 | 507 (printed 3 times), 559 (length mismatch), 561 (both tabs), 565 (printed 3 times), 580 (both tabs) |
| piece-24-02 | 1 | 5 | 530 (length mismatch), 623 (printed 3 times), 628 (printed 3 times), 628 (printed 3 times), 731 (no tab) |
| piece-22-03 | 5 | 5 | 588 (length mismatch), 604 (unpaired), 608 (length mismatch), 806 (length mismatch), 808 (length mismatch) |
| piece-12-11 | 1 | 5 | 605 (no tab), 648 (printed 4 times), 649 (length mismatch), 848 (length mismatch), 873 (unpaired) |
| piece-24-06 | 1 | 5 | 631 (unpaired), 632 (both tabs), 682 (length mismatch), 718 (length mismatch), 727 (length mismatch) |
| piece-09-06 | 3 | 5 | 651 (length mismatch), 668 (no tab), 678 (unpaired), 680 (both tabs), 681 (unpaired) |
| piece-11-09 | 3 | 4 | 12 (printed 3 times), 43 (unpaired), 168 (printed 3 times), 224 (length mismatch) |
| piece-24-03 | 3 | 4 | 13 (length mismatch), 748 (printed 3 times), 750 (length mismatch), 789 (unpaired) |
| piece-16-01 | 1 | 4 | 15 (line not found), 159 (both tabs), 183 (no tab), 365 (unpaired) |
| piece-06-01 | 5 | 4 | 20 (printed 3 times), 28 (length mismatch), 355 (unpaired), 391 (unpaired) |
| piece-05-04 | 5 | 4 | 46 (printed 3 times), 53 (both tabs), 54 (length mismatch), 60 (length mismatch) |
| piece-12-09 | 3 | 4 | 28 (length mismatch), 260 (both tabs), 262 (printed 3 times), 677 (length mismatch) |
| piece-23-01 | 7 | 4 | 30 (printed 3 times), 231 (unpaired), 236 (length mismatch), 248 (no tab) |
| piece-10-07 | 3 | 4 | 046 (unpaired), 89 (no tab), 216 (printed 3 times), 859 (no tab) |
| piece-11-11 | 2 | 4 | 57 (length mismatch), 760 (printed 3 times), 761 (both tabs), 762 (unpaired) |
| piece-24-14 | 3 | 4 | 69 (both tabs), 88 (printed 4 times), 88 (printed 4 times), 104 (printed 3 times) |
| piece-10-03 | 5 | 4 | 360 (printed 3 times), 361 (both tabs), 362 (unpaired), 868 (length mismatch) |
| piece-20-04 | 6 | 4 | 128 (printed 3 times), 129 (unpaired), 469 (length mismatch), 487 (length mismatch) |
| piece-14-04 | 3 | 4 | 137 (length mismatch), 141 (printed 3 times), 158 (no tab), 200 (printed 3 times) |
| piece-14-08 | 6 | 4 | 178 (printed 4 times), 200 (printed 3 times), 209 (unpaired), 291 (unpaired) |
| piece-12-03 | 5 | 4 | 154 (both tabs), 406 (printed 4 times), 408 (printed 3 times), 746 (unpaired) |
| piece-16-08 | 3 | 4 | 162 (printed 3 times), 167 (both tabs), 186 (both tabs), 758 (printed 3 times) |
| piece-12-02 | 5 | 4 | 206 (printed 3 times), 258 (unpaired), 497 (no tab), 498 (no tab) |
| piece-04-04 | 5 | 4 | 262 (printed 3 times), 411 (printed 3 times), 412 (printed 3 times), 412 (printed 3 times) |
| piece-07-06 | 5 | 4 | 265 (length mismatch), 287 (printed 3 times), 296 (printed 4 times), 827 (unpaired) |
| piece-07-10 | 2 | 4 | 274 (length mismatch), 295 (length mismatch), 295 (length mismatch), 657 (no tab) |
| piece-24-01 | 2 | 4 | 276 (printed 3 times), 277 (length mismatch), 278 (both tabs), 280 (length mismatch) |
| piece-16-07 | 2 | 4 | 277 (length mismatch), 372 (length mismatch), 376 (both tabs), 736 (no tab) |
| piece-09-05 | 4 | 4 | 296 (printed 4 times), 296 (printed 4 times), 300 (length mismatch), 323 (length mismatch) |
| piece-10-05 | 4 | 4 | 299 (unpaired), 328 (length mismatch), 338 (length mismatch), 752 (printed 3 times) |
| piece-08-04 | 7 | 4 | 318 (length mismatch), 328 (length mismatch), 338 (length mismatch), 889 (length mismatch) |
| piece-09-07 | 4 | 4 | 312 (length mismatch), 314 (length mismatch), 325 (printed 3 times), 327 (unpaired) |
| piece-24-13 | 3 | 4 | 446 (printed 3 times), 448 (printed 3 times), 448 (printed 3 times), 459 (unpaired) |
| piece-21-02 | 9 | 4 | 430 (printed 3 times), 445 (both tabs), 466 (length mismatch), 483 (printed 4 times) |
| piece-19-03 | 4 | 4 | 539 (unpaired), 551 (no tab), 643 (both tabs), 644 (length mismatch) |
| piece-19-02 | 2 | 4 | 507 (printed 3 times), 538 (length mismatch), 844 (length mismatch), 886 (both tabs) |
| piece-15-03 | 3 | 4 | 551 (no tab), 637 (unpaired), 642 (unpaired), 643 (both tabs) |
| piece-17-10 | 8 | 4 | 513 (length mismatch), 537 (no tab), 561 (both tabs), 565 (printed 3 times) |
| piece-07-02 | 2 | 4 | 619 (length mismatch), 624 (length mismatch), 685 (length mismatch), 813 (unpaired) |
| piece-07-03 | 5 | 4 | 651 (length mismatch), 662 (both tabs), 853 (both tabs), 865 (both tabs) |
| piece-10-04 | 3 | 4 | 688 (both tabs), 703 (no tab), 818 (both tabs), 889 (length mismatch) |
| piece-11-01 | 3 | 3 | 000 (unpaired), 26 (printed 3 times), 33 (length mismatch) |
| piece-11-08 | 4 | 3 | 18 (printed 3 times), 19 (length mismatch), 20 (printed 3 times) |
| piece-23-02 | 4 | 3 | 27 (printed 3 times), 226 (printed 3 times), 250 (unpaired) |
| piece-10-06 | 4 | 3 | 34 (line not found), 446 (printed 3 times), 716 (length mismatch) |
| piece-21-06 | 9 | 3 | 45 (length mismatch), 78 (printed 3 times), 446 (printed 3 times) |
| piece-20-08 | 3 | 3 | 53 (both tabs), 67 (printed 3 times), 88 (printed 4 times) |
| piece-05-06 | 5 | 3 | 79 (length mismatch), 224 (length mismatch), 234 (no tab) |
| piece-15-05 | 2 | 3 | 109 (both tabs), 502 (both tabs), 805 (unpaired) |
| piece-14-01 | 6 | 3 | 145 (both tabs), 147 (length mismatch), 298 (length mismatch) |
| piece-23-04 | 7 | 3 | 246 (unpaired), 251 (unpaired), 346 (length mismatch) |
| piece-10-02 | 4 | 3 | 341 (line not found), 360 (printed 3 times), 697 (unpaired) |
| piece-16-06 | 1 | 3 | 341 (line not found), 735 (line not found), 738 (printed 3 times) |
| piece-17-07 | 3 | 3 | 629 (length mismatch), 730 (unpaired), 944 (line not found) |
| piece-21-07 | 6 | 3 | 420 (printed 3 times), 435 (length mismatch), 452 (unpaired) |
| piece-21-05 | 2 | 3 | 422 (printed 3 times), 481 (printed 4 times), 488 (printed 3 times) |
| piece-15-10 | 8 | 3 | 527 (length mismatch), 537 (no tab), 559 (length mismatch) |
| piece-17-08 | 4 | 3 | 521 (no tab), 656 (length mismatch), 999 (both tabs) |
| piece-07-04 | 3 | 3 | 660 (no tab), 663 (no tab), 818 (both tabs) |
| piece-17-06 | 1 | 3 | 735 (line not found), 944 (line not found), 959 (unpaired) |
| piece-07-09 | 4 | 2 | 275 (unpaired), 802 (no tab) |
| piece-14-05 | 3 | 2 | 18 (printed 3 times), 137 (length mismatch) |
| piece-12-01 | 4 | 2 | 308 (length mismatch), 390 (no tab) |
| piece-17-02 | 3 | 2 | 512 (both tabs), 513 (length mismatch) |
| piece-23-06 | 8 | 2 | 226 (printed 3 times), 248 (no tab) |
| piece-08-06 | 6 | 2 | 303 (printed 3 times), 305 (both tabs) |
| piece-15-09 | 8 | 2 | 616 (length mismatch), 859 (no tab) |
| piece-24-10 | 4 | 2 | 633 (printed 3 times), 636 (length mismatch) |
| piece-05-08 | 7 | 1 | 20 (printed 3 times) |
| piece-20-05 | 4 | 1 | 116 (no tab) |
| piece-12-08 | 6 | 1 | 308 (length mismatch) |
| piece-13-04 | 4 | 1 | 687 (length mismatch) |
| piece-21-08 | 5 | 1 | 467 (unpaired) |

Full table: `bowser-edges.csv`.
