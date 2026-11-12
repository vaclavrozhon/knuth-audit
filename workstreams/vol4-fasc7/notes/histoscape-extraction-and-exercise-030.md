# Histoscape boundary extraction — exercise30

Scope: exercise30 p115/file130; answer30 p163–164/files178–179, all four
marking stages, polygon walks, and every vertex/polygon of the ring example.
Both original answer pages have been viewed. The12 September2025 primary
replacement changes the array bound to(2m+1)×(2n+1)×(2t−1), restates the three
marking passes symmetrically, and calls the example a square doughnut. These
known changes are not findings. The abbreviated fourth-pass condition in the
replacement is treated explicitly below, with its literal wording left partial.

## X30-1 — coordinate representation and bounds

Assumem,n≥1, integer heights0≤aij<t witht≥1, and a3VP histoscape as required
by the exercise. Represent an original lattice vertex by its doubled integer
coordinates. A unit cell center has three odd coordinates; a unit face center
has two; a unit edge center has one; a vertex has none. An object's midpoint
with an adjacent parallel object has the intermediate parity. This follows
coordinate by coordinate from taking means of consecutive doubled integers.
The cited representation in Volume4B answer145 p455/file475 was read in the
original; it agrees exactly (`images/vol4b-p455.png`). No unrelated results
from that exercise are needed.

The highest occupied unit cell has originalz≤t−2, so its doubled center is
at most2t−3 and its top boundary at most2t−2. This proves the corrected
inclusive range0≤k≤2t−2 and dimension2t−1. Thex/y ranges are0≤i≤2m and
0≤j≤2n. Outside reads are zero, expressing absent cells. Every mark written
by a pass lies within those bounds: it is midway from a present cell of odd
coordinate to the neighboring position two units away. Even a boundary
face at coordinatezero has only its other, odd coordinates stepped in the
next pass. Empty inputt=1 produces no marks or polygons.

## X30-2 — four marking stages, including internal faces

First mark exactly the occupied cell centers(2i+1,2j+1,2k+1) for0≤k<aij.
Each such mark is unique and agrees with the definition of the union.

Second, for each marked cell and each coordinate direction, mark the halfway
face center when the cell two units away is absent. A unit square is on the
boundary exactly when one of its two adjacent cells is occupied. Therefore
this marks all and only exposed unit squares. Here “visible” means exposed
on the solid's boundary, not visibility from the camera in answer29.

Third, for each marked face and each of its two odd coordinates, compare the
face two units away in its own plane. Mark the intervening unit edge when
that coplanar face is absent. Within a3VP, two adjoining exposed coplanar
unit squares have the same outward normal: opposite normals along their
common side would give a four-face, nonmanifold spatial edge. Hence such
adjacent squares belong to the same planar face, and their internal seam
must be suppressed. The edges left by this pass are exactly the boundaries
of connected planar faces, including hole boundaries. Each geometric unit
edge is found from its incident faces; duplicate writes simply set1 again.

Fourth, for each **marked** unit edge, compare its collinear edge neighbors
two units away in its one odd coordinate. An absent neighbor marks the
endpoint halfway between. Within a trihedral orthogonal surface, a geometric
vertex has one edge in each coordinate direction. In particular there are
no two collinear incident edges continuing through such a vertex. Along the
interior of a long edge, by contrast, the adjacent unit edge is present and
the intermediate lattice point must not be marked. Thus the fourth pass
marks exactly all geometric vertices. This uses the3VP input assumption;
the procedure is not asserted to repair singular histoscapes.

The qualification **marked** is explicit in the original fourth step and
in every preceding pass. The replacement says to do “those same three
operations” at parity sumone, but does not repeat b_ijk=1. The proved
algorithm retains that activation condition. If its new quantifier were
read literally as ranging over unmarked edge positions too, even an empty
histoscape would acquire spurious vertex marks. The natural inherited-guard
interpretation is plausible, so this wording is a separate partial
interpretation, without a new finding card. It is not silently proved under
an absent condition.

## X30-3 — polygon walks, hole components and termination

