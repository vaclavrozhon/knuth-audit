# The Bell expansion remainder needs logarithmic factors

Volume 4A, first edition, first printing (2011), Exercise 7.2.1.5–45, displayed remainder,
printed page 437, file page 454.

Let xi be the positive solution of xi*exp(xi)=n, and let b_jprime denote the coefficients in this exercise. The printed remainder after b_mprime/n^m is O(n^(-m-1)). However the coefficients depend on xi, which tends to infinity like log n.

For m=1 the next coefficient satisfies

```
b2prime = xi^2/288 + O(xi),
```

so the relative remainder after `1+b1prime/n` has leading size xi^2/(288*n^2), not O(n^-2). This is a failure at a nonempty truncation, independent of whether m=0 is intended. At m=0 the explicit b1prime is already asymptotic to -xi/12.

The leading coefficient of b2prime follows directly from answer 45: with `c_j ~ 2^(j/2)*xi^(j/2-1)/j!` and `a=-sqrt(2/(xi+1))`, a term containing k powers of a in b2prime is O(xi^(2-k)). Only k=0 contributes to xi^2, giving the same leading term as b2 in (28), namely 1/288. The short coefficient calculation is recorded in `../results/bell-asymptotic-targeted-algebra.json`.

Replacing the remainder by `O((log n/n)^(m+1))`, as in main equation (26), gives the appropriate asymptotic scale. The displayed formula for b1prime is correct.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-saddle-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.

A second occurrence is the final note in answer 52, printed page 774/file 791. For the distribution there, with xi*exp(xi)=n,

```
Pr(X=n) = B_n*xi^n/n! * exp(1-exp(xi))
        = (1+b1prime/n+O((log n/n)^2))/sqrt(2*pi*n*(xi+1)).
```

Since b1prime is asymptotic to -xi/12, the relative error of the leading Gaussian probability is of order (log n)/n, not O(1/n). The leading normalizing factor is correct: sigma lies outside the radical. This occurrence was screened with `../sources/set-partition-probability-source-check.json`.
