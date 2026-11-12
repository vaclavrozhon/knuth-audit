# Volume 4B: F173–F196 publication review

Reviewed on 2026-11-12 against the first edition, second printing. The original
typesetting and every existing detailed argument were reread. All 24 cards are
retained. Existing small certificates were inspected rather than restarting
large enumerations.

| Card | Rechecked reason |
| --- | --- |
| F173 | MPR111(b): sketches are permutation images, which need not belong to A union B. With A=B={1} and permutation 21, both sketches are 2. Use the image of the union, or pull back the sketches. The Jaccard collision probability is unchanged. |
| F174 | MPR112(b): nine entries in the displayed partial permutations fail to preserve the preceding placements. In the first, third and fourth tables, entries 3,9,12 should be 1032,3210,0321, with 0 denoting a blank. Completing the first printed branch gives a 7-to-5 imbalance for positions {2,3}. The second branch is correct. |
| F175 | MPR113(a): the union has n-k+1+t elements, not n-k+t. For n=5,k=4 the printed inclusion–exclusion sum is 1/4 instead of 1/20. The missing +1 repairs it. |
| F176 | MPR116: subtracting the product of (1-x_e) makes the top coefficient (-1)^(m+1), not (-1)^m. Five parallel edges at p=3 give coefficient 1 rather than 2. The nonzero-coefficient argument still works. Alon's original proof has the correct sign. |
| F177 | MPR125(e): the convolution step applies the sum-closure result (d), not the single-sequence inequality (c). This is a cross-reference error, not a false convolution theorem. |
| F178 | MPR140(a): the unmarked-record expectation has a nonzero 1/n correction, not an exponentially small remainder. At p=q=1/2 the stored conditional-gap calculation gives a lower bound of order 1/n. The cited Banderier–Beier–Mehlhorn paper also explicitly includes the 2q/(p^2*n) term. |
| F179 | MPR140(e): fifty zeros followed by fifty ones, with epsilon=1/4, k=51 and m=5, make events (*) and (**) have probabilities 1 and 0. The asserted comparison is false. Bounding the two events separately still proves the final bound. The old erratum only removes an extra parenthesis. |
| F180 | MPR145: the product has one factor for each of the n coordinates, not m. At n=3,m=2 and k=(0,0,2), the printed ratio is 3 while the actual ratio is 1. |
| F181 | Answer 291's explicit rejection rule removes 57 triples, not the stated 53, and rejects QTX although the next sentence describes its solutions. This establishes an internal inconsistency only: 57 is not asserted to be the true number of unsuitable triples. |
| F182 | Answer 343: the listed 29 weights sum to 8708; removing 200 and 210 leaves 8298, not 8296. Both values are below 311*27, so the height bound survives. The earlier R-tower correction concerns a different example. |
| F183 | Answer 354(f): TR fixes e12 but maps e13 to e32 and e14 to e42, contradicting the two alleged impossible cases. The printed alternative T^2RT does not fix e12. The stored exact matrix products verify the corrected cases. |
| F184 | Answer 356(b): the set {i,j,n,o,p} packs R_(2x7) and S_(2x7), not S_(7x2). The straight four-sphere piece cannot fit the last shape; its only possible collinear direction there is not a nearest-neighbor direction of the sphere lattice. The printed table independently reports zero all-planar solutions for that shape. |
| F185 | Answer 371(a): iterating rho(a,b,c,d)=(c,d,n-b,n-a) gives rho^2=(n-b,n-a,n-d,n-c) and rho^3=(n-d,n-c,a,b). The printed iterates can reverse an interval; n=4 and (0,1,2,4) suffice. |
| F186 | Answer 371's merged-option examples contain two wrong colored interval items: part (a)'s third component needs y02, and part (b)'s first component needs x01. The cell items already specify the intended rectangles and determine these colors directly. |
| F187 | Answer 371(b)'s intersection rejection also rejects rectangles fixed by the tested reflection. For example, (0,1,3,4) at n=4 is a valid two-rectangle orbit but fails b>c. Apply the rejection only to distinct images, or form the set of unique orbit rectangles first. |
| F188 | Answer 393 says to enumerate subsets of five cells in a six-clue problem. Its surrounding 5^6, Bell number 203 and binomial coefficient all confirm that six is intended. |
| F189 | Answer 392's 46 eight-element classes contradict its split 26+18=44. Those two counts agree with 2976=173*16+26*8 and 4000=241*16+18*8 and the stated total 458. No new census is claimed. |
| F190 | Exercise 394 needs the assumption that the puzzle is solvable. Four clues 1,2,3,4 in the first column and a 5 in row 5, column 2 are locally consistent but have no completion. The immediately preceding exercises explicitly include puzzles with zero solutions, so solvability is not implicit in this usage. |
| F191 | Answer 405 starts with an empty visited set and fails to exclude the starting vertex on extension. The one-edge graph then admits v,u,v as a simple path. Exclude the union of S and {v}. In answer 404 this only weakens a preliminary filter; it does not invalidate final solutions. |
| F192 | Answer 413 only tests edges assigned color 1 and therefore accepts the empty edge set, including the all-zero weak solution already counted in 410(a). At completion require E to be nonzero. The historical replacement and unpurify correction do not add this test. |
| F193 | Answer 416's finite bound for 3-clue puzzles fails on a 3x3 puzzle with six 3s and its unique 16-edge loop. It needs a boundary term for odd n. The zero-clue argument also overstates required edge deletions: a 2x2 puzzle with one corner 0 deletes four edges and leaves one cycle. The valid general lower bound uses n^2-1, not n^2+2n. Both asymptotic density conclusions survive. |
| F194 | Answer 430(d) intersects combination bitmaps X_hp and Y_vq. The later V_vq is an item name, not that bitmap; replace it by Y_vq. |
| F195 | Answer 434's leading maximum-block count is 2n^2/3, not n^2/3. The displayed periodic pattern supplies n^2/3 horizontal and n^2/3 vertical blocks up to boundary terms. The finite 9x9 value 38 is not disputed or recomputed. |
| F196 | SAT25: seven-clause internal nodes number floor(n/2)-2, not ceil(n/2). At n=7 the actual contributions are 3*3+1*5+1*7+2=23, agreeing with the correct final 5n-12. The printed intermediate categories instead sum to 44. |

