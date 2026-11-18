# F258 — Two incorrect sign claims in the overlap-ratio proof

**Location:** Volume 4B, first edition, second printing (November 2022),
answer 7.2.2.2–203(e), printed page 587, file page 607. The same two claims
occur in the September 23, 2015 Pre-Fascicle 6A, printed page 223, file
page 231. Both original page images were inspected. This card groups two
local defects in one paragraph; it is not a counterexample to the final
satisfiability-threshold conclusion of exercise 203.

## The sign of f(1/2)

In the exercise, `p` is the fraction of forbidden pairs in each randomly
chosen constraint, and `r` controls the number of constraints. Part (e)
chooses `epsilon = 1 + r ln(1-p)` small and positive. The answer defines

```text
f(sigma) = 2pr sigma / (1-p+p sigma^2) - 1,
```

where `sigma` is the fraction of coordinates shared by two assignments.
It then asserts that this choice of parameters implies `f(1/2) < 0`.

Take `p = 1/2` and `r = 7/5`. These are within the specified range, with
`epsilon = 1 - (7/5) ln 2 = 0.0295939472... > 0`. Direct substitution gives

```text
f(1/2) = (7/10)/(5/8) - 1 = 3/25 > 0,
f(1)   = 7/5 - 1             = 2/5.
```

The issue persists for arbitrarily small positive epsilon: keeping
`p = 1/2` and taking `r = (1-epsilon)/ln 2` gives

```text
f(1/2) = 4(1-epsilon)/(5 ln 2) - 1 > 0
```

whenever `0 < epsilon < 1 - (5/4)ln 2 = 0.133566...`. It is therefore not
a disagreement about how small epsilon should be.

In fact, for every fixed `0 < p <= 1/2`, the intended sufficiently small
epsilon regime has `f(1/2) > 0`. To check this, put
`A(p) = p/(1-3p/4) + ln(1-p)`. Then `A(0)=0` and

```text
A'(p) = p(8-9p) / (16(1-3p/4)^2(1-p)) > 0.
```

Thus `p/(1-3p/4) > -ln(1-p)`, which gives the required strict positivity
at epsilon zero and, by continuity, for sufficiently small positive epsilon.

## The sign near the pole of g

The next line defines `g(sigma) = f(sigma)/ln(sigma/(1-sigma))` to locate
changes in the direction of the sequence of overlap contributions. The
printed approximation uses the opposite paired sign in
`g(1/2 +/- 1/N)`: it puts `-/+ f(1/2) N/4` on the right.

For a real displacement `h` tending to zero,

```text
ln((1/2+h)/(1/2-h)) = 4h + O(h^3).
```

Consequently, when `f(1/2) != 0`,

```text
g(1/2 +/- 1/N) = +/- f(1/2) N/4 + O(1).
```

The signs must match. For the rational parameter choice above, the two
limits after division by `N` are respectively `+3/100` and `-3/100`,
whereas the printed formula predicts their negatives. This defect remains
even if the preceding claim about `f(1/2)` is repaired.

Correct both sign statements and adjust the accompanying root-location
discussion. The exact ratio formula at the beginning of part (e) is
consistent with these computations. No new proof of the general Model RB
threshold theorem is claimed here.

## Sources and status

- [Original page 587](../../integration/2026-11-17-focused-4b/sources/vol4b-p587.png)
- [Author draft page 223](../../integration/2026-11-17-focused-4b/sources/fasc6a-answer203.png)
- [Current source retrieval](../../integration/2026-11-17-focused-4b/sources/retrieval.json)
- [Focused source check](../results/focused-overlap203-sources.json)

The current short and complete Volume 4B and Fascicle 6 errata, including
their TeX sources, were refreshed on November 17, 2026. No corresponding
correction was located. The Fascicle 6 changes on page 223 replace answers
204 and 205, not part 203(e). Focused public searches found no matching
report; this is not a claim of absolute priority. The physical printed copy
and every later printing have not been inspected. Nothing has been sent.
