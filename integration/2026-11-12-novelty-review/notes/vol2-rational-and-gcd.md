# Publication review: C0111–C0130

Reviewed November 12, 2026. All eighteen baseline-confirmed cards in this
range remain supported, with the limitations below. The original pages,
surrounding hypotheses and existing arguments were re-read. Current and
historical errata were checked in all2-prepre, all2-pre, all2 and err2,
using the November 12 source refresh. No matching prior public report of
these particular book defects was found. This is a bounded search, not a
claim of absolute priority or a check of an unseen physical printing.

| Card | Assessment and limits |
| --- | --- |
| V2-C0111 | The original listing allocates two twenty-word buffers, but a MIX printer reads twenty-four words. Its second output therefore includes four code words; asynchronous output also allows the next line to overwrite four words still in use. Volume 1's device definition confirms both facts. The existing forty-eight-word repair and simulation address both faults. |
| V2-C0112 | The 1999 replacement needs decimal exponents 237 in both places and binary mantissa 1111111010. Exact integer midpoint comparisons were freshly checked for u=1017*2^774 and U=1011*10^233: 2021*10^233 < 2u < 2023*10^233 and 2035*2^774 < 2U < 2037*2^774. The earlier smallest-example claim is restricted to positive integers, not arbitrary real floating-point values. |
| V2-C0113 | At N=2, the legal sum 1/1+1/1 has intermediate numerator two, exceeding the claimed maximum one. The formula works for N>=3. Retain only as a small-format exception. |
| V2-C0115 | For q=1 the finite nonnegative value is zero and infinity is representable. At x=1 the mediant tie rule chooses infinity, which has smaller denominator, whereas the stated zero region includes this endpoint. The definition gives no q>=3 restriction. The signed q=2 interpretation is secondary; the q=1 witness suffices. |
| V2-C0116 | The exercise allows integer rectangle bounds without a positivity condition. For (-1,1] by (0,2], three pairs are coprime, but the displayed sum gives four because it counts (0,2). Nonnegative lower bounds repair the intended positive-input formula. |
| V2-C0117 | At N=1 the only positive pair is (1,1), whose MIX time is nineteen rather than the claimed maximum twenty-one. The attaining pair in answer 37 also needs n>=2; at n=1 it gives the forbidden zero input. Retain as a minor one-bit exception, not a failure of the main asymptotic bound. |
| V2-C0118 | Algorithm X on u=1,v=2 ends with v_1=-2, so v_1*u is minus the least common multiple. Its absolute value is required. The separately allowed input (0,0) also needs an exception to the quotient expression. |
| V2-C0119 | In the ternary variant, u=1,v=7 yields t=-6 and then -2; the subsequent replacement rule cycles. Taking the absolute value before removing powers of three repairs it. The book's own worked example already uses the positive difference. |
| V2-C0121 | In decimal precision four, u=10001,v=10000 produces leading words 1000,1000. The trial quotients disagree immediately, so B=0, although the true quotient is one. The family b^p+1,b^p works at arbitrary word size. Only the explanation that this branch necessarily means a very large quotient is incorrect; Algorithm L remains valid. |
| V2-C0122 | The 2016 erratum identifies Morris's positive normalized density xi with G'. The book defines G as a decreasing tail with G(0)=1,G(1)=0, so xi=-G'. Morris's preprint Theorem 2 and the original erratum were visually checked. The 2022 page-range correction does not fix this sign. |
| V2-C0123 | The asserted reuse of the odd-input averaging formula for the shift count misses the initial difference of the two powers of two. For inputs 1,...,3, the actual average is 8/9 and the weighted formula gives 4/9. The omitted term tends to 4/3; the leading logarithmic coefficient is unaffected. |
| V2-C0124 | Direct substitution of phi=(1+sqrt(5))/2 into the correctly printed general identity gives -2G(1+4phi) on the right, not 2G(2phi^2). The tail function's sign for arguments above one distinguishes the two values. The general identity and proof survive. |
| V2-C0125 | The definition gives 4*tau(2n)-tau(n)=1/(exp(n)-1)>0. An exact expression n^-2 times a function periodic in log2(n), as asserted in the next paragraph, would give zero. The missing remainder is -sum over r>=0 of 4^r/(exp(2^r*n)-1), which is O(exp(-n)). Retain as an exact-versus-asymptotic error, distinct from Brent's already public missing-periodic-term correction. |
| V2-C0126 | The first two residue expansions require derivatives at -1, not at 1. The double pole is at s=-1, and the printed b(s) itself has a pole at 1. Re-reading the definitions and residue coefficient confirms this local substitution error. |
| V2-C0127 | The fourth expansion's k-th term at x=1 approaches (-1)^k/4 and therefore does not tend to zero. Its displayed common domain must exclude this endpoint, or explicitly use an Abel limit there. The first three expansions are not implicated. The stored bound on the periodic contribution and binomial-sum asymptotic support this conclusion independently of floating-point plots. |
| V2-C0128 | The original definition is the exact logarithm m=lg(max(abs(u),abs(v))). For the example u=1,v=3*2^k-1, it is not k+2; k=2 already gives lg(11), not four. The ceiling equals k+2. The operation counts and bound are not disputed. |
| V2-C0129 | The original Lebesgue article ends on page 517; Serret's separate article starts on 518. Both original pages and NUMDAM's catalogue agree. The two book citations ending at 520 need 517. This is a bibliographic correction, not a new historical attribution. |
| V2-C0130 | The answer explicitly states a general strict bound for finite continued fractions with positive integer entries, but the one-entry list (1) has value one. Retain only as a minor overstatement of this auxiliary fact. The exercise already requires its finite last entry to exceed one, so every actual application in the uniqueness proof is valid. This is not a counterexample to uniqueness and does not require replacing that proof. |

