# Penrose31 and every part of58

Originals: p15/file30 and p119/file134; answer p171/file186. The
original pages have been displayed. All four paths58–61 of31 and
all eighteen paths19–36 of the four exercise drawings are checked
in `check_penrose58.py` / `results/penrose58.json`.

The known6September2026 correction to answer58(a) is applied:
`w_k=W(v_(k+1),u_(k-1),v_k)`. The erroneous duplicate `v_k` and
wrong index on `u` are known corrections, not findings.
The primary source is `sources/err4f7-2026-11-06.textxt`, lines1082–1084.
No additional brute-force census or spatial realization search is used.

## P58-1 — every native junction, line, and region

Indices below are modulo n, with n≥3. The complete ordered network is

    t_k=T(t_(k-1),t_(k+1),u_k),
    u_k=V(w_(k+1),t_k),
    v_k=V(w_k,w_(k-1)),
    w_k=W(v_(k+1),u_(k-1),v_k).

There are4n junctions and5n physical lines. In source134, if the
paths for a given drawing are numbered i=0,…,n−1, path i visits
`t_(-i),u_(-i+1),w_(-i+2),v_(-i+2),w_(-i+1)`; its first segment
passes through `t_(-i+1)`. Thus every line, including each T bar
split at its junction, is accounted for.

For31 the four original paths become

    w0 v0 w2 v2 w1 v1 w0;
    w0 u2 t1;
    w2 u1 t0;
    w1 u0 t2.

Native PDF coordinates have small rounding discrepancies at intended
T incidences. The script keeps every t endpoint, averages duplicate
w occurrences, and projects u onto the exact line t_(k−1)t_k.
Each projection extends that line strictly beyond t_k. Every original
point occurrence moves less than.01pt, with the exact squared residual
saved. No other intersection or angular type is snapped. Segment
splitting then verifies all4n vertices, all5n edges, and every exact
ordered junction above, rather than comparing only a graph census.

The face permutation gives precisely the following n+2 walks:

* the central walk t0,t_(n−1),…,t1;
* the outside walk v0,w0,v1,w1,…,v_(n−1),w_(n−1);
* for each k, the seven-sided walk
  `w_k,u_(k−1),t_(k−1),t_k,u_k,w_(k+1),v_(k+1)`.

The last n walks are the printed regions F_k. Their seven vertices
are distinct even when n=3. The identity follows directly by applying
the clockwise successor permutation at each V,W,T; it accounts for
all10n directed edges because n+2n+7n=10n. Each finite picture is
also checked against these exact walks and the outside walk.

## P58-2 — an HC drawing exists for every n, not just the four examples

This construction concerns a planar HC picture, not a physical3VP.
Use positive determinant orientation in the picture plane. Put
theta=2pi/n, c=cos(theta), and let t_k be a regular positively oriented
n-gon on the unit circle. Write e_k=t_k−t_(k−1); hence
e_(k−1)+e_(k+1)=2c e_k and cross(e_k,e_(k+1))=s>0.
For sufficiently small positive epsilon set

    u_k=t_k+epsilon e_k,
    w_k=t_k+3epsilon e_k+epsilon e_(k−1).

Then `w_(k+1)−u_k=(1+3epsilon)e_(k+1)`. The t/u orders are
exactly the stated T and V, since cross(e_k,e_(k+1))>0. The w's
form a rotated and scaled regular polygon: multiplication by the
same nonzero complex number takes each t_k to w_k.

Both t_k and u_k are strictly inside the w polygon for small epsilon.
For the incoming and outgoing sides at w_k, their first nonzero
signed margins, divided by epsilon s, are respectively
`1,3+2c` for t_k and `1,2+2c` for u_k. These are positive for
n≥3. All other side margins are already strictly positive at
epsilon=0 and remain so by continuity.

The segment u_(k−1)w_k is parallel to e_k and lies strictly outside
the central polygon's supporting line t_(k−1)t_k. Consecutive such
carriers intersect at `u_k−epsilon e_(k+1)`, which is before the
start of the next segment, so their finite segments do not cross.
Nonconsecutive segments have disjoint limiting central sides and
remain disjoint for small epsilon. A t_k u_k segment meets only
its incident spoke: its only other nearby spoke is parallel and
distinct, and all other pairs have disjoint limiting neighborhoods.
The extended t edge lies outside the central polygon except at t_k.
These arguments exhaust the possible segment intersections.

Finally choose positive delta much smaller than epsilon and put

    v_k=w_k−delta(e_k+e_(k+1)).

