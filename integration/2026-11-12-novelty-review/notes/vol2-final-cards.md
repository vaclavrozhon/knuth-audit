# Volume 2: final twenty confirmed cards

Reviewed on 2026-11-12 against the third edition, first printing (1997).
All twenty cards are retained. Each listed report and its short argument
were read again, and the relevant original typesetting was inspected.
The four applicable official errata layers were checked against the
refreshed source manifest. No matching prior report was found in this
search. This is not a claim of priority or of inspecting a later physical
printing.

| Card | Reassessment |
| --- | --- |
| V2-C0240 | Algorithm X on p. 557 lacks the permitted one-symbol case. For m=k=1 its initialization is all zeros and X2 cannot choose an index with a positive entry. Return zero before X2. This is only a degenerate endpoint; ordinary alphabets are unaffected. |
| V2-C0242 | For the permitted modulus 1, Theorem P has equality in its allegedly strict error bound, and its second proof drops a nonzero delta term. The Dedekind-tableau bound also fails at h=k=1, with one step versus log_phi(1)=0. The main formulas remain correct. These are minor endpoint qualifications. |
| V2-C0245 | The Seysen citation on p. 118 ends at 375; the publisher gives Combinatorica 13 (1993), 363–376. This is bibliographic only. |
| V2-C0247 | The 26.8N coefficient on p. 340 disagrees with the program's 19T+6 cost and its Fibonacci worst case. For N=28, inputs 165580141 and 267914296 require 41 divisions and 785 cycles, above 769.4. The asymptotic leading coefficient is 19 ln(2)/ln(phi)=27.36798…, not 26.8; the gcd program remains correct. |
| V2-C0248 | The composed selection rule on p. 597 omits the first rule's test on the current position. Taking R to select even indices and R-prime to select everything makes the printed rule select odd positions too. Multiply the two Boolean tests. The closure theorem remains true. |
| V2-C0249 | The harmonic remainder on p. 594 is O(p_n/n), not generally O(1/n). The permitted distinct points U_j=1−2^(−j) give p_n=(2n−1)/2 and an error at least (2n−1)/(8n). The main lower bound follows directly by dividing by the harmonic sum; alternatively separate infinite limsup first. |
| V2-C0250 | The two normalized terms on p. 596 need a plus between them. The 2-distributed period 0011 gives left side 1/2 and printed product 0 for n divisible by four. The later upper bound already uses the intended sum. |
| V2-C0251 | N4's ENTX 1 on p. 219 discards the nonzero trailing register. With radix 100 and the two recorded normalized inputs, the exact sum 1.000049500001 is nearer 1.000050, but the original and 2002-corrected programs return 1.000049. The instruction trace and exact neighbor distances were rechecked; the known opposite-sign correction does not touch N4. Preserve whether old X was nonzero. This does not transfer the old timing bound to modified code. |
| V2-C0252 | Under the stated free quarter-turn convention the radix-four FFT count on p. 700 is two too large for every even exponent n>=2. A four-point transform uses zero counted products, not two. The count is (9n−26)2^n/24+4/3; the propagated 1024-point totals on p. 710 become 10928 real multiplications and 25944 real additions. Transform correctness is unaffected. |
| V2-C0253 | Answer 50 on p. 708 needs Lemma T, not L, for the flattening bound. Its Winograd citation needs journal volume 23, not 3, as the publisher and answer 38 confirm. The rank conclusion is correct. |
| V2-C0254 | Answer 39 on p. 705 omits beta1 from the quadratic constant: b=beta1+alpha_m. For w1=x²+1 and w2=(x²+1)², the printed formula produces constant coefficient 2 instead of 1. The representation theorem is unaffected. |
| V2-C0255 | The answer for arbitrary P on p. 711 confuses the degree of its minimum polynomial with the dimension of its representation. For P=I2 the printed tensor rank is 1, while its identity slice forces rank 2 and a two-term diagonal decomposition attains it. For diag(0,0,1,1) the discrepancy is 2 versus 4. The cyclic/companion-matrix theorem remains valid. |
| V2-C0256 | The last paragraph of answer 56, p. 711, needs rank(R+Rswap)>=rank(T), not the sum of the two separate ranks. The following row-deletion argument already proves the correct statement. The theorem survives. |
| V2-C0257 | Answer 67 has inconsistent one-based indices in its length mn+1 construction, a C coefficient labelled B, missing diagonal indicators in parts (c) and (g), and a missing extra d in the approximation order in (g). The m=n=2 construction already fails as printed. Use the corrected indices, identity block, and order 2d+e+2 recorded in the report; the border-rank conclusions are not refuted. |
| V2-C0258 | The assertion that all second partial derivatives cost at most 9m+3d multiplications and 4d divisions is false. The product of twenty variables uses m=19,d=0, but its 190 distinct degree-18 mixed partials are linearly independent modulo affine polynomials. Each multiplication adds at most one dimension, so 171 multiplications cannot produce them. Repeating the scalar differentiation construction gives one Hessian row. The local p1-prime times y_r also needs y1. |
| V2-C0259 | The claimed exact addition count in answer 69 gives 22 at n=2, versus one subtraction for its specified base case. In answer 70 the claimed determinant-only saving removes all two multiplications at n=2, leaving an impossible affine computation of a quadratic determinant. These refute the exact counts, not their asymptotic orders; no general replacement count is asserted. |
| V2-C0260 | Answer 4.7–15 on p. 722 reverses an exponent: the parenthesis needs z^(k−1). With U=z/(1+z), even the first printed iterate is z²/(1+z), rather than U. The integrated identity immediately preceding it is correct. |
| V2-C0261 | The polynomial-in-alpha argument on p. 723 needs normalization by the nonunit constant term. For U=2+z the induced series has linear coefficient 2^alpha. Divide out the common factor U0^(x+n alpha) before using the polynomial identity principle. The desired coefficient identity is correct. |
| V2-C0262 | The online composition route on p. 720 requires V1 nonzero. The allowed series V=z² cannot be normalized by V1 or reverted as an ordinary series. Qualify this route or supply another case; the offline method remains valid. Its explanatory invariant also needs V^n rather than V^N during iteration n. |
| V2-C0263 | The gamma-distribution index subentry on p. 741 incorrectly repeats the floating-point-distribution pages 253–264, instead of the gamma pages 133–134 and 140. The m-ary index entry on p. 749 misspells exponentiation as exponention. Both are navigation/editorial defects. |

