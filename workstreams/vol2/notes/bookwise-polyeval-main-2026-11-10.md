# Polynomial evaluation: remaining exposition and exercises 8–17

10 November 2026. Newly read the original exposition on printed pages
497–515 and exercises 8–17 with their answers on 699–701. This continues
the earlier reviews of pages 485–496 and exercises 1–7,18–36; it does
not yet close exercises 37–74. Ambiguous formulas were checked against
page images, including the matrix and tensor displays on 500,507,509,
511–512 and the original FFT answer on 700–701.

The determinant recurrence and its operation totals, both matrix
multiplication identities, the recursive counts, the Fourier indexing,
and the interpolation/divided-difference algorithms were checked.
The secret-sharing argument uses distinct nonzero evaluation points
and uniform independent coefficients, as intended in the text. The
barycentric interpolation formula has an already published correction
on page 504; the distinct-point restriction on page 505 is explicit.

The bilinear-form definition, realizations, index permutations and
flattening lemma are consistent. The displayed convolution algorithms
follow the stated polynomial remainder identities, including their
5-multiplication/15-addition and 7-multiplication/17-addition counts
when the first input is precomputed. Theorem W's proof correctly
reduces the lower bound to a nonsingular matrix from at most q rows:
each irreducible factor excludes at most one scalar when supports are
combined. The infinite-field hypothesis is stated. The upper bound
uses interpolation within each primary factor and the Chinese
remainder formula. The rational/real/complex examples on page 514
have the stated factor counts.

For exercises 8–17, the factorial-power nesting, Ryser cancellation,
subset recurrence, inverse transform, divided differences and equally
spaced interpolation all agree with the answers. The permanent counts
follow by counting the nonempty Gray-code subsets and adjacent subset
layers, respectively. Research exercises 11–12 are read as research
questions; their cited bounds and historical records are external
results, not newly proved or updated here.

One new discrepancy was found: answer 14's radix-four FFT count is
two too large under the answer's explicit convention. See
`C0252-fft-count.md` for the short counterexample and corrected count.
The radix-two count, inverse formula, and real-input conjugacy check
are sound. The wrong `C8` reference in answer 16 is already corrected
to `T8` in the 2001 errata and is not a new finding.

Exact scope limits: the cited lower-bound and optimality theorems on
497,499,501,514 and answer 12 are accepted as named external results;
their source proofs have not been independently reconstructed. The
historical benchmarks and crossover sizes on 501, historical priority
claims, and the source-level claim about numerical stability of
barycentric interpolation are not independently replicated. Equations
with divisions by small integers are read in their ordinary rational,
real or complex setting, not as an unstated algorithm for every small
finite field. No open complexity problem is being solved.

All relevant historical/current official errata were consulted. Known
changes to Hadamard–Walsh attribution, interpolation, matrix-rank
records and references are excluded from new findings. Later exercises
and answers sharing these pages retain their separate coverage status.
