# Exercise63: all chart entries and the necessary linear system

Question p119/file134 and the complete answer p172–173/files187–188
were displayed, including both chart halves at high resolution.
The source still says “will corresponds”; the13September2026 grammar
correction is known. The22October2026 erratum changes the two T-shadow
entries to `m∈C,m≺B` and `m∈B,m≺C`. These are applied below and are
not findings. The primary TeX lines1109–1120 and both complete errata
texts were inspected; there is no listed p173 chart correction.

`check_linear_chart63.py` / `results/linear-chart63.json` save every
displayed row and two small exact witnesses discussed below. They
reuse the already closed native32/strong59 certificate; no geometry
or labeling enumeration was rerun. Bibliographic dependence on
Sugihara's1986 Chapter3 is explicitly skipped: the argument here is
independent, and no assertion about the scope of that book is verified.

## E63-1 — faces, junctions, and the depth convention

Use positive z away from the viewer. The already proved generic
view assumptions exclude a visible plane parallel to the viewing
direction, so each physical face plane has a unique representation

    z=h_f(x,y)=−a_f x−b_f y−c_f.

Within a connected open region of the projected line arrangement,
the nearest surface cannot change from one physical face to another
without crossing a projected visible edge or an occluding contour.
Thus an open planar face that shows the object belongs to one physical
face plane. Different planar faces may use the same physical plane;
introducing separate variables for them is harmless for necessity.

A sufficiently distant background plane exists because the finite
closed polyhedron is bounded: choose constant depth Z greater than
the maximum z of all its vertices, hence of all its faces. Any open
region whose rays miss the object can use this same plane. This
includes the unbounded face, and can include bounded faces as well;
the latter qualification is needed for the literal opening sentence
and is documented separately in E63-9.

At V/W/Y junctions the relevant point is the visible physical vertex,
by the complete generic trihedral classification in E41-c3. At T,
the point used by its own chart is on the terminating, rear edge,
behind the foreground bar. At a midpoint of an arrow segment, use
the point on the rear surface (or background) just behind that
occluding contour. The midpoint is in the relative interior of the
segment and cannot be another junction in an embedded HC graph.
These are the artificial points intended by J. There is exactly one
new midpoint per arrow segment. Fixed input coordinates determine
all their x,y values without any depth choices.

Write `p∈A` for z_p=h_A(p), `p≺A` for z_p>h_A(p), and
`p≻A` for z_p<h_A(p). The signs refer to front/back geometry, not
to an ordering of plane names. All strict comparisons below are
strict because an unrelated surface does not touch the visible
edge/vertex and no two supporting planes coincide at an off-crease
point in a generic view.

## E63-2 — local geometric rules, including off-edge extrapolation

For two visible faces meeting along a crease, their affine depth
difference vanishes on its carrier and changes sign on its two
sides. A convex crease has, on each face's visible side, that face
behind the extension of the other plane: a transverse section of a
convex solid has interior `z≥h_A,z≥h_B`, and the front surface is
max(h_A,h_B). A concave crease reverses this order: locally the
front surface is min(h_A,h_B). This proves the strict signs; it
does not assume that the extrapolated point lies in the finite other
face polygon. The two planes are distinct and their difference is
nonzero everywhere off their common carrier.

At an occluding segment the arrow identifies the foreground side
by the already proved Table1 convention. A shadow point lies in
the rear plane and strictly behind the foreground plane. At a T
the bar is foreground, and the terminating stem is strictly behind
it. If the stem is a crease, the artificial T point belongs to
both stem face planes. If the stem is an occluding contour, it
belongs to the stem's own foreground plane, in front of its rear
plane. These rules also cover the distant background plane.

For a W/Y consisting of three creases, all three face planes meet
at j. The sign of the difference between two of these affine
functions anywhere on a third ray is obtained from the two-face
rule above. It is constant along that open ray: the difference is
linear, vanishes at j, and has no second zero unless the two
distinct crease carriers coincide. Hence checking which sector a
ray enters determines the sign at its entire positive portion.
This is the reason the inequalities below apply at arbitrary
noncentral endpoints, not just at points infinitesimally near j.

