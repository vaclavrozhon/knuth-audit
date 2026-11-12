# Bookwise review: two-tape sorting, 10 November 2026

Reviewed §5.4.8, printed pp.348–356, all ten exercises and answers
on pp.694–696. Shared pages 356 and 696 continue into disks and drums
and are deferred to the next certification block.

Checked the order-P bubble-sort inversion argument, the buffer-size
optimization with the official square-root correction, and the two-stack
quicksort subroutines. The original SORT01 copies keys <= K; OCR loses
the equality sign, so there is no missing-pivot defect. The X_N/Y_N
recurrences count the two pivot transfers and extra lower-part copy
consistently. Their closed forms in answer 2 have the correct starting
values and leading coefficient 20/3.

Read the radix variants and the Hennie–Stearns zone simulation,
including its geometric scan-cost sum and overwrite requirement.
The bounded-internal-memory discussion is consistent with the model
intended by the tape-reversal sketch in §5.4.4-18, but does not supply
a full proof of that sketch's path-count premise. That limitation is
retained rather than replaced by a new lower-bound proof.

Checked Karp's elevator algorithm with its balance identities,
direction-change condition and the weaker extremal-passenger invariant
used in the proof. An upward move reduces ceil(u_k/m) by one without
increasing ceil(d_{k+1}/m); a downward move reduces ceil(d_k/m) by one.
The component splicing and unequal floor-capacity extension preserve
the stated crossing bounds. The answer-5 counterexample concerns the
stronger invariant, not the one used in the theorem. The ternary-word
bijection in answer 8 has inverse determined by the signs of a_k-k;
its generating function and closed form agree.

No new finding. Existing C0027 remains a low-severity candidate about
whether a final verification pass is counted in the cocktail-shaker
formula. This section does not resolve that convention and does not
justify upgrading it to a confirmed error. The already reviewed
threshold argument for first becoming sorted is reused.

Limits: historical runtime estimates and the external simulation
theorem were not independently reproduced. Answer 3's linear-time
two-tape selection/merging constructions remain at the supplied sketch
level. Exercise 7's free-tree transport research problem was not solved.
The lower-bound arguments use the intended fixed internal-memory
record model; no broader encoding model was independently formalized.

Source screen: `sources/two-tapes-errata-review.json`.
Next: §5.4.9, printed p.356 / file p.367.