Each v_k is just outside the incoming side of the w polygon and
inside every other side. Thus replacing each side w_(k−1)w_k by
the two edges through v_k produces a simple convex2n-gon enclosing
the previous graph. It introduces no crossing with the inner graph.
At v_k the leading V determinant is delta s>0. At w_k, the three
W determinants for the ordered rays
`v_(k+1),u_(k−1),v_k` have positive leading terms s,delta s,delta s
as epsilon then delta tend to zero. The exact coefficients vary
continuously; for sufficiently small choices they remain positive.
All junction types are therefore the stated ones. There are finitely
many strict conditions for each fixed n, so one common positive
choice of epsilon and then delta satisfies all of them. This supplies
the all-n geometric existence argument without extrapolating the
four printed drawings.

## P58-3 — all forced inner labels

Use O/I for outgoing/incoming arrows at a junction. The T rows in
the proved Table1 have first branch O and third branch I. Thus
every t_k→t_(k−1) is an arrow in that direction, and u_k→t_k is
an arrow in that direction. The second T branch is already fixed
consistently by the neighboring T; every T is the row OII.

At u_k=V(w_(k+1),t_k), the second branch is O. The only permitted
V rows with second O are IO and +O, so the u_k–w_(k+1) line is
either an arrow or+. At w_(k+1) that same physical line is its
middle branch, which a W requires to be+or−. Hence it is+.
All u's are therefore +O, all middle W branches are+, and every
inner physical line has one forced label. No assumptions about
outer labels were used.

## P58-4 — exact Lucas count, standardness, and free boundary

With its middle+, w_k permits only O+I or−+−. Along the outside
direction `v_k→w_k→v_(k+1)`, its two boundary edges are therefore
both arrows in that direction or both−. Denote that common state
by a_k in {>,−}.

At v_k=V(w_k,w_(k−1)), the three possible pairs are

    (a_(k−1),a_k)=(>,>),(>,−),(−,>).

They are respectively the local rows OI,−I,O−, with the branch
directions accounted for. Two consecutive−states are forbidden;
these are all restrictions. Conversely, every cyclic word with no
adjacent−pair, together with the forced inner labels of P58-3,
satisfies every V,W,T row. This is an explicit bijection, so neither
GAC nor a numerical sample is being used as a completeness proof.

The transition matrix in order >,− is A=[[1,1],[1,0]]. Therefore
the number is trace(A^n)=F_(n+1)+F_(n−1)=L_n. The powers and Lucas
identity were already proved, including the small-index conventions,
in `hc-boundary-matrix-bounds-055.md`, E55-0 and E55-a. Here n≥3.
The tiny independent certificates list every allowed binary word for
n=3,4,5,6 and check every resulting physical edge label against all
local relations: counts4,7,11,18.

The outside walk is fixed by P58-1/P58-5. Exactly the all-arrow word
is standard. Since the inner assignment is the same for every
boundary word, the full solution set is exactly

    {the one inner assignment} × {the L_n allowed boundary words}.

This proves the printed free-boundary assertion in its defined
Cartesian-product sense, not just equality of two counts. The
comparison with51 is justified by its separately proved cyclic-word
reduction; no new claim about the smile boundary is inferred here.

## P58-5 — the unique embedding claim and its exact scope

In any HC realization of this ordered network, the cyclic order at
every vertex is fixed by its specified V,W,T order. Consequently
the same face permutation and the same n+2 face walks result.
This is the precise combinatorial meaning of the printed phrase
"uniquely embeddable"; it does not assert unique coordinates.

No seven-sided F_k walk can be outside: at its t_k it uses both
collinear T bars. Exercise47 explicitly excludes such an outer T
from a realizable network; its physical impossibility has already
been proved in `hc-boundaries-and-exercises-045-047.md`. The central
walk has only T vertices and cannot be the outside boundary of a
finite straight picture: the proved47(d) hull argument requires at
least three V or W vertices. Thus the only possible outside walk
is the alternating v,w walk of P58-1.

This outside polygon is strictly convex. At every w the two boundary
rays are the first and third W rays, with the middle ray inside
their angle less than pi; at every v they are the ordered V rays.
In each case the boundary turn has positive determinant. A simple
polygon with all turns in this same strict direction is convex:
its tangent angle turns by2pi, every interior angle is less than pi,
and any hypothetical reflex vertex would contradict that condition.
The same argument at the t cycle, using the ordered T stem, makes
the t polygon strictly convex. Both statements concern every HC
realization, not just the native coordinates.

## P58-6 — the central point lies on the required side of every crease

