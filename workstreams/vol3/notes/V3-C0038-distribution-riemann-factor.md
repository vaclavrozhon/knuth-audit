# V3-C0038 — A Riemann sum is missing its bin-count scale

Confirmed, low. Volume 3, second edition, first printing (1998),
answer5.2.5-18, printed p.652 / file p.663, final line.

The proof partitions [0,1) into cN bins and defines b_k as the supremum
of the density f on bin k. It then asserts that sum(b_k) approaches
N times the integral of f, which is N. The bin width is 1/(cN), so
the correct normalization is

```
(1/(cN)) * sum_{k=0}^{cN-1} b_k -> integral_0^1 f(x) dx = 1,
```

or `sum b_k = cN + o(N)` for fixed positive c. The omission is visible
even for the constant density f=1: each b_k is1, so the sum is exactly
cN. Taking the book's c=1/8 and N divisible by8 gives N/8, not N.

The preceding estimate is T_k=O(b_k/c); hence summing it still gives
O(N) after inserting the missing factor. The error is local and does
not invalidate the asymptotic linear-time conclusion for a fixed
bounded Riemann-integrable density.

The original page was inspected and saved in `images/bookwise-p652.png`.
The1999 erratum repairs a different displayed line earlier in this
answer. All five freshly matched errata layers were checked in
`sources/distribution-errata-review.json`, with no matching change to
the last line. Targeted public searches found no corresponding report;
absolute priority and later physical printings remain unverified.
No computation was necessary.
