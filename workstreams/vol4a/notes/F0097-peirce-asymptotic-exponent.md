# The Peirce estimate uses k instead of k-1

Volume 4A, first edition, first printing (2011), Answer 7.2.1.5–46, first formula,
printed page 772, file page 789.

Let w_(n,k) be the entries of Peirce's triangle, B_n its first entry in row n, and xi the positive solution of xi*exp(xi)=n. Equation (13) expresses w_(n,k) as a sum involving binomial coefficients of order k-1. Together with (31), it gives, for fixed k,

```
w_(n,k) = (1-xi/n)^(k-1) B_n (1+O(1/n)).
```

The answer prints exponent k. Already for k=1, w_(n,1)=B_n exactly, while the printed approximation has relative discrepancy asymptotic to xi/n, which is not O(1/n). For k=2, the exact relation is w_(n,2)=B_n-B_(n-1), so the first-order factor is 1-xi/n, not its square.

The later statement for k=n uses the much weaker relative error O((log n)^2/n); this particular change of exponent does not invalidate that weaker estimate.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-saddle-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
