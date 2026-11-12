# F235 — The strict comparator clause count ends in −1

Confirmed in Volume 4B, answer 414, printed 633/file 653.
The parenthetical clause count for strict lexicographic comparison is
printed as 2^n+2^(n−1)+1. It should be 2^n+2^(n−1)−1.

For n=2, the strict version of (169), after eliminating its one auxiliary
variable, has exactly these five clauses:

    (not x1 or y1)
    (not x1 or not x2)    (not x1 or y2)
    (y1 or not x2)        (y1 or y2).

The printed expression gives seven. In general let T_n be the count after
eliminating auxiliaries from the last toward the first, as directed.
The one-bit strict comparison has T_1=2. Each preceding stage duplicates
the suffix clauses with the two distinct prefix literals and adds one
new non-strict bit clause, so T_n=2*T_(n−1)+1. Thus
T_n=3*2^(n−1)−1. The non-strict count 2^n−1 is unchanged.

The fixed resolution check is in results/bookwise-order-fixed-witnesses.json.
The author draft page 268 numbers this answer 413 and has the same +1.
The known 2025 correction to answer 415 concerns a different formula.

The original Volume 4B typesetting and the corresponding September 23, 2015
author draft were inspected. Relevant current and historical Volume 4B and
Fascicle 6 errata, including their available TeX sources, have no matching
correction. This is not a claim about absolute priority or a physical copy.
Source details are in sources/bookwise-order-arithmetic-source-check.json.
