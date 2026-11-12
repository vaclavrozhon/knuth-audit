# Homomorphisms, GCP, and exercises 7–11

Source: first digital Fascicle 7, main p. 3–4 (file 18–19), exercises
on p. 113 (file 128), answers on p. 158–159 (file 173–174). The original
images for p. 3–4 and the exercises/answers were inspected. Only the portion of p. 4 above Statistical
mechanics is closed by this note. Formulas (9) onward are a separate block.
The source text loses several primes and nonequality signs; conclusions
below use the images, not those OCR substitutions.

Finite graphs are simple and undirected unless explicitly described as
digraphs. In particular, an ordinary graph is loopless, as specified at
the start of p. 3. External complexity theorems are identified separately
from the arguments proved here. Bibliographic priority for Jeavons,
Feder–Vardi, and Codd, and the database textbook citation, is not audited.

## G-P01: Relations, coloring, cliques, and embeddings

A digraph with vertex set V and arc set A is exactly a binary relational
structure (V,A): each arc is an ordered pair, including a possible loop.
A symmetric, irreflexive relation E instead pairs the two orientations
of each unordered two-element edge. Passing in either direction recovers
the same ordinary graph. There are no hidden multiple edges in this
set-based representation.

For the complete loopless graph K_d, an ordered pair is an edge exactly
when its entries differ. Thus h:G→K_d preserves edges exactly when the
endpoints of each edge of G have different labels in {1,…,d}. This is
proper d-coloring, including unused colors. Conversely, for h:K_d→G,
each distinct i,j is adjacent in K_d, so h(i),h(j) are adjacent in G.
Since G has no loop, h(i)≠h(j). The d images are distinct and pairwise
adjacent, hence form a d-clique. Every such clique, with any enumeration,
gives h. The d=0 case is the unique empty map and empty clique; d=1
requires a vertex of G and imposes no edge condition.

For structures with the same ordered list of arities, preservation means
applying the same function componentwise to every tuple in each source
relation, and requiring the resulting tuple in the corresponding target
relation. Preservation of the extra relation ≠ is exactly injectivity:
every unequal source pair must have unequal images. With the edge
relation also preserved, restriction of h to its image is a bijection
from G onto the subgraph whose edges are exactly the images of G's edges.
Extra edges of the target can be omitted in this subgraph. Thus this is
an embedding as a subgraph, not necessarily as an induced subgraph.
For C_n (n≥3), distinct vertex images and all n cyclic edges give the
claimed n-cycle. Both the injectivity condition and the cycle claim
need this augmented structure; ordinary homomorphisms alone do not
give them, as exercise 7 illustrates.

## G-P02: The constant relation and the known reachability correction

A relation containing exactly one k-tuple requires the image of that
particular tuple to belong to the corresponding target relation. This
includes k=0: the unique nonempty nullary relation consists of ε.

The printed directed example is already corrected by the public erratum
dated 20 August 2026, replacing (V,A) by an undirected graph (V,E) and
using different connected components in the converse. See
`sources/err4f7-2026-11-06.textxt`, lines 282–292; the shared original and
public errata layers were checked. This is not a new finding.

For the corrected structures (V,E,{ab}) and ({0,1},=,≠), an edge uv
forces h(u)=h(v). Induction along any path therefore makes h constant
on a component. The singleton source tuple ab forces h(a)≠h(b), so
a,b must be in different components. Conversely, if their components
are different, put 0 on a's component, 1 on b's, and choose either label
on each remaining component. This map preserves both relations. If
a=b, no such map exists and the zero-length path makes b reachable,
as required. Isolated vertices are components too. In the original
digraph formulation equality propagates against arc orientations as
well, which is precisely why one-way nonreachability was insufficient.

## G-P03: CSP to GCP, including the printed structures (7)–(8)

Let a finite CSP have variables 1,…,n, domains D_i, and constraints
R_j(x_i1,…,x_ik). Choose a target universe U′ containing all D_i and
all relation entries; the union of those finite sets suffices. Use
source universe {1,…,n}. For each i add a unary source relation {i}
and target relation D_i. For each constraint add a source relation
containing the single index tuple (i1,…,ik), with target relation R_j.
Every source relation is constant. Repeated indices in a scope cause
no problem: the repeated coordinate is sent to the same value.

