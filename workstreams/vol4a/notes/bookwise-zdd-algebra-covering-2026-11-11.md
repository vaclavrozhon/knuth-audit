# Family algebra and exact covering

Main251–252, exercises203–218 and answers660–665 through218 were
read together. Whole main251–252, exercise273–274 and answer660–664
are certified. Shared answer665 awaits the dictionary exercises.
F0047 and F0048 concern the exact-cover profile comparison and the
last two coverage counts of the mutilated chessboard.

In203–204, ordinary union/intersection of families are distinct from
joining/intersecting their member sets. The existential Boolean
formulas, distribution counterexamples, orthogonality and fixed
families were checked. An apparent mismatch in203(c)(iv) disappeared
on enlarging the original: the round union signs differ from the
square join signs. The quotient's universal condition gives its
intersection law and order reversal; applying that reversal twice
to the displayed inclusion gives the triple-quotient identity.
The decomposition by presence of one element is unique and yields
the listed quotient/remainder formulas.

The five recursions in205 follow that decomposition. In a join, the
high branch combines three ways to contain the element; in a meet,
the analogous three cases belong to the low branch; in a delta,
the two equal choices go low. Division first enforces all high
members of the divisor, then intersects with the low-member condition.
Terminal cases and the explicitly stated temporary-reference changes
were checked. The obsolete polynomial upper bounds in206 are a
known2025 correction and are excluded from new findings. No new
worst-case construction or implementation was attempted.

The symmetrizing recursion207 tracks how many chosen elements remain
and inserts both branches for variables outside the selected set.
Its changing f_v is read as a local index, not a mutation of a shared
node. Counting208 counts branch paths without skipped-variable
multipliers. Truth-table elaboration209 fills skipped high halves
with the all-false suffix. Optimization210 retains exactly the
branches attaining max(m_l,m_h); its stated optimum-value field is
read with this implicit maximum assignment. No complete toolkit was
implemented or subjected to a general verifier.

The exact-cover encoding129 imposes one selected row per column.
The intermediate q[k]-1 comparison in211 fails when zero is absent
(F0047), while the intended BDD/ZDD comparison follows using q'[k].
The five accumulation orders in212 are valid conjunction trees;
their historical costs and node totals were not rerun. The transpose
restriction pairs coverings by the orientation of the top-left
domino. Color balance proves the mutilated-board impossibility;
the printed final coordinate pairs have wrong parity (F0048).

The faultfree and tatami constraints214–215 respectively require a
crossing domino on each interior line and a domino through each
interior grid corner. The sample variable sets match the ordering
of the112 placements. Tripling each nonsink in216 gives the stated
color-choice structure, and existentially forgetting color merges
all colorings of the same covering. Separation217 is a conjunction
of forbidden adjacency pairs. Exact census/uniqueness/node totals,
all682/4198/1948 adjacency cases and external tiling classifications
were not independently reproduced.

For Langford pairs218, the first2n columns are positions and the
last n columns select each number once. The seven displayed rows
for n=3 use reversal symmetry: the first1 lies in positions1..n-1.
This removes n-1 rows from the unrestricted 3n(n-1)/2, giving the
printed C(2n-1,2)-C(n,2) and187 for n=12. The previously established
definition of L_n counts reversal classes. Its numerical census and
the associated historical ZDD/BDD benchmarks were retained, not rerun.

Next: dictionaries from main253, exercises219 onward, answers665 onward.
