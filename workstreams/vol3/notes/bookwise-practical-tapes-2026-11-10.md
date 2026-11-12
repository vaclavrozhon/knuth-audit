# Bookwise review: practical tape merging, 10 November 2026

Reviewed §5.4.6, printed pp.317–343, all sixteen exercises and answers
on pp.692–694. Shared pages 343 and 694 continue into external radix
sorting and are deferred to the next certification block.

Checked the MIXT density, transfer, gap and delay model, the forecasting
algorithm and both parts of its buffer-availability proof. The required
order of the full-output and empty-input tests, P=1 adjustment, and
consistent equal-key tie breaking were read with answers 2–5. The
2P-1-buffer counterexample is consistent with the full/partial buffer
count used in the proof.

Read the ten merge schedules, their memory allocations and the
approximate timing formulas. Checked dimensional consistency, the
separation of distribution, intermediate and final passes, the source
of the replacement-selection run counts, and the use of copy savings
to estimate rewinds. These are estimates within the historical MIXT
model, not exact runtime identities. The heapsort overlap schedule
keeps the newly read blocks separate from the shrinking old heap.

Answer 6's changes to Algorithm C use the added free tape and reverse
all T+1 tape labels after a pass; this resolves the forward reference
from §5.4.3-13. Answer 7 was read with the three official corrections
to its dummy-run distribution and merge string. The Markov transition
matrices, Q=1 and Q=2 generating functions, Q=3 coefficient, and the
column operation in answer 15 were checked. The claimed asymptotic
coefficient uses the usual finite-state Markov argument in addition
to the displayed determinant factorization; no new general theorem
was proved here.

No new finding. In particular, p.341's denominator p_1 must be
p_{>=1}, but that correction is already official (30 April 2008).
Other known corrections include example 8's reference to example 5,
the example-10 schedule, N in the final-pass time, and typographical
changes to the buffer and date-format discussions.

Limits: the full foldout Chart A timelines, historical simulations,
efficiency plots and all numerical timing totals were not independently
reproduced. The main-text schedules, model and printed derivations
were reviewed. Answer 12(a)'s necessity/sufficiency assertion for
3P+3 buffers is not supplied with a full proof and was not independently
proved; its lookahead-key alternative is queued for §5.4.9. The complete
dummy-placement optimum in exercise 7 and the empirical crossover
ranges were not independently optimized. Exercise 16's large
simulation study was not performed. The stochastic buffer model is
explicitly approximate; it is not a correctness claim about every merge.

Source screen: `sources/practical-tapes-errata-review.json`.
Next: §5.4.7, printed p.343 / file p.354.
