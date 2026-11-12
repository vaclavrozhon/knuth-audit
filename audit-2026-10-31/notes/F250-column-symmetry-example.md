# F250 — The second column ends in 32, not 13

Confirmed in Volume 4B, answer 495, printed 648/file 668; author draft 284.
Two-digit names ij denote the matrix variable x_ij. For the swap of columns
2 and 3, the example prints

    12 22 13 <= 13 23 33.

It should read

    12 22 32 <= 13 23 33.

The immediately following involution (12 13)(22 23)(32 33) is correct.
For a concrete illustration, the binary matrix

    0 1 1 1
    0 1 1 1
    1 0 0 1

has nondecreasing rows and columns, and swapping columns 2 and 3 leaves it
fixed. Nevertheless the printed comparison is 111 <= 110, which is false;
the corrected comparison is 110 <= 110. The general double-lex argument
is unchanged. The known February 2024 erratum on the same answer changes
the concluding attribution and does not repair this earlier index.

The original Volume 4B typesetting and the September 23, 2015 author draft
were inspected. Relevant current/historical 4B and Fascicle 6 errata,
including available TeX sources, contain no matching correction. Focused
public searches found no matching report, without establishing absolute
priority. See sources/bookwise-quenching-symmetry-source-check.json.