## E63-3 — all four T rows, including every shadow entry

Use the chart's A above the bar, B below-left, C below-right,
with l and r the two bar shadows.

* T+ has `j∈B,C`, `j≺A`; `l∈B`, `l≺A,C`;
  `r∈C`, `r≺A,B`. The first three statements locate the rear
  convex crease endpoint. The l/r memberships and comparisons
  with A follow from occlusion. The comparisons with C/B follow
  from the convex max rule, on the B/C sides of the stem carrier.
* T− has `j∈B,C`, `j≺A`; `l∈B`, `l≺A`, `l≻C`;
  `r∈C`, `r≺A`, `r≻B`. Only the two crease comparisons change:
  the concave min rule reverses them. Occlusion by A is unchanged.
* Downward stem arrow has `j∈B`, `j≺A`, `j≻C`;
  `l∈B`, `l≺A`; `r∈C`, `r≺A`; and, after the known correction,
  `m∈C`, `m≺B`. The rear stem's foreground is B and its rear is
  C. Thus its endpoint j lies in B, whereas its shadow m lies in
  C. Both are behind A where required; the chart does not assert
  an unnecessary comparison between A and m away from the bar.
* Upward stem arrow has `j∈C`, `j≺A`, `j≻B`;
  `l∈B`, `l≺A`; `r∈C`, `r≺A`; and corrected
  `m∈B`, `m≺C`. This swaps the stem foreground/rear roles only.

These four lists account for every one of the36 printed/corrected
T relations. The previous wrong choices for m are not reused.

## E63-4 — all six V rows

Use the exact left/right rays and A-inside/B-outside sectors drawn
in the chart. The order of the six rows below is the source order.

* I+: `j∈A,B`, `l∈A`, `l≺B`. The crease gives the two
  memberships at j; the left arrow's rear is A. Its strict sign
  also agrees with the convex max rule for the right crease.
* IO: `j∈B`, `j≻A`, `l∈A`, `l≺B`, `r∈A`, `r≺B`.
  Both contours have foreground B; the actual corner j is in B,
  in front of A, and both artificial shadows are on A behind B.
* +O: `j∈A,B`, `r∈A`, `r≺B`. This is the other convex
  crease/contour placement; its only shadow is r in rear A.
* O−: `j∈A,B`, `l∈B`, `l≺A`. The left contour's rear
  is B; the right concave crease reverses the extrapolated order
  compared with the first row, exactly as its min rule requires.
* OI: `j∈A`, `j≻B`, `l∈B`, `l≺A`, `r∈B`, `r≺A`.
  Now both contours have foreground A, with corner j on A and
  both shadows on B strictly behind it.
* −I: `j∈A,B`, `r∈B`, `r≺A`. This is the other concave
  crease/contour placement, with r on rear B.

Thus every equality and inequality in all28 V entries is justified.
No arbitrary unidentified hidden third face is used in these rows.

## E63-5 — all W/Y rows and the endpoint qualification

For W(O+I), A and B meet at the middle convex crease; C is the
rear region outside the two contour rays. Therefore

    j∈A,B; l∈C; r∈C; l≺A; r≺B.

For **front-surface points** a and b on the left and right outer
carriers, respectively, the convex max rule gives the other four
printed relations

    a∈A; b∈B; a≺B; b≺A.

This geometric assertion is correct with that front-point premise.
The printed identification of a,b as members of J is not specified;
it cannot always mean the adjacent graph junction. E63-8 gives an
exact conflict if it does. Consequently this one row is closed as
a conditional geometric lemma, while its general use in the
printed construction remains partial.

For W(−+−), all of `j∈A,B,C` hold, and the remaining relations are
`a≺B`, `b≻C`, `c≺A`. The central + crease makes h_A>h_B
on its left side, hence at a where h_A=h_C, and h_B>h_A at
c where h_B=h_C. The left − crease makes h_A<h_C on A's
side, hence at b where h_A=h_B. This proves all three signs.
For W(+−+), exactly the same three sector comparisons reverse,
giving `a≻B`, `b≺C`, `c≻A`, together with `j∈A,B,C`.

