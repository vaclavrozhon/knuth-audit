# Volume 4B: CDCL details and arithmetic encodings

Reviewed on 12 November 2026: C013 and F221–F239. All twenty cards are retained. This is a second correctness and publication review of the baseline findings, not a claim of absolute priority.

The source is the 2022 second printing, identified in `inventory/books.json`. Original page images were checked for pp. 89, 110, 256, 260, 284, 354, 474, 600, 602–604, 627, 630, 632–634. The existing individual proof notes and fixed witnesses were read together with the typesetting. Previously successful exhaustive checks were not needlessly repeated.

## Card decisions

Here SAT means section 7.2.2.2; a literal is a Boolean variable or its negation. CDCL is conflict-driven clause learning, the SAT method that records assignments and their reasons on a trail. `VAL` is indexed by variables, not by encoded literals.

| Card | Rechecked reason and scope |
| --- | --- |
| C013 | P1 inherits C1 initialization, and p. 89 explicitly permits uninitialized COLOR fields in primary headers. Answer 220 later reads those fields as option-address marks. The three-row input with primary items a,b and secondary item s, rows `a s:1`, `a`, `b s:2`, skips a blocking test when COLOR(b)=5. Zero initialization fixes it. This is incomplete preprocessing, not loss of solutions; the author's calloc-based program already avoids it. |
| F221 | SAT270(b) indexes VAL by MEM[c+j'] directly. Literal code 3 represents negative x1 but reads variable 3. Reduce the literal to its variable before consulting its assignment level. |
| F222 | At the stated insertion point in SAT272, d already denotes the backjumped level. Giving free literals rank d therefore misclassifies a reflected clause with two free literals as conflicting. The symmetric four-clause witness has a legitimate free reflected clause. Free and satisfied literals need a rank above all false-literal levels. |
| F223 | Independently, SAT272 appends the reflected forced literal to the trail without setting its VAL field. The recorded witness appends variable 5 while leaving VAL(5)=-1; set its value and current level as well as its reason and trail position. |
| F224 | SAT284 initializes VAL to 0, meaning true, rather than -1, meaning unassigned. The satisfiable formula consisting of negative a then accepts a false empty-clause certificate. Initialize variables to -1 and assign only the dummy variable and explicit assumptions. |
| F225 | SAT284 starts its reverse dependency scan at the maximum trail position of l1,...,l(k-1), omitting l0. For the two contradictory units a and negative a, this can retain only one unit as a purported unsatisfiable core. Include l0 in the maximum. |
| F226 | SAT288 neither initializes nor counts histogram bucket m0 for protected clauses. With two protected and six ordinary clauses, target four is already miscomputed even with correct tie handling. Count protected clauses, including those learned during the run. |
| F227 | Independently, SAT288 discards T-sj boundary clauses although that is the number to keep. The discarded number is sj+mj-T, including the equality case T=sj. The example sj=2,mj=6,T=4 exposes the reversed count. |
| F228 | Equation (126) tests the activity of a next decision without establishing that the next level exists. A root-level learned unit provides a reachable example. Short-circuit with d'<d before reading the next decision. |
| F229 | On p. 256, forgetting 3114 of 6240 unprotected clauses while retaining 12 protected ones leaves 3138, above the target 3126. Forget 3126, or say to keep 3114 unprotected clauses. |
| F230 | In SAT392(a)(iv), row 5 column 11 is an isolated G, separated from the other 25 G cells by A,A,H,H. Changing it to A preserves the twenty givens and restores connected letter regions. |
| F231 | SAT392(b)'s nine-column argument refers to diagram (vi), not (vii), which has eight columns and seven letters. The impossibility argument itself is unchanged. |
| F232 | SAT394 specifies p inputs but gives a clause count using undefined n. The count is p*l+p-2^l. For p=3 it gives five clauses; the encoding itself is sound. |
| F233 | The reflected unary string before (165) must end at d-1, not j-1. The displayed reflection formula itself is correct. |
| F234 | SAT406(a) omits the first product-threshold clause when sqrt(a+1) is not integral. At d=5,a=7 the printed clauses admit x=y=3. The first upper limit needs ceil(sqrt(a+1)); the second endpoint has its separately derived bound. |
| F235 | SAT414's strict comparison count is 2^n+2^(n-1)-1, not the expression ending in +1. At n=2 elimination gives five clauses; the recurrence T(n)=2*T(n-1)+1 with T(1)=2 verifies the correction. |
| F236 | The five relaxed full-adder inequalities in SAT410–411 admit three input ones with output carry 1 and sum 0, understating 3 as 2. The proposed multiplier admits 7*7=37. The particular final inequality in SAT410 still agrees on all 64 original inputs, so the card must not claim that particular decision result is wrong. Adding local carry exclusion, or using direct parity/majority clauses, repairs the faulty relaxation. |
| F237 | SAT407(b)'s described recursive merge introduces 2d-4 auxiliary bits per merge, giving leading term 2d lg d rather than d lg d. The asymptotic order and the separate clause count remain unchanged. |
| F238 | SAT418 copies row terminal polarities into the column construction, although the required column output is the opposite. All-ones 3-by-3 is accepted, and a valid 3-by-4 witness is rejected. Complement the column output tests and change the initial c index from i to j. |
| F239 | SAT428(b) initializes a circuit signal to the complement of an edge input, violating the claimed monotonicity. Initialize only positive signals for present edges and leave absent edges unassigned in the simulated propagation. The same recurrence then yields the claimed monotone bound; the theorem is not refuted. |

## Errata and public-source comparison

The current and historical Volume 4B, Fascicle 5 and Fascicle 6 layers were refreshed on the review date; hashes and retrieval information are in `../sources/manifest.json`. Relevant page and exercise entries in all4b/err4b, all4f5/err4f5 and all4f6/err4f6 were compared, including the available TeX corrections. Draft-to-book offsets were applied separately to text and answer sections. No matching correction was found. In particular, the COLOR table correction initializes a spacer, not the primary headers; the known P3 and P5 corrections do not initialize the marks. The 2022 SAT410 index/high-bit changes do not repair the full-adder relaxation. The SAT415 and SAT418 cross-reference corrections do not address these findings.

Public searches combined Knuth/TAOCP with certificate initialization, clause purging, reflection, literal ranks, full-adder relaxation, hidden weighted bit, monotone propagation, strict comparison clause counts, and COLOR initialization. Results were screened for an actual matching report, not merely a description of the correct standard method.

The public exercise collection [tamnd/brain](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4) was read for DLX220 and SAT270,272,284,288,392,394,406,407,410,414,418,428. Several entries discuss different exercises; SAT394 repeats the undefined-n expression rather than correcting it, and DLX220 does not address the COLOR marking method. None reports these defects.

[Schlenga's 2020 CDCL exposition](https://www21.in.tum.de/teaching/sar/SS20/1.pdf) describes the main implementation but provides no matching report of these exercise-level defects. The original Knuth source programs used in the prior proofs distinguish working implementation details from faulty printed pseudocode. Existing code that correctly implements a standard operation is not by itself an explicit prior report of a book error.

Result for every card in this block: **no matching prior report found in the checked sources; priority not established**. Detailed witnesses remain in the original card evidence, with the qualifications above controlling the current assessment.
