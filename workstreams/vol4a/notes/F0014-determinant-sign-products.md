# V4A-F0014: two determinant products have the wrong signs

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), answer 7.1.2-70(c), printed page 575 / file page 592.
Original: `images/bookwise-p575.png`; question: `images/file147.png`.

The exercise asks for the indicator [det X > 0], where X is the 3 by 3
matrix with rows (x1,x2,x3), (x4,x5,x6), (x7,x8,x9). The answer sets
y2=x1*x6*x8 and y5=x3*x4*x8, then compares y1+y2+y3 with y4+y5+y6.
But y2 is a negative term of the determinant and y5 is a positive term.

For the matrix

    1 0 0
    0 0 1
    0 1 0

the determinant is -1. The printed products are (0,1,0,0,0,0), so the
printed comparison is true. The final 11-step comparator also returns
1: its intermediate values are (z1,z2,z3,z4)=(1,1,0,0).

Interchange the definitions of y2 and y5. Then the first three products
are precisely the positive determinant terms and the last three are
the negative terms. This also restores the stated equivalence between
all three positive terms being 1 and all three negative terms being 1:
either event requires all nine entries of X to be 1. The stated cost
23 remains available with this repair.

The current and historical Volume 4A errata and both Fascicle 0 layers
were screened, including corrections to answer 70 and nearby answer
pages. No matching correction was located. Targeted public searches
found no matching report; absolute novelty is not established. See
`sources/determinant-tictactoe-source-check.json`. The counterexample
and the comparator values were checked by hand; no computation was run.