For the Y with two arrows and a concave downward stem, the
foreground crease faces are B,C and the rear plane is A. Hence
`j∈B,C`, `j≻A`, `l∈A`, `l≺B`, `r∈A`, `r≺C`.
The two shadows are distinct samples of rear A. Rotating the
ray/face names cyclically gives the other two arrow Y patterns:
apply `(A,B,C)→(B,C,A)` and `(A,B,C)→(C,A,B)` to this complete
list, with the corresponding ray/shadow rotation. These are exactly
the three arrow entries among the five Y rows of Table1.

For Y(−−−), all `j∈A,B,C` hold, and
`a≻C`, `b≻B`, `c≻A`. For example a is on A/B; comparing
its common depth with C using either adjacent concave sector gives
h_A(a)=h_B(a)<h_C(a). The other two follow by the explicit cyclic
substitution of face/ray names. For Y(+++), all three comparisons
reverse by the convex rule, giving
`a≺C`, `b≺B`, `c≺A` and the same memberships at j.

In the last four all-crease W/Y rows, a,b,c are endpoints of
nonarrow edges. They cannot be T-bar endpoints because T bars
are arrows. At V/W/Y endpoints, the actual point lies on both
incident crease planes; at a T-stem endpoint, the artificial point
does too. Thus the membership premise used for these endpoints
is valid even when other graph junctions intervene elsewhere.
The W(O+I) ambiguity is not extended to these valid cases.

The16 displayed chart cases cover all18 Table1 patterns: four T,
six V, three W, and five Y, with the arrow Y row covering three
cyclic positions. Reflection merely relabels the displayed face/ray
roles and preserves every front/back statement.

## E63-6 — exact linearization and elimination of strict inequalities

For every listed relation, substitute

    L_A(j)=a_A x_j+b_A y_j+z_j+c_A=z_j−h_A(x_j,y_j).

The constants x_j,y_j are input coordinates, while a_A,b_A,c_A,z_j
are unknowns. Therefore L is linear, with at most four nonzero
variable coefficients, despite the displayed products a_A x_j
and b_A y_j. `j∈A` is exactly L=0; `j≺A` is exactly L>0;
`j≻A` is exactly L<0. These are the printed signs, including the
convention positive z away from the viewer.

There are finitely many strict conditions. Given a strict solution,
let δ be the minimum of all positive margins L or −L required
by them. Then δ>0. Multiply **all** a,b,c,z variables by any
λ≥1/δ. Every homogeneous zero equation remains zero, and each
strict margin becomes at least1. Conversely L≥1 implies L>0
and L≤−1 implies L<0. This proves equivalence of strict and
nonstrict feasibility, rather than an equivalence of their individual
solution sets. When there are no strict conditions, choose λ=1;
no minimum of an empty set is taken. This also covers the empty
graph and a system with no shadow points.

The argument requires that every equation is homogeneous in these
unknowns; fixed x,y are coefficients, and no absolute depth, slope,
or size normalization is imposed. It would fail if a nonhomogeneous
normalization were silently added. None is added by the answer.

## E63-7 — a complete necessary construction, size, and termination

The exercise asks for a necessary linear system, not a decision
procedure for strong realization. With background assigned also to
bounded empty regions, the only unresolved identification in the
printed construction is W(O+I)'s a,b. A precise repair uses no new
depth variables: replace its four a,b relations by

    h_A(x_l,y_l)−h_B(x_l,y_l)>0,
    h_B(x_r,y_r)−h_A(x_r,y_r)>0.

Here l,r are the already defined shadows, but the displayed formulas
evaluate the **foreground planes** at their known screen positions;
they do not use the rear depths z_l,z_r. Each positive ray point
has the same strict crease sign proved in E63-5. Thus an actual
generic projection supplies a satisfying assignment for every row
of this fully specified repaired system. Replacing >0 by≥1 after
the same common scaling remains valid because these added forms
are homogeneous too.

