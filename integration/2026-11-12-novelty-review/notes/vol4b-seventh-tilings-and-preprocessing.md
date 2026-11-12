# Volume 4B: F125–F148 publication review

Reviewed 2026-11-12 against the first edition, second printing PDF, with the
relevant original page images, detailed existing arguments, and certificates.
All 24 findings are retained. This is a review of correctness and available
prior reports, not a claim of absolute priority.

The November 12 source refresh covers cumulative and current Volume 4B and
Fascicle 5 errata, including the TeX versions. Relevant entries were compared
using the published fascicle and prefascicle page offsets. In particular, the
corrections to answer 120(a), the boundary convention in answer 133, the polygon
parameters in answer 143, the gallery in answer 173, and benchmarks in answer
207 do not repair the findings below. F140 concerns an error in the current
official correction itself.

| Card | Rechecked reason |
| --- | --- |
| F125 | Answer 86: a cleansing count C after choosing one of theta branches has sampling weight D*theta, not D. Two differently colored options on p and x already give estimate 1 instead of the full count 2. This is independent of the rollback defect in F124. |
| F126 | Answer 86: when the selected item is empty, the early jump skips the LLINK(r) update. The single empty primary item has full update count 1 but estimate 0; a nonempty two-option example has 5 versus 4. Account for C4 even when theta is zero. |
| F127 | Answer 91: the WORDS500 left-word graph core has 12,269 arcs, not 13,677. The archived input, independent core reductions, and native DLX2 construction agree; the longest-period claim is unaffected. |
| F128 | Answer 92: right-stair constraints require the i-j diagonal index, with the appropriate reversed color sequence, instead of i+j. The WAVES/LINED/LEPER example directly distinguishes the two diagonals; a two-letter certificate also distinguishes the resulting solution sets. The earlier marker-name erratum does not fix the index. |
| F129 | Answer 109: under the stated one-based grid convention the forced items are H11, H31, V41; the printed H00, H20, V30 are undefined or displaced. |
| F130 | Answer 109: after explicitly dropping connectivity condition (iii), a single row containing ZERO through TEN separated by dots has area 53, below the claimed minimum 55. The original question does not require both side lengths to exceed one. No claim that 53 is globally minimal is needed. |
| F131 | Exercise 120: Wang's November 1965 Scientific American article is in volume 213, issue 5, pages 98–106, not volume 231. Fresh Crossref metadata for DOI 10.1038/scientificamerican1165-98 agrees with the archived primary bibliographic evidence. |
| F132 | Answer 120(b): tile types 2, 4, 6 repeated by (row+column) mod 3 form a valid periodic tiling, distinct from the displayed 13-cell pattern. No condition requires using every tile type. The official replacement concerns part (a). |
| F133 | Answer 134: the component multiplicities are P=1,685 and Y=243, not 1,672 and 242. The small explicit certificate alone exceeds both printed counts; the complete stored census agrees and uses the corrected symmetry convention. |
| F134 | Answer 140(c): the third tetrahex has a mismatched triangle. Rotating the indicated triangle by 120 degrees repairs the two mismatches while preserving all 24 tile types. The detailed original color crop and the 72-corner verifier agree. |
| F135 | The cited title is Surprenants triangles, with a final s in the first word. The archived BnF record cb346060085, field 200$a, and original Trioker rules agree. The current BnF web fetch was unavailable; the previously retrieved primary record remains the evidence. |
| F136 | Answer 142(ii): the cylinder count is 2*55,980, not 2*5,980. The stored explicit 5,981 representatives and their reflected partners already exceed the printed total, without rerunning the full census. The cut is distinguished and color renaming is factored out consistently. |
| F137 | Answer 143(b,c): the 12-by-1 strip can also be tiled by all 24 Langford triangles. The embedded two-row color certificate verifies directly, so four of the six shapes are possible, not three. The old correction of the strip parameters to (12,12,1,0) is already incorporated and does not remove this counterexample. |
| F138 | Answer 147(b): four entries in the 2-by-2-by-4 brick symmetry histograms are wrong. The stored witnesses and automorphism checks give (0,3,4,1), (0,11,12,2), (0,2,2,4), (0,1,3,1) for the four affected color patterns. The total number of classes remains 48. |
| F139 | Exercise 150: the pictured Endless Chain inventory has odd endpoint parity, so it cannot form a closed chain. It has one L piece and two S pieces where the answer uses two L and one S. The parity obstruction is independent of enumeration and agrees with the original piece crop. |
| F140 | The March 13, 2026 erratum changes Kautz's page range to 179–189, but the correct range is 179–180. Fresh Crossref metadata for DOI 10.1109/TEC.1958.5222529 confirms the two-page range. The full article was not newly obtained. |
| F141 | Answer 173: the claimed first publication in December 2018/January 2019 is too late. Nacin's own dated posts describe knight sudoku on May 16 and bishop sudoku on June 6, 2018; the knight puzzles also appear in the September 2018 College Mathematics Journal. The October 2023 gallery erratum leaves this historical paragraph intact. |
| F142 | Answer 189: the stated Gompertz formula is not a proper distribution for arbitrary positive a,b. With a=4, b=1/2, x=1 its value is -1. For a proper finite distribution of the displayed form require a>1 and b>1; both below one instead leave positive mass at infinity. |
| F143 | Main text page 104: the example called 2DM is a general exact 2-cover instance, not bipartite matching. Its edges 14, 15, 45 form a triangle, contradicting the immediately preceding definition of 2DM. The unsatisfiability and tree size do not change. |
| F144 | Answer 207(c): after choosing 00 01, item 04 has degree 5, not 4. The four-way branch is on 03 (or 05). The residual options give degrees 3,4,5,4; mu=5/4 and rho=1/2 make the printed branch preference fail for 04. |
| F145 | Answer 221: the q>=x loop revisits its starting node after the end spacer points back to x. With primary a,b and secondary s, options a s:1, a, b s:2, deleting the first option falsely reaches P9 although the last two solve the instance. A post-test q>x traversal, or processing the first node last, removes each node once. |
| F146 | Page 111: no Y pentomino placement contains both 00 and 22; its bounding box is 2-by-4 or 4-by-2. Thus 22 cannot force 00 in the stated residual instance. The stored native traces support 11 as the intended item, but the geometrical contradiction establishes the error independently. |
| F147 | Answer 236: the displayed 128-queens board has only 127 queens and an empty final row. The missing queen is at (128,65), matching the last entry of Fischetti and Salvagnin's original list. The fresh bottom crop confirms the empty row. |
| F148 | Page 116: the stated historical population data give New England 14,445,438 (14.4 million), with New York 33,823,525 (33.8), and the smallest displayed non-New-York cluster 37,177,055 (37.2). The printed 14.3, 33.7 and 37.3 are inconsistent with these inputs; no new optimization is required. |

