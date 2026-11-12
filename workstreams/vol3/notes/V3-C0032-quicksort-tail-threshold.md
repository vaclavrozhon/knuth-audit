# V3-C0032 — The Quicksort tail threshold can be below its deterministic minimum

Confirmed, medium. Volume 3, second edition, first printing (1998),
exercise 5.2.2-42, printed p. 137 / file p. 148. The answer on p. 636
only refers to Karp's theorem; it does not supply a proof of the printed bound.

Here H_n = sum(1/k, k=1,...,n) is the nth harmonic number, and C is
the number of key comparisons in the partition phases of Algorithm Q.
The exercise claims, for every real c > 0,

```
Pr(C > (c+1)(N+1) H_N) < exp(-c).
```

Take the permitted cutoff M = 1, N = 63 distinct keys, and c = 1/20.
Every input requires at least 320 partition comparisons. But the printed
threshold is

```
(21/20) * 64 * H_63 = 317.739468729... < 320.
```

Consequently the left side is 1, whereas the proposed upper bound is
exp(-1/20) = 0.9512294245... . Including the final insertion pass only
increases the number of comparisons, so it cannot remove the contradiction.

To justify the deterministic minimum without enumerating inputs, let d(n)
be the least partition comparison count for n distinct keys with M = 1.
The book's partition analysis gives

```
d(0) = d(1) = 0,
d(n) = n+1 + min(d(s-1) + d(n-s), 1 <= s <= n),  n >= 2.
```

Write lg for the base-two logarithm. Induction gives
d(n) >= (n+1)(lg(n+1)-1). Indeed, for the two child weights a=s and
b=n+1-s, the induction step reduces to
a lg(a) + b lg(b) >= (a+b) lg((a+b)/2), by convexity of x lg(x).
The bases n=0,1 satisfy the inequality. For n=63 this lower bound is 320,
and balanced splits attain it: the five nontrivial levels each cost 64.
The short exact-rational calculation in
`../results/quicksort-tail-counterexample.json` also evaluates the finite
recurrence through 63 and the threshold. No permutation census was run.

The problem is substantive for the printed probability statement, not an
issue with strict versus non-strict inequalities or a rare input. It is
consistent with a missing factor of two in the threshold: the mean
partition cost is asymptotic to 2N ln(N), rather than N ln(N).
This report does not certify a replacement bound for every cutoff convention.

Source check: the original page is saved as `../images/bookwise-p137.png`.
All five author errata layers were freshly retrieved on 2026-11-10 and
match the archive; see
`../../../integration/2026-11-10-bookwise/errata/vol3-manifest.json`.
The first-edition supplement's addition of exercise 58 on p. 139
(14 September 1996) already contains the same threshold. Subsequent
corrections to p. 137 concern exercises 41 and 49, not this one.
Targeted public searches for the exercise, Karp, and a correction found
no matching report. This does not establish absolute priority or the
state of every later physical printing.

The publisher's [Karp article](https://doi.org/10.1145/195613.195632)
was identified, but its PDF was unavailable through the tool (HTTP 403).
The author-hosted [Tassarotti paper, Theorem 2 and the Quicksort example
on p. 10](https://cs.nyu.edu/~jt4767/papers/probrec/draft.pdf)
states the Karp bound using (c+1) times the **expectation** and gives the
usual mean with leading coefficient two. It supports the diagnosis;
the finite counterexample above is independent of that external theorem.
