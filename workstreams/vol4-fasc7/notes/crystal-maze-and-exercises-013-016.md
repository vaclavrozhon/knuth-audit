# Crystal Maze: every relation, both models, and exercises 13–16

Source: first digital p. 6 (file 21), exercises p. 113–114 (128–129),
answers p. 159–160 (174–175). Original images, including the graph's
geometry and small vertex labels, were inspected. All relevant public
errata layers were checked. The replacement of answer 13 dated
20 August 2026 is known, applied below, and not a new finding.
Historical TV/Gardner/Gruenberger/Cohoon anecdotes and priority are
explicit bibliographic exceptions. The arithmetic 8!=40320 in that
anecdote is simply 1·2·3·4·5·6·7·8; it does not imply that a solver
needs to inspect every permutation.

## M-P01: The drawn graph and every tuple in (12) and (15)

The five horizontal edges are 12,34,45,56,78; four vertical edges are
14,25,47,58; eight diagonal edges are 13,15,24,26,37,48,57,68. These
are distinct and account for every segment in the drawing, giving
17 edges. The vertex numbering is the one shown beside the text:
top 1,2; middle 3,4,5,6; bottom 7,8. Thus the 28 possible unordered
pairs leave exactly the following 11 complement edges:

    16,17,18,23,27,28,35,36,38,46,67.

Every ordered pair in (15) is one of these edges in one orientation,
and each orientation occurs once. It has 22 tuples, with no loops.

For the letter relation, integer codes must be consecutive in letter
order (A=1,…,H=8 suffices). Of the 64 ordered pairs, eight have equal
letters and fourteen have consecutive letters, with no overlap
between those classes. The remaining 42 are exactly the pairs with
absolute code difference greater than one. All 42 printed tuples in
(12), not merely their count, were compared to this defining set;
each appears once. The saved small exact check is
`results/crystal-maze-targeted.json` and its reproduction script
`check_crystal_maze_targeted.py`. Arbitrary nonconsecutive character
encodings would require a rank conversion before using (13).

## M-P02: Equivalence of the two vertex models

In the first model x_v is the letter at vertex v. The edge constraints
forbid equal or consecutive letters at adjacent vertices. All-different
on eight variables with the common eight-letter domain makes the
assignment a permutation, hence places every disk exactly once.
Therefore its remaining restrictions are exactly the puzzle's rule.
Conversely every placement gives such a satisfying assignment. Since
the 17 edges already force unequal letters, adding inequalities on
the other 11 pairs is equivalent to adding the global all-different
constraint. This explains the printed count of extra constraints.

In the second model each letter is a variable whose value is its
vertex. All-different again makes the assignment a permutation. For
each of the seven consecutive letter pairs, (15) requires distinct
nonadjacent vertices. These are exactly the forbidden contacts in
the puzzle. Conversely every valid placement satisfies them. Taking
the inverse of the first model's permutation gives the second
model's assignment and vice versa, so their full solutions correspond
bijectively. Omitting all-different changes both models, as follows.

## E13-1: The corrected first-model count, witness, and minimality

The public replacement of answer 13 states 2624 assignments without
all-different. Here is a bounded exact decomposition, rather than a
search over 8^8 assignments. Write
A(a)={b∈{1,…,8}:|a−b|>1}. Fix the central values x_4=a,x_5=b, which
require b∈A(a). Every one of x_1,x_2,x_7,x_8 lies in L=A(a)∩A(b).
Write their values as u,v,r,s respectively. The only conditions
among these four are v∈A(u) and s∈A(r), for edges 12 and 78.
Then x_3 has precisely

    |A(u)∩A(a)∩A(r)|

choices, because its neighbors are 1,4,7; independently x_6 has

    |A(v)∩A(b)∩A(s)|

choices, because its neighbors are 2,5,8. There is no edge 36 and no
other omitted edge. Multiplying these two cardinalities and summing
over those u,v,r,s gives F(a,b); summing F over all 42 allowed central
pairs is therefore a disjoint, exhaustive count of all assignments.

For such a,b, the excluded neighborhoods together contain at least
four letters, so |L|≤4. There are at most 12 ordered unequal pairs
in L, hence at most 42·12²=6048 summands in this formula. The actual
nonempty pair domains give only 480 summands. The saved result gives
the complete 8×8 F matrix, whose row totals are

    606,66,406,234,234,406,66,606;

their sum is 2624. Each summand is a product of cardinalities of
explicit subsets of an eight-element set, so the short nice15 run
evaluates this finite proof without a large enumeration.

