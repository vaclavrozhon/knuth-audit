# The derivative bound has a sign and power error

Volume 4A, first edition, first printing (2011), Answer 7.2.1.5–56(c), first inequality chain,
printed page 776, file page 793.

The printed chain is

```
n!*(1-beta/alpha) < (-sigma)^n*g^(n+1)(sigma) < 0.
```

Its left endpoint is positive because 0<beta<alpha, so the chain is impossible. It also lacks a power of sigma. Parts (a) and (b) give the correct statement directly: if

```
S = sum(A(n,k)*alpha^k*beta^(n-k), k=0,...,n),
```

where A(n,k) is an Eulerian number, then `(-sigma)^(n+1)*g^(n+1)(sigma)=n!-S` and `(beta/alpha)*n!<S<n!`. Therefore

```
0 < (-sigma)^(n+1)*g^(n+1)(sigma) < n!*(1-beta/alpha).
```

Together with the subsequent inequality `1-beta/alpha<2*(1-beta)`, this proves the desired main-text derivative bound (42).

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-probability-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
