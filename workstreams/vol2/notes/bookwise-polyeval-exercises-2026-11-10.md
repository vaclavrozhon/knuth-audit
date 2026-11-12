# Volume 2: remaining polynomial-evaluation exercises

Reviewed 10 November 2026 under the bookwise audit policy. This block
reads exercises 4.6.4-37–74 on printed 518–524 together with their
answers on 704–719. Exercise 50 was already recorded in the preceding
block. Original pages were inspected for formulas whose OCR was
ambiguous and for every reported error. Earlier detailed reviews of
exercises 1–7 and 18–36, and the current review of 8–17, are retained.

The printed arguments were followed through continued fractions,
polynomial chains, tensor rank and border rank, integer convolution,
matrix multiplication, division-free determinants and differentiation.
No old computation or large verifier was rerun. The only computation
in this section's current pass was the short FFT count check already
documented with C0252. All remaining checks were algebraic reading.

The following points record the substance of the review, rather than
creating a separate inventory of every statement.

- Exercises 37–44: the continued-fraction degree reduction, elimination
  of the first coefficient-dependent multiplication, canonical chain
  parameter counts, reduction modulo 2, block Horner evaluation and
  simultaneous power/geometric-sum recursion were checked. The complex
  product formulas, including the unit-modulus shear construction,
  expand correctly in their natural nonsingular cases. The monic
  integer-polynomial recursion has the stated leading operation bounds.
  In the supplementary Rabin–Winograd construction, the listed covered
  exponents are the nonconstant coefficients; the final constant can
  be adjusted separately within the stated O(sqrt(n)) overhead. The
  exact global optimality results quoted from external papers are not
  independently reproved. C0254 repairs the missing beta1 in answer 39.
- Exercises 45–56: changes of tensor coordinates, elementary rank
  bounds, sums/products, the flattening argument and the cyclic
  multiplication constructions were checked. The length-2 and length-3
  cyclic algorithms expand to the required products. Coprime-size
  composition gives the stated multiplication and addition recurrences.
  The 1008-point comparison composes the 16, 7 and 9 transforms with
  the stated costs; C0252 corrects the 1024-point comparator. The
  finite-field interpolation bound and the quadratic-to-bilinear
  reduction were read with their field assumptions. C0253 fixes the
  references in answer 50, C0255 refutes the arbitrary-matrix rank
  answer 55, and C0256 repairs the rank-of-a-sum line in answer 56.
- Exercises 57–60: zero padding and the modular FFT convolution are
  consistent with N<=4n. The support lower bound for integral
  convolution and the printed small integer realizations were checked.
  For answer 58(b), the eight products give the six consecutive
  convolution coefficients. The supplementary degree-2, degree-3
  and degree-4 realizations were checked by expressing columns as
  products of sums and cancelling diagonal terms. For example, the
  fourteen-column degree-4 scheme combines products on the subsets
  {0,1}, {0,2}, {1,2}, {0,3}, {1,4}, {0,1,3,4}, {0,2,3},
  {1,2,4}, {3,4} with the five singleton products; its nine output
  rows give exactly the pairs of indices with sums 0 through 8.
  Nussbaumer's cyclic/negacyclic split, omitted first FFT pass, bit
  reversal, inverse scaling and final folding were checked against
  the original pseudocode. The recurrence uses ceil(n/2) for the
  recursive negacyclic size, and its coefficient bounds account for
  the additional n bits. Trilinear aggregation in answer 60 was read
  with the known 2002 correction to the dimensions and index order.
- Exercises 61–67: coefficient extraction, border-rank sums and
  products, the nilpotent rank-3/border-rank-2 example, tensor powers
  and the asymptotic sum inequality were checked. Answer 64 was read
  with its official 21 December 2011 replacement: the constant and
  linear powers of the approximation variable cancel, and the
  quadratic coefficient is the required matrix-multiplication tensor.
  The 2023 updates on small border ranks are known amendments, not
  findings. In 65 the row/column sum constraints remove the unwanted
  terms. In 66 the binomial expansion and the limit absorb the
  polynomial overhead. C0257 records the indexing, identity-slice
  and approximation-order errors in 67. With those local repairs,
  the displayed tensor dimensions in its repeated-squaring argument
  agree: after deleting the final dot product, each of the first two
  dimensions is 3333, so the replacement dot product has size
  10000-2*3333=3334.
- Exercises 68–74: the explicitly open optimization and rational
  tensor-rank questions were reviewed as research questions. The
  division-removal construction uses series with unit constant pivots,
  and the characteristic-polynomial construction has the stated
  quartic leading cost. Their exact-count inconsistencies are C0259.
  Reverse differentiation gives the first-derivative result, but the
  last sentence about all second derivatives is refuted in C0258;
  that note also records the first y subscript typo. The bounded-
  coefficient Fourier lower bound is understood in determinant
  magnitude. The unimodular substitution in 74 preserves the stated
  integer-independence property and removes one multiplication; the
  printed one-multiplication example expands to both required forms.

The seven new findings from this exercise block are C0253–C0259;
C0252 was found in the preceding block and propagates into answer 53.
All have original-page evidence and separate English argument notes.
The official errata were screened across the four third-edition
lists, current TeX and the older second-edition list. In particular,
the known question-56 index typo, question/answer-60 dimensions,
question-67 parenthesis and answer-64 replacement are excluded from
new finding cards.

Specific limits retained with this review: cited optimality theorems
in 37, 40–42 and 44; the full exceptional-parameter analysis behind
the almost-everywhere Motzkin construction in 39; published prime and
primitive-root lists in 57; the external coding-theoretic asymptotic
constant and its long decimal expansion in 58; optimized transform
tables in 53 beyond their displayed composition arithmetic; the last
decimal digits of the limiting exponent in 67; current solutions of
the research problems in 68 and 72; and historical priority or every
original bibliographic source. These are explicit external or research
exceptions, not unread portions of the printed argument. No claim is
made to have solved an open problem or reproduced a benchmark.

The complete §4.6.4 reading now consists of this note,
`bookwise-polyeval-main-2026-11-10.md`, and the accepted earlier notes
`polyeval-basic.md`, `polyeval-adapt.md`, `polyeval-chains.md`, and
`polyeval-small-bounds.md`. The next new text is §4.7, printed 525.
