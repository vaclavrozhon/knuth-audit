# The second moment and variance of forest path length are misstated

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–54, second display and final sentence, printed 795.

Let S=c_1+...+c_n be the total internal path length of an n-node forest, and let C_n be the nth Catalan number. Exercise 46 gives C_n(x)=sum_F x^S. Thus C_n''(1)=sum_F S(S-1), whereas the answer equates it to sum_F S^2.

The printed closed expression

```
((5n^2+19n+6)/6)*binom(2n,n) - (1+3n/2)*4^n
```

is the factorial second moment. For n=2 the two forests have S=0 and S=1; their squared values sum to 1, while this expression is 0. To obtain the raw second moment, add the correct first-moment sum already given in the answer, 4^n/2-(3n+1)C_n/2.

Writing R=4^n/C_n and dividing these sums by C_n gives the exact variance

```
Var(S) = (10n^3+21n^2+14n+3)/12 - R^2/4.
```

The Catalan asymptotic R=sqrt(pi)*n^(3/2)*(1+9/(8n)+O(n^-2)) then gives Var(S)=(5/6-pi/4)n^3+O(n^2). The printed (5/6-pi/4)n^(3/2)+O(n) has the wrong order. The stated mean sqrt(pi)*n^(3/2)/2+O(n) is correct. A short symbolic simplification checked the exact variance algebra; no tree census was used.

Original typesetting inspected. No matching repair was found in the historical/current Volume 4A errata, refreshed Fascicle 4 errata or targeted public searches; see `../sources/tree-counting-source-check.json`. Absolute novelty is not established.
