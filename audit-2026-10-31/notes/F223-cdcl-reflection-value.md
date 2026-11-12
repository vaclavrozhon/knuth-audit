# F223 — Reflected unit propagation omits its value assignment

Confirmed in Volume4B, SAT answer272, printed600/file620.

When a reflected clause forcesu, answer272 writes L_F,TLOC(|u|),R_u andF,
but omits VAL(|u|). This leaves a literal simultaneously on the trail and free,
violating(117). Insert VAL(|u|)←2d+(u&1), withd the current level after any
extra backjump (and d' synchronized with it).

Use the same symmetric four-clause formula asF222, now with decisions
not6,not1,not2 at levels1,2,3. The first conflict again learns(1 or2).
After backjumping to2, the reflected(6 or5) has6 false at level1 and5 free.
The printed ranking choosesu=5,v=6, then jumps to1 and appends5. This branch
does not hitF222's false-conflict test, yet VAL(5) stays-1. The correct encoded
value is2 (true at level1). This is an independent omission, even when the rank
issue is repaired. The fixed script verifies the precursor propagation trace.

The original4B typesetting was inspected, and the same issue is present in the
2015 author draft at the corresponding answer (F6 pages233–236, file241–244).
Current/historical4B andF6 errata were checked. No matching correction was found;
the2026 corrections toC9 and answer263 are separate known errata. Focused public
searches found no matching report; absolute priority is not claimed.

Evidence: bookwise-cdcl-source-check.json, the cited original page image, and
check_bookwise_cdcl.py with results/bookwise-cdcl-fixed-witnesses.json. The script
checks fixed local states and small explicitly given formulas; it is not a full
independent CDCL implementation or a general instance census.
