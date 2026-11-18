# F260: Newton's inequalities were proved before Sylvester's 1865 paper

**Location:** TAOCP Volume 4B, first edition, second printing (November
2022), answer MPR26, printed page 374, file page 394. The same historical
sentence appears in the September 11, 2019 Pre-Fascicle 5A, printed page
31, file page 37. Both original page images were inspected.

The answer attributes the eventual proof of Newton's coefficient
inequalities to Sylvester in 1865. Maclaurin's 1729 paper already gives
a proof covering the coefficients used here. Sylvester's cited paper
concerns a stronger rule for counting nonreal roots. The inequality and
the mathematical proof in the answer are unaffected.

## The earlier result is the relevant inequality

In Maclaurin's notation, let `n` be the degree of the polynomial and
let `D, E, F` be three adjacent coefficients, with `E` multiplying
`x^(n-r)`. Proposition IX and its corollary, on pp. 69–70 of his paper,
give the coefficient comparison with factor

```text
[r/(r+1)] [(n-r)/(n-r+1)] E^2 >= D F.
```

Here the non-strict sign includes equal-root limiting cases; the
historical prose says that the left side exceeds the right side.
On p. 68, Corollary I supplies nonnegative expressions for real roots
of the same sign. Proposition IX combines these expressions to prove
the displayed comparison. Its corollary explicitly identifies the
factors in Newton's rule. This is not merely the different chain of
inequalities now commonly called Maclaurin's inequalities.

To compare it with MPR26, let `p_i` be the success probability of trial
`i`, for `1 <= i <= n`, and let `c_k` be the coefficient of `z^k` in

```text
Q(z) = product_i (1-p_i + p_i z).
```

Thus `c_k` is the probability of exactly `k` successes. For probabilities
strictly between zero and one, all roots of `Q` are real and negative,
so Maclaurin's same-sign hypothesis suffices. His comparison becomes

```text
[k/(k+1)] [(n-k)/(n-k+1)] c_k^2 >= c_(k-1) c_(k+1).
```

Writing `r_(n,k) = c_k / binom(n,k)` gives exactly
`r_(n,k)^2 >= r_(n,k-1) r_(n,k+1)`, the inequality named at the start of
the answer. Endpoint probabilities follow by continuity. This
identification does not require any claim about the first proof in all
possible historical formulations: a proof in 1729 already refutes the
claimed wait until 1865.

## What Sylvester proved

The cited Proceedings paper is reprinted as article 84 in volume II of
Sylvester's *Collected Mathematical Papers*, pp. 498–513. Its first two
pages state upper bounds for the numbers of positive and negative roots
using signs of normalized coefficients and their adjacent quadratic
differences. On p. 508 Sylvester explicitly distinguishes this counting
rule from the earlier result that a negative quadratic difference
implies the existence of nonreal roots. The latter, by contraposition,
is the coefficient inequality for polynomials with only real roots.

The attribution in the book therefore conflates the coefficient
inequalities with the stronger root-counting result. A minimal repair
is to cite Maclaurin (1729), pp. 68–70, for the earlier proof. Sylvester
can still be cited separately for the stronger rule.

## Primary sources and status

- Colin Maclaurin, *A Second Letter ... Concerning the Roots of
  Equations, With the Demonstration of Other Rules in Algebra*,
  Philosophical Transactions 36 (1729), 59–96,
  [original scan](https://archive.org/details/jstor-103506),
  [DOI](https://doi.org/10.1098/rstl.1729.0011).
  Printed pp. 68–70 are file pp. 11–13; all three images were inspected.
- J. J. Sylvester, *On an Elementary Proof and Generalization of Sir
  Isaac Newton's Hitherto Undemonstrated Rule for the Discovery of
  Imaginary Roots*, Proceedings of the London Mathematical Society 1
  (1865–1866), 1–16;
  [collected-papers scan](https://archive.org/details/SylvesterCollected2).
  Reprint pp. 498, 499, and 508 are file pp. 515, 516, and 525;
  all three images were inspected.
- [Original book page](../../integration/2026-11-17-focused-4b/sources/vol4b-p374-newton.png)
  and [author draft](../../integration/2026-11-17-focused-4b/sources/fasc5a-p31-newton.png).
- [Focused source record](../results/focused-newton26-sources.json).

The current short and complete Volume 4B, Fascicle 5, and Fascicle 6
errata and the relevant TeX sources contain no located correction of
this attribution. Focused public searches found no matching report.
This does not establish absolute priority. A physical copy and every
later printing have not been inspected. The exact Newton 1707 page
reference was not independently checked; it is not part of this finding.
No report has been sent.
