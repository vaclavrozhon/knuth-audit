# Graceful labels: all of Fig.105, arrays33--35, and exercises67--70

Original p16--17/file31--32, question p120/file135, answer67 at
p173/file188, and answers68--70 at p174/file189 were displayed.
The known7June2025 correction to68 is applied explicitly below;
the uncorrected last-line edge is not a new finding. The complete
primary errata TeX has that correction at lines1119--1121.

`check_graceful_colonies67_70.py` and
`results/graceful-colonies67-70.json` contain exact certificates.
The only searches were the fixed puzzle, the fixed rare GA--SC
branch, and one witness for each other possible longest edge.
Together they visited4726 nodes and took less than0.2seconds at
nice15. No full641952-labeling census or historical benchmark was
run. The two completed search trees are retained, including every
branch and every empty-column leaf.

## G105-1 — every native edge and vertex label

The source SVG contains12 straight paths per panel,48 in total.
Every segment endpoint in each of the four panels was matched
to its named grid vertex with squared error below1/10000pt².
Each panel has exactly the same18 edges and13 vertices; no extra
crossing or intermediate junction is introduced. The labels were
read in the original image, not inferred from the desired differences.

The complete panel(b) assignment is

    NH8 NY0 MA17 PA18 NJ12 CT15 RI1 MD10 DE5 VA6 NC3 GA13 SC14.

Here are all edges, ordered by their differences; this is also an
individual verification of every equality in(33):

| Difference | Edge | Endpoint calculation |
|---:|---|---|
|1|GA--SC|14−13|
|2|MA--CT|17−15|
|3|VA--NC|6−3|
|4|MD--VA|10−6|
|5|MD--DE|10−5|
|6|PA--NJ|18−12|
|7|NJ--DE|12−5|
|8|PA--MD|18−10|
|9|NH--MA|17−8|
|10|NC--GA|13−3|
|11|NC--SC|14−3|
|12|NY--NJ|12−0|
|13|PA--DE|18−5|
|14|CT--RI|15−1|
|15|NY--CT|15−0|
|16|MA--RI|17−1|
|17|NY--MA|17−0|
|18|NY--PA|18−0|

The13 vertex values are distinct and lie in0,…,18. Thus every
defining condition is satisfied. Panel(c), read independently,
has each entry18 minus the corresponding panel(b) value. The
checker compares all18 of its differences with this same list.
Panel(d)'s three given entries are GA0,SC18,NJ5; no other vertex
is prescribed in the source.