## Errata and public-report search

The November 12 source manifest covers cumulative and current 4B, Fascicle 5
and Fascicle 6 errata, including the available TeX sources. Relevant historical
answer coordinates were checked as well. Nearby changes to MPR114, MPR140(e),
MPR144, tower examples, twin trees, answer 404, answer 413 and SAT24 address
different lines. In particular the complete historical replacement of answer
413 still lacks a test excluding the empty solution.

Public searches combined Knuth/TAOCP, exercise numbers and distinctive terms:
minwise sketches, smoothed records, pentomino calendar QTX, polyspheres,
motley dissections, futoshiki, slitherlink empty solutions, kakuro and totalizer
node counts. No matching prior error report was found.

The relevant public [tamnd/brain answers](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4/7.2.2.1)
were inspected at 291,343,354,356,371,392,393,394,405,413,416,430,434.
Several are incomplete or mathematically incorrect. Answer 405 independently
uses the usual visited set containing the start, and 413 proposes a different
terminal connectivity test, but neither identifies the printed discrepancy.
Answer 434 discusses only the finite 9x9 result, not its asymptotic coefficient.
The SAT25 page answers an unrelated local-lemma problem and supplies no report.

The [original smoothed-analysis paper](https://lipn.univ-paris13.fr/~cb/Papers/smoothed.pdf)
is supporting provenance for F178, not a later erratum to this book. Likewise
the correct coefficient in Alon's original Nullstellensatz proof supports F176.
[Curtis Bright's totalizer discussion](https://www.curtisbright.com/bln/2024/12/31/the-totalizer-cardinality-constraint-encoding-for-sat/)
does explicitly discuss Knuth, but its concern is balanced versus complete
binary trees and attribution, not the wrong intermediate count in SAT25.
The [Japanese SAT tutorial](https://taocp-fun.gitlab.io/v4f6-sat-tut/)
did not supply a matching correction either.

These checks establish no absolute priority. Private reports and unavailable
physical copies were not inspected.
