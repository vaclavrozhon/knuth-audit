# F264 — The bounded-occurrence construction uses about 6m variables

**Location:** Volume 4B, first edition, second printing (November 2022),
answer 7.2.2.2–204(c), printed page 587, file page 607, final line.
The printed estimate `N ≈ 7m + 30` should be `N ≈ 6m + 30`.
This is a counting error; the reduction and its linear-size conclusion
remain valid.

## Count directly from the construction

Here `m` is the number of original ternary clauses, and `N` is the number
of variables in the transformed instance. Part (a) introduces one variable
for each original literal occurrence, giving `3m` variables. Part (b)
adds its separate forcing gadget on 35 variables:

- `a_i, ..., h_i` for `i = 1, 2`: 16 variables;
- `A, ..., E`: 5 variables;
- `F_1, ..., F_7, G_1, ..., G_7`: 14 variables.

Part (c) extends the last two families. For each integer
`j = 7, ..., ceil(3m/2) + 3`, it adds two clauses and two fresh variables,
`F_(j+1)` and `G_(j+1)`. Thus, for `m >= 2`, this extension introduces
`2 ceil(3m/2) - 6` variables. Padding the binary clauses with the resulting
false literals introduces no further variables. Consequently,

```text
N = 3m + 35 + 2 ceil(3m/2) - 6
  = 3m + 2 ceil(3m/2) + 29
  = 6m + 29  when m is even,
    6m + 30  when m is odd.
```

In particular, `N/m` tends to 6, not 7. This is not a rounding issue.
For example, when `m = 10`, the construction uses 30 occurrence variables,
35 gadget variables, and 24 extension variables, for a total of 89.

The neighboring clause bound is correct: the construction has at most
`4m + 44 + 2 ceil(3m/2) - 6` clauses, which is `7m + 38` or `7m + 39`.
The leading coefficient 7 belongs to that count, rather than to the
variable count. No additional algorithmic or satisfiability defect is claimed.

## Edition and source review

The [original page image](../../integration/2026-11-17-focused-4b/sources/vol4b-p587.png)
was inspected together with the question on printed page 334.
The author's [Fascicle 6 errata source](https://www-cs-faculty.stanford.edu/~knuth/err4f6.textxt)
contains the same construction and the same incorrect variable estimate
in the replacement for answer 204(b,c,d), dated April 26, 2019. That entry
introduces the present solution; it does not correct this counting error.
The older September 2015 draft has a different construction and is not
evidence for the present numerical claim.

The six short/complete errata layers for Volume 4B and Fascicles 5 and 6,
and their three current TeX sources, were checked. No correction to this
count was located. Focused public searches found no matching report.
This does not establish absolute priority or verify every later printing.
See [the source-check record](../results/focused-bounded204-sources.json)
and [the current retrieval record](../../integration/2026-11-17-focused-4b/sources/retrieval.json).
No computation or publication was needed.
