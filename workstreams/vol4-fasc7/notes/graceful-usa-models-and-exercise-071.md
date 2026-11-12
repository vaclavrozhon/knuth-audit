# Main p18--19: every USA entry, both models, complete graphs, and stars

Original F7 p18--19/file33--34 and answer71 at p174/file189 were
displayed. The earlier USA diagram, Volume4A p15/file32, was also
displayed at full readable resolution, with all49 postal-code
positions matched to Fig.106. The mathematical certificates are
`check_graceful_usa_and_families71.py` and
`results/graceful-usa-and-families71.json`. These checks perform no
graceful search and no restart. A follow-up5671-pair segment check
uses the saved graph, without repeating the earlier arithmetic.

The primary adjacency data were downloaded from
[Knuth's contiguous-usa.dat](https://www-cs-faculty.stanford.edu/~knuth/contiguous-usa.dat),
linked by his [GraphBase page](https://www-cs-faculty.stanford.edu/~knuth/sgb.html).
The exact local file and SHA256 are recorded. This is an exact
comparison with the mathematical example; it is not a new survey
of real state boundaries. Historical attribution to Rokicki in
October2020 was not independently researched. Exercise102's general
randomized algorithm and performance remain for its later block,
rather than being considered proved by the one displayed solution.

## G18-1 — two elementary obstructions

A graceful labeling is an injection V→{0,…,m}. Hence |V|>m+1
makes one impossible by the pigeonhole principle, whether or not
the graph is described as disconnected. This includes m=0 and
several isolated vertices.

For C5, orient the cycle and telescope the signed vertex differences:
their sum is0. Modulo2, changing a sign does not change an integer,
so their absolute differences must have an even sum. A graceful
labeling would instead give sum1+2+3+4+5=15. This contradiction
proves the stated impossibility without enumeration. No general
cycle sufficiency theorem is inferred from this parity condition.

## G18-2 — all49 native values and all107 native edges

The exact Fig.106 SVG has49 vertex ovals and106 straight paths;
one straight path contains two edges, giving107 edges in total.
Every path endpoint is matched to its grid vertex with squared
residual below1/10000pt². All49 vertices are distinct, all107
unordered edges are distinct, and the named edge set equals the
107-edge primary GraphBase data exactly.

Here is the entire displayed assignment, in source grid rows:

    ND58 VT33 NH83 ME27
    WA59 MT53 SD6 MN97 WI93 MI23 NY64 MA9
    OR41 ID26 WY106 NE107 IA48 IL11 IN55 OH84 PA62 NJ90 CT16 RI78
    CA31 NV98 UT86 CO0 KS104 MO2 KY95 WV19 MD92 DE24
    AZ15 NM103 OK25 AR66 TN101 VA5 DC56
    TX8 LA100 MS3 AL88 GA7 NC82
    FL96 SC28.

Thus the49 vertices are the48 contiguous states and DC. The
locations and all named adjacency lines agree with the original
4A diagram. The complete edge/endpoint/difference list is saved.
Every one of the107 printed equalities is separately parsed and
checked: its subtraction is correct, its two values name an actual
native edge, and the result list is exactly1,…,107. Conversely,
every native edge occurs once in that table. The49 vertex values
are distinct and lie in0,…,107. These facts prove gracefulness,
not merely the correctness of selected table entries.

Restricting the native graph to the13 vertices of Fig.105 produces
exactly the18 edges already proved in the previous note. Thus
Fig.105 is indeed the stated **induced** subgraph: no additional
edge between those13 vertices is silently discarded.

The literal source grid has no unwanted crossings or overlaps,
as checked for every one of the5671 pairs of segments by integer
orientation determinants and bounding intervals. Shared endpoints
are allowed, but coincident positive-length rays are excluded.
Every directed edge is then followed in the exact cyclic order,
producing60 face walks, with49−107+60=2. The outer walk contains
the consecutive path

    CA OR WA ID MT ND MN WI MI OH PA NY VT NH ME.

This gives the15 states on the upper/western **drawn graph** border.
It is not a claim that every member individually shares a modern
international land boundary. Their consecutive two-digit labels
are31,41,59,26,53,58,97,93,23,84,62,64,33,83,27.

## G18-3 — a rigorous30-digit check, not a copied decimal

Their concatenation is314159265358979323846264338327. To verify
that this is the first30 digits of π, including its integer3,
let a=arctan(1/5),b=arctan(1/239). The tangent double-angle formula
gives tan(2a)=5/12 and tan(4a)=120/119. Consequently

    tan(4a−b)=(120/119−1/239)/(1+120/(119·239))=1.

The alternating first two terms of arctan show4a−b>0, while
4a−b<4/5. Also π/2=2arctan(1)>1, by integrating
1/(1+x²)>1/2 on0≤x<1. Thus4a−b lies in the principal interval
and equalsπ/4. This proves Machin's identityπ=16a−4b here.

For each arctangent, the alternating series has strictly decreasing
term magnitudes. Its partial sum and the partial sum with one more
term enclose its exact value. Use25 terms for1/5 and8 for1/239;
combine lower/upper endpoints with the correct sign of−4b. Both
resulting rational bounds, multiplied by10^29, have integer part
314159265358979323846264338327. Therefore every claimed digit is
certified. The rational endpoints are saved; no floating-point
rounding or external decimal source enters this check.

## G18-4 — direct CSP, including isolated vertices

Give one variable to each vertex, domain0,…,m, and one to each
edge, domain1,…,m. The edge constraint equates its variable with
the absolute difference of its endpoints. Impose all-different
separately on all vertex variables and all edge variables.

Any satisfying assignment restricts to an injective vertex labeling
with distinct edge differences, hence a graceful labeling. Conversely
a graceful labeling determines every edge variable uniquely and
satisfies all constraints. This is a bijection. Isolated vertices
remain genuine vertex variables and are included in all-different.
For m=0, an empty graph has its empty assignment and K1 has label0;
two or more isolates are rejected. Thus the model itself needs no
missing-isolate convention. The qualitative comparative speed
claims on p19 are not established by this logical equivalence.

## G19-1 — reverse model and the exact limit of C0002

For every d=1,…,m, LO[d] chooses one of0,…,m−d and requires
NAME[LO[d]]--NAME[LO[d]+d] to be an edge. Defined NAME entries are
distinct actual vertices; '?' is not an endpoint of any graph edge.
Thus the two ends of each chosen edge are defined and distinct.

The m edges so obtained are all different. If two choices named
the same graph edge, its two endpoint names would occur at the
same two label positions, by injectivity of defined NAME values;
their difference would therefore be the same d. Since G has m
edges, the choices exhaust its edge set. Every nonisolated vertex
consequently appears. If G has no isolated vertices, this gives
exactly one label to every vertex, and its inverse NAME/LO arrays
are uniquely determined by the graceful labeling. This proves
the model bijection on that domain.

For arbitrary G, suppose the preceding necessary condition
n≤m+1 is enforced first. Let r be the number of nonisolated
vertices and k the number of isolates already placed by NAME.
The remaining n−r−k isolates can be placed injectively into the
m+1−r−k unused label positions because n≤m+1. This changes no
edge or difference. Therefore **after that precheck, satisfiability
of the printed reverse constraints is equivalent to existence of
a graceful labeling**, even with isolates. This is a full extension
argument, not just an example suggesting a repair.

The literal model still is not a bijection on graphs with isolates:
for a triangle plus one isolate, the unused label can be '?' or
the isolate name, giving two model assignments that complete to
the same graceful vertex labeling. Without the size precheck,
one edge plus two isolates is the original false-positive witness.
Requiring every vertex name to appear exactly once gives a direct
bijective repair. Alternatively one can precheck and explicitly
enumerate completions of missing isolates with a fixed convention.

Page23 explicitly treats unused labels as absent or isolated
vertices in its different all-graphs enumeration. That supplies
context for an implicit convention but does not itself specify
the reverse CSP's handling of named isolates. C0002 therefore
remains candidate/interpretation, with its decision-level objection
now sharply limited. No claim of a faulty concrete implementation
is made, and no new finding is introduced.

## G19-2 — largest domains and complementation

The LO[d] domain has m−d+1 values. In particular LO[m]=0 for
m≥1, and LO[m−1]∈{0,1} for m≥2. The provedE70 formula gives

    LO'[m−1]=m−(m−1)−LO[m−1]=1−LO[m−1].

Thus exactly one of a complementary pair has LO[m−1]=0, and this
restriction loses no equivalence class. The domains' small size
for large d is a literal count; improved overall running time
does not follow as a theorem from that count alone. At m=0 or1
the m−1 normalization is not invoked.

## G19-3 — all four small complete graphs and their uniqueness

In Kn there are m=n(n−1)/2 edges. By injectivity of defined names,
any two distinct real-label positions name distinct vertices,
which are adjacent; therefore constraint36 says exactly that both
positions are real. Vertex names can then be permuted arbitrarily,
an automorphism of Kn. The following unique label sets are thus
unique up to the already specified equivalence.

For n=1, m=0 and the only vertex label is0. For n=2, the unique
difference1 edge forces labels{0,1}. For n≥3, the top two normalized
edges force real labels0,m−1,m. At n=3 these are{0,2,3}, with
LO[3]=0,LO[2]=0,LO[1]=2; all three differences occur.

The remaining case has n≥4, so m≥6. The difference m−2 edge is
one of{0,m−2},{1,m−1},{2,m}, and each now introduces one new real
vertex. For n=4, m=6, the three possible sets are{0,4,5,6},
{0,1,5,6},{0,2,5,6}. The first two have no pair of difference3,
so they cannot supply LO[3] without a fifth vertex. The third has
all six differences, respectively from pairs5--6,0--2,2--5,2--6,
0--5,0--6. Hence its LO array is(LO[1],…,LO[6])=(5,0,2,2,0,0).
This closes each printed branch, not only the final K4 example.

## E71 — every forced branch and every final exclusion for n≥5

Now m=n(n−1)/2≥10. Of the three four-vertex possibilities just
derived, {0,m−2,m−1,m} has two edges of difference1 among its
last three vertices. Likewise {0,1,m−1,m} has two difference1
edges,0--1 and(m−1)--m. Completeness of Kn forces all these
edges, contradicting distinct differences. The only remaining
four labels are therefore{0,2,m−1,m}.

Their forced pair{2,m−1} supplies difference m−3, so LO[m−3]=2.
The next difference m−4 has only these five lower-end choices:

|Lower end|Proposed pair|Reason for exclusion, when excluded|
|---:|---|---|
|0|0,m−4|The only remaining possibility|
|1|1,m−3|New1 creates0--1, duplicating the existing difference1|
|2|2,m−2|New m−2 creates(m−2)--(m−1), duplicating1|
|3|3,m−1|New3 creates2--3, duplicating1|
|4|4,m|New4 creates2--4, duplicating the existing0--2 difference2|

Hence LO[m−4]=0 and label m−4 is real. At m=10 this already
produces an extra duplicate difference4, but no special shortcut
is required. The next difference m−5 has these six possibilities:

|Lower end|Proposed pair|Forced duplicate|
|---:|---|---|
|0|0,m−5|(m−5)--(m−4) duplicates difference1|
|1|1,m−4|0--1 duplicates difference1|
|2|2,m−3|(m−4)--(m−3) duplicates difference1|
|3|3,m−2|2--3 duplicates difference1|
|4|4,m−1|2--4 duplicates0--2, difference2|
|5|5,m|2--5 duplicates(m−4)--(m−1), difference3|

These alternatives cover the complete domain0≤LO[m−5]≤5.
All named inequalities and distinctions hold for m≥10, including
the smallest n=5 case. Consequently there is no possible LO[m−5]
and no graceful labeling of Kn for n≥5. This verifies the entire
printed proof, including its omitted final six-case explanation.

## G19-4 — every star and the graceful-permutation definition

K1,n has n+1 vertices and n edges, one center joined to every leaf.
For n>1, the normalized edges{0,n} and{0,n−1} make vertex0 have
at least two neighbors. Only the center can do so; hence0 is the
center. Every remaining edge then joins it to its own difference
d, so LO[d]=0 for all1≤d≤n and the leaves use exactly1,…,n.
Permuting the leaves is an automorphism, giving a unique equivalence
class. K1,1=K2 has already been closed; if n=0 is allowed, it is
K1, also already closed. This supplies both existence and uniqueness.

For Pn, n≥1, m=n−1 and its n distinct vertex values in0,…,n−1
must be a permutation. Its edges are exactly consecutive path
pairs, so gracefulness is equivalent to their absolute differences
being a permutation of1,…,n−1, exactly(37). At n=1 the difference
sequence is empty and the sole permutation0 is valid. The path
algorithms and their subsequent examples require their own next
block; this definition alone does not verify them.
