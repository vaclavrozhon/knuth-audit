# Minimum-comparison selection — 10 November 2026

Reviewed §5.3.3, printed pp.207–219, exercises 1–27 and answers
pp.660–666, including the original diagrams. New findings C0042
(false probability estimate in answer 24) and C0043 (index in answer 21).
Shared pp.219 and 666 continue into sorting networks and await that
block for whole-page certification.

Theorem S's adversary, its superseded-set bound, and the maximum/second
maximum counts were reviewed. The tree-selection depth multiset and
Kislitsyn argument give the stated upper bounds; the reserve-element
construction explains the improvement in (11). The eight-element
selection example was traced through both discard cases. Theorem L
was read with the 2025 clarification: distinct dummy elements,
induction on n, and recursive arguments greater than 32. Its constants
and padding slack agree with 15n-163. The five-element-group variant
also gives the looser stated 18n-151 bound for sufficiently large n.

The decision diagrams in answers 9–10 were inspected. In Fig.42 the
representative leaf weights sum to 90 and their weighted depths sum
to 585; restoring the eight initial symmetries gives mean 6.5. The
second-largest partial-order formula, three comparison types, and
power-of-two ceiling argument in answer 6 were checked. The leaf
count in answer 4 uses a falling factorial, not a binomial coefficient.
The strict monotonicity in answer 3 justifies the padding subtraction
used in answer 21. Its two-tree updates and amortized extra comparison
were read with the corrected index recorded in C0043.

For answer 13, a direct accounting of the described operations uses
a positive recursive sample cost and an O(n^(2/3) log n) remainder:
T(n) <= T(n^(2/3)) + n - n^(2/3) + n/2 + O(n^(2/3) log n).
This proves the requested stated order. The printed negative recursive
term can be absorbed in its O(n^(2/3)) term, so that sign alone was not
promoted to a separate asymptotic counterexample. The smaller remainder
in the printed accounting was not independently justified. No additional
finding based only on that presentation ambiguity was created.

The useful/useless charge proof in answer 25 was read through its
permutation mappings and the final paired-charge inequality. The
component reductions of answer 26 and the randomized adversary of
answer 27 were reviewed, including the final leaf-probability count,
the two cases for the size of Q, and the choice of q and r. As usual
these adversaries answer nonredundant comparisons; they do not require
independent coin flips for relations already forced by transitivity.
The terminal partial-order-production theorem concerns a prescribed
output order shape; it is not a claim that an already known total
ordering needs sorting again.

Known corrections were applied from
`sources/minimum-selection-errata-review.json`: distinct keys, the
correct exercise reference for the Bent–John bound, the 2013 extra
V3 counterexample, Theorem L clarifications, the Fig.41 caption, the
updated Dor–Zwick reference, and the answer 21 wording clarification.
Adjacent merging/network corrections in that extract belong to their
respective blocks. None was entered as a new error.

Exceptions: the exact computer-derived optimum entries and comparison
tree censuses behind Tables1–2 were not rerun. External Kirkpatrick,
Eusterbrock, Noshita, Hadian–Sobel, Dor–Zwick, and Yao results were accepted
as attributed; their full source proofs were not reconstructed. The
generalization sketched in answer 22 and the reserve-element extension
in answer 21 were read as cited/sketched constructions, without building
new full general proofs. Research exercises 19–20 and 23 were not solved
anew. No numerical implementation of the selection algorithms was built.
The final bound in exercise 24 remains supported by later literature,
but its printed proof is invalid at the tail estimate (C0042).

Next: §5.3.4, sorting networks, printed p.219.
