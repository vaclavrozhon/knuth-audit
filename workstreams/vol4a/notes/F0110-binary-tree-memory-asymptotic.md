# The second term in Algorithm B's memory estimate

Volume 4A, first edition, first printing (2011), answer 7.2.1.6–44,
printed page 793, file page 810, final equality.

Let C_n be the nth Catalan number. The answer gives the total memory cost as

```
C_(n+1) + 4*C_n + 2*(C_(n-1)+...+C_1) + O(n)
  = (26/3 - 10/(3*n) + O(n^-2))*C_n.
```

The coefficient -10/3 is inconsistent with the preceding expression. Equation
(20), printed page 450, gives

```
(C_(n-1)+...+C_1)/C_n = 1/3 + 2/(3*n) + O(n^-2),
C_(n+1)/C_n = (4*n+2)/(n+2) = 4 - 6/n + O(n^-2).
```

The latter identity follows immediately from the Catalan formula (15). Therefore
the correct cost is `(26/3 - 14/(3*n) + O(n^-2))*C_n`. The additive O(n)
term is exponentially small after division by C_n and cannot account for the
discrepancy. The leading 26/3 and the efficiency claim in the main text survive.

Both original pages were inspected. The historical/current Volume 4A errata,
the refreshed Fascicle 4 errata and targeted public searches yielded no matching
repair; see `../sources/tree-basics-source-check.json`. Absolute novelty is not
established.