Given a homomorphism h, the unary relations give h(i)∈D_i and each
constraint relation gives R_j(h(i1),…,h(ik)). These are exactly the
CSP conditions. Conversely, a satisfying assignment defines h(i)=x_i
and preserves every relation just listed. The two constructions are
inverse, so this is a bijection, not merely equivalence of existence.
An empty domain precludes both maps and solutions. If n=0, the empty
assignment/map exists precisely when all included nullary constraints
are true. A true source nullary relation forces its target to be true.

For (7)–(8), the five unary source relations are {1},…,{5}; the three
remaining source tuples are 135,14,245, of arities 3,2,3. Their respective
targets are exactly D_1,…,D_5 and R_1,R_2,R_3 of (1)–(2). A…Z is an
adequate target universe. Consequently h(1)…h(5) is precisely the
original five-letter CSP word. This verifies every relation slot in
the displayed example; the two solutions were already proved in
`csp-opening-and-exercises-001-006.md`, section C-P01.

## G-P04: Exercise 11, the converse construction

For finite similar structures S=(U,R_1,…,R_t) and
S′=(U′,R′_1,…,R′_t), create one variable x_u per u∈U, each with domain
U′. For every tuple (i1,…,ik)∈R_j impose
R′_j(x_i1,…,x_ik). If h is a homomorphism, x_u=h(u) satisfies all of
these constraints by definition. Conversely, a satisfying assignment
defines a function U→U′ preserving every source tuple, hence h.
Again the transformations are inverse.

An empty source relation imposes no constraint; it does not require
the corresponding target relation to be empty. A repeated coordinate
in a tuple becomes a repeated occurrence of the same variable. A
nullary source relation is either empty (no constraint) or {ε} (the
target nullary truth value must hold). If U is empty, these nullary
tests are all that remain. If U is nonempty and U′ empty, every domain
is empty, correctly making a homomorphism impossible. These cases
also verify that the construction does not tacitly assume positive
arity or nonempty universes. No complexity claim is made in the text;
with explicit tuples the construction adds one constraint per source
tuple and copies its index list.

## G-P05: The database table and natural join

Use the following per-attribute bijections: basement↔B, solarium↔S;
Chris↔C, Logan↔L; Alice↔A, Iris↔I, Udo↔U; test↔E, code↔O;
deutsch↔D, norsk↔N. The three Departments rows become BAN,BUD,SIN
in coordinates 135. Layout becomes BE,SE,SO in coordinates 14.
Personnel becomes COD,CON,LED in coordinates 245. These are exactly
the three printed relations in (2). No duplicate row or attribute is
lost by these bijections.

By definition the natural join consists of full five-attribute tuples
whose restrictions to each table's attributes are rows of that table.
Thus it is exactly the same conjunction as this CSP. The previously
proved words BLUED and SCION decode to
(basement,Logan,Udo,test,deutsch) and
(solarium,Chris,Iris,code,norsk). The exact earlier elimination proof
in section C-P01 of the preceding note excludes every other row; it is
reused rather than rerun. This verifies both the table correspondence
and the implied complete answer to its question.

## E7: Odd closed walks versus specified cycles

Enumerate C_9 cyclically as vertices 0,…,8 and map them, in that order,
to 0,1,2,3,4,3,4,3,4 of C_5. Every consecutive difference is ±1
modulo 5, including the last-to-first step 4→0. This checks all nine
source edges. C_5 has no 9-cycle because it has only five vertices,
and no 3-cycle because neither neighbor of a vertex is adjacent to
its other neighbor. Therefore the assertion is false.

The image of any odd cycle under a graph homomorphism is an odd closed
walk. If it has a repeated vertex before the final return, split at
two occurrences: the two resulting closed walks have lengths summing
to the original odd length, so one is odd and strictly shorter.
Repeat until there is no such repetition. Termination follows from
strict decrease of positive length. The result is an odd simple cycle;
the loopless hypothesis rules out length one. A graph with an odd
cycle cannot be bipartite because alternating two side labels around
that cycle returns the wrong label. This proves every assertion of
answer 7. There is no specified 3- or 9-cycle guarantee.

## E8: The three-edge replacement and the external dichotomy

Construct G* by replacing each edge uv by u—uv—vu—v with two fresh
vertices private to that edge. Work modulo 5 on C_5. A walk of length
3 takes three steps from {−1,+1}, so its total displacement is one of
−3,−1,1,3. These residues are precisely the four nonzero residues
modulo 5. Thus its endpoints differ; conversely every pair of distinct
vertices of C_5 can be joined by such a three-step walk. For instance,
displacements 1,−1,3,−3 use steps (+,+,−),(−,−,+),(+,+,+),(−,−,−).