For C0251, the saved one-case machine execution was inspected, not rerun.
Its register snapshots independently agree with the manual trace, and
the two exact distances are 500001/10^12 and 499999/10^12. For C0258 the
lower bound is a symbolic vector-space argument in the book's cost
model, not a count of output-storage instructions or numerical tests.

## Prior-publication check

The refreshed `all2-prepre`, `all2-pre`, `all2`, `err2`, and current TeX
contain no matching correction. Nearby changes concern X's reference,
answer 30 punctuation, the 2002 opposite-sign MIX branch, matrix
multiplication records, the FFT's in-place layout, Kaltofen's complexity
bound, and different power-series formulas. These do not fix the cards
above. The original reports additionally record second-edition errata
that introduced several of the same formulas; introduction of a formula
is not its correction.

Public searches combined Knuth/TAOCP with the individual section and
answer numbers, unary Algorithm X, unit-modulus Theorem P, Euclid 26.8,
ENTX/N4 and rounding, selection-rule composition, parity and the missing
plus, harmonic remainders, FFT radix-four counts, minimum-polynomial
tensor rank, improvable tensors, all second derivatives/Hessians,
determinant operation counts, power-series iteration/composition,
induced-series polynomial dependence, and exponention. No matching
public error report was returned. The Hessian-related literature returned
by search addresses derivative estimation and sparse Hessians, not this
particular assertion. General implementations and copies of the book
were not treated as independent reports.

The following primary publisher records were opened and agree with the
bibliographic corrections:

- [Seysen, Simultaneous reduction of a lattice basis and its reciprocal basis](https://link.springer.com/article/10.1007/BF01202355):
  volume 13, pages 363–376, September 1993.
- [Winograd, On the number of multiplications necessary to compute certain functions](https://onlinelibrary.wiley.com/doi/10.1002/cpa.3160230204):
  volume 23, pages 165–179, March 1970.

This completes the review of all 226 baseline-confirmed Volume 2 cards:
223 retained, one previously publicly reported, and two withdrawn.
