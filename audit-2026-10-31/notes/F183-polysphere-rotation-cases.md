# F183 — incorrect rotation cases in answer 354(f)

Volume 4B, first edition, second printing (November 2022), §7.2.2.1,
answer 354(f), printed page 515 / file page 535. The error is in the
case analysis of a proof; it does not refute the proposed generators.

Let e_i be the i-th coordinate vector in four dimensions and write
e_ij = e_i − e_j, as in the answer. Let T, R and H denote the matrices
printed just above the proof. Matrix products act on column vectors.
The proof has already normalized the rotation Q so that Q e_12 = e_12.

The two cases (i,j,i',j') = (1,3,3,2) and (1,4,4,2) are called impossible.
Both are realized by Q = TR:

```
TR e_12 = e_12,
TR e_13 = e_32,
TR e_14 = e_42.
```

For example, V = {0,e_12,e_13} is a connected, noncollinear polysphere,
and TR maps it to {0,e_12,e_32}. This satisfies all the stated hypotheses.
T and R are proper rotations, so their product is one as well.

The same paragraph gives T²RT as an alternative for both (1,3,4,2)
and (1,4,3,2). But T²RT e_12 = e_34, which violates the normalization.
Delete those two alternatives. The other printed products in these
cases, THR³T² and HR, respectively, do have the required images.
Replace the two allegedly impossible cases by Q = TR. The cases
(1,3,1,4) and (1,4,1,3), represented by TH and HT², are correct.

The small exact calculation in `check_bookwise_polysphere_cases.py`
records all these images in `results/bookwise-polysphere-cases.json`.
It also checks orthogonality, determinant 1 and preservation of the
coordinate sum for T, R and H. No classification census is involved.

The actual typesetting was inspected in `images/bookwise-p515.png`
and `images/bookwise-p515-rotations.png`. The author's September 2019
[pre-fascicle](https://www.ioccc.org/2019/ciura/fasc5c.pdf), answer 354(f)
on printed page 219, contains the same case analysis.
The current and historical Volume 4B/Fascicle 5 errata, freshly retrieved
on 11 November 2026, contain no matching correction. Public searches
found no matching report; this is not a claim of absolute priority.
See `sources/bookwise-polysphere-source-check.json` for the scope.
