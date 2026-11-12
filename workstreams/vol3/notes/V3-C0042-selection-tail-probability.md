# V3-C0042 — The selection proof uses a false tail bound

Confirmed in volume 3, second edition, first printing (1998), answer
5.3.3-24, printed pp.664–665, file pp.675–676. The proposed sampling
scheme has a failure probability much larger than the proof claims.

Let n tend to infinity through even integers, and set the target parameter
t=n/2. The sample consists of the first n elements of a uniformly random
permutation of 2n distinct elements. In the book's notation, its lower
pivot u has sample rank

```
r = t_- = floor(n/2 - sqrt((n/2) ln n)).
```

Let S be u's rank among all 2n elements, and put

```
T = T_- = floor(n - sqrt(n ln(2n))),
s = T + 1,
d = s - 2r.
```

The event S>T is explicitly one of the failures asserted on p.664 to
have probability O(n^(-1-epsilon)), for some positive epsilon. The final
bound on p.665 is O(n^(-1.2) sqrt(ln n)). Both are false.

Indeed, the correct probability formula printed on p.664 gives

```
Pr(S=s) = binom(s-1,r-1) binom(2n-s,n-r) / binom(2n,n).
```

Here s=n+O(sqrt(n ln n)) and

```
d = (sqrt(2)-1) sqrt(n ln n) + O(sqrt(n)/sqrt(ln n)).
```

For L of order n and z=O(sqrt(n ln n)), Stirling's formula yields the
uniform central-binomial estimate

```
binom(L,L/2+z)
  = 2^L sqrt(2/(pi L)) exp(-2z^2/L + o(1)).
```

Apply it to the two numerator factors, first using
binom(s-1,r-1)=(r/s)binom(s,r). Their offsets from their midpoints are
-d/2 and d/2. Since r/s tends to 1/2, division by binom(2n,n) gives

```
Pr(S=s) = (1+o(1))/sqrt(pi n) * exp(-d^2/n + o(1))
        = n^(-1/2-(sqrt(2)-1)^2+o(1))
        = n^(-0.671572875...+o(1)).
```

This single admissible value s>T already contradicts both asserted
upper bounds. There is no need to estimate the entire tail. The
exponential bound attributed to Stirling on p.665 is too strong.

The five local probability evaluations in
`results/selection-tail-local-probabilities.json` corroborate this
calculation; they are not the proof. For example n=1,000,000 gives
r=497371, s=996191, and Pr(S=s) approximately 0.0000690141.

Impact: the displayed probabilistic induction is invalid as written.
This does not refute the section's final comparison-complexity bound.
A valid replacement analysis or modified sampling parameters are needed;
no replacement algorithm is claimed here.

Original pages were visually checked and are saved as
`images/bookwise-p664.png` and `images/bookwise-p665.png`. The five
applicable official errata layers were screened on 10 November 2026;
see `sources/minimum-selection-errata-review.json`. The first-edition
addition dated 13 September 1996 already contains this same tail argument,
so it is not a correction of the issue.

Related public discussion: K. C. Kiwiel, *Improved randomized selection*
(2004), [arXiv:cs/0402005](https://arxiv.org/abs/cs/0402005), pp.1–2 and
12–13, criticizes the precision and practical sampling costs of Knuth's
scheme and studies an emulation of its gap choice. That discussion does
not identify the false probability estimate established above. Its PDF
and text were retained in `sources/kiwiel-2004-improved-selection.*`.
Targeted public searches found no report of this specific calculation;
this is not a claim of absolute priority.
