# The scaled factorial approximation has the wrong correction

Volume 4A, first edition, first printing (2011), Answer 7.2.1.5–40, final correction factor,
printed page 771, file page 788.

For a fixed positive constant c, the coefficient of z^(n-1) in exp(cz) is exactly c^(n-1)/(n-1)!. Its asymptotic expansion, obtained either from equation (21) or from Stirling's formula, is

```
e^n (c/n)^(n-1) / sqrt(2*pi*n) * (1 - 1/(12*n) + O(n^-2)).
```

The answer instead multiplies the same leading factor by `1+n/12+O(n^-2)`. That multiplier diverges, whereas the correct multiplier tends to 1. The saddle point and the preceding local expansion in this answer are correct.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-saddle-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
