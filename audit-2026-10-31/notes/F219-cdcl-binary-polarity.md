# F219 — Binary propagation starts from the opposite literal

Confirmed in Volume4B, SAT answer267, printed599/file619.

Answer267 defines BIMP(l) as consequences of makingl true, but the hook after
G←G+1 starts the closure with l0←not l. It must use l0←l. The step reference
there should also be C3, where that increment occurs.

A complete two-variable counterexample is (a) and(not b) and(not a or b).
Represent its binary clause only inBIMP, as the answer explicitly permits,
and initialize the two unit trail entries correctly (isolatingF215).
Then BIMP(a)={b} and BIMP(not b)={not a}. The printed hook instead checks the
empty lists BIMP(not a) andBIMP(b), reaches G=F=n, and declaresSAT despite the
falsified binary clause. Correct propagation reports the immediate conflict.
SAT13 starts each binary closure from the actual true trail literal.

The original4B typesetting was inspected, and the same issue is present in the
2015 author draft at the corresponding answer (F6 pages233–236, file241–244).
Current/historical4B andF6 errata were checked. No matching correction was found;
the2026 corrections toC9 and answer263 are separate known errata. Focused public
searches found no matching report; absolute priority is not claimed.

Evidence: bookwise-cdcl-source-check.json, the cited original page image, and
check_bookwise_cdcl.py with results/bookwise-cdcl-fixed-witnesses.json. The script
checks fixed local states and small explicitly given formulas; it is not a full
independent CDCL implementation or a general instance census.
