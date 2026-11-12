# Distribution and radix sorting — 10 November 2026

Reviewed §5.2.5, printed168–179, exercises1–18 and answers650–652.
Original tables, card illustrations, flowchart and MIX program were
inspected together with the printed arguments and all errata layers.

The card-order argument, stable digit distribution, linked queues,
hooking through an empty pile0 and the overwritten MIX instructions
agree with their invariants. Algorithm R reverses equal-key records
because its first pass traverses the input backwards; later passes are
stable on the already linked order. Table1 and Fig.33 appropriately
use different first-pass conventions. Answer11 refers to Table1 and
its five remaining inversions, not the reversed linked input.

The MIX instruction-frequency sum gives 32N+48M+38-4E; the general
p-pass version and eight-byte instruction replacements agree. However,
E counts only emptiness tests on piles1 through M-1, while the stated
probability formulas count all piles. This is new **V3-C0036**, with
an exact repair via g_M,N+1(z)^p and a two-record counterexample.
Exercise6's occupancy recurrence, factorial moments and variance are
otherwise correct.

Signed-key ordering, alternating stack collection, MacLaren's final
insertion/rearrangement and the reading-count card bounds were checked.
The illustrated permutation has four increasing and ten decreasing
readings. Equation(8) agrees with the rounded table entries; its linear
time conclusion uses an appropriate choice sqrt(N)<M=O(N), as in the
discussed optimization, not arbitrarily superlinear memory allocation.
The trie-style string refinement in16 matches the cited method's
organization; a fresh implementation of its linear alphabet handling
was not constructed.

Theorem T and answer18 were read with the published1999 correction to
the pair-probability calculation. Two local new errors remain:
**V3-C0037** (floor(N/8) allocated bins can be exceeded by floor(KN/8))
and **V3-C0038** (the final supremum sum is cN+o(N), not N+o(N)).
The latter does not change the O(N) conclusion after summing O(b_k/c).
For the theorem we accept the usual fixed-density asymptotic reading:
a universal eventual linear coefficient, with a threshold N_0 that
may depend on the density. The printed proof does not establish one
finite-N bound uniformly over all bounded densities; that stronger
literal interpretation is not certified here.

Explicit limits: new implementations requested in10/13 were not built;
full reconstruction of Paige–Tarjan's alphabet-refinement implementation
in16 and Tamminen's original paper is outside this pass. A brief source
search identified Tamminen's paper and DOI but did not retrieve the full
article. Historical priority, MacLaren's original machine model and
benchmarks, and comparative pipeline-machine recommendations were not
independently reproduced. No broad computation was run.

Known corrections, including the2012 branch comment,2025 bibliography
and2023 historical quotation, were screened in
`sources/distribution-errata-review.json`. They do not create red markers.
