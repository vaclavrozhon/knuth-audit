# V3-C0036 — The radix program excludes pile zero from its empty-pile count

Confirmed, medium. Volume 3, second edition, first printing (1998),
§5.2.5, printed pp.174–175 and answer6 on p.651. The instruction counts
and running-time formula use a different random variable from the
occupancy distribution and its stated mean.

Let E count the empty-pile tests that succeed during the p passes.
Algorithm H starts at pile0 in H2, increments the pile index in H3,
and only then tests emptiness in H4. Thus **pile0 is never tested**.
The MIX program has the same control flow: lines21–22 enter line32
for pile0; lines29–30 test only piles1 through M-1. The frequency
3M-3 of line29 confirms the exclusion.

Consequently the running time 32N+48M+38-4E for three passes is correct
when E excludes pile0. But Eq.(7) and the parenthesis in answer6 treat
E as the number of empty piles among all M piles. For N=2, M=3, use
keys (1,1,1) and (2,2,2). On each pass only pile0 is empty. The actual
E is zero, contradicting the printed minimum max(M-N,0)p=3. The
instruction counts give 246u; substituting the total empty-pile count
3 would instead give 234u. The discrepancy occurs for any input with
an empty pile0, not just this small example.

There is a compact correction. Let g_MN(z) be the probability generating
function for the total number of empty piles after N independent
uniform placements, as defined in exercise6. Ignoring pile0 is equivalent
to first occupying it with one extra fixed item. By symmetry the
resulting empty-count distribution is the same as adding one extra
uniformly placed item. Therefore the generating function for the
program's E, with independent random digit passes, is

```
g_M,N+1(z)^p,
```

rather than g_MN(z)^p. Equivalently, the one-pass polynomial is
`g_MN(z) + (1-z) g'_MN(z)/M`, by conditioning on whether pile0 is empty.
Equation(7) should become, for N>=1,

```
minimum E = max(M-1-N,0) * p,
mean E    = (M-1) * (1-1/M)^N * p,
maximum E = (M-1) * p.
```

Equation(6) is correct for total empty piles, but its use as the
distribution of E requires N+1 placements. Exercise6's own definitions,
recurrence and moments remain correct; only its final application to
Program R is wrong. For p=3 the mean running time is consequently
`32N+48M+38-12(M-1)(1-1/M)^N`.

Original pp.172,174,175,651 were inspected and saved. All five author
errata layers, freshly matched on 2026-11-10, were screened in
`sources/distribution-errata-review.json`. The known2012 correction to
the comment on line20 does not affect this issue; no matching change
to E was found. Public searches for the radix empty-pile count and
Knuth errata produced no matching report. Absolute priority and later
physical printings remain unverified. The counterexample is a direct
control-flow and frequency trace; no full MIX emulator was run.
