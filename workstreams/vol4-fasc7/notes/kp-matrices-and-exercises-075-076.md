# KP matrices and exercises 75–76

Original p20–21/files35–36, questions75–76 at p120/file135, and
answers p175–176/files190–191 have been displayed. This block
checks all entries and differences of both matrices(39), the KP
automorphism assertion, every step of the corrected75 answer,
and the corrected canonicalization procedure in76. It does not
claim that Fig107 or the remaining p176 answers are checked.

Known corrections are applied, not reported as findings:

* 13September2026 replaces(40) by the first-column ordering and
  **all n** comparisons x11<xir, 1≤i≤n.
* 4September2026 changes the75 recurrence from m−2d+2 to m−2d.

Both public errata text extractions and the original errata TeX
contain these corrections. The remaining conventions below stay
explicitly partial. No new finding card is created by this block.

`check_kp_matrices39_and_exercise75.py` produces
`results/kp-matrices39-and-exercise75.json`. Its sole small run
took under0.2s at nice15. It checks the two given matrices and
fixed-cardinality subsets only for n≤5; it does not perform a
general graceful-labeling census.

## KP-1 — vertex and edge counts, including the r=2 simplification

The vertices of Kn□Pr are pairs(i,j), 1≤i≤n, 1≤j≤r. For each j,
every pair of different i values is adjacent; for each i, adjacent
j values are adjacent. These edge families are disjoint. Thus
there are nr vertices, r·n(n−1)/2 column edges and (r−1)n row
edges, totaling m=r·n(n−1)/2+(r−1)n. At r=2 this is
n(n−1)+n=n². The stated KP scope n>2,r>1 is used throughout.

Every graph labeling has exactly the n×r matrix representation
xij=l(i,j). The vertex-injectivity, range0,…,m, column differences,
and consecutive-row differences express exactly the original
gracefulness constraints, in both directions.

## KP-2 — every entry and difference of both matrices(39)

The source matrices are transcribed in the checker, with75 vertex
values in total. The left40 values are distinct and within[0,96];
the right35 values are distinct and within[0,100]. For each of
the17 columns the certificate lists every unordered row pair,
its two labels and its difference; for each of the9 rows it lists
every consecutive column pair likewise. It checks every one of
the196 edges, not a sample or only the displayed examples.

The left column differences, column by column, are:

    1 91 95 90 94 4
    93 87 68 6 25 19
    9 83 69 74 60 14
    28 86 81 58 53 5
    84 72 50 12 34 22
    76 40 73 36 3 33
    51 7 71 44 20 64
    63 16 55 47 8 39
    59 29 46 30 13 17
    26 15 57 11 31 42.

The left row differences are:

    96 92 89 88 85 79 77 66 62
    2 10 52 24 75 48 37 56 23
    82 78 80 70 27 32 54 21 18
    67 45 61 43 38 65 49 35 41.

Together these are exactly1,…,96. In particular the printed
first-column list{1,91,95,90,94,4} and first-row list
{96,92,89,88,85,79,77,66,62} each agree term by term.

For the right matrix, its7 columns contribute70 edges and its5
rows30. Their complete lists in the certificate exhaust1,…,100
once each. Thus both displayed matrices are graceful, independently
of any canonical-form claim. The counts60+36 and70+30 follow
both from the formula and from the full listed edge families.

## KP-3 — the complete automorphism group and the factor4n!

An edge inside a column lies in a triangle since n≥3. An edge
between columns has no common neighbor: a vertex adjacent to its
two endpoints would have to belong simultaneously to incompatible
row/column positions. Therefore the edges lying in triangles are
exactly the column edges. Their connected components are the r
columns, so every automorphism permutes columns and induces an
automorphism of the quotient path Pr. That quotient action is
either identity or reversal: an endpoint image determines the
whole path successively.

Between any two adjacent columns the edges form the matching
(i,j)–(i,j+1). Hence their row permutations must be identical.
Connectedness of Pr forces one common row permutation for all
columns. Conversely every common permutation and either column
orientation preserve all edges. These2n! maps are distinct and
exhaust the automorphism group, including r=2 and n=3.

