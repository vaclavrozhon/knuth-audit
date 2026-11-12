# F226 — The purge histogram omits protected clauses

Confirmed in Volume 4B, SAT answer 288, printed 603/file 623.

Here mj is the number of learned clauses with RANGE j, and sj is the
number in smaller buckets. Equation (124) needs m0, which includes the
protected reason clauses. The detailed procedure initializes only m1 through
m255, sets RANGE(c)=0 for a protected clause without incrementing a count,
and likewise assigns zero to newly learned clauses without counting them.

Even granting an implicit initial m0=0 does not fix the omission. Suppose two
clauses are protected and six ordinary clauses have range 16. The total is
eight and the target T is four. The correct count is m0=2, leaving room for
two ordinary clauses. If the zero bucket is left at zero, the threshold
calculation allows four ordinary clauses plus the two protected clauses,
retaining six. This example assumes the tie-selection error F227 has already
been fixed, so it isolates the missing histogram entries.

Initialize m0 and count every range-zero clause as it is assigned that range,
or maintain an equivalent separate protected count. The official SAT13 source
uses a separate asserts counter in its threshold computation; its treatment of
newly learned clauses differs slightly from the book and is not transcribed
here as a wholesale replacement algorithm.

The original Volume 4B typesetting and the corresponding September 23, 2015
author draft were checked. Current and historical Volume 4B/Fascicle 6 errata
contain no matching correction. The known answer 288 VAL-read correction and
answer 293 schedule correction are separate. Focused public searches found no
matching report; this does not establish absolute priority.

Evidence: sources/bookwise-cert-purge-source-check.json, the cited original
page image, check_bookwise_cert_purge.py, and its fixed-witness result file.
The checks cover these explicit examples, not a full independent solver.
