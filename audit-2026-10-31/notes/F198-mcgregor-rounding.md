# F198 — the McGregor coloring bound needs rounding

Volume 4B, exercise 7.2.2.2–18, printed page 318 / file page 338.

The requested bound is that some color occurs at most 5n/6 times.
For n=8 this allows at most six occurrences, but seven are necessary.
The table in answer 17 already states f(8)=7, and the explicit
construction in answer 18 has color-class sizes (20,23,22,7).

This was independently checked for this one disputed order. The graph
defined in answer 15 has 72 vertices and 210 edges. Its edge definition
was compared with Knuth's published mcgregor-graph.w. The answer 18
coloring satisfies every edge and has the stated distribution.
A four-color SAT encoding with a cardinality bound of six on color 1
is unsatisfiable. No color symmetry was fixed, so any putative small
color class could be renamed color 1. The emitted proof was checked
by the separate drat-trim program: VERIFIED.

A compatible correction is `ceil(5n/6)`. In the displayed construction,
the only residue class exceeding 5n/6 is n=6k+2, for which the fourth
color is used 5k+2 times, exceeding 5n/6 by 1/3. The construction's
claimed general optimality remains a conjecture; this check does not
address it.

The error belongs to the question's bound, not to the table or color
distribution in the answers. Original page 318 was inspected; the
September 2015 draft page 134 has the same unrounded bound. Fresh
4B/Fascicle 6 errata and targeted public searches yielded no matching
correction. No absolute priority claim.

Evidence: `check_bookwise_mcgregor18.py`, the CNF, DRAT proof, witness
distribution and independent check log in `results/bookwise-mcgregor18/`.
Only n=8 with the bound six was solved; no general census was run.
