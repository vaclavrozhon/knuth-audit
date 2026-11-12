# Exercise61: four originals, every count factor, and spatial realization

The question p119/file134 and the complete answer p171–172/files186–187
were displayed. The13September2026 known correction replaces−2z by−2x
in the third barycentric coordinate; the primary TeX and displayed short
errata PDF p13 were checked. It is applied throughout, not reported.

Evidence:
`check_box_arrays61.py`, `results/box-arrays61-native-cache.json`,
`results/box-arrays61.json`, `check_box_arrays61_geometry.py`,
`results/box-arrays61-geometry.json`, `check_box_arrays61_spatial.py`,
`results/box-arrays61-spatial.json`.

## E61-1 — every original path and every ordered junction

The four exact native path ranges, half-open, are37–775,775–1579,
1579–2321,2321–3089. All points are mapped to one triangular integer
grid per image. A fitted positive affine screen transform has residual
less than.01pt at every native point occurrence. Exact duplicated
segments are merged; every segment intersection is then checked and
split, and every local V/W/Y/T branch order is determined geometrically.

| Picture | V | W | Y | T | Total vertices | Lines |
| --- | --- | --- | --- | --- | --- | --- |
|i|48|83|36|95|262|369|
|ii|83|48|36|130|297|404|
|iii|51|80|36|98|265|372|
|iv|64|67|36|111|278|385|

Every outside face walk is computed from the exact rotation system.
Only its actual lines receive the standard clockwise boundary arrows.
No count is transferred from an assumed ideal picture: all counts below
use the fully reconstructed native relations.

## E61-2 — a finite certificate for complete factorization

Each junction has its complete previously proved Table1 relation.
Arc-consistency deletion removes a value only when no currently
allowed row contains it; thus it cannot remove a solution. At the
fixed point substitute all singleton values into every relation.
For each remaining relation, keep its complete projected row set
on the uncertain variables, removing duplicate rows only.

If that row set is the full Cartesian product of its variable domains,
the relation imposes no restriction. For every other relation, connect
its uncertain variables into one component. All proper constraints
then lie within a component; all constraints spanning components are
full Cartesian products. Consequently the solution set is exactly
the product of the component solution sets, with the fixed variables
inserted. This proves both completeness and independence.

Each small component is solved by natural joins of its explicitly
listed local rows: retain exactly those pairs of partial rows agreeing
on shared variable names. An induction on the number of joined
relations proves that the intermediate rows are precisely their
compatible partial assignments. Duplicate assignments are counted
once. The largest intermediate has64 rows; there is no unrestricted
search over all edge labels. The final complete representative is
checked against every original relation. Every propagation step,
projected relation, join size and final component row is saved.

The geometry was computed once and cached. An initial deliberately
bounded Cartesian method stopped before trying a5832-case component;
the final join method above handles it with at most64 partial rows.
No geometric restart or large enumeration was needed.

## E61-3 — picture(i) and every ambiguity of(ii)

For(i), all variables become singletons and their complete assignment
satisfies every relation. This proves existence and uniqueness.

In(ii), exactly25 components remain, each one binary physical line.
The non-T endpoint of each is a V and the other endpoint a T stem.
The fixed V branch leaves exactly two Table1 rows; the T bars are
already fixed and its stem imposes no additional restriction.
Every other variable is fixed. Thus all25 choices are independent
and exhaustive, giving2^25=33,554,432.

In the native cell coordinates(r,s), these are precisely
`1≤r≤5, 0≤s≤4`, a5×5 set of box tops. The geometry certificate
associates each physical V and each complete factor with its unique
box. Thus the printed explanation by25 interior box tops is checked
separately from the numerical product.

## E61-4 — every layer and local factor of(iii)

Use cell colors(r+s) mod3. The three adjacency steps(1,0),(0,1),(1,1)
change color by1,1,2, so each color is an independent set. Each of
the six rows has exactly two cells of each color, giving12 of each.
The observed T occlusions put color2 in front of both others, and
color1 in front of color0. The explicit depth model in E61-8 verifies
also the pairwise comparisons hidden by a third box.

Every front/color2 box is labeled uniquely. For the back/color0 set,
seven boundary boxes are labeled uniquely, while the following five
interior boxes contribute an unconstrained Y with three T stems:

    (1,2),(2,1),(2,4),(3,3),(4,2).

