# V4A-F0045: The multiplication profile bound counts only one sink

Confirmed, low severity. Volume4A, first edition, first printing
(2011), answer7.1.4-177, printed pages656–657 / files673–674.
Originals: `images/bookwise-p656.png` and `images/bookwise-p657.png`.

The quasi-profile q_k counts every QDD node on level k, including
both sinks on the final level. The function Z_n, the middle bit of
the product of two variable n-bit numbers, is nonconstant: the
products 0*1 and 2^(n-1)*1 give different outputs. Hence q_(2n)=2.

Answer177 sums a tail bound 2^(3n-2*floor(k/2)-ceil(k/2)) all the
way through k=2n. At that endpoint it gives 1 instead of 2. The
low-part memory argument in TheoremA is for branching levels; at
the terminal level it cannot discard the already computed output.

Add one to the summed bound. Consequently its evaluation on page657
becomes

    (2^ceil(6n/5) * c_(n mod 5) - 5) / 7,
    (c0,c1,c2,c3,c4) = (19,10,12,13,17),

instead of the expression with -12. The advertised upper bound
Q(f) <= (19/7)*2^ceil(6n/5) in TheoremA still follows. This is an
error in the intermediate profile bound, not in that final theorem.

No matching correction or report was located in the current and
historical Volume4A/Fascicle1 errata or public searches. See
`sources/bdd-multiplication-source-check.json`. Absolute novelty is
not established. No computation was needed.
