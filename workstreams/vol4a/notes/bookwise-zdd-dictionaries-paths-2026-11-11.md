# Dictionary queries and graph paths

Main253–255 through graph paths, exercises219–235 and answers665–669
through235 were read together. Whole main253–254, exercise275 and
answers665–668 are certified. Shared main255/exercise276/answer669
await prime implicants and extended family algebra. F0049 concerns
the median-word definition; F0050 concerns the forest postorder claim.

The25-bit and130-bit word encodings and their example assignments
were checked. The family operations in222 correctly form subwords,
pattern matches, vowel counts, repeated matches and letter replacements.
For repeated matches, removing full words from pairwise intersections
before taking downward closure excludes self-pairs. The final quotient
of the complementary dictionary excludes patterns for which every
vowel completion fails, leaving those with at least one completion.
The individual dictionary counts, linguistic membership assertions,
node totals and timings were not independently recomputed.

The expectation formula221 counts possible zeads, then uses inclusion-
exclusion over disjoint prefix blocks. At position l and letter j,
the suffix pool has L=26^(5-l)*(27-j) elements. A size-s zead must
contain the current letter, giving C(L,s)-C(L-26^(5-l),s) possibilities.
For k prescribed prefix blocks, exactly sk selected words are fixed
and all remaining selected words lie among26^5-kL possibilities.
This yields the printed alternating sum; the floating-point total
and average profile were retained without a new numerical evaluation.

The median definition223 permits an input word itself as the result,
invalidating its two-distance-pattern assertion (F0049). The answer's
recursive construction explicitly excludes that case; its intended
three positive distances sum to five. The omitted eight recursive
variants and its full median census were not reconstructed.

The source-to-sink forest correspondence224 uses high edges for first
children and low edges for next siblings. Its additional postorder
claim is false (F0050). For225, the mate table records unfinished path
endpoints, untouched vertices and degree-two vertices. The virtual
source-target edge turns completion into cycle closure. The endpoint
splice and both rejection tests were traced through the displayed
first transitions. Closing a component is accepted only if no other
unfinished component remains; leaving the frontier with an unfinished
endpoint is rejected. The cycle, Hamiltonian and variable-endpoint
changes226–228 retain these invariants. Signed endpoint updates233
enforce one incoming and one outgoing arc, under the corresponding
directed closure interpretation. No full frontier implementation was run.

The small path figures were inspected, and the main text's first
four-edge route agrees with the labels. The DC explanation229 accounts
for the difference between the two graph models. The moment formulas
for route length230 and the corner-neighbor decomposition2h+d for
king's tours232 were checked. Exact route/cycle counts, extremal
uniqueness and lengths, full edge-distance sums and ZDD sizes were
not recomputed. The known2017 amendment cites Beluhov's even-board
maximum-tour theorem; that external theorem was not reproved.
Postal-code overlap and word-suffix graphs234–235 were read as given;
their pruning preserves cycles, and the sample cycles follow the
specified overlap rule. Their exhaustive classifications were retained.

Next: main255 prime implicants, exercises236 onward, answers669 onward.