Every one of its five Table1 rows works, independently, so each gives5.

The middle/color1 set has five interior boxes

    (1,3),(2,2),(3,1),(3,4),(4,3).

Each has a Y joined to the middle branch of each of three W's.
The W middle branch must be+or−, so the Y can only be+++or---.
For+++, each W independently chooses O+I or−+−, giving2^3=8.
For---, each W must be+−+, giving1. Their other edges end in free
T stems. Hence the complete local total is8+1=9. This proves the
printed nine-way intermediate, not just a final aggregate.

Six middle boundary boxes contribute one binary W factor:

    (0,1),(0,4),(1,0),(2,5),(4,0),(5,2).

Its middle+is fixed and the other branches end in T stems, so its
two rows are O+I and−+−. The seventh middle boundary box, (5,5),
is the bottom one in the original screen transform and has every
label fixed by the standard outside boundary. This checks the
printed bottom exception. All24 front/back boxes and all12 middle
boxes have now been individually accounted for.

The separated local factors therefore give

    5^5 ·2^6 ·9^5=11,809,800,000.

## E61-5 — both circulations and every factor of(iv)

The outer perimeter has20 cells. In native coordinates take the walk
down r at s=0, across s at r=5, back up r at s=5, then back along
s at r=0. Every cell on this walk is in front of the next. The
analogous12-cell walk around1≤r,s≤4 has every next cell in front
of the current one. Both complete edge lists are checked from the
actual T occlusions. The walks have negative oriented screen area.
Thus, under the convention that overlap progression goes from the
covered box to the covering box, the outside progression is clockwise
and the inside progression counterclockwise, as printed. Their
opposite circulations do not depend on that naming convention.

The complete standard-label certificate has16 binary components,
one5-way isolated Y at(2,2), and two4-way Y/W components at(3,2)
and(2,3). A Y joined to one W middle branch permits two Y rows
with that branch−, each extending in one way, and the+++row
with two W extensions. Thus each4 is1+1+2. The saved rows
account for every physical edge of these components.

Consequently the exact product is

    2^16 ·4^2 ·5=2^20 ·5=5,242,880.

## E61-6 — every corrected barycentric coordinate and hidden corner

For the book's row/column indices(i,j), the corrected map is

    A=6i+j−2y−2z,
    B=−i+5j+2x+2z,
    C=−5i−6j−2x+2y,

where x,y,z∈{−1,+1}. Its sum is exactly zero. On this two-dimensional
coordinate plane, the affine map to the native integer grid is
`(A+B−30,A−5)`. The native cell coordinates correspond to
`i=s,j=5−r`. The resulting centers are exactly

    c_(r,s)=(−6r+5s,−r+6s).

All288 corner evaluations are explicitly saved and checked. Writing
x=2alpha−1,y=2beta−1,z=1−2gamma gives the screen displacements

    alpha(4,0)+beta(−4,−4)+gamma(0,4).

The two opposite vertices alpha=beta=gamma=0 and1 have the same
screen center. The former is the front Y; the latter is precisely
the book's(1,1,−1) and is hidden. The other six are the distinct
hexagon corners. The positive-depth chip construction of59 proves
the seven-front-corner statement for an isolated box; overlap can
hide more corners but cannot make the rear corner visible.

All36 Y centers and every non-T vertex in every original drawing
match their unique physical front corner. Every native line lies
on exactly one of the prescribed front cube edges, and every T
lies on exactly two original front-edge interiors. Thus the formula
is checked against every line, not merely its center lattice.

The reversed column coordinate between this formula and the convenient
coordinates in62 is explicit: in(r,s), adjacent boxes differ by
(1,0),(0,1),(1,1), up to sign. There is no unnoticed orientation
change in the dynamic-programming model.

## E61-7 — all intersections and the general-position assertion

Each projected box has the convex outline

    H={(X,Y): |X|≤4, |Y|≤4, |X−Y|≤4}.

Two outlines can overlap only if their center difference is in2H.
For a difference(X,Y)=(-6dr+5ds,-dr+6ds), the inverse formulas are
`dr=(-6X+5Y)/31`, `ds=(-X+6Y)/31`. On2H the absolute value of
either numerator is at most48. Hence dr,ds are each−1,0,1.
Of the eight nonzero choices, exactly the six signed neighbors
(1,0),(0,1),(1,1) lie in2H. This proves the neighbor list for
arbitrary array size; it is not extrapolated from six rows.

