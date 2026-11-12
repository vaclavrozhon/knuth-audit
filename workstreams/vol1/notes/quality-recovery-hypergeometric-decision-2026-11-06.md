# §1.2.6, p64–65: sufficient proofs for the algorithmic claims

Recovery audit, 6 November 2026. This supplements, rather than replaces,
`hypergeometric-summation.md`. The earlier note established the intended
meaning of closed form and proved the generic binomial-prefix obstruction.
The following supplies the missing decision and termination arguments.
There is no new erratum and no computational run.

The primary source is the locally held author PDF of Petkovšek, Wilf and
Zeilberger, *A=B*. The relevant text has now been read in full: printed
64–68, 73–77, 79–86, 92–94, 101–109, 141–153 and 157–159. Printed
75, 80, 85, 105, 108, 149, 153 and 159 were also directly rendered and
viewed. The exact source fingerprints and this reading scope are in
`../results/quality-recovery-hypergeometric-sources-2026-11-06.json`.
The source statements used below are Theorems 4.4.1, 5.3.1, 5.6.1,
5.6.3, 6.2.1, 8.4.1 and 8.7.1, and the polynomial-solution algorithms
of Chapters 5 and 8. Their proofs, not merely their statements, were read.
The reconstruction below makes the finite searches and domain limits explicit.

## 1. Exact scope and arithmetic model

Work over an effective characteristic-zero field, for example rational
numbers with algebraic constants or rational functions in finitely many
symbolic parameters, permitting the finite algebraic extensions encountered
by polynomial factorization. Polynomial arithmetic, gcds, factorization,
roots of a univariate polynomial, and the extraction of its nonnegative
integer roots are effective in this model. This does not promise an
algorithm on arbitrary real constants supplied without an effective encoding.

A nonzero hypergeometric sequence has a rational consecutive-term ratio.
Statements about that ratio are initially statements on a tail, beyond its
finitely many zeros and poles. Finite initial portions and parameter
specializations at singular values are checked separately. A closed form
here is a finite linear combination of hypergeometric terms, with a number
of terms independent of the summation endpoint. This is the qualified class
used by *A=B*, not a decision procedure for every meaning of simple function.

## 2. Gosper's rational normal form

Given a nonzero rational function r(k), write r=λf/g with f,g monic and
coprime. We construct

    r(k) = a(k)/b(k) · c(k+1)/c(k),
    gcd(a(k),b(k+h)) = 1 for every integer h≥0.             (G1)

The possible bad shifts h form a finite computable set: they are among
the nonnegative integer roots of Res_k(f(k),g(k+h)). This resultant is
not the zero polynomial, since in an algebraic closure its roots are
differences of the finitely many roots of f and g. Constant f or g gives
an empty set. Integer roots can therefore be found by a finite algebraic
calculation; over Q one can clear denominators, remove a power of h and
use the integer-divisor bound. The analogous test in an algebraic or
parameter field uses its effective equality and root operations.

Start p=f,q=g,c=1. Visit the possible shifts in increasing order. At h,
put s(k)=gcd(p(k),q(k+h)), and replace

    p(k) ← p(k)/s(k),
    q(k) ← q(k)/s(k−h),
    c(k) ← c(k) ∏_{j=1}^h s(k−j).

The ratio of the new c(k+1) to c(k) contributes s(k)/s(k−h),
so the represented rational function is invariant. The current p,q
always divide the original f,g; a new bad shift cannot appear. Removing
s removes the entire gcd at h, and subsequent divisions cannot restore
it. At termination set a=λp,b=q. This proves (G1) and termination.

The ordered construction also gives

    gcd(a,c)=1,                 gcd(b(k),c(k+1))=1.         (G2)

For the first assertion, a common root with a newly accumulated factor
s(k−j), 1≤j≤h, would give a surviving p-root and a q-root separated
by h−j<h, a shift already eliminated. For the second, a common root
with s(k+1−j) gives a p-root and a surviving q-root separated by
j−1<h. The same contradiction applies. Divisions made later preserve
these properties. This proves the extra conditions needed in §5 below.

## 3. Rational antidifferences reduce to a finite linear system

Let t(k+1)/t(k)=r(k). A hypergeometric H with H(k+1)−H(k)=t(k)
exists exactly when there is a rational y=H/t satisfying

    r(k)y(k+1)−y(k)=1.

Necessity follows from t/H=H(k+1)/H(k)−1; sufficiency follows by
substitution. With (G1), put y(k)=b(k−1)x(k)/c(k). Then

    a(k)x(k+1)−b(k−1)x(k)=c(k).                           (G3)

Every rational solution x of (G3) is a polynomial. To see this, take
a nonempty orbit of its finitely many poles under integer translation,
with first pole α and last pole β=α+h, h≥0. At k=α−1 only x(k+1)
has a pole, so a(α−1)=0. At k=β only x(k) has a pole, so
b(β−1)=0. Thus a(k) and b(k+h) have a common root α−1, contrary
to (G1). This argument is in the algebraic closure and excludes all
finite poles, including nonrational ones. Hence x is a polynomial.

