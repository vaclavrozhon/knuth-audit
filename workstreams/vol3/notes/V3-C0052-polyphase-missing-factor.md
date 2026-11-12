# V3-C0052 — The polynomial recurrence omits a factor x

Confirmed in volume 3, second edition, first printing (1998), §5.4.2,
printed p.276, file p.287, the unnumbered display between (15) and (16).

A_n(x) counts initial runs by their number of later merges on the first
tape, and T_n(x) sums the corresponding polynomials over all five input
tapes. Every term contributed by the previous level acquires one extra
merge. Summing the five identities in (13) therefore gives

```
T_n(x) = x(5 A_(n-1)(x) + 4 A_(n-2)(x) + 3 A_(n-3)(x)
           + 2 A_(n-4)(x) + A_(n-5)(x)).
```

The printed display omits the outer factor x. Already at n=1 it gives
T_1(x)=5, whereas each of the five initial runs is merged once, so
T_1(x)=5x. The following generating function (16) and coefficient table
(17) include the correct factor; this is a local recurrence typo.

Original p.276 was visually checked and retained as
`images/bookwise-p276.png`. The five official errata layers were screened
in `sources/polyphase-errata-review.json`. A targeted public search found
no matching correction; absolute priority is not asserted.
