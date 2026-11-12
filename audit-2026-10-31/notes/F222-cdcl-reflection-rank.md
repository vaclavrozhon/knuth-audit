# F222 — Reflection ranks free literals as a conflict

Confirmed in Volume4B, SAT answer272, printed600/file620.

Answer272 executes just before C9 returns to C3. But C8 has already setd←d',
so its default rank(l)=d gives a free literal the same rank as a false literal
at the current level. Two free reflected literals then satisfy rank(u)=rank(v)=d'
and are incorrectly passed to C7 as a conflict.

Use the reflection-invariant input
(1 or2 or3),(1 or2 or not3),(6 or5 or4),(6 or5 or not4), with reflection i↦7-i.
The answer explicitly extends the method to any order-two automorphism.
Decisions not1,not2 force both signs of3. Resolution learns(1 or2), backjumps
to level1, and appends2. Its reflected clause(6 or5) has two free literals,
but both printed ranks are1 and the algorithm wrongly enters conflict analysis.
The fixed script checks this concrete propagation trace and the resolution.

A sufficient corrected ranking is infinity for true or free literals, and the
actual trail level for false literals. A clause with two free watches is then
stored without either propagation or conflict. Merely appealing to the old
conflict leveld does not match the printed C8/C9 state.

The original4B typesetting was inspected, and the same issue is present in the
2015 author draft at the corresponding answer (F6 pages233–236, file241–244).
Current/historical4B andF6 errata were checked. No matching correction was found;
the2026 corrections toC9 and answer263 are separate known errata. Focused public
searches found no matching report; absolute priority is not claimed.

Evidence: bookwise-cdcl-source-check.json, the cited original page image, and
check_bookwise_cdcl.py with results/bookwise-cdcl-fixed-witnesses.json. The script
checks fixed local states and small explicitly given formulas; it is not a full
independent CDCL implementation or a general instance census.
