# Minimum-comparison merging — 10 November 2026

Reviewed §5.3.2, printed pp.197–207, all 25 exercises and their answers
on pp.658–660. File pages are printed pages plus 11. No new finding.
Shared pp.207 and 660 continue into selection and are deferred for
whole-page certification.

The alternating-order adversary for Theorem M, its unequal-length
companion, and all six constrained splitting strategies were checked
against the original inequalities and boundary-constraint table.
The strict inequalities in strategies B and C ensure that the initial
comparison is outside the two subsequent subproblems; the repeated
pivot in those subproblems does not transfer useful information.
The minimum over first questions and maximum over legal adversary
responses have the required directions. Theorem K's two inductions,
and the reductions suggested in answer 6, were read with the 2015
clarification. Its finite computational base cases were not rerun.

The upper-bound relations (9)–(14), Algorithm H and its symmetric
branch were reviewed. The original Table2 traces comparisons
512:703, 512:653, 512:509, 512:612, 503:426, 503:509, 087:154,
087:061, giving the stated eight. The recurrence uses H, as corrected
in 1999; its scaling relation and formula (19) are consistent with the
binary insertion work and with the near-equal-length case. The
factorial inequality in answer 17 gives the claimed additive bound.

The decision diagrams for exercises 8–10 were inspected, including
their remaining merging subproblems and path costs. The deepest
paths in the twelve-comparison construction have depth eight followed
by at most four comparisons; the other displayed terminal costs also
respect twelve. The two-key threshold proof was read in both parity
cases: its five-query even-case reduction leaves g_(t-5) elements.
The corrected indices in answer 12 give the stated recurrence. The
functional definition of Graham's G and the formula for R were read
with Fig.38; their full external proof was not reconstructed.

The even-index merge in answer 19 leaves disjoint insertion intervals
whose total number of A elements is at most m. The permanent adversary
in answer 23 was checked with the corrected assignment x_11=0: deleting
the first matched row/column removes at least n tested entries, then
n-1, and so on. The sampled merge in answer 24 and the monotone-matrix
reduction in answer 25 were also reviewed. The latter concerns deciding
absence from an otherwise real-valued monotone matrix, so in the 0/1
hard case every entry must be classified by queried information; it
does not give the search algorithm advance knowledge that the matrix
contains only zeros and ones.

Known corrections are recorded in
`sources/minimum-merging-errata-review.json`: the H recurrence, the
sorting-function index in answer 1, Theorem K clarification, both
answer 12 indices, the permanent assignment, and the moved Kollár
citation. None was entered as a new error.

Exact exceptions: the full four-table constrained-adversary
computation was not reproduced; neither were the cited general
Stockmeyer–Yao bound, Christen's stronger algorithm/counterexample,
Graham's closed-form recurrence proof, the three-/four-key merging
threshold theorems, or the Tanner/Kollár average-case results. These
are accepted as attributed external results. Exercise 5 has no printed
answer; no separate new proof of its adversary inequality was built.
The open inequalities in exercise 21 were not investigated as a
research problem. Historical priority, original implementations and
the present research frontier were not independently surveyed.

Next: §5.3.3, minimum-comparison selection, printed p.207.
