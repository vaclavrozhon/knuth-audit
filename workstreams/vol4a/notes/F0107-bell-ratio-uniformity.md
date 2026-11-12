# The Bell ratio estimate linearizes an exponent outside its small range

Volume 4A, first edition, first printing (2011), Equations 7.2.1.5–(50) and (51),
printed page 427, file page 444.

Let B_n be the Bell number and let xi*exp(xi)=n. Put

```
A(n,k) = k*xi*(k*xi+k+1)/(2*(xi+1)^2*n).
```

Equation (50) states `B_(n-k)/B_n=(xi/n)^k*(1+A(n,k)+O(k^3/n^2))` for k<=n^(2/3). This linearization is not valid throughout that range. Take k=floor(sqrt(n)). Taylor expansion of the already established logarithmic Bell estimate gives

```
log(B_(n-k)/B_n) = -k*xi + 1/2 + o(1).
```

Thus the ratio divided by (xi/n)^k tends to exp(1/2), whereas the printed right side tends to 1+1/2. Its claimed remainder tends to zero.

A valid, slightly conservative repair obtained by subtracting the logarithmic estimates at n-k and n is

```
B_(n-k)/B_n = (xi/n)^k * exp(A(n,k) + O((k^3+xi^2)/n^2)),
1 <= k <= n^(2/3).
```

For this deduction, the smooth leading logarithm has third derivative O(n^-2); the first rational correction changes by O(k*xi/n^2); and the retained Bell expansion has error O(xi^2/n^2). These bounds are uniform since n-k is comparable to n.

Even at k=1, the original O(n^-2) remainder is too small. The next coefficient in the normalized ratio is

```
-xi^2*(2*xi^4+2*xi^3-19*xi^2-52*xi-48)/(24*(xi+1)^5),
```

which is asymptotic to -xi/12. This follows by subtracting the next-order logarithmic expansions; a targeted simplification is in `../results/bell-ratio-targeted-algebra.json`.

The intermediate `1+O(1/n)` in (51) also treats k as fixed despite the surrounding range k<=n^epsilon. For example, at k=floor(n^(1/4)), the logarithm of the mean divided by xi^k/k! has leading term `-k^2/(2*n*(xi+1))`, exceeding O(1/n). Replacing that intermediate error by O(k^2/n) for k=o(sqrt(n)) suffices; the final weaker O(n^(2*epsilon-1)) estimate in (51) is valid.

Original typesetting inspected. Errata/public-source screening: `../sources/random-set-partition-source-check.json`.
No matching repair was found in the sources searched; absolute novelty is not established.
