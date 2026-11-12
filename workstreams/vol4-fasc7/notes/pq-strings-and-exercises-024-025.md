# (p/q)-strings: complete arguments for exercises 24–25

Sources: exercises p. 114 / file 129, answers p. 161–162 / files
176–177, first digital edition; original pages inspected. Assume
integers 1≤p<q, length n≥0, and height parameter m≥0. A (p/q)-string
has at most p ones in every contiguous block of q or fewer bits.
This explicit short-block convention is used throughout. Relevant
F7 errata layers contain no correction to these two answers.
The historic attribution to Ira Gessel in March 2020 and names of
the non-Fibonacci sequences are not independently sourced.

All count identities below have their own proofs. One wording issue
about the orientation of the referenced rim representation is kept
separate at the end; the existence of a valid bijection does not by
itself check that printed intermediate instruction.

## E24(a): The finite walk model and all three numerical answers

The states are q-bit strings of weight at most p. An arc shifts the
string one place left and appends a bit, provided the resulting
state still has weight at most p. This is exactly the stated suffix/
prefix overlap relation. Starting at 0^q, the successive appended
bits of an n-edge walk give a unique binary string of length n, and
the string in turn determines its unique sequence of states.

After each append, the state is the last q bits of the zero-padded
prefix. If the string satisfies the (p/q) condition, each such
state has weight at most p. Conversely any block of at most q bits
ending at a given position is contained in that state's suffix;
therefore its weight is at most p if the state is legal. This proves
both directions, including n<q and n=0. The empty string corresponds
to the unique zero-edge walk. The number of walks is not multiplied
by a choice of starting state.

Let A be the transition matrix acting on column vectors of endpoint
counts, e the unit vector at 0^q, and l the all-ones row. Then the
answer is C_pqn=l A^n e. An independent recurrence below gives the
first eleven terms in the three requested cases:

    (1,2): 1,2,3,5,8,13,21,34,55,89,144;
    (1,3): 1,2,3,4,6,9,13,19,28,41,60;
    (2,3): 1,2,4,7,13,24,44,81,149,274,504.

Thus the stated answers 144,60,504 are correct. The exact transfer
calculation in `results/pq-generating-functions.json` agrees with
all these entries. It is a tiny fixed-state calculation, not a
search through all length-ten strings.

## E24(b): The maximum weight and an attaining construction

Write n=qm+r, 0≤r<q. Partition the string into m full q-blocks and
one final block of length r. Their respective maxima are p and
min(p,r), so the total weight is at most

    pm+min(p,r).

The first n bits of the infinite periodic string (1^p 0^(q−p))^∞
attain this bound: each full period has p ones, and the initial r
bits of the next have min(p,r). Any q consecutive bits of that
periodic string have exactly p ones, while shorter blocks have at
most p. Hence every finite prefix is legal. This proves the printed
formula and attainment, also for n=0 or n<q.

## E24(c)-1: The generating-function system and its unique solution

For each state α, let G_α(z) count walks from the fixed initial state
σ to α. A zero-edge walk contributes [α=σ]. Every nonempty walk has
a unique penultimate state β with arc β→α, so removing its last
edge gives the exact formal-power-series equation

    G_α(z)=[α=σ]+z sum_(β→α) G_β(z).

The overall function is sum_α G_α. The coefficient of degree n on
the right depends only on coefficients of degree n−1; induction
therefore proves existence and uniqueness of the formal series
solution. In matrix terms G(z)=l(I−zA)^(-1)e, where the inverse is
the formal geometric series sum_(n≥0) z^n A^n. This also proves
rationality because the finite matrix inverse is a matrix of rational
functions with denominator having constant term one.

For (p,q)=(1,2), the states are 00,01,10. Their incoming arcs give
exactly the three equations in the answer:

    G00=1+z(G00+G10),  G01=z(G00+G10),  G10=zG01.

Thus G01=G00−1, G10=z(G00−1), and
G00(1−z−z²)=1−z². Summing these three functions yields
(1+z)/(1−z−z²), as printed.

## E24(c)-2: The two general families and their initial conditions

For p=1, ones are separated by at least q−1 zeros. For n≥q, split
legal strings according to their last bit: a final zero leaves an
arbitrary legal length-(n−1) prefix; a final one forces its preceding
q−1 zeros and leaves an arbitrary legal length-(n−q) prefix. Hence
C_n=C_(n−1)+C_(n−q). For 0≤n<q, there can be at most one one, so
C_n=n+1. Multiplying the series by 1−z−z^q cancels all coefficients
of degree at least q and leaves one in every degree 0,…,q−1. Thus

    G_1q=(1+z+…+z^(q−1))/(1−z−z^q).

For p=q−1, the only prohibited full q-pattern is 1^q; shorter
patterns impose no further restriction. Splitting at the final zero
followed by 0,…,q−1 terminal ones gives, for n≥q,
C_n=C_(n−1)+…+C_(n−q). For n<q all 2^n strings are legal.
The same coefficient multiplication now leaves one in each degree
0,…,q−1 and gives

    G_(q−1),q=(1+z+…+z^(q−1))/(1−z−z²−…−z^q).