Given G*→C_5, restricting the map to the original vertices gives
different labels to the ends of every original edge, hence G→K_5.
Given G→K_5, regard its five labels as C_5 vertices and choose one of
the above walks for each edge. Its two private internal vertices can
be assigned independently of every other edge, giving G*→C_5. This
is exactly the printed equivalence, with the prime restored from the
original image. The construction uses |V|+2|E| vertices and 3|E| edges
and takes O(|V|+|E|) time with adjacency lists. It is therefore a
polynomial reduction from 5-colorability. A proposed map to fixed C_5
can be checked by scanning all vertices and edges, which proves NP
membership. Isolated vertices impose no edge condition; the empty
graph has the empty map in both directions.

External dependency: the precise finite-template theorem is
Hell–Nešetřil, Theorem 1, JCT B 48 (1990), 92–110. The original PDF was
not obtainable in the brief retrieval attempt. A primary new proof
states the identical theorem as Theorem 1.1 in Meyer–Opršal,
[arXiv:2409.12627v2](https://arxiv.org/html/2409.12627v2), with the finite
graph convention in Section 2 and the fixed-template definition in
Section 2.1. It gives NP-completeness for a fixed nonbipartite loopless
undirected H. K_5 and C_5 satisfy these hypotheses. This supplies the
5-colorability premise and matches the general hardness assertion in
answer 8. This external dichotomy is not claimed as independently
re-proved here. Source bytes, version, retrieval failures, hash and
exact locations are in `sources/hell-nesetril-manifest.json`.

For completeness, the printed easy side has its own argument. If a
fixed bipartite H has an edge, G→H holds exactly when G is bipartite:
compose with a bipartition H→K_2 in one direction; map G's two sides
to the chosen H edge in the other. Two-color propagation, starting
each unvisited component arbitrarily, visits every vertex once and
scans every edge at most twice. A conflicting edge makes alternating
labels impossible along its component, so no two-coloring exists;
without a conflict the resulting coloring is valid. This is linear.
If H has vertices but no edge, the answer is exactly whether G has
no edge; if H has no vertices, it is exactly whether G has no vertices.
These boundary templates are also polynomial. Ordinary graphs in
F7 are explicitly irreflexive, so the external theorem's additional
polynomial case of a looped H lies outside the printed assertion's
scope. No missing-loop counterexample is being asserted.

## E9(a): Independent set

For distinct u,v, define complement adjacency to mean uv∉E. A set of
k distinct vertices is independent in G exactly when all its distinct
pairs are edges of the complement. By G-P01 this is exactly a
homomorphism K_k→complement(G). Injectivity follows from the
complement's lack of loops. This also handles k=0 and k>|V|. Negative
k is not a set size and can be rejected before constructing a graph.

## E9(b): Vertex cover

C⊆V hits every edge iff no edge has both ends in V\C, iff V\C is
independent. For finite V, |C|=k iff |V\C|=|V|−k. Applying E9(a) to
that size therefore gives the exact-size cover problem, including k=0
and k=|V|. A requested size outside 0,…,|V| is impossible and is
rejected directly. This proves the printed complement-of-cover step.

## E9(c): Isomorphism and the single GCP

If each finite graph embeds in the other, the injections force equal
vertex counts; the induced injections of their finite edge sets force
equal edge counts. One embedding is then bijective on vertices and
maps E injectively onto a subset of E′ of equal size, hence onto all
of E′. It therefore preserves both edges and nonedges, and is an
isomorphism. An isomorphism and its inverse plainly give both
embeddings. Finiteness is essential to the counting argument.

For equal vertex counts, a map preserving E and its irreflexive
complement is injective: each distinct pair belongs to one of those
relations, and its image must remain distinct. It is consequently a
bijection. Preservation of both relations gives the required edge
biconditional; conversely an isomorphism preserves both. Thus the
printed pair (V,E,complement(E)) and (V′,E′,complement(E′)) is one
GCP with exactly the required solutions. For unequal counts reject
immediately (or output a fixed unsatisfiable GCP); the case of two
empty graphs gives the empty isomorphism. No assumption that a
general embedding already preserves nonedges was used.

## E9(d): Bandwidth and normalization of labels

The parenthetical question defines bandwidth at most the nonnegative
integer k. Given distinct integer labels h(v), sort them as
t_1<…<t_n and replace t_i by i. For i<j, integrality gives
t_j−t_i≥j−i, so this rank replacement cannot increase any edge's
absolute label difference. Hence a feasible integer labeling exists
iff one using exactly {1,…,n} exists. Such a labeling is a bijection
to the vertices of the target graph with distinct i,j adjacent iff
|i−j|≤k, and it preserves edges exactly when the bandwidth conditions
hold. Conversely any embedding into that n-vertex graph provides
the required labeling. The implicit i≠j is the ordinary-graph
convention established on p. 3; loops would in any event be irrelevant
to an injective map from a loopless graph. For k=0 this target has no
edges, correctly accepting exactly edgeless graphs. n=0 uses the empty
map. This proves the omitted normalization step as well as the model.

## E9(e): Eulerian trail under Knuth's closed-trail convention

For m=|A|>0, let the vertices of the target structure be the individual
arcs uv∈A; restrict the displayed successor relation A′ to A×A.
Then (uv,u′v′)∈A′ exactly when v=u′. An injective map from the m
indices of the oriented cycle into this m-element set is a permutation
of all arcs. Preserving O requires each consecutive arc's head to be
the next arc's tail, including last-to-first. The mapped sequence is
therefore a closed walk using every arc exactly once. Conversely,
enumerating such a walk gives an injective map preserving O and ≠.
This proves both directions and the role of each displayed relation.
When m=1, the source O has its self-loop and the construction accepts
precisely when the sole arc is itself a loop, as a closed trail requires.
Extra isolated vertices of the original digraph do not matter.

The closure requirement is consistent with Knuth's terminology:
Volume 1 §2.3.4.2, p. 374 explicitly requires fin(e_m)=init(e_1) in its
definition of Eulerian circuit, and the 15 July 2004 public erratum
changes that term to Eulerian trail starting with the 17th printing.
The subsequent 2008 walk/path terminology correction does not remove
closure. The local sources are `text/vol1.txt` around line 23102 and
`errata/text/all1-prepre.txt` around lines 1130–1140. Thus a one-way
single arc is not a counterexample under this established convention.

Empty boundary remains explicit: for m=0 the source universe is empty
and O can be read as an empty relation, without evaluating a modulo-zero
term. The homomorphism test then answers yes for an arc-free graph.
That agrees with a convention permitting an empty Eulerian traversal.
The cited nonempty sequence definition does not settle the empty graph
convention, so this degenerate interpretation is recorded as partial,
not as a confirmed error or a new finding card.

## E10: Coordinate-disjoint tuples and its nullary boundary

For k≥1, a map h:V→R preserves the two displayed relations iff for
each pair u≠v the k coordinates of h(u),h(v) differ pairwise in the
same positions. Hence the |V| selected tuples are distinct and
coordinate-disjoint. For any fixed coordinate j, their |V| entries
belong to V and are pairwise distinct, so they use every element of
V exactly once. They form a perfect matching between the k labeled
copies of V, using only tuples in R. Conversely, enumerate the
|V| tuples of such a matching by V; this gives precisely the required
homomorphism. This proves the k-dimensional matching interpretation
and the implicit distinctness/exhaustion arguments. V=∅ has the
empty matching and map; when V≠∅ and R=∅ neither exists. For k=1
the condition simply requires R=V and h is a permutation.

For k=0 the relation “unlike” is vacuous and therefore reflexive on
{ε}; the same injectivity argument is unavailable. If R={ε}, a
homomorphism exists for every V, even |V|>1, by assigning ε repeatedly.
If R=∅ it exists only for empty V. The standard positive-dimensional
matching interpretation has thus been proved with its exact k≥1
assumption. Applying the printed distinct-tuple interpretation at k=0
would require an additional convention; it remains a separate partial
scope item, not a new finding. The ordinary kDM result is unaffected.

## Errata and scope ledger

All relevant public layers for p. 3, 113, 158 and 159 were consulted,
including the current primary TeX source. The p. 3 correction is
incorporated as a known correction. The p. 158 correction to answer
2(b) belongs to the prior block. The p. 113/159 changes for answer 12,
and p. 159 replacement of answer 13, belong to the following blocks.
There is no erratum for exercises 7–11 in those layers. No new finding
is opened here, and no numerical or brute-force experiment is needed
for these proofs.