All these graphs have m>1. The already closed E68 argument in
`graceful-colonies-and-exercises-067-070.md` applies: injectivity
makes distinct automorphisms give distinct labelings, while an
automorphism inducing complement would swap the unique possible
m−1 edges{0,m−1} and{1,m}, contradicting uniqueness of their
difference. Thus the commuting complement doubles the orbit to
exactly4n!, with no stabilizer exception here.

## E76 — all steps and uniqueness for the corrected(40)

The edge of difference m is{0,m}. The edge of difference m−1
is either{0,m−1} or{1,m}, never both. Complement interchanges
the two cases. Consequently exactly one choice of complement
has0 adjacent to m−1; row permutations and column reversal do
not change that choice. This proves the first printed instruction,
including the case where label1 is absent (then1–m is false).

The two end columns have different minima, because all vertex
labels are distinct and the columns are disjoint. Reflect exactly
when the left minimum is larger. This chooses the unique column
orientation whose left minimum is smaller than every entry of
the right column. Finally sort rows by their first entries; the
distinct entries determine one unique permutation. The resulting
x11 is the left minimum, the first column increases, and all n
corrected inequalities x11<xir hold.

Conversely any equivalent matrix obeying the m−1 normalization
must have that same complement choice. Its first-column order
makes x11 its left minimum, so the n inequalities choose exactly
the same column orientation. Its row order is then forced.
Existence and uniqueness both follow. The procedure terminates
after at most one complement, one reversal, and one finite sort.
A direct implementation costs O(nr+n log n) comparisons/word
operations and O(nr) storage including the matrix; no numerical
performance claim from the book is inferred from this bound.

The original single comparison x11<x1r is insufficient. In the
right matrix(39), the left minimum is10, the right minimum8, but
x11=10<93=x1r. Reflect and sort rows to obtain first-column
entries8,24,59,71,93; its first row ends in81, so it also satisfies
the original condition. This is precisely the known(40) error,
not a new finding.

## KP-PARTIAL — the two nearby prose conventions

The left matrix(39) satisfies corrected(40). The right original
matrix does not:10 is not less than the right-column entry8.
The corrected algorithm instead gives its reflected, sorted
version, recorded explicitly in the certificate. The adjacent
sentence saying that both printed matrices are canonical is
therefore stale when the known correction is applied. Its exact
editorial treatment is left partial; the gracefulness witnesses
and the corrected theorem do not depend on it.

The optional phrase “0 and m−1 occupy the same column” is also
stronger than the proven universal normalization. In the right
matrix,0 is in column4 and99 in column3;100 is in column5 and1
in column3. Every automorphism preserves equality of columns,
and complement changes the pair(0,99) to the old(100,1). Neither
pair shares a column. Thus that condition cannot select a
representative from this orbit. It is harmless if intended as
a restriction to a subclass of solutions; no universal
canonicalization claim for that optional subclass is accepted.
This wording remains partial, with no new card.

## E75-1 — the model and exact quotient by equivalence

For n≥1, K1,1,n has two apex vertices joined by one edge and
n other vertices each joined to both apices. Thus m=2n+1.
The unique0–m edge contains an apex. If its zero endpoint is a
leaf, complement puts zero at an apex; swap the two apices if
necessary. We may therefore label them0,d, 1≤d≤m. Let S be
the set of n leaf labels. All labels are distinct, so S avoids
0,d, and the m edge differences are exactly

    S, {|k−d|: k∈S}, {d}.

They must form a disjoint partition of{1,…,m}. Conversely that
partition, together with |S|=n, gives exactly a graceful labeling.
The first two vertex parts have no other constraints. Permuting
the n leaves changes only their names, so a set S represents
their entire permutation orbit.

When n>1 the apices have degree n+1, and leaves have degree2.
Every graph automorphism preserves the two classes, permutes
leaves arbitrarily, and may swap apices. After zero is placed at
an apex, a complementary canonical description is possible only
when the old label m is also an apex, namely d=m. Otherwise its
new zero is a leaf and no automorphism can move it to an apex.
For d=m, complement followed by swapping apices sends S to m−S.
Exactly one of those two sets omits1: S contains exactly one of
1,m−1. This proves the printed extra condition1∉S when d=m.

At n=1 the graph is K3, so the apex/leaf degree distinction fails.
The parameterization with its stated d=m convention gives three
descriptions: (d,S)=(1,{3}),(2,{3}),(3,{2}). All are equivalent
by a triangle permutation and/or complement, and K3 has just
one graceful class by the already closed small-complete-graph
argument. This explains the exceptional subtraction2[n=1].

