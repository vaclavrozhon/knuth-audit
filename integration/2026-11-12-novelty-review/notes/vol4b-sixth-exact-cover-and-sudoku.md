# Volume 4B: exact cover and sudoku, F101–F124

Reviewed on 12 November 2026 against the first edition, second printing.
The original typesetting and the existing proof/counterexample records
were compared. DLX below means section 7.2.2.1; earlier exercises are
in section 7.2.2. Large completed searches were not repeated.

| Finding | Correctness review |
|---|---|
| F101 | Answer 37(e): the two commafree constructions do select different words. However, the exact length-33 counterexample was explicitly published by Perrin and Reutenauer in Example 17. This is prior public mathematical discussion, even though the article does not label the book sentence an erratum. Remove from the new-finding view. |
| F102 | Answer 27: the completed unmodified author program used 1,828,460,227,444 memory accesses, approximately 1.83 teramems, not 18.3. Independently, the printed profile and rounded mean domain sizes imply a conservative upper bound of 6,635,380,138,340 accesses, already refuting 18.3. The precise revised value relies on the stored completed run, not a new timing experiment. |
| F103 | Answer 32: Strand volume 56 is July–December 1918; its page 74 contains the specified NESTLES word square. The printed second citation's 1919 should be 1918. The archived title and contents pages corroborate the year. |
| F104 | Page 36: allocated trie nodes represent proper prefixes, with length less than n. The final edges contain word ranks. Including length n would give 39,394 nodes instead of the stated correct 23,667 for the six-letter dictionary. Change the upper inequality only. |
| F105 | DLX 14: expanding the preceding correct sum requires numerator indices n−2, n−4, n−6. The printed n−1,n−2,n−3 gives −5/6 at n=3, whereas the sole permissible seating gives 1/6. The subsequent asymptotic claim is outside this local correction. |
| F106 | DLX 23(a): the first example has the top queen in column 2, so its parameter is a=2. The bottom mate belongs in column 15, with diagonal labels 31 and 1. Keeping column 14 requires removing y1; the stored legal sixteen-queen placement demonstrates the otherwise false exclusion. The published ratio 3.68→3.58 is a separate correction. |
| F107 | DLX 24: at n=4, the stated half-turn filter rejects both 2413 and 3142, although it should retain one. The quarter-turn filter similarly removes both options. The defect survives the natural geometric reading. Filtering the actual top-row queen by k>n/2 repairs the first; deduplicating identical item sets repairs the second. |
| F108 | DLX 22(c): the last count is 1,220,918, not 1,220,908. The decomposition (14,772,512−454,376−8·568,849)/8 gives the corrected number independently of the stored direct enumeration. |
| F109 | DLX 32(d): primary a,b and secondary x,y with options ab, ax, by give two solutions at Hamming distance three although every option has two items. Equal numbers of primary items, as already used by the answer, are the required hypothesis. |
| F110 | DLX 39(b): sampling with replacement counts solutions by option indices. With three singleton options independently chosen from a,b, the mean number of solutions is 3/2; the printed formula gives 3/4 by counting distinct partitions. For n=kr, the corrected mean is P·(m)_k/N^k, where P=n!/(k!(r!)^k), N=binomial(n,r), and (m)_k is the falling factorial. The numerical effect in the book's large examples is small. |
| F111 | DLX 37(a): the displayed recurrence gives a[2,3]=5 and a[3,2]=1, while q_2=3. Thus the stated unit entry is a[q_i,i], with the indices interchanged. |
| F112 | DLX 48(a): row 5, value 5 must name column 4, already fixed in the input sudoku. The printed 6 is a single erroneous entry in the transposed candidate chart. |
| F113 | DLX 49(a,b): in the column construction the varying row index is i, hence the left endpoint is u_i. In part (b), the complementary size is r−q, using the variable introduced in the question, not n−q. The Hall-style matching argument otherwise remains valid. |
| F114 | DLX 57: after fixing the first box and first row 1472AB3CD as printed, there are 432 solutions. The stored 864 solutions use a weaker normalization permitting exchange of the two right stacks; this freely pairs them, with exactly one partner satisfying the printed first-row condition. |
| F115 | DLX 57: row and column permutations alone leave six classes of the listed sudoku solutions. The stored witness has a row-pair digit permutation absent from every row pair of the displayed grid, ruling out even unrestricted row/column permutations. Allowing digit renaming gives the intended single class. |
| F116 | Page 78, figure 35(b): the sixth row 6971426 repeats 6, as do the affected column and box. Replacing its last digit by 5 repairs all three. This is a direct contradiction of the stated rules for the rectangular sudoku. |
| F117 | Answer 65: retain only as a local PDF defect. The lower-right SOLVING cell paints S over the given and correct G. The author PostScript has a clean G. This does not establish an error in the printed book or attribute the corruption to the author. |
| F118 | Answer 65: SUDOKU's second row must be DUSKO., since the printed DUSK.O repeats O in the last column. The June 2022 erratum swaps D and U in the first row and does not fix this second-row defect. |
| F119 | DLX 69: the number of admissible convex nonomino placements containing six B cells is 1647, not 1467. The stored 1647 distinct witnesses, full 12097-placement histogram and independent subset construction agree. This count concerns individual placements; the final counts of complete districtings are unaffected. |
| F120 | Page 82: with row index 0 through 19 and column index 0 through 2, the last cell is j2, where j denotes 19. The printed 2j names a column outside the rectangle. |
| F121 | DLX 75(b): the required identity is f(t XOR f(t))=t. With f=(0,2,3,1), ordinary addition asks for undefined f(5) at t=2; addition modulo four also fails at t=3. The five multiplication tables themselves remain correct. |
| F122 | DLX 76(c): an identity element 0 forces x composed with x to equal 0. The reduced item universe must therefore omit diagonal items too. At order two, the legitimate XOR table exists, whereas the literal reduction leaves item 11 with no covering option. |
| F123 | DLX 83: pairwise distinct final secondary items do not prevent an earlier such item from occurring inside a later option. For p a / p a b / p c / q a, the modified algorithm covers a twice and later restores the forbidden q a row. Both the literal trace and adapted author program exhibit the invalid solution. A uniqueness hypothesis among the options for p repairs this; the known j>N1 erratum does not. |
| F124 | DLX 86: an empty C6 loses both the reverse uncommit operations and restoration of the current item i. The two singleton options p and q already leave p covered after the trial, so a second trial explores a different tree. Preserve rollback and i restoration, skipping only advancement to another option. |

