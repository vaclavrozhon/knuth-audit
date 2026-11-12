# F224 — Verifier initialization can accept a false certificate

Confirmed in Volume 4B, SAT answer 284, printed 602/file 622.

The answer defines VAL(k)=0 for true, 1 for false, and -1 for unassigned,
but starts each verification with VAL(j)←0 for every variable. Only the dummy
x0 and the negated literals of the candidate clause are actually put on the trail.

Take the satisfiable input F={(not a)} and the purported certificate consisting
of the empty clause. The prescribed unit-clause representation is (not a or not x0),
with x0 true. The printed initialization also makes a true, so propagation of x0
reports a conflict and accepts the empty clause. With the correct unassigned
initialization, propagation merely forces a=false and ends without a conflict;
the invalid certificate is rejected. No earlier CDCL implementation error is
needed for this counterexample.

Set every VAL entry to -1 first and then write the actual initial assignments.
The initial trail positions must of course have their corresponding TLOC values.

The original Volume 4B typesetting and the corresponding September 23, 2015
author draft were checked. Current and historical Volume 4B/Fascicle 6 errata
contain no matching correction. The known answer 288 VAL-read correction and
answer 293 schedule correction are separate. Focused public searches found no
matching report; this does not establish absolute priority.

Evidence: sources/bookwise-cert-purge-source-check.json, the cited original
page image, check_bookwise_cert_purge.py, and its fixed-witness result file.
The checks cover these explicit examples, not a full independent solver.