## E75-2 — every terminal case of the recurrence

We use the intended fixed cardinality |S|=(m−1)/2, for any odd
m≥1. The auxiliary m=1 case has S=empty,d=1; it is needed for
the recursion, without extending the exercise's n≥1 quotient.

If d>m there is no set, since{d} is outside the required range.
If d=m, the other values split into disjoint pairs{k,m−k},
1≤k≤(m−1)/2. Each pair must contribute exactly one element to
S; it then contributes the other as an absolute difference.
The choices are independent, yielding2^((m−1)/2) sets. There
is no middle singleton because m is odd.

If d=ceil(m/2)=(m+1)/2, every value d+1,…,m must occur in S:
absolute differences from d are at most d−1, and{d} supplies
only d. There are exactly(m−1)/2 such values, so S is forced.
Their differences are1,…,(m−1)/2, proving that it works.

If ceil(m/2)<d<m, the same argument forces d+1,…,m into S,
so difference1 is already present from d+1. To supply d−1,
one must use leaf d−1 directly, or a leaf1 or2d−1 whose
distance from d is d−1. Leaf d−1 would repeat difference1;
leaf1 would repeat it as an edge to zero;2d−1>m is impossible.
Thus this entire case is empty. This supplies the omitted
reason behind the printed “no way to get edge d−1” step.

## E75-3 — both directions of the corrected recursive step

Suppose d<ceil(m/2), equivalently2d≤m−1. The top d values
m−d+1,…,m cannot be absolute differences from d and are not d,
so they must belong to S. Their distances from d occupy exactly
m−2d+1,…,m−d. Since the edge differences are disjoint, no
remaining member of S can lie in that middle band. Remove the
top d leaves. Their2d edges have supplied precisely the top2d
differences, so the remaining S' together with its distances
and{d} must partition{1,…,m−2d}.

Thus S' is a(d,m−2d)-set of cardinality(m−2d−1)/2. If d is
outside that reduced range, both sides are impossible; this is
handled by the d>m terminal case. Conversely, any valid S' in
the reduced range can be extended by those top d leaves. Their
new vertex labels exceed every old label; their differences
are exactly the previously absent top2d values. Hence the
extension is valid and is inverse to deletion. This proves a
bijection, not just equality of counts. The corrected recursion
terminates because the positive odd parameter m decreases by2d.

## E75-4 — deriving every term in the divisor formula

For fixed d, repeated subtraction of2d leaves the unique odd
remainder r in1,…,2d−1 congruent to m modulo2d. The only
nonempty terminal cases are:

* r=d, possible when d is odd and divides m, with
  2^((d−1)/2) sets;
* r=2d−1, equivalent to2d dividing m+1, or d dividing n+1,
  with one set.

The two cases overlap exactly at d=1. Indeed an overlap gives
d=2d−1; equivalently gcd(2n+1,n+1)=1. Summing over d gives

    sum(d|m) 2^((d−1)/2) + sum(d|(n+1)) 1 − 1

canonical zero-apex descriptions before the extra d=m rule.
At d=m exactly half of the2^n sets contain1, so that rule
subtracts2^(n−1). The separate K3 correction then yields

    sum(d|m) 2^((d−1)/2) + sum(d|(n+1)) 1
      − 2^(n−1) − 1 − 2[n=1],       m=2n+1,

which is exactly the printed final formula. Every transformation
of the recurrence is reversible, so it determines all labelings,
not only their number. The small independent subset check
agrees with every individual d case for n=1,…,5, and gives
the respective final counts1,4,7,12,20. The proof is for all n;
these small counts are supporting checks only.

## E75-PARTIAL — the literal union definition lacks cardinality

The answer calls S a(d,m)-set using ordinary set union alone,
without explicitly saying |S|=(m−1)/2 or that the union is
disjoint. In isolation that definition is broader than the one
used by the subsequent argument: d=m=3,S={1,2} satisfies the
union equality, as do{1} and{2}, while the printed claim counts
only two such sets. The leaf interpretation supplies |S|=n;
then the m edge occurrences and full union force disjointness.
All closed arguments above state this assumption explicitly.
Whether this is an implicit contextual convention or a separate
wording correction remains partial. No unconditional claim
about the broader literal family is marked checked.
