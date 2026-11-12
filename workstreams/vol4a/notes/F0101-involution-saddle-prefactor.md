# The involution saddle prefactor is missing sqrt(e)

Volume 4A, first edition, first printing (2011), Answer 7.2.1.5–51, intermediate asymptotic expansion,
printed page 774, file page 791.

The positive saddle sigma satisfies sigma^2+sigma=n+1. Consequently

```
exp(g(sigma)) = exp((n+1+sigma)/2) / sigma^(n+1).
```

Gaussian integration of the immediately preceding integral therefore gives numerator `n!*exp((n+1+sigma)/2)`. The next display instead has `n!*exp((n+sigma)/2)`, losing the constant factor sqrt(e). Since the following correction factor tends to 1, it cannot absorb this discrepancy.

The final expansion in powers of n^(-1/2) is correct. A short expansion of the corrected prefactor and b1 reproduces its coefficients 7/24, -119/1152, and -7933/414720; see `../results/involution-prefactor-targeted-algebra.json`. The error is confined to the intermediate display.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-probability-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
