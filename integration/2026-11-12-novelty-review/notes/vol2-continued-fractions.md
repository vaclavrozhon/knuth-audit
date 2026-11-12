# Publication review: C0132–C0146

Reviewed November 12, 2026. The eleven baseline-confirmed cards in this
range remain supported. The original text and relevant replacement
passages were visually checked, along with the four applicable errata
layers refreshed on November 12. No matching prior public report was
found in the bounded searches below. Absolute priority and an unseen
physical printing remain unverified.

| Card | Assessment and limits |
| --- | --- |
| V2-C0132 | The original answer claims that the partial-quotient sum divided by n*lg(n) tends to one for almost all inputs. Khintchine's original p. 377 explicitly states convergence in measure and rejects almost-everywhere convergence. The stored conditional-cylinder proof independently gives infinite limsup almost surely: its conditional probability of a quotient at least m is (1+r)/(m+r)>=1/m. Retain as a misstatement of a known theorem, not a newly discovered probability result. |
| V2-C0133 | The 2011 replacement visibly omits the subscript in I_N union K_N. Its final limits also fix epsilon and N, so they equal mu(I_N) and 1-mu(J_N), not generally mu(I). Alternating dyadic intervals give the explicit distinct limits 2/3-(2/3)*4^-N and 2/3+(1/3)*4^-N. The intended squeeze proves Lemma M after letting epsilon go to zero; the lemma is correct. |
| V2-C0134 | The prose on pp. 653–654 calls the expression a total, and the exercise defines the total over all numerators. For prime p that total is at least p, whereas the expression is O((log p)^2). This contradicts its O(p^-1/2) residual for infinitely many p. An average was presumably intended, but the inaccessible Pitteway–Castle paper and its constants are not claimed verified. |
| V2-C0135 | The allowed ordered inputs (5,3,3) take four divisions, yet their last input three and first input five are smaller than both claimed minima four and seven. The stored Fibonacci lower-bound proof and attaining construction support minima F_(N-n+3) and F_(N-n+4), respectively, including early termination. Bradley's inaccessible original is not attributed the book's error. |
| V2-C0136 | At n=3, T(5,3)=3, but the original upper bound log_phi(3*sqrt(5)+1)-2 is below three. The corrected final constant -1, or an added ceiling with -2, follows from the Fibonacci step bound. The separate lower-bound exercise is unaffected. |
| V2-C0137 | The stated maximizing order for the permitted multiset {1,2,2,2,2} gives continuant 45; another ordering gives 46. The original hypothesis does not require distinct entries. The literature distinguishes the distinct-input Motzkin–Straus result from the later general problem. Retain the missing hypothesis; the minimum claim and the maximum with pairwise distinct inputs have supporting stored proofs. Do not claim a new general continuant theorem. |
| V2-C0138 | For the explicitly closed interval [2/5,1/2], the original rule returns 2/5, although the finite prefix endpoint 1/2 has smaller denominator. Appending infinity as directed does not fix this. Handling that endpoint first repairs the rule. The baseball answer 287 and the 2000 correction to its first sentence are separate and correct. |
| V2-C0141 | The original square root contains v/d, while the continuant product for the unnormalized remainder includes d. With u=6,v=4 and both weights one, the three tested absolute values are 4,3-sqrt(2),2, all greater than sqrt(2). This example uses no split final quotient. Restoring d and using sqrt(lambda*mu*v), or normalizing all remainders by d, repairs the proof. |
| V2-C0142 | With alpha=sqrt(2)-1, beta=alpha/2 and gamma=alpha, the printed recursion returns zero, outside the interval. The first valid index is three. Reciprocation reverses which interval endpoint is included; the stored two-function repair tracks that reversal and proves termination. This is an exact permitted-input counterexample, not numerical rounding. |
| V2-C0145 | The explicit range of all positive epsilon permits epsilon=4. Its stated exception bound then tends to zero, while (1,1) remains an exception for every N. This also survives a fixed multiplicative constant. Dixon's own 1971 recap repeats the same wording, so this is an inherited missing-range qualification, not a demonstrated misquotation or a refutation of small-epsilon concentration. |
| V2-C0146 | The 2005 addition visibly assigns a logarithmic variance to tau_n, but equation (48) defines tau_n as a deterministic average for fixed n. Morris's precise probability model and moment formulation confirm the intended random division count over pairs with both entries bounded. Retain the notation/model correction; Hensley's full original article remains unavailable. |

Originals freshly viewed: pp. 367, 369, 372–374, 378–379 and 652–654,
656; the 2011 Lemma M replacement and 2005 variance addition. Existing
large finite checks were reused. The short counterexamples and formula
substitutions were checked directly; no new census was run.

Public searches combined Knuth/TAOCP with the exercise numbers and
partial-quotient sum, almost all versus probability, Lemma M, distinct
continuant entries, minimum GCD inputs, smallest-denominator prefix,
rotation interval, Dixon epsilon and Hensley variance. Sources giving
correct general mathematics were distinguished from reports of the
specific TAOCP defects.

- [Khintchine 1935](https://www.numdam.org/item/CM_1935__1__361_0.pdf),
  original p. 377, states both the positive result and the excluded stronger
  conclusion. The relevant page was freshly viewed.
- [Diamond–Vaaler 1986](https://msp.org/pjm/1986/122-1/pjm-v122-n1-p06-p.pdf)
  is an additional prior mathematical source. The result is not new.
- [De Luca–Zamboni, cyclic continuants](https://arxiv.org/pdf/2108.11313)
  and [De Luca–Edson–Zamboni, semi-regular continuants](https://arxiv.org/pdf/2105.00496)
  distinguish the distinct-input result and later multiplicity problem.
  Neither searchable paper mentions Knuth. Ramharter's 2006 introduction
  was also freshly viewed and gives the same distinction.
- [Yao–Knuth 1975](https://pmc.ncbi.nlm.nih.gov/articles/PMC388801/)
  states the asymptotic for the total, including its factor n. It does
  not repair the later empirical expression's prose normalization.
- [Dixon's 1971 recap](https://www.cs.drexel.edu/~jjohnson/2017-18/winter/cs300/resources/Dixon1971.pdf),
  original p. 374, was viewed from the stored public scan. Its wording
  establishes the inherited nature of the epsilon omission.
- [Morris 2015](https://arxiv.org/pdf/1502.07616v1), pp. 2–3,
  defines the probability spaces and gives the moment method for the
  division count. The stored full moment verification supplies the
  variance interpretation; no new proof of the analytic theorem is claimed.

No corrected book report matching these cards was located. All reports
remain unsent, and every novelty conclusion remains qualified.
