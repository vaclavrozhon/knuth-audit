# Volume 4B: SAT and exact-cover exercises, F053–F076

Reviewed on 12 November 2026 against the first edition, second printing
(November 2022). The original typesetting was inspected on printed pages
183, 335, 359, 367, 447, 449, 461–463, 467, 473, 475, 478, 483,
544, 546–547, 559, 589, 636–637 and 651–652. Existing reports, proofs,
small witnesses, and completed computation certificates were read; large
enumerations were not repeated. Here SAT means section 7.2.2.2 and DLX
means section 7.2.2.1. A symmetry class identifies arrangements related
by the geometric transformations specified in the exercise.

| Finding | Correctness review |
|---|---|
| F053 | SAT 443(e): the examples in (c) have unit-contradiction level zero, so cannot establish failure at level n−1. The two clauses (x), (not x) provide the n=1 witness; the complete Boolean cube supplies the general family. The false assertion is correctly rejected, but its cited counterexample is wrong. |
| F054 | SAT 442: for clauses (a or b), (a or not b) and the four clauses (not a or ±c or ±d), the strict sequence definition permits only a as its first forced literal. It detects a level-two contradiction through (a,c) and (a,not c), yet cannot derive not a. Thus the asserted property that every literal follows from a detected contradiction does not hold under this definition. This is a defect in the inference relation, not a counterexample to the intended UNSAT decision procedure. |
| F055 | SAT 212: the partial Latin-square definition restricts allowed colors but omits the cardinality requirements needed for the prescribed three-dimensional margins. For N=1, row and column margin one and symbol margin zero, the blank partial square satisfies the printed restrictions while no corresponding tensor exists. The cited Irving–Jerrum formulation explicitly includes the missing cardinality requirement. |
| F056 | Answer 212(d): the condition must be k=K′, not k=(I,J,K′). With N=1 and L11={1}, the printed construction gives incompatible row, column, and symbol margins. The corrected row and column matrices are both [[1,0],[1,0]]. |
| F057 | SAT 60: direct truth-table probabilities give P(f)=113/256, P(h)=11/32 and P(f and h)=603/2048. Their symmetric difference is 402/2048, not 404/2048. |
| F058 | DLX 262(b): the unprimed triangle coordinates also require x+y<n+16. Without that restriction there are 28 isolated items and 16n+92 items rather than 16n+64. |
| F059 | DLX 262(a): the asymptotic prefactor is a_(2m)^(-1/2), not a_(2m). At m=1 this follows immediately from the Fibonacci count and a_2=5. Stanley's cited paper has the same error in its equation (9); its equation (2) and preceding lemma give the correct factor. The cited erroneous formula is not independent verification. |
| F060 | DLX 443: the 3 by 3 cover with four black corners and a connected white cross contradicts the claimed (mn+2)/3 bound. It can be the unique solution of the puzzle AAA/BCD/EEE. The corrected boundary argument gives 3s≤mn+3−[m even]−[n even], where s is the number of black cells. The failure extends to an infinite family of odd-width, three-row covers. |
| F061 | DLX 442: the first multiplicity interval in the hitori encoding must be [0..0], not [1..1]. A single white cell exposes the mismatch directly. |
| F062 | DLX 432(a): the displayed kakuro row clues sum to 31 but the column clues sum to 29. Changing the column clue 11 to 13 yields the reported unique filling and the book's search-node count. |
| F063 | DLX 125: the second coordinate in both expanded-triangle formulas must use ky, not kx. Already k=1 and (x,y)=(0,1) fails the printed identity. |
| F064 | SAT 515(vi): the statement must restrict the alternating 2 by 2 rectangle to two boxes. The printed clauses impose precisely that restriction, while a valid encoded puzzle can have a blank alternating rectangle occupying four boxes. The stored full grid and clause certificate establish this mismatch; no uniqueness assumption is added to the stated problem. |
| F065 | DLX 129: the number of weak but not strong left-right symmetry classes is 294457, not 281618. The branch with no fixed monochromatic cell contributes 186846 classes, and the other branch contributes 107611. The geometric normalization proof, both independent enumeration records, and the reconciliation of overlapping symmetry classes support this count. The proposed explanation that one position case was omitted is a hypothesis, not an established account of the author's computation. |
| F066 | DLX 443: the printed mod-five construction plus added black cells does not prove the mn/5+2 bound. On a 7 by 7 board its ten initial black cells require at least two additional cells, exceeding 11.8; the completed finite check actually needs thirteen black cells. This refutes the proposed construction, not the general existence bound: a different eleven-black cover exists. |
| F067 | DLX 160: the small components reach size 20, not 12; the last illustrated placement belongs to a component of size 20, not 8. A closed component with 20 vertices and 26 edges is explicitly certified. The total component count, isolated-vertex count, and giant component remain correct. |
| F068 | DLX 158: an explicit 28 by 16 packing of one unit square, two side-two squares, through six side-six squares has area 448, below the claimed optimal 30 by 15 area 450. Nonoverlap and multiplicities are certified directly. Establishing the global optimum is unnecessary for this refutation. |
| F069 | DLX 162(e,h): the full geometric counts are 19 and 116 classes under the eight symmetries of the square, not 4 and 28. The labeled counts split as 144=17·8+2·4 and 896=108·8+8·4. Even merging inner patterns according to the suggested exact-cover encoding gives 5 and 30, so that alternative interpretation does not rescue the two claims. |
| F070 | DLX 177(b): the recurrence needs binomial(t,k), not binomial(n,k); n is not its parameter. The reported Q(5,5) remains correct. |
| F071 | DLX 167: changing a nonbinding upper bound can change the SLACK tie breaker of answer 166 and therefore the selected item. The five-option example AX, AY, BU, BV, BW changes the first branch and yields 37 versus 35 nodes with the same twelve solutions. The offset argument would apply only with an invariant item-selection rule. |
| F072 | DLX 215(d): level ell has 2(q−ell+1) nodes, not 2(q−ell). The root's two children at q=1 already expose the missing one. |
| F073 | DLX 216: lexicographic option order is not worst at every level. On K7, placing edges 12,13,23 first and then using lexicographic order gives profile (1,6,2,4), compared with (1,6,4,2). Both trees have thirteen nodes; the witness does not claim a larger total tree. |
| F074 | DLX 224: the proposed chain propagates backward earlier than stated. At n=6 it performs four productive rounds and five visits to P2, rather than six visits. The stored trace locates the first premature deletion; no new large experiment is needed. |
| F075 | DLX 236: the stated N=20 costs are too large by a factor of 1024. The exact costs are 130230066663839627189/64 and 130915446232517223025/64. Their ordering is unaffected. |
| F076 | DLX 236: the assertion “if and only if N≥21” omits N=2, for which every queen permutation has the same cost 680. Among positive integer exponents the correct condition is N=2 or N≥21. The previous finite and asymptotic optimality certificates were retained, without repeating the enumeration. |

