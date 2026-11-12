# Exercise64: both complete drawings have explicit strong realizations

The question's full picture p119/file134 and the answer's two-bar
hint p173/file188 were displayed at high resolution. All23 source
paths of the first picture and all11 paths of the second were
extracted from the original SVG. These are not illustrations drawn
by the checker. The canonical normalization has maximum squared
source residual below1/10000 pt² in each picture; separate positive
screen scales preserve the intended projection and junction types.

Evidence:

* `check_twisted_bars64.py` constructs the explicit finite union,
  certifies its entire boundary, and tests every physical edge's
  visible intervals against every original line segment.
* `results/twisted-bars64-{hint,full}-{native,union,visibility}.json`
  contain all points, planes, cells, faces, incidences, and intervals.
* `check_twisted_bars64_certificates.py` and
  `results/twisted-bars64-small-certificates.json` add the strict
  common-interior witness, each coplanar face component, all T depth
  gaps, and both exact copies of the right half of26. They reuse
  the saved boundary/visibility data, without rerunning geometry.

There was one small implementation correction before any full-model
result: a supporting plane can have two disjoint exposed face
components, so it must not be counted as a single face. The final
certificate separates every such component and verifies one boundary
cycle per component. No large search or geometric fitting search
was performed; the solids below are explicit.

## E64-1 — exact drawings and the two copies of26

In canonical screen coordinates the main picture has38 junctions
and53 lines:8 V,16 W,8 Y,and6 T. The smaller answer hint has
18 junctions and25 lines:4 V,8 W,4 Y,and2 T. Every path is split
at all exact intersections, so the T points on a longer source
stroke are included. All resultant degrees and cyclic orders are
saved, not inferred merely from the counts.

The seven source paths47–53 making up the right end of26 are
exactly the main64 paths3089,3091,3093,3095,3097,3099,3101 under
the canonical map `(x,y)→(x−94,2y)` to26's saved right-end grid.
The half-turn `(x,y)→(108−x,16−y)` maps each of those seven
paths to the immediately following left-end path of64. This proves
the question's “twice” statement for every endpoint and segment,
including the three short connectors. The long horizontal joining
strokes are separately included in the full network comparison.

Boundary arrows and the complete Table1 relations propagate to a
single standard labeling of each picture. For the hint the final
counts are6 arrows in each direction,10 pluses,and3 minuses; for
the main picture they are12,12,20,and9. The saved propagation
trace records each removed value; every final singleton tuple is
present in its local table. Thus the singleton assignment exists
and every standard solution equals it. This fact alone would not
prove physical realizability; E64-2–5 provide that separately.

## E64-2 — the explicit family of solids

Use coordinates(x,y,z), viewing from negative z, and abbreviate

    u=y+z,       v=y−z.

For the hint take n=2,L=84; for the main picture take n=4,L=92.
For i=0,…,n−1 define c_i=4i+2,U_i=6n−2i,V_i=−2−2i and the
closed convex solid

    B_i={c_i≤u≤U_i, V_i≤v≤c_i,
         c_i≤x+z, x−z≤L+c_i}.

The required object is the union X of these n solids. It is a
single solid, with overlapping interiors; treating the apparent
bars as mutually disjoint ordinary prisms would give the wrong
concave junctions.

For any choices u∈{c_i,U_i},v∈{V_i,c_i}, its two endpoint
vertices are

    y=(u+v)/2, z=(u−v)/2,
    x=c_i−z or x=L+c_i+z.

Since u≥c_i≥v, z≥0. The x interval has length L+2z>0;
both cross-section intervals have positive length. Consequently
these are eight distinct vertices of a full-dimensional convex
hexahedron, with exactly the six displayed supporting planes.
Their complete polygons are obtained by holding one of the
three binary choices fixed. Planarity and all six half-space
inequalities are checked exactly at every vertex.

The numbers are chosen to produce the apparent conflicting ends.
The front ridge of B_i has y=c_i,z=0 and runs from x=c_i to
x=L+c_i. Its two front planes are z=c_i−y and z=y−c_i.
Adjacent ridges intersect in the concave valley y=4i+4,z=2.
The left end plane is x+z=c_i, whereas the right is x−z=L+c_i.
Their intersections with the two ridge planes yield exactly the
two opposite diagonal slopes of each drawn end polygon.

For example, on the right of the main picture, the exposed cap
of ridge i has the four projected corners

    (96+7i,i), (94+4i,2+4i),
    (96+4i,4+4i), (98+7i,2+i),

with depths2+3i,0,2,4+3i respectively. The remainder of its
cap, when present, is concealed by the next solid. On the left,
the corresponding visible corners are

    (4i,4i), (2+4i,2+4i),
    (−9+7i,13+i), (−11+7i,11+i),

with depths2,0,11−3i,13−3i. The previous solid conceals the
other part there. These formulas explain the different apparent
lengths. The exhaustive boundary and ray calculation below proves
that no additional visible piece has been omitted.

