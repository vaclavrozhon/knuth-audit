# F160 — arbitrary predictable widths do not give the printed Azuma bound

Confirmed mathematical discrepancy, medium severity, in Volume 4B,
printed p. 9 (file 29), the sentence after (38) allowing a_n and b_n
to be arbitrary functions of the previous observations. The fixed-width
bound (37) is valid. The unrestricted extension is false.

Use this three-atom probability space, with Y0=0:

| probability | Y1 | Y2 | a2 | b2 | sum of squared widths |
|---:|---:|---:|---:|---:|---:|
| 1/2 | 1 | 0 | −1/4 | 1/4 | 17/4 |
| 3/10 | −1 | 2 | −3 | 2 | 29 |
| 1/5 | −1 | −3 | −3 | 2 | 29 |

In every row a1=−1 and b1=1. Both second-step endpoints are functions
of Y1, and both intervals have strictly positive width. All atoms have
positive probability; all variables are bounded.

We have EY1=0. Conditional on Y1=1, Y2=0. Conditional on Y1=−1,
Y2 takes values 2 and −3 with probabilities 3/5 and 2/5, so its mean
is also zero. This is a fair sequence. It may be continued with zeros
after time 2, if an infinite sequence is wanted.

For x=1 the first two rows meet Y1+Y2≥1, hence

```
P(Y1+Y2≥1) = 1/2 + 3/10 = 4/5.
```

The displayed right-hand side of (37), with the allowed predictable
endpoints substituted, equals exp(−8/17) on the first row and
exp(−2/29) on the other two. In particular it is not even a fixed
number, and the proposed inequality fails on the first row. This is
a positive-mass failure, not a choice of version on a null event.

Even interpreting the intended extension as an *average* of those
exponentials cannot repair it. Positive Taylor terms give

```
exp(−8/17) < 1 / (1+8/17+(8/17)²/2) = 289/457,
exp(−2/29) < 1 / (1+2/29) = 29/31.
```

Therefore

```
E exp(−2 / sum_k(bk−ak)²)
 = (exp(−8/17)+exp(−2/29))/2
 < 11106/14167 < 4/5.
```

All comparisons are exact rational inequalities. No numerical search,
zero-width case, or zero denominator is needed.

The correct generalization retains predictable endpoints but requires
a deterministic upper bound v on the sum of squared widths. Conditional
Hoeffding gives

```
E(exp(tYk) | past) ≤ exp(t²(bk−ak)²/8).
```

Thus Mj=exp(t sum_{k≤j}Yk − t² sum_{k≤j}(bk−ak)²/8) is a nonnegative
supermartingale with EMn≤1. If the sum of squared widths is at most
the fixed v, Markov gives P(sum Yk≥x)≤exp(−tx+t²v/8); choose t=4x/v.
For v>0 and x>0 the result is exp(−2x²/v). More generally the same
argument bounds the joint event {sum Yk≥x, sum widths²≤v}.

In particular, predictable endpoints with deterministic width bounds
bk−ak≤ck are valid with v=sum ck². The hashing and bounded-differences
applications on p. 10 have exactly such fixed width bounds, so their
conclusions do not fail. The error is the unqualified extension on p. 9.

Source checks, 6 November 2026:

- Original 4B p. 9 and the entire cited exercise 90 and answer were viewed.
- The identical extension appears in the author's Pre-Fascicle 5A,
  printed p. 9, file 15, dated 11 September 2019, also viewed.
- All six local errata layers and the three available raw TeX errata
  sources were checked. No applicable correction was found. Same-number
  hits in other sections are explicitly separated in the result file.
- The coordinator independently checked the original and the witness,
  and supplied the strictly positive-width refinement used above.

Evidence, relative to repository root:

- `audit-2026-10-31/images/sequential/file-029.png`
- `audit-2026-10-31/images/sequential/ref-040.png`
- `audit-2026-10-31/images/sequential/ref-403.png`
- `audit-2026-10-31/images/sequential/fasc5a-15.png`
- `audit-2026-10-31/sources/fasc5a-manifest.json`
- `audit-2026-10-31/results/sequential/mpr-009-090-witnesses.json`
- `audit-2026-10-31/results/sequential/mpr-009-090-errata.json`

A physical printing and priority of the report were not verified.
No report was sent. Only file 29 is the finding location.