The corrected witness is x=(A,C,C,E,G,A,A,C). Checking the listed
17 edges shows that every difference is at least two. It is also
lexicographically smallest: x_1 cannot precede A; given that choice,
x_2 and x_3 cannot precede C because both are adjacent to vertex 1.
Their adjacency with vertex 4 makes E its earliest possible value;
adjacency with A,C,E makes G the earliest value at 5. The values A,A
at 6,7 are already smallest; vertex 8 is adjacent to those A values,
so C is its earliest value. Since this sequence extends to the full
displayed witness, each successive lower bound is simultaneously
attainable. The original claim that the 17 constraints force all
letters distinct is thus false, exactly as the known replacement
acknowledges; its removed radio-coloring assertion is superseded too.

## E13-2: The second-model count and its explicit repeated-value example

Without all-different, the eight letter variables form a walk of seven
edges in the complement H listed above. Let q_r(v) count walks of
r edges ending at v. Then q_0(v)=1 and

    q_(r+1)(v)=sum_(u adjacent to v in H) q_r(u).

The recurrence follows by deleting the last edge, a bijection with
the disjoint union of shorter walks ending at each neighbor. Seven
updates of eight entries suffice. In vertex order 1,…,8, the final
vector is

    (2931,2931,3268,1049,1049,3268,2931,2931),

whose sum is 20358. Every intermediate vector is saved in the result.
There are only 22 directed-edge additions per update. The printed
assignment A=C=E=G=1 and B=D=F=H=8 alternates along the complement
edge 18, so it satisfies all seven relations and plainly violates
all-different. This checks both the count and the example.

## E13-3: Exactly four full solutions, without an exhaustive search

With all-different, the walk just described is a Hamiltonian path
in H. The vertices 4 and 5 have degree one, with neighbors 6 and 3,
so they must be its two endpoints. Orient the path from 4 to 5.
It begins 4,6 and ends 3,5. The four remaining vertices are 1,2,7,8,
whose induced graph is K_(2,2), with parts {1,2} and {7,8}. The first
one after 6 is 1 or 7; the last one before 3 is 2 or 8.

Starting at 1, alternation makes the last one lie in {7,8}, hence
it must be 8, forcing the middle sequence 1,7,2,8. Starting at 7
similarly forces 7,1,8,2. Thus the only paths in this orientation are

    4,6,1,7,2,8,3,5  and  4,6,7,1,8,2,3,5.

Together with their reversals they give exactly four solutions. The
corresponding first-model words are CEGAHBDF, DFGAHBCE, FDBHAGEC,
ECBHAGFD. In particular exactly four of the 2624 weak assignments
satisfy all-different, as the erratum says. This also proves the
four-path assertion in the unchanged continuation on p. 160.

## E14: Both symmetry factors and the surviving solution

Left-right reflection is L=(1 2)(3 6)(4 5)(7 8), while top-bottom
reflection is U=(1 7)(2 8), fixing 3,4,5,6. The edge list is invariant
under each; they commute and generate four automorphisms. These are
all: in H an automorphism either fixes or exchanges the two degree-one
vertices 4,5, thereby fixing or exchanging 6,3. After fixing those
four, choosing the image of vertex 1 among {1,7} determines the
images of the other three vertices in their induced K_(2,2). There
are exactly two choices for each endpoint action, hence four in total.

On a placement of eight distinct letters, a nonidentity vertex
permutation cannot fix the assignment. Every orbit therefore has
four elements. L exchanges the left half {1,3,4,7} and the right half
{2,5,6,8}, so restricting A to the left half keeps exactly half. U
preserves each half and exchanges vertices 2,8. Since x_2≠x_8,
exactly one of a remaining pair has x_2<x_8. Thus the second condition
halves the count again without losing an orbit. CEGAHBDF is the unique
survivor among the four explicit solutions.

The two domain-removal instructions in answer 14 are exactly the
same left-half condition in the inverse models. The comparison
x_2<x_8 uses the letters occupying fixed vertices. The second model's
variables are fixed letters whose values are vertices, so that
comparison refers to an inverse assignment and is not the same
direct comparison of two existing variable values. The text's need
to probe deeper means this representation issue; it does not assert
that no higher-arity constraint could express the condition.

## E15-1: The exact-cover construction and the displayed option

The 64 options (v,k) each cover one vertex primary item and one letter
primary item. Exact coverage of the 16 primary items is therefore
equivalent to a bijection between vertices and letters. For each
original edge uv and consecutive pair j,j+1, the secondary item juv
appears in the four options stated in the answer. In a primary-valid
selection, two of these options can coexist only when they use
opposite endpoints and opposite letters. Those are exactly the two
ways to place consecutive letters at the ends of uv, and their
shared secondary item forbids them.

All other pairs from those four already repeat a primary vertex or
letter, so adding the secondary item introduces no additional
restriction on a primary-valid placement. Conversely every forbidden
adjacent-consecutive placement repeats its corresponding secondary
item. Thus the construction is an exact bijection with the puzzle's
solutions. There are 17·7=119 such secondary items; all-different
indeed comes from the primary cover conditions.

