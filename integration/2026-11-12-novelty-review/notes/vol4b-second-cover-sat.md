# Volume 4B: exact cover, SAT, restarts, and local-lemma findings

Publication review, 2026-11-12. Rechecked F017–F032 against the November
2022 second-printing PDF on pp. 99–100,148,330,468–469,579,609,611–612.
Retain fifteen findings; withdraw F025 after discovering a mistranscribed
prime. Detailed existing proofs and finite verification records were
reused without repeating their large enumerations.

| Finding | Independent reason and scope |
| --- | --- |
| F017 | The doomsday recurrence needs D(1)=2 to count the root and solution leaf. This affects ordinary instances: the five distinct options a,b,c,ab,bc give seven search-tree nodes while the printed bound is six. The corrected initial sequence is 1,2,3,4,6,8,10,14,19,25,33,43. Its periodic constants become (200,263,350,464,608)/96; the exponential rate is unchanged. |
| F018 | Answer 180, p. 468, first confines i_2 to o_2,o_3,o_4,o_5, then incorrectly adds it to o_6. Delete that occurrence. The strict staircase rows 1000,1100,1110,1111,0111,0011,0001 satisfy the intended conditions. The known 2026 correction to the exercise does not repair this answer. |
| F019 | Answer 187(b), p. 468: differentiating the defined integral gives T_(r,s)'=exp(z)T_(r,s)+z^r exp(sz). The displayed general identity lacks exp(sz); specializing explicitly to s=0 also repairs the line. The requested special case is unaffected. |
| F020 | Exercise 189, p. 148: R(z) needs a minus sign in front of the integral. At z=0 its definition is -g, whereas the printed integral is +g. Absolute-value estimates survive. |
| F021 | Answer 189(c), p. 469: substitution x=exp(t)-1 gives the leading term g/e, not g/3. The following maximum-modulus integrand also needs exp(-exp(uz)); its printed positive exponent already disagrees at z=0. These are errors in one displayed analytic decomposition. |
| F022 | Answer 189, p. 469: the first integral for g_k requires denominator (k-1)!, not k!. Integration by parts supplies the factor k needed to match the second integral. The cited Asakly et al. paper, Corollary 4, has the correct factor. |
| F023 | Answer 191, p. 469: subtract e from the incomplete-gamma series. At z=0 the printed series equals e, although the probability generating function has zero constant coefficient. Its derivatives and reported moments are unaffected. |
| F024 | Answer 164, p. 579: Algorithm R can take exponential time on 2SAT, contrary to T_n=n. Use m disjoint three-variable implication cycles followed by an unsatisfiable two-variable core. With the permitted first-clause tie rule, the two autarky tests fail, both branches re-solve the remaining core, and R2 visits satisfy C_0=3, C_m=5+2C_(m-1). Thus C_m=8*2^m-5 for n=3m+2. This does not concern other 2SAT algorithms. |
| F025 | Withdrawn: the original defines l' -> l, which is already the orientation needed for both the in-degree bound and binary-clause test. The previous audit reversed it by misreading the prime. See the separate dismissal note and corrected verifier. |
| F026 | Answer 162(b), p. 579: a strong component must be consistent to define an autarky. The two clauses (a or -b or c), (-a or b or -c) give one component containing all six literals, in the actual printed orientation too. Reversing the graph in the old audit did not affect this witness. |
| F027 | Answer 307(a), p. 609: multiply E_(N_j) by the probability of reaching run j, namely the old alpha. For p_1=p_infinity=1/2 and all cutoffs one, the expectation is two; the printed partial sums 1,7/4,19/8,47/16 diverge instead. |
| F028 | Answer 307(b), p. 609: the product of the first j-1 failure probabilities is Pr(X>T_(j-1)), not Pr(X>T_j). Already j=1 has empty product one versus tail probability 1/2 in the preceding example. The subsequent expected-cost expansion uses the correct product. |
| F029 | Answer 306(h), p. 609: N*=infinity does not imply the claimed n' exists. The book's own example (j) has ell(2)=4 and q_N ell(N)=3-2^(2-N)<3. Begin instead with E_infinity=infinity and argue by contraposition; the theorem itself is correct. |
| F030 | Answer 321, p. 611: in the opposite-pair mass replace 2 theta' (1-c)^3 by 2 theta' c(1-c)^2; in the all-four mass restore the factor two before theta^2 c^2. With multiplicities 1,4,4,2,4,1 the printed masses sum to about 1.79553 at p=0.3. The corrected expressions match the book's numerical line and follow from independently turning on missing events in the boundary distribution. |
| F031 | Answer 322(c), p. 612: the second solution needs nu=1/3, not 2/3. Its c=0,c'=1/2,d=1,d'=0 then have both weighted means 1/3; the printed weight gives 1/6 and 2/3 and violates the constraint. |
| F032 | Answer 322(a), p. 611: interchange W and Y in the right diagram. After conditioning on Z, C depends on Y and D on W. The product underneath is correct. |

## Prior-report screen

Compared the refreshed all4b/err4b, all4f5/err4f5, and all4f6/err4f6
layers with the historical TeX comparisons. Dancing Links answer pages
468–469 correspond to published Fascicle 5 pages 276–277; SAT answer
pages 579,609,611,612 correspond to Fascicle 6 pages 215,245,247,248.
The 2019 correction to 189(a), the 2026 correction to exercise 180,
the added OEIS reference in answer 185, and the 2024 correction to
answer 318 do not repair the retained findings in this block.

Fresh searches combined Knuth/TAOCP with doomsday bounds, Gould numbers,
Gompertz integrals, blocking graphs, Algorithm R/2SAT, exercise 164,
restart exercise 307, and the probability table in exercise 321.
No matching prior report was found. F025 requires no novelty claim
because it is not an error in the book.

[Eppstein's original Algorithm X analysis](https://11011110.github.io/blog/2008/01/10/analyzing-algorithm-x.html),
including its comments, concerns structural and exponential bounds;
it does not report the book's exact doomsday initial-value error or
answer 180's extraneous item. The cited
[Asakly et al. paper](https://math.sun.ac.za/swagner/gould.pdf) already
has the correct integral normalization. The prior downloaded copy and
source comparison were reused after a fresh retrieval timed out.

Screened [tamnd/brain](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4)
Dancing Links entries 180,181,187,189,191 and SAT entries
162,164,306,307,321,322. Most are unrelated generated answers or
criticisms of those answers. Entry 162 discusses two-element autarkies
without reporting the book's strong-component omission. Entry 164 gives
a weaker exponential upper bound without a lower-bound counterexample
or a report of the incorrect linear claim. None reports these retained
defects. This screen does not establish absolute priority.