The detailed supporting arguments remain in the corresponding local finding
notes and reports, including `SYMMETRIES129_NOTES.md`,
`PARTRIDGE157_158_SOURCE_NOTES.md`, `TILING_ZDD_NOTES.md`, and the
per-finding certificates under `audit-2026-10-31/results/`.

## Prior-publication review

The refreshed current and cumulative author errata for Volume 4B,
Fascicle 5 and Fascicle 6, including their available TeX sources, were
checked at the matching printed and fascicle page numbers and by subject.
The 2023 corrections to answer 162 change the encoding, heuristic and
illustration, not the two counts in F069. The 2022 corrections to answer
215 concern parts (e) and (g), not the level formula in (d). The 2017
correction to SAT 212(a) does not repair its definition or part (d).
Corrections to the continuation of SAT 515 do not add the two-box
restriction to (vi). The later illustrations for hitori answer 445 do
not correct answer 443. No matching correction was found in these layers.

Fresh public searches included the exercise numbers and distinctive terms
or constants: unit contradiction, 281618, 294457, MacMahon symmetries,
partridge 28 by 16 and area 448, hitori mn/5, 402/2048, Stanley dimer
prefactors, and hard sudoku 515/two boxes. Many results were unrelated
or copies of the book. The inspected public
[tamnd/brain exercise collection](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4)
included SAT 60, 212, 442, 443, 515 and DLX 125, 129, 158, 160, 162,
167, 177, 215, 216, 224, 236, 262, 432, 442, 443. Several contain
unrelated generated answers; the relevant hitori answer repeats the false
bound with an invalid boundary argument. The item labeled “corrected
solution” for DLX 216 does not identify the book's levelwise claim or
provide the counterexample here. No matching prior error report was found.

[Friedman's August 2002 page](https://erich-friedman.github.io/mathmagic/0802.html)
and its two final packing diagrams were inspected. They give exact
order-eight rectangle packings; the order-six result earlier on the page
uses rectangular pieces of aspect ratio three, not the square pieces of
F068. The [Mathpuzzle account](https://www.mathpuzzle.com/partridge.html)
likewise does not supply the order-six 28 by 16 square packing.
[Stanley's original paper](https://math.mit.edu/~rstan/pubs/pubfiles/64.pdf)
was consulted directly for F059, with the distinction between its correct
product formula and erroneous asymptotic prefactor recorded above.

All 24 findings are retained. The novelty conclusion is only **no matching
prior report found in the searched sources**. It does not establish
priority for the underlying mathematics or exclude inaccessible reports.
