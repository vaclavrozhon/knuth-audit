# Reutersvard32, the strong witness59, and the full count60

Originals displayed: p16/file31, question p119/file134, answer p171/file186.
The correction applicable to59 is the15September2025 erratum:
the side view is replaced by an80%-squashed illustration, and the
historical assertion about the star of David is reworded. The primary
TeX and both printed replacement diagrams on the displayed short
errata PDF p13 have been inspected. These are known changes, not
findings. The precise replacement side-view parameters are separate
from the explicit spatial construction proved below.

## R32-1 — complete original drawing

`check_reutersvard32_60.py` maps every path18–214 of source31 to an
exact triangular grid. The fitted independent x/y units and every
point residual are saved; every source occurrence is within.01pt.
This accounts also for the doubled strokes and their tiny endpoint
rounding differences, not merely a selected outline.

Exact subdivision and local angular tests give72 junctions:
18V,24W,9Y,21T; there are99 physical lines. The outside walk has
33 lines. Every ordered relation from Table1 is saved in
`results/reutersvard32-60.json`. The center locations of the nine
apparent boxes, in the same grid, are

    c0=(4,20), c1=(9,27), c2=(14,34), c3=(19,41),
    c4=(20,30), c5=(21,19), c6=(22,8), c7=(16,12), c8=(10,16).

Each apparent box has the same projected cube outline, whose offsets
from c_i are `(0,−8),(4,−4),(4,4),(0,8),(−4,4),(−4,−4)`.
Thus all nine apparent boxes, not just their count, are identified.

## E59-1 — explicit solid for each chip

Put o=(15,23), epsilon=1/100, and

    h_i(p)=−cross(c_i−o,p−o),
    a=(−4,−4), b=(4,−4), c=(0,8).

The ith solid is the affine image of the unit cube0≤alpha,beta,gamma≤1:

    p=c_i+alpha a+beta b+gamma c,
    z=h_i(p)+epsilon(alpha+beta+gamma).

Depth z increases away from the viewer. Since a+b+c=0 and a,b
are independent, the three spatial edge vectors have independent
columns: their sum is `(0,0,3epsilon)`, independent of their two
screen directions. The map is invertible. Each chip is therefore a
convex8-vertex12-edge6-face polyhedron, every vertex has degree3,
all six quadrilateral faces are planar, and face intersections are
exactly those of the cube. This establishes solid validity without
depending on a sampled rendering.

For a single chip the visible part has the ordinary cube projection:
the three coordinate-zero faces are front faces, the three
coordinate-one faces are back faces. Adding the same affine h_i
to every depth does not change the order of points on one viewing
ray. Thus the center Y and its three+creases, the six silhouette
vertices, and the9 front edges have exactly the required screen
positions. The opposite center is hidden, at depth3epsilon behind
the front center. Coincidence of those two projected centers is
irrelevant to stability of the visible graph: the rear one is
strictly occluded.

Multiplying every depth by any common positive rho preserves this
projection, all intersections and all depth orders. Taking rho small
makes all chips arbitrarily close to flat hexagonal tiles in parallel
image coordinates, with the small tilts prescribed by h_i. Thus the
construction supplies the flattening mechanism, with exact geometry,
instead of merely asserting that some thin solids should work.

## E59-2 — all inter-chip intersections excluded

The projection outlines are convex. Exact half-plane clipping of
all36 pairs yields precisely12 nonempty overlap polygons. At each
overlap vertex, h_i−h_j has one sign and absolute value among
34,54,70,90. An affine function has its extrema at polygon vertices,
so the sign is uniform on the entire overlap. The additional cube
depth term is between0 and3epsilon. Consequently the separation
between any two chips on every shared viewing ray is at least

    34−3epsilon=3397/100>0.

Pairs with disjoint projections cannot intersect in space. Hence
all nine closed solids are mutually disjoint. Their finite union
has72 spatial vertices,108 spatial edges and54 faces, each component
being a valid3VP and every vertex still of degree3.

For the twelve overlapping pairs, the nearer box is:

| Pair | Nearer box |
| --- | --- |
|0,1|1|
|0,8|0|
|1,2|2|
|1,8|1|
|2,3|3|
|2,4|4|
|3,4|4|
|4,5|5|
|5,6|6|
|5,7|7|
|6,7|7|
|7,8|8|

In particular the outer chain contains a cyclic order of overlapping
boxes. There is no contradiction: different comparisons occur over
different screen regions, and their affine heights vary with position.
The explicit solids prove this point directly.

## E59-3 — every visible line and general position

`check_reutersvard59_spatial.py` cuts every one of108 physical edges
at every projected edge crossing. At each open subinterval it uses
the exact ray/face inequalities for all54 planar convex faces. Those
inequalities cannot change inside the subinterval: their boundaries
are projected face edges, all of whose crossings were used as cuts.
The procedure therefore determines each complete visible interval,
not a finite sample conjecture. After merging straight subdivisions,
the result equals every one of the99 original grid lines, in both
directions, with exactly the72 original junction points.

