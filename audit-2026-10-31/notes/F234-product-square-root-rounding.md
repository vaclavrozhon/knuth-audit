# F234 — The product bound omits its central threshold

Confirmed in Volume 4B, answer 406(a), printed 630/file 650.
Write x^j=[x>=j] and y^j=[y>=j] for order bits. The first conjunction's
upper endpoint must be ceil(sqrt(a+1)), not floor(sqrt(a+1)).

Take d=5, a=7, and x=y=3. Both printed conjunctions have the nonempty
index range consisting of j=2. Their two clauses are

    (not x^2 or not y^4) and (not x^4 or not y^2).

Both are true, although xy=9 exceeds 7. Changing the first upper endpoint
to 3 adds (not x^3 or not y^3), which rejects this assignment.

For the general repair, put q=a+1 and r=ceil(sqrt(q)). A pair with xy>=q
is excluded by the clause at x's threshold if x<=r, or by the transposed
clause at y's threshold if y<r. If both x and y are at least r, the clause
at j=r excludes it since ceil(q/r)<=r. Thresholds below
ceil(q/(d−1)) cannot witness a violation within the domain. This accounts
for the asymmetry: the first conjunction includes r and the second stops
at r−1. The printed formula already works at perfect-square q.

The fixed witness and its corrected clauses are in
results/bookwise-order-fixed-witnesses.json. Draft page 266 has the same
floor sign. The known 2022 replacement of answer 404 is unrelated.

The original Volume 4B typesetting and the corresponding September 23, 2015
author draft were inspected. Relevant current and historical Volume 4B and
Fascicle 6 errata, including their available TeX sources, have no matching
correction. This is not a claim about absolute priority or a physical copy.
Source details are in sources/bookwise-order-arithmetic-source-check.json.