The geographical wording is kept separate from this exact graph.
The historical boundary epoch has not been established: a graph
on the modern states bearing the colonies' names need not be the
1776 colonial boundary graph. A quick primary-source lookup found
the [Library of Congress1776 map](https://www.loc.gov/resource/g3710.ar071402/)
and its [historical-boundary overview](https://loc.gov/exhibits/mapping-a-growing-nation/overview.html),
which discusses unresolved early western boundaries. This does
not settle the intended convention in the book. The map comparison
remains partial, without a finding card. The mathematical audit
uses precisely the drawn18-edge graph.

## G105-2 — definition, complement, and graph automorphisms

Work with a finite simple graph having m edges. An injective
vertex labeling into{0,…,m} gives a nonzero absolute difference
on every edge, at most m. If these m differences are distinct,
they exhaust{1,…,m}; this is a bijection, not merely an upper
bound. Conversely, injective vertices and that exact difference
set satisfy the definition. In particular n≤m+1 is necessary.

Complementation sends l to m−l. It preserves the vertex range,
injectivity, and every edge difference because

    |(m−l(u))−(m−l(v))|=|l(u)−l(v)|.

It is an involution. For an automorphism α, l'(v)=l(vα) is again
injective with the same range. The permutation of vertices induces
a permutation of the finite edge set, so its edge differences
are the same m distinct values. A bijection preserving edges in
one direction preserves them in both directions, by finiteness.
Complementation commutes with this action.

For this particular graph the entire automorphism group has order2.
NH is the unique degree1 vertex, so NH and its neighbor MA are
fixed. Of MA's other neighbors, NY,CT,RI have distinct degrees4,3,2,
so all are fixed. NY's remaining PA and NJ have degrees4 and3,
so both are fixed. Among PA's two remaining degree3 neighbors,
DE is adjacent to the already fixed NJ, whereas MD is not; hence
both are fixed. This fixes VA and then NC. Only GA and SC remain,
and swapping them preserves the graph because both are adjacent
exactly to NC and to one another. Thus the identity and this swap
are all the automorphisms.

The general orbit argument inE68 below shows that m=18 makes the
combined action free, with2·2=4 labelings per orbit. It justifies
the four equivalent versions described in the main text, as well
as division by4 if the full census is eventually verified.

## E67 — every listed change, including both additional triples

Changing VA6 to7 affects only MD--VA and VA--NC. Their differences
4,3 become3,4;7 was unused, so the result remains graceful.

Keep all other labels fixed and write x=l(GA),y=l(SC). The three
affected differences must be{1,10,11}, and NC has value3. Three
ordered points on a line have their largest distance equal to the
sum of the smaller two, so their successive gaps are1 and10.
With one point fixed at3, the remaining possible unordered pairs
inside[0,18] are{2,13},{4,14},{13,14}; pairs extending to a
negative label are excluded. Each value in these three pairs is
unused by the other11 vertices. Both orders are possible, giving
exactly

    (2,13),(13,2),(4,14),(14,4),(13,14),(14,13).

The original is(13,14); the other five are precisely the answer.
This reasoning is exhaustive. The independent finite certificate
checks all56 ordered pairs from the eight unused values. None of
the six solutions uses6 or7, so they also work after VA6→7.

For the parenthetical additional replacement
(NJ,VA,GA):(12,6,13)→(6,13,7), the seven changed differences are

    NY--NJ 12→6, PA--NJ 6→12, NJ--DE 7→1,
    MD--VA 4→3, VA--NC 3→10, NC--GA 10→4, GA--SC 1→7.

This permutes{1,3,4,6,7,10,12}; the new vertex labels remain
distinct. Every other edge is unchanged. For the other replacement
(NH,VA,SC):(8,6,14)→(6,7,4), the five changed differences are

    NH--MA 9→11, MD--VA 4→3, VA--NC 3→4,
    NC--SC 11→1, GA--SC 1→9.

This permutes{1,3,4,9,11}; again the new vertex labels are distinct.
Thus both extra solutions, not just the requested pair changes,
are verified.

## E68 — the full orbit proof and its small-edge scope

Let Aut(G) have order k and let l be graceful. The k functions
l(vα) are distinct because l is injective; likewise their k
complements are distinct. A collision between the two sets is
equivalent, after composing by an inverse automorphism, to an
automorphism γ with l(vγ)=m−l(v). This is the printed β⁻α step
under its right-action convention. Thus only an automorphism
inducing complement on the labeled graph can reduce the orbit.

Suppose m>1 and such a γ exists. Add isolated vertices for missing
labels and identify every vertex with its label. This is valid
for the contradiction: the original used-label set is closed
under complement if γ exists, so the missing-label set is too;
extend γ there by j→m−j. No new edges are introduced. There is a
unique edge{0,m} with difference m. The unique edge with difference
m−1 is either{0,m−1} or{1,m}. Complement interchanges these two
distinct edges. They cannot both exist, since they have the same
difference. Therefore complement is not an automorphism.

Equivalently, orient the overall labeling so that the m−1 edge
is{0,m−1}; then{1,m} is absent. This is exactly the book's final
argument **after the known correction1→0**. It works also at m=2.
Hence the orbit has2k members and2k−1 other labelings for m>1.

At m=1 a gracefully labeled graph must be K2, since its edge uses
both available vertex values. Its k=2 automorphisms already
include complement, so its orbit has2 members and only1 other,
not3. This proves the stated counterexample.

At m=0, the empty graph or one isolated vertex is graceful under
the literal definition; k=1 and complement is the identity, so
the orbit has1 member. Thus the printed parenthesis singling out
m=1 additionally requires a positive-edge convention. That boundary
convention is an explicit partial, not a new finding. Graphs with
too many isolated vertices simply have no graceful labeling, so
they do not provide a counterexample to a statement quantified
over existing labelings.

## E69-1 — exact XCC model and both directions of its bijection

There are18 edge-difference primary items,18 graph-edge primary
items,13 colony secondary items, and19 holder secondary items.
For each oriented assignment of distinct labels x,y to the two
ends u,v of a graph edge e, include the option

    |x−y|, e, u:x, v:y, h_x:u, h_y:v.

For difference d there are19−d choices for the smaller label and
two orientations. Hence one graph edge has

    sum(d=1..18) 2(19−d)=18·19=342

options, giving18·342=6156. This proves the printed multiplication
and accounts for both endpoint orientations. PA3,DE9 gives the
displayed difference6 example exactly.

In a color-controlled cover, the primary graph-edge item chooses
one assignment per edge, and the primary difference item uses
every d once. Repeated appearances of a colony must have the same
color, so they define one label for that vertex. Every vertex of
this graph is incident to an edge, hence none is omitted. Repeated
appearances of holder h_x must have the same colony color; therefore
two different vertices cannot share label x. These assignments
are exactly a graceful labeling.

Conversely, a graceful labeling selects the unique specified
option for each graph edge. It covers each primary once and is
consistent at every colony and holder color. This is inverse to
the first construction, so the model counts labelings exactly,
with neither duplicates nor extra solutions. Isolated vertices
are not present in this example; their treatment in a general
model is not silently inferred from this proof.

## E69-2 — symmetry breaking,6156→5814, and the fixed clues

Retain only options on NY--MA with l(NY)<l(MA), and only options
on GA--SC with l(GA)<l(SC). These comparisons can be enforced
locally because the compared pairs are graph edges. Each deletes
171 of the342 orientations on its edge; the two sets are disjoint.
Thus6156−171−171=5814 options remain.

For any full labeling, record the two signs of those comparisons.
The GA/SC automorphism flips the second sign only. Complement
flips both. Their four actions yield all four sign pairs once,
so exactly one member of each four-element orbit satisfies both
inequalities. This proves the intended quotient independently of
the unverified full census.

For part(b), the new primary item* occurs in only one new option,
so that option must be chosen. Its three secondary colors force
GA0,SC18,NJ5. Every one of those vertices occurs in ordinary edge
options, so purification transfers the values throughout the model.
The holder items in the ordinary options enforce injectivity;
their omission from the extra clue option is harmless. Conversely
any graceful labeling with the clues adds this unique option and
is a cover of the augmented instance. This proves the exact puzzle
encoding, including both directions.

## G105-3 — uniqueness, the24 rare classes, and all18 longest edges

The bounded exact-cover search uses one primary column for each
edge and each difference. A row conflicts with all rows that use
either of its primaries, give either endpoint another label, or
give its label to a different vertex. These are exactly the XCC
incompatibilities proved above. At each node choose a smallest
remaining primary column and visit every currently compatible
row in it. Every cover chooses exactly one such row, so branches
are disjoint and exhaustive. Removing two primaries decreases
their finite count; empty columns reject and no remaining primary
accepts. This proves termination and completeness of each completed
saved tree. Initial fixed colors only delete logically impossible
rows, including holder collisions with a fixed vertex.

The puzzle tree has216 nodes and exactly one leaf solution:

    NH9 NY15 MA7 PA2 NJ5 CT3 RI14 MD16 DE11 VA1 NC17 GA0 SC18.

All18 differences are checked directly in the saved certificate.
The count216 belongs to this independent search order and is not
a reproduction of the printed192/62/23 counts.

The separate GA0,SC18 branch, with NY<MA, has1761 nodes and24
solutions. ByE69-2 these are exactly the24 equivalence classes
whose longest edge is GA--SC: its lower value must be0 and its
upper value18, while the remaining comparison chooses the unique
orbit representative. Thus this particular main-text census is
closed without enumerating the full graph census.

The result also contains18 complete explicit assignments, one for
each possible longest graph edge. Their endpoint values are0 and18,
and every assignment has all distinct vertex values and every
difference1,…,18. This proves the assertion that each edge can be
longest; existence witnesses do not establish their frequencies.

The full641952 total, quotient160488, and respective NY--PA/NY--MA
counts22782/24896 remain unverified. The division641952/4=160488
is arithmetically exact and its use is justified byE68, but that
does not prove the input census. Historical90/33gigamems and the
three named algorithm node counts likewise remain partial. The
informal hard-sudoku comparison has no defined quantitative
criterion and is not counted as a mathematical verification.

## G105-4 — complete meaning, construction, and cost of the arrays

Since n≤m+1, introduce one isolated vertex at each missing label.
Rename every original or added vertex by its label, giving exactly
0,…,m and l(v)=v. For the unique edge of difference d write its
ends as v,v+d and set LO[d]=v. Then, for any v<w, adjacency
implies LO[w−v]=v by uniqueness. Conversely that equality describes
precisely the edge{v,w}. This proves both directions of the O(1)
word-RAM adjacency test. LO[0] is unused.

Choose any order of the neighbors of each vertex. Set FIRST[v]
to its first neighbor, or−1 if none. For each occurrence of neighbor
w in v's list, store its successor (or−1 at the tail) in
NEXTL[v−w] when w<v, and NEXTH[w−v] when w>v. Each edge difference
occurs once globally, and its two endpoint incidences use opposite
arrays; thus no two needed pointers overwrite one another.

The invariant of(34) is that w is the current neighbor in the
chosen list. The indicated array entry is exactly its successor.
The list has deg(v) distinct members and ends with−1, so traversal
visits every neighbor once, visits no nonneighbor, and terminates.
Isolated vertices execute zero iterations. The client performs its
visit before advancing w, as the displayed loop intends. Time is
O(1+deg(v)) including initialization, and all vertices together
take O(m+1). Constructing the arrays from adjacency lists likewise
takes O(m+1) work and space after padding. This includes the m=0
one-vertex representation and does not interpret O(m) as a literal
zero running time there.

Every used entry in each of LO,FIRST,NEXTL,NEXTH,NAME from(35) is
transcribed in the certificate. For all171 unordered distinct
vertex pairs, the adjacency predicate matches the native graph;
all19 full pointer chains give exactly their neighbor sets and
end at−1. The13 NAME entries match the displayed colonies and the
six added isolates have unused names. Index0 of LO/NEXTL/NEXTH is
unused as indicated in the source. Thus no array entry is justified
only by an overall count or by one sample traversal.

## E70 — every complement formula and every resulting entry

An edge{v,v+d} becomes{m−v−d,m−v}, with lower endpoint
m−d−LO[d]. Hence LO'[d]=m−d−LO[d] for1≤d≤m. Its0 entry remains
unused; the answer's common range0≤l≤m is read with this explicit
unused-entry convention. NAME'[v]=NAME[m−v] is simply the inverse
renaming, preserving unused names.

Use at new vertex v the old neighbor order at m−v, with each value
complemented. This gives FIRST'[v]=m−FIRST[m−v]. A lower neighbor
of the new vertex was a higher neighbor of the old one, so its
next pointer comes from old NEXTH; similarly a new higher neighbor
uses old NEXTL. Therefore

    NEXTL'[d]=m−NEXTH[d], NEXTH'[d]=m−NEXTL[d].

For all three pointer formulas, an old−1 tail yields m+1, which
must be converted back to−1. No actual label produces m+1, so the
conversion cannot destroy a genuine neighbor. This verifies the
printed sentinel instruction and both endpoint cases.

For completeness, these are the entire transformed numeric arrays
for m=18, in index order0,…,18; a dash denotes an unused entry:

    LO'    = — 4 1 12 8 8 0 6 0 1 5 4 6 0 3 3 1 1 0
    FIRST' = 6 3 −1 1 5 4 0 −1 12 −1 1 −1 15 8 −1 12 −1 3 6
    NEXTL' = — 15 17 5 −1 6 13 0 −1 −1 4 −1 3 −1 1 1 −1 0 −1
    NEXTH' = — 15 10 8 13 0 8 18 13 17 −1 −1 −1 18 18 −1 18 −1 −1
    NAME'  = PA MA — CT SC GA NJ — MD — NH — VA DE — NC — RI NY.

All19 transformed traversals are checked, and each is exactly the
termwise complement of the corresponding old traversal. The
source observes that other neighbor orders are possible; this
follows directly from the arbitrary-order construction inG105-4.
