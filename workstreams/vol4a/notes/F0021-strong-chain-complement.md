# V4A-F0021: the strong-chain construction omits complemented Boolean operations

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), answer 7.1.3-113, printed page 600 / file page 617.
Original: `images/bookwise-p600.png`; definition and question:
`images/bookwise-p193.png`.

A strong n-bit chain must give the same intermediate numbers when
its operations are interpreted as operations on 2-adic integers,
without n-bit truncation. The answer copies an operation unchanged
whenever it is not addition, subtraction, or left shift.

This omits the allowed Boolean operations whose output on (0,0)
is 1, such as NOR, NAND, and equivalence (XNOR). For example, take
n = 2 and the one-step chain

    x_1 = NOR(x_0,x_0) mod 4.

At x_0 = 0 its n-bit result is 3. The printed construction copies
NOR unchanged and gives the 2-adic value NOR(0,0) = -1. Thus its
asserted equality x'_1 = x_1 fails, and the constructed chain is
not strong.

This is a defect in the construction, not a counterexample to the
exercise's O(r) existence claim. One can replace NOR by

    u = a | b,
    v = u XOR (2^n - 1),

where both intermediate values stay in the n-bit range. The same
method works for each omitted operator: first compute its Boolean
complement, which maps (0,0) to 0, then XOR with the n-bit all-ones
mask. Merely applying an AND mask after the original NOR would
not suffice for a strong chain, because the intervening -1 would
still be outside the n-bit range.

The subtraction branch has the same issue internally: it forms
the equivalence `a' XNOR b'` before ANDing with h. At a' = b' = 0
that intermediate is -1. Compute `a' XOR b'` followed by
`h & ~(a' XOR b')` instead, using the allowed AND-NOT operation;
both values remain bounded and this pair still costs two steps.

The historical and current Volume 4A and Fascicle 1 errata contain
no matching correction. Fresh official files match the archived
copies. Public searches found no matching report; absolute novelty
is not established. See `sources/strong-chain-source-check.json`.
The counterexample uses only the definitions; no enumeration was run.
