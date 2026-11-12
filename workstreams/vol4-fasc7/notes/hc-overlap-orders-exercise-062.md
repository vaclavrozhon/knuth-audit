# Exercise62: every constraint, transfer coefficient, total, and asymptotic

Original question p119/file134 and answer p172/file187 were displayed.
The known13September2026 corrections change x_j to x_i and the second
displayed transfer row to(9,12,10,11). The9September2026 improvement
rewrites the directional counts30 and25; their values are unchanged.
The primary TeX and the displayed short errata PDF p13 were checked.
None of these known changes is a finding.

Evidence: `check_overlap_orders62.py`, `results/overlap-orders62.json`.
The complete requested55-entry table for1≤m≤n≤10 is in the result,
with its parameters attached to every integer. The largest transfer
has512 boundary states and262144 coefficients. One exact column-DP
run computed the table; no full enumeration of edge orientations was
started. The subsequent small rounding and overlap certificates reuse
those saved totals.

## E62-1 — all neighbors, triples, and geometric impossibility of a3-cycle

Use cells(i,j) with0≤i<m,0≤j<n and the three positive adjacency
steps(1,0),(0,1),(1,1). The exact neighbor proof in E61-7 applies;
the column reversal relating these coordinates to the corrected61
barycentric formula was made explicit there.

There are(m−1)n vertical,m(n−1) horizontal,and(m−1)(n−1) diagonal
pairs, so their total is

    E=m(n−1)+(m−1)n+(m−1)(n−1).

For m=n=6 this is30+30+25=85. The25 diagonal pairs can equally
be grouped by the nine diagonals of their5×5 starting positions,
of lengths1,2,3,4,5,4,3,2,1, exactly as the improvement states.
The85 independently chosen two-way relations would have2^85
unrestricted specifications before constraints are imposed.

The neighbor graph has only two types of triangle, the two halves
of each elementary square; its neighbor-six-cycle proof in E61-7
also excludes any omitted triangle. Thus there are exactly
2(m−1)(n−1) ternary constraints,50 for6×6.

These triangles do have a common open projected region, not merely
three pairwise overlaps. In the integer screen coordinates of61,
the two representatives have centers

    (0,0),(−6,−1),(−1,5),
    (0,0),(5,6),(−1,5).

Their three outline intersections are respectively the triangles

    (−2,2),(−3,1),(−2,1),
    (2,4),(1,4),(1,3),

each of area1/2. They follow by exact half-plane clipping, with the
full rational calculation saved. At any common interior pixel, the
three nearest visible-depth candidates have a strict linear order.
Therefore A<B,B<C,C<A cannot all hold. The reversed3-cycle is
equally impossible. This proves the question's geometric restriction
on every adjacent triple.

For bits[A<B],[B<C],[C<A], the two cycles are precisely000 and111.
The other six orientations are exactly those whose sum is1or2.
Thus the printed ternary constraint excludes exactly the required
assignments. The counting task concerns these local constraints;
it does not impose a global acyclic order. The cyclic arrangements
in61(iv) explain why a global-order condition would change the task.

## E62-2 — complete frontier invariant and initialization

Let A_i=(i,n−1) be the existing last column, and B_i=(i,n) the new
column. For1≤i<m put

    x_i=[A_(i−1)<A_i],       y_i=[B_(i−1)<B_i].

Define c_n(x) to count all valid orientations in the first n columns
with exactly this last-column vector. It counts each physical
neighbor-pair assignment once. For n=1, there are only the m−1
vertical bits and no triangles, so c_1(x)=1 for every x, including
the empty vector when m=1.

All old constraints remain satisfied by a counted prefix. Every new
constraint is in the new strip between A and B, and its old variables
consist only of x. Thus the number of extensions depends solely on
x and the prescribed new vector y. Distinct old assignments and
distinct strip assignments give distinct extended orientations;
restriction recovers both uniquely. This proves the transfer

    c_(n+1)(y)=sum_x M(y,x)c_n(x),

where M(y,x) counts the strip's horizontal and diagonal bits.
No memory of previous columns is omitted.

## E62-3 — every local coefficient and the O(m) construction

The new strip has horizontal bits h_i=[A_i<B_i],0≤i<m, and
diagonal bits d_i=[A_(i−1)<B_i],1≤i<m. At row i its two triangles
give exactly

    x_i+h_i+1−d_i ∈{1,2},
    h_(i−1)+y_i+1−d_i ∈{1,2}.

The first constraint forces d_i=x_i if x_i=h_i; otherwise it
allows either d_i. The second forces d_i=y_i if h_(i−1)=y_i;
otherwise it allows either. Incompatible forces give0 choices,
no force gives2, and all other cases give1. In row/column order
h_(i−1),h_i∈{0,1}, all sixteen resulting entries are

    K00=[[1,1],[1,2]],       K01=[[1,2],[0,1]],
    K10=[[1,0],[2,1]],       K11=[[2,1],[1,1]].

The first subscript is x_i, the second y_i. Each entry's allowed
diagonal values are independently saved by direct evaluation of both
triangle constraints. Multiplying matrices sums over the shared
horizontal bits and multiplies the independent diagonal choices.
Therefore, with1 the column vector(1,1),

    M(y,x)=1^T K_(x1,y1)···K_(x_(m−1),y_(m−1))1.

This proves every transfer coefficient. An m-stage calculation with
a two-entry row vector takes O(m) additions and multiplication by0,1or2;
it terminates after m−1 local steps. Each coefficient counts at most
the2^(2m−1) new-bit assignments, so its integer length is O(m).
The printed O(m) is an arithmetic-step bound; elementary bit
operations give O(m²) for this direct calculation. In the requested
widths m≤10, every coefficient fits comfortably in a machine word.

