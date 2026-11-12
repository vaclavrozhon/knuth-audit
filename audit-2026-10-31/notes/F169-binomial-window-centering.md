# F169 — Missing centering in the binomial-window probability

Status: confirmed locally; low severity. This is a local proof typo.
The exercise and its final classification remain correct.

Location: Volume4B p384, answer MPR96, the probability immediately
after the local binomial-coefficient estimate; original file404.
The author's Pre-Fascicle5A of11September2019 has the same text
on p41/file47. Both original pages were viewed directly.

The exercise defines X as the number of heads in n fair independent
coin flips. The answer later prints

```
Pr(|X| < sqrt(n)) = Theta(1).
```

X has not been redefined as a centered variable. For every n≥16,
sqrt(n)≤n/4 and X≥0, so the established fair-binomial tail bound gives

```
Pr(|X| < sqrt(n)) ≤ Pr(X ≤ n/4) ≤ exp(−n/8) → 0.
```

This contradicts the positive eventual lower bound required by
Theta(1). It is an exact asymptotic contradiction, without a simulation.

Replace `|X|` by `|X−n/2|`. The companion complete exercise note proves
the corrected central-window estimate by exact binomial ratios and
the previously established integral bounds for the central coefficient.
It also supplies a positive-probability annulus outside the window,
which explicitly proves that part(iv) is not asymptotically almost sure.
The corrected Theta(1) central estimate alone should not be mistaken
for that separate conclusion.

All four requested classifications are proved in
`notes/sequential-mpr-ex095-097.md`: (i) quite sure and asymptotically
almost sure; (ii) and(iii) asymptotically almost sure but not quite sure;
(iv) neither. No change to the question on p20 is needed.

The six local current/cumulative errata layers and all three TeX
sources were checked with page, answer-number and content searches;
`results/sequential/mpr-095-097-tails-errata.json` records their hashes
and the unrelated matches. No applicable correction was found in
those snapshots. This does not claim a live refresh or historical priority.

Only file404 is an error location. The valid question and referenced
Volume1 tail bounds must not be marked as errors. No independent
coordinator acceptance is asserted by this local record.
