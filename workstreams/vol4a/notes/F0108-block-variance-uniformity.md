# The block-count variance error is not uniform in block size

Volume 4A, first edition, first printing (2011), Answer 7.2.1.5–65, final asymptotic estimate,
printed page 778, file page 795.

Let X_k count the blocks of size k in a uniformly random partition of an n-element set. Put xi*exp(xi)=n and lambda=xi^k/k!. The exact formula in the answer is correct:

```
mu = E(X_k) = (n falling k)/k! * B_(n-k)/B_n,
E(X_k*(X_k-1)) = (n falling 2k)/(k!)^2 * B_(n-2k)/B_n,
Var(X_k) = mu + E(X_k*(X_k-1)) - mu^2.
```

The following rate, `Var(X_k)=lambda*(1+O(n^(4*epsilon-1)))`, is not uniform over the nearby main-text range k<=n^epsilon. Set k=floor(xi), which satisfies that range for every fixed positive epsilon and large n. Expanding the exact moments with the repaired Bell ratio gives

```
E(X_k*(X_k-1))/mu^2
 = exp(-k^2/(n*(xi+1)) + O(xi^3/n^2)),
mu/lambda = 1+O(1/n).
```

Stirling's formula at k=floor(xi) gives `lambda ~ n/(xi*sqrt(2*pi*xi))`. Consequently

```
Var(X_k)/lambda = 1 - 1/sqrt(2*pi*xi) + o(1/sqrt(xi)).
```

For example epsilon=1/8 would require error O(n^-1/2), much smaller than this logarithmic discrepancy. The leading Poisson-scale statement Var(X_k)~lambda remains valid; its claimed rate needs a fixed-k qualification or a covariance term. No large numerical census was used.

Original typesetting inspected. Errata/public-source screening: `../sources/random-set-partition-source-check.json`.
No matching repair was found in the sources searched; absolute novelty is not established.
