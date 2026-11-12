# Bookwise review: digital searching, 10 November 2026

Reviewed §6.3, printed pp.492–512, all 44 printed exercises plus the
added exercise 45, and answers on pp.721–728. Shared answer p.728 is
deferred to hashing for page coverage.

Checked trie, digital-tree and Patricia search/insertion/deletion,
the key truncation variant, longest-prefix reasoning, tagged links,
skip updates and enumeration after a prefix search. The compressed
49-entry table preserves the nonblank entries; its zero-character
transitions terminate, and the stated TRASH trace takes six iterations.
The fifteen-key example and its depth argument were checked without
a permutation census. Checked the figures against their branching
rules and the illustrated generating functions.

Checked multinomial/binomial recurrences, the internal/external
generating-function relation, product expansions, trie cutoff
calculations, occupancy counts, successful and unsuccessful search
weights, elementary bounds, the Patricia recurrence, Bernoulli-series
argument, shape probabilities, modified path-length extrema, dynamic
programming parameters and front/rear compression count. The corrected
May 2026 proof of exercise 34(b) was read from the official errata;
its two ranges m<=n and m>=n and the summable error estimates were
checked. The Mellin evaluation is used at the exercise's stated
asymptotic precision, with its existing error term.

New findings C0065–C0072 concern timing, a query bound, a recurrence
cross-reference, missing branch multiplicities, the general-alphabet
successful-search formula, an incorrectly named trie quantity, a
subgroup-reduction cycle, and a missing series factor. C0073 concerns
two errata headings only. Known corrections were excluded from the
book's findings. See `sources/digital-searching-errata-review.json`.

The pending reference from 5.2.3-37 is checked: equation (13) identifies
the insertion depth with the difference of successive path lengths,
and the binary unsuccessful-search expansion in exercise 28 gives
the stated constant. The periodic term in 5.2.3-37 is defined locally
only as a periodic function, so its sign convention is not treated as
a contradiction with the explicitly defined function here.

Limits: no proof that 48 packed locations are impossible, full
permutation census, forty-digit constant recalculation, or new
implementation of the cited optimum/ternary structures was attempted.
External leaf-count, variance, limiting-distribution, height and
ternary-search results were accepted as cited; the abstract Nielsen
generator theorem was not reproved. The printed membership procedure
itself was checked and fails as documented in C0071. No replacement
algorithm or full program for that exercise was newly supplied.
Standard Mellin and partition identities were used, not independently
reproved. One short numerical check supports the specific M=3
coefficient defect; it is not a general verifier.

Next: §6.4, printed p.513 / file p.524.
