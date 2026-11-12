# Szilassi polyhedron and exercise 26 — exact argument

Scope: main p9/file24, exercise26 p114/file129 and the complete answer26
p162/file177. Original layouts have been inspected, including all coordinates
and the three printed face cycles. The 1986 historical attribution and paper
construction are bibliographic skips; the construction below is independently
proved. Current primary TeX errata and both cumulative/public text layers contain
no change to exercise26 or answer26. Adjacent answer27 has a known replacement
and is a separate block. No new finding results from this check.

## S26-1 — incidence and coordinates

Interpret each printed triple cyclically, so its three pairs are ordered.
The fourteen triples supply all42 ordered pairs of distinct digits0–6 once.
This finite assertion is certified by the complete pair list in
`results/szilassi-exact.json`. Consequently each unordered pair occurs in exactly
two triples, and each digit occurs in six triples (six outgoing ordered pairs).

Intersect the three named planes for each triple using Cramer's rule. In the
printed triple order the determinants are

`−10, −280, 20, 66, 20, 8, −16, −10, −16, 8, 20, 66, 20, −280`.

All are nonzero. The resulting14 triples agree entry by entry with the printed
coordinates, are all distinct, and satisfy the three specified equations.
Thus there is a unique assigned point per triple; merely having three equations
would not by itself establish uniqueness or consistency. The certificate records
all plane coefficients, determinants and coordinates, with exact fractions.

## S26-2 — all seven polygon boundaries

Within facej join two vertices when their labels have two digits in common.
The resulting boundaries, up to rotation and reversal, are:

| Face | Vertex cycle |
| --- | --- |
|0|023,206,460,054,501,310|
|1|134,310,501,165,612,421|
|2|023,206,612,421,245,532|
|3|023,310,134,643,356,532|
|4|134,421,245,054,460,643|
|5|245,054,501,165,356,532|
|6|356,165,612,206,460,643|

Each list has six distinct vertices and the indicated closing edge. The three
cycles printed in the answer agree. Each adjacent face pair shares exactly its
two vertices and their edge. At a vertexijk there are exactly the three edges
for face pairsij,jk,ki, with three distinct other endpoints.

Planarity follows from S26-1. To establish that these are simple, nondegenerate
hexagons, project each face by deleting a coordinate whose plane coefficient is
nonzero. This projection is one-to-one on that plane. Every consecutive triple
has nonzero signed area. All nine nonadjacent edge pairs in each hexagon are
disjoint, as certified by exact2D orientation tests. For segmentsab andcd the
test rejects a proper crossing when the two products of endpoint orientations
are both negative, and rejects boundary contacts when an endpoint is collinear
and lies between the other segment's endpoints. This accounts for crossings,
overlaps and nonadjacent touching, not just vertex containment. Consecutive edges
share only their prescribed endpoint because their signed area is nonzero.

## S26-3 — exclude all unwanted spatial intersections

Checking simple faces separately is insufficient. Two distinct face planes
intersect in the infinite line through their common edge. Parameterize this
line as A+t(B−A), whereA,B are that edge's listed endpoints. Its intersection
with either closed polygon is a finite union of closed intervals.

Every finite interval endpoint lies on a polygon edge. Evaluating the other
plane's linear equation at an edge's endpoints finds these boundary points
exactly: a zero gives an endpoint on the line; opposite signs give the unique
crossing by linear interpolation; two zeros give the entire collinear edge.
After sorting these parameters, membership is constant on each intervening
open interval, since no polygon boundary is crossed there. Exact midpoint
point-in-polygon testing determines that membership; a horizontal ray counts
crossings with a half-open endpoint convention, after an explicit boundary
test. The line is outside the bounded polygon before its first and after its
last boundary parameter. This procedure therefore gives the complete line
intersection, including isolated boundary points. It is not a sample-based
claim about the geometry.

The complete interval pairs for all21 face pairs are in the certificate. In
every case their intersection is exactly[0,1]. Some polygons meet the line
beyond the common edge, so this check has real content. For example, faces1
and5 have line intersections[0,1] and[−7/5,−5/13]∪[0,1]; faces3 and4 have
[0,11/10] and[−1/10,1]. In both cases the common part is exactly the edge.
Thus no faces cross or meet at any unintended point.

## S26-4 — polyhedral object and counts

The seven simple polygonal disks meet exactly along their prescribed edges.
Each edge belongs to two faces, and the link at each vertex is the triangle
formed by its three incident faces and edges. The union is therefore a closed
embedded polygonal surface with no local singularity. A consistent orientation
of all face cycles, also recorded, traverses every shared edge in opposite
directions. The resulting compact embedded closed surface bounds the ordinary
polyhedral solid (equivalently, take the bounded side of this surface).

There are14 distinct vertices,21 distinct edges (one per unordered face pair)
and7 faces. Every vertex has exactly three incident edges and three faces;
every face is adjacent to all six others. These prove all numerical and
adjacency claims in Fig.101(b), as well as the existence requested in26.
The count14−21+7=0 is a consequence, not the evidence for the construction.

## Certificate scope and remaining main-page claims

`check_szilassi_exact.py` was run once at nice15. Its integer/Fraction operations
cover14 linear systems,7 hexagons and21 face pairs. No possible realizations or
geometric samples were searched. The determinant expression was subsequently
simplified by cancelling two identical sign factors; this is an algebraically
identical expression and the saved certificate is unchanged.

The usual cube has the three incident coordinate faces at each vertex; a
tetrahedron has three of its four faces there. An octahedron has four triangular
faces at each vertex, and a square pyramid has four at its apex. These establish
the named qualifying and nonqualifying introductory examples.

The small unnamed pictograms, hidden-face count of the stylized sphinx
(68,102,38), and exact cut/interlocking geometry and counts of the clasp
(20,30,14) remain explicit partials until their complete constructions are
available. The definitions permit faces with holes; Euler arithmetic is not a
substitute for reconstructing them and does not refute the sphinx's counts.
Fig.101(d) is a separate histoscape construction, to be checked with27–30.
The preceding competition/history paragraph and subjective perception comments
are explicitly skipped nonmathematical material. This proof does not mark
the whole of file24 or177 complete.