At a vertex exactly three faces meet, with distinct constant coordinatesi,j,k.
Fix one orientation, say constanti. The boundary graph of that planar face
uses thej/k directions, with exactly one outgoing edge of each direction at
every vertex. Each component is a finite orthogonal polygon; a hole is another
component, to be output separately. Different constanti boundary components
cannot share a vertex, since a3VP vertex has only one face in this orientation.

Starting at an unvisited vertex, the printedj-step follows the positivej
direction if the intervening unit edge is marked, otherwise the negativej
direction. Exactly one exists. The successive increments by±2 pass only
unmarked collinear interior points until the next geometric vertex; the
finite long edge guarantees that vertex is reached within the array. The
followingk-step does the same in the other direction. A mark2 records a
visited vertex but is still nonzero when terminating an edge scan.

After entering a vertex along one axis, leaving along the other follows the
polygon without backtracking. A finite2-regular boundary component is one
cycle. Its first repeated vertex must be the start: revisiting another
vertex first would require three distinct incidences there. Consecutive
edges alternatej/k, so the cycle length is even and the return occurs after
a completej/k pair. Thus the outer while condition stops exactly after one
whole polygon, with no missing or duplicated vertex. Repeating from all
remaining mark1 vertices outputs each component once, including holes.
Every vertex is visited in this orientation and ends with mark2, as printed.

For the other two orientations perform the analogous scan with fresh vertex
visitation flags (or reset the even/even/even marks2→1). The edge/face marks
are unchanged. This is the required initialization when repeating the
described single-orientation procedure; otherwise its consumed visitation
flags would suppress subsequent scans. No additional geometric assumption
is introduced by using one visited flag per orientation.

These walks output the boundary polygons requested in the answer. A geometric
face with holes consists of several polygons, so polygon counts and connected
face counts must be distinguished. If face grouping is wanted, merge the
coplanar connected exposed squares, whose boundary components are exactly
these walks. Their plane and connected component determine the grouping.

## X30-4 — cost and independent finite verification

LetA=(2m+1)(2n+1)(2t−1). Array initialization and three full marking scans
takeO(A) time and space; filling occupied cells is at mostmn(t−1)=O(A).
In all three polygon orientations each marked unit boundary segment is
traversed at most twice, once for each incident face. Each vertex is output
three times, once per incident face. Hence polygon tracing is alsoO(A),
including finding starts and resetting flags. The bounds assume unit-cost
arithmetic on coordinate-sized integers; no runtime census is inferred.
All loops are finite, and each edge scan has a known endpoint, proving
termination independently of a successful run.

`check_histoscape_extraction.py` follows the corrected parity marking and
the alternating polygon walk. Its result is compared with the separate
exposed-square/component construction from H27-4, which does not use parity
passes. One nice15 run covers only the printed ring, the fixed replacement
8×8 witness, and the empty histoscape. It does not repeat the75-order-type
certificate or enumerate any8×8 space. For the replacement witness the new
walk agrees with every previously saved vertex and all104 boundary polygons,
including the two extra hole boundaries of its102 connected faces.

## X30-5 — every printed ring entry

The3×3 matrix of ones with centerzero is a unit-height square frame. Its
planar footprint has four outer and four inner corners; each has a bottom
and top vertex, giving16. Each boundary corner has its vertical edge and
two horizontal edges, so the graph is trihedral and has24 edges. There
are four outer and four inner vertical rectangles and two horizontal annuli:
ten connected faces and12 boundary polygons.

The full printed vertex list is

`000,001,030,031,110,111,120,121,210,211,220,221,300,301,330,331`.

These are exactly the two levels of the eight footprint corners. All four
printed constant-i rectangles, four constant-j rectangles, and four constant-k
loops were transcribed individually and compared up to cyclic start/reversal
in `results/histoscape-extraction.json`. They agree with the actual unit-square
boundary. The two constant-k pairs are an outer square and its hole, not four
independent horizontal faces. This establishes every displayed intermediate
polygon as well as the total, and geometrically justifies the square-doughnut
description. It does not address the later whirlpool exercises on this page.
