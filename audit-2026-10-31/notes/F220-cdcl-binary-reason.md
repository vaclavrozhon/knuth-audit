# F220 — Binary reasons use the outer trigger instead of their source

Confirmed in Volume4B, SAT answer267, printed599/file619.

The breadth-first loop enumerates l-prime inBIMP(l0), while the accompanying
operations record R[l-prime]←-l and a conflict clause(not l or l-prime).
Here l is the outer watch-list trigger from261, not the current source l0.
Both operations must use l0. This is independent ofF219's starting-polarity fix.

Let the input be(not a or not s or b) and(not b or c). With a=true already
on the trail, s=true triggers the ternary clause, which forcesb. Its immediate
binary closure has sourceb and forcesc, but the printed reason is(not s or c).
That is not even a consequence of the input: a=false,s=true,b=false,c=false
satisfies both input clauses and falsifies the recorded reason. The correct
reason is(not b or c). SAT13 uses its current binary-loop source for every
reason and advances that source with the breadth-first cursor (lines1514–1541).

The original4B typesetting was inspected, and the same issue is present in the
2015 author draft at the corresponding answer (F6 pages233–236, file241–244).
Current/historical4B andF6 errata were checked. No matching correction was found;
the2026 corrections toC9 and answer263 are separate known errata. Focused public
searches found no matching report; absolute priority is not claimed.

Evidence: bookwise-cdcl-source-check.json, the cited original page image, and
check_bookwise_cdcl.py with results/bookwise-cdcl-fixed-witnesses.json. The script
checks fixed local states and small explicitly given formulas; it is not a full
independent CDCL implementation or a general instance census.