All12 projected edges of each cube, including rear ones, were
checked. Relative to cell(0,0), the complete inter-box crossing
lists for the three positive neighbor offsets are

    (0,1): (3,4),(1,4),(4,2),(2,2);
    (1,0): (−2,2),(−4,−1),(−4,−3),(−2,0);
    (1,1): (0,2),(−3,1),(−1,3),(2,4).

Each crossing is transverse and has edge parameters among1/4,1/2,3/4;
none is a corner. There are no other inter-box intersections.
The neighbor graph has maximum clique size3: the neighbors of one
cell form a six-cycle. A coincidence of crossings from different
pairs would therefore involve one of the two elementary triangles.
For triangle(0,0),(1,0),(1,1), the additional third-pair crossing
list is the(0,1) list translated by(−6,−1); it is disjoint from
the two lists involving(0,0). For the other triangle, translate the
(1,0) list by(5,6); again the three lists are disjoint. These two
checks exhaust possible triple coincidences up to translation.

Thus all inter-box crossings are distinct and avoid every corner
for arbitrary arrays under this map. In the particular6×6 array,
the exact computation accounts for all85 neighboring pairs and
all340 crossings. Every figure therefore has the asserted planar
general-position arrangement before visibility is selected.

## E61-8 — explicit strong witnesses, including the two opposite loops

Reuse the fully proved affine-chip map of E59-1 with the three screen
vectors in E61-6 and epsilon=1/100. At cell c let h_c(X,Y) be an
affine depth function. The solid is

    p=c+alpha(4,0)+beta(−4,−4)+gamma(0,4),
    depth=h_c(p)+epsilon(alpha+beta+gamma),  0≤alpha,beta,gamma≤1.

Every component is a valid convex3VP by the same nonzero-determinant
argument. For(i) and(ii), the observed front-before-back comparisons
have a complete acyclic ordering, explicitly saved. Give consecutive
boxes constant depths0,100,…,3500. For(iii), use constant depth
`100(2−((r+s) mod3))`. These choices realize every prescribed
comparison. Comparisons hidden by a third box are resolved explicitly
by these depth functions, rather than silently omitted.

For(iv), put o=(−5/2,25/2), let
`d=min(r,s,5−r,5−s)`, and write c=c_(r,s). Use

    d=0: h_c(p)=cross(c−o,p−o);
    d=1: h_c(p)=−10000−cross(c−o,p−o);
    d=2: h_c(p)=10000−100(r+s).

The opposite signs provide the two circulations; the constant offset
places the middle ring in front of both its neighboring layers.
All85 exact overlap polygons are checked. On each polygon, every
vertex has the same strict sign of h_a−h_b, so that sign holds
throughout. The whole solids are separated by at least9997/100
in(i–iii), and3247/100 in(iv), after allowing the3epsilon thickness.
All nonneighboring boxes have disjoint projections. Therefore the
36 solids are pairwise disjoint in each of the four models.

To check the complete image, clip each of the324 front edges against
the convex outlines of every nearer neighboring box. A half-plane
inequality along an edge is affine in its parameter, so it gives an
exact interval; intersect the six intervals and take the union over
nearer boxes. Its complement is the exact visible interval set.
For each physical front edge, this set equals the union of *all*
original native fragments assigned to it, including empty sets.
Every one of the four images matches at every edge. Rear edges are
already hidden by the same chip and need no inter-box visibility
assumption.

The strict depth gaps, nonzero single-face view signs, and complete
transverse/nonvertex crossing proof in E61-7 give stability under a
sufficiently small change of view. All four native pictures therefore
have actual strong realizations, including(iv). Common positive
scaling of depth makes the chips arbitrarily flat without changing
any of these conclusions. The witness realizes a convex standard
labeling; it does not assert that every locally permitted labeling
has a spatial realization.

No bibliography is needed for this exercise's mathematical assertions.
The general phrase "any desired overlaps" from59 remains separately
qualified; this note proves all four specific images and all of their
printed count and coordinate intermediates.
