# Volume 4A: graph and Boolean findings, publication review

Reviewed on 12 November 2026 against the first edition, first printing
(2011). All sixteen findings below are retained. This is a review of the
identified defects, not a claim that the underlying mathematics is new.

The original page images were inspected together with the exercise or
definition needed for each claim. The existing detailed notes and finite
counterexamples were checked; no large computation was repeated.

| ID | Reason for retaining the finding |
| --- | --- |
| V4A-F0001 | Answer 7-46(b), p. 521: contracting an arbitrary edge of a maximal planar graph need not remove exactly three edges and preserve maximality. An equatorial edge of the triangular bipyramid has three common neighbors; simplifying after contraction leaves five edges on four vertices. The Euler-formula conclusion remains correct. |
| V4A-F0002 | Answer 7-90, p. 526: the diameter characterization needs connected induced subgraphs. The cograph K4 contains a noninduced four-vertex path of diameter three. The book explicitly distinguishes subgraphs from induced subgraphs. |
| V4A-F0003 | Answer 7-110, p. 528: the odd-degree construction overlaps its two circulant ranges when n=d+1. For n=4,d=3,p=4, the printed construction has degree two, not three. The separate complete-graph construction in the detailed note repairs this boundary. |
| V4A-F0004 | Answer 7-126, p. 530: the asserted five-color rule misses further three-row tori. The 3 by 6 kingwise torus contains K6 and has a six-coloring. The cited paper restricts its five-color theorem to odd cycles longer than three. |
| V4A-F0005 | Answer 7-128, p. 530: the Cartesian-product chromatic-number equality needs nonempty factors. The book allows K0 explicitly. K0 times K2 has at most one color, whereas the maximum of the two factor chromatic numbers is two. This is a minor boundary omission, retained from the baseline rather than a new boundary search. |
| V4A-F0006 | Exercise 7.1.1-50, p. 86: the displayed random-Horn limit fails for the specified uniform clause model. At c=10 the printed expression is at least exp(-10), but the least-model union bound and Poisson coupling in the detailed note give limsup at most exp(-18)+exp(-12)/(1-exp(-6)), which is smaller. The argument checks the actual normalized clause count and does not assume a replacement limiting law. |
| V4A-F0007 | Answer 7.1.1-52(d), p. 544: the probability that an n-bit uniformly chosen integer is prime is of order 1/n, not 1/log(n). The nearby Fibonacci-game answer confirms that n denotes the bit count. |
| V4A-F0008 | Exercise 7.1.1-70, p. 89: for n=1 the prime-point flip takes the monotone self-dual function x to its complement. The latter is not monotone. The nontrivial construction needs n at least two. |
| V4A-F0009 | Answer 7.1.1-85, p. 550: acyclicity must disregard self-loops. The formula (x OR y) AND (x OR NOT x) defines the reduced median set {01,10,11} but its implication graph has loops. The given construction does not exclude tautological clauses. |
| V4A-F0010 | Answer 7.1.1-132(b), p. 560: the generalized bent construction uses the permutation on the wrong half of the variables relative to the arbitrary added function. The six-variable example in the detailed note has Walsh coefficient 16, hence an affine agreement count of 40 instead of the bent maximum 36. The standard construction uses u dot g(v)+h(v), or g(u) dot v+h(u). |
| V4A-F0011 | Answer 7.1.2-33, p. 565: masking the remaining inputs by the leading-zero test loses information needed by the minterms. For n=4,N=3, inputs 0000 and 1000 become identical after this operation although their zero-minterm values differ. Masking the computed outputs repairs the argument. |
| V4A-F0012 | Answer 7.1.2-47, p. 570: the stated finite counting bound for several outputs misses output choices. At n=256,m=r=4, the ordered distinct choices of four essential binary functions already give 11349915205231040601600 functions, exceeding the stated upper bound 10367357475042936177152. This refutes that bound, not the leading asymptotic conclusion. |
| V4A-F0013 | Answer 7.1.2-38(a), p. 567: the listed thresholds put the sorted outputs in reverse order. The exercise explicitly specifies ascending order. For input (1,0), the printed top-to-bottom order gives (1,0), whereas ascending order is (0,1). The kth output needs threshold n+1-k. |
| V4A-F0014 | Answer 7.1.2-70(c), p. 575: two determinant products have the wrong signs. For the matrix with rows 100,001,010 the determinant is -1 but the printed circuit reports positivity. Interchanging products y2 and y5 fixes this sign mismatch. |
| V4A-F0015 | Exercise 7.1.2-67, p. 130: minimizing X's worst-case outcome reverses the stated objective. Page 115 requires winning when possible and avoiding avoidable losses; answer 66 on p. 574 explicitly says maximized. The March 2010 Fascicle 0 change introduced the erroneous word rather than correcting it. |
| V4A-F0016 | Answer 7.1.2-75, p. 576: flipping the all-zero and all-one inputs of every decomposable function need not make it indecomposable. Four-variable OR becomes NAND. Both have a two-block decomposition. The surrounding exercise does not impose an additional restriction that excludes this example. |

