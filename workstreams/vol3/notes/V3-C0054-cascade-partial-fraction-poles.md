# V3-C0054 — The partial fractions invert the pole locations

Confirmed in volume 3, second edition, first printing (1998), answer
5.4.3-8, printed p.685, file p.696. The answer expands the rational
generating function `A(z)=q_3(z)/(q_4(z)-z)` by summing over the roots
rho of `q_4(rho)=rho`. It uses the factor `1-rho*z`; this should be
`1-z/rho`.

For a simple denominator root rho, the contribution is

```
q_3(rho) / (rho (1-q_4'(rho))) * 1/(1-z/rho).
```

This follows directly by matching the residue at z=rho. The printed
factor instead locates its pole at z=1/rho.

The error cannot be removed by permuting the roots. All eight roots
listed on p.296 have magnitude at most 2, so the printed right-hand
side is analytic for |z|<1/2. But A(z) has a genuine pole at
`rho=2 sin(pi/22)<1/2`; the numerator does not vanish there. Thus the
two rational functions cannot agree.

The main formula (12) on p.296 already has the correct factor, so the
cascade coefficient formulas and growth ratio are not refuted.
The original pages were visually checked and retained as
`images/bookwise-p685.png` and `images/bookwise-p296.png`. The five
official errata layers were screened in `sources/cascade-errata-review.json`;
targeted public searches found no matching correction. No absolute
priority claim is made.
