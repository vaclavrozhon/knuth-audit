# Publication review: C0057–C0070

Reviewed November 12, 2026. Thirteen cards remain supported. C0067 is
dismissed because its counterexample misreads the printed definition;
the separate dismissal note gives the decisive original and calculation.
All relevant current and historical errata were checked again. No
matching additional correction or explicit prior TAOCP report was found
for the retained cards. Priority is not established.

| Card | Assessment and limits |
| --- | --- |
| V2-C0057 | The final displayed mean has a free left index `m` where all right-hand quantities and the recurrence use `n`. Since `A_1=2` and `A_2=8/3`, the indices cannot be independent. Retain as a local subscript typo. |
| V2-C0058 | Exercise 23 supplies positive coordinates in a quarter disk, so the prescribed sine in answer 31(c) always has the same sign. For the stated pool size and 682 returned X entries, the expected two-pass transformation gives covariance `-(682/1024)[3(sqrt(3)-1)/pi]^2=-0.325469...` between normalized block sums. The exact printed scale changes it by less than 0.1, so it remains below -0.22. The argument includes rare sign reversals in the scale numerator. Retain for this specific recipe and output ordering. Brent had already published the general nonzero-mean-transform problem and random-sign remedy; neither that idea nor a defect in every Wallace implementation is claimed as new. |
| V2-C0059 | With two coordinates, base 2 and interval `[0,1/4)`, the inner box is empty but the printed product is 1/4. The outer equality can likewise exceed probability 1 at a boundary. Clipped grid intervals repair the proof, and the limiting distribution theorem survives. |
| V2-C0060 | The explicit period on p. 155 has upper-half bit frequency 1/4 at even positions. The answer's `(X_n+U_n)/2` therefore gives 1/4, whereas the exercise asks for 3/4. Complementing `X` repairs the direction and preserves three-distribution. The 2024 correction changes different pair indices. |
| V2-C0061 | Changing a term can affect up to `k` overlapping windows. For `k=2,n=16`, the displayed square-position replacement changes seven of the counted pairs, exceeding 4. A bound of order `k sqrt(n)` suffices and preserves complete uniform distribution. |
| V2-C0062 | W6 increments the counter before using it, so its first value is `V_1=1/2`, already contradicting the required lower-half majority. Each node contributes `floor(j/2)` lower-half values. Using `V_(k-1)` gives `ceil(j/2)` instead and preserves the distribution proof. The 2002 correction to the exercise's index is separate. |
| V2-C0063 | If every selection rule selects every term, blocks at depths one and two emit only 3+12 terms. At `r=q=1,N=16`, the cited element has depth three, contradicting the intermediate bound of two. The same boundary occurs for arbitrarily large `N=4^(q+1)`. A weaker capacity bound proves the theorem; the report does not claim the final constant 2 is false. |
| V2-C0064 | Reflection about 1/2, with the initial zero retained, gives a different admissible point sequence with exactly the same multiset of gaps at every stage. Its second point is `log_2(4/3)` rather than `log_2(3/2)`. The uniqueness claim can concern gap multisets, not the point sequence. The minimax conclusion is unaffected. |
| V2-C0065 | A point indexed `m` is present only when there are `m+1` points. With `n=2` and points `0,1/2,1/4,1/8`, the printed birth index compares a final gap of 1/8 to a minimum of 1/4. Adding 1 inside both relevant index expressions repairs the harmonic-sum proof. |
| V2-C0066 | For the legal computable injection `s_j=j`, the proposed initial boundary remains zero forever; `(1,0,2,3,...)` also gives a positive fixed boundary of one. Starting at at least two forces growth because `2^a-1>a`. The selection theorem survives. |
| V2-C0067 | Dismissed. The original counts `j<=n`, while the alleged empty-prefix counterexample counts `j<n`. For `N=1,n=0` and `U_0<u<1`, the original count is 1, so its strict inequality holds. See the dedicated dismissal note. |
| V2-C0068 | With one deterministic zero variable and `t=2`, the non-strict probability event has probability 1 and the stated bound is 1/2. Positive variance or a strict event repairs the boundary. The separate deterministic case in the downstream application remains valid. |
| V2-C0069 | The construction substitutes a prediction-success indicator for a predicted bit. For `N=1,S={1},A(B)=B`, the printed construction predicts zero with certainty. Using the predictor itself returns one. The answer to exercise 41 has the same distinction between output probability and success probability. The reduction statements remain true. |
| V2-C0070 | Retain explicitly as a research-status update, not a new theorem. Shen, Uspensky and Vereshchagin's 2017 Theorem 203(b) states the binary every-prefix property. The audit's independent-coordinate construction and bounded martingale-difference estimate verify it directly for all bases in the book's real R6 definition. The probability of all positive prefix excesses is positive after 4096 initial lower-half variables. This concerns frequency selection, not the stronger modern betting notion of Kolmogorov–Loveland randomness. |

Original pages re-inspected: 140, 153, 155, 160, 163–165, 171–172,
181–183, 589–590, 594–598. For C0058, Brent's section 5.2 was opened
again and viewed in its original page. Its discussion is prior work on
the mechanism, not an explicit report identifying this TAOCP answer's
angle construction. The 1997 implementation also changes angles inside
a pass and is not the exact printed recipe.

For C0070, the 2017 book's original pp. 307–308 were viewed again from
the previously retrieved excerpt. The public PDF could not be opened
by the web tool because of its size; this is not evidence of its absence.
The elementary real-variable proof in the existing note was reread in
full, including stopped adaptive selections and the summable deviation
bound. No new numerical experiment was needed.

Public query families paired Knuth/TAOCP with Wallace/590/sine/random
signs/31(c), 589/A_m, distribution boxes/153, square positions/k-tuples,
Wald/165/depth, 3.5–28/alternating bias, Ramshaw/uniqueness/reflection,
subsequence/598, discrepancy/3.5–39/empty prefix, Chebyshev/zero variance,
P2/predictor and R6/Shen/counterexample. Searches were inspected on the
review date. Unrelated results and reproductions of the book were not
counted as independent reports.

Relevant primary sources:

- [Brent's discussion of Wallace generators](https://maths-people.anu.edu.au/~brent/pd/rpb213.pdf), section 5.2.
- [Brent's original vectorized implementation](https://maths-people.anu.edu.au/~brent/pd/rpb170tr.pdf), section 7, already archived and inspected.
- [Shen, Uspensky and Vereshchagin](https://www.lirmm.fr/~ashen/kolmbook-eng-scan.pdf), Theorem 203(b), pp. 307–308.
- [Shen's 1988/1989 paper](https://www.lirmm.fr/~ashen/mathtext/1988/english.pdf), the earlier biased-product method; not attributed an explicit every-prefix theorem.
