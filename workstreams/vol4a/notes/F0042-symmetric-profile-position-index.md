# V4A-F0042: The profile formula uses a variable label as its position

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), answer 7.1.4-158, printed page 650 / file 667.
Original: `images/bookwise-p650.png`.

For m=1 and n=3t-1, the answer puts the exceptional variable xn at
position k=n*pi. It then gives the number of nodes testing variable j
as a_j, b_j or a_(n+2-j), according as j*pi is less than, equal to or
greater than k. The profile indices must use the position j*pi too.
Equivalently, when j denotes a position, the comparisons must be
j<k, j=k and j>k, and the stated a_j,b_j,a_(n+2-j) may be retained.

For a concrete check, let n=5, t=2, g(x5)=x5, and test the variables
in the order x1,x2,x5,x3,x4. The covering-by-population function here
is [x1+x2+x3+x4=1] OR (x5 AND [x1+x2+x3+x4=3]). After the first two
tests, precisely two distinct residual functions depend on x5:

    [x3+x4=0] OR (x5 AND [x3+x4=2]),
    x5 AND [x3+x4=1].

Thus there are two nodes testing x5, namely b_k=b_3=2. With j=5 the
printed rule instead gives b_5=min(5,2,1)=1. This is a local indexing
error; the subsequent size comparisons use positions and are not
refuted by this example.

No matching erratum or public report was located in the screened
sources; see `sources/bdd-order-source-check.json`. Absolute novelty
is not established. No computation was needed.
