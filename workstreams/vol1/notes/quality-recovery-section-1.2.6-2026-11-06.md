# §1.2.6: complete claim and exercise reconciliation

Recovery audit, 6 November 2026; checkpoint V1-X0994. Scope: every
main-text assertion, all 68 original exercises and every answer part,
including the mathematical additions in the errata. There is no added
exercise. Original printed 52–74 and 483–491 were directly viewed,
not merely read through the incomplete Markdown transcription. In
particular the transcription loses factorial-power marks and several
whole formulas; it is not the authority for the equations below.

This review accepts exact prior general proofs after reading them and
comparing their hypotheses and conclusions with the original. It does
not rerun their diagnostic examples. The four old checking programs
and their complete saved results were read: `check_binomial_base.py`,
`check_stirling.py`, `check_q_binomial.py`, `check_binomial_extras.py`,
and `results/binomial-base.json`, `stirling.json`, `q-binomial.json`,
`binomial-extras.json`. Their table and short enumeration checks are
supplementary; finite samples are not proofs of the identities.

## 1. A precise remaining mathematical interpretation

Answer 52, printed 489, first paragraph, states absolute convergence
and uniform convergence in bounded regions, with complex parameters
and z≠0. The earlier `abel-extensions.md` proves absolute convergence
and uniform convergence on compact subsets of a nonsingular analytic
domain. Its O(k^−2) majorant depends on keeping z away from zero and
on consistent local branches of the powers. That proof is sufficient
for the derivative identities, but does not establish uniform convergence
on every bounded region merely satisfying z≠0.

Here is an exact distinction. With x=n=−1, y=1 and real 0<z≤1,
the k-th summand of the answer's Abel series, including k=0 after
its prescribed cancellation, is

    t_k(z)=(1+kz)^−2.

Every term is defined and the series converges absolutely at every
such z. But sup_{0<z≤1} t_k(z)=1 for every k. Equivalently, taking
z=1/k² gives t_k(z)→1. A uniformly convergent series must have terms
tending uniformly to zero: subtract its two successive partial sums.
Consequently convergence is not uniform on this bounded set.

The same obstruction lies inside the bounded open analytic region

    |x+1|<1/4, |n+1|<1/4, |y−1|<1/4,
    0<|z|<1, |arg z|<π/4.

Here Re(y+kz)>0, so the principal powers of y+kz are consistently
defined. For k≥1 the exponent k−1 of x−kz is a nonnegative integer;
for k=0 cancellation gives y^n. There is no hidden undefined term
in this witness. The obstruction approaches the excluded boundary z=0.

This does **not** establish a new erratum: “bounded regions” may
implicitly mean regions whose compact closures lie inside the analytic
domain. That customary interpretation agrees with the existing proof.
The exact interpretation is therefore **partial**, not confirmed and
not a new candidate card. Exercise 52 and the previous blanket X0940
return to partial for this scope alone. X0072 stays checked for its
explicitly restricted O(k^−2) proof. The Hautus attribution is a
separate permitted source skip and cannot close this mathematical gap.

## 2. Proof references actually read

The following names abbreviate exact local proofs, all read in full:

| Name | File and sufficient scope |
|---|---|
| B | `binomial-identities.md`: definition, polynomial extensions, finite differences, binomial theorem and finite convolutions, elementary exercises. |
| C | `binomial-congruences.md`: formal-series Lucas proof including negative upper indices, Kummer carries and all rows without a multiple of p. |
| R | `rothe-abel.md`: polynomial Rothe/Abel identities, convergence of their generating functions, all five examples, Pfaff and rising powers. |
| S | `stirling-identities.md`: both bases, recurrences, inverse matrices, every finite identity and polynomial duality. |
| A | `stirling-analytic.md`: absolute/local uniform convergence of (59), sector remainder for (60), and its actual convergence exceptions. |
| E | `binomial-exercises.md`: multinomials, roots-of-unity filter, beta/gamma, combinadics, telescoping, bounds and absolute deviation. |
| BB | `bilateral-binomial.md`: iterated coefficient convention, first bilateral formula, counterexample to the second and a sufficient repaired convolution domain. |
| Q | `q-binomial.md`: finite and infinite q-products with domains, two Vandermonde forms, q-Pfaff and q-Dixon. |
| H | `abel-extensions.md`: Prüfer/tree proof of Hurwitz, symmetric Abel identity, analytic tail and derivatives. |
| G | `hypergeometric-summation.md`, supplemented by `quality-recovery-hypergeometric-decision-2026-11-06.md`: precise closed-form class, complete algorithmic proofs and generic binomial-prefix obstruction. |
| D | `binomial-double-sum.md`: finite coefficient-extraction proof for every allowed integer l,m in exercise 63. |
| I | `binomial-inequality.md`: both inequalities, equality conditions and every boundary of original and corrected exercise 66. |

