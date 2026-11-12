# V3-C0033 — A sign in the binomial-ratio expansion

Confirmed, low. Volume 3, second edition, first printing (1998),
answer 5.2.2-52, printed p. 637 / file p. 648, second line of the
displayed exponential expansion. It contains

```
-(1/(6n)) (x^2 - x^4 + ...),   where x = t/n.
```

The sign before x^4 must be **plus**. Let
R = binom(2n,n+t) / binom(2n,n) = (n!)^2/((n+t)!(n-t)!).
The 1/(12u) term of Stirling's expansion for log(u!) contributes to
log(R) exactly

```
2/(12n) - 1/(12(n+t)) - 1/(12(n-t))
  = -(1/(6n)) * x^2/(1-x^2)
  = -(1/(6n)) * (x^2 + x^4 + x^6 + ...),  |x| < 1.
```

Higher Stirling terms begin at order n^(-3) for fixed x, so they cannot
change this coefficient of n^(-1). The first two groups in the printed
exponent are correct. The error is local: at the central scale
t = O(sqrt(n)), the wrong term is too small to affect the final answer's
requested O(n^(-1)) accuracy. This report does not reject that final
divisor-sum asymptotic formula.

The original page was inspected and saved as `../images/bookwise-p637.png`.
The five author errata layers, freshly retrieved and matched to the archive
on 2026-11-10, contain corrections to nearby answers 50, 51 and 53 but
no matching change to this expansion. The relevant historical first-edition
answer pages 612–613 likewise contain no such correction. See
`sources/exchanging-errata-review.json` and the fresh manifest under
`integration/2026-11-10-bookwise/errata/vol3-manifest.json` in the repository.
Targeted public searches for Knuth, p.637, exercise52 and errata found
no matching report; absolute priority and later physical printings remain
unverified. No computation was required for the algebraic diagnosis.
