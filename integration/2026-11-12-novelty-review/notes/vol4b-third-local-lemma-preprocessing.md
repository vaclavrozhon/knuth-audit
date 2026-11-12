# Volume 4B: local lemma, surveys, and preprocessing

Publication review, 2026-11-12. Retain F033–F052. The original November
2022 second-printing PDF was inspected on pp. 273,277,346–347,349,
615–620,623–624,626–627. Existing proofs, exact witnesses, and author-draft
comparisons were reused; earlier large enumerations were not repeated.

| Finding | Independent reason and scope |
| --- | --- |
| F033 | SAT 343: a cograph consisting of two disjoint edges has Mobius polynomial (1-p1-p2)(1-p3-p4). At all p_i=3/4 it is positive, but setting p3=p4=0 makes it negative, contradicting the claimed region-membership criterion. Joining a universal vertex of probability 1/10 gives a connected counterexample too. Positivity at every node of the decomposition tree repairs the criterion. |
| F034 | Answer 341: the recurrence omits w_ij before W(S minus {i,j}). With two vertices, diagonal weights one and off-diagonal weight two, the defined polynomial is x^2-2 but the recurrence gives x^2-1. The next paragraph uses the weights correctly. |
| F035 | Answer 345: decreasing one coordinate at a boundary point need not make the polynomial strictly positive. Two disjoint edges at probabilities 1/2 retain a zero factor after just p1 is decreased. Nonnegativity and continuity suffice for the intended construction. |
| F036 | Exercise 339(b): b7 a8 c3 has two maximal pieces, a8 and c3, because a and c commute; it is not a pyramid. The example needs four factors b6 c2 e4 d1, b7 c3, f5, a8 with top labels 1,3,5,8. The theorem is unaffected. |
| F037 | Answer 346(a): decreasing a nonnegative probability cannot increase a trace's weight. The final word in the sentence must be increase. For a single edge, K_a=1/(1-p_b) falls from two to 4/3 when p_b falls from 1/2 to 1/4, with p_a=1/8 keeping both points in the region. |
| F038 | Answer 348: the derivative sum indexed by m requires coefficient a_m, not a_n. For f(z)=1/(1-2z), n=0, r=1/4 the printed sum is 4/3 instead of two. |
| F039 | Answer 355: the concluding inequality for E_j is reversed. A single edge at p1=p2=1/4 has slack delta=1 and E_j=1/2, contradicting E_j>1/delta. A proof covering zero coordinates uses non-strict inequalities and gives E_j<=1/delta. |
| F040 | Exercise 356(b): minimize over clique indices j with i in U_j. The printed neighbor index confuses vertices with cliques and can refer to undefined theta and Sigma values even for one edge covered by one clique. The answer already uses the intended membership condition. |
| F041 | Answer 356(a): the conditioning set can overlap the clique, so the induction hypothesis does not apply. For the documented three-clique construction with disjoint events of probability 2/5, the asserted conditional bound is 2/3<=2/5. Assigning each vertex to its last containing clique repairs the partition and the final avoidance product. |
| F042 | Exercise 356: covering edges does not necessarily cover isolated vertices. With two isolated vertices, U1={1}, theta11=0, p=(0,1), all stated parameter conditions hold but the Mobius polynomial is zero. Cover all vertices or require p_i<1 separately for uncovered ones. This retained baseline finding concerns only the omitted isolated-vertex condition. |
| F043 | Main text p. 273: Case 1 is slower, not faster, than Case 2. For the book's seven-bit examples the exact means are seven and 1139/729; the following discussion and answer 349 already agree with this direction. |
| F044 | Answer 357: for (p,q)=(1,0), use y=0. The printed x=1/2,y=1 gives field (0,1/2,1/2); the defining r=xy/(x+y-xy) also immediately excludes y=1. |
| F045 | Answer 360: at a=b=c=0,d=1 the fixed-point equations reduce to x=y=z, permitting every common value in [0,1]. The displayed fraction is 0/0 there and the claim that d=1 forces all three to one is false. The documented full message assignment verifies every update. |
| F046 | Algorithm S: opposite unit clauses with initial messages 1/2 reach iteration one with both flexibilities zero and delta zero. Because i<N0, S3 was skipped; S8 then uses an undefined field. Check for the contradiction after S5 or before S8. Answer 362 also needs to reject a conflicting initial unit list. The actual SAT9 implementation has a guard before field division. |
| F047 | Answer 363(g): index the negative literals by L, not L'. Since the positive literal belongs to L', every printed clause is tautological. The family empty,{1},{1,2} supplies an explicit failure; the corrected clause x1 or -x2 excludes the unwanted predecessor. |
| F048 | Answer 364(c): the empty assignment needs four stars for the four variables of R'. Three stars are a transcription error; the classification and displayed weights are correct. |
| F049 | Answer 376, p. 623: clear LINK(c) after popping c from the exploitation stack. Otherwise a later shortened clause cannot be reinserted. The documented four-clause witness leaves a subsumption unperformed. SAT12 already clears the corresponding stack link. |
| F050 | Answer 376, p. 624: the timestamp test needs SIZE(c)-[TIME(l)!=T]. All nonpivot literals must be current, giving count SIZE(c)-1+[TIME(l)=T]. For C=(a,b,c) and a new clause (-a,b,c,d), the printed equality rejects the valid pivot. The stored reachable full-round witness supports the local calculation. |
| F051 | Answer 390(d): the clauses propagate walks of exactly j steps. On a single edge s--t with k=2, layers (1,0),(0,1),(1,0) satisfy the printed clauses and -t2 although the distance is one. Forcing s at every layer repairs the at-most-k encoding. The 2016 official replacement still has this defect. |
| F052 | Answer 390 introduction and (b): the claim of just n variables omits the auxiliary counters explicitly required by (18),(19). An internal vertex of degree four uses four additional variables for the at-most-two condition. The O(m) clause bound and induced-path argument remain valid. |