The earlier source reviews were also read, not inferred from their labels:
`knuth-wilf-primary.md`, `binomial-primary-root-review.md`,
`binomial-identity-origins-root-review.md`, `hurwitz-root-review.md`,
`scherk-forstemann-root-review.md`, `dixon-primary-root-review.md`,
`rogers-primary-root-review.md`, `dougall-primary-root-review.md`, and
`macmahon-summation-root-status.md`. These support only their recorded
pages and propositions. They do not verify every historical assertion
or every theorem in a cited book.

## 3. Every main-text mathematical claim

| Original scope | Argument and hypotheses |
|---|---|
| Definition (1)–(4), ten triples, Table 1, Fig.8 | For k≥0, C(r,k) is the falling product divided by k!, a polynomial in r; for k<0 it is zero. Ordered choices counted k! times give the subset formula. The original ten triples include bcd and bce, despite OCR. Table 1 rows 0–9 are fixed by Pascal's rule and boundary 1; the saved exact check matches every printed entry. Fig.8 corresponds to four nonnegative coordinates of sum n−1; stars and bars gives C(n+2,3). At n=4 the layers have 1+3+6+10=20 balls. |
| (5)–(9), real extension and polynomial-identity rule | B proves factorial quotient, symmetry for nonnegative integral upper index, both absorption laws and Pascal for all integral lower indices. Divided forms exclude their zero denominators; their multiplied polynomial forms extend across them. Extension in two real parameters is applied one variable at a time. The 2021 real r≥k extension of (5) follows by gamma recurrence. |
| (10)–(12) | Pascal telescopes C(r+k,k); C(k,m) telescopes to C(n+1,m+1). Original n,m≥0 suffice; the later negative-n reading of (10) is empty on both sides. k²=2C(k,2)+C(k,1) gives (12), including n=0. |
| (13)–(15), finite and infinite binomial theorem | Finite product expansion counts choices, including exponent zero. For general r the coefficient ratio gives convergence for |x|<1; termwise differentiation gives (1+x)F'=rF and F(0)=1, uniquely F=exp(r Log(1+x)). The two-variable form uses a compatible branch and |x/y|<1. The printed ordinary real case satisfies this. The 2022 binomial strong-zero convention explicitly cancels the negative powers of zero in the finite form. |
| (16), Abel polynomial | R takes the leading homogeneous part of Rothe with r=hx, s=h(y+nz), t=hz. H independently counts rooted weighted functions. The empty-subset term is canceled to 1 before substitution, so zero parameters are included. |
| (17)–(20) | B reverses the falling product for upper-index negation, telescopes Pascal for the alternating prefix, combines negation/symmetry for (19), and cancels falling products for the product rule (20). Negative lower indices and out-of-range integer indices give zero on both sides; no division by those zeros is used. |
| (21)–(25) | B: finite coefficient convolution proves Vandermonde for all integral n; symmetry under the stated nonnegative integral r gives (22); repeated Pascal differences give (23). For (24), zero support or j=k−t and negation reduce it to Vandermonde. For (25), choose a subset by its (n+1)-st smallest element, or use the requested (24) substitution. The required 0≤s≤n integral condition is essential; exercise21 records the full correction. |
| (26), polynomial interpretation | R defines A_0=1 and A_k(r,t)=r∏_{j=1}^{k−1}(r−tk−j)/k! for k≥1. This removes apparent denominators before any parameter substitution. The special s=n−1−r+tn makes an n-th difference of a polynomial of degree n−1. The shift recurrence in s and induction in n then give infinitely many s values; polynomial identity proves the general formula. |
| Examples 1–2, including (28) | R explicitly shifts the lower index, applies the convolution and restores the prefactor. Both methods of Example2 produce δ_{n0}; the missing 1/(n+1) in the uncorrected intermediate expression is a known erratum. Finite support justifies every sum interchange. |
| Example3 and exercise30 alternative | R distinguishes the original j≥n support statement from the later finite j=0,…,n−1 replacement and reduces the inner sum to δ_{j0}. The corrected alternative uses (r,s,t,N)=(-1,2n−m,1,n−m) and gives C(n−1,n−m), valid at n=0 too. |
| Example4, (29)–(31) | For r+s−tn≠0, the displayed partial fraction and two uses of Rothe give convolution of A-polynomials. Polynomial continuation supplies the excluded hyperplane. The generating-function proof in R uses convergent series near the inverse branch x=1 and gives the same identity without singular division. |
| Example5, (32)–(33) | Finite triangular binomial inversion leaves only a_m: the inner alternating sum is δ_{mn}. Its diagonal is nonzero and hence the solution is unique. The result a_m=Σ_{j=0}^m(-1)^j/j! matches the earlier permutation formula. |
| (34)–(35) | C(k,0),…,C(k,r) form a polynomial basis, with ΔC(k,j)=C(k,j−1). Thus Δ^r kills degrees below r and multiplies the leading coefficient by r!. Applying this to C(s−tk,r), whose leading coefficient is (-t)^r/r!, gives (35). No lower-degree terms survive. |
| (36)–(38) | G proves the generic binomial-prefix obstruction in the stated hypergeometric class, not a claim about every conceivable special function. For each explicit negative integer m, C(m,k)=(-1)^k P(k); solve Q(k)+Q(k−1)=P(k), an invertible triangular polynomial operator with diagonal 2, to obtain (-1)^nQ(n)+constant. The m=-2 example gives (-1)^n ceil((n+1)/2). For (38), (k−m/2)C(m,k)=m/2[C(m−1,k−1)−C(m−1,k)] telescopes, including m=0. |
| Algorithmic paragraph and (39) | G plus the new full proof supplies Gosper's invariant, finite dispersion, pole elimination, degree bound and terminating linear system; proper-term creative telescoping; and the finite Hyper decision. Boundary sums and the effective coefficient field are explicit. The ratio of coefficients in (39) is rational. For a nonterminating nonsingular series its radius is infinity, 1 or 0 according as the number of upper parameters is ≤, =+1, or >+1 the number of lower parameters. Terminating and singular cases are separated. No runtime bound is asserted here by the book. |
| (40), q-generalization | Q defines the quotient for nonsingular q, or formally using q^r. Each (1−q^a)/(1−q) tends to a as q→1. For nonnegative integral upper index cancellation gives the Gaussian polynomial, degree k(n−k), nonnegative coefficients and leading coefficient 1 by the q-Pascal recurrence. Roots of unity are handled by that polynomial after cancellation. |
| (41)–(43), multinomials | E counts words with prescribed multiplicities, derives the finite multinomial theorem by distributing choices, and telescopes successive binomial factors. Empty products and zero counts give 1. The trinomial explanation of (20) holds first on nonnegative integer counts and then polynomially where appropriate. |
| Table2, (44)–(46), two examples | S defines the two triangular basis changes and derives their recurrences by multiplication by x, using x·x-underlined-k=x-underlined-(k+1)+k x-underlined-k. The cycle-insertion and block-insertion bijections give their interpretations. Rows 0–8 and both displayed degree5 expansions match the saved exact table check. |
| (47)–(50) | Composition of the finite triangular changes of basis proves both inverse matrices. Empty partitions/cycles, singleton blocks, one merged pair, one cycle and two nonempty blocks prove all special values, with the n=0 convention explicit. |
| (51)–(53) | Shift the rising-power polynomial by one and apply binomial inversion for the first pair. Partition by the block containing the last element for the second pair. Inclusion–exclusion counts surjections onto m labeled boxes for (53), including 0^0 and n=m=0. |
| (54)–(56) | S interpolates the degree2m diagonal polynomial at -m,…,m, with its negative nodes zero; the remaining Lagrange weight is C(m−n,m+k)C(m+n,n+k). Duality gives the other formula. Composition with (47) proves (55); recurrence telescoping proves (56), both sums 0≤k≤n as corrected in 2026. |
| (57)–(58), all diagonal extensions | With P_d(n)=c(n,n−d), Q_d(n)=S(n,n−d), recurrences give ΔP_d(x)=xP_{d−1}(x), ΔQ_d(x)=(x+1−d)Q_{d−1}(x). Zero initial values and P_0=Q_0=1 determine degree2d polynomials with leading coefficient 1/(2^d d!). They imply Q_d(x)=P_d(d−x). The d=2,3 expressions satisfy these same recurrences and bases. This extends only fixed nonnegative integral index difference, not two arbitrary independent indices. |
| (59), including arbitrary complex r | A derives the logarithmic generating function, bounds its coefficients by a power of log(k+2), and combines a beta factor O(k^(-Re z−1)) for absolute/local uniform convergence when Re z>0. A finite shift removes restrictions on r; no illegal continuation of a divergent sum is used. |
| (60), companion asymptotic | A expands the Laplace kernel at zero and bounds its Taylor remainder, giving the displayed power remainder uniformly in closed sectors |arg z|≤π/2−δ. For noninteger r the branch singularities at ±2πi force the full coefficient series to diverge. Positive integers terminate; negative integers instead give a convergent Laurent expansion outside a finite disk. The printed “not convergent” is read as the generic contrast, not as a claim excluding those explicit special cases. |

