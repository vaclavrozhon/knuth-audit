# Bookwise review: balanced trees, 10 November 2026

Reviewed §6.2.3, printed pp.458–481, all 33 exercises and answers
on pp.713–719. Shared pp.481 and 719 are deferred to multiway trees.

Checked AVL height bounds, insertion rotations and balance updates,
Program A's instructions and timing branches, positional search and
all rank updates in Algorithm C. Checked deletion's three balancing
cases, concatenation's height choice, the splitting construction and
its telescoping-height explanation, including the illustrated trees.

Checked the generating-function recurrence, extreme coefficients,
product decomposition and doubly exponential calculation, mean-size
recurrence and the fringe-count expectation in exercise 11. The
empirical model is explicitly heuristic. Checked the linear rebuilding
algorithm and its binary-carry count, weighted-height bounds, the
height/weight counterexamples, storage-allocation augmentation,
rotation-order argument and implicit balance-bit encoding.

New findings: C0059 (the 2022 height-bound erratum), C0060 (root
initialization missing from the counter's definition), C0061 (shared
index changed during recursive reconstruction), C0062 (minimum in
place of maximum in a path-length argument), and C0063 (keys versus
internal nodes in the 2–3 comparison estimate). The apparent missing
equality case in answer 15 was an OCR error; the original is correct.
Known height-coefficient, probability-table, reference, numerical,
notation and nonempty-input corrections were excluded. Source screen:
`sources/balanced-trees-errata-review.json`.

The balanced-tree operations required by 6.2.2-45 are now checked;
rotations preserve the separate inorder list links. The online linear
rebuilding procedure requested through 6.2.2-46 is also checked; its
cited average comparison theorem remains an external result.

Limits: no new 7!/10! permutation census, empirical timing experiment,
full extremum census for exercise 12, or long-constant digit
recomputation was performed. The external enumeration, one-bit
insertion, weighted-rotation case analysis, finger-tree bounds,
splay/treap guarantees and partial 2–3 average analysis were accepted
as cited or explicitly sketched; source proofs were not recreated.
The unsupplied research/design work in exercises 26 and 28 was not
newly undertaken, nor was the open portion of 29 solved. The detailed
implementation behind the splitting and finger-tree sketches was not
newly supplied.

Next: §6.2.4, printed p.481 / file p.492.