To construct it, trace the two sides of each graph edge in the
given planar embedding to enumerate the face incidences, add each
arrow midpoint once, and append the constant-size row list for
each original junction. Each directed half-edge is visited once
and every junction is processed once, so it terminates after
O(v+e) combinatorial/arithmetic steps, given the embedding's face
representation. Disconnected components need their supplied
nesting/face incidence, not an assumption that each component's
outside is a separate physical background region.

There are |J|=v+e_arrow point variables and3f plane variables;
each displayed junction has at most10 conditions. Euler's formula
f=1+e−v+c, with c≤v for a nonempty graph, gives f≤e+1, hence
O(v+e) variables and conditions. The empty graph has one face and
three unused plane variables and is handled directly. Input
rational coordinates and their midpoints keep polynomial bit size;
this construction claim does not estimate the bit cost of an LP
solver or of choosing an actual spatial witness.

All local necessary relations, after this explicit qualification,
are therefore closed. They do not prove global nonintersection,
closure of hidden surfaces, or sufficiency for a3VP. The answer
explicitly says that sufficiency is unknown. That research claim
remains partial, not a supposed theorem supplied by these tests.

## E63-8 — exact adjacent-endpoint conflict, with no new finding card

The source defines J to contain original junctions and one midpoint
shadow for each arrow edge; it introduces no separate foreground
points called a,b. In the W(O+I) diagram they are circled at the
outer ends of the arrow lines. Under the natural adjacent-junction
reading, the construction is inconsistent even for the already
strongly realized original Reutersvard picture32.

Use the complete saved native network and the all-arrow-center
standard labeling whose explicit nine-chip witness was proved in
E59. In integer screen coordinates,

    j=v10=(8,16), type W, neighbors(v11,v03,v09), row O+I;
    b=v09=(6,14), type T, neighbors(v10,v08,v02).

The T bars are v09–v10 and v09–v02. Their common foreground planar
face has boundary

    F=(v00,v03,v10,v09,v02).

For the W chart this is its B face, so the printed `b∈B`
requires z_v09=h_F(6,14). For the T chart this same face is its A,
so `j≺A` requires z_v09>h_F(6,14), or≥h_F+1 after scaling.
These two constraints alone are inconsistent.

The saved physical model removes any doubt that this is a legal
projection: at the crossing, foreground physical edge6 has depth
−14397/200, and rear terminating edge104 has depth1441/80. Their
strict separation is35999/400. Both values are obtained by exact
interpolation of the already certified endpoints; the entire
visibility computation is not repeated. The model has only convex
chips and all its local labels are the ones just used.

Following the straight bar through v09 to physical endpoint v02
would repair this particular use of b: v02 lies on the front plane.
More generally one can skip bar-T subdivisions of the same straight
physical contour until its real endpoint, or introduce independent
front samples, or use E63-7's direct plane comparison. Such a chain
terminates because it moves along a finite straight segment and
cannot form a cycle. The text does not say which convention for
a,b is intended. Therefore the general printed row stays partial;
the conditional contradiction is saved for independent review,
without declaring an unambiguous new error or rejecting all of63.

## E63-9 — bounded background and the open sufficiency question

The opening prose exempts only the exterior face from corresponding
to a face of X. A bounded empty region also needs a background
plane. In the same strong Reutersvard witness, planar face14 has
the12-vertex boundary saved in `linear-chart63.json`. The point
(15,23) is strictly inside it by an exact odd ray-crossing count,
and lies outside all nine projected cube hexagons. Each such
hexagon centered at c satisfies

    |x−c_x|≤4,       |x−c_x|+|y−c_y|≤8.

The saved nine offsets each violate at least one inequality.
Thus this bounded face does not show any physical face of X.
Allowing it the same distant background plane fixes the semantic
statement and does not harm the linear construction. This limited
prose scope is recorded as partial, without a new finding card.

Neither this clarification nor the endpoint repair establishes
sufficiency. A feasible collection of local supporting planes may
still lack the required finite, globally consistent, closed
trihedral solid. The source explicitly leaves that implication
unknown; no experimental feasibility result is substituted for it.
