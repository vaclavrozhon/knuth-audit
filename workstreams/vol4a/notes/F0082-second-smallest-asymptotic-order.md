# The second-smallest-part estimate has the wrong exponent

Volume 4A, first edition, first printing (2011), Answer 7.2.1.4–50(f), first estimate,
printed page 755, file page 772.

Let p(n) count partitions of n, P(z) be its generating function, and G_k(z) count partitions whose second-smallest part is at least k. Part (e) defines `G_k(z)=F_(k+1)(z)/(1-z)`, where F_j counts nonempty partitions with smallest part at least j.

Part (f) claims `[z^n]G_k(n)/p(n)=O(n^(-k/2))` for k<=5. In addition to the argument typo G_k(n), the asymptotic exponent is incorrect.

For k=1, every partition except the single-part partition has a second-smallest part at least 1. Equivalently,

```
G_1(z)=((1-z)P(z)-1)/(1-z)=P(z)-1/(1-z),
[z^n]G_1(z)/p(n)=1-1/p(n) -> 1.
```

It cannot be O(n^(-1/2)). The correct fixed-k order is `O(n^(-(k-1)/2))`: for example G_2 gives coefficient p(n)-p(n-2)-1, whose ratio is asymptotic to 2C/sqrt(n), where C=pi/sqrt(6). In general `G_k(z)=P(z)*product(1-z^j,j=2,...,k)-1/(1-z)`, and the book's ratio expansion gives leading term `k! C^(k-1) n^(-(k-1)/2)` for fixed k. The subsequent conclusion c(m)/p(m)=1+O(m^(-1/2)) is consistent with this repaired estimate. No explicit finite threshold for the later all-m bound is asserted here.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/partition-counting-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