These recurrences yield the numerical lists above. In particular
C_12n=F_(n+2) with F_0=0,F_1=1, because the recurrence and the first
two values agree; this establishes the Fibonacci identification.
The p=1,q=3 and p=2,q=3 substitutions give exactly the other two
explicit formulas in the answer. Together these families cover
seven of the ten pairs 1≤p<q≤5.

## E24(c)-3: Full certificates for the three remaining rational functions

The remaining displayed formulas are

    G24=(1+z+z²+z³−z⁴−z⁵)/(1−z−z²−z⁴+z⁶),
    G25=(1+z+2z²+2z³+2z⁴−z⁵−z⁶−2z⁷−z⁸−z⁹)
         /(1−z−z³−2z⁵+z⁸+z¹⁰),
    G35=(1+z+z²+2z³+2z⁴−z⁵−z⁶−z⁸−z⁹)
         /(1−z−z²−z⁴−2z⁵+z⁷+z¹⁰).

They are checked as formal identities by the following finite-dimensional
lemma, not by guessing from an initial coefficient sample.

**Lemma.** In a vector space of dimension d, if l A^k v=0 for
k=0,…,d−1, then the same holds for every k≥0.

If v=0 this is immediate. Otherwise, among v,Av,…,A^d v, let A^r v
be the first vector dependent on its predecessors. Then 1≤r≤d and
A^r v is a linear combination of v,…,A^(r−1)v. Multiplying that
relation by powers of A gives a recurrence for all later vectors.
Applying l and using induction proves that every later observation
is zero. This proves the lemma, including possible singular A.

To certify a proposed P(z)/Q(z), write Q=sum_(j=0)^D q_j z^j with
q_0=1 and deg P<D. Check the coefficients of QG−P below degree D
directly. For all later coefficients, put

    v=sum_(j=0)^D q_j A^(D−j)e.

The degree D+k coefficient of QG−P is exactly l A^k v. Verifying
the first d of these values as zero proves every later coefficient
zero by the lemma. Since Q has constant term one, QG=P then proves
G=P/Q as a formal series.

The exact integer certificates in `results/pq-generating-functions.json`
give the complete ordered state sets, all transition edges, numerator
and denominator coefficients, initial residuals, vector v, and d
successive zero observations. The three state dimensions are 11,16,26,
respectively. Every residual and required observation is exactly zero.
Thus every coefficient in the three printed rational functions is
verified with a finite proof certificate. The same short nice15 run
also supplies certificates for the seven general-family instances;
the largest state space is only 31 states. Its reproduction script
is `check_pq_generating_functions.py`. No symbolic infinite expansion
or large enumeration is assumed.

## E25(a)-1: The complete block-dominance criterion

Consider a legal length-qm string with exactly pm ones. The m aligned
q-blocks each have at most p ones, so each must have exactly p. Let
F_k(s) be the number of ones in the first s positions of block k,
0≤s≤q. A q-window crossing from block k to block k+1, after omitting
the first s positions of block k, has weight

    p−F_k(s)+F_(k+1)(s).

It obeys the cap iff F_(k+1)(s)≤F_k(s). Hence the full string is legal
iff these prefix inequalities hold for each adjacent pair of blocks
and every s. This condition covers every q-window. Shorter windows
are contained in one full window when m≥1; the empty case m=0 is
handled separately. Writing the one positions of block k as
a_(1,k)<…<a_(p,k), the prefix inequalities are equivalent to

    a_(i,k)≤a_(i,k+1) for every i.

Indeed, later i-th one positions cannot give a larger prefix count;
and if the later block has an earlier i-th one, its prefix ending at
that position has at least i ones while the earlier block has at
most i−1. This proves both implications of the equivalence.

## E25(a)-2: An explicit bijection with boxed plane partitions

From such one positions define row lengths

    lambda_i^(k) = q−p+i−a_(i,k),  1≤i≤p.

Since i≤a_(i,k)≤q−p+i, these lie in 0,…,q−p. Strict increase of
the one positions implies weak decrease of the lambda row lengths:
lambda_i−lambda_(i+1)=a_(i+1,k)−a_(i,k)−1≥0. The block-dominance
condition implies lambda_i^(k)≥lambda_i^(k+1). We thus obtain nested
Ferrers shapes in a p by (q−p) rectangle. Define

    P_ij = number of k for which lambda_i^(k)≥j.

Then 0≤P_ij≤m and P is weakly decreasing in each index. It is a
plane partition fitting in the stated box.

