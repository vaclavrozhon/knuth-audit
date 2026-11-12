# The higher Taylor terms have the opposite sign

Volume 4A, first edition, first printing (2011), Equation 7.2.1.5–(41), sign before the sum,
printed page 425, file page 442.

The notation g^(k)(sigma) denotes the kth derivative of g at sigma. Taylor's formula is

```
g(sigma+i*t) = g(sigma) - t^2*(1-beta)/(2*sigma^2)
               + sum((i*t)^k*g^(k)(sigma)/k!, k>=3).
```

Equation (41) prints a minus before the sum, reversing every term of degree at least three. The discrepancy is nonzero in the text's example sigma=log 2, alpha=log 4, beta=log 2: here `sigma^3*g^(3)(sigma)=3*(log 2)^2-2`, which is not zero.

The normalized expansion in answer 58(b) uses the correct signs, and the displayed coefficient b1 in (44) agrees with that corrected expansion.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-probability-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