Public checks included distinctive combinations of Knuth/TAOCP with 12269 and
13677, the 53-cell word rectangle, Wang tiles and exercise 120, the cleansing
estimator, 1685 pentomino components, Langford's 12-cell triangle strip, the
5980 cylinder count, Endless Chain parity, Gompertz restrictions, 2DM triangles,
answer 207's four-way branch, answer 221's deletion loop, missing 128th queen,
and the population summaries. No matching prior error report was found.

The public [tamnd/brain solutions](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4/7.2.2.1)
for the relevant exercises were also screened. Several pages answer an unrelated
problem or explicitly remain unverified. In particular, exercise 150 asserts an
unsupported chain count and does not notice the inventory defect; 207 discusses
a different interpretation of growth and does not identify 04; 221 gives a
generic once-around deletion description, without identifying the printed
loop's repeated first node. A correct independent algorithm is not itself an
explicit prior report of this typo. Pages 239 and 246 do not discuss the
population arithmetic.

Primary source checks supporting individual corrections:

- [Nacin: Knight's Sudoku, May 16, 2018](https://quadratablog.blogspot.com/2018/05/knights-sudoku.html)
  and [Bishop's Sudoku, June 6, 2018](https://quadratablog.blogspot.com/2018/06/bishops-sudoku.html),
  both read again, plus his [2019 CV](https://www.wpunj.edu/cosh/departments/math/assets/2019_06_CV_Nacin.pdf).
- [BnF title record](https://catalogue.bnf.fr/ark:/12148/cb346060085), using
  the archived original XML when the current fetch failed.
- [Wang article metadata](https://doi.org/10.1038/scientificamerican1165-98)
  and [Kautz article metadata](https://doi.org/10.1109/TEC.1958.5222529),
  rechecked through Crossref's works API.
- [Fischetti and Salvagnin](https://arxiv.org/abs/1907.08246v1),
  [Knuth's population input](https://www-cs-faculty.stanford.edu/~knuth/contiguous-usa.gb),
  and the archived historical Census table used by the existing verifiers.

These sources establish the corrections; except where explicitly stated, they
do not identify the corresponding TAOCP error. Search coverage cannot establish
absolute novelty, and inaccessible full articles were not treated as read.
