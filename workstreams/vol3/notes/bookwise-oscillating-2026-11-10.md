# Bookwise review: oscillating sort, 10 November 2026

Reviewed §5.4.5, printed pp.311–317, its five exercises and answers
on pp.691–692. Shared pages 317 and 692 continue into practical tape
merging and are deferred to that next certification block.

Checked Sobel's cyclic distribution, radix-counter algorithm in
answer 1, the perfect-power pass count, and the early finish in answer 2.
Read Algorithm B with its nominal run lengths, dummy suffixes,
level transitions and recursion-induction sketch. The small examples
and the nine-run endgame illustrate the stated transfers. The redundant
assignments in answer 4 and the parity condition in answer 5 agree
with the control structure.

In answer 3, the unchanged variable s in B7 initially looked suspect.
It is not a demonstrated defect: promotion when s'-s is odd moves
q by (-1)^s, whereas demotion when it is even moves q by -(-1)^s.
Both therefore move q by -(-1)^s'. The intervening writes are to the
row being discarded; the retained lower row receives s'+1 explicitly.
No finding was created from this concern.

Checked the read-forward Goetz example with its preserved unused
short run and cyclic distribution order. In the S=18 example the
remaining real input in phase 9 goes to T3; T2 retains its existing
short run, and T4, T5 and T1 receive dummies. Thus the accompanying
description is consistent. The known phase-5 head-position typo
and the ten, not eleven, dummy runs in exercise 2 are excluded.

No new finding. Limits: the recursive correctness discussion remains
at the printed sketch level; no independent full invariant proof or
exhaustive implementation test was added. The efficiency curves,
historical apparatus constraints and external gyrating-sort result
were not independently reproduced. Patent commentary was read in its
historical setting and with the official dated wording correction.

Source screen: `sources/oscillating-errata-review.json`.
Next: §5.4.6, printed p.317 / file p.328.
