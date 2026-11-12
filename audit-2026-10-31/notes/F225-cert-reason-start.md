# F225 — Certificate trimming omits the first conflict literal

Confirmed in Volume 4B, SAT answer 284, printed 602–603/files 622–623.

A conflict clause c=(l0,...,lk-1) is false under the trail, including l0.
The reason for the assignment of its complement can be essential, even when
its trail position exceeds those of all the other conflict literals.

Assume F224 is fixed. Let F={(a),(not a)}, and check its one-clause certificate
consisting of the empty clause. Represent the units as (a or not x0) and
(not a or not x0), with x0 true. Process the positive unit first. Then the
trail is [x0,a], E=1, and the second clause is the conflict, with l0=not a
and l1=not x0. The printed maximum is TLOC(x0)=0. Consequently the backward
loop never runs, and only the negative unit is marked. Deleting unmarked
input clauses leaves the satisfiable family {(not a)}.

The maximum must include l0: starting at TLOC(a)=1 marks the positive unit's
reason, preserving the unsatisfiable core. The 2019/2026 corrections to the
related answer 263 do not correct the separate formula in answer 284.

The original Volume 4B typesetting and the corresponding September 23, 2015
author draft were checked. Current and historical Volume 4B/Fascicle 6 errata
contain no matching correction. The known answer 288 VAL-read correction and
answer 293 schedule correction are separate. Focused public searches found no
matching report; this does not establish absolute priority.

Evidence: sources/bookwise-cert-purge-source-check.json, the cited original
page image, check_bookwise_cert_purge.py, and its fixed-witness result file.
The checks cover these explicit examples, not a full independent solver.