The result `reutersvard59-spatial.json` contains each interval and
every overlap depth separation. It also records a stability check
for every source junction. Each non-T junction is exactly one visible
physical vertex, with only its incident front edges present there.
Each of the21 T junctions is a transverse crossing of exactly two
front-surface edge interiors, and no physical front vertex is there.
The nearer/farther order has the strict margin of E59-2. Each single
chip has all face/view scalar products nonzero, so its own visible
faces persist under a small rotation. Together these strict finite
conditions preserve all visible incidences and their ordering under
sufficiently small perturbations. This is the qualitative general
position required for strong realizability, and is not inferred from
the insufficient answer40 condition.

Thus the actual native32 picture is strongly realizable. This proves
the mainp16 claim and the existence task in59 for one standard
labeling. All solid edges here are convex. The other seven standard
labelings in60, which contain one or more concave center edges, are
not certified by this convex witness.

## E60-1 — three inner choices, their locations and independence

The central region's complete boundary is

    v23 v24 v25 v29 v39 v38 v47 v43 v42 v37 v27 v28.

Its three V junctions are v28=(14,20),v29=(14,26),v43=(17,23).
The other nine are W/T. With the standard outside arrows, table
propagation fixes every inner variable except the three physical
lines

    v23–v28: {−,<};  v29–v39: {−,>};  v42–v43: {−,<}.

The arrows here are global increasing-name directions. At each of
the three named V junctions the variable is its first branch, with
choices−or outgoing O; the second branch is incoming I. The two
permitted Table1 rows are therefore exactly−I and OI. Translating
the outward arrow to each original oriented line gives the printed
choice−or<. The saved ordered relations check the direction at
both physical endpoints, including the globally reversed29–39 line.

The opposite endpoint is a T stem whose label is unrestricted after
its two bar arrows have been fixed. No other relation uses the free
line. Thus the three choices are independent. More explicitly, the
certificate's fixed-point rows show every remaining local relation
equals the Cartesian product of its surviving domains. Selecting
any one of the2^3 choices therefore satisfies every relation; all
other variables are singletons. The saved propagation steps prove
that every solution is in those domains. This proves both directions
of the exact count8 without enumerating all4^99 labelings.

## E60-2 — each printed boundary factor

The33-edge outside cycle has a four-state transfer matrix at every
junction. The certificate multiplies all33 matrices and, for every
local pair, multiplies the complementary cyclic product to determine
whether that pair is globally supported. Every surviving pair fixes
every inner port to the same value. These values agree when a
physical port occurs more than once. Thus no hidden compatibility
assumption about repeated port names is used.

Fixing that common port vector splits all uncertain outer variables
into nine independent components. Six have two choices and three
have three. In the variable order shown, the complete component
tables are:

| Variables | Allowed words |
| --- | --- |
|00–01,00–02,01–04,04–06|`--<<`, `<>--`, `<><<`|
|07–14,14–19|`--`, `<<`|
|08–09,08–15|`--`, `<>`|
|20–31,31–33|`--`, `<<`|
|21–22,21–35|`--`, `<>`|
|34–50,50–64,61–63,63–64|`-->>`, `<<--`, `<<>>`|
|45–46,45–58,58–70,70–71|`-->>`, `<>--`, `<>>>`|
|62–66,66–67|`--`, `>>`|
|65–68,68–69|`--`, `>>`|

Every two-digit endpoint has prefix v. The three larger components
are exactly the three outer corners of the triangular arrangement;
the six smaller ones belong to its six other boxes. These tables
come from the complete surviving W/V/T rows, all saved. Their
small exhaustive checks cover at most four uncertain variables per
component and are coupled with the explicit separation certificate.
No relation couples two components except a full Cartesian relation,
which imposes no further restriction.

Consequently the boundary count is `2^6 3^3=64·27=1728`. Every
boundary choice has the same full inner port vector. Combining it
with any of E60-1's eight inner assignments satisfies all junctions,
and restricting any full labeling gives one such pair. Hence the
boundary is free and the total is `8·1728=13824`, exactly as printed.
The common port vector alone is forced: the three interior free
lines remain independent, so the sentence about the same labels
inside is interpreted consistently with the immediately preceding
eight interior possibilities.

## Remaining printed assertions kept separate

1. All eight standard labelings being physically realizable has not
   yet been proved. The explicit model59 closes exactly the all-arrow
   choice at the three inner V junctions. A convex cube model cannot
   itself certify a concave physical edge.
2. The corrected side-view diagram's exact80% flattening parameter
   and its individual strokes have been displayed, but no matching
   three-dimensional parameter reconstruction has been completed.
3. The unqualified phrase about chips permitting any desired overlaps
   is not promoted to a theorem about arbitrary pairwise orders.
   The12 actual overlaps of32 are fully proved; larger arrays are
   checked separately in61–62.

Historical Reutersvard/Huffman quotations and dates, the museum
catalogue, Latin-class anecdote and Ernst references are explicitly
omitted bibliography. No mathematical argument above depends on them.
