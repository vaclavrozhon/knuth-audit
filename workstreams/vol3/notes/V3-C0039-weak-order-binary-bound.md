# V3-C0039 — A binary lower bound is applied to ternary comparisons

Confirmed, medium. Volume 3, second edition, first printing (1998),
answer 5.3.1-11, printed p.655 / file p.666.

Here S_m(n) is the minimum worst-case number of comparisons needed to
sort n keys drawn from m ordered values, including discovery of all
equalities. A comparison has the three outcomes less, equal and greater,
as specified by exercises 5 and 11. Let Q_m(n) be the number of possible
weak orderings, where a weak ordering records both order and ties. Then

```
Q_m(n) = sum_{k=1}^m StirlingSecondKind(n,k) * k!.
```

The answer asserts `S_m(n) >= ceil(lg Q_m(n))`, with lg denoting the
base-two logarithm. This is false. For m=2 and every n>=2,

```
Q_2(n) = 2^n - 1,
ceil(lg Q_2(n)) = n,
S_2(n) = n - 1.
```

The last equality is proved immediately above in answer 9: compare
the first key with every other key. With only two possible values,
the comparison outcomes determine all equivalence classes and their
order; the all-equal input requires n-1 comparisons. At n=2 this is
simply one ternary comparison distinguishing three weak orderings,
whereas the printed lower bound demands two comparisons.

Counting leaves of a ternary tree gives the valid elementary bound
`S_m(n) >= ceil(log_3 Q_m(n))`. Substituting this bound does not prove
the asymptotic assertion in exercise 11. The printed upper bound also
does not close that gap for general fixed m. This finding refutes the
displayed lower bound and the supplied proof; it does not claim to
determine the correct sharp asymptotic for every m.

The original pages 194 and 655 were inspected; the latter was also
rendered at higher resolution to verify the ceiling and the base of
the logarithm. Saved images: `images/bookwise-p194.png` and
`images/bookwise-p655.png`. All five errata layers in
`sources/minimum-sorting-errata-review.json` were checked, together with
targeted public searches for this exercise and page. No matching
correction was found. Absolute priority and later physical printings
remain unverified. No computation was needed.
