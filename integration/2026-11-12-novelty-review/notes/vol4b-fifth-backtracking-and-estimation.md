# Volume 4B: backtracking and estimation, F077–F100

Reviewed on 12 November 2026 against the first edition, second printing.
Original typesetting was inspected on pages 37, 45–46, 49, 60, 121,
153, 398, 400, 402, 404, 406–407, 409–410, 414–415, 476, 478 and 481.
The existing per-finding reports and witnesses were read. Completed
enumerations were not repeated. Here DLX denotes section 7.2.2.1;
the other numbered exercises are in section 7.2.2. A ZDD is the
zero-suppressed decision diagram used to represent a family of sets.

| Finding | Correctness review |
|---|---|
| F077 | DLX 229: the exhibited valid order-sixteen Langford sequence beginning 16,14,15,11 is lexicographically larger than (108), whose fourth entry is 9. Every two copies of k have k intervening entries. The stored independent prefix searches additionally establish the actual maximum, but the single witness already disproves the printed claim. |
| F078 | DLX 243: secondary items need not be covered. With primary a,b, secondary s, unit weights and options a, as, b, the two solutions have squared-weight totals 2 and 5, but squared deviations from r=2 of 2 and 1. The argument becomes correct if only primary items receive nonzero weights. |
| F079 | DLX 255 and p.121: the sum for even N counts the completed state with contribution −1 although it produces no branch node. Its node count is V_N+3, not V_N+2. K2 has one branch and two terminals; the corrected formula also agrees with the printed 99 and 10228 examples. |
| F080 | DLX 259(b): levels ell=0 through n−1 contribute ell+1 cache states, followed by the empty state. Thus the count is binomial(n+1,2)+1. At n=2 the four states already contradict the printed two. The accompanying signature description uses covered Y items, and needs explicit complementation to agree with the active-item convention. |
| F081 | Answer 5: iterating over every integer between the minimum and maximum domain value is not equivalent to iterating over the domain. The one-variable domain {1,3} and an always-true predicate make the printed recursive procedure visit the forbidden value 2. The nonrecursive Algorithm B handles the domain correctly. |
| F082 | Answer 22: the two forced choices can disagree at n=6; the literal modification then outputs thirteen representatives instead of ten. At n=10 the reachable prefix (1,−1,9) leads to a repeated scan between labels 8 and 10 when the forced second slot is occupied. The recorded state cycle proves nontermination. Backtracking on conflicting requirements and on failed forced placement repairs these cases; the count table remains correct. |
| F083 | Answer 33: the 6347-node trie belongs to five-letter words, while the 63060-entry compressed trie belongs to six-letter words. Prefix counts and the compression formula reconcile all four printed numerical sizes; only the two length labels are exchanged. |
| F084 | Page 37: intersecting the five explicitly printed letter restrictions after SLUMS and TOTAL gives 62 words of WORDS(5757), not 221. The stored complete list and independently computed trie-prefix constraints agree. |
| F085 | Answer 44(b): candidate selection must use the class c selected in part (a), not the class of the old x. After 0001 and 0011, the old expression returns the already selected 0011 instead of the sole blue candidate 0111. The author program already selects the intended class; that correct implementation is not itself an explicit error report. |
| F086 | Algorithm C specifies sets of exactly g words but visits sets of at least g words. At m=2,g=2, its first output has three words; the completed small enumeration gives fifteen two-word and fourteen three-word outputs. The remaining slack is not tested at the visit. |
| F087 | Answer 38: the n=9 probability at m=2 is 486/504=27/28. The printed 32/35 would give a noninteger number of aperiodic words. Expanding the correct preceding generating function yields the corrected general probability as well. |
| F088 | Answer 53: the array recurrence omits the node-cost factor before twice COST. A two-node chain with both costs two has deterministic estimate four, but the printed recurrence returns variance −4. The general recurrence immediately above already includes the missing factor. |
| F089 | Answer 54: the last factor in the path probability must condition on the parent prefix ending at x_(ell−1), not the resulting prefix ending at x_ell. The printed conditional distribution is undefined at a leaf; the weighting rule itself is correct. |
| F090 | Answer 49: a separate uniform choice among five possibilities needs at least 27/8 fresh fair bits on average, already exceeding the stated 10/3. The exact optimal expectation is 18/5, obtained by summing the residual binary probabilities and attained by recycling rejections. This finding uses the single-choice model of the surrounding comparison; amortized generation of multiple outputs has different bounds. |
| F091 | Page 49: for n=100 the stated 2.7·10^(−9) is the tail probability at termination level at least 21, not at least 20. The latter is 1.9519870726687698·10^(−8). The distinction follows from level=number of chosen entries+1 and the printed generating function in answer 52. |
| F092 | Answer 58: the return label must follow the initialization of u,T,S. On the four-vertex star with edges 01,12,13, deleting vertex 1 causes the second layer to discard its next tarnished vertex and use a null vertex. The February 2025 erratum fixes other operations but leaves the label in the wrong place. |
| F093 | Answer 62: the first percentage distribution sums to 110.9 percent, beyond any rounding error. The last 12.2 should be about 1.2; the stored exact weighted count gives 1.2104667080 percent. The sum discrepancy alone proves the printed table invalid. |
| F094 | Answer 66: 9+7+4+4=24 contradicts the stated exclusion. The two compatible rotations must instead be rejected using their northeast–southwest sums, 19 and 20. The final puzzle solution remains correct. |
| F095 | Answer 64: hiding the rotated-A face and its opposite allows the illustrated B/A/D pattern, with O on the other faces, to contribute legitimate letters in eight orientations. Turning the displayed D by ninety degrees produces the intended impossible pattern. The actual puzzle's solution counts are unaffected. |
| F096 | Exercise 70: the correct growth constant is 2^m+3m−15/2+O(m²/2^m), so an additive O(1) is false. The derivation from the exact recurrence in NES_NOTES.md controls the remainder and identifies the positive pole. The cited preprint also has an erroneous second coefficient; the corrected asymptotic is derived independently, not inferred from that expression. |
| F097 | BACK-20Q still has the unreachable question-18 branch in the current author source. However, sjnam/gweb-examples explicitly described and fixed that same defect in a commit dated 17 August 2026. It is a real but previously public program error, and is removed from the new-finding view. |
| F098 | Answer 78: the initial singleton visit omits the lower weight bound. An edge with both weights one and bounds L=2,U=3 makes it output invalid singletons. Search should continue below L but the singleton should be visited only when its weight is at least L. |
| F099 | Answer 79(h): subtract one after the entire product defining h, rather than within its second factor. At switch setting 11, the thirty-two pedals give thirty-two distinct three-pipe sounds, while the printed expression counts only eight. The corrected polynomial agrees with the numerical examples already in the answer. |
| F100 | Answer 79(g,h): exactly eight sounds omit one of the 812 pipes. Missing pedal indices range from 12 through 19, rather than through 23. At index 20 the printed construction silences three pipes; the same problem occurs at 21,22,23. The pedal polynomial's own coefficient eight confirms the correction. |

