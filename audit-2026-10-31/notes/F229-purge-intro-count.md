# F229 — The introductory purge example swaps keep and forget

Confirmed in Volume 4B, main printed 256/file 276.

The example has 6252 learned clauses, including 12 protected reasons,
and wants at most 3126 clauses to remain. Thus it must discard at least
6252-3126=3126 clauses from the 6240 unprotected clauses. The printed instruction
to forget 3114 leaves 3138 clauses. The number 3114 instead counts the
unprotected clauses to keep: 3126-12=3114.

The later main-text threshold example and the knapsack constraint in exercise
286 use the intended keep count. This is a local arithmetic/wording error,
separate from answer 288's general tie-breaking error F227.

The original Volume 4B typesetting and the corresponding September 23, 2015
author draft were checked. Current and historical Volume 4B/Fascicle 6 errata
contain no matching correction. The known answer 288 VAL-read correction and
answer 293 schedule correction are separate. Focused public searches found no
matching report; this does not establish absolute priority.

Evidence: sources/bookwise-cert-purge-source-check.json, the cited original
page image, check_bookwise_cert_purge.py, and its fixed-witness result file.
The checks cover these explicit examples, not a full independent solver.
