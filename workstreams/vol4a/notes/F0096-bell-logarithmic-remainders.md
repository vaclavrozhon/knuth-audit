# The simplified Bell estimates omit terms larger than their remainders

Volume 4A, first edition, first printing (2011), Equations 7.2.1.5–(29) and (30),
printed page 423, file page 440.

Let B_n denote the Bell number and let xi be the positive solution of xi*exp(xi)=n. Thus xi tends to infinity like log n. Let b1 be equation (27)'s coefficient and b1prime the coefficient in exercise 45. Combining the preceding expansions with Stirling's formula gives the following terms of order 1/n in the logarithms:

```
log B_(n-1): (b1 + 1/12)/n,
log B_n:     (b1prime + 1/12)/n.
```

Equations (29) and (30) replace both terms by -xi/(12n). The omitted amounts are respectively

```
xi*(11*xi^2+32*xi+26) / (24*n*(xi+1)^3),
-xi*(xi^2+4*xi-2) / (24*n*(xi+1)^3).
```

Their products with n tend to 11/24 and -1/24. Consequently neither can be absorbed in `O((log n/n)^2)`, as printed. Keeping the exact terms `(b1+1/12)/n` and `(b1prime+1/12)/n` repairs the estimates with that error bound. Alternatively, the simpler displayed expressions are valid with remainder O(1/n).

The ratio estimate (31) remains valid: `b1-b1prime=xi*(xi+2)/(2*(xi+1)^2)` is bounded. A short symbolic simplification of these specific coefficients is recorded in `../results/bell-asymptotic-targeted-algebra.json`. The known 2018 correction changes a later cross-reference from (29) to (26), not these formulas.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-saddle-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
