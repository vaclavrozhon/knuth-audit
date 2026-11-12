# The single-crossing count omits an enclosing block

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.7–27, printed 815–816, especially the slot argument and final formula.

A genji-ko diagram represents each block of a set partition by vertical lines of equal height, joined by a horizontal bar. Heights may differ between blocks. The answer counts partitions that admit a diagram with exactly one intersection between lines belonging to different blocks.

The answer treats the elements outside the two crossing blocks as independent noncrossing partitions in the intervening slots. This misses a block surrounding the entire crossing pair. For example,

    16 | 24 | 35

has exactly one crossing when the heights of these three blocks are respectively 3, 1, and 2. The vertical line at position 3 crosses the bar from 2 to 4; there are no other crossings. The enclosing block 16 is not contained in any one of the five slots of the crossing pattern 24|35.

This changes the numerical answer, not just its proof. The final expression, C_(n-5,n+3) + C_(n-4,n+4), uses the Catalan triangle C_(m,n) = binomial(m+n,m) - binomial(m+n,m-1). At n=6 it gives 9+54=63. The correct number is 64:

* Two blocks: the three printed patterns give 6+3+4=13.
* Three blocks of sizes 3,2,1: choose the singleton in 6 ways, then one of the 5 crossing two-block partitions on the other five elements, giving 30.
* Three blocks of sizes 2,2,2: there are 6, namely 12|35|46, 13|24|56, 13|26|45, 15|23|46, 15|26|34, and 16|24|35.
* Four blocks: choose the four nonsingleton elements, then use their unique crossing pairing, giving binomial(6,4)=15.

Other block-size patterns cannot have a crossing. The total is 13+30+6+15=64. Adding the 132 noncrossing partitions gives 196 with at most one crossing, as requested by the exercise. A short check of the 203 partitions on six elements independently minimizes the crossing count over block-height orders and gives counts 132,64,6,1 for minima 0,1,2,3. See `../scripts/genjiko-six-counterexample.py` and `../results/genjiko-six-counterexample.json`.

The general formula must account for blocks enclosing the crossing pair; no complete replacement formula is asserted here. Original pages 513,815,816 were inspected. The same incorrect formula occurs in the locally archived history pre-fascicle, printed 32. No matching correction was found in the historical/current Volume 4A or refreshed Fascicle 4 errata, or in targeted public searches. See `../sources/history-final-source-check.json`; absolute novelty is not established.
