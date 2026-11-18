# C048: The cited prime-number error bound has the wrong exponent

Confirmed November 17, 2026, as a misstatement of the cited result.
This does **not** claim a counterexample to the stronger asymptotic assertion.
The candidate ID is retained. The previous assessment below is historical.

On p. 388 (PDF p. 408), in the notes after MPR 113, define
`psi(n) = ln(lcm(1,...,n))`, the sum of `ln(p)` over prime powers
`p^k <= n`, with each power counted once. The book and the September 11,
2019 author draft, p. 45, both print

```
psi(n) = n + O(n exp(-C log n)),  C > 0 constant,
```

and attribute this to de la Vallée Poussin's 1896 article. For any fixed
base of `log`, this is an error of order `n^(1-delta)` for some fixed
`delta > 0`. It is substantially stronger than the cited historical result.

Two original scans now resolve the source question:

1. *Recherches analytiques sur la théorie des nombres premiers*, first
   part, reprinted in 1897 from the 1896 article, p. 62 (PDF p. 71),
   explicitly says that the rate of the remainder's convergence is not
   established, and that convergence slower than every negative power
   has not been excluded. This is in section 52, before the ensuing
   prime-number asymptotics.
2. *Sur la fonction zeta(s) de Riemann et le nombre des nombres premiers
   inférieurs à une limite donnée* (1899), p. 6 (PDF p. 19), explicitly
   distinguishes the new quantitative estimate from the earlier result.
   Section 55, p. 54 (PDF p. 67), gives the prime-power sum with a
   logarithmic prefactor times `exp(-sqrt(p ln x))`, where the source's
   constant `p` is approximately 0.03282. Here `p` is a constant in the
   bound, not the prime summation variable. Section 47, p. 47 (PDF p. 60),
   defines the prime-power sum. Its strict upper endpoint instead of
   `<= n` changes at most `ln n` and has no effect on this estimate.

Consequently, a suitable correction is

```
psi(n) = n + O(n exp(-c sqrt(log n))),  c > 0 constant,
```

with a reference to the 1899 paper. The logarithmic prefactor can be
absorbed by decreasing the positive constant in the exponent. Alternatively,
the book can retain the 1896 reference and use the simpler
`psi(n) = n + o(n)`, which suffices for the following growth conclusion.
The combinatorial argument in MPR 113 is unaffected.

Original scans: [1896/1897 reprint](https://archive.org/details/recherchesanaly00pousgoog)
and [1899 paper](https://archive.org/details/surlafonctionze00pousgoog).
Downloads, hashes and the inspected page images are recorded in
`results/focused-prime113-sources.json` and
`../integration/2026-11-17-focused-4b/sources/vallee-originals-retrieval.json`.
The original book detail and author draft images were rechecked. Fresh
official 4B/F5/F6 errata and available public searches supplied no matching
correction or prior report; absolute priority is not established.

## Previous candidate assessment

Candidate only. TAOCP4B p388/file408, notes following MPR113.
The original PDF and the author's Pre-Fascicle5A p45/file51 both
print ψ(n)=n+O(n exp(−C log n)) for a positive constant C.
There is no square root in either source.

November 17 source follow-up: a download advertised as the collected
works, volume 1, is only a 16-page scanned front-matter extract. Its
contents locate the 1896 first part at collected pp. 223–296, but the
article itself is absent. It is archived under
`integration/2026-11-17-focused-4b/sources/vallee-poussin-collected-vol1.pdf`
and must not be cited as having supplied the original theorem. The
candidate decision is unchanged.

For any fixed logarithm base, the printed expression is a fixed
power saving O(n^(1−δ)) for some δ>0. A change of logarithm base
cannot explain the difference from a square-root exponent.

The primary comparison source, Trudgian's arXiv:1401.2689v2,
Theorem1 on p3, bounds |ψ(x)−x| by
x sqrt(8/(17π)) X^(1/2) exp(−X), where
X=sqrt((ln x)/6.455), for x≥23. Its exponential scale is
exp(−c sqrt(ln x)); it does not establish the printed stronger bound.

This is not a counterexample to the stronger statement. No proof of
its falsehood is claimed, and no finite calculation can by itself
settle an asymptotic bound with unspecified constants. A missing
square root is a plausible intended correction, pending assessment
of the intended theorem and the cited historical source.

The six local errata layers and three TeX sources contain no
applicable correction. The historical1896 article has not been
fully assessed. The complete exercise remains partial specifically
for this mathematical note; its combinatorial parts, the Θ(n)
growth bounds and the exact LCM value are independently proved.

Evidence: `sequential-mpr-ex113.md`, original images `ref-408.png`,
`mpr113-notes-detail.png`, `fasc5a-51.png`, and the saved primary
paper `sources/trudgian-2014-pnt.pdf` with image `trudgian-2014-03.png`.