Vertex 2 has neighbors 1,4,5,6. Option (2,E) therefore contains the
primary items 2,E and the eight secondary items
D12,D24,D25,D26,E12,E24,E25,E26, exactly as printed. The four-solution
count follows from E13-3, independently of search-engine statistics.

## E15-2: The ordering trick, every added item, and its correctness

The four A-option deletions impose the first symmetry condition.
Neither vertex 2 nor 8 can then hold A. To impose x_2<x_8, delete
(2,H) and (8,B). The remaining alternatives are
α_i=(2,B+i), β_j=(8,C+j), 0≤i,j<6, and x_2<x_8 is exactly i≤j.

The exact referenced construction in Volume 4B answer 7.2.2.1–20,
p. 419 (`text/vol4b.txt` around line 36218), puts y_k in α_i for
k≤i<min(m,k+t) and in β_j for k−t≤j<k, where t is the lowest set
bit of k. For m=6 it gives the following complete table:

| index | α items | β items |
|---|---|---|
| 0 | none | y1,y2,y4 |
| 1 | y1 | y2,y4 |
| 2 | y2 | y3,y4 |
| 3 | y2,y3 | y4 |
| 4 | y4 | y5 |
| 5 | y4,y5 | none |

For each column β_j the α rows that share an item are exactly those
with i>j, as seen directly from this finite table. Hence the new
at-most-once constraints forbid precisely the unwanted orderings.
The option (2,E) is α_3, so it gains y2,y3 as claimed. The gadget
uses exactly five new secondary items, with no need to change any
other option. The all-primary coverage condition picks exactly one
α and one β. Therefore the symmetry-restricted construction has
exactly the one solution already derived in E14. This verifies the
particular invoked ordering construction, without claiming an audit
of every generalized case of the separate Volume 4B exercise.

## E15-3: Sharp preference versus unverified empirical counts

The precise definition of the referenced sharp preference heuristic
is in Volume 4B exercise 7.2.2.1–10, p. 125: a nonsharp primary item
can be selected only when its list has at most one option or no sharp
choice exists. Its answer gives the implementation by penalizing
the nonsharp list score. In this restricted instance every primary
list initially has at least four options: letter A has four, vertices
2 and 8 have six, and the other lists have seven or eight. Vertex 5
has seven. After renaming only 5 to #5, there is thus exactly one sharp
choice and no empty/singleton exception. The heuristic must select
vertex 5 for its first branch. This verifies the explanatory claim.

The reported 300 kilomems/485 nodes, 108 kilomems/146 nodes, and
35 kilomems/43 nodes are not independently reproduced. Their exact
values depend on the historical implementation, option/item order,
and counting conventions; the proof of solution counts does not
verify those empirical search traces. They remain an explicit partial
performance item, with no claim that they are erroneous. No historical
benchmark was restarted merely to fill that gap.

## E16: The seven edge variables, all 48/62 pairs, and reconstruction

Use seven variables e_1,…,e_7 for AB,…,GH, each ranging over the
11 unordered complement edges. For adjacent indices require exactly
one shared vertex. For nonadjacent indices require disjoint edges.
The degrees in H are (3,3,4,1,1,4,3,3). Two distinct edges can share
at most one endpoint, so the number of ordered intersecting pairs is

    sum_v deg(v)(deg(v)−1)=4·3·2+2·4·3=48.

There are 11·10=110 ordered pairs of distinct edges altogether, leaving
62 ordered disjoint pairs. Identical edges share two vertices and
belong to neither relation. This proves both printed tuple counts;
the saved check also compares the full pair partition.

For a satisfying assignment, consecutive edges are different, and
nonconsecutive edges are disjoint, so all seven selected edges are
distinct. For an interior edge e_i, its intersection with e_(i−1)
and its intersection with e_(i+1) are different endpoints: otherwise
e_(i−1) and e_(i+1) would share that endpoint, contrary to their
nonadjacent constraint. Starting at the endpoint of e_1 not in e_2
therefore orients each edge consistently into a chain. No vertex can
recur except as the shared endpoint of two consecutive edges, since
any other repetition would lie in two nonconsecutive edges. Thus it
is a simple path of seven edges and eight vertices, necessarily using
all vertices of H. Reading them in order gives A,…,H, a full puzzle
solution. Conversely the seven edges of any such Hamiltonian path
satisfy all these intersection and disjointness constraints. The
reconstruction is unique for this seven-edge sequence. This proves
both directions, the redundancy of all-different, and that this
third model also has exactly four solutions.

## Saved scope

The short exact run used nice15 once: 480 structural sum terms,
seven eight-entry walk-vector updates, the fixed ordering table, and
the finite tuple/edge-pair checks. It performed no 8^8 assignment
search, long brute force, historical benchmark reproduction, or
restart. All general model implications and the four-path count
have independent arguments above. Only the specified empirical
performance counters remain partial in this block.
