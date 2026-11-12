# Volume 2: power series

Reviewed 10 November 2026: all printed text of §4.7, pages 525–537,
exercises 1–28 and their paired answers 719–725. The added 2024
exercise 29 is accepted from the detailed `series-determinant.md`
review, including the already confirmed C0231. No previous verifier
or determinant computation was rerun.

The convolution, reciprocal and arbitrary-power recurrences follow
from the displayed product and derivative identities. Leading terms
are normalized before reversion. The update order in Algorithms L
and G divides the already known coefficients by the input series
before obtaining the next coefficient from Euler's recurrence. The
Catalan example gives the printed rows and outputs 1,1,2,5,14.
Algorithm T uses only previously completed columns when computing
each new power coefficient; it also handles U1=0 as advertised.
Algorithm N's residual and derivative quotient produce precisely
the next block of coefficients. Its signs, truncation orders and
input/output ranges were checked against the original typesetting.

The conjugation formulas for iteration and the Brent–Traub recursion
were checked, including the transformed coefficient W*(z/U)^n and
the residual sign. The n scalar base problems have the stated
nonresonant denominators. The tangent-to-identity case was read with
the two auxiliary algorithms of answer 14: the first removes a
leading power from the composition equation, and the second solves
a first-order coefficient recurrence. Linearizing the residual in
the correction z^(k+n) P_hat gives the displayed equation on 722.
The zero-multiplier formula has the geometric exponent
(k^n-1)/(k-1), as required by repeated composition. Fixed-point
translation is read in its natural setting where the indicated
expansion about that fixed point exists, not for arbitrary divergent
formal series at a nonzero argument.

The exercise answers were followed through integer-scaled division,
exponential/logarithmic recurrences, generalized Lagrange inversion,
composition, reversed polynomial division and the Euclidean Padé
construction. The four displayed rational approximations have the
stated first coefficients. Power-matrix multiplication, the two
poweroid convolution identities, Bell-polynomial recurrence and
the inversion duality agree with coefficient extraction. An apparent
problem in 21(b) was rejected: the original question explicitly
divides by V1^n before claiming polynomial dependence on n; OCR had
lost that normalization.

The logarithm of a unit triangular power matrix is locally finite,
and exponentiating it gives the stated formal iteration law. The
generator's entry formula, its commutation recurrence, the first
displayed generator coefficients and the chain-of-indices formula
in 23(e) were checked. The nonresonant case of exercise 24 is read
under the main text's explicit nonzero-multiplier assumption; the
matrix logarithm is not asserted to cover U1=0. The commuting-series
argument in 25 compares the first differing coefficient. The mod-2
composition algorithm uses squaring to split even and odd parts.
The q-product recurrence in 27 follows from its displayed functional
identity. The Dirichlet-series recurrences in 28 use the additive
prime-factor count as a derivation; their divisor indices and initial
values agree with the power-series analogues.

New findings are C0260 (reversed exponent in the elementary iterate),
C0261 (missing constant-term normalization in the induced-series
proof), and C0262 (the extra online composition route requires V1!=0,
with an accompanying loop-index typo). All have original-page
evidence, concise corrections and English cards. Known corrections
to the Lagrange proof in answer 16, the older answer-14 derivative,
power branches on 526 and other editorial changes were applied or
explicitly excluded from the new findings. The added exercise 29
was compared with the current unchanged errata text; its prior
determinant-factor finding is retained.

Explicit review limits: the external Brent–Kung, Ritzmann and
Kung–Traub speedups are accepted as cited algorithms rather than
reimplemented; the saddle-point asymptotic quoted in the note after
answer 17 is not independently certified outside its source's
analytic hypotheses; and historical priority, complete original
bibliography and source-level epigraph verification are not claimed.
The displayed algorithms, coefficient arguments and paired exercises
have been read. No new computation was needed for this block.
