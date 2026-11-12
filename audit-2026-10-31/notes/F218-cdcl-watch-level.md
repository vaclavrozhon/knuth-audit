# F218 — A false watch need not have the highest clause level

Confirmed in Volume4B, SAT answer265, printed599/file619.

The last paragraph says that any false watched literal must have the highest
trail level of all literals in its clause. Take clause(not x1 or x2 or x3),
watching(not x1,x2). Make the three decisions not x1,not x2,not x3 at levels1,2,3.
There is no propagation or conflict: the first watch is true, so the second is
retained when it becomes false. The false watchx2 is at level2, belowx3 at3.
All three decisions agree with AlgorithmC's initial negative polarity.
The algorithm's behavior is valid; the general invariant is not. SAT13's nearby
comment makes the narrower claim for both watchers of an entirely false clause
during a full run, rather than every false watcher of a satisfied clause.

The original4B typesetting was inspected, and the same issue is present in the
2015 author draft at the corresponding answer (F6 pages233–236, file241–244).
Current/historical4B andF6 errata were checked. No matching correction was found;
the2026 corrections toC9 and answer263 are separate known errata. Focused public
searches found no matching report; absolute priority is not claimed.

Evidence: bookwise-cdcl-source-check.json, the cited original page image, and
check_bookwise_cdcl.py with results/bookwise-cdcl-fixed-witnesses.json. The script
checks fixed local states and small explicitly given formulas; it is not a full
independent CDCL implementation or a general instance census.
