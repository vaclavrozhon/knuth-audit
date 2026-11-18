# C006 — Misplaced minus sign in the exponential modulus

**Location:** Volume 4B, first edition, second printing (November 2022),
answer 7.2.2.1–189(a), printed page 469, file page 489. The same error
appears in the December 19, 2019 replacement answer in the Fascicle 5
errata, under page 277.

For a complex number `z = x + i y`, where `x` and `y` are real and
`i^2 = -1`, the second identity in part (a) should be

```text
|exp(-exp(z))| = exp(-exp(x) cos(y)).
```

The printed right side is `exp(exp(-x) cos(y))`: the minus sign is
inside the inner exponential instead of before it. At `z = 0`, the
left side is `exp(-1) = 1/e`, whereas the printed right side is `exp(1) = e`.
More generally, the modulus identity `|exp(w)| = exp(Re(w))`, where
`Re(w)` denotes the real part, gives the corrected formula immediately.

This is a local formula error. The subsequent estimates use the intended
negative exponent; the principal asymptotic conclusion is not refuted.
F021 concerns two different expressions in part (c), and F022 concerns
the later factorial. Neither already records this identity in part (a).

## Why the classification changed

Earlier notes established the mathematical discrepancy but retained C006
as a candidate, because it would amend an already published erratum.
That was too conservative: the published replacement itself contains
the erroneous formula and is reproduced in the 2022 book. It is not a
published correction of this misplaced minus sign. C006 is now confirmed,
with its existing identifier preserved; this is a reassessment of an
existing candidate, not a newly discovered discrepancy.

The [original book page](../images/gould189-192-original-489.png) and
[typeset errata page](../images/gould189-192-errata5-14.png) were inspected.
The [current official TeX source](https://www-cs-faculty.stanford.edu/~knuth/err4f5.textxt)
still has the same expression. No correction to it was found in the six
short/complete errata layers for Volume 4B and Fascicles 5 and 6, their
three current TeX sources, or focused public searches. These checks do
not establish absolute priority or cover every later printing.

See [the source-check record](../results/focused-modulus189-sources.json)
and [the source retrieval record](../../integration/2026-11-17-focused-4b/sources/retrieval.json).
No computation was rerun, and nothing was published or sent.
