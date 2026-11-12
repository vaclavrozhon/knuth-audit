# The near-diagonal saddle expansion drops r+1 to r

Volume 4A, first edition, first printing (2011), Answer 7.2.1.5–61, first two sentences,
printed page 777, file page 794.

For m=n-r the definition is alpha=(n+1)/(n-r), hence

```
alpha = 1+(r+1)/n+O(r*(r+1)/n^2).
```

The answer prints 1+r/n+O(n^(2*epsilon-2)). For the useful regime 0<epsilon<1/2 and r<=n^epsilon, the omitted 1/n is larger than that remainder. The same shift is lost in beta and N=(n+1)*(1-beta).

For example take r=1 and epsilon=1/4. Then alpha=1+2/n+O(n^-2), beta=1-2/n+O(n^-2), and N=2+O(n^-1). The answer instead predicts alpha=1+1/n+O(n^-3/2) and N=1+O(n^-1/2). The separate boundary computation in answer 59 is consistent with the corrected +1.

Uniform expansions with r+1 in place of r repair these intermediate steps. The final leading estimate in exercise 61 has an additional O(1/r) relative allowance and is unaffected by this shift; its fixed-r explanation is also consistent with the combinatorial leading term.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-probability-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
