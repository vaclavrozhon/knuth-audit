# Volume 4B follow-up review — November 17, 2026

This pass added 15 new findings (F257–F271) and confirmed five earlier
candidates (C025, C048, C034, C008 and C006). Volume 4B now has 276 retained
findings in the catalog, up from 256. The catalog still has 38 candidates
and three dismissed items for this volume. Two earlier findings, F242 and
F023, were extended without increasing the count.

These are results of the AI-assisted audit, not author-confirmed errata.
No matching correction was found in the sources checked for each addition;
this does not establish absolute priority or cover every later printing.
The supplied source is the first edition, second printing (2022).

The [plain-text list](volume-4b-findings.txt) contains 274 selected corrections.
It preserves the explanations already drafted and adds the final two findings
from this pass. The [20 new review decisions](data/focused-4b-review-decisions.json)
supplement the historical 806-card review in [REVIEW.md](REVIEW.md).

The most consequential addition is [F261](audit-2026-10-31/notes/F261-lookahead-deferred-propagation.md). In the printed lookahead procedure, delaying newly forced assignments until after the propagation loop can produce an unjustified clause. A seven-variable satisfiability example has sixteen valid assignments, all excluded by that clause. The argument accounts for the earlier independent corrections F208 and F209. A short check covers all 128 assignments; this is not a verification of an entire solver.

[F263](audit-2026-10-31/notes/F263-resolution-pruning-still-awkward.md) gives a small resolution-proof example where the prescribed single pruning step leaves the property it was meant to remove. Additional pruning or induction repairs the proof; the underlying theorem is not refuted. [C048](audit-2026-10-31/notes/C048-prime-number-error-exponent.md) identifies a misstated historical prime-number error bound, including its exponent and attribution. The primary papers support the correction, but the evidence does not prove that the stronger asymptotic claim is false.

The twenty newly confirmed cards consist of seventeen low-severity corrections, two medium-severity findings and one high-severity finding. Severity is the current UI classification.

