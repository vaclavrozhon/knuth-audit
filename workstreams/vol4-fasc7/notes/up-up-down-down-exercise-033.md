# Up-up-or-down-down permutations — exercise33 in full

Scope: exercise33 p115/file130 and every part/intermediate assertion of answer33
p165–166/files180–181. Both original answer layouts, including the short p166 continuation, have been
viewed. The13 September2026 erratum removes an extra μ² from the
pole subtraction and inserts2^(−n) into the coefficient error bound. Both
corrections are proved below and excluded from findings. Historical Laplace/
Cauchy attributions and publication details are explicit bibliography skips.

Sources consulted for the referenced mathematics: Gessel's primary
arXiv2411.16113v1, especially its recurrence and main theorem; and Knuth's
four-page “Whirlpool permutations,” revised6 December2024, especially its
bijection. They are saved with hashes in `sources/whirlpool-primary-manifest.json`.
The proofs below supply the individual arguments, rather than treating an
external result or a numerical match as the proof of the printed steps.

## U33-a — recurrence, auxiliary counts, and the initial values

LetU_n count permutations of2n−1 distinct ordered elements whose consecutive
comparisons occur in equal pairs: a_(2k−1)<a_(2k) iff a_(2k)<a_(2k+1).
Thus an even-indexed element cannot be a local maximum or minimum. Define
Q0=1 andQ_n=nU_n for n≥1.

For an even-length permutation b0,...,b_(2n−1) imposing the same conditions
only at centers2,4,...,2n−2, b0 is free before the up-up-or-down-down suffix.
There are2n choices for its value andU_n for the remaining relative order,
giving2nU_n=2Q_n. Complementing all ranks preserves every paired comparison
and interchanges b0<b1 with b0>b1; distinctness precludes equality. Exactly
Q_n therefore have either prescribed initial orientation. This proves the
answer's auxiliary even-length count and halving assertion.

In a permutation counted byU_(n+1), the maximum2n+1 cannot be in an even
position, so it occupies position2k+1 for a unique0≤k≤n. Choose the2k
values to its left in choose(2n,2k) ways. Ifk>0, the final pair on the left
must increase toward the maximum. Reverse that even-length left sequence:
its paired-comparison centers remain even and its first pair decreases,
so it hasQ_k possible relative orders by the preceding halving argument.
The right even-length sequence begins by decreasing away from the maximum;
its remaining paired centers also giveQ_(n−k) possibilities. Empty sides
contributeQ0=1. Conversely, such chosen sides and the maximum satisfy every
paired comparison, including the two next to the maximum. The decomposition
is unique. Hence, including n=0,

U_(n+1)=sum_(k=0)^n choose(2n,2k) Q_k Q_(n−k).

This givesU1=1,U2=2,U3=4+6+4=14,
U4=42+60+60+42=204, and
U5=816+1176+1120+1176+816=5104. Every printed initial value follows from
the proved recurrence; the small saved recurrence calculation agrees.

## U33-b — the univariate generating function

Use exponential generating functions
U(z)=sum_(n≥1)U_n z^(2n−1)/(2n−1)! and
Q(z)=sum_(n≥0)Q_n z^(2n)/(2n)!.
Coefficient convolution of the recurrence givesU′=Q². Also
Q=1+zU/2 by Q_n=nU_n and(2n)!=2n(2n−1)!. This is the printed Riccati
equationU′=(1+zU/2)² withU(0)=0; successive formal coefficients determine
a unique solution.

Put w=z/√2, T=tanhw andD=1−wT. For the proposedU=√2 T/D,
T′=1−T² andD′=−T−w(1−T²), where primes here meanw derivatives. Thus
its z derivative is
((1−T²)D−TD′)/D²=1/D².
Meanwhile1+zU/2=1+wT/D=1/D, andU(0)=0. This verifies the entire closed
form and its initial condition, so formal uniqueness proves the identity.

## U33-b-refined — every p_n row and the bivariate identity

Letp_n(k) count the2n+1-element permutations on{−n,...,n} beginning withk.
Complementing ranks givesp_n(k)=p_n(−k); reversing an odd-length sequence
preserves the even comparison centers, so first-entry and last-entry counts
agree. This verifies the convention change from Gessel's last-entry theorem
to the book's first-entry formulation.

Delete the first two valuesk,h of a permutation counted byp_(n+1)(k), then
renormalize the remaining2n+1 values to{−n,...,n}. Suppose its first value
becomesj. The first three original values must be monotone. In the increasing
case their third value isj+1 (two lower entries were deleted), and h has the
j−k choicesk+1,...,j. In the decreasing case that third value isj−1, andh
has thek−j choicesj,...,k−1. Both cases uniquely reconstruct the original
sequence from the reduced one andh. Therefore

p_(n+1)(k)=sum_(j=−n)^n |j−k| p_n(j),  |k|≤n+1,