## E64-3 — closed body, complete boundary, and trihedral vertices

The point

    P=(L/2+2n,2n,2n)

has u=4n,v=0 and lies strictly inside every B_i. In particular
max c_i=4n−2<4n<min U_i=4n+2 and max V_i=−2<0<min c_i=2;
both x inequalities have a positive margin as well. Every margin
is saved individually. Each B_i is bounded and convex and contains
P in its interior. In any direction from P its intersection is a
closed interval ending at a positive continuous radial function.
The union's radial function is the maximum of finitely many such
continuous functions. Hence X is homeomorphic to a closed ball,
and its boundary is an embedded closed sphere, not a collection
of surfaces that merely touch along edges or at vertices.

To compute that boundary exactly, start with every face polygon
of every B_i and split it by all the other supporting planes.
Each resulting full-dimensional planar cell has a constant sign
with respect to each plane. A cell is hidden inside the union
precisely if its relative-interior sample is strictly inside another
B_k. Otherwise it lies on the union boundary. No other supporting
plane is coplanar with the current face, so an interior sample
cannot be an unresolved equality case. The exact sample signs
and the finite splitting construction establish the classification
for whole cells, not just for the sample points.

All cell edges are subdivided at every collinear cell vertex before
incidences are counted. An edge between two cells of the same
plane is removed; an edge belonging to two distinct boundary planes
is retained. Consecutive collinear pieces with the same two plane
owners are joined. This yields the physical edges and vertices.
The follow-up certificate joins coplanar cells across positive-length
shared edges, and checks that each component has exactly one simple
boundary cycle matching its saved physical face. Thus disconnected
patches on the same plane are separate faces, and no interior hole
is silently counted as another face.

The complete results are:

| Picture | Vertices | Edges | Faces | Convex boundary cells |
|---|---:|---:|---:|---:|
| answer hint |24|36|14|38|
| main64 |56|84|30|198|

Each physical vertex has exactly three incident physical edges
and three supporting face planes. The determinant of their normals
is always+2 or−2, so the planes are independent. Each edge belongs
to exactly two faces. Together with the ball argument and complete
cell decomposition, this proves that X is a valid3VP. The Euler
equalities24−36+14=2 and56−84+30=2 are consistency checks, not
substitutes for the manifold or planarity arguments.

All constructions are finite. A face is cut by at most6n−1
specified planes; the largest actual planar subdivision has only
28 cells. Exact rational arithmetic is used throughout. The
certificate is a finite verification of these two explicit objects,
not a claim of an efficient general realization algorithm.

## E64-4 — every visible edge and every original source line

For each physical edge, split its projected parameter interval at
every intersection with a projected physical edge. On each resulting
open interval, every ray/face incidence has a constant status.
For a midpoint p, intersect the ray p+t(0,0,−1),t>0, with each
convex boundary cell. A cell hides p exactly when the intersection
parameter is positive and all of its polygon half-plane tests
are satisfied. No face is parallel to this ray: every supporting
plane normal has z component+1 or−1.

This tests every cell and every edge interval. Joining adjacent
visible pieces gives the full exact visible-edge projection. Removing
degree-two collinear subdivisions in that projection yields exactly
the source network:18 junctions/25 lines for the hint and38/53
for the main picture. Equality is tested as a complete set of
endpoint pairs, so both extra and missing segments would fail it.
Every original path endpoint was already matched to the canonical
grid in E64-1. Thus the comparison includes every printed stroke,
not just a selected silhouette or some suggestive front faces.

The locally consistent standard labeling from E64-1 is necessarily
the one produced by this strong witness: boundary contours have
the standard foreground orientation, and every physical3VP labeling
obeys Table1. Since propagation proves uniqueness, all its plus,
minus,and arrow labels agree. This avoids assuming that an unlabeled
wireframe automatically has the intended crease signs.

## E64-5 — generic view and the answer's strong conclusion

Every physical edge has a nonzero projection. Every non-T source
junction is exactly one visible physical vertex with the expected
incident visible edges. Each of the two hint T points and six main
T points is a transverse crossing of exactly two relevant physical
edges, with no physical vertex at the crossing. Their two depths
differ by exactly2 in all eight cases; the exact depths, edge names,
and nonzero crossing determinants are saved individually.

There is therefore no grazing face, collapsed edge, vertex-edge
coincidence at a visible T, or equal-depth contact causing one of
the pictured junctions. The other boundary/visibility decisions are
strict on the finite subdivision cells and intervals. Hidden
coincidences have positive depth separation from the visible part.
These conditions persist under a sufficiently small change of
viewpoint; the apparent T bars remain one physical edge and their
crossings remain transverse. Thus the matching projection is in
general position and is a **strong** realization, not only a weak
network embedding.

The answer's proposed two-bar starting example and the full
four-bar question are both explicitly realized. No impossibility
claim or new erratum arises from64. This construction is independent
of the unresolved interpretation in63 and does not assume that
63's necessary linear system is sufficient in general.
