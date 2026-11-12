# A power of v disappears from the Jacobi calculation

Volume 4A, first edition, first printing (2011), Answer 7.2.1.4–23, second equality,
printed page 750, file page 767.

The answer converts the quotient

```
(v^choose(n,2)-v^choose(n+2,2))/(1-v)
```

into `sum(v^k, k=0,...,2n)`. The correct expression is that sum multiplied by **v^choose(n,2)**.

For n=2 the quotient is `(v-v^6)/(1-v)=v+v^2+v^3+v^4+v^5`, whereas the printed replacement is `1+v+v^2+v^3+v^4`. Since this n is the unique term with u-exponent choose(3,2)=3, summing over n cannot repair the error. The subsequent instruction to set v=1 removes the missing factor, so the desired Jacobi identity remains valid.

The June 18, 2010 replacement answer in the historical Fascicle 3 errata, printed errata page 13, contains the same error; it is not a correction of this missing factor. Its original typesetting was also inspected.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/partition-counting-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
