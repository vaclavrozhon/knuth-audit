# Volume 4B: first matching and probability findings

Publication review, 2026-11-12. Retain F001–F016, C003, and C004.
The source is the PDF identifying itself as second printing, November
2022; its original typesetting was checked on pp. 24–25,27,149,374,
390–391,393–395,470–471. No physical-copy inspection is claimed.
Existing author-draft comparisons and detailed arguments were reused.

| Finding | Independent reason and scope |
| --- | --- |
| F001 | Exercise 7.2.2.1-197(a,b), p. 149: use the individual bound a_j instead of a_n. At n=2 with bounds (1,2), the printed conditions permit t_1=t_2=2 and produce the forbidden permutation 21. |
| F002 | Answer 7.2.2.1-201(b), p. 471: for even n there are four permutations moving everybody, including the two perfect adjacent-swap matchings, and L_n-2 with fixed points. At n=4 these derangements are 2143,2341,4123,4321. The total L_n+2 is correct. |
| F003 | Answer 7.2.2.1-196(i), p. 470: after the forced X_9 Y_9 choice, X_1 has two remaining options and X_2 four. The minimum-remaining-values rule therefore cannot choose X_2 next; the example needs X_1. |
| F004 | Answer 7.2.2.1-196(h), p. 470: both floor expressions need factorial signs. For n=4 with bounds 2444 the product of available choices is 2*3*2*1=12, not 2*3=6. The main-text expression is correct. |
| F005 | Answer 7.2.2.1-196(h), p. 470: the printed series sums to 4e+3. To obtain the stated 4e-1, replace the initial six by two, or omit the term 4/1!. The exact preceding update formula supports this correction. |
| C003 | Answer 7.2.2.1-200(b), p. 471: for the polynomial xy over the field with five elements, the zero probability is 9/25, attaining 1-(1-1/5)^2. The first strict inequality must be non-strict. For one variable the next inequality is also attained. The conditional guarantee concerns a random evaluation of a fixed nonzero polynomial; the final error bound below 1/2 survives. |
| F006 | MPR 121(d), p. 24: entropy requires E(log_2(1/y(Y))), not E(log_2(1/Y)). A variable identically equal to two has entropy zero but the printed expression is -1. |
| F007 | MPR 123, p. 25: if Z=A?Y:X and Pr(A)=p_k, its mass function is p_k*y(t)+(1-p_k)*x(t). The displayed mixture interchanges these weights. The later Bayesian update uses the intended weights. |
| F008 | MPR 121 and introduction to 124, pp. 24–25,390: the expectation identities require y(t)=0 whenever x(t)=0. With X=0 surely and Y uniform on {0,1}, E(rho(X)*log_2(rho(X)))=-1/2 while the divergence sum is infinite, and E(rho(X))=1/2 rather than one. For f=1 the introductory sampling identity also fails. The finite-divergence theorem in 124 already enforces the missing support condition. |
| C004 | Answer MPR 124, p. 390: after the known statement correction, the proof still needs the triangle inequality and expectations. With x=y=(1/2,1/2), f=(0,1), n=2, its random squared error is zero or 1/4, not its variance 1/8. The existing positive-support witnesses also refute the signed equality and the pointwise tail bound. The corrected theorem is true. |
| F009 | Answer MPR 127(b), p. 391: at theta=1/3, n=3k+1, the omitted rounding contribution tends to -1/3; at n=3k it tends to zero. It cannot fit O(1/n). Add -frac(theta*n)*log_2((1-theta)/theta), or use O(1). The final order estimate is unaffected. |
| F010 | Answer MPR 130(e), p. 393: the joint-density factor needs ((z-q*y)/p)^2, not (z-q*y/p)^2. This follows directly from the preceding transformed interval. At p=q=1/2,z=1,y=0 the factors disagree. |
| F011 | Answer MPR 130(e), p. 393: the integral's value needs a factor pi. At p=q=1/2,z=0 it is four times the integral of (1+y^2)^(-2), hence 2*pi rather than two. The final Cauchy law is correct. |
| F012 | Answer MPR 132(a), p. 393: the second upper hypergeometric parameter is -n, not -N. At N=4,K=2,n=1 the printed expression is 1/2+2z+z^2, although the probability generating polynomial is (1+z)/2. |
| F013 | Answer MPR 132(b), p. 393: the variance lacks a factor K. For N=4,K=2,n=1 the draw is a fair bit with variance 1/4, not the printed 1/8. |
| F014 | MPR 134(b) and answer, pp. 27,394: two independent fair bits with m=1 and epsilon=9/10 differ with probability 1/2, exceeding 2*exp(-81/50). The pooled-sample threshold is epsilon*m/2, not epsilon*m; the repaired exponent -epsilon^2*m/2 suffices for part (c). The previously inspected April 2026 publisher preview still has the defective statement. |
| F015 | Answer MPR 137(d), p. 395: for x<m the formula needs c-m+2*max(0,x-c). With median m=1, c=0, x=-1, the difference of distances is -1, not -3. The later lower bound and theorem remain true. |
| F016 | Answer MPR 28(b), p. 374: the endpoint perturbation uses epsilon=-min(p_(n-1),1-p_n), not delta. For the probabilities 1/4 and 3/4, epsilon=-1/4 gives the induced product change delta=-3/16. Substituting -1/4 for delta would make probabilities negative. |

## Prior-report screen

Compared the refreshed `all4b`, `err4b`, `all4f5`, `err4f5` layers and
the archived TeX source comparisons, using the published Fascicle 5
answer offset of 192 pages and its main-text offset of two pages for
Dancing Links. The standalone 2019 pre-fascicles have different offsets;
they were not confused with the published fascicle. Nearby corrections
to the divergence terminology, answer 198's inequality, Baxter
permutations, and the MPR 124 statement do not repair these findings.
In particular the July 15, 2025 entry for MPR 124 adds an expectation
to the statement on p. 25, without correcting the proof on p. 390.

Fresh queries combined Knuth/TAOCP with exercise 197's bound, answer
196's series, entropy, Cauchy integration, hypergeometric variance,
two-sample bounds, rounding at MPR 127, circular matching, and importance
sampling. No matching prior report was found. The
[Chatterjee–Diaconis paper](https://arxiv.org/pdf/1511.01437), Theorem 1.1
and its proof, already uses the correct triangle inequality and expected
errors. This is the book's cited source, not a report of its defective
transcription. Its previously checked support assumption was reused.

Screened [tamnd/brain's Dancing Links entries](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4/7.2.2.1)
196,197,200,201. The first two describe an unrelated problem. Entry 200's
"corrected solution" replaces an earlier symbolic approach with the
standard randomized test; it does not report the book's strict bound.
Entry 201 contains an independent incorrect omission of the two cyclic
shifts and does not report the even-n fixed-point classification error.
The archive has no separate MPR section. It was not used to establish
correctness. Absence of a matching report does not establish priority.