withp0(0)=1. This proves the unusual recurrence, including its endpoints.
It gives the three printed rows
(1,0,1), (4,2,2,2,4), and(42,28,22,20,22,28,42).

Here is a complete derivation of the bivariate formula, rather than just
a citation. Writef_(m,n)=p_((m+n)/2)((m−n)/2) whenm,n≥0 have equal parity,
and set the other coefficients tozero. LetF(w,z)=sum f_(m,n)w^m z^n/(m!n!).
The second finite difference of|j−k| in k is2 whenj=k andzero otherwise.
Consequently

(∂_w−∂_z)²F=2F.

Symmetry givesF(w,z)=F(z,w). Also, forr≥1,
p_r(r)=sum_(j=−r+1)^(r−1)(r−j)p_(r−1)(j)=rU_r,
because the signed first moment vanishes by symmetry. Therefore
F(w,0)=1+sum_(r≥1)rU_r w^(2r)/(2r)!=Q(w).

Setu=(w+z)/√2 andv=(w−z)/√2. The differential equation isF_vv=F, so
formallyF=A(u)coshv+B(u)sinhv. Symmetry forcesB=0. Onz=0 we havev=u,
and the already provedQ gives
A(u)coshu=Q(√2u)=coshu/(coshu−u sinhu).
Sincecoshu has constant term1, division is valid formally. Thus

F(w,z)=cosh((w−z)/√2)/
       (cosh((w+z)/√2)−((w+z)/√2)sinh((w+z)/√2)),

exactly as printed. The parity restriction is the admissible integer-index
interpretation of that sum; odd total-degree coefficients vanish on both
sides. This argument also proves uniqueness from the recurrence/PDE data.

## U33-c1 — V, real poles and all local expansion coefficients

From the univariate identity,
V(z)=1/(1−z tanhz)=1+zU(√2z)/√2.
HenceV=1+sum_(n≥1)V_n z^(2n)/(2n−1)! withV_n=2^(n−1)U_n, proving
the displayed coefficient conversion.

The functiong(x)=x tanhx increases strictly forx>0 because
g′=tanhx+x sech²x>0. It starts atzero and tends toinfinity, so a unique
positiveμ satisfiesg(μ)=1. It lies between1 and5/4: g(1)<1, while
exp(5/2)>1+5/2+25/8+125/48=443/48>9 gives tanh(5/4)>4/5 andg(5/4)>1.

At a rootμ, tanhμ=1/μ. Therefore the Taylor coefficients ofg nearμ satisfy
c0=1,
c1=tanhμ+μ(1−tanh²μ)=μ,
c2=(1−tanh²μ)(1−μ tanhμ)=0.
Expanding the last expression gives exactly the four terms printed forc2.
ThusV has principal part−1/(μ(z−μ)) there, with the corresponding reflected
principal part at−μ. The rational function2/(μ²−z²) has exactly these
two residues. This is the corrected subtraction; the original extra μ²
would not cancel the poles.

## U33-c2 — exclude every off-axis root and locate the imaginary roots

Writing
V(z)=coshz/H(z),  H(z)=coshz−z sinhz,
removes the apparent singularities at the poles of tanh. IfH(z)=0, then
z≠0 andcoshz≠0, so it is a genuine pole ofV. Setu(x)=cosh(zx) on0≤x≤1.
It satisfiesu″=z²u, u′(0)=0, andu′(1)=u(1). Multiplication by the complex
conjugate ofu and integration by parts yield

z² integral_0^1 |u|² = |u(1)|² − integral_0^1 |u′|².

The right side is real and the integral multiplyingz² is strictly positive
(u(0)=1). Hencez² is real: every zero ofH lies on the real or imaginary
axis. On the real axis the monotonicity already proved leaves only±μ.

Forz=iy, y>0, the equation iscosy+y siny=0, equivalentlyy tany=−1.
It has no solution in a positive-tangent half-period. On each interval
((k−1/2)π,kπ), k≥1, y tany increases from−infinity tozero, since
its derivative is(y+sinycosy)/cos²y>0. There is exactly one rootμ_k there.
These and their negatives exhaust the imaginary axis. All roots are simple:
H′(z)=−z coshz is nonzero at a zero ofH. Thus the book's final tentative
global pole list actually has this complete independent proof; no unproved
root-location conjecture is being used to establish the asymptotic.

Moreoverμ1>5π/6, because at that pointy tany=−5π/(6√3)<−1 and the
function is increasing. Sinceπ>3 andμ<5/4, we haveμ1>5π/6>5/2>2μ.
This proves specifically the printed assertion that±μ are the only roots
in|z|≤2μ, without relying on a numerical root search or a plotted contour.

## U33-c3 — coefficient asymptotic and exact decimal certificates

After subtracting2/(μ²−z²), the remaining function is analytic on a
neighborhood of the closed disk|z|≤2μ: all other poles lie at distance
at leastμ1>2μ. Cauchy's coefficient bound therefore gives

[z^(2n)]V = 2/μ^(2n+2) + O((2μ)^(−2n)).

