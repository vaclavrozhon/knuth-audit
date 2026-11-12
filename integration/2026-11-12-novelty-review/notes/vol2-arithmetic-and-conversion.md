# Publication review: C0091–C0110

Reviewed November 12, 2026. The fifteen baseline-confirmed cards in this
range remain supported. Original statements, surrounding assumptions,
existing certificates and all four applicable errata layers were checked.
No matching prior TAOCP report was located in the bounded public search.
This does not establish priority or verify an unseen physical printing.

| Card | Assessment and limits |
| --- | --- |
| V2-C0091 | For opposite normalized operands of equal magnitude, both addition routines take the zero branch without normalization shifts. The modification adds JOV, DEC2 and JNOV, so its time increases by three units, rather than decreasing by three. The stored 60/63-cycle trace agrees with the original instruction paths. For multiplication, the existing 112/108-cycle example saves a six-unit normalization iteration, outweighing two extra earlier units. The 2012 instruction-number correction is included. The numerical outputs and accuracy bounds are not disputed. |
| V2-C0092 | The original sequence really starts with 2!, then iterates factorial. Every term equals two, so it cannot have the proposed logarithmic distribution. Retain as a starting-value typo, not a resolution of the nonconstant iteration problem. |
| V2-C0093 | The strict leading-digit indicator counts eleven integers among 1,...,20 at r=s=2, while the exact equality on p. 258 counts twelve. Its other branch omits the new decade endpoint at s=10. The explicit allowed values r=1 and r=10 also need exceptions in the nonconvergence claims; answer 8 has the r=10 exception. Limiting formulas and the principal theorem survive these finite endpoint corrections. |
| V2-C0094 | The preceding bound is m'-m+1; substitution must retain its minus sign. The printed plus gives 3n+1 rather than n+1 when a=10,b=100 and fails to establish the required squeeze. Retain as a proof typo; the weaker printed inequality and final theorem remain true. |
| V2-C0095 | The three initial instructions and final store in answer 3 cost five units, not four. Answer 8's initial ENT1,JOV,STZ cost four, not three. Their displayed frequency columns give exact times 5MN+7N+K+5 and 9N+L+7K+4. The concrete cases in the reports meet the assumptions on the carry counts. Both programs compute correct results. |
| V2-C0096 | For n=1 or 2 no digit products satisfy i+j>n+2, so omission error is zero. The claimed strict bound is negative or zero. Restrict that bound to n>=3, and similarly separate the zero-error cases in the parenthetical next bound. Retain as a minor missing small-length qualification. |
| V2-C0097 | With m=2,n=1 and operands (10)_b and 1, the printed alias v_j at w_(j+n) puts the multiplier at w_1. M1 erases it before use, yielding zero. The original algorithm has no m<=n assumption. Placing v_j at w_(j+m) is safe because the last carry overwrites it only after its final use. |
| V2-C0099 | The explicit update u'=u-w_0*v lacks division by the radix. With radix 2, n=4, u=165 and v=15, it makes the next quotient bit zero although 165/15=11 has that bit one. Using (u-w_0*v)/2 gives the correct next bit. This is distinct from the well-publicized trial-quotient and overflow repairs in Algorithm D. |
| V2-C0100 | Substitution of the logarithms printed immediately above the BBP proof line gives (pi/2-ln(2))*(1+3i), not pi. Removing the extra factor two before l_1 and changing the final plus to minus gives pi. The original image confirms both coefficient errors. The series for pi is correct, and the 2024 historical citation addition does not repair this line. |
| V2-C0103 | The auxiliary input range permits e=1,f=2,u=3. Then b=1 and no iteration follows initialization, so the algorithm returns 3 rather than the canonical residue zero modulo 3. Normalize the initial residue or exclude this endpoint. The surrounding conversion already supplies canonical residues. The 2000 coprimality and 2025 conversion corrections are included and do not change this auxiliary bound. |
| V2-C0104 | The permitted input v=1/2 makes the initial reciprocal exact and delta_k=0. The intermediate strict inequality is therefore 0<0. Change it to a non-strict inequality. This is a minor proof endpoint; the algorithm and accuracy result remain correct. |
| V2-C0106 | The cited 1974 paper's Theorem 2(ii) explicitly gives Omega(n log n) for the ordinary one-dimensional multitape Turing-machine model, whereas the book calls the weaker Omega(n log n/log log n) bound the best known one. The latter belongs to the source's broader machine class. The theorem and model definition were re-inspected. Retain as a source/model correction, not a new complexity lower bound. The 2020 erratum only updates the upper bound. |
| V2-C0108 | For word capacity w and decimal divisor D=10^n, the exact sufficient and necessary word-constant condition is D-gcd(w,D)<=c<w. This follows by considering the smallest positive remainder of wu modulo D. Binary MIX with w=64^5,n=1,c=8 works for all ten inputs although the printed lower bound is nine. The printed condition is sufficient, but not necessary. |
| V2-C0109 | The original MIXAL // operator truncates. Thus MUL =1//10= uses a lower reciprocal and input 10 produces the invalid digit 10. Raising the reciprocal alone still leaves ADD U using the original input on later iterations, producing 0,10. Saving the current quotient before each reciprocal multiplication repairs this second defect. Both faults follow directly from the original listing; the existing exact simulator checks of the combined correction are retained. |
| V2-C0110 | The input has m+1 digits and program (6) performs m loop iterations, each with one multiplication and addition. The following sentence says m-1. The two-digit case already contradicts that count. The 2018 replacement concerns a later paragraph. |

