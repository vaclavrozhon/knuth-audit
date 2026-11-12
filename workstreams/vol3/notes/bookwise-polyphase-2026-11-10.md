# Bookwise review: polyphase merging, 10 November 2026

Reviewed §5.4.2, printed pp.267–287, all 31 exercises and their answers
on pp.680–684. The shared answer page 684 begins cascade merging and
is deferred to that next certification block. Read Algorithm D, the
perfect-distribution and merge-number recurrences, the dummy-placement
analysis, Caron's schedule, and tape splitting together with their
exercise arguments and the five official errata layers.

Checked the backwards Fibonacci distributions and their generating
functions; horizontal dummy allocation and the disappearance of dummies;
the dominant-root argument and the simple/double-pole coefficients;
generalized Fibonacci compositions, bit strings and numeration; the
unimodality and crossing argument used to order optimal levels; and the
gcd invariant for merge-until-empty schedules. The polynomial recurrence
between (15) and (16) has the missing factor recorded in C0052. The
exact reverse-generation claim in answer 28 needs the domination or
partial-addition repair in C0053; its final phase bound survives.

The 49-run and 82-run schedules, merge-number string rules and
tape-splitting recurrences were compared with their tables. The
six-tape run-length recurrence factors as
`(1-z-z^2)(1+z+z^2)`, yielding the mod-3 correction in answer 22.
The coupled recurrences for the altered split in answer 23 and the
four-tape power-of-two counts in answers 25–26 are consistent with the
displayed schedules. The 9-run improvement in answer 18 has costs 32
and 31 as claimed. The ordered-tree/composition correspondence in
answer 31 adds one leaf plus its newly distinct ancestors at each step.

Known corrections to D1, the tape-splitting balance equation and final
table rows, the partial-fraction coefficient, and the root-expansion
formula were incorporated; they are not new findings.

Limits: the optimal-distribution tables and Mortenson's table in answer
30 were not recomputed as censuses. Zave's results in answers 15–17
were accepted as attributed external results; the local polynomial
counts and the 144/145-run obstruction in answer 17 were inspected.
Research tasks 24 and 29 were not solved. The interpretation of Q in
exercise 11 was checked against its recurrence and generalized
numeration, without writing a new full proof of the correspondence.
Historical timing and least-squares fits were not reproduced.

In particular, the linear overlap estimate on p.280 is approximate:
literal phase-by-phase maxima can leave extra waits when r=3t/4.
Earlier initiation of rewinding an exhausted input tape changes some
of those waits, so no exact scheduling or hardware-performance claim
is certified here, and this observation was not promoted to a finding.
The exact combinatorial schedules were reviewed separately from that
performance approximation.

Source screen: `sources/polyphase-errata-review.json`. Next: §5.4.3,
printed p.288 / file p.299.
