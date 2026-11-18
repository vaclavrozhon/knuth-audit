# F268 — One extra changed level in the clause-signature argument

**Location:** Volume 4B, first edition, second printing (2022), p. 257,
the paragraph immediately after the worked signature of clause (122)
(PDF page 277). The same wording is in the September 2015 Fascicle 6A
draft, p. 73 (PDF page 81).

A **literal** is a Boolean variable or its negation. A **trail** records
assigned literals, grouped into decision levels. The book defines a clause's
signature `(p,q)` by counting its levels: `p` contain a true literal of the
clause, and the other `q` contain only false literals of that clause.

The paragraph compares clauses `C,C'` with signatures `(p,q),(p',q')`,
assuming `p+q=p'+q'` and `p<p'`. It claims that `C'` cannot force a literal
until signs have changed on at least `p+1` different levels. The bound is
too large by one in the tight case `p'=p+1`.

## Three-variable counterexample

Let `x,y,z` be Boolean variables and take

```
C  = x OR NOT y
C' = y OR z.
```

Initially assign `x=true`, `y=true`, and `z=true` on levels 1, 2, 3,
respectively. These are valid decisions for the two clauses, and neither
clause is a reason for an assignment. Their signatures are

```
(p,q)   = (1,1)   for C,
(p',q') = (2,0)   for C'.
```

Thus both signatures have total 2 and `p<p'`, as required. Backtrack to
level 1 and assign `y=false` on level 2. Clause `C` remains satisfied by
`x`, while `C'` now has the single unassigned literal `z` and forces
`z=true`. Only `y` changed sign relative to the initial trail. Its old
level is 2, so just **one** old level has a sign change, whereas the printed
bound demands `p+1=2`. Reassigning `z` to its former value is not a sign
change. Whether a clause was original or previously learned has no effect
on this unit-propagation calculation.

## Correction and scope

The general necessary bound is **`p'-1` old levels**. When `C'` becomes
unit, every literal except the one about to be forced is false. Therefore
each old positive level, except possibly the level of that one literal,
must contain a literal whose sign changed. The example attains this bound.
Since `p<p'`, this also implies at least `p` changed levels. Replacing
`p+1` by `p` in the printed comparison is sufficient; stating `p'-1`
gives the more precise bound.

This is a local error in the explanation of clause selection. The corrected
bound still supports the qualitative preference for fewer positive levels.
It does not refute the heuristic, its empirical table, or Algorithm C.

## Source and novelty check

The original p. 257 image was inspected, including the prime on `C'` and the
plus in `p+1`. The draft has the same expression. The six archived current
and historical errata lists and three author TeX errata files have no matching
correction. Focused public searches found no matching prior report; absolute
priority is not established. The author's archived SAT13 source describes
the same signature and heuristic but does not repeat this numerical claim.

Hashes, page mappings, inspected errata blocks and search queries are in
`results/focused-signature257-sources.json`. This check uses the explicit
trail calculation above; no solver, benchmark or exhaustive search was run.
