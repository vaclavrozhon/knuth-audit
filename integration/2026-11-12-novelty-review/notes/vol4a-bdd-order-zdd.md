# Volume 4A: variable order and ZDD findings, publication review

Reviewed on 12 November 2026 against the first edition, first printing
(2011). All sixteen baseline findings F0041–F0056 are retained. Their
original notes were read and the small witnesses checked directly.
Original pages 236, 247, 275–276, 646–647, 650, 656–657, 659,
663, 666–667, 669, 674–676 and 678 were inspected as relevant.
BDD, QDD and ZDD mean binary, quasi-reduced and zero-suppressed decision
diagrams. The detailed notes define the relevant functions and profiles.

| ID | Reason for retaining the finding |
| --- | --- |
| V4A-F0041 | Answer 142(b), p. 647: exactly m entries are selected in every row and column of the 2m by 2m weight matrix, so the displayed weight sum lacks a factor m. At m=2 it is 1950, not 975. This is a local calculation error in the threshold argument. |
| V4A-F0042 | Answer 158, p. 650: the piecewise profile formula tests the position j*pi but indexes its sequences by the variable label j. In the five-variable example with order x1,x2,x5,x3,x4, two nodes test x5, whereas the printed b5 is one. Use the position consistently. |
| V4A-F0043 | Theorem W proof, p. 247: under equation (91)'s convention on p. 236, stable unshuffling of the printed order gives sigma=(3,1,4,5,7,2,6,9,8). The printed permutation changes the order within the first component. This affects the proof setup, not the theorem's conclusion. |
| V4A-F0044 | Theorem X and answer 176(d), pp. 247 and 656: the proof fixes a variable order, forms P,Q from it, and then chooses the multiplier a. It does not prove that one a works for every order, as B_min requires. Woelfel's original Theorem 11 explicitly has the former quantifier order. This is a proof gap, not a refutation of the numerical assertion. |
| V4A-F0045 | Answer 177, pp. 656–657: the summed profile bound gives one node at k=2n, but the nonconstant multiplication-bit function needs two terminals. Adding one changes the evaluated numerator from -12 to -5. The advertised upper bound still follows. |
| V4A-F0046 | Answer 197, p. 659: support masks are compared with the index of the zero-function node. Both terminal support masks are zero, so the one-variable function x1 incorrectly receives empty support and is classified as zero. Compare child indices with zeta instead. |
| V4A-F0047 | Answer 211, p. 663: the exact-cover comparison subtracts a zero residual even when none exists. For rows ab,cd,a,b,c,d, the two residuals after the first choice are nonempty, distinct, and both support the next row; q1=z1=2. Replace q_k-1 by the number of nonzero residuals. The final Z<=B result remains valid. |
| V4A-F0048 | Answer 213, p. 663: the last two coverage counts (2,1) or (3,2), added to sixty ones, give an odd total although every domino contributes two. The color balance requires their difference to be two; the possible pairs are (2,0) and (3,1). |
| V4A-F0049 | Exercise 223, p. 275: while, whale, stiff meet the coordinatewise median definition with result while, giving distances 0,1,4. The claimed positive partitions require excluding each input word as the median, as the later algorithm already does. |
| V4A-F0050 | Answer 224, p. 667: the path family {{a,b},{a,c}} has a tree-shaped ZDD in preorder a,b,c, but in postorder b,c,a the nonsink a is shared. The assertion that postorder preserves the diagram is false; preorder and level order retain the intended correspondence. |
| V4A-F0051 | Answer 236(d), p. 669: identity (xvi) is valid, including empty families. A set hits f union g exactly when it contains a minimal hit of each; minimizing their unions proves the identity. The blocker of an empty family is the unit family, so the asserted exception is also incorrect. |
| V4A-F0052 | Answer 247, p. 674: k is undefined in the conjunction bound 2^(k-1). With 2^n inputs, the correct largest index j is 2^(n-1)-1; merely changing k to n still permits an out-of-range input. No additional defect in the base case or census is claimed. |
| V4A-F0053 | Answer 255(b), p. 675: k starts at zero and the while-k<m body never changes it. For positive m the loop does not terminate. Increment k after computing the sum and carry. The full-adder formulas themselves are correct. |
| V4A-F0054 | Answer 267, p. 678: the minimum descendant-family ZDD has n+2 nodes, not n. The printed maximum already fails at n=2, where both forests give four rather than six. The stated auxiliary recurrence gives maximum floor(n^2/4)+n+1 for n>=2, with value three at n=1. |
| V4A-F0055 | Answer 267, p. 678: the printed derivative has coefficient two at z, but the one-vertex tree contributes one. Differentiating the displayed functional equation yields z/s+z/(4*s^2)-z/4, where s=sqrt(1-4z). This agrees with the final forest first moment, which needs no correction. |
| V4A-F0056 | Answer 261, p. 676: the QDD for x1 AND x2 has five nodes, while the complete minimum DFA accepting only 11 has four states. Rejecting residuals at different levels must merge. The general uniqueness analogy remains valid after that qualification. |

## Official and public-source comparison

Compared the refreshed [prepublication changes](https://www-cs-faculty.stanford.edu/~knuth/all4a-pre.ps.gz),
[later changes](https://www-cs-faculty.stanford.edu/~knuth/all4a.ps.gz),
[current errata](https://www-cs-faculty.stanford.edu/~knuth/err4a.ps.gz),
and both Fascicle 1 layers
([all4f1](https://www-cs-faculty.stanford.edu/~knuth/all4f1.ps.gz),
[err4f1](https://www-cs-faculty.stanford.edu/~knuth/err4f1.ps.gz)).
Nearby entries concern the index sets in answer 142, a multiplier-name
correction in answer 176, the Sauerhoff citation in answer 177,
answer 198's cross-reference, answer 160's symmetry claim, exercise 253,
and numerical or bibliographical details of answers 255 and 260.
None repairs the respective retained defects.

New public queries combined Knuth/TAOCP with Theorem X and Woelfel,
unshuffle and page 247, exercise 197, blocker 236, median word,
ZDD postorder, descendants 267, QDD minimum automaton, sweetness 247,
and vector addition 255/increment. Existing targeted query logs linked
by the individual notes were also retained.

The cited primary [Woelfel paper](https://cspages.ucalgary.ca/~woelfel/paper/OBDD-MUL/obdd-mul-journal.pdf)
was reopened: Theorem 11 fixes the variable order before selecting a,
and Section 3 explicitly repeats this dependence. It supports the
scope of F0044 but does not report the later book error.

The public [tamnd/brain solutions](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4/7.1.4)
were screened at exercises 142, 158, 166, 176, 177, 197, 211, 213,
223, 224, 236, 247, 255, 261 and 267. Several address different
problems or misstate basic definitions. Exercise 211 only discusses
the empty-row exception already recognized by the book. Exercise 267
corrects its own proposed model, then gives incompatible asymptotics;
it does not identify either printed defect reviewed here.

Exercise 236 labels (xvi) true, without noting the book's contrary
answer or its asserted empty-family exception. This is an earlier
correct classification, amid other incorrect classifications, not an
explicit report of this book defect. The underlying blocker identity
is standard; no novelty of that identity is claimed.

No matching prior error report was found in the checked sources.
Absolute priority is not established.