| Card and argument | Change | Printed page | Severity | Correction or reason |
| --- | --- | --- | --- | --- |
| [F257](audit-2026-10-31/notes/F257-walksat-restart-cutoff.md) | New | 608 | low | For the twelve-variable instance in answer 305, restarting after eight flips takes 12.297... flips on average, not the printed 16.1. An exact 33-state computation confirms the success probability and weighted duration already given in the book. The printed 16.1 instead corresponds to restarting after twelve flips. |
| [F258](audit-2026-10-31/notes/F258-overlap-ratio-signs.md) | New | 587 | low | Answer 203(e) asserts f(1/2)<0, but the allowed choice p=1/2, r=7/5 gives f(1/2)=3/25>0. The discrepancy persists for arbitrarily small positive epsilon. The following approximation near 1/2 also uses the opposite paired sign: g(1/2 +/- 1/N) has leading term +/- f(1/2)N/4. Both defects occur in one proof paragraph. |
| [F259](audit-2026-10-31/notes/F259-minimality-permutation-inverse.md) | New | 592 | low | After deleting M_(j0,m), the listed permutation gives the wrong element the largest rank. For m=3 and j0=1, the proposed assignment still violates M_23. |
| [F260](audit-2026-10-31/notes/F260-newton-inequality-history.md) | New | 374 | low | The answer credits the eventual proof to Sylvester in 1865, although Maclaurin's 1729 paper already proves the coefficient inequality used here. |
| [F261](audit-2026-10-31/notes/F261-lookahead-deferred-propagation.md) | New | 581 | high | Answer 175 processes deferred units after the loop that propagates their effects on nonbinary clauses. Step X9 can then add an unsafe clause. |
| [F262](audit-2026-10-31/notes/F262-minimality-clause-deletion.md) | New | 588 | low | Answer 206 conditions C on the fresh variable instead of removing the clause that C became in the joined formula. |
| [F263](audit-2026-10-31/notes/F263-resolution-pruning-still-awkward.md) | New | 592 | medium | The construction in answer 225 shortens the tree but does not necessarily eliminate every resolution variable from its conclusion. |
| [F264](audit-2026-10-31/notes/F264-bounded-occurrence-variable-count.md) | New | 587 | low | The final variable estimate in answer 204(c) counts one extra m; the displayed construction gives 6m+29 or 6m+30 variables. |
| [F265](audit-2026-10-31/notes/F265-relaxed-product-clause-count.md) | New | 632 | low | The relaxed multiplication construction yields 9mn-5m-8n clauses; the printed expression subtracts another 2n. |
| [F266](audit-2026-10-31/notes/F266-double-lookahead-example-size.md) | New | 229 | low | The example should use S=16 and DT=258. It substitutes the number of free variables for the number of candidate literals. |
| [F267](audit-2026-10-31/notes/F267-lookahead-wraparound-exits.md) | New | 331 | low | Exercise 173(ii) sends an exhausted candidate scan to X6 or Y3, which reads the undefined entry at index S. |
| [F268](audit-2026-10-31/notes/F268-clause-signature-change-bound.md) | New | 257 | low | The p+1 bound on p.257 is too large: a clause with signature (2,0) can force a literal after just one old level changes sign. |
| [F269](audit-2026-10-31/notes/F269-signed-cycle-repeated-negation.md) | New | 365 | low | Exercise494(iii) repeats NOT j in both cycles and omits j. The displayed object is not the required signed permutation. |
| [F270](audit-2026-10-31/notes/F270-viennot-publication-year.md) | New | 267 | low | The citation on p.267 dates Lecture Notes in Mathematics 1234 to 1985, the conference year. The cited volume was published in 1986. |
| [F271](audit-2026-10-31/notes/F271-motley-overlap-cell.md) | New | 521 | low | Answer 370 names p22 and p23 as shared cells. The stated rectangles actually share p12 and p22. |
| [C025](audit-2026-10-31/notes/C025-acta-anniversary.md) | Promoted | 87 | low | The footnote links a 1913 index to the journal’s 21st birthday. The original index explicitly covers 1882–1912, and the first issue appeared in December 1882. |
| [C048](audit-2026-10-31/notes/C048-prime-number-error-exponent.md) | Promoted | 388 | medium | The note prints exp(−C log n) and attributes this fixed power saving to the 1896 paper. The original sources instead give a later bound with sqrt(log n) in the exponent. |
| [C034](audit-2026-10-31/notes/C034-colored-cubes-cross-reference.md) | Promoted | 456 | low | The cited1978 article asks for five disjoint six-cube rows using all thirty cubes. The book instead points to the part asking how many individual rows there are. |
| [C008](audit-2026-10-31/notes/C008-stable-versus-covering.md) | Promoted | 619 | low | Answer361 identifies two classes that exercise364 explicitly distinguishes. A stable assignment need not have each assigned variable constrained. |
| [C006](audit-2026-10-31/notes/C006-exponential-modulus.md) | Promoted | 469 | low | Answer 189(a) gives exp(exp(-x) cos y), but the modulus is exp(-exp(x) cos y). The same typo survives in the 2019 replacement answer. |

Existing-card extensions: [F242](audit-2026-10-31/notes/F242-quad-free-uniqueness-proof.md) corrects an additional set in the quad-free uniqueness proof; [F023](audit-2026-10-31/notes/F023-tail-generating-function.md) also records “set permutation” where the question means “set partition”. Neither is counted as a new card.

Findings were checked against original typesetting. The checked sources
include current and historical Volume 4B and Fascicle 5/6 errata, including
current TeX files retrieved on November 17. Each argument records the
relevant sources and the scope of its checks. Book files and scans are not
included in this repository. The saved checks support the individual
findings; they are not a verification of an entire solver or of every
claim in the book.