Let P be any point strictly inside the t polygon. For the crease
from u_k to w_(k+1), put d=w_(k+1)−u_k and e=t_k−t_(k−1).
The T incidence gives u_k=t_k+alpha e with alpha>0. The V order
at u_k says cross(d,t_k−u_k)>0, hence cross(e,d)>0.

The full negative ray u_k−r d, r>0, lies outside the central polygon:
its signed side value with respect to the central side e is
`cross(e,u_k−r d−t_k)=−r cross(e,d)<0`, whereas the central
polygon lies in the nonnegative half-plane. The finite positive
segment u_k w_(k+1) cannot cross the central cycle by planarity.
Past w_(k+1), the positive ray is outside the convex outside polygon,
because w_(k+1) is its boundary point and u_k is inside. Thus the
entire crease carrier misses the central polygon.

The connected central polygon must lie strictly on the side already
occupied by t_k: `cross(d,P−u_k)>0`. This proves the side needed
for the depth inequality for every embedding. The script also checks
all central vertex margins for each native picture, but those finite
checks are not the general argument.

## P58-7 — every face-plane height inequality and cyclic contradiction

Assume a strong realization X exists for some HC picture with this
network. Each open seven-sided region F_k has a single visible planar
face; a change to a noncoplanar visible face inside it would introduce
a drawn crease. Let pi_k be its containing plane. General position
excludes a face parallel to the viewing direction, so pi_k is the
graph of an affine depth function z_k(x,y), taking positive depth
away from the viewer. This choice of sign agrees with the displayed
inequality in the answer; reversing depth reverses every inequality
and leaves the contradiction unchanged.

The edge u_(k−1)w_k is forced+ by P58-3. It is therefore a genuine
convex crease shared by the planes pi_(k−1) and pi_k. The interior
of region F_k lies on the positive side of the oriented carrier
u_(k−1)→w_k, as is seen from its exact face walk in P58-1. At a
convex crease, a perpendicular planar section has two facets bending
away from the viewer. On the side occupied by facet k, its depth
is greater than the extension of facet k−1. Algebraically,

    z_k(Q)−z_(k−1)(Q)
       = lambda_k cross(w_k−u_(k−1), Q−u_(k−1)),  lambda_k>0.

Equality holds on the crease carrier; convexity fixes the positive
coefficient, and a noncoplanar genuine crease makes it strict.
This affine identity remains valid beyond the finite faces.
By P58-6 its right side is strictly positive at P. Thus

    z_k(P)>z_(k−1)(P),  for every k modulo n.

Summing these n inequalities gives0>0. This excludes every strong
realization of every picture with the network, so the Penrose n-gon
is not weakly realizable for any n≥3. Adjacent faces are distinct
because their edge is a genuine crease; possible repeated names for
nonadjacent physical faces cannot avoid the cyclic contradiction.

The printed line through P always meets each containing plane pi_k
once. It need not be justified as meeting the finite polygonal face
F_k itself: P is in the central region, not its visible seven-sided
region. The proof above uses only the plane. The literal face versus
containing-plane wording is retained as an interpretive partial,
without a finding card; the final impossibility theorem and every
height comparison have the complete plane-based argument above.

## P31-1 — what is closed for the main triangle and what is separate

All31 native lines have exactly the n=3 network of P58-1. Hence
P58-3–P58-7 prove its four consistent labelings, unique standard
labeling, free boundary, and failure of even weak realizability.
This verifies the main result using the stated exercise58 route.

In the native31 drawing, its three forced crease carriers also have
an exactly nonzero homogeneous3×3 determinant; all three carriers
and the determinant are saved in the result. Thus the printed
Huffman concurrency obstruction is valid for this fixed drawing.
The valid three-plane concurrency lemma is the one already proved
in `hc-truncated-tetrahedron-030.md`, R30-4, using nonparallel
intersection lines, not merely pairwise nonparallel planes.

The stronger claim that the *nonconcurrency argument itself* excludes
every other coordinate realization of this network is kept separate:
the n=3 instance of P58-7 proves the intended non-weak-realizability
conclusion, but does not automatically prove that every alternative
drawing's three extended crease lines are nonconcurrent. That
particular printed route remains partial. No error is inferred from
having a complete alternative proof.

Bibliography is explicitly skipped here: the original1958 paper and
the assertions about its equilateral version and crack lines;
Huffman's attribution; Draper, Ernst, and Alexeev's gallery history
and item number. They are not used to establish any mathematical
claim above and are not counted as checked assertions.