## Official errata

Compared the refreshed current and historical layers
[all4a-pre](https://www-cs-faculty.stanford.edu/~knuth/all4a-pre.ps.gz),
[all4a](https://www-cs-faculty.stanford.edu/~knuth/all4a.ps.gz),
[err4a](https://www-cs-faculty.stanford.edu/~knuth/err4a.ps.gz),
[all4f0](https://www-cs-faculty.stanford.edu/~knuth/all4f0.ps.gz), and
[err4f0](https://www-cs-faculty.stanford.edu/~knuth/err4f0.ps.gz).
The refresh manifest records the files and dates. Relevant original
Fascicle 0 answer locations were checked as well as the Volume 4A pages.

Nearby corrections change the cograph equation and wheel indices, the
even-degree case of answer 110, the year in answer 126, the ordering of
exercise 67 in Boolean Basics, affine constants in answer 132(b), and the
wording of exercise 7.1.2-38(b). None repairs the corresponding defects
above. The March 2010 tic-tac-toe replacement repeats the wrong objective.

## Public-source screen

Queries combined Knuth or TAOCP with triangulation/edge contraction,
cograph/induced, near-regular, kingwise/coloring, Cartesian-product errors,
Horn/Istrate/error/normalization, prime-bit probability, 7.1.1-70,
bent/errata, minterms, multiple-output counting, worst-case/minimizes,
and decomposable/all-equal. No matching public error report was found.
Search engines often returned unrelated results; this is a bounded
screen, not proof of absence.

The following specific leads were checked:

- [Vesztergombi's original paper](https://cyber.bibl.u-szeged.hu/index.php/actcybern/article/view/3179/3164)
  states the five-color theorem for odd cycles longer than three and
  discusses the seven-color triangular factor separately. This supports
  the counterexample to the book's overgeneralization; it is not a report
  identifying a book error.
- [Istrate's cited paper](https://onlinelibrary.wiley.com/doi/pdf/10.1002/rsa.10028)
  and its [preprint](https://arxiv.org/abs/cs/9912001) state the same limiting
  expression. The [later k-Horn paper](https://arxiv.org/abs/cs/0007029)
  cites that result; its September 2025 revision is described as a title
  update. No published correction of the normalization was located.
- [Carlet and Villa](https://link.springer.com/article/10.1007/s10801-025-01415-5),
  section 6, gives the standard Maiorana–McFarland form. It does not
  identify the book's swapped-argument error.
- The public [tamnd/brain exercise collection](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4)
  was screened at 7.1.1 exercises 50, 52, 70, 85, 132 and 7.1.2 exercises
  33, 38, 47, 67, 70, 75. These generated solutions are not mathematical
  authority. Their discussions of previous errors generally refer to
  their own earlier solutions. Exercise 50 repeats the disputed limit;
  exercise 85 gives a different, invalid characterization; exercise 75
  misinterprets the all-equal function. Exercise 38(a) does give the
  correct reversed threshold indexing, and exercise 67 uses the usual
  maximizing objective. Neither explicitly compares this with the
  erroneous printed answer or identifies an erratum. These prior correct
  solutions are disclosed here; the audit claims a defect in the printed
  answer, not novelty of the correct sorting or game-theoretic formula.

For every retained card the precise conclusion is **no matching prior
error report found in the checked sources**. Absolute priority is not
established.
