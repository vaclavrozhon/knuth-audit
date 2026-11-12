# Bookwise review: cascade merging, 10 November 2026

Reviewed §5.4.3, printed pp.288–299, all thirteen exercises and their
answers on pp.684–685. Shared pages 299 and 685 begin backwards-tape
merging and are deferred to that next certification block.

Checked the complete-pass schedules, reverse cumulative-sum
distributions, Ferguson's dummy constraints, and Algorithm C, including
its special initialization, distribution sublevels, bypassed copies,
first-pass dummy consumption and reversal of logical tape labels. The
100-run answer is consistent with the stated stopping point and merge
weights. The known correction to the residual constraints on p.291
was applied.

Checked the polynomial recurrences for the cascade counts, their
Catalan boundary values, the finite polynomial corrections in (8),
the trigonometric form of q_m, root cancellation and the resulting
coefficient formulas. The matrix in answer 6 is symmetric and gives
the convolution identity in exercise 5. The suppressed-copy sum in
answer 7 reproduces the 25 saved run lengths in the 190-run example.
The r_m and f_m identities in answers 10–11 give the alternative
reduced generating function. Answer 8 has the pole-location typo
C0054; formula (12) in the main text is correct. The already official
2026 correction of q_m(±2) was not made into a finding.

The cascade-distribution inverse in exercise 4 uses adjacent differences
of sorted counts and preserves the gcd, unlike the incomplete
full-addition characterization in the preceding section. Its induction
works under the natural nonnegative run-count interpretation.

Limits: historical timing tables and compromise-merge numerical
comparisons were not independently reproduced. Exercise 12 gives no
printed proof of the global optimum of the distribution scheme; that
optimality claim was not independently proved. Exercise 13's scheduling
exploration is referred to §5.4.6-6 and is queued for that section.
No new proof of the cited external optimization results was attempted.

Source screen: `sources/cascade-errata-review.json`.
Next: §5.4.4, printed p.299 / file p.310.
