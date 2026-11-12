# The Bell-period hint raises g_j to the wrong power

Volume 4A, first edition, first printing (2011), Exercise 7.2.1.5–24, definition in the hint,
printed page 434, file page 451.

The hint defines `g_j(x)=(x^p-x-1)^(p^j)` and claims that the falling factorial of length p^e is congruent to g_e(x)+1 modulo the stated polynomial ideal. The power in the definition must be **p^(j-1)**.

For p=3 and e=1 the claimed polynomial congruence reduces to

```
x(x-1)(x-2) = (x^3-x-1)^3+1  (mod 3).
```

Its left side is x^3-x modulo 3, whereas its right side is x^9-x^3. These are different polynomials over the field with three elements. The surrounding argument uses polynomial congruences, not just agreement on the three field elements.

With the corrected exponent, g_1=x^p-x-1 and the base congruence is the standard falling-factorial identity from exercise 23(c). More generally, reduction modulo p gives x^(p^e)-x^(p^(e-1)) on both sides. This restores the indexing used by the induction in answer 24; the stated Bell-number period is unchanged.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-counting-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
