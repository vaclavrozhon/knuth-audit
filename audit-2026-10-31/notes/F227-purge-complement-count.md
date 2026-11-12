# F227 — Purge tie breaking discards the number that should be kept

Confirmed in Volume 4B, SAT answer 288, printed 603–604/files 623–624.

Let sj count clauses below the boundary range j and mj count clauses at j.
To retain T clauses, one must retain T-sj of the mj boundary clauses, hence
discard sj+mj-T. The printed procedure instead bumps T-sj least-active
clauses above j, then discards all clauses above j. Its heap description also
implements that incorrect discard count.

With two protected clauses below the threshold, six tied at range 16, and
T=4, the printed rule discards two and retains six in total. The correct rule
discards four and retains four. This example supplies the correct histogram,
so it is independent of F226. In the book's larger example, sj=3081, mj=59,
T=3126, the printed rule retains 3095 instead of 3126.

Use h=sj+mj-T as the discard count. Handle T=sj as well: all mj boundary
clauses must then be removed, whereas the printed T>sj condition skips them.
Equivalently, select the T-sj most-active boundary clauses to keep. SAT13 uses
the inclusive threshold count minus the budget as its discard count.

The original Volume 4B typesetting and the corresponding September 23, 2015
author draft were checked. Current and historical Volume 4B/Fascicle 6 errata
contain no matching correction. The known answer 288 VAL-read correction and
answer 293 schedule correction are separate. Focused public searches found no
matching report; this does not establish absolute priority.

Evidence: sources/bookwise-cert-purge-source-check.json, the cited original
page image, check_bookwise_cert_purge.py, and its fixed-witness result file.
The checks cover these explicit examples, not a full independent solver.