Original book images checked in this block include pp. 331–333, 340–342,
347–349, 355, 374, 637–647 and 662, plus Volume 1's printer description
on pp. 136–137 and the 1999 and 2016 replacement passages. Earlier stored
large checks were not repeated. The round-trip midpoint test above was a
short exact calculation.

Public searches covered the exercise numbers and distinctive terms for
printer-buffer size, Tydeman's round-trip example, slash arithmetic,
ternary GCD, initial binary shifts, Lehmer's large-quotient explanation,
the golden-ratio example, Mellin remainder and derivative points, and the
continued-fraction endpoint. General algorithm descriptions, book mirrors
and unrelated hits were not treated as prior reports.

Relevant primary sources and resolved leads:

- [Morris, preprint 1409.0729](https://arxiv.org/pdf/1409.0729), Theorem 2,
  p. 7: positivity and integral-one normalization. The preprint and final
  journal version are distinguished; the full published version was not
  re-audited.
- [Brent, Further analysis of the binary Euclidean algorithm](https://arxiv.org/pdf/1303.2772),
  section 9, pp. 14–15: the public correction concerns the periodic term
  omitted in Brent's 1976 analysis, subsequently included in answer 29.
  It does not report the exponential remainder in answer 28 or the other
  local answer-30 defects. The 1999 lecture PDF also surfaced, but its
  broken text encoding was resolved by reading this author preprint.
- [GMP's Lehmer algorithm description](https://gmplib.org/manual/Lehmer_0027s-Algorithm)
  discusses a large-quotient fallback in its own implementation. It does
  not establish that Knuth's B=0 condition is sufficient for a large
  quotient or report the counterexample on the card.
- [NUMDAM's Lebesgue record](https://www.numdam.org/item/JMPA_1847_1_12__497_0/)
  gives 497–517, verified against the scanned ending and Serret's opening
  page. The correct article range is already public information; no
  earlier correction of these two TAOCP citations was located.

All retained assessments mean “supported defect; no matching report found
in the checked sources.” No report has been sent to an author or publisher.
