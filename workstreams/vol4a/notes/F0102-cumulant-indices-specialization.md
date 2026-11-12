# The cumulant formula reverses the Stirling indices

Volume 4A, first edition, first printing (2011), Answer 7.2.1.5–52, cumulant formula and final note,
printed page 774, file page 791.

Let S(j,k) be a Stirling number of the second kind, B_j the Bell number, and kappa_j the jth cumulant. The displayed expansion of log G(exp(t)) correctly has terms `(exp(t)-1)^k*xi^k/k!`. Extracting j! times the coefficient of t^j gives

```
kappa_j = exp(xi) * sum(S(j,k)*xi^k, k=1,...,j),  j>=1.
```

The following formula instead uses S(k,j). For j=1 and xi=1/2, the printed sum is exp(1/2), twice the correct mean exp(1/2)/2. For xi>=1 it even diverges.

The final bracketed note also claims kappa_j=e*B_j when xi*exp(xi)=1. At j=1 that condition makes the mean 1, not e. The intended specialization is **xi=1**. Case (b)'s separate generating function does yield kappa_j=B_j; its opening notation, printed as “kappa = j = B_j”, should likewise read kappa_j=B_j. These corrections preserve the two probability distributions and their generating functions.

The last sentence's error bound is handled separately as another occurrence of F0100. The normalizing factor there is correctly typeset as 1/(sigma*sqrt(2*pi)); sigma is outside the radical.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-probability-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
