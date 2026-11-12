# Exercises65–66: complete orthogonal labeling proof and explicit open scope

Question p119/file134 and answer p173/file188 were displayed. The
general hardness claim, its exact input convention, and the research
question66 are distinguished from the fully proved orthogonal
labeling algorithm below. No new finding card is introduced here.

The original paper's text was read through the author's uploaded
[1988 article](https://www.academia.edu/110337075/The_complexity_of_recognizing_polyhedral_scenes)
(also the duplicate upload ending110337067). Its Theorem1 concerns
labelability of a given planar image; Theorem3 concerns the restricted
orthogonal catalog. The discussion of Theorem1 uses bounded-occurrence
planar clauses and several drawn gadgets. Those figures could not
be obtained with the available PDF sources, so their relations and
geometric composition are **not verified** by that text retrieval.
The publisher, author PDF, repository, and old CiteSeer links did
not supply a readable PDF. This limitation is logged in
`sources/kirousis-1988-access.json`. The cited
[Lichtenstein paper](https://epubs.siam.org/doi/10.1137/0211025)
has a verified title/journal pointer, but its full bounded-occurrence
reduction was not read. Bibliographic and missing-figure scope is
explicitly left open, without treating the abstract as a proof.

The orthogonal argument below is independent: it reuses the already
proved complete cubie classification from41, and verifies every local
Boolean projection in `check_orthohedral65.py` /
`results/orthohedral65.json`. No spatial search or old cubie
classification was rerun.

## E65-1 — which decision problem, and membership in NP

Given an HC picture/network with its ordered junction types, a
labeling uses one of four symbols for each edge. A certificate
therefore needs two bits per edge. Compare the two endpoint
conventions by reversing I/O when the edge direction is reversed,
and check the resulting tuple at each junction against its fixed
Table1 list. These lists have at most six rows and arity at most
three, so this verification takes O(v+e) time and space. Thus
ordinary line labelability is in NP, including disconnected
networks, empty pictures, and prescribed finite edge domains.

The adjective “realizable” in question65 needs care. Exercise47
defines a **network** to be realizable when it admits a planar HC
drawing with the stated outer-T condition. Page15 instead defines
strong/weak **physical** realizability for pictures. Either physical
notion already implies labelability: take the actual3VP's edge
labels, use the complete41 local classification, and in the weak
case transfer the labels through the identical ordered HC network.
Consequently a promise of physical realizability would make the
yes/no labeling question identically yes on its promised inputs.
The primary Theorem1 has no such physical promise. The natural
intended reading is geometrically drawn HC inputs as in47; the bare
picture/network wording is recorded as an interpretation partial.

## E65-2 — axis normalization and the60°/120° assertion

In an orthohedral scene, every physical face is a coordinate plane
and every physical edge is parallel to one coordinate axis. A
histoscape satisfies this condition: horizontal faces have constant
z, and its vertical walls have constant x or y, as in the closed27
model. Nonconvexity and different column heights do not change
these face orientations.

Let the viewing direction be q with all three coordinates nonzero,
as required for a generic view. Reflect coordinate axes if needed
to make q_i>0, then rescale coordinate i by1/q_i. This invertible
diagonal map preserves coordinate planes and converts viewing rays
to direction(1,1,1). It induces an invertible linear change on the
screen quotient. Therefore it preserves junction types, crossings,
occlusion order,and convex/concave labels, although it changes
the numerical screen angles. This justifies “can be assumed” rather
than asserting60° angles in every arbitrary original camera view.

Orthogonal projection perpendicular to(1,1,1) sends axis e_i to
u_i=e_i−(1,1,1)/3. Each has squared length2/3, and for i≠j,
u_i·u_j=−1/3. Thus distinct positive axis rays form120° angles;
reversing one ray gives60°. Opposite rays of one axis form180°,
the two bars of a T. All resulting line angles are multiples of60°.

For bookkeeping use six cyclic directions0,…,5, represented by
integer pairs

    (1,0),(0,1),(−1,1),(−1,0),(0,−1),(1,−1).

They have their actual60° geometry in the metric induced by mapping
(a,b) to(a+b/2,sqrt(3)b/2). The three positive axes used by the
saved41 cases are directions0,4,2. Their opposites are3,1,5.
Changing from41's unequal projection lengths to these canonical
directions leaves every visibility and oriented-label relation
unchanged: the view remains in the same open octant and the cyclic
order of the six projected axis rays is the same.

All18 visible V cases from41 are checked individually. Their two
direction indices differ by one step precisely in the six cases
that contain a plus; the angle is60°. Each of the other12 cases
has a two-step separation, angle120°. Grouping by ordinary Table1
row proves exactly the printed statement: its two plus-containing
V patterns require60°,and its other four V patterns require120°.
The exact direction pair, labels,and angle for each of the18 cases
are saved, so this is the complete classification, not a sample.

## E65-3 — every restricted local relation

Group the32 visible cubie cases of41 by their actual set of
canonical ray directions, keeping the I/O labels relative to the
outgoing ray. This produces12 V,6 W,and2 Y geometric relations.
They are complete because41 classifies all trihedral octant
occupancies, and every orthohedral vertex is one of these exact
octant configurations. Conversely each saved occupancy supplies
the stated local configuration.

For T, choose one of three bar axes and any of the four remaining
noncollinear stem rays. The material on the foreground side is
opposite the stem. A bar ray therefore has label O when its cross
product with the stem ray is positive,and I otherwise; the other
bar is opposite. The stem has any of the four labels. This gives
all12 T relations, for32 geometric relations in total.

The full lists, with witnesses, are saved. Their structure is:

* Every acute V has one row with a plus and an arrow. An obtuse
  V is either fixed at two arrows, or has three rows: two arrows,
  or one arrow and one minus, with each arrow direction fixed.
* A W is either fixed with two pluses and a middle minus, or has
  a fixed middle plus and two outer ports that are both minuses
  or both arrows in their prescribed directions.
* The Y on directions{0,2,4} is fixed at three pluses. The inverted
  Y on{1,3,5} has, in sorted-direction order, exactly

      ---, -OI, I-O, OI-.

* Every T fixes its two bar arrows and leaves the stem independent.

The lists include all rotations, so the phrases acute/obtuse or
inverted do not leave a hidden choice of drawing orientation.

## E65-4 — all edge domains and the elimination of larger ambiguities

For an edge, intersect the marginal labels allowed at its two
endpoints, reversing I and O at the second endpoint. If the
intersection is empty, reject. Every possible nonempty intersection
of the32 local catalogs is included in the finite certificate.

Every surviving domain is either a singleton, a two-element set
{−,a} with a fixed arrow a, or one of these independent larger
cases:

1. A T-stem to T-stem edge has all four labels. Neither endpoint
   relates its value to another edge, so it can be omitted and
   assigned arbitrarily when a solution is reconstructed.
2. An inverted-Y to T-stem edge has{−,I,O}. It occurs in only
   the Y's nontrivial relation; existentially eliminating it from
   that one local relation loses no global information. Once the
   Y's retained ports are assigned, choose a witnessed extension.

There is no edge with two inverted-Y endpoints: every ray of
such a Y has an odd direction index, while at the other endpoint
the same straight edge has the opposite, even direction. No other
non-T relation has a three-way marginal domain. These facts prove
that every omitted larger domain is indeed local to one remaining
constraint, not a variable whose consistency was accidentally
discarded. Multiple free ports at one Y are eliminated jointly.

Singletons are substituted. For each remaining edge define Boolean
x_e=0 for minus and x_e=1 for its one permitted arrow. This is a
bijection between its two remaining values and{0,1}; no plus or
second arrow is silently combined with another state.

## E65-5 — complete2-CNF representation, not a heuristic propagation

For each local relation, substitute its singleton ports and
existentially eliminate its independent larger-domain ports.
The resulting relation has at most three Boolean ports. The
following gives all of its exact clauses: for each missing one-
or two-port assignment, forbid that assignment by a unit or binary
clause. For example a missing pair(x_i,x_j)=(b_i,b_j) yields

    (x_i≠b_i) or (x_j≠b_j).

An empty local relation yields an empty, false clause. The finite
checker constructs these clauses for **every possible combination
of endpoint marginal domains**, and compares their satisfying
assignments with the entire projected local relation. There are
367 nonempty-domain combinations,plus524 combinations rejected for
an empty edge intersection. At most eight Boolean assignments
exist in any individual comparison. All agree exactly, and an
original-table extension witness is stored for every accepted
Boolean tuple.

The table structure also explains this result directly. A variable
obtuse V requires at least one arrow, giving x∨y. A variable W
requires both outer choices equal, giving x↔y. At an inverted Y,
allowed arrows are a correctly directed pair or none. If all three
ports are binary, a fixed I/O choice permits at most one of its
three cyclic pairs, so that pair is equal and every other port is
zero. If one port is locally free, the remaining two have either
equal values, at most one arrow, a forced zero, or no restriction.
If two or three ports are locally free, no relation of arity above
one remains. Substitution of fixed ports only removes more choices;
the367-case certificate includes each such boundary case.

Conjoin all of these clauses. Any original labeling gives a
satisfying Boolean assignment. Conversely a satisfying assignment
chooses a tuple in every exact local relation. Restore each
eliminated Y–T edge from that Y's saved extension, and each T–T
edge arbitrarily. No restored edge is constrained by another Y,
and T stems add no condition. Thus the restored labels satisfy
every original restricted junction relation. This proves both
directions of the reduction.

## E65-6 — solving, reconstruction, termination,and the linear bound

For a clause a∨b add implications not-a→b and not-b→a; a unit
clause repeats its literal. If a Boolean variable and its negation
belong to the same strongly connected component, either truth
choice would force both, so the system is inconsistent. Otherwise
topologically order the component DAG and set a literal true when
its component comes after that of its negation.

This assignment satisfies every implication. Indeed, if u→v had
u true and v false, the implication and its contrapositive
not-v→not-u would give

    index(u)≤index(v)<index(not-v)≤index(not-u)<index(u),

a contradiction. Hence all clauses hold. Strong components are
computed by the already fully closed Tarjan algorithm from the
preface; its termination and O(vertices+arcs) bound are reused.
An empty formula, no Boolean variables, disconnected components,
and immediate empty-domain/local-relation failures are all included.

Each original edge and junction requires constant work to select
its catalog, intersect domains,and generate at most a constant
number of clauses. There are O(v+e) Boolean variables,clauses,and
implication arcs. The component calculation and one local extension
lookup per junction therefore take O(v+e) time and space, including
the output labeling. This is the usual combinatorial/arithmetic
bound; it does not assert constant bit cost for arbitrarily large
input-coordinate comparisons.

If the three undirected axis directions are given without a
global orientation of their canonical frame, there are only two
possible alternating choices of the three positive rays,up to
renaming axes. Apply the catalog and its global180° rotation as
two separate problems. Either successful run supplies an admissible
oriented interpretation; this doubles the work only. The two
catalogs must not be mixed independently at different vertices.
For a fixed oriented orthogonal frame, use its single catalog.

This proves the printed linear-time **restricted labelability**
result. It is not an algorithm deciding whether the labeled picture
has a globally consistent solid orthohedral realization.

## E65-7 — remaining general hardness obligations

Membership in NP is closed. The hard direction for ordinary HC
labelability remains partial until all of the following are checked
in an actual construction: the nonarrow filter, bounded-occurrence
variable fanout, negation/bending gadget, all eight clause input
patterns, fewer-than-three-literal cases, disposal of hanging edges,
planar placement, and a polynomial output-size/coordinate bound.
The primary text describes these ingredients, but its unviewed
figures cannot substitute for their exact ordered junction lists.
Neither recognition of the cited result nor the independent
orthogonal algorithm closes this separate proof.

The ambiguity of “realizable HC picture” is likewise kept separate.
The physical promise would trivialize labelability,while the planar
network convention leads to the intended nontrivial problem. The
current record does not declare an unambiguous book erratum from
that adjective alone.

## E66-1 — research question and model boundary

Exercise66 asks whether weak3VP realizability is decidable, then
asks for its complexity if so. No algorithm or complexity bound
for that exact model is established here. The earlier48 result
concerns whether an abstract network admits a planar HC drawing;
it does not produce hidden spatial faces and cannot answer66.
The complete strong witnesses for particular pictures,including64,
likewise do not give a bound on hidden complexity for arbitrary
networks.

The answer explicitly distinguishes Sugihara's model from3VPs.
The1988 article also invokes an LP reconstruction theorem and a
completion of visible patches, but its text alone does not verify
that the completed objects satisfy this book's exact trihedral and
generic-view requirements. Those bibliographic/model claims remain
partial. In particular, no transfer of its realizability theorem
is used to mark63's sufficiency or66 as solved. These are explicit
research/model gaps,not findings and not missing arithmetic tests.