Global reversal of all comparison bits maps x to its bitwise
complement and preserves every constraint. Thus

    c_n(x)=c_n(complement x),
    M(y,x)=M(complement y,complement x).

For m≥2, it suffices to compute2^(m−2) destination rows, each
with2^(m−1) entries: exactly2^(2m−3) coefficients, as stated.
The other half of the actual output vector is obtained by reversal.
This output symmetry does not say that two full matrix rows are
identical on arbitrary nonsymmetric input vectors.

## E62-4 — every width-three coefficient and both printed equalities

For m=3, order the boundary words00,01,10,11. The complete matrix is

    M=[[13,11, 9, 6],
       [ 9,12,10,11],
       [11,10,12, 9],
       [ 6, 9,11,13]].

For example, the first row is the sum of all entries in
K00K00,K00K10,K10K00,K10K10, respectively. The second is from
K00K01,K00K11,K10K01,K10K11. Direct2×2 multiplication gives
every displayed number, including both corrected9/11 entries.
The final two rows follow by simultaneously complementing x,y.

Since the actual c_n vector has c_n(00)=c_n(11) and
c_n(01)=c_n(10), these last rows give precisely the printed
`c_(n+1)(10)=c_(n+1)(01)` and
`c_(n+1)(11)=c_(n+1)(00)`. Their assumptions are explicit.

## E62-5 — total, all boundary dimensions, and full table

Every complete orientation has one unique last-column vector, so

    t_(m,n)=sum_x c_n(x).

For m=1 the matrix product is empty and1^T I1=2: there is one
free horizontal bit per added column. Consequently t_(1,n)=2^(n−1).
At1×1 there are no variables and no constraints, hence one empty
assignment. At n=1 the initialization gives t_(m,1)=2^(m−1).
For m=2, M=[[5,4],[4,5]], and the symmetric initial vector gives
t_(2,n)=2·9^(n−1). These cover every small boundary of the request.

The exact implementation shares prefixes when generating the transfer
matrix but computes the same formula of E62-3. Its state invariant is
the row vector1^T times the matrices for the already assigned bit
pairs; each branch appends one x/y pair, and each leaf stores its sum
in M[y][x]. The recursion depth is m−1 and all4^(m−1) pairs are
reached exactly once. Matrix/vector multiplication then realizes the
proved column invariant for n=1,…,10. All computations use integers.
The full matrices need O(4^(m−1)) entries, and each column update
uses O(4^(m−1)) arithmetic operations; no complexity claim about
an optimal implementation is needed.

All55 requested values are saved individually. As a separate exact
consistency check, all100 computed values obey t_(m,n)=t_(n,m):
transposing the cell grid swaps horizontal and vertical edges and
preserves the diagonal neighbor set, giving a direct bijection.
The closed m=1,2 formulas are checked for every saved n as well.

In particular the exact reported counts are

    t_(6,6)=22406540276117433798,
    t_(10,10)=23336231715157046447023761145710030876842913391344045399558.

The latter has exactly the printed prefix and suffix. The middle
digits omitted by the answer are supplied here by the exact DP.

## E62-6 — all width-three asymptotic intermediates

Write a_n=c_n(00)=c_n(11), b_n=c_n(01)=c_n(10). Then

    [a_(n+1);b_(n+1)]=R[a_n;b_n], R=[[19,20],[20,22]],
    a_1=b_1=1,    t_(3,n)=2(a_n+b_n).

Thus t_(3,1)=4, t_(3,2)=2(39+42)=162. Direct multiplication gives
R²=41R−18I, so

    t_(3,n+2)=41t_(3,n+1)−18t_(3,n),
    t_(3,3)=41·162−18·4=6570.

The characteristic roots are

    r=(41+sqrt1609)/2,     s=(41−sqrt1609)/2.

They are distinct, with0<s<1<r. Solving for the two coefficients
from4 and162 gives the exact identity for n≥1

    t_(3,n)=c r^n+c' s^n,
    c =(1609+31sqrt1609)/28962=(1+31/sqrt1609)/18,
    c'=(1609−31sqrt1609)/28962=(1−31/sqrt1609)/18.

For example, c=(162−4s)/(r(r−s)); multiplying numerator and
denominator by41−sqrt1609 gives the stated form. Both coefficients
are positive because sqrt1609>31. Since(s/r)^n tends to zero,
t_(3,n)/(c r^n) tends to1. This proves the printed asymptotic,
including its index n rather than n−1 and its coefficient c.

## E62-7 — rigorous checks of every displayed approximation

The exact rational square comparisons give

    40.11234<sqrt1609<40.11235.

Monotonicity of the formulas for r and c then puts r in the
rounding interval for40.556 and c in that for.0985. The saved
60-digit evaluations are r=40.5561711201… and c=.0984905258424….

For the logarithmic exponents no floating-point trust is needed.
The saved exact integer tests are

    2^12855 < t_(6,6)^200 < 2^12857,
    2^38777 < t_(10,10)^200 < 2^38779.

Taking increasing200th roots and base-two logarithms yields
64.275<log2(t_(6,6))<64.285 and
193.885<log2(t_(10,10))<193.895. Thus the displayed64.28 and193.89
are correctly rounded. The higher precision values64.2805537…
and193.8944011… are supplementary, not the proof of rounding.

## E62-8 — one literal coefficient-count edge case remains separate

The problem explicitly includes m=1. The algorithm and all its
counts are fully proved there: one empty frontier and one coefficient2.
The sentence counting2^(2m−3) coefficients presupposes a nonempty
bit vector so that complement pairs are distinct; taken literally
at m=1 it gives1/2. Whether the intended trivial-width exception is
implicit remains an interpretive partial, without a finding card.
It does not affect the validity of the transfer method, requested
table or any printed numerical total.