There is a computable degree bound. If a and b have different degrees
or different leading coefficients, any nonzero solution of degree d
has d=deg c−max(deg a,deg b). Otherwise let their common degree be q
and common leading coefficient λ, and write

    a(k)=λk^q+A k^(q−1)+…,
    b(k−1)=λk^q+B k^(q−1)+….

For x(k)=Ck^d+… the coefficient of k^(d+q−1) in (G3) is
C(λd+A−B). Therefore d is either deg c−q+1 or (B−A)/λ.
Only nonnegative integral possibilities are retained. When q=0 use
A=B=0; the constant solution is tested directly, and the usual
finite-difference bound is deg c+1. Zero polynomials are treated
separately. Taking the largest possible degree and comparing coefficients
in (G3) gives a finite linear system, whose solution is both necessary
and sufficient. The returned H=b(k−1)x(k)t(k)/c(k) is checked by (G3).

Thus the algorithm terminates and decides the specified question. The
proof makes no polynomial-time or minimal-cost assertion. Factorization,
large shift dispersion and coefficient growth can be expensive.

Pairwise dissimilar hypergeometric terms are linearly independent over
rational functions, where similar means that the quotient is rational.
Indeed, a shortest nontrivial relation can absorb its rational
coefficients into the terms. Shift it and subtract the last term's
ratio times the original relation. Minimality forces every remaining
ratio to equal the last one; those terms are then constant multiples,
contrary to dissimilarity. Grouping an arbitrary finite sum by similarity
classes proves the general statement. Applying it to ΔH=t shows that
classes dissimilar to t can contribute only constants, whereas the class
of t is a single rational multiple of t. Gosper's failure consequently
excludes all finite hypergeometric combinations as antidifferences,
not just a single-term candidate (Theorem 5.6.3).

The earlier note's equation (m−k)x(k+1)−kx(k)=1 for t=C(m,k),
with m indeterminate, has no rational solution: a pole orbit would need
first pole m+1 and last pole 0, impossible for generic m; a nonzero
polynomial gives leading term −2Ck^(d+1), never 1. Together with the
preceding independence argument this proves the qualified negative
closed-form assertion. Special integer m and the full finite row sum
are separate cases, as the book explicitly recognizes.

## 4. Proper definite sums: recurrence construction terminates

For this part require a proper term

    F(n,k)=P(n,k) z^k
             ∏_s (a_s n+b_s k+c_s)! / ∏_s (u_s n+v_s k+w_s)!,

where P is a polynomial, a_s,b_s,u_s,v_s are fixed integers, and the
number of factors is fixed. On ordinary integer arguments, numerator
factorials must be defined; a reciprocal factorial at a negative integer
is zero. Meromorphic parameter identities may be used away from their
poles. For example C(an,n) with unspecified symbolic slope a is not
covered by this fixed-integer-slope hypothesis.

For 0≤i≤I and 0≤j≤J, the ratios F(n−j,k−i)/F(n,k) are rational.
Their denominators admit one common multiple consisting of P and a
fixed number of consecutive-factor products of lengths O(I+J).
This follows by canceling each factorial ratio: shifting its argument
changes it by at most |a_s|J+|b_s|I, and the single largest interval
of factors contains all shorter intervals. After clearing this common
denominator, the degrees in k are O(I+J), with constants depending
only on F. A k-free linear relation between these shifts has
(I+1)(J+1) unknown coefficients in the field of rational functions of n
and only O(I+J) coefficient equations. Searching I=J eventually gives
a nonzero relation. This proves the needed existence and finite search
without assuming the source's sharper explicit span bound.

Write N and K for forward shifts in n and k. In the ring of shift
operators with coefficients rational in n, K commutes with N and
with coefficients. Choose a nonzero annihilator P(n,N,K) of F having
minimal K-degree, converting backward shifts to forward shifts first.
Polynomial division in K gives

    P(n,N,K)=L(n,N)−(K−1)Q(n,N,K),    L=P(n,N,1).

Here L is nonzero. If L=0, then G=QF is independent of k. If G=0,
Q is an annihilator of smaller K-degree. If G≠0, it is a rational
multiple of F and is hypergeometric in n: evaluate at any fixed generic
k for which this rational representation is regular. A nonzero
first-order n-operator H annihilates G, and HQ is again an annihilator
of smaller K-degree. Products of nonzero operators here are nonzero
by their leading shift coefficient. Both alternatives contradict
minimality. Thus

    L(n,N)F=(K−1)G,               G/F rational.             (T1)

