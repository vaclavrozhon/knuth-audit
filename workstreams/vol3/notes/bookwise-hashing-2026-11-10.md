# Bookwise review: hashing, 10 November 2026

Reviewed §6.4, printed pp.513–558, exercises 1–77 and added exercise
78, with answers on pp.728–743 and the later additions. Shared answer
p.743 is deferred to §6.5 for page coverage.

Checked the hash transformations, BCH argument, corrected three-gap
description, coalesced chains, linear and double probing, Brent's
relocation, deletion, abbreviated keys, and the linked-memory overlay.
Checked the printed MIX paths and cost totals, the deletion invariant,
the distinction between occupied and deleted cells, and the circular
interval test. Applied the known repairs to Algorithm R and overlay
step A7. The three-gap ratio argument survives the new normalizer
finding. No separate finding is made from its initial-interval convention.

Checked the uniform-probing calculation, parking counts and Abel sums,
the Q-function bounds, carry recurrence, the stated independence failure
in the Schay–Spruth model, the moment relations, and Theorem U's induction
with its known binomial-index correction. Read the three parking/tree
correspondences with their inverses. Checked the chain-length recurrences,
the secondary-clustering recurrence and its asymptotic substitution,
the special probe-order counting argument, Poisson bucket sums, the
R-function conversion, and the displayed Lagrange/root-filter steps.
The variance bound in answer 36 is read in the section's usual load
range 0<=alpha<=1, not extended to arbitrarily overloaded chains.

Checked universal-family and collision arguments, the counterexample
for a fixed bucket's expected size, three-way independence and the
four-key counterexample, variable-length extensions, and the iterated
hash bound. The added multiply-and-shift exercise 78 was read with its
full proof on errata PDF pp.38–39: translation invariance of the collision
count, the truncated triangular expression, and the odd-multiplier sum.
The M=5 uniform-probing example was checked by its prefix-set orbits;
the M=6 and M=7 displayed weights normalize correctly.

New C0074–C0078 concern the three-gap normalizer, a shifted carry formula
in the errata, ordered-search indices, the MIX comparison coefficient,
and the conversion between the two R functions. Only C0075 is an
errata-only finding. Known corrections, including the 2026 missing
constant in answer 43 and the 2005 variance correction, are excluded.
See `sources/hashing-errata-review.json` for the source screen.

Limits: historical performance tables and experimental exercises 19
and 71 were not recreated. The cited higher-dimensional gap theorem,
coalesced-table deletion scheme, auxiliary-overflow analysis, tertiary
clustering theorem, exact bucket analysis, ordered-hashing theorem,
Robin Hood/total-displacement moment results, and refined double-hashing
probability estimates were accepted as external results. Their printed
formulas and local consistency were read; the cited papers' proofs were
not reproduced. Exercises 57 and 60–62 remain research-level questions;
no new solution or minimum-size permutation census was attempted.
The long algebra suppressed by 'after some maneuvering' in answer 44
and 'some more juggling' in answer 55 was not independently reconstructed
in full; the displayed setup, transformations and limiting relationships
were checked. No large hash simulation or new general verifier was run.

Next: §6.5, printed p.559 / file p.570.
