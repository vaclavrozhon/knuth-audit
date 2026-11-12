# V4A-F0041: The paired matrix weight is missing a factor m

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), answer 7.1.4-142(b), printed page 647 / file 664.
Originals: `images/bookwise-p646.png` and `images/bookwise-p647.png`.

The construction uses a 2m by 2m matrix with weights

    w_ij = 2^i + m*2^(2m+1+j),  0 <= i,j < 2m.

Its paired complementary assignments give exactly m ones in each
row and exactly m ones in each column. Therefore their total weight is

    m * (2^(2m)-1) * (1 + m*2^(2m+1)).

The displayed equality on page 647 omits the first factor m. For
example m=2 gives 1950, whereas the printed expression gives 975.
The corrected value is half the sum of all matrix weights, as the
subsequent threshold argument needs. The additional variable x0 of
weight one is fixed to zero and does not change this calculation.

This is a local arithmetic error in the proof; the construction and
lower-bound argument retain their intended threshold after correction.
The historical correction to the index sets on the same page does
not correct this missing factor.

No matching erratum or public report was located in the screened
sources; see `sources/bdd-order-source-check.json`. Absolute novelty
is not established. No computation was needed.