For completeness, the usual constructive search can find (T1). Fix an
n-order J and put t(k)=Σ_{j=0}^J a_j(n)F(n+j,k). Clear its known
denominators to write t=p_0(k)F(n,k)/D(k), with p_0 linear in the
unknown a_j. Normalize the known ratio of F/D by (G1); the additional
factor p_0(k+1)/p_0(k) merely replaces c by c p_0. Equation (G3)
then has right side c p_0 and is linear in both the a_j and the
coefficients of x. Its degree is bounded by deg c plus the known
maximum degree of p_0. The pole argument requires only (G1), which
still holds. The degree alternatives above, including the homogeneous
case, give a finite bound. If p_0=0, a nonzero a-vector already gives
a direct recurrence and zero certificate. Otherwise solve the joint
linear system and retain only a nonzero a-vector. Each J is finite,
and (T1) guarantees that increasing J eventually succeeds.

Summation gives a homogeneous recurrence for f(n)=Σ_k F(n,k) only
when the certificate's boundary term vanishes, as for suitable compact
support, or when its endpoint limits have been proved to vanish.
Otherwise it gives that explicit boundary term. Infinite sum/shift
interchanges require convergence and a justification of the limits.
Neither properness alone nor a formal telescoper supplies those facts.

## 5. Hyper: deciding the specified closed-form solutions of a recurrence

Consider L=Σ_{i=0}^d p_i(n)N^i, with p_0p_d≠0; remove zero initial
coefficients by a shift when necessary. For a hypergeometric solution y,
put its consecutive ratio in the normal form

    y(n+1)/y(n)=ζ a(n)/b(n) · c(n+1)/c(n),

with a,b,c monic and (G1)–(G2). Substitution and clearing denominators
give

    Σ_{i=0}^d ζ^i P_i(n)c(n+i)=0,
    P_i(n)=p_i(n) ∏_{j=0}^{i−1}a(n+j) ∏_{j=i}^{d−1}b(n+j).       (H1)

Every term except i=0 is divisible by a(n); the coprimalities imply
a divides p_0. At the other endpoint the same argument gives
b(n+d−1) divides p_d(n), or b divides p_d(n−d+1). Thus a and b
come from finite lists of monic polynomial divisors. For each pair let
M=max_i deg P_i and let α_i be the coefficient of n^M in P_i.
The highest coefficient of (H1), using that c is monic, gives

    Σ_i α_i ζ^i=0.

This polynomial is nonzero by the definition of M. There are finitely
many nonzero ζ to try, in finite algebraic extensions if needed.

For each triple (a,b,ζ), (H1) is a polynomial-coefficient recurrence
for the polynomial c. The following establishes a finite bound for
all its polynomial solutions; it also handles inhomogeneous equations.
Rewrite any recurrence operator as Σ_j q_j(n)Δ^j, using
q_j=Σ_{i≥j} C(i,j)p_i. Let

    b_0=max_j(deg q_j−j),
    A(D)=Σ_{deg q_j−j=b_0} lc(q_j) D(D−1)…(D−j+1).

The polynomial A is nonzero, since distinct falling factorials are
linearly independent. For a polynomial y of degree D, the prospective
coefficient of n^(D+b_0) in Ly is lc(y)A(D). In Ly=f there are only
three possibilities: D+b_0<0, hence D≤−b_0−1; A(D)=0; or
D=deg f−b_0. In the homogeneous case the last alternative is absent.
The finitely many nonnegative integral roots of A and these explicit
bounds give a finite maximal D. Coefficient comparison finds the
complete polynomial-solution space, or proves it empty. This also
proves the finite polynomial subroutine used above.

For a fixed triple let H(n+1)/H(n)=ζa(n)/b(n). Every polynomial
solution c gives y=Hc, and a basis for the polynomial solutions spans
all these y. Enumerate the finite triples and collect their bases.
Conversely the divisibility and leading-coefficient arguments show
that every hypergeometric solution is on this list. A finite sum of
pairwise dissimilar hypergeometric terms is a solution only if each
term is: Lh_i is a rational multiple of h_i, so the independence
proved in §3 forces every Lh_i to vanish (Theorem 8.7.1). The collected
list therefore spans all solutions in the stated closed-form class.

Finally choose an integer N after the integer zeros of the leading
coefficient p_d and all exceptional indices under discussion. A
solution on n≥N is uniquely determined by d consecutive values,
because the recurrence solves successively for the next value.
This final decision step requires the actual definite sum's initial
values to be effectively and exactly available in the chosen coefficient
field (or its specified finite extensions). Finite sums of the encoded
terms have this property. Mere convergence of an infinite sum does not
provide an equality algorithm for its value. Subject to this explicit
input condition, compare those initial values with the finite span of
the candidate solutions by a finite linear system.
A match proves equality of the tails by this recurrence invariant;
a mismatch excludes every closed form in the specified class.
Any requested initial indices before N are evaluated and checked
separately, retaining explicit exceptional values when needed.

All searches are finite: dispersion, polynomial divisors, roots,
degree candidates and linear systems. The increasing-order telescoper
search terminates by §4. TAOCP states no asymptotic running-time bound
for these algorithms here, and none is inferred. This closes the
algorithmic assertion on p65 in its expressly qualified scope; it
does not assert a decision procedure for arbitrary infinite sums,
singular specializations, or every possible class of closed forms.
