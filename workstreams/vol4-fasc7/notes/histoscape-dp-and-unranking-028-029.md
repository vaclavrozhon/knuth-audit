# Histoscape dynamic programming and unranking — exercises28–29

Scope: exercises28–29 p115/file130, answer28 p162–163/files177–178,
and every algorithmic step of answer29 p163/file178. Originals have been viewed.
Known corrections:11 September2025 changes the description of the fixed
coordinates in Q's subroutine;12 September2025 replaces the8×8 census;
13 September2026 changes n→t summands and suffix−1→+1 in29;14 September2025
replaces its example and geometric data. None is counted as a new finding.
The terminal index identification is separately documented in `F7-C0004.md`.

## Q28-1 — local constraint model

By H27-1 in `histoscapes-and-exercise-027.md`, the boundary at an interior
vertical grid line depends only on its four neighboring heights. The same
complete octant-link argument applies for every interior grid intersection
of anm×n matrix. Outer intersections have at most two adjacent nonzero
columns and introduce no additional failures. Thus the histoscape is3VP
iff every adjacent2×2 block satisfies the corrected relationr of27. There
are(m−1)(n−1) such blocks whenm,n≥1. In particular an8×8 matrix has64
independent entries and10^64 possible assignments before constraints.

The transfer method below does not rely on any symmetry ofr and permits a
different relation at each block. Optional seam relations also work, as in
the printed generalization.

## Q28-2 — invariant, initialization and all loop indices

Assume initiallym≥2,n≥1 and a finite common domaint. Write the entries in
row-major order asy0,...,y_(mn−1), wherey_(in+j)=aij. Immediately before
subroutine(i,j), putR=in+j. Exactly the firstR entries have been assigned.
The frontier consists of the lastn+1 of these entries, positions
R−n−1,...,R−1. The array valuec(x0,...,xn) counts assignments of that prefix
which satisfy all already completed constraints and have these frontier
values in cyclic order starting at slotq=(j−i) mod(n+1).

For the first step(i,j)=(1,1), R=n+1 andq=0. Fixing all frontier values
already fixes the entire prefix, which has no completed constraint. Every
initial count is therefore1. This explicitly justifies the initial array;
it is not a count of arbitrary unconstrained earlier entries.

Forj<n the four arguments of the new relation are positions
R−n−1,R−n,R−1,R, namely
`(a_(i−1)(j−1), a_(i−1)j, a_i(j−1), a_ij)`.
The first three occupy slotsq,q+1,q−1 modulo(n+1). On crossing a row boundary,
j=n, the new value isy_R=a_(i+1)0 and the same four positions are exactly
the four seam entries printed in the answer. Making this relation universal
adds no unwanted condition. It is needed to advance/eliminate one variable
between the end of a row and the next ordinary block.

Q2 therefore runsj=1,...,n for every nonfinal row and1,...,n−1 for the final
row. There areP=(m−1)n−1=mn−n−1 updates, exactly the number of variables
remaining after initialization. No seam after the last row is processed.
The new position grows by one at every update. The oldest frontier slot
also advances by one, because
R−(n+1)=(i−1)n+j−1≡j−i mod(n+1).
This proves the printed cyclic invariant even across row transitions.
The2×(m−1)n display is precisely two consecutive row-major windows separated
byn positions; neighboring columns of that display give the same ordinary
and seam relations. It is a restatement of the indices, not a new model.

## Q28-3 — update, in-place safety, summation and termination

Fix every coordinate other thanq. For a proposed new valued, partition all
admissible prefixes by the old oldest valuek. The new constraint permits the
class exactly whenr_ij(k,x_(q+1),x_(q−1),d) holds. These classes are disjoint,
so their counts add and give precisely the printed sums_d. Replacing slotq
byd discards the oldest value and appends the new one. No later constraint
can need that discarded entry: every future ordinary/seam relation uses
only the current frontier and its new value. Thus the invariant propagates.

Allt sums in one fiber must be computed before any value in that fiber is
overwritten, exactly as printed. Different fixed-coordinate fibers have
disjoint array cells, so updating another fiber never destroys a needed
input. The public wording correction clarifies that there aret^n choices
of the other coordinates; the original x_q=0 notation was a way to choose
representatives of those same fibers.

AfterP updates every entry and every required constraint has been processed.
The frontier tuples partition all full solutions, so Q3's sum gives their
number with no multiplicity. The nested finite loops terminate, and all
index accesses are within the stated cyclic array and finite matrix.

For reference, each update uses at mostt^(n+2) relation tests/additions,
plusO(t^(n+1)) assignments. Initialization/final summation costO(t^(n+1));
the count array and temporary fiber useO(t^(n+1)+t) integers. For explicit
constant-time relation lookup andt≥2 this gives
O(t^(n+1)+P·t^(n+2)) arithmetic operations. Counts haveO(mn logt) bits, so
the arithmetic model must not silently treat arbitrarily large counts as
fixed machine words. The historical teramem/24GB assertions are not implied
by this bound and remain separately partial.

The analogy to4.6.4–(40) was checked in the actual Volume2 p502/file514,
saved as `images/vol2-p502.png`. That formula likewise successively sums out
one coordinate with a weight while retaining the others and rotating the
coordinate order. Finite distributivity establishes this structural analogy;
no Fourier-transform theorem or complexity bound is imported into Q.

## Q28-4 — boundaries and tiny independent traces

