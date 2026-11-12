# V4A-F0040: The profile inequalities are not sufficient

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), exercise 7.1.4-146(b), printed page 268 / file 285, and its
answer on page 647 / file 664. Originals are saved for both pages.

Write b_k for the number of BDD nodes on level k and q_k for the
number on level k after redundant variable tests are retained in
the corresponding quasireduced diagram. Part (b) claims that the
inequalities in part (a) suffice for realizing b0,b1,q0,q2.

Take (b0,b1,q0,q2)=(1,2,1,5). All three printed inequalities hold:

    1 <= min(1,(2+5)*(2+5-1)),
    2 <= min(1+1,5*(5-1)),
    1+2 >= 1-5.

But q0=1 gives a single QDD root. After two binary decisions it can
reach at most four distinct nodes, contradicting q2=5. All four
parameters in this counterexample are positive.

The answer constructs arbitrary level-2 subfunctions and does not
ensure that all of them are reachable from its proposed roots.
At least the necessary upper bound q2 <= q0+b0+b1 is missing:
q1 <= q0+b0 and q2 <= q1+b1. This finding does not claim that adding
this one inequality alone provides a complete corrected converse.

No matching erratum or public report was located in the screened
sources; see `sources/bdd-order-source-check.json`. Absolute novelty
is not established. No computation was needed.
