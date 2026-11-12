# F216 — Watch-list cursor is not advanced on two branches

Confirmed in Volume4B, SAT answer261, printed598/file618.

Answer261 places c←c' at the end of the forced-unit case. The satisfied-clause
case runs(*) and leavesc unchanged; the moved-watch case also lacks an advance.
A reachable example is the clause(not x1 or x2 or x3), watched at(not x1,x2),
with decisions not x1 then not x2. When the second watch becomes false, the
first is true. Repeating(*) first keeps the samec, then links it to itself.
The cursor must advance unconditionally after each nonconflicting iteration;
the binary propagation added in267 remains specific to the unit-forcing case.
SAT13 instead uses a for-loop with wa=next_wa at every iteration, including
its satisfied-clause and moved-watch continue paths (lines1571ff).

The original4B typesetting was inspected, and the same issue is present in the
2015 author draft at the corresponding answer (F6 pages233–236, file241–244).
Current/historical4B andF6 errata were checked. No matching correction was found;
the2026 corrections toC9 and answer263 are separate known errata. Focused public
searches found no matching report; absolute priority is not claimed.

Evidence: bookwise-cdcl-source-check.json, the cited original page image, and
check_bookwise_cdcl.py with results/bookwise-cdcl-fixed-witnesses.json. The script
checks fixed local states and small explicitly given formulas; it is not a full
independent CDCL implementation or a general instance census.
