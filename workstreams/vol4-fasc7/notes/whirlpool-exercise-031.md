# Whirlpool permutations — exercise31, every part

Source: exercise31 p115/file130 and answer31 p164/file179; both original
layouts have been viewed. The7 June2025 public correction changes answer(d)
from True to False. The corrected answer is proved below; it is not a new
finding. A matrix's entries are distinct, and a histoscape additionally uses
the nonnegative integer heights of27. Matrix comparison for(c) is row-major
lexicographic order. No numerical search is needed for this block.

## W31-0 — local vortex criterion and all eight examples

For a2×2 matrix `[[a,b],[c,d]]`, read the circular boundarya,b,d,c. LetS be
the number of ascents on its four directed edges, includingc→a. Since the
four values are distinct, S is1,2 or3. S=3 means exactly one descent, so
starting after that descent lists all four values in increasing order.
S=1 similarly lists them decreasingly after a suitable cyclic start. Thus
the boundary is a vortex iff S is odd, exactly the auxiliary criterion in
answer(b). S=2 has at least two ascents and descents and cannot be a vortex.

Choose the position of the minimum in four ways and the direction of increase
in two ways. The rest of a vortex is then forced, giving exactly eight for
the values1,2,3,4. The printed matrices

`[[1,2],[4,3]], [[1,4],[2,3]], [[2,1],[3,4]], [[2,3],[1,4]],`
`[[3,2],[4,1]], [[3,4],[2,1]], [[4,1],[3,2]], [[4,3],[1,2]]`

have precisely these four minimum positions and two directions without
duplication. Each boundary follows the corresponding cyclic sorted order.

## W31-a — the Dürer-square repair

Exchange14 and15 in the last row, changing it from(4,14,15,1) to(4,15,14,1).
The ascent-countS table for the nine adjacent2×2 blocks then is

`[[3,1,1],[1,3,3],[3,3,1]]`.

Every entry is odd, proving that all blocks are vortices. For example, the
bottom central block has boundary6,12,14,15, with three ascents. Before the
swap its boundary was6,12,15,14, with two ascents. No other block changes
validity: the two other affected bottom blocks retain counts3 and1, while
the upper six are untouched. The two exchanged cells are rookwise adjacent,
as required. This verifies the before/after obstruction and every block.

## W31-b — adjacent swaps and the dimension boundary

Take a circularly sorted list of four values and interchange two neighboring
positions. Orient/restart the circle so the original order is increasing.
If the exchanged pair does not straddle the maximum/minimum break, its
internal edge becomes a descent while the original break remains a descent;
the two other edges retain at least two ascents. If it does straddle the
break, instead start the cycle at another point: the swapped extreme values
create two descents at their two outer neighbors and two ascents. Equivalently
checking the four adjacent pairs of(1,2,3,4) gives exactly two ascents each.
Reversing orientation gives the same conclusion. The swapped block is never
a vortex. This is a complete four-position argument, not a claim that every
adjacent swap of a non-vortex reverses ascent parity.

For m,n≥2 any rookwise adjacent pair belongs to at least one adjacent2×2
block. Swapping it therefore destroys at least that vortex and hence the
whole whirlpool property. There is a genuine dimension qualification:
with one row or one column the2×2 conditions are vacuous, so a nontrivial
adjacent swap preserves the property. The exercise does not state a minimum
dimension, and the usual nontrivial-grid convention may be implicit. Keep
this exact one-dimensional exception partial as an interpretation, without
a new error card. The1×1 case has no adjacent pair and is vacuously safe.

## W31-c — lexicographically first matrix

The claimed matrix has consecutive blocks ofn values in successive rows,
increasing in the first row and alternating direction thereafter. In any
two adjacent rows, all lower-row values exceed all upper-row values. If
the upper adjacent pair increases, an opposite decreasing lower pair has
three cyclic ascents; if the upper pair decreases, an increasing lower pair
has one. Thus every adjacent block is a vortex and the whole construction
is feasible.

Now prove lexicographic minimality. The first row can be1,...,n and no
smaller row is possible. Suppose all earlier rows have been fixed as stated;
they have used exactly the smallest available prefix of values. Every
remaining value is larger than the preceding row. The odd-ascent criterion
then forces every adjacent pair of the next row to have the opposite order
from the preceding row. Hence the next row must increase or decrease as
specified. If increasing, its lexicographically smallest choice uses the
n smallest remaining values in order. If decreasing, its first value must
have at leastn−1 smaller remaining values, so it is at least the nth
smallest remaining value. Equality, followed by the n−1 smaller values in
descending order, gives the unique lexicographically smallest row. The
alternating construction extends either choice through all remaining rows,
so no feasibility constraint forces a larger choice. Induction proves the
claim. For n=1 the same formula gives1,...,m, the ordinary lexicographic
minimum; for m=1 it gives1,...,n. These cases need no vortex constraint.

## W31-d — corrected answer False, with both directions separated

For four distinct nonnegative heights, H27-2 says the block is a3VP exactly
when its unique maximum and second-largest value occupy adjacent corners.
Every vortex has that adjacency. Therefore a whirlpool matrix does yield
a3VP histoscape, by the complete local criterion.

The converse fails already for `[[4,3],[2,1]]`. The maximum4 is adjacent to3,
so it is valid case4 of27, and its histoscape is a3VP. Its cyclic boundary
4,3,1,2 has two ascents, so it is not a vortex. The corrected False answer
is established by a positive-height example with distinct entries and no
degenerate dimensions. The public correction accounts for the printed True.

## W31-e — translation moduloM

Assume M exceeds the full matrix's value range, henceM>0. Distinct entries
remain distinct moduloM: equality of two residues would make their nonzero
difference an integer multiple ofM, impossible in absolute value less thanM.
All translated entries lie in an interval of length less thanM. Reducing
moduloM cuts that interval at at most one wrap point, so their linear sorted
order is changed only by a cyclic rotation. For every subset of four entries,
their circular sorted order is consequently unchanged. A clockwise or
counterclockwise vortex remains such a vortex. Applying this to each2×2
block proves the transformed matrix is a whirlpool, for every real shiftx.
No integrality ofx is needed for this order argument. In a histoscape use,
heights would of course need to remain nonnegative integers, a different
condition not asserted by part(e).

Every part is now proved on its explicit input scope. Only the unstated
dimension convention in(b) remains partial; the later enumeration/recurrence
exercises32–33 are separate work.