For t=0 and positive dimensions the sum is empty and the solution count0;
for t=1 the same invariant applies with at most one assignment. Forn=1,
ordinary2×2 constraints are absent, but the universal seam steps correctly
produce t^m. The one-row case m=1 needs separate treatment: there are t^n
matrices, whereas the literal unmodified initial array would sum to t^(n+1).
The official `HISTOSCAPE-COUNT` and `HISTOSCAPE-UNRANK` explicitly require
m,n≥2, supporting the intended nontrivial scope. Since the book's general
algorithm paragraph does not state that bound, its one-row wording remains
an explicit scope partial, not a confirmed new finding.

Four fixed traces in `results/histoscape-dp-targeted.json` use dimensions
2×3,3×2,3×2 with an additional seam relation, and3×1. The ordinary relation
is asymmetric and position dependent, so exchanging its arguments would
not pass unnoticed. All terminal counts and index positions are stored.
The traces agree with direct inspection of only219 tiny assignments and
yield39,42,25,27 solutions. They support the general invariant proof; they
are not evidence for the large8×8 number. One nice15 run, no large restart.

## U29-1 — terminal choice and the required rotation

For nonnegative integer weights c0,...,c_(L−1) with totalN and integer
0≤k<N, subtract each weight untilk falls below the next one. Zero weights
are automatically skipped. Disjoint half-open rank intervals of these
lengths partition[0,N), so a unique choice is made, the residual rank lies
in that class, and the loop terminates before reachingL. This proves the
first weighted selection in the answer, for any fixed enumeration of counts.

The chosen slot values must be assigned to the actual final frontier.
Immediately after the last update the cyclic start is
s=(n−m+1) mod(n+1), so the lastn+1 row-major entries correspond to slots
s,s+1,...,n,0,...,s−1. The answer's unshifted tuple is the specific issue
F7-C0004. The official source's `pos[q]` mapping preserves the rotation.
Everything below assumes this corrected mapping; a proven unranking method
does not retroactively validate the erroneous printed intermediate mapping.

## U29-2 — reverse update, suffix length and complete reconstruction

Suppose the suffix starting at the current oldest frontier entry is fixed,
andk is its rank among the compatible earlier prefixes. To undo update(i,j),
obtain the counts immediately before it and consider each old valuea in a
fixed order. Its weight is the old count multiplied by the new relation's
0/1 indicator, with the already fixed new valued and other frontier values.
There are at mostt such terms, as in the public n→t correction. Their sum
is exactly the count of the chosen later class, so the weighted selection
lemma applies. The chosena fixes positionR−n−1=(i−1)n+j−1 and leaves the
residual rank within that prefix class.

Consequently the known suffix has length
mn−((i−1)n+j−1)=(m−i+1)n−j+1, proving the other public correction.
Reversing all updates, including seam advances, fixes one more entry at each
step. At the initial table all counts are1 and the remaining frontier fixes
the whole prefix, leaving rankzero. The final matrix satisfies every relation,
because each selected predecessor had positive weight. Conversely, any valid
matrix follows a unique terminal class and a unique predecessor at each step.
The resulting correspondence between ranks and solutions is therefore a
bijection, not merely a generator that happens to produce valid examples.

If earlier tables were discarded, rerunning Q up to the required point
recovers exactly the same predecessor counts; the terminal aggregate alone
does not determine its separate summands. The answer explicitly supplies
this rerunning step. A straightforward implementation uses at mostO(P²)
updates in total, thusO((P+1)·t^(n+1)+P²·t^(n+2)+mn) arithmetic operations and the
same count-array space, plusO(mn) cells for the selected solution. Restricting
the recalculations to the fixed suffix is valid: inconsistent states have
zero weight, and no branch leading to the selected suffix is removed. The
official program's particular speedups/counters are not independently proved
or benchmarked by this argument.

The four small traces unrank every one of their133 solutions and compare the
entire resulting set with direct assignments: no duplicate or missing rank.
They keep small predecessor tables for review rather than reproducing a
large rerun. Uniform integer choice ofk in[0,N) now gives each solution
probability1/N by the bijection. N=0 admits no choice; deterministic k≈N/phi,
used by the book as a quoted “random” example, does not itself claim a uniform
random draw. Its exact rank is a separate unverified item below.

## U29-3 — printed matrices and explicit remaining partials

Both the original and replacement8×8 matrices were transcribed directly
from the original page/primary erratum. A fixed boundary construction,
`results/histoscape-witnesses.json`, verifies all local3VP conditions and
lists their entire geometry. The original has184 vertices,276 edges and94
faces, each with one boundary polygon. The replacement has204 vertices,
306 edges and102 connected faces but104 boundary polygons. The replacement
specifically says104 **face polygons**, which agrees; treating that as104
connected faces would create a false discrepancy. The geometric extraction
is justified by the exposed-square/merged-plane construction in H27-4 and
the detailed algorithm30 proof to follow. This is only two fixed objects,
not an enumeration of the8×8 solution space.

The following remain separate partial claims:

* The corrected exact8×8 census
  573350756580609962448490328484980268982588520613841558, and its2.3-teramem
  historical cost/24GB measurement. Neither the printed old number nor the
  new one has been independently reproduced here.
* The claim that the replacement example is obtained by the specified rank
  N/phi and enumeration, which depends on that census and large unranking.
* Exact visibility in the particular projected illustrations (89 vertices;
  original48 or replacement49 partly visible faces).
* Projected T/V/W/Y junction counts and the line-labeling solution counts,
  independent ambiguities and forced labels. These require the later line
  labeling definitions and an exact reconstruction of the illustrated view.

Those are mathematical/model gaps, not bibliography skips or checked pages.
The official source references are retained in
`sources/histoscape-programs-manifest.json`; they support the intended input
scope and rotation comparison, not a claim that the large runs were executed.
