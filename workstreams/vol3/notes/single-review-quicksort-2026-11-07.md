# Quicksort core and its extreme cases — reviewed

7 November 2026. Coherent scope: Algorithm Q, its MIX implementation and
analysis, printed 113–121, with paired exercises 17–27 and answers 630–632.
The completed core/program/mean-cost recovery notes are reused; the remaining
25–27 question/answer block was read with the saved extreme-case notes.
No new independent optimality proof or computation was requested or made.

For the ordered input, the printed partition removes one minimum each time:
A=N−M, B=D=E=S=0 and C=binom(N+2,2)−binom(M+2,2). The two worse inputs
in answer 26 leave a reverse-ordered final M-block, adding D=M−1 and
E=binom(M,2). Thus the printed comparison with the ordered input assumes
M>1 if “more slowly” is intended strictly. For M=1 the cost is equal;
this harmless threshold case is recorded here, not promoted to a defect.

The answer-27 permutation produces the stated balanced/trisected blocks,
A=5, C=64, S=1 and B=D=E=0. The printed timing formula gives
24·5+4·64+7·23+9=546u. The existing saved lower-bound work is retained;
this pass does not create another proof of the unrestricted optimum.

The random-pivot replacement at the end of 121 was read together with its
continuation on 122: moving the selected pivot back into the left endpoint
is needed for the scan sentinel. Later median/sample-sort and radix-exchange
material is outside this completed block; merely reading its introduction
does not certify all of its cross-referenced exercises.

Existing supported defects C0011 (stack numerator) and C0030 (undefined
third phase in the faulty equal-key variant) remain findings. C0031 remains
an unconfirmed interpretation of the admissible MIX threshold/address
range. The checked algorithm uses valid memory addresses, distinct-key
assumptions where the analysis requires them, and its specified sentinels.
Historical authorship and publication-priority assertions are not rechecked.
No new finding. No old simulations or proof inventories were rerun.

Whole-page certification adds printed 114–121 (file 125–132) and printed
631 (file 642); other previously completed pages retain their evidence.
Shared question page 136 and answer page 632 contain additional exercises,
so this block alone does not turn those whole pages green.

Evidence: `exchanging-proof-quicksort-core-113-117-17-21.md`,
`exchanging-proof-quicksort-mix-117-118.md`,
`exchanging-proof-quicksort-means-119-121-22-24.md`,
`exchanging-proof-quicksort-limit-cost-120-121.md`,
`exchanging-proof-quicksort-worst-25-26.md`,
`exchanging-proof-quicksort-best-27.md`, original pages and the five-layer
`sources/exchanging-errata-review.json`. The former planned P1076–P1088
inventory expansion is unnecessary under the new standard.