## 4. Every exercise and every answer part

The following rows include the answer's additional mathematical claims.
“Checked” concerns the stated mathematical scope, with the explicit
source skips in §6. Only 52 and 53 remain partial.

| No. | Parts and exact sufficient argument |
|---|---|
| 1 | B: C(n,n−1)=n for n≥1 by complementing the omitted element; formal n=0 gives zero on both sides. |
| 2 | The empty choice is unique, so C(0,0)=1, also the empty-product definition. |
| 3 | B: unordered 13-card hands count 52·…·40/13!=635013559600; the old exact arithmetic check agrees. |
| 4 | Prime valuation of that quotient gives 2^4·5²·7²·17·23·41·43·47, including complete cancellation of all other primes. |
| 5 | (10+1)^4 and Pascal row4 give decimal 14641 because each coefficient is below10, so there is no carry. |
| 6 | Upper-index negation gives rows (-1)^k, (-1)^k(k+1), (-1)^k(k+1)(k+2)/2 for k≥0 and zero for k<0; direct Pascal subtraction verifies each neighboring row. |
| 7 | Consecutive positive coefficients have ratio (n−k)/(k+1), above1 before the middle and below1 after it. Thus floor(n/2),ceil(n/2), with one index when n even. |
| 8 | Complementation reverses the nonzero row; B proves exactly the stated symmetry. |
| 9 | C(n,n)=1 for n≥0 and0 for n<0, because the lower index is then negative. |
| 10(a–f), including answer's block proof | C proves (1+x)^(pq+a)=(1+x^p)^q(1+x)^a in F_p[[x]], allowing negative q by the unique inverse series. Coefficients give Lucas for all integer n,k; k<0 vanishes. k=p gives(a); absorption gives(b); products of units give(c); Pascal gives(d), empty when p=2; iteration gives(f) for the stated finite digit expansions. The answer's block cancellation cancels only units modulo p and treats b>a separately. |
| 11, both valuation directions and carries | C uses v_p(N!)=(N−s_p(N))/(p−1); digit equations a_i+b_i+ε_i=c_i+pε_{i+1}, summed through the final carry, give exactly the valuation, not merely a lower bound. Zero inputs and carry chains are included. Exact Kummer and Knuth–Wilf source scopes retained. |
| 12, odd rows and general p answer | Lucas makes all entries nonzero mod p iff every digit below the leading digit is p−1. A deficient lower digit supplies k≤n violating this. Hence n=a p^m−1, 1≤a<p; for positive odd-only rows n=2^m−1,m≥1. |
| 13 | B telescopes Pascal to (10); n=0 and the later negative-n extension are separated. |
| 14 | k⁴=24C(k,4)+36C(k,3)+14C(k,2)+C(k,1); prefix summation yields the printed quartic-power formula, with zero base. This is an exact polynomial identity. |
| 15 | Finite choice expansion and the differential-equation proof in B establish the finite and convergent noninteger versions, with the required domain and constant term. |
| 16 | B reduces both sides to (-1)^(n+k−1)C(n+k−2,k−1), for positive integers n,k as specified. |
| 17 | Multiply the two convergent binomial series near zero and compare the finite coefficient of x^n; polynomial continuation proves all upper parameters. Negative n has zero coefficients. |
| 18 | With nonnegative integral r, replace C(r,m+k) by C(r,r−m−k), shift j=n+k, then use Vandermonde. Arbitrary integral m,n cause no unsupported terms. |
| 19 | Repeated ΔC(s+k,n)=C(s+k,n−1) gives the requested induction and its r=0 base. |
| 20, both requested deductions | B treats the zero-support cases first, then j=k−t and upper negation reduce (24) to Vandermonde. For (25), t=n−s and s'=-n−1 in (24), followed by integer symmetry, give precisely the printed right side. |
| 21, original objection and complete corrected answer | The two sides have degrees at most n and m+n+1; n+1 matching s-values do not imply equality. B proves the correction by multiplying x^(m+1)Σ_{k=0}^r C(r−k,m)(1+x)^k=(1+x)^(r+1)−Σ_{j=0}^m C(r+1,j)x^j by (1+x)^s. The missing subtraction is Σ_{j=0}^m C(r+1,j)C(s,m+n+1−j). The original m=0 exception fails already r=m=n=0,s=1 and is a known erratum. |
| 22 | R inserts s=n−1−r+tn into the A-polynomial convolution; the remaining nth difference has degree n−1 and is zero for n>0. The n=0 case is1. Corrected r factor and sign are included. |
| 23 | Pascal on the second binomial gives F_n(s+1)=F_n(s)+F_{n−1}(s−t), exactly the required implication. |
| 24 | Induction on n, followed by repeated forward s-shifts from the special value in22, gives infinitely many s; polynomial equality finishes. This avoids assuming a polynomial is determined by too few points. |
| 25, convergence, hint and branch | R bounds |A_k|≤D^k k^k/k!≤(eD)^k. The hint is the kth difference of degree≤k−1. Absolutely convergent double-series rearrangement gives 1=(1+w)^rΣ_j A_j[-w/(1+w)^(t+1)]^j. Put x=1/(1+w); z=(x−1)x^t has derivative1 at x=1 and hence a unique local inverse there. Apparent r denominators are polynomially canceled. |
| 26 | Differentiate25 and use dz/dx=x^(t−1)((t+1)x−t), yielding Σ C(r−tk,k)z^k=x^(r+1)/((t+1)x−t). The r=0 case follows by the polynomial coefficient continuation, not division by zero. |
| 27, both requests | Product of the two convergent A-series proves Example4 by coefficient comparison; product with the series of26 gives Rothe. All compared coefficients have finite convolution support. |
| 28 | R derives G_n(r,s)=C(r+s,n)+tG_{n−1}(r+t−1,s−t). Repeated substitution terminates after n steps, with total upper index decreasing by1 each step; the corrected shifted parameters in the answer match this invariant. |
| 29 | In Lagrange interpolation at0,…,n the kth denominator is k!(-1)^(n−k)(n−k)!. Multiplying the leading-coefficient formula by n! gives exactly (34). |
| 30 | R's corrected2023 substitution in Rothe gives C(n−1,n−m), valid for all n≥0 and integer m; n=0 is explicitly checked and invalidates the old unrepaired alternative. |
| 31, Pfaff, later integer-domain extension | Expand the third coefficient by Vandermonde, apply the product rule, then Vandermonde twice; R gives C(r,m)C(s,n). Negative m or n has empty support and zero right side. The exact historical Pfaff pages37–57 are distinguished from the old38–57 citation. |
| 32 | Replace x by -x in the falling-power expansion and cancel (-1)^n, giving Σ_k c(n,k)x^k=x-rising-n. |
| 33 | R rewrites rising powers as factorials times C(x+k−1,k), and applies negation/Vandermonde. All terms are polynomials, so arbitrary real/complex x,y follow. The equation's earlier origin is confined to the exact source review. |
| 34, rising and falling answer forms | Substitute r=x,s=y−1+nz,t=z−1 in Rothe and multiply by n!; cancel the k=0 factor first. R then changes signs to obtain the separately corrected falling-power version. |
| 35, both recurrences | Multiply each basis identity by x; x·x-underlined-k=x-underlined-(k+1)+k x-underlined-k gives the second recurrence, while multiplying the defining falling product by x−n gives the first. Compare coefficients in a genuine basis. |
| 36, ordinary and alternating | Evaluate (1+x)^n at1 and-1: 2^n and δ_{n0}, including n=0. |
| 37 | Half the sum of the two answers in36 gives the even-index sum: 2^(n−1) for n>0,1 for n=0. |
| 38, root filter, real form, m=3 example and m>n | E uses m^−1Σ_j ω^{j(l−k)}=[l≡k mod m]. Expand (1+ω^j)^n and conjugate-pair the terms to obtain the cosine expression. This remains valid when only one residue term exists, when n=0, and at roots with 1+ω^j=0 using the finite polynomial convention. Exact Ramus source scope retained. |
| 39, two first-kind sums and second-kind answer | Substitute x=1 and x=-1 into the rising-power polynomial: n! and δ_{n0}−δ_{n1}. The second-kind row counts all set partitions/equivalence relations by number of blocks; no missing closed form is asserted. |
| 40(a–c), beta | E evaluates B(x,1)=B(1,x)=1/x, adds integrands for(b), and integrates by parts for(c); x,y>0 make both boundary terms vanish. |
| 41(a–b), finite recurrence and gamma relation | Iterate40(c) and combine with40(b) to get the displayed beta product. Scale its integral and use the bound (1−u/m)^m≤e^−u with an integrable power majorant to obtain Γ, valid for real m→∞ as well as integer m. The ratio limit from §1.2.5 supplies B(x,y)=Γ(x)Γ(y)/Γ(x+y). |
| 42, limit order, first bilateral formula, second formula | E and BB take the lower-index limit before the upper-index limit, as explicitly printed. BB's Fourier integral equals C(r,w) by beta/reflection; Dirichlet estimates prove the first bilateral formula inside the unit-circle cut for Re r>−1, with its endpoint and terminating exceptions stated. C0007 refutes the unrestricted second formula at r=s=α=β=-1/2: only k=0 contributes1, but C(-1,-1)=0 under the prescribed limits. A sufficient L² convolution domain Re r,s>−1/2 is proved; maximal repair is not claimed. |
| 43 | Substitute t=u² to get B(1/2,1/2)=2∫_0^1(1−u²)^(-1/2)du=π. The beta/gamma relation and positivity of the gamma integral give Γ(1/2)=√π with its positive sign. |
| 44, duplication and meromorphic limits | Split B(a,a) at1/2 and substitute t=(1−u)/2 in the first half: B(a,a)=2^(1−2a)B(1/2,a) for a>0. The beta/gamma relation gives duplication. E applies it to obtain C(r,1/2)=2^(2r+1)/(π C(2r,r)). At poles it is an identity after meromorphic continuation, not arithmetic cancellation of two infinities; stated divergent special values are separated. |
| 45 | For fixed lower parameter, the gamma ratio from §1.2.5 gives the printed n→∞ asymptotic. At negative integral lower parameter the coefficient is zero under the prescribed limit convention, which is handled separately. |
| 46, two-variable asymptotic and central case | Apply Stirling to Γ(x+y+1),Γ(x+1),Γ(y+1). Relative error is O(1/x+1/y) as x,y→∞ independently, so no bounded-ratio hypothesis is needed. x=y=n gives C(2n,n)~4^n/√(πn). |
| 47, both identities and zero indices | Split the (2k)-factor product into even and odd factors and simplify; k<0 makes both sides zero. The half-integer specialization and central coefficient follow by the same product calculation. |
| 48, rational formula and noninteger extension | E gives the finite partial fractions by their residues, or integrates (1−t)^n t^(x−1) for x>0 and continues rationally. Negative integral x at poles is excluded before continuation. For noninteger n the term is asymptotic to a nonzero constant times k^(-n−2), so the ordinary series converges exactly for Re n>−1, with terminating exceptions and singular denominators separated. |
| 49 | Multiply the two binomial generating series and extract the specified finite coefficient. E tracks the powers and signs explicitly; no interchange of an unbounded double sum is required. |
| 50 | Expand in y−x; the inner nth difference kills every polynomial degree<n, leaving the leading coefficient1. n=0 is the empty base. E's alternate expansion proves the same identity. |
| 51, Abel proof, Torelli, symmetric and Hurwitz additions | E expands u=x+y and invokes50 coefficientwise; the factorial-power variant uses the same finite argument. H proves Hurwitz by weighted Prüfer trees plus the unique basin reaching root X; splitting a root of weight x+y into X,Y proves symmetric Abel. Empty trees have weight1 after cancellation. No nonnegative-weight restriction survives the polynomial proof. |
| 52, exact counterexample, convergence and derivatives | The requested n=x=-1,y=z=1 gives Σ(k+1)^−2=π²/6, while the finite-form left expression is singular. There is also a finite-valued witness: n=x=-1,y=2,z=1 gives left side1 and terms [(k+1)(k+2)]^−1((k+1)/(k+2))^k. The k=0 term is1/2, and each k≥1 term is strictly less than1/((k+1)(k+2)); telescoping proves the absolutely convergent sum is strictly less than1. H proves the O(k^−2) tail on compact nonsingular domains and both partial derivatives after termwise differentiation; the corrected coefficient is n, not r. The z-dependence is strict on x=n=-1,y=1,z>0 since its derivative is -2Σ_{k≥1} k/(1+kz)^3<0. The unrestricted “bounded regions” wording is the partial interpretation of §1; the vague “rare” agreement observation is not a classification theorem. |
| 53(a), all integer m; (b), proven prefix domain | For T_m=(m+1)(n−m)C(r,m+1)C(s,n−m), E proves T_m−T_{m−1}=C(r,m)C(s,n−m)(nr−(r+s)m). T_{-1}=0 handles the empty endpoint and oriented negative prefixes. Substitution r=1/2,s=-1/2 proves(b) for n≥1,m≥0, including the exceptional k=0 contribution. If (b) inherits(a)'s all-integer m, m=-1,n=1 gives0 versus1; the intended inheritance remains C0009candidate. Thus53 remains partial. |
| 54, inverse matrix and hint | Finite triangular matrix multiplication with alternating Vandermonde gives the Kronecker delta, hence the checkerboard-signed Pascal inverse. Every diagonal entry is1 and each finite leading principal inverse is unique; these compatible blocks define the infinite lower-triangular inverse, whose individual product entries are still finite sums. |
| 55, both inversions | The two basis changes in S are inverse triangular maps. Substitution of either displayed transformation into the other gives (47) coefficientwise; finite support justifies interchange. |
| 56, construction, uniqueness and both lists | E greedily chooses largest a_d with C(a_d,d)≤N; Pascal gives residual<C(a_d,d−1), so the next chosen digit is<a_d. Repetition decreases d and terminates; existence of each largest digit follows from C(a,d)→∞. Consecutive largest-digit intervals are disjoint and exhaustive, proving uniqueness by induction. N=0 has digits d−1,…,0. The two original lists and the errata's index-renaming convention match the saved exact enumeration. No asymptotic implementation cost is asserted. |
| 57, all coefficients | Expand log(j!)=Σ_{k≤j}log k in the finite mth difference, interchange finite sums, and telescope alternating Pascal coefficients. The difference is Σ_{k=1}^m(-1)^(m−k)C(m−1,k−1)log k for m≥1. Dividing by m! gives the requested falling-power coefficient a_m; its sign is (-1)^m(-1)^k as printed. |
| 58, all recurrences/products/convolutions and Cauchy addition | Q derives both q-Pascal laws, symmetry/reciprocity, negation, finite product and both q-Vandermonde weights by product splitting and polynomial continuation. The infinite product obeys (1+q^r x)F(x)=(1+x)F(qx); coefficient recursion proves it only on the correct |q^r x|<1 domain for0<|q|<1. C0006's q=1/2,r=-1,x=3/4 gives terms(-3/2)^k while the product is2/5. The transformed Cauchy formula has its separate |x|<1 condition. |
| 59, recurrence and closed form | E verifies the stated boundary values and Pascal recurrence for (n+1)C(n,k)−C(n,k+1). Induction in n makes the recurrence solution unique; out-of-range k uses the zero convention. |
| 60, multisets and all empty cases | Sort the choices a_1≤…≤a_n and map to distinct b_i=a_i+i−1. The inverse subtracts i−1, giving a bijection and C(m+n−1,n). Empty choices are one, while no objects with positive requested count gives zero. Exact Scherk/Förstemann reading retained. |
| 61 | S derives a(n,m)=n a(n−1,m)+δ_{nm} by the first-kind recurrence and inverse relation(47), with a(0,m)=δ_{m0}. Induction gives [n≥m]n!/m!, including m=0. |
| 62, ordinary and q-Dixon, Rogers and Dougall additions | Q proves q-Pfaff by expanding its extra Gaussian coefficient and applying q-Vandermonde. In the q-Dixon reduction the inner sum becomes a finite q-product containing(1−q^0) unless the remaining index h=0; that lone term gives the stated q-factorial quotient. q→1 gives ordinary Dixon. The read primary reviews verify the exact Rogers and Dougall formulas and the finite parameter substitutions connecting them to the book; their unrestricted analytic theorems are not claimed as newly audited. MacMahon's pages remain a permitted source skip. |
| 63, full integer l,m scope | D forms the m-generating series; for each coefficient k≤n and j≤m make it finite. Coefficient extraction gives (-1)^n(1+y)^(s−r)[t^(n+l)](1−yt)^(n+r), hence (-1)^l C(n+r,n+l)C(s−r,m−n−l). Laurent extraction accommodates negative l; negative m or negative target degree gives zero. |
| 64, partitions and original first row | Put the last element in an existing block or alone: kS(n,k)+S(n,k−1). The unique empty partition supplies S(0,0)=1 and all other impossible indices zero; the corrected first-row statement is essential. This recurrence equals the algebraic one, so induction identifies the count. |
| 65, all complex r and stated half-plane | A gives the full coefficient bound, beta integral, finite shift in r, and sector Taylor remainder described in §3. It proves both the convergent factorial expansion and the companion power asymptotic; no numerical agreement is substituted for convergence. |
| 66, original, broadened statement, equality and boundary | I compares logarithmic derivatives of the root products, with Y=0 allowed, and obtains a strictly decreasing sign-determining function from the extra1/x term. Its unique zero and endpoint signs give the second inequality and its equality; the order n−1 comparison and limiting endpoint give the first. n=2 is checked directly. Both final inequalities hold for y≥n−1,z>n−2. C0008 concerns only a false strict step in combined2005+2015 errata at n=2,y=z=1,x=2; the original1997 proof is distinguished. |
| 67, upper, lower and comparison | E applies the exact factorial bounds and product inequalities, yielding the printed upper bound, corrected lower ((n−k+1)e/k)^k/(ek) for k>0, and simpler (n/k)^k. The latest wording says “often sharper”; neither k=n nor other cases are claimed to improve the simple bound universally. |
| 68, centered absolute deviation and answer's extensions | E telescopes T_k−T_{k+1}=C(n,k)p^k(1−p)^(n−k)(k−np); splitting at a=ceil(np) gives2T_a. n=0,p=0,p=1 are direct zero cases with the printed strong-zero conventions. For real p outside[0,1], the absolute linear factor has one sign over0≤k≤n, so the first-moment identity gives zero; the right coefficient is out of range and zero too. The exact original de Moivre specialization assumes integral np. |

