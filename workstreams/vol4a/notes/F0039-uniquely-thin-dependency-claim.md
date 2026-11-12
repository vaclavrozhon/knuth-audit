# V4A-F0039: A dependency claim in the uniquely thin proof is false

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), answer 7.1.4-135, printed page 643 / file 660.
Original: `images/bookwise-p643.png`.

The answer defines theta_0=1, theta_1=x1, theta_2=x1 AND x2, and
theta_n = (xn ? theta_(n-1) : theta_(n-3)). Here the conditional
uses its first alternative when xn=1. It asserts that for n>=5
and k<n, both functions obtained by fixing xk depend on every other
variable, with only one stated exception at k=n-1.

For n=5 and k=1, however,

    theta_2 | x1=0 = 0,
    theta_3 | x1=0 = NOT x3,
    theta_4 | x1=0 = x4 AND NOT x3,
    theta_5 | x1=0 = x5 AND x4 AND NOT x3.

The last function does not depend on x2. This case is outside the
printed exception. Consequently the edge from {1} to {1,2} in the
master profile chart has weight one, not the claimed two: the other
cofactor is x2 OR (x5 AND (NOT x4 OR NOT x3)), which does depend on x2.

This refutes the auxiliary dependency and edge-weight assertions,
not the existence of a uniquely thin function. The proof needs to
handle this additional case; no general replacement proof is claimed.

No matching erratum or public report was located in the screened
sources; see `sources/bdd-order-source-check.json`. Absolute novelty
is not established. No computation was needed.
