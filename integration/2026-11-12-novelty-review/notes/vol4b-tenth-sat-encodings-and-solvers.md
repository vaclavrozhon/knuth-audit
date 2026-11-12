# Volume 4B: F197–F220 publication review

Reviewed on 2026-11-12. All 24 findings are retained after rereading their
detailed proofs and the original first-edition, second-printing pages. Existing
fixed witnesses and independent proof-check logs were reused. No solver
benchmark or large enumeration was restarted.

| Card | Rechecked reason |
| --- | --- |
| F197 | SAT29: caps (1,1,1,3,4,5) satisfy the stated assumptions but request s_2^2 outside the counter's sole column. The assignment 101000 satisfies the printed encoding while violating the third prefix bound. First normalizing each cap increment to at most one repairs the missing propagation. |
| F198 | SAT18: at n=8 the printed 5n/6 bound permits only six uses of a color, whereas the answer's table requires seven. The archived n=8 CNF has an independently verified DRAT unsatisfiability proof for six; the displayed construction has class sizes (20,23,22,7). Use ceil(5n/6). General optimality remains outside this finding. |
| F199 | SAT45 allocates only floor(t/2) effective root bits. For t=5 it excludes 25=5^2. Both factors need ceil(t/2) bits, with the extra product bit forced to zero when t is odd. |
| F200 | SAT64's trailing-one substitution uses wire j instead of n+1-j. On unsorted input 0101, the printed leading-zero and trailing-one rules give conflicting constants on wire 1. The author's sorting-network generator uses the correct index. |
| F201 | SAT64's common range i<j<=n omits preservation clauses for unused wire n. The fixed three-wire trace 110→111→111→110→011 satisfies the printed clauses although the actual comparator sequence leaves 101. Give the preservation clauses their own range 1<=i<=n. |
| F202 | SAT77: (f,g,h,i)=(0,1,1,0) satisfies all four printed binary clauses but violates two stated sum conditions. Add not-g OR not-h. The tuple is compatible with a local still-life block; no claim that it is a four-step eater is needed. The author's change file repeats this omission. |
| F203 | SAT92 deletes the entire waiting implication, losing its guard. The stored five-step path reaches simultaneous critical states using an illegal B1→B3 jump while the light is on. Remove only the successor literal, or retain the original waiting clause with the distinct-state constraints. |
| F204 | SAT117 uses n input bits but n-1 pair leaves. The new two-leaf clauses need input subscripts increased by one, and the three-leaf identity is 2k=n-2. At n=6,r=3 the printed encoding accepts 011111 despite its four adjacent 11 pairs. The author's helper instead consistently uses a pair-count parameter. |
| F205 | SAT134 doubles capacity without updating the stored exponent K. After 4→8, the next request still uses K=2 and requests eight again. Add K←k+1. The archived SAT11 implementation already performs this update. |
| F206 | Step X2 indexes the variable array VAL by an encoded literal. In a reachable state for (x2),(x3),(x1 OR x2), the free literals 2 and 3 erase the true values of x2 and x3. Use the underlying variable index. The July 2020 erratum introduced this defective line; it is not an existing correction of the defect. |
| F207 | L3 fails to save BACKF at branchless levels, but L15 reads it there unconditionally. The archived instrumented 175-variable run reaches exactly such a read; the guarded transcription reports an unsaved value. Move the backup saves before the zero-decision test. This is a reached invalid read, not a claim of a demonstrated false SAT answer. |
| F208 | SAT175 restores expired clause reductions, then unchanged routine (72) resets G to F and loses its retained visible prefix. The four-literal witness loses a's undo record and later reaches a spurious unit case. Retain G and set E←G, also in double lookahead. SAT11K does so. |
| F209 | SAT175 decrements the stored size only when the residual clause has at least two literals, but undo increments it unconditionally. The fixed three-literal example returns with size four. Store every decrement before the branch; the archived SAT11K code already does this. |
| F210 | SAT178's color-first prefix for k six-vertex blocks has 6k variables, not 6kq. At q=5,k=4 the printed 120 levels exceed all 90 variables. Removing q preserves the intended exponential comparison. |
| F211 | SAT215's stationary-point formula requires alpha>(7/6)*ln(4). At alpha=1 the maximum is at the endpoint t=1/2, and the proposed stationary depth lies outside the tree. At equality the Gaussian is one-sided. The exact profile and alpha=4 example remain valid; the 2018 expansion correction does not supply the missing restriction. |
| F212 | SAT217's answer is false as posed: A=B={l} are simultaneously satisfiable, but deleting both signs of l leaves the empty clause. A={l,a}, B={l,b} also refutes the printed proof's claim about the particular covering assignment. Ordinary resolution with complementary pivot assumptions is unaffected. |
| F213 | SAT227 reverses the Delayer's unequal-label choices. For {x,not-x OR y,not-x OR not-y}, the x=true branch has label one and x=false label zero. The printed choice takes the immediately contradictory branch and earns no point. Swap 0 and 1 in the two cases. |
| F214 | SAT243(d) must say that clause C contains the boundary literal, not V. V(F') denotes a variable set and is not the clause selected by the argument. The intended width proof is valid. |
| F215 | SAT260 initializes a unit's value and position but never writes its literal into the trail. Even input (x1) leaves the slot read by C3 undefined. Add L_F←l0 before incrementing F. SAT13 contains that write. |
| F216 | SAT261 advances its watch-list cursor only in the forced-unit case. A reachable satisfied-clause iteration instead processes the same clause repeatedly and can link it to itself. Advance after every nonconflicting iteration, including a moved watch. SAT13's loop does so. |
| F217 | SAT262 increases ACT but sifts with the old value alpha. A two-element heap of zero priorities fails its invariant after bumping its child by one. Use the new activity in both storage and comparisons. This affects the heuristic invariant, not logical satisfiability by itself. |
| F218 | SAT265's claimed highest-level property is false for a satisfied clause. Watching (not-x1,x2) in (not-x1 OR x2 OR x3), decisions not-x1,not-x2,not-x3 at levels 1,2,3 retain the false second watch at level 2. The actual propagation behavior is valid. |
| F219 | SAT267 starts binary propagation from the complement of the true trail literal. With units a,not-b and binary clause not-a OR b stored only in BIMP, it checks two empty lists and falsely declares SAT. Start from the true literal and reference C3. |
| F220 | SAT267 records binary reasons using the outer trigger l rather than the current source l0. In the fixed ternary-then-binary chain it records not-s OR c, which is not even implied by the input. Use l0 for both reasons and binary conflict clauses. This is independent of the starting-polarity correction. |

## Novelty checks and limits

The November 12 cumulative/current 4B and Fascicle 6 sources were screened at
all relevant book and historical fascicle coordinates. The 2020 X2 erratum
explicitly contains the bad index. The 2018 SAT215 replacement still omits the
endpoint regime. The March 2026 SAT263 replacement and earlier changes to
answers 24,43,46,257,263 and the binary-loop cursor are different corrections.
No matching official correction was found.

Focused public searches covered prefix counters, McGregor rounding, square
encodings, eater conditions, lookahead backup pointers, search profiles,
Prover–Delayer moves, watched literals and SAT11/SAT13 errors. Returned program
mirrors and general tutorials did not identify these discrepancies. The
[Japanese SAT tutorial](https://taocp-fun.gitlab.io/v4f6-sat-tut/) supplies related
exercises and implementations, without a matching report located here.

Public [tamnd/brain SAT answers](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4/7.2.2.2)
18,29,45,64,77,92,117,134,175,178,215,217,227,243,260,261,262,265,267 were
checked. Many contain an unrelated repeated answer; others give a different
construction or an incomplete argument. In particular 18 retains an incorrect
unrounded bound, 117 uses separate pair variables, 134 omits the stored exponent
altogether, 175 never specifies restoration, and 178 does not identify the
extra q. None supplies a matching error report.

Relevant portions of the archived author programs SAT11, SAT11K and SAT13
were reread against the book. Their correct implementations substantiate the
textual discrepancies; a correct independent implementation is not, by itself,
an explicit public report that the book is wrong. Program links and retrieval
hashes remain in the individual cards' source manifests. No absolute priority
is established, and no private reports or physical copies were checked.
