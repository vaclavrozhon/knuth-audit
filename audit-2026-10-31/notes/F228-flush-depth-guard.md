# F228 — Literal flushing reads beyond the current decision levels

Confirmed in Volume 4B, main printed 260/file 280, equation (126).

In (126), d is the current decision depth and i_j is the start of decision
level j. The loop starts d-prime=0 and repeatedly examines the activity of the
decision at level d-prime+1. If every current decision has activity at least
that of the selected free variable k, it reaches d-prime=d and next reads
i_(d+1), which does not describe a current decision. For d=0, even the first
iteration has no valid decision to inspect.

The root-level case can occur in the ordinary solver. Start with the clauses
(x1 or x2) and (x1 or not x2). The initial negative decision for x1 forces both
polarities of x2, learns the unit x1, and backjumps to depth zero. Now x2 is
still free, one learned clause triggers the initial flushing schedule, and
agility is small. Both variables were bumped by the conflict. A stale i1=0
points at the root literal x1; the printed comparison can succeed, after which
i2 has never been initialized. This does not rely on F217: assume the activity
heap update has been corrected.

The loop condition needs d-prime<d before reading the next decision. This also
makes the intended no-change outcome d-prime=d explicit. SAT13 checks the
current depth and bounds its loop by that depth.

The original Volume 4B typesetting and the corresponding September 23, 2015
author draft were checked. Current and historical Volume 4B/Fascicle 6 errata
contain no matching correction. The known answer 288 VAL-read correction and
answer 293 schedule correction are separate. Focused public searches found no
matching report; this does not establish absolute priority.

Evidence: sources/bookwise-cert-purge-source-check.json, the cited original
page image, check_bookwise_cert_purge.py, and its fixed-witness result file.
The checks cover these explicit examples, not a full independent solver.
