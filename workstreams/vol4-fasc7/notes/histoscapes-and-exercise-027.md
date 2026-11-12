# Histoscapes, Fig.101(d), and exercise27

Original sources: main p9/file24, exercise27 p115/file130, answer27 p162/file177.
All three originals have been viewed; the small p9 pictograms were also rendered
at higher resolution. The printed example matrix is `[[4,3],[1,2]]`; its matrix
row index is the Cartesian x coordinate, as in the definition, not a page's
vertical drawing coordinate.

The public11 September2025 replacement of answer27 changes both local forbidden
patterns, the fourth valid case, the count4150→5830 and the leading asymptotic
coefficient1/3→2/3. The complete replacement has been read in the current primary
TeX and public/cumulative layers. These are known corrections, not findings.
The arguments below prove the corrected text and account for each old step.

## H27-1 — cubies and local completeness

Six face neighbors differ by±1 in one coordinate. Twelve edge-diagonal
neighbors choose two coordinates and their signs, giving3·4; eight corner
neighbors differ by±1 in all three coordinates. The definition includes shared
boundary points, and the more distant diagonal neighbors are classified by the
dimension of their common part, not counted again as face neighbors.

A histoscape is a finite union of the indicated closed cubies. Boundary faces
come from exposed unit squares, merging connected coplanar squares with the
same outward normal. At a point with integer x,y, the four neighboring column
heights completely determine the local boundary. At heightz>0, a neighboring
octant below the point is occupied iff its column heighth≥z, and an octant above
iffh>z. Atz=0 every lower octant is empty. Heights outside the matrix are zero.

For a fully explicit local test intersect the occupied octants with a small
octahedron centered at the point. Its six vertices are the signed coordinate
axis rays. Each triangular facet corresponds to one octant. A boundary edge
of this spherical link is present exactly when the two octants on opposite
sides of the corresponding coordinate plane have different occupancy. Thus
the boundary link is a graph on the six signed rays, with edges only between
different axes. A boundary point is locally a surface exactly when this graph
is one simple cycle. An axis ray is a geometric crease when its two adjacent
link edges lie in different coordinate planes; the other degree-two rays are
just subdivisions of a flat face. After removing those subdivisions, a smooth
face point has no corners, an interior edge point has two opposite corners,
and a trihedral vertex has three corners. Four or six corners fail3VP. A link
vertex of degreefour signifies four faces on the same spatial edge.

This is a complete incidence test, rather than a test of the degree sum alone.
The union of selected octant triangles lies on a sphere; a single simple link
cycle bounds a disk on either side, so the original boundary is locally a disk.
The graph gives all its plane changes. Empty links are exterior/interior points.

It suffices to test heights zero and the distinct neighboring column heights.
Between successive heights the occupied octants do not change, and their
vertical-ray behavior is already included just above/below the endpoints.
Points inside a cell or on just one vertical grid plane lie in an ordinary
face or an extrusion of a two-column step; they introduce no further vertex
pattern. At the outer boundary there are at most two adjacent nonzero columns,
so the same step argument gives only ordinary corners. Consequently all
possible failures for a2×2 matrix occur on its central vertical grid line.

The all-zero matrix is counted: its empty boundary vacuously satisfies the
definition. This is also the convention of the printed corrected count.

## H27-2 — every forbidden and permitted order type

Place a maximum at the upper left, writing the matrix `[[a,b],[c,d]]`, and
reflect across its diagonal when necessary to arrangeb≥c. This symmetry acts
on the solid by an isometry, so it preserves3VP.

Ifd>b, then a,d are the only occupied diagonal sectors above heightb and below
the next higher height. Their cubies touch along the central vertical edge,
which has four incident faces. This fails3VP even ifb=0. The answer's identity
matrix is the basic example. At(1,1,1) it has the four horizontal edge rays and
the downward vertical ray, hence five edges; its downward edge has four faces.

Assumed≤b. Ifa>b=c>d, then atz=b the occupied sectors change from the three
sectorsa,b,c below to the single sectora above. The local link has all six
coordinate rays as corners, yielding six incident faces/edges. Ifa>b=d>c,
the change is froma,b,d below toa above; its link has four corners. These are
exactly the two milder forbidden patterns in the corrected answer.

All remaining arrangements, up to symmetry, are the four printed families:

| Case | Heights | Local justification |
| --- | --- | --- |
|1|a=b=c≥d|At the lower level, four sectors become three; at the upper level three become zero. Each nonflat event is an ordinary concave or convex corner. All four equal is one rectangular prism.|
|2|a=b>max(c,d)|The two highest sectors are adjacent. At each lower distinct level four become three, or three become those two adjacent sectors. If the lower levels coincide the event is flat; at the upper level two adjacent sectors disappear together, giving a regular straight edge.|
|3|a>b=c=d|At the lower level four sectors become one, and at the upper level that one disappears. Both nonflat events are ordinary corners.|
|4|a>b>max(c,d)|The unique maximum and unique second-highest sectors are adjacent. Lower distinct events go four→three→two adjacent sectors, or directly four→two if tied; the upper events go two adjacent→one→zero. Every nonflat event is an ordinary corner.|