Multiply by2^(1−n) to convertV_n/(2n−1)! toU_n/(2n−1)!, obtaining

U_n/(2n−1)! = 2^(2−n)/μ^(2n+2)
              + O(2^(−n)(2μ)^(−2n)).

This proves the public error-term correction. Dividing by the positive
leading term gives relative errorO(4^(−n)), exactly the exercise's requested
precision. Removable tanh poles inside the contour have already been
accounted for by theH representation.

All40 printed decimal places and their directional signs were certified
in `results/upup-targeted.json`. A high-precision approximation only chose
a candidate interval with endpoints separated by10^(−55); exact rational
Taylor bounds then proved opposite signs of
f(x)=(x−1)exp(2x)−(x+1) at those endpoints. For the positive exponential
argumentw, the certificate uses
S_K≤expw≤S_K+(w^(K+1)/(K+1)!)/(1−w/(K+2)), K=80.
The upper tail is valid because every subsequent term ratio is at most
w/(K+2)<1. Strict monotonicity ofg proves the interval contains the uniqueμ.
The printedμ decimal lies above it by less than10^(−40), establishing the
minus suffix. Squaring the endpoints shows thatλ=√(μ²−1) lies above its
printed decimal by less than10^(−40), establishing the plus suffix.

The printedμ1≈2.79839 was checked by rational sine/cosine Taylor bounds:
cosy+y siny is positive at2.798385 and negative at2.798395. Uniqueness in
the already proved interval then certifies rounding to those five places.
Geometric upper bounds on the absolute Taylor tails make this a signed
interval certificate, not an unverified floating-point result. One small
nice15 run produced all these certificates and the recurrence rows.

## U33-d — complete whirlpool bijection, including its inverse

First normalize the whirlpool so its lower-left entry iszero, as in the
referenced note. The exercise's upper-left-zero version is obtained by
interchanging the two rows, which preserves the vortex property. A one-column
normalized matrix is necessarily[[1],[0]] and maps to the one-element
sequence1.

For a normalized2×k matrixP_k, k>1, call its first two top entriesx,y and
the entry belowyz. The first block has boundaryx,y,z,0. All three positive
entries are distinct; its odd-ascent condition is precisely
x<y<z orx>y>z. Remove the first column, whose entries arex andzero, and
compress the remaining ranks by
f_x(v)=v−1−[v>x]. LetL=2k−2 andw=f_x(z). Subtractw moduloL from all
remaining entries, giving a normalized whirlpoolP_(k−1). Both compression
and this translation preserve every remaining vortex by W31-e.

Let its first top entry ber. Then
r=(f_x(y)−f_x(z)) modL. Ifx<y<z, this isL+y−z and lies in[y−1,L−1].
Ifx>y>z, it isy−z and lies in[1,y−1]. Recursively encodeP_(k−1) as a
sequence on1,...,2k−3, then order-embed that sequence into the set of positive
integers1,...,2k−1 excludingx,y, and prependx,y. Its first following value
has rankr in that remaining set. Whenx<y there arey−2 remaining values
below y, so r≥y−1 makes the following value exceedy. Whenx>y there are
y−1 values belowy, so r≤y−1 makes it smaller thany. Thus the new first
triple is monotone in the same direction asx→y; all later paired comparisons
hold by induction. This proves the output is up-up-or-down-down.

Conversely, take any such sequence on1,...,2k−1. Its first two valuesx,y
are distinct. Normalize the remaining sequence to1,...,2k−3 and recursively
decode it toP_(k−1), with first top entryr. The first monotone triple says
r≥y−1 whenx<y andr≤y−1 whenx>y. Recover uniquely

z=L+y−r ifx<y;  z=y−r ifx>y.

In the first casey<z≤2k−1; in the second1≤z<y. Thereforez is a valid
positive value distinct fromx,y. Setw=f_x(z), addw moduloL toP_(k−1),
expand by the inverse off_x, and prepend the column(x,0). The second column
has topy and bottomz by the defining congruence forr. Its first block is
a vortex becausex,y,z are monotone; all other blocks were preserved by the
inverse translation and order expansion. This constructs a unique normalized
P_k and reverses every encoding operation. Induction proves a bijection,
including existence, uniqueness and both inverse identities for allk≥1.

The note's worked example[[5,7,6,9,3],[0,8,4,1,2]] gives successive pairs
(5,7),(7,6),(1,2),(3,2), followed by1. Order expansion yields
5,7,9,8,1,2,6,4,3. The fixed certificate checks this example and its inverse;
the general proof does not depend on it.

Finally, adding a common value modulo2n acts freely on whirlpool permutations
of{0,...,2n−1}, preserving vortices by W31-e. Each orbit has2n elements and
exactly one with its specified first entryzero. The proved bijection says
there areU_n such normalized matrices. Hence the full count is2nU_n,
as required. Forn=1 this gives the two orderings of a single column; n=0
is outside the exercise's2n−1-element definition and is not used here.