## 5. Additional analytic detail for the bilateral convolution

BB's sufficient condition Re r,s>−1/2 can be justified without an
unstated formal multiplication of infinite Fourier series. Its functions
f(t)=(1+e^{it})^r e^{-iαt} and g(t)=(1+e^{it})^s e^{-iβt}
on (-π,π), with the compatible branch, are square-integrable under
these conditions. Their endpoint behavior is bounded by a constant
times |π−|t||^{Re r} and the analogous s-power. Cut off small endpoint
intervals; the remaining function can be extended continuously and
periodically, with arbitrarily small L² error. The explicit Fejér
kernel proved in the recovery of §1.2.4 approximates that continuous
function uniformly by trigonometric polynomials. Hence these particular
f,g are L² limits of trigonometric polynomials.

Orthogonal projection onto frequencies -N,…,N cannot increase the
L² norm: subtract its finite polynomial and expand the integral of the
squared absolute value. It therefore converges in L² to each of f,g,
using the polynomial approximation just proved. Cauchy–Schwarz shows
that the integrals of the products converge, since
|∫(f_Ng_N−fg)|≤||f_N−f||₂||g_N||₂+||f||₂||g_N−g||₂.
Finite Fourier multiplication gives the convolution coefficient;
Cauchy–Schwarz for the coefficient sequences makes its limit absolutely
convergent. The coefficient integral already evaluated in BB identifies
the result. This proves the safe domain, including each interchange;
it does not rescue C0007 outside that domain or claim maximality.