## Sources and novelty

The refreshed current/cumulative 4B and Fascicle 5 errata and their TeX
sources were compared by page, exercise and subject. Published F5 pages
use the main-text offset −2 and answer offset −192. The 2019 pre-fascicle
5C answer offset is −296. The recorded queen ratio, graph-edge addition,
first-row SUDOKU swap, grope bibliography addition and secondary-item
threshold correction concern different assertions. No matching official
correction was found for this block.

F101 is nevertheless already public: see the
[specific review](vol4b-f101-prior-public-report.md) and
[Perrin–Reutenauer, Example 17](https://arxiv.org/pdf/1609.05438).
The preprint submission is dated 18 September 2016; the journal version
appeared in 2018. Our original audit had already cited this example,
but absence from official errata did not justify treating it as novel.

Searches combined Knuth/TAOCP with Scholtz/Eastman, 18.3 teramems,
Strand 1919, the ménage identity, 1220908/1220918, uniformity and secondary
items, random exact cover, sudoku 432/864, Behrens, DUSK, 1467/1647,
grope XOR, and Algorithm C/C6/Monte Carlo and exercise 83. Search results
were mostly unrelated or reproduced the original text.

The [public tamnd/brain entries](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4)
were also read for backtracking 27,32,37 and DLX
14,22,23,24,32,37,39,48,49,57,69,75,76,83,86. No matching error report
was found there. In particular, entry 57 weakens the distinct-trio
condition and discusses an earlier proposed solution; it does not give
our normalization count or row/column obstruction. Entry 86's corrected
solution discusses its own generic estimator and does not identify the
book's rollback error.

Decision: 23 retained, including the explicitly scoped local file defect;
F101 previously publicly discussed. For the retained findings, the
conclusion is no matching prior report found in the searched sources,
not established priority.
