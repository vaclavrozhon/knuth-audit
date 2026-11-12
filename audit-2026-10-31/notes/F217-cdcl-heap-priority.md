# F217 — Activity increase sifts using the old priority

Confirmed in Volume4B, SAT answer262, printed598/file618.

In the C7 case, answer262 sets alpha←ACT(k), then ACT(k)←alpha+DEL, but the
sift-up comparisons still usealpha. A valid heap[1,2] with both activitieszero
and DEL=1 therefore stays[1,2] after bumping variable2: its child has priority1
and its root0. Such a forced variable is allowed to remain in the heap.
Set alpha←ACT(k)+DEL and ACT(k)←alpha before sifting. SAT13 does exactly this
with av (lines1755–1761). This breaks the stated heap/maximum-activity invariant;
it need not change the logical satisfiability answer.

The original4B typesetting was inspected, and the same issue is present in the
2015 author draft at the corresponding answer (F6 pages233–236, file241–244).
Current/historical4B andF6 errata were checked. No matching correction was found;
the2026 corrections toC9 and answer263 are separate known errata. Focused public
searches found no matching report; absolute priority is not claimed.

Evidence: bookwise-cdcl-source-check.json, the cited original page image, and
check_bookwise_cdcl.py with results/bookwise-cdcl-fixed-witnesses.json. The script
checks fixed local states and small explicitly given formulas; it is not a full
independent CDCL implementation or a general instance census.
