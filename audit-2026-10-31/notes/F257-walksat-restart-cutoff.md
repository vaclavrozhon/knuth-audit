# F257 — The twelve-variable WalkSAT example uses the cost of a different cutoff

**Location:** Volume 4B, first edition, second printing (November 2022),
answer 7.2.2.2–305, printed page 608, file page 628; the paragraph beginning
with the twelve-variable calculation. The September 23, 2015 author draft,
Pre-Fascicle 6A, has the same numbers on printed page 244, file page 252.
Both original page images have been inspected.

The stated cutoff of eight flips gives approximately **12.3**, rather than
16.1, flips in total before success. Alternatively, changing the cutoff to
twelve preserves the printed 16.1. This is a numerical error in the example;
it does not invalidate WalkSAT or the general restart formula.

## Short verification from the paragraph itself

Let `p_t` be the probability that one independently initialized run first
succeeds after exactly `t` flips. Its probability generating function is
`g(z) = sum_t p_t z^t`; runs that never succeed contribute no coefficient.
Put `q = g(1)` and `d = g'(1)`. Thus `q` is the success probability, while
`d` is the probability-weighted number of flips in successful runs. When
all successful runs finish by a cutoff `N`, the expected total number `L`
of flips under independent restarts satisfies

```text
L = d + (1-q)(N+L),
L = (d + N(1-q))/q.
```

The paragraph gives `q ≈ .51`, `d ≈ 2.40`, and `N = 8`. These values imply
about 12.3 flips, far from 16.1. The book's preceding four-variable example
uses this same definition of cost and the same restart formula correctly.
Initialization costs are counted separately in both examples.

## Exact confirmation

The clauses are `not x_j or x_k` for every ordered pair `j != k`, together
with `not x_1 or not x_2`. Algorithm W chooses a uniformly random false
clause and, with greed avoidance zero, a uniformly random variable of
minimum break count in that clause. A variable's break count is the number
of currently true clauses that its flip would make false.

Permutations of the first two variables and of the remaining ten variables
preserve both the clauses and this transition rule. Consequently the pair
`(a,b)`, counting true variables in these two groups, gives an exact chain
with 33 states. Its initial state has probability
`binomial(2,a) binomial(10,b) / 4096`. The script computes transitions
directly from the clauses, removes states from which success is unreachable,
and obtains the following finite success polynomial:

```text
g(z) = 1/4096 + (3/1024)z + (33/2048)z^2 + (55/1024)z^3
     + (495/4096)z^4 + (99/512)z^5 + (18753/151552)z^6
     + (49/49152)z^7 + (245/606208)z^8.

q = 116471/227328       = 0.5123477970...
d = 4363123/1818624     = 2.3991341806...

L(8)  = 11457971/931768 = 12.2970213615...
L(12) = 15005395/931768 = 16.1042180028...
```

The number of initializations remains `1/q ≈ 1.95`. The printed 16.1 is
therefore explained by charging twelve flips, rather than eight, to each
failed run. This identifies a plausible source of the mistake without
claiming knowledge of the author's computation.

As controls, the same clause-based computation reproduces the entire
printed four-variable polynomial and its `1577/382` restart expectation.
An exact rational solve also reproduces all seven positive-noise figures
in the twelve-variable paragraph. No random simulation or large census
was used; the check takes less than one second locally.

## Sources and status

- [Verification script](../check_focused_walksat305.py)
- [Exact results](../results/focused-walksat305.json)
- [Original page 608](../../integration/2026-11-17-focused-4b/sources/vol4b-p608.png)
- [Author draft page 244](../../integration/2026-11-17-focused-4b/sources/fasc6a-answer305.png)
- [Current source retrieval](../../integration/2026-11-17-focused-4b/sources/retrieval.json)
- [Focused source check](../results/focused-walksat305-sources.json)

The official short and complete errata for Volume 4B and Fascicle 6, plus
their TeX sources, were refreshed on November 17, 2026. They match the
archived files and contain no matching correction. The nearby 2017
corrections concern answer 304 and do not fix this paragraph. Focused
public searches found no matching report. This establishes neither
absolute priority nor the state of every later printing. The physical
printed book has not been checked, and no report has been sent.
