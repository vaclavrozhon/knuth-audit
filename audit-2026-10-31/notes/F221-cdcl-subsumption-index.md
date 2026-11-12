# F221 — Subsumption reads VAL using a literal code

Confirmed in Volume4B, SAT answer270(b), printed600/file620.

Answer270(b) tests VAL(MEM[c+j'])≥2d, although MEM holds encoded literals
and VAL is indexed by variables. The test must be VAL(|MEM[c+j']|)≥2d.

The example in270(a) already supplies a witness. Before strengthening R6,
its literals may be(6,not5,not4,not1), encoded(12,11,9,3). Variable1 is true
at level1, and variables3,4,5,6 are true at level2. After the size decrement,
the printed largest-index test examines the last code3 and reads VAL(3)=4,
therefore selecting not1 at the wrong level. The corrected test reads VAL(1)=2,
rejects that candidate, and selects not4 at level2. No out-of-bounds read is
needed for this witness. SAT13 uses vmem[thevar(lll)].value (lines2277–2282).

The original4B typesetting was inspected, and the same issue is present in the
2015 author draft at the corresponding answer (F6 pages233–236, file241–244).
Current/historical4B andF6 errata were checked. No matching correction was found;
the2026 corrections toC9 and answer263 are separate known errata. Focused public
searches found no matching report; absolute priority is not claimed.

Evidence: bookwise-cdcl-source-check.json, the cited original page image, and
check_bookwise_cdcl.py with results/bookwise-cdcl-fixed-witnesses.json. The script
checks fixed local states and small explicitly given formulas; it is not a full
independent CDCL implementation or a general instance census.