## 6. Errata, history, source limits, and final status

All four local errata layers were compared for printed52–74/483–491.
Their complete relevant blocks and fingerprints are saved in
`../results/quality-recovery-binomial-errata-2026-11-06.json`, including
the malformed `xPage k4851` header for answer22, identified by the
unambiguous corresponding err1 entry. The known corrections include
the 2022 strong-zero convention,2023 replacement for answer30 and2026
finite bounds in(56). The later JLMS(2) correction does not affect
the original1997 caption, which already says33. The source-specific
Halayudha correction likewise is not retroactively a first-print error.

The strong-zero addition on printed57 expressly concerns C(r,k) for
k<0 or k>r=floor(r), strong enough to cancel negative powers of zero.
It broadens the available convention beyond false Iverson brackets,
but does not expressly extend it to every ordinary zero coefficient
times a divergent sum. It therefore supplies relevant context, without
settling the separate partial interpretation of §1.2.3 equation(18).

Permitted bibliography skips remain explicit: Dickson383–384;
Ramshaw223–226; the separate Hautus provenance; unretrieved parts of
the Rothe/Schweins/Gauss/Cauchy/Jacobi/Heine and q-history references;
MacMahon274–288; Lovász13.31a and Redheffer62–64; de Moivre101,
Poincaré56–60 and Diaconis–Zabell284–302. Exact mathematical links
to Concrete Mathematics or volumeII are replaced here by the stated
independent proofs, without claiming those external pages were read.
The main-text historical priorities and broad descriptions remain
partial wherever no exact primary proof has been recorded. Neither
the table-caption papers nor the bibliography are claimed as audited
in their entirety. Relevant previously verified primary passages are
retained at their exact scope by the source reviews listed in §2.

Result: all68 exercise/answer entries and all mathematical main-text
assertions have explicit proof or gap maps. Exercise52 is partial only
for the uniform-domain interpretation;53 retains its existing C0009
domain candidate. The other66 exercises are checked in the stated
mathematical scope, with named bibliographic skips. C0006,C0007,C0008
and C0009 retain their previous statuses; no new finding is created.
X0940 is partial for52, while its complete earlier subproofs remain
usable. The new algorithm proof closes an evidentiary omission in
the former source-scope-only explanation. No mathematical jobs were
run; only eight short source-page renders were made with nice15.