## Prior-report screen

Compared refreshed complete/current 4B and Fascicle 6 errata and the
historical TeX comparisons. Fascicle 6 offsets are 184 pages in the
main text and 364 in the answers. The 2017 theorem-reference correction
in 356(b), the terminology change in exercise 363, and the 2022 changes
to 376 concern different details. The 2016 replacement of answer 390
was read in full: both retained defects are present in it. Later nearby
changes to answers 379,388,392 do not repair them.

Fresh searches combined Knuth/TAOCP with cographs, exercise 343, the
clique local lemma/356, isolated vertices, survey propagation, pyramid
factorization/339, exploitation stacks, LINK/376, and graph-distance
encoding/390. No matching report of these defects was found.

The [RWTH 2021/22 seminar page](https://tcs.rwth-aachen.de/lehre/Help-Knuth/WS2021/)
lists several relevant exercises but contains no public verdict or
correction for them. Its topic-assignment colors do not constitute
correctness certificates or prior error reports.

Screened [tamnd/brain SAT entries](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4/7.2.2.2)
339,341,343,345,346,348,355,356,357,360,362,363,364,376,390. Most contain
unrelated generated answers or requests for missing context. Entry 356
already states the correct clique-index minimum for F040, as does the
book's own answer, but does not identify the printed exercise's index
error. Its proof does not diagnose either the overlap or uncovered-vertex
defect. The public correct formula is recorded here without claiming
priority for that formula.

Freshly read the relevant sections of the author's
[SAT9](https://www-cs-faculty.stanford.edu/~knuth/programs/sat9.w) and
[SAT12](https://www-cs-faculty.stanford.edu/~knuth/programs/sat12.w).
SAT9 checks for both zero flexibilities before computing a field;
SAT12 clears the popped clause's stack link and implements the timestamp
conditions through its special-case tests. These working implementations
are useful correction sources, not discovered reports of the book's
omissions. No absolute priority is established by this screen.
