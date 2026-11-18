# F265 — The relaxed product construction has two more clauses per y bit

**Location:** Volume 4B, first edition, second printing (November 2022),
answer 7.2.2.2–411, printed page 632, file page 652, third line.
For the construction actually specified, `9mn - 5m - 10n` should be
`9mn - 5m - 8n`. Here `m` and `n` are the bit lengths of the two factors,
with `2 <= m <= n` as in the referenced multiplication construction.

## Direct count

Answer 41 on printed page 556 gives `mn` initial AND gates,
`mn - m - n` full adders, and `m` half adders. A half adder combines two
input bits into a sum bit and a carry bit. A full adder does the same
for three input bits. Answer 410 specifies their gate-by-gate relaxation:

| Operation constrained | Clauses |
| --- | ---: |
| `t >= u AND v` | 1 |
| `t >= u XOR v` | 2 |
| `t >= u OR v` | 2 |
| Half adder: one AND and one XOR | 3 |
| Full adder: two ANDs, two XORs, one OR | 8 |

Thus the clause count before the final comparison is

```text
mn + 8(mn - m - n) + 3m = 9mn - 5m - 8n.
```

The smallest example already distinguishes the two formulas. For `m=n=2`,
the construction has four partial-product AND gates and two half adders,
giving `4 + 2*3 = 10` clauses; the printed formula gives 6. Explicitly,
if `x=(x2 x1)` and `y=(y2 y1)` are the binary inputs, the relaxed gates are

```text
w1 >= x1 AND y1       a >= x1 AND y2
b  >= x2 AND y1       d >= x2 AND y2
w2 >= a XOR b        c >= a AND b
w3 >= d XOR c       w4 >= d AND c.
```

The six AND constraints contribute six clauses and the two XOR constraints
contribute four. These are distinct clauses; no constants were substituted.

Adding the stated `3m + 3n - 2` comparator clauses gives
`9mn - 2m - 5n - 2`, still below `9mn`. This count correction does not
repair the separate semantic defect in the full-adder relaxation,
documented in [F236](F236-relaxed-full-adder.md). The two-bit example
contains no full adder, so the present counting error is independent.

## Edition and source review

The original images of [answer 411](../../integration/2026-11-17-focused-4b/sources/vol4b-p632-product-count.png)
and [answer 41](../../integration/2026-11-17-focused-4b/sources/vol4b-p556-product-gates.png)
were inspected. The September 23, 2015 Fascicle 6 draft, printed page 268,
file page 276, contains the same incorrect formula. The official
[October 8, 2022 correction](https://www-cs-faculty.stanford.edu/~knuth/err4b.textxt)
on page 632 concerns answer 410 and does not correct this count.

No matching correction was found in the six short/complete errata layers
for Volume 4B and Fascicles 5 and 6, their three current TeX sources, or
focused public searches. This does not establish absolute priority or
verify every later printing. See the [source-check record](../results/focused-product411-sources.json).
No mathematical computation or publication was needed.
