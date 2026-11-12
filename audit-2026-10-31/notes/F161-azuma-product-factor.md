# F161 — the product in answer 90(e) has a factor-of-two error

Confirmed local proof discrepancy, low severity, in Volume 4B,
answer MPR 90(e), printed p. 383 (file 403). The desired exponential
moment bound and the final Hoeffding–Azuma inequality remain true.

Part (d) establishes factors of the form

```
exp(ck²t²/8) + Yk hk(t),   ck=bk−ak.
```

Part (e) defines c=(c1²+···+cn²)/2 and asks for the moment bound
exp(ct²/4). But its printed answer uses the product

```
(exp(c1²t²/4)+Y1 h1(t)) ··· (exp(cn²t²/4)+Yn hn(t))
```

and identifies its constant term with exp(ct²/4). The constant term
of this displayed product is actually

```
exp((c1²+···+cn²)t²/4) = exp(ct²/2).
```

For a concrete nondegenerate instance take n=1, t=1, a1=−1/2,
b1=1/2 and Y1=±1/2 with probability 1/2 each. Then c1=1 and c=1/2.
The expectation of the printed factor is exp(1/4), because EY1=0.
The claimed constant is exp(1/8), strictly smaller. Everything is
finite and both atoms have positive probability.

Replace `/4` by `/8` in each individual factor of the product. Their
constant term then is exp(sum ck² t²/8)=exp(ct²/4), exactly as needed.
The final `/4` in exp(ct²/4), and the optimization in part (f), should
remain unchanged. This is separate from the unrestricted predictable
width claim on p. 9, recorded as F160.

With fixed widths, cancellation of the other terms is valid: in any
nonempty product of Yk hk, take its largest index j. All other factors
are measurable with respect to the past before Yj, so conditioning
on that past kills the term because E(Yj|past)=0. The corrected
individual upper bounds are positive, hence they can be multiplied
before expectations are taken. Equivalently one can apply the
conditional moment bound successively without expanding the product.

Source checks, 6 November 2026:

- The whole original question on p. 20 and answer on p. 383 were viewed;
  the two individual displayed factors both have denominator 4.
- The same product and final constant appear in the author's
  Pre-Fascicle 5A, printed p. 40, file 46, also viewed.
- Six local errata layers and three raw TeX sources contain no applicable
  correction. The historical answer 90 changes on Fascicle 5 p. 243
  concern a different exercise about word puzzles.
- The coordinator independently checked both original pages and the
  factor-of-two calculation.

Evidence, relative to repository root:

- `audit-2026-10-31/images/sequential/ref-040.png`
- `audit-2026-10-31/images/sequential/ref-403.png`
- `audit-2026-10-31/images/sequential/fasc5a-46.png`
- `audit-2026-10-31/sources/fasc5a-manifest.json`
- `audit-2026-10-31/results/sequential/mpr-009-090-witnesses.json`
- `audit-2026-10-31/results/sequential/mpr-009-090-errata.json`

A physical printing and priority of the report were not verified.
No report was sent. Only file 403 is the finding location; neither the
exercise statement nor the valid fixed-width main-text bound is marked.
