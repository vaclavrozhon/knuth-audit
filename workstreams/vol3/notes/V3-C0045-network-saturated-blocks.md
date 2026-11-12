# V3-C0045 — Blocks below the transition contain ones, not zeros

Confirmed in volume 3, second edition, first printing (1998), answer
5.3.4-54, printed p.673, file p.684. In the analysis of the third stage,
c_j denotes the number of ones in its jth block of m^2 positions. The
sentence beginning with the hypothesis `0<c_k<m^2` ends by asserting
`c_j=0 for j>k+1`. It should say `c_j=m^2 for j>k+1`.

Take m=3 and the already sorted 27-bit input consisting of one zero
followed by 26 ones. Each sorting operation in the first three stages
acts on an already ordered subsequence, so the input remains unchanged.
The three block counts are therefore

```
(c_0,c_1,c_2) = (8,9,9).
```

The hypothesis holds at k=0, but the asserted conclusion gives c_2=0
instead of 9. The corrected statement also agrees with the preceding
upper-region zero-block statement and the subsequent narrow transition
region argument. This typo does not refute the sorting construction.

The original was visually checked and saved as `images/bookwise-p673.png`.
All five official errata layers were screened in
`sources/networks-errata-review.json`. Targeted public searches for
answer 5.3.4-54 and the p.673 block counts found no matching report;
absolute priority is not asserted.
