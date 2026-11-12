# The expected leftmost-leaf depth has the wrong power of two

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–53(c), printed 795.

Let X be the distance from the root to the leftmost external node. In a uniformly random degenerate binary tree, each of the first n-1 internal nodes independently continues to the left or right. Consequently P(X>=k)=2^(1-k) for 1<=k<=n, and

```
E(X) = sum_(k=1)^n 2^(1-k) = 2-2^(1-n).
```

For n=2 the two possible trees give distances 1 and 2, hence mean 3/2; the printed answer gives 7/4. The distribution p_k=2^(-k+[k=n]) printed in part (d) agrees with the corrected expectation. The identity E(2^X)=n+1 is unaffected.

Original typesetting inspected. No matching repair was found in the historical/current Volume 4A errata, refreshed Fascicle 4 errata or targeted public searches; see `../sources/tree-counting-source-check.json`. Absolute novelty is not established.
