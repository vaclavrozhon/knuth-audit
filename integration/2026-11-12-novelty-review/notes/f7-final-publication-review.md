# Fascicle 7: final publication review

Reviewed on 12 November 2026 against the first digital release, March 2025 (ISBN 978-0-13-532824-8, SHA-256 `3acff1263e51e3e390d19b0f9f20f49d34caf61baff967c41d1981133146dd39`). All 16 baseline-confirmed cards are retained in the scopes below. Their full argument notes were reread and the affected original typesetting inspected, together with relevant definitions, questions and adjacent algorithms. Prior successful calculations were reused.

## Fresh errata and public reports

All three [official current TeX](https://www-cs-faculty.stanford.edu/~knuth/err4f7.textxt), [current rendered](https://www-cs-faculty.stanford.edu/~knuth/err4f7.ps.gz) and [cumulative rendered](https://www-cs-faculty.stanford.edu/~knuth/all4f7.ps.gz) sources were refreshed. The TeX has SHA-256 `8f29e4e9da410a2fcd0142aa3ce1e9c7189bc29d5ce5d07f26102ccbeb2dc285`; this is the same November 7 revision used in the bookwise refresh earlier on November 12. Its changes since the older October archive were explicitly considered.

In particular, the November 6 answer-50 amendment repairs the separate shared-inner-line issue in the final algorithm paragraph; it does not change part (a). The October 4 matching recurrence still starts its exclusion strings at 1. The answer-305 singleton-domain change and answer-429 subset clarification leave the respective residual-support and invariance problems intact. Known nearby corrections were not recounted.

Fresh targeted public searches combined Knuth/Fascicle 7 with the specific claims and locations: no girl is free; one option for each slot; answer 29 cyclic histoscape; general position/triple crossing; clasp arrow; six boundary W cases; answer 166 self-compatible; answer 224 order encoding; Fig.116; answer 278 matching recurrence; residual supports; Algorithm A/A6/secondary items; 137.4/factor 60; answer 364 polynomial; answer 429 Inv(O); and Algorithm N independent of n. The results were principally copies of the text, unrelated uses of the same words, and general material rather than matching reports. No matching prior public report was found. This is not an exhaustive history of private reports or a guarantee of priority.

The original [Compact-Table paper](https://arxiv.org/abs/1604.06641), the author’s [histoscape-unrank](https://www-cs-faculty.stanford.edu/~knuth/programs/histoscape-unrank.w), and [xccdc](https://www-cs-faculty.stanford.edu/~knuth/programs/xccdc.w) are supporting comparisons already recorded with the individual arguments; correct behavior in those programs is not itself a prior report of a book error.

## Decisions

- **F7-C0001:** With unequal bipartition sizes, covering all girls need not give a perfect matching: K(1,2) is a direct counterexample. The matching is still maximum. Remove the perfection claim or qualify it by equal side sizes.

- **F7-C0003:** The first sentence of answer 20 calls the slot/type items options. The construction has one item per slot and per model type, and options for allowed slot/model pairs. The September and October 2026 amendments affect different sentences.

- **F7-C0004:** Answer 29 identifies the final cyclic-buffer arguments with matrix suffix cells without the required rotation. For a 2-by-2 binary histoscape the count interpreted by the printed tuple is 2 versus the actual suffix count 1. The official unranking program performs the rotation and is not faulty.

- **F7-C0005:** Even after applying the September 2026 amendment, answer 40 permits three projected edges to cross at one nonvertex point. The explicit three-tetrahedron configuration meets both printed conditions yet has four visible branches there, contrary to the HC-picture definition. This is a defect in the sufficient conditions, not in the theory assuming genuine general position.

- **F7-C0006:** The specified downward arrow in Fig. 104(c) lies on a visible edge whose two incident faces are both front-facing. It must be the convex-edge mark, not a half-edge arrow. The claim concerns the depicted clasp; it does not rule out a different spatial scene with an abstractly admissible labeling.

- **F7-C0008:** The six cases in exercise 50(a) omit another boundary placement of a W junction. The simple, biconnected eight-vertex picture with chord ac realizes W(h,b,c), not the listed W(b,c,h). The new November 6 erratum restricts the algorithm in the last paragraph of answer 50(c); it does not amend the six-case assertion in part (a). The separate shared-inner-line defect is already known and is not counted here.

- **F7-C0011:** For ordinary subgraph isomorphism in answer 166(b), the absent-edge label Lambda must be compatible with every target label, not only itself. Fixing an endpoint of a three-vertex path in a triangle gives two valid embeddings, both incorrectly eliminated by the stated compatibility extension.

- **F7-C0012:** The units for order encoding in answer 224 set w1 = 0 and w2 = 1, falsifying Table 2’s domain clause not w2 or w1. The order-encoding exception must set w1 = 1. The other encodings and the graph-coloring reduction are unaffected.

- **F7-C0013:** The first filtering round in the prose below Fig. 116 produces panel (b), not (c). Four more deletions then produce (c). Change the panel reference; the diagrams and no-solution conclusion remain valid.

- **F7-C0014:** The current October 4 replacement proof for answer 278 still starts the exclusion strings at index 1 despite zero-based rows and columns. The 3-by-3 witness with rows 001,010,101 makes its b22 recurrence false. Start at b_i0 and b_0j. This finding is in the official errata, not in the original book page.

- **F7-C0015:** The residual-support shortcut can read an inactive word that Algorithm R intentionally leaves nonzero. Removing y = e in the recorded (e+1)-tuple example invalidates the sole support for x = 1, but the cached word still passes the shortcut. The defect is missed pruning; it does not by itself establish an invalid final solution.

- **F7-C0016:** Algorithm A, step A6, reads ITEM[k] after incrementing k without testing the array end. The ordinary nonempty exact-cover instance with two primary items and no secondary items reaches the uninitialized ITEM[ACTIVE]. The official xccdc program uses a bounded scan and is correct at this point.

- **F7-C0017:** The factor greater than 60 on page 74 contradicts the fastest domain-consistency column for H in table (130). The displayed numbers give 52.984..., and their full rounding intervals still give less than 53.847. This is a local comparison error, not a rerun or challenge to the historical measurements.

- **F7-C0018:** Answer 364’s explicit-table construction can have exponentially many tuples: m distinct two-tuple relations yield a product with 2^m tuples. Its unqualified polynomial-time parenthetical is false when the input relations are part of the input. Satisfiability equivalence and the exercise’s permission to ignore efficiency remain valid.

- **F7-C0019:** The projection-table subset P in answer 429 need not be invariant under the clone: for Boolean OR, 0011 OR 0101 = 0111 is outside P. The September amendment P subset R is correct but does not remove the preceding false membership claim. The proof is repaired by using the invariance of R, already established.

- **F7-C0020:** N5 seeds its dictionary from every source tuple, so its cost is not independent of n. For Boolean ternary majority, N1 contributes at least binomial(n,2) distinct tuples, and the first constrained call scans them even though the projected dictionary has only four keys. The overall fixed-arity polynomial-time conclusion survives.

