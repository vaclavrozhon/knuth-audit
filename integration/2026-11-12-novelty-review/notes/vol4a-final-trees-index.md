# Volume 4A: tree moments, spectra, history, and index

Publication review, 2026-11-12. The fourteen remaining baseline-confirmed
findings are retained. Checked the first-printing originals at the cited
locations, with the Christmas-tree pattern and Algorithm H on pp. 457,
459–460, and the duplicate index entries on pp. 840 and 845. Earlier
original-page checks of the mathematical destinations were reused.
The individual notes define the notation and give fuller calculations.

| Finding | Independent reason and scope |
| --- | --- |
| V4A-F0121 | Answer 7.2.1.6-54, p. 795: the second derivative sums S*(S-1), not S^2, where S is total internal path length. For n=2 the raw sum is one and the printed expression zero. Add the first-moment sum. The variance grows as (5/6-pi/4)*n^3+O(n^2), not a constant times n^(3/2). |
| V4A-F0122 | Answer 7.2.1.6-55, p. 795: the last simplification is invalid on the principal diagonal r=0. At p=2 it gives -2, while the area polynomial 1+x has derivative one. Add [r=0]*binom(2p,p)/2 or restrict this last equality to r>=1. The preceding coefficient expressions remain valid. |
| V4A-F0123 | Answer 7.2.1.6-57, p. 796: at a=b=1 the truncated first-moment sum is one, not four; its expression needs division by 2(a+b). The moment recurrence needs multiplier 2b(2b-1). The third-moment denominator is (a+b)(a+b-1), not (a+b)^2. Each follows termwise or by telescoping; the final worm-depth formula survives. |
| V4A-F0124 | Answer 7.2.1.6-67, p. 798: the Schroder recurrence begins (n+1)*S_n, not (n-1)*S_n. At n=2 the printed recurrence asserts 3=9, contradicting the exercise's own values. The generating function is correct. |
| V4A-F0125 | Answer 7.2.1.6-82(c), p. 801: for n=2 both AND and OR require three evaluations in Algorithm H, but OR has three positive outputs rather than one. The maximizing threshold is weight >= ceil(n/2), not weight > n/2. The odd-n answer and main worst-case lower bound remain valid. |
| V4A-F0126 | Answer 7.2.1.6-75, p. 799: the initial Christmas-tree row is in equation (35), not (33), which depicts Remy's leaf insertion. The descendant-count argument itself is correct. The 2015 changes to subscripts on this page do not repair this reference. |
| V4A-F0127 | Exercise 7.2.1.6-90(a), p. 481: the condition must say that vertex 0 is the unique centroid. The canonical parent sequence 011 represents a four-vertex star with centroid 1, but its forest component has size three, exceeding floor(3/2). The generation procedure in the answer uses the intended root condition correctly. |
| V4A-F0128 | Answer 7.2.1.6-106(b), p. 807: on the four-cycle at j=3, the proposed sin(k*theta) vector fails the Laplacian eigenvector equation. Keeping the printed index ranges requires sin((2k-1)*theta); simply doubling k leaves a zero vector at j=n/2 for even n. The eigenvalues and final tree-count products are correct. |
| V4A-F0129 | Answer 7.2.1.6-104(a), p. 806: absolute values belong inside the off-diagonal sum. The symmetric matrix with rows (1,2,-2), (2,1,-2), (-2,-2,4) meets the printed weaker condition but has eigenvector (1,-1,0) with eigenvalue -1. The surrounding graph-Laplacian argument remains valid because its off-diagonal entries share a sign. |
| V4A-F0130 | Answer 7.2.1.6-105(h), p. 806: insert a minus before n'*[j=0] in the first factor. For K3 and K2 the printed odd-product spectrum contains -1, impossible for a Laplacian; the repaired expression gives the triangular prism's spectrum 0,2,3,3,5,5. The April 2007 Fascicle 4 addendum introduces the same defective formula and is not a correction of it. |
| V4A-F0131 | Answer 7.2.1.6-117, p. 809: the tree whose root has children a,c and whose a has child b has prepostorder r,b,a,c, with no unlucky transition, but a has both binary children. Reversing the two root children gives the converse counterexample. Reverse child lists at even depths before applying the degenerate-binary-tree characterization. The count 2^(n-1) remains valid. |
| V4A-F0132 | Answer 7.2.1.7-27, pp. 815–816: the slot argument misses blocks enclosing the crossing pair. The partition with blocks {1,6}, {2,4}, {3,5}, at heights 3,1,2, has one crossing. For n=6 there are 64 single-crossing partitions, not the printed 63. The existing six-element verifier was inspected; no general replacement formula is claimed. |
| V4A-F0133 | Appendix B, p. 826: the subset/superset family entries need an existential condition, not the printed implication for all members of G. For F={{1}}, G={{1},{2}}, both intended outputs are F but both printed set-builders are empty. The adjacent complement equalities and answer 7.1.4-236(a) already give the correct operations. |
| V4A-F0134 | Index, pp. 845–846: de Bruijn cycles needs 626,658 in place of 625,657; Differential quantification needs 634–635,637 in place of 633–634,636. Duplicate entries under Bruijn and the quantifier symbol agree with the corrected destinations. Only the locators change. |

## Prior-report screen

Compared all relevant entries in the refreshed official `all4a-pre`,
`all4a`, `err4a`, `all4f4`, `err4f4`, `all4f1`, and `err4f1` layers. The
2015 Christmas-tree subscript changes, answer 85 replacement, historical
answer 105 additions, and Appendix B minimal-element arrow correction
are distinct from these findings. None repairs the retained defects.

Fresh web queries covered Knuth/TAOCP with variance at p. 795, Schroder
recurrence errors, genji-ko single crossings, cycle sine eigenvectors,
unlucky forests, Hansel exercise 82, p. 806 errata, and differential
quantification. No matching prior report was found. The
[Lescanne paper](https://perso.ens-lyon.fr/pierre.lescanne/PUBLICATIONS/Hol_Lin_Gen.pdf),
section 9, discusses Schroder generation and cites Knuth, but does not
report the incorrect factor in answer 67. Its indexing differs, so its
display was not used as a substitute for the direct n=2 check.

Screened the [public exercise archive](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4/7.2.1.6)
for exercises 54,55,57,67,75,82,90,104,105,106,117. Most files contain an
unrelated product/sum problem. Exercise 75 discusses a malformed exercise
transcription and an earlier attempted solution; it does not report the
equation-number error. The requested 7.2.1.7 directory was unavailable
(404). These archive entries are not correctness evidence.

No matching prior report was found in the sources checked. Absolute
priority is not established. This completes the review of all 133
baseline-confirmed Volume 4A cards: 132 retained, F0035 dismissed after
fresh inspection showed that the supposedly missing prime is present.