At levelzero replace the four sectors below by zero. The positive footprint in
each valid family is one sector, two adjacent sectors, three sectors, or all
four; its floor is therefore an ordinary corner, edge, or flat face. This
covers all zero-height boundaries rather than assuming every column positive.
The local link construction in H27-1 directly justifies each transition in
the table, including the concave three-sector corners.

To see the list is exhaustive, split first by the multiplicity of the maximum.
Three/four maxima give case1. Two adjacent maxima give case2, unless a third
ties (case1); two diagonal maxima have the forbidden diagonal edge. With a
unique maximum, three equal smaller heights give case3. A unique runner-up
adjacent to the maximum gives case4; a diagonal runner-up gives the forbidden
edge. Two tied runner-ups either occupy its two neighbors (the six-corner
pattern) or a neighbor and opposite corner (the four-corner pattern).

As a finite exact certificate of these symbolic cases, all75 weak order types
of four numbers were checked using the octahedral-link test, once with minimum
zero and once with positive minimum. Strictly increasing changes of the chosen
levels do not change any octant pattern; these150 cases therefore cover every
nonnegative integer matrix, not a finite-height sample. Every boundary grid
point is included, not only the central line. `results/histoscape-local.json`
records all order types and every failed point/link. The case classification
and local incidence test are independent constructions and agree in all cases.

## H27-3 — corrected exact count and asymptotic

Choose heights from0,...,B−1. The case counts, without overlap, are:

* Case1: B all-equal matrices; or choose two levels and the low corner, giving
  B+4·choose(B,2).
* Case2: choose one of four edges for the adjacent equal maxima. If the two
  lower values tie, this gives4·choose(B,2); if distinct, their two assignments
  give8·choose(B,3).
* Case3: choose two levels and the unique high corner, giving4·choose(B,2).
* Case4: choose the high corner and adjacent second-high corner in4·2=8 ways.
  The lower values either tie, giving8·choose(B,3), or have two assignments
  of distinct values, giving16·choose(B,4).

The sum is B+12·choose(B,2)+16·choose(B,3)+16·choose(B,4). ForB=10 the
individual case counts are190,1140,180,4320, totaling5830. The fourth-degree
term is16B^4/24=(2/3)B^4 and every other contribution isO(B^3). The rank
certificate independently records coefficients1,12,16,16. B=1 gives the
single empty matrix, and B=0 gives none. No10000-matrix brute force or8×8
enumeration was performed.

## H27-4 — Fig.101(d) and the two small pictograms

For the actual printed matrix `[[4,3],[1,2]]`, the center line has a trihedral
vertex at each of levels1,2,3,4. Each of the four outer corner lines has its
bottom and top vertex, contributing8. Each of the four outer side midlines has
two distinct heights and contributes2 more, hence another8. The total is20.
There are no additional vertices by H27-1. Trivalence gives exactly30 edges:
every finite straight edge has two distinct endpoints and contributes twice
to the sum3·20.

There are four horizontal top faces and one bottom face. There are four outer
vertical faces. Internally, the two exposed strips in planex=1 share an edge
over2≤z≤3, forming one connected planar face; the two exposed strips in
planey=1 are disjoint and have opposite normals, forming two faces. Thus there
are5+4+1+2=12 faces. The solid belongs to valid case4. An independent explicit
boundary construction in the certificate lists every one of its20 vertices,
30 long edges, and all12 face boundary polygons. It starts with exposed unit
squares, merges exactly coplanar connected squares, removes internal edges,
and contracts straight degree-two subdivisions. This verifies the drawing's
numbers without presuming an Euler formula.

The qualifying small pictogram is an L of three unit columns, represented up
to an isometry by `[[1,1],[0,1]]`, and is case1. In the nonqualifying pictogram
one end of that L is raised to heighttwo, giving `[[2,1],[0,1]]`. Its central
height-one vertex is the four-corner patterna>b=d>c. These identifications
use the enlarged original outline, including the low column behind the tall
one; treating it as only two adjacent columns would miss that vertex.

## Certificate limitations

The small fixed certificate was run once at nice15. The general criterion and
case count are proved above; explicit stored link graphs permit review of all
finite incidence checks. Fig.101(a)'s sphinx and Fig.101(c)'s interlocked
tetrahedral cuts are still partial because their full hidden constructions
are not supplied by the histoscape argument. Algorithms and counts in28–30
are separate work; the certificate does not close those answers or file130.
