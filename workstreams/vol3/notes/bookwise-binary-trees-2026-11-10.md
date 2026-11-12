# Bookwise review: binary tree searching, 10 November 2026

Reviewed §6.2.2, printed pp.426–458, all 49 original exercises,
added exercise 50, and answers on pp.708–713. Shared pp.458 and 713
are deferred to balanced trees for certification.

Checked tree insertion and its MIX counts, the random-permutation
recurrence, rank-dependent search costs, deletion cases, the deletion
bijection and its precise restriction to tree shapes. Checked the
path-length changes, commutation of deletions, probability-weighted
insertion and the distinction between a frequent-first tree and an
optimum tree.

Checked the dynamic-programming recurrence, root-set monotonicity
argument in exercises 24–27 and the quadratic running-time bound.
Checked the entropy decomposition and both cost bounds, including the
zero-weight reduction. Checked the corrected Garsia–Wachs lemmas,
weight shifts, recursive restoration of the two-step descending
invariant, depth marking and reconstruction in leaf order. The
alphabetic code and the RIGHT ON example agree with the final tree.

Known corrections to threading, deletion notation, numerical examples,
Theorem M, Garsia–Wachs proofs/figures/subroutine, answer 29, and the
random-height result were screened and excluded. No new finding.
The apparent strict inequality in the definition of C1 on p.429 was
resolved by enlarging the original: it is correctly non-strict.
Source screen: `sources/binary-trees-errata-review.json`.

Added exercise 50 was checked against the author's
[OFFLINE-TREE-INSERTION program](https://www-cs-faculty.stanford.edu/~knuth/programs/offline-tree-insertion.w).
Its inverse permutation assigns insertion priorities; the stack finds
each node's parent in the corresponding Cartesian tree. Each index
enters and leaves the stack at most once, yielding the claimed linear
bound on valid permutation input.

Limits: the complete numerical word-frequency examples and permutation
counts, the closed-form internal-path variance derivation, and all
27-leaf combination operations in Fig.18 were not independently
recomputed. Exercise 17's unsupplied threaded-deletion implementation
and exercise 28's macro design were not newly implemented. Research
exercises 9 and 48 were not newly solved. The external results on
quadrangle inequalities, worst optimum cost, unequal branch costs,
sawtooth order, rebuilding, higher branching and random height were
accepted as cited; their source proofs and historical data were not
reproduced. Exercise 45's balanced-tree data structure and exercise
46's reference to 6.2.3-21 are followed in the next section.

Next: §6.2.3, printed p.458 / file p.469.