Original pages re-inspected: 248–252, 257–258, 268, 282–284, 304–305,
312, 321, 323, 618, 620, 622–625, 627–629, 634 and 636; the definition
of MIXAL // on volume 1 p. 153; and the 1974 lower-bound source's pp. 7
and 21. Existing hand calculations and short instruction traces were
read rather than rerunning their large finite test sets.

The official layers `all2-prepre`, `all2-pre`, `all2`, and `err2` were
searched at these locations. In particular, the 2002 parenthesis repair
on p. 622, the 2012 p. 618 repair, the 2026 cross-reference on p. 624,
the 2000 exact-division bibliography update, the 2024 BBP attribution,
and the 1998 normalization changes are separate from these cards.

Public searches combined TAOCP/Knuth with double-precision timing,
Benford boundary formulas, iterated factorials, multiplication storage
overlap, exact division answer 40, BBP coefficient errors, the MIX
timing expressions, modular reciprocal endpoints, online multiplication
lower bounds, radix-conversion errata and the ADD U reciprocal loop.
No matching report of these specific defects was found. Book copies
and repetitions of their claims are not independent corrections.

Investigated leads and primary context:

- [Paterson, Fischer and Meyer, 1974](https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TM-040.pdf), pp. 7 and 21: source of the already-known stronger lower bound in C0106.
- [Clifford and Jalsenius, 2012](https://arxiv.org/pdf/1101.0768): a different cell-probe model, with no occurrence of Knuth in the retrieved paper; not a located report of the erroneous textbook attribution.
- [Russ Cox, January 10, 2026](https://research.swtch.com/fp-knuth.pdf), pp. 20–22: exercise 4.4-3's rounding history and change of problem specification. It explicitly distinguishes the first-edition problem from later correct rounding. It does not concern the word-constant condition or the integer reciprocal loop in C0108/C0109.
- [Ada User Journal 43(1)](https://ada-europe.org/archive/auj/auj-43-1-withcovers.pdf): the SPARK account identifies the already-published 1995 and 2005 Algorithm D overflow repairs. It does not report the missing radix shift in answer 40. Web retrieval timed out; the public PDF was subsequently retrieved directly and its relevant passage read.
- The 2024 Stack Overflow normalization question and 2026 Algorithm D article concern other division steps. The latter is already accounted for separately in V2-C0001's prior-public decision.