## Sources and novelty

The refreshed cumulative/current Volume 4B and Fascicle 5 errata and
their TeX sources were screened by page offsets, exercise and subject.
Known corrections to E5, answer 44(a), the generating-function index in
answer 38, the distance-update loop, R6/R2′, and one monomial in the
organ polynomial are separate from these findings. No matching author
erratum was found. F097's current author source was fetched again and
is byte-identical to the reviewed original; its SHA-256 and exact public
antecedent are recorded in
[the F097 review](vol4b-f097-prior-public-report.md).

Public searches included Langford lexicographic maxima, SLUMS and 62,
trie sizes 6347 and 63060, commafree probability 27/28, the five-way
random-bit cost 3 1/3, BACK-20Q bugs, the percentage sum 110.9, Q811,
and Bousquet-Mélou importance-sampling corrections. The public
[BACK-20Q report](https://github.com/sjnam/gweb-examples/blob/d92b5f8329426b28b8bc14d8a486d74b6c5f0443/back-20q.w)
is an exact match to F097, including the two erroneous source statements.
The report's commit predates this local audit. Its separate question-15
issue is not added to this review's scope.

The corresponding [tamnd/brain exercises](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4)
were also inspected: DLX 229,243,255,259 and backtracking
5,22,23,33,38,44,49,53,54,58,62,64,66,70,71,78,79. Many have unrelated
answers. The relevant ZDD and Langford entries give incorrect alternative
answers, not these corrections. The disk answer's “earlier solution”
refers to its own Fourier argument, not the book's arithmetic exclusion.
[The public study guide](https://cracked.guide/guide/knuth-w117-0)
has no discussion posts identifying these defects.

[Lumbroso's primary paper](https://arxiv.org/abs/1304.1916) distinguishes
single draws from batched generation, as required for F090. The correct
general sampling theorem does not constitute a report of the book's
wrong constant. [Bousquet-Mélou's v2 preprint](https://arxiv.org/abs/1106.1876v2)
was checked at Proposition 5; its expansion omits the parameter-dependent
term. The author's publication page timed out. The final journal text
was not newly verified, and no claim about its typesetting is made.

Decision: 23 retained; F097 previously publicly discussed. For the
retained cards, the limited conclusion is **no matching prior report
found in the searched sources**, not established priority.
