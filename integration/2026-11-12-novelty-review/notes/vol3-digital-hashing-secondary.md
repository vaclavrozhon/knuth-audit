# Volume 3: digital searching, hashing and secondary keys

Publication review, 12 November 2026. All 17 baseline-confirmed findings below
remain confirmed. The checked book is the second edition, first printing
(March 1998), with file pages offset by 11. The original images and the detailed
proof notes in `workstreams/vol3` were reread. This finishes the 72-card Volume 3
review. No matching prior public report was found; priority is not established.

| Card | Independent check |
| --- | --- |
| V3-C0065 | The instruction frequencies in answer 6.3-6 give 10C−6S+4, where C counts comparisons and S is 1 on success. A root success costs 8 units, whereas the printed formula gives 11. The successful-search constant consequently decreases by 3; unsuccessful searches are unaffected. |
| V3-C0066 | Exercise 6.3-40 permits arbitrary pattern length n independently of period N. For period 01 and pattern (01)^t, changing any one input bit destroys the match. Reading the pattern already takes order n time in the stated finite-word model. The O(N) query claim cannot hold uniformly in n. |
| V3-C0067 | The binomial recurrence for the Patricia external path length on p. 506 has the same index on both sides, as in (5), rather than the N+1 left index of (6). The reference after (16) is wrong. |
| V3-C0068 | In answer 6.3-24, summing the remaining m−1 multinomial cells supplies (m−1)^(n−k). Both displayed binomial reductions omit it. For m=3, x_2=5/2, the next recurrence gives 17/4 with the factor and 53/16 without it. The final stated identity remains valid. |
| V3-C0069 | Answer 6.3-28 omits division by N in the U_(N+1) term of the average. Also the coefficient of log_M(N)/N is 1/(M−1), not 1. In the exact product formula, writing u=M^(−j) gives (1−product_(r≥1)(1−u M^(−r)))/u=1/(M−1)+O(u); summing the occupied scales gives log_M(N)/(M−1)+O(1) in the total. This is a successful-search correction. |
| V3-C0070 | The n=0 term of (14) on p. 505 is N−1+U_N, not N−1 plus the trie bit-inspection total. At N=2 the term sums to 2, whereas the claimed trie expression is 5. |
| V3-C0071 | The one-generator system theta=ab satisfies the stated Nielsen condition. Query a reduces to b^−1 and then back to a, each time with k=l=1. The rejection test l>k never fires, so the asserted termination fails. No general repair of the algorithm is claimed. |
| V3-C0072 | The Bernoulli expansion in answer 6.3-33 has z coefficient 1/4, whereas tanh(z/2) has derivative 1/2 at zero. The displayed series needs a factor 2. The May 2026 correction concerns answer 34, not this step. |
| V3-C0073 | The September 2024 erratum for pp. 493–494 names Program P, although the original is Program T. The May 2026 rating change names exercise 43 on p. 510, although it is exercise 34; exercise 43 is on p. 512 and already HM42. These are defects of the errata locators. |
| V3-C0074 | In answer 6.4-9 the normalizing denominator uses theta_(k−2) instead of theta_(k−1). With theta=1/sqrt(2), k=2, r=1, the actual interval is theta, but the printed denominator yields 1/(1+theta). The final classification by ratios is unaffected. |
| V3-C0075 | The January 2002 replacement for answer 6.4-32 is shifted by one index. For M=3 and b=(2,0,0), the carry recurrence gives c=(1,0,0), while the replacement gives (0,0,1). Sum up to j−1 in the prefix sum, or relabel its stated carry as c_(j+1). This finding concerns the replacement, not the superseded proof. |
| V3-C0076 | The ordered-hashing unsuccessful-search mean in answer 6.4-66 must use C_(N+1), not C_(N−1). For N=2 the latter equals 1, contradicted by the positive probability of requiring further probes. The insertion sentence also needs a consistent N versus N+1 convention. |
| V3-C0077 | The common probe loop in Program D costs 8 units per additional ordinary unsuccessful probe. Answer 6.4-18 credits only 4 times the change in the probe count although (30) and (31) replace only the step-size calculation. The total 8C term is explicit on p. 531 and in the 1980 first-edition correction. The old 94%/71% thresholds are not justified; no universal replacement thresholds are asserted. |
| V3-C0078 | Comparing the defining series gives R(n)=1+R(1,n), rather than R(1,n)−1 as printed on p. 544. Equations (58) and (60) require the plus sign; the b=1 specialization also detects the discrepancy. |
| V3-C0079 | In answer 6.5-8(a), g_t(s)=f_t(s,m−1) and h_t(s)=f_t(s,m−2). The last exceptional-case inequality must use g, not h; m=4, s_0=7, s_1=5 otherwise calls h on a set larger than its universe. In (b), the size of S_0 is ceil(s/2), not ceil(s_0/2). The February 1997 replacement already repeats both slips. |
| V3-C0080 | The general comparison on p. 574 contradicts the earlier balanced k-d tree bound on p. 566. With two coordinates and one unspecified, that bound is O(sqrt(N)), the same exponent as Rivest's scheme, rather than order N. Compound sorted lists on p. 567 give another counterexample for fixed attributes. |
| V3-C0081 | The original p. 566 prints Acta Informatica volume 23. The publisher record gives volume 9, pages 23–29 (March 1977), DOI 10.1007/BF00263763. This is a bibliographic correction. |

