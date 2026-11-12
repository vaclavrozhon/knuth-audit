# F215 — Initial unit literals are never written to the trail

Confirmed in Volume4B, SAT answer260, printed597/file617.

Answer260's k=1 branch makes a new unit known and records its trail position,
then incrementsF without assigning L_F. Even the single input clause(x1) leaves
L0 undefined, although C3 will immediately read it. Insert L_F←l0 before F←F+1.
SAT13 lines1432–1437 do write trail[eptr++]=l. The fixed witness uses one unit
and an uninitialized-slot sentinel; no incorrect SAT output is invented for
undefined memory.

The original4B typesetting was inspected, and the same issue is present in the
2015 author draft at the corresponding answer (F6 pages233–236, file241–244).
Current/historical4B andF6 errata were checked. No matching correction was found;
the2026 corrections toC9 and answer263 are separate known errata. Focused public
searches found no matching report; absolute priority is not claimed.

Evidence: bookwise-cdcl-source-check.json, the cited original page image, and
check_bookwise_cdcl.py with results/bookwise-cdcl-fixed-witnesses.json. The script
checks fixed local states and small explicitly given formulas; it is not a full
independent CDCL implementation or a general instance census.
