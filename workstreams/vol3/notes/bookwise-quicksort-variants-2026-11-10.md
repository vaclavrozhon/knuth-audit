# Quicksort variants and paired exercises

Reviewed the random-pivot continuation on pp. 121–122, the median,
samplesort and introspective variants on p. 122, exercises 28–32, 41–42,
55–56 on pp. 136–138, and their answers on pp. 632–636, 638–639.
The core, extremes and exercises 17–27 were already accepted in X0091;
the previously reserved P1076–P1088 inventory expansion is unnecessary
under the current printed-argument standard.

Checked the pivot move and scan sentinel, median rank probabilities,
the finite-difference and generating-function steps of 28–29, multikey
partition invariants and increasing common-prefix length in 30, the
one-branch selection recurrence and boundary terms in 31–32, the five
regions and cleanup indices of 41, and the six median order cases,
partition endpoints and recurrence solutions in 55–56. The type in
answer 41 is `b <= c`, not the strict comparison suggested by OCR.
Answer 53's later decimal example uses p = phi^(-1), not p = 0.1.

A concrete suspicion that the fixed three sample positions invalidate
the exact comparison recurrence in 28 was checked with a short, nice-15
implementation of Q2–Q6 for M=2. For n=3,...,8 the exact averages were
4, 5, 42/5, 57/5, 516/35, 183/10, agreeing with the recurrence.
This check is evidence against the suspicion, not a proof of a universal
statement. No new finding is retained on that point.

The new finding **V3-C0032** refutes the probability threshold in exercise
42 with N=63, M=1, c=1/20: the threshold is below the deterministic
minimum. The existing C0012 (reciprocal leading constant in 29) and
C0015 (negative exchange count at M=2 in 56) are retained without
duplicate cards. The new source/argument note gives the precise scope.

Known corrections were applied, not counted as findings: the reference
58 -> 42 on p. 122; excluding sample-median comparisons in 28; the left
endpoint `l` in 41; the two harmonic indices in answer 32; Dijkstra's
chapter number; M>1 in 55; and the qualified sentinel remark in answer55.
The current official errata match the archive (fresh manifest under
`integration/2026-11-10-bookwise/errata/vol3-manifest.json`).

Explicit exceptions: the quoted historical performance percentages and
samplesort measurements were not reproduced. The external proofs of
samplesort's asymptotic bound and the optimized historical program
benchmarks are accepted as cited results, not newly proved here. The
introspective worst-case bound follows from the stated depth cutoff
and the subsequent heapsort bound; its practical average-time comparison
is not an independently reproduced measurement. The numerical tail
claim on p.122 is not independently established by the erroneous
exercise42 threshold. Karp's general theorem is not reproved; the
finite counterexample does not question that theorem. No search for
globally optimal median code or cutoff was undertaken.

Whole-page certification waits for the radix material sharing these pages.
Next: radix exchange, pp. 123–134 and exercises33–40,45–54; the earlier
detailed bubble asymptotics and exercises43–44 are reused.