## Errata comparison

The official sources were refreshed earlier in this review and their hashes are
in the source manifest. Checked all3-prepre, all3-pre, all3, err3, err3-1e and
err3.textxt, including the first-edition page mappings recorded in the
digital-searching, hashing and secondary-keys source reviews. Relevant known
changes include the 1975 and 2026 answer-34 revisions, the 1980 Program D timing,
the 1995 ordered-hashing addition, the 1997 answer-8 replacement and the 2002
carry replacement. None repairs the distinct claims retained here. The seemingly
empty p. 734 entry in all3-pre is the relocated layout of the rounding-symbol
correction in answer 36, not a change to the carry formula.

## Public-source screen

Queries combined Knuth/TAOCP with Patricia errata, digital-search timing,
6.3-28 digit inspections, 6.3-40, Nielsen/trie error, tanh factor, ordered-hashing
error, p. 734/Janson, p. 731/4u, R(1,n), Rivest/p. 574, p. 745/exercise 8,
6.4-9 and the Lee–Wong citation. Exact exercise queries often returned unrelated
material; that is a limit of the screen, not positive evidence of priority.

The public `tamnd/brain` solution pages for 6.3 exercises 24, 28, 33, 40, 41;
6.4 exercises 9, 18, 32, 66; and 6.5 exercise 8 were also inspected. Their
June/July 2026 dates precede this audit, but none identifies the retained book
error. Their references to an incorrect previous solution concern their own
attempts. In particular, 6.3-40 still claims the requested bound after an
O(n) preprocessing step, 6.3-41 substitutes a false no-cancellation lemma,
6.4-32 changes the meaning of c to occupancy, and 6.5-8 proposes a different,
incorrect recurrence. They are not used as mathematical evidence.

- Solution collection: https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol3
- Publisher citation: https://link.springer.com/article/10.1007/BF00263763
- Burnol, *Some geometric series for Euler's constant*, v6 (June 2026):
  https://arxiv.org/abs/2603.29998 . The relevant discussion and errata footnote
  concern 6.3-34, rather than the factor in answer 33.
- Flajolet, Regnier and Sotteau, *Algebraic Methods for Trie Statistics* (1985):
  https://algo.inria.fr/flajolet/Publications/FlReSo85.pdf . Its Patricia discussion
  derives the standard result; the inspected text does not report this book typo.
- The search hit https://marcinciura.github.io/all3-prepre.pdf reproduces the
  official 2002 carry replacement, including the defective index; it is not a
  correction of that replacement.

Original pages checked in this block: 493, 494, 505, 506, 510–512, 530–531,
538, 543–544, 566–567, 574, 722–723, 725–727, 729, 731, 734, 741 and 745;
also Volume 1 p. 116 and the two original errata images for C0073 and C0075.