Conversely, for any such plane partition, let lambda_i^(k) count
the j with P_ij≥k, and set a_(i,k)=q−p+i−lambda_i^(k). The row
inequalities ensure strictly increasing one positions within 1,…,q;
the nested-level inequalities ensure weakly increasing positions
across blocks. E25(a)-1 therefore gives an extreme (p/q)-string.
Counting levels and then taking level sets recovers the original
shapes and P; solving the displayed formula for a recovers the
original strings. The constructions are inverse. This proves the
claimed equality with the boxed plane-partition count.

For m=0 there is one empty string and one all-zero plane partition;
both constructions are empty and remain inverse. No product formula
for plane partitions is needed or silently imported.

## E25(a)-3: Every word in the printed example

For p=2,q=5,m=6 and P with rows (4,4,1),(2,1,0), the level shapes
have row lengths

    (3,2), (2,1), (2,0), (2,0), (0,0), (0,0).

The formula a_i=3+i−lambda_i gives the six one-position pairs

    (1,3), (2,4), (2,5), (2,5), (4,5), (4,5).

These yield exactly 10100,01010,01001,01001,00011,00011. The first
one positions are weakly increasing, as are the second one positions,
so the concatenation is legal by E25(a)-1. It has 12 ones in length
30, hence attains the maximum. This verifies every word and the
concatenation assertion without relying on the ambiguous rim wording.

## E25-rim: The referenced orientation is still a partial intermediate step

The actual original Volume 4A p. 395, §7.2.1.4–(14), says that a
zero is an upward step and a one a rightward step, along the boundary
from lower left to upper right. The original is saved in
`images/vol4a-p395-rim.png`; the local text around line 19938 supplies
the context. With i as the usual row index, a p by (q−p) tableau
therefore has p zero steps and q−p one steps in its bounded rim.

For the first level shape (3,2), that convention gives 11010. The
printed F7 word 10100 is instead the rim of the conjugate shape
(2,2,1), or the reversal-complement of 11010. The same transformation
accounts for the other five printed words. The explicit bijection
proved above therefore corresponds to taking the conjugate shapes
before applying that referenced rim convention.

An implicit transpose of the coordinates could explain the wording,
because the box count is symmetric in the two horizontal dimensions.
The mathematical count identity and the displayed binary example
are correct under the explicit construction above. The literal
instruction to use the rim of the unqualified level shape, however,
has not yet been reconciled with the source convention; it remains
a separate partial orientation item, not a confirmed finding. The
coordinator independently inspected both originals and confirmed the
11010 versus10100 orientation difference. The explicit row/column-versus-
Cartesian warning in answer27 on the same F7 page supports retaining
the convention as partial; it does not supply the missing conjugation
in answer25. No new finding card is created from this ambiguity.

## E25(b)-1: Remainder r<p

Let n=qm+r and an extreme string have mp+r ones, where r<p. Each
aligned q-block must have p ones and the tail of length r must be
all ones, since their individual maxima sum to mp+r. The q-windows
crossing from the last full block to the tail imply
F_m(s)≥s for 0≤s≤r, so the first r bits of that block are all ones.
Block dominance forces those same leading r ones in every earlier
block. Thus the string has the unique form

    (1^r y_1)(1^r y_2)…(1^r y_m)1^r,

where each y_k has length q−r and p−r ones. After removing the common
r ones from the prefix profiles, adjacent block dominance is exactly
the dominance criterion for the y blocks. Therefore their
concatenation is an extreme ((p−r)/(q−r))-string of length m(q−r).
Conversely any such y string reconstructs the original string and
satisfies both all adjacent-block and final-tail window inequalities.
This is a bijection, proving c_pqn=e_(p−r),(q−r)(m).
It includes r=0 as the identity map and m=0 as the unique all-one
tail of length r.

## E25(b)-2: Remainder r=p

The same argument forces the first p bits of every full block to be
ones. Since it has exactly p ones, the remainder must be zeros.
The unique extreme string is

    (1^p 0^(q−p))^m 1^p.

It is legal by the periodic construction in E24(b), proving the
printed count one. This also handles m=0 without introducing an
undefined zero-dimensional parameter into e.

## E25(b)-3: Remainder r>p

Now the extremal weight is (m+1)p. Every full block has p ones and
the final r-block also has p. Its prefix count at r is p. The final
crossing-window inequality implies F_m(r)≥p, hence all ones of the
last full block lie among its first r positions. Block dominance
forces the same fact for every earlier full block. The string has
the unique form

    (y_1 0^(q−r))…(y_m 0^(q−r)) y_(m+1),

with each y_k of length r and weight p. Prefix comparisons beyond
r are automatic, and those up to r are exactly the dominance
comparisons for the y blocks. Removing the forced zero stretches
therefore gives an extreme (p/r)-string of length (m+1)r, and the
inverse insertion restores every original window inequality. The
count is e_pr(m+1)=e_pr(ceil(n/q)), as printed. When m=0 this simply
counts all r-bit strings of weight p, consistent with the short-block
definition. Thus every branch, the floor/ceiling parameters, and all
small-length boundaries of part (b) are proved independently of the
rim-orientation question.
