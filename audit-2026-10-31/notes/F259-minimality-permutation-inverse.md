# F259: The minimality witness uses a permutation instead of its inverse

**Location:** TAOCP Volume 4B, first edition, second printing (November
2022), answer 7.2.2.2–230, printed page 592, file page 612. The same
construction occurs in the September 23, 2015 Pre-Fascicle 6A, printed
page 228, file page 236. Both original page images were inspected.

The answer proves that a collection of clauses is minimally
unsatisfiable: deleting any one clause should leave a satisfiable
collection. Its final witness, for deletion of a successor clause,
uses the wrong permutation direction. This is a defect in the witness,
not a counterexample to minimal unsatisfiability.

## A three-element counterexample

The Boolean variable `x_ij` says that element `i` precedes element `j`.
The clauses include `I_j = (not x_jj)`, expressing irreflexivity;
`T_ijk = (not x_ij or not x_jk or x_ik)`, expressing transitivity for
the indicated triples; and

```text
M_jm = (x_j1 or x_j2 or ... or x_jm),
```

which says that element `j` has a successor among the `m` elements.
After deleting `M_(j0,m)`, the answer sets `x_ij = [p_i < p_j]`, where
brackets denote the Boolean value of the enclosed comparison, and lists
the permutation

```text
p_1 ... p_m = 1 ... (j0-1) (j0+1) ... m j0.
```

Take `m = 3` and `j0 = 1`. The printed permutation is `(2,3,1)`, so
the proposed Boolean matrix, with rows indexed by `i` and columns by `j`, is

```text
       j=1  j=2  j=3
i=1     0    1    0
i=2     0    0    0
i=3     1    1    0
```

It satisfies every irreflexivity and transitivity clause, since it is a
strict total order. But `M_23 = (x_21 or x_22 or x_23)` is false. This
clause has not been deleted: only `M_13` was removed. Thus the proposed
witness does not satisfy the remaining clauses.

## Correction

For the displayed permutation, set `x_(p_i,p_j) = [i < j]` instead.
Equivalently, retain `x_ij = [p_i < p_j]` but use the rank permutation

```text
p_i = i       if i < j0,
p_i = m       if i = j0,
p_i = i - 1   if i > j0.
```

Now element `j0` has the largest rank. It is the unique element without
a successor, and all irreflexivity and transitivity clauses hold. In the
example the corrected ranks are `(3,1,2)`, not `(2,3,1)`.

## Sources and status

- [Original page 592](../../integration/2026-11-17-focused-4b/sources/vol4b-p592.png)
- [Author draft page 228](../../integration/2026-11-17-focused-4b/sources/fasc6a-answer230.png)
- [Current source retrieval](../../integration/2026-11-17-focused-4b/sources/retrieval.json)
- [Focused source check](../results/focused-minimality230-sources.json)

The current short and complete Volume 4B and Fascicle 6 errata, including
their TeX sources, were refreshed on November 17, 2026. No corresponding
correction was located. The Fascicle 6 correction on page 228 concerns
the final resolution step in answer 231, not this witness in answer 230.
Focused public searches found no matching report; absolute priority is
not established. A physical copy and every later printing have not been
inspected. Nothing has been sent.
