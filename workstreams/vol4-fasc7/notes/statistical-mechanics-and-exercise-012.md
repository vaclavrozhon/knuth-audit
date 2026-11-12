# Statistical mechanics, all 48 table entries, and every part of exercise 12

Source: main p. 4–5 (file 19–20), exercise 12 on p. 113 (file 128),
answer on p. 159 (file 174), first digital edition. All four original
pages were inspected. The public corrections of 9 May and 22 October
2026 rename the site-weighted generating functions, define w=z^B,
and reverse the two diagonal magnetization coefficients' signs.
They are applied below and are not new findings. All relevant errata
layers, including the primary source and its minor-correction list,
were checked. Historical claims about Lenz, Ising, Boltzmann, and the
origin of survey propagation, and the cited 2009 textbook's exposition,
are explicitly excluded as bibliography. The mathematics here is
derived independently, without requiring those external texts.

Throughout the Ising calculation N≥1, B is a fixed real number, and
z>0. This is exactly the domain needed for z=exp(−β) with finite real
β. General real B need not give a polynomial with integer exponents;
the finite sum of real powers is nevertheless differentiable on z>0.
The probabilistic normalization requires a nonempty finite set of
configurations, as in the spin spaces and all examples here. An empty
CSP domain instead gives no configurations, partition sum zero, and
no normalized probability distribution; it can be rejected as UNSAT
before this probabilistic interpretation. Empty products with no
variables have one configuration, not zero.

## S-P01: Local Ising energy and the spin-flip statement

Formula (9) assigns −σ_jσ_(j+1) to each neighboring pair and −Bσ_j
to each particle. It therefore is a sum of local contributions. Each
σ_j is one of −1,+1, so there are exactly 2^N independent configurations.
If an interior site has σ_(j−1)=σ_(j+1)=−σ_j, its two interaction
contributions are initially +1,+1. Flipping σ_j changes them to −1,−1,
and changes its field contribution from −Bσ_j to +Bσ_j. Every other
term is unchanged. Thus

    E(after)−E(before) = −4+2Bσ_j = 2(Bσ_j−2),

which is negative under the printed inequality. The two-neighbor
premise implicitly requires 2≤j≤N−1; it says nothing about an endpoint.
For an endpoint with one opposite neighbor the corresponding difference
would be −2+2Bσ_j. Equality Bσ_j=2 in the interior gives a tie rather
than a strict improvement. The mathematical assertion in the physical
phrase “tend to” is the stated strict energy reduction.

## S-P02: Every energy in (10) and the table

An indicator [R] is one exactly when its relation is satisfied and
zero otherwise. The negative sum of the three indicators is therefore
exactly minus the number of satisfied constraints. For each printed
word abcde, evaluate its projections ace,ad,bde in

    R1={BAN,BUD,SIN}, R2={BE,SE,SO}, R3={COD,CON,LED}.

`results/statistical-mechanics-targeted.json` records all 48 words,
all three projection strings, all three membership bits, and the
printed and independently summed energies. Every printed row was
checked, not a sample. The word set was also checked to be precisely
BS×CL×AIU×EO×DN, without repetitions or omissions. The source image
confirms the table layout, signs and words used by the extraction.
The short reproducible calculation is
`check_statistical_mechanics_targeted.py`, executed once with nice15.

There is an independent count of the resulting coefficients. The two
words satisfying all three constraints are exactly BLUED and SCION,
by the complete argument C-P01 in the earlier CSP note. A word with
zero satisfied constraints must fail R2, so it has first coordinate
B and fourth O. If its second coordinate is C, R3 is true for either
language, so its second coordinate must be L. R1 then excludes the
pairs (A,N) and (U,D) in coordinates 3,5, leaving exactly four words:
BLAOD, BLIOD, BLION, BLUON. This proves n_3=2 and n_0=4, where n_i
counts words satisfying i constraints.

R1 is satisfied by 3·2·2=12 words, R2 by 3·2·3·2=36, and R3 by
3·2·3=18. Summing the number of satisfied constraints over all words
therefore gives 66. The remaining counts satisfy

    n_1+n_2=48−2−4=42,
    n_1+2n_2=66−3·2=60.

Consequently n_2=18 and n_1=24. This independently proves the printed
generating function

    G(z)=2z^(−3)+18z^(−2)+24z^(−1)+4.

The proof of the coefficient counts does not substitute for the 48
individual table checks; both are provided.

## S-P03: Partition probabilities, both limits, and the CSP conclusion

For any nonempty finite configuration set, real finite energies E(s)
and finite real β, each exp(−βE(s)) is strictly positive. Their sum Z
is positive and finite, so dividing each by Z gives positive weights
summing to one. Substitution z=exp(−β) makes Z(β)=G(z) term by term.
As β→0 each weight tends to 1, hence each normalized probability
tends to the uniform value 1/number-of-configurations.

Let E_min be the minimum and let g≥1 configurations attain it. Divide
all weights by exp(−βE_min). The denominator becomes

    g + sum_(E(s)>E_min) exp(−β(E(s)−E_min)).

Every gap is positive. Thus a ground state's probability tends to 1/g,
while each other state's probability tends to zero exponentially.
The ratio of a ground state's weight to that of a state with gap Δ
is exactly exp(βΔ), proving the text's comparison. If all energies
are equal, there are no nonground states and the distribution remains
uniform; this is included without a nonexistent positive gap.

In the 48-state example each of the two ground states has probability

    p(β)=1/(2+18exp(−β)+24exp(−2β)+4exp(−3β)).

At β=0 the denominator is 48 and its derivative is −78. Differentiating
the reciprocal gives p(0)=1/48 and p′(0)=78/48²=13/384. Analyticity
near zero then proves the printed remainder O(β²). For q=exp(−β)→0,

    p(β)=(1/2)/(1+9q+12q²+2q³)=1/2−(9/2)q+O(q²),

which proves the other printed asymptotic coefficient and order.

For m constraints, the analogous energy is −sum_j[R_j], an integer
between −m and zero on every configuration. The energy equals −m
exactly for satisfying assignments. When such assignments exist they
are precisely the minima; otherwise minimizing energy is exactly
maximizing the number of satisfied constraints. This justifies both
the satisfiable and unsatisfiable conclusions, subject to the explicit
nonempty-configuration condition for discussing probabilities or minima.

## E12(a)-1: Transfer matrix, induction, and the two printed base cases

Put w=z^B and order the two spin states as −1,+1. Let

    l=(w,w^(−1)),  e=(1,1)^T,
    T = [[w/z, z/w], [wz, 1/(wz)]].

The initial weight for spin σ_1 is z^(−Bσ_1), giving l. The transition
from σ to τ has weight z^(−στ−Bτ), giving precisely the four displayed
entries of T in that order. Multiplying weights along a spin sequence
counts the first spin's field once and thereafter each new spin's
field and its incoming interaction once, so its product is exactly
z^E. Summing over successive spin values is ordinary matrix
multiplication. This proves by induction, including N=1,

    G_N(z)=l T^(N−1) e.

Directly G_1=w+w^(−1). For N=2 the equal-spin configurations have
weights w²/z and w^(−2)/z; the two unequal-spin configurations both
have weight z. Hence G_2=w²/z+2z+w^(−2)/z, exactly as printed.

## E12(a)-2: Diagonalization and the coefficients a,b

Define

    u=(w+w^(−1))/(2z),  d=(w−w^(−1))/(2z),
    v=d²+z²,  δ=sqrt(v)>0,  λ=u+δ,  μ=u−δ.

Writing T=uI+Q gives Q=[[d,z/w],[wz,−d]], and direct multiplication
gives Q²=vI. Thus λ and μ are distinct eigenvalues. The vector
(t−1/(wz),wz)^T is an eigenvector for eigenvalue t: its second
coordinate equation is immediate, and its first is exactly the
characteristic equation. Taking t=λ,μ gives the two columns of the
printed S. Its determinant is wz(λ−μ)=2wzδ>0. Hence S is invertible
and T=S diag(λ,μ) S^(−1), with no diagonalization exception on z>0.

The scalar sequence lT^(N−1)e consequently satisfies the order-two
recurrence with characteristic roots λ,μ, and it has the form
aλ^(N−1)+bμ^(N−1). The printed coefficients are

    a=λz+(z−z³)/δ,    b=μz−(z−z³)/δ.

Their sum is z(λ+μ)=w+w^(−1)=G_1. Also det T=z^(−2)−z², so

    λ²+μ²=(w²+w^(−2))/z²+2z².

It follows that

    aλ+bμ=z(λ²+μ²)+2(z−z³)
          =(w²+w^(−2))/z+2z=G_2.

These two base values determine the recurrence completely, proving
both coefficients for every N≥1. This checks the intermediate
diagonalization and coefficient formulas, not just the final result.

When B=0, w=1, δ=z, λ=z^(−1)+z, μ=z^(−1)−z, a=2 and b=0. Thus

    G_N(z)=2(z^(−1)+z)^(N−1).

This supplies the complete closed form for part (a)(i), in addition
to the displayed simplification of λ.

## E12(b): Exact finite-size energy, including the differentiation step

Termwise differentiation of the finite sum gives
zG′_N(z)=sum_s E(s)z^E(s), so the mean energy per particle is indeed
zG′_N/(NG_N). B is held fixed: w depends on z and cannot be treated
as a constant during the differentiation. To make the answer's
“differentiate and plug in” fully explicit, set

    u′=[B(w−w^(−1))−(w+w^(−1))]/(2z²),
    d′=[B(w+w^(−1))−(w−w^(−1))]/(2z²),
    δ′=(dd′+z)/δ,  λ′=u′+δ′,  μ′=u′−δ′,
    f=z−z³,  f′=1−3z²,
    a′=zλ′+λ+f′/δ−fδ′/δ²,
    b′=zμ′+μ−f′/δ+fδ′/δ².

For N≥2 the exact answer is z/(NG_N) times

    a′λ^(N−1)+b′μ^(N−1)
    +(N−1)[aλ^(N−2)λ′+bμ^(N−2)μ′].

For N=1 omit the second line; do not evaluate a negative power of
a possibly zero eigenvalue and multiply it by zero. Scalar powers
with exponent zero are 1, including μ=0. This covers z=1 as well.
Then substitute z=exp(−β). Equivalently the exact result is
−(1/N)∂_β ln G_N(exp(−β)), since B is fixed.

For B=0 this simplifies to

    energy/N = ((N−1)/N)(z²−1)/(z²+1)
             = −(1−1/N)tanh β.

For N=1 it is −B tanh(βB). At β=0 it is zero for every N,B, also
seen directly from the uniform independent spins: each field spin
and each adjacent product has mean zero. These boundaries verify
the differentiation convention and factors of N.

## E12(c): Dominant eigenvalue and the full asymptotic answer

Since u>0 and δ>0, λ>0 and |μ|<λ. The coefficient a is positive.
For a direct proof, the eigenprojector P=(T−μI)/(2δ) has all entries
positive: δ>|d| implies μ<min(T_11,T_22), and the off-diagonal
entries of T are positive. Therefore a=lPe>0. Consequently, with
fixed z>0 and fixed B,

    G_N=aλ^(N−1)(1+(b/a)(μ/λ)^(N−1))
       =aλ^(N−1)(1+O(ρ^(N−1))),  ρ=|μ|/λ<1.

The functions are differentiable in a neighborhood of that fixed z.
On a sufficiently small neighborhood the ratio remains bounded in
magnitude by some constant below one, so differentiating the remainder
contributes O(Nρ_1^(N−2)) for a fixed ρ_1<1. Thus

    G′_N/G_N=(N−1)λ′/λ+a′/a+O(Nρ_1^(N−2)),
    zG′_N/(NG_N) → zλ′/λ.

This justifies the printed omission of μ and the derivative step,
including its error after division by N. The additive form is valid
also at a zero of λ′; a ratio-style asymptotic symbol at that point
is read through this precise formula. The limit is at fixed finite
β and B, not uniform in a simultaneous zero-temperature limit.

At z=exp(−β), put h=βB, s=sinh h, c=cosh h, and
q=sqrt(s²+exp(−4β)). Substitution into u,δ gives exactly the printed

    λ=exp(β)c+sqrt(exp(2β)s²+exp(−2β))
     =exp(β)(c+q).

In particular q>0. Differentiating this expression explicitly yields
the limiting energy per particle

    −∂_β ln λ
    =−1−B s/q+2exp(−4β)/(q(c+q)).

Indeed q′=(Bsc−2exp(−4β))/q, and the B-dependent terms in
(c′+q′)/(c+q) simplify to Bs/q. This proves the asymptotic energy
requested in (c), rather than leaving the derivative unevaluated.
For B=0 it reduces to −tanh β, matching the exact finite-size
expression. At β=0 it is zero.

## E12(d)-1: Site generating function and the two corrected coefficients

Use the corrected notation calG_k=sum_s σ_k z^E(s), for 1≤k≤N.
Inserting X=diag(−1,1) at the kth spin multiplies exactly that
configuration's weight by σ_k. Therefore

    calG_k=l T^(k−1) X T^(N−k) e.

Substituting T=S diag(λ,μ) S^(−1) and Y=S^(−1)XS gives precisely
the printed expression with the two diagonal powers and Y between
them. To verify every resulting coefficient, set

    P=(T−μI)/(2δ),  Q0=I−P.

These are the rank-one eigenprojectors, with T^r=λ^rP+μ^rQ0 for
r≥0. For any rank-one projector R, writing it as rℓ/(ℓr) shows
RXR=trace(RX)R. Here the diagonal entries of P give
trace(PX)=−d/δ; those of Q0 give trace(Q0X)=d/δ. Thus

    ahat=lPXP e=−da/δ=(w^(−1)−w)a/(2zδ),
    bhat=lQ0XQ0 e=db/δ=(w−w^(−1))b/(2zδ).

These are exactly the signs in the 22 October 2026 correction. The
opposite signs in the first digital printing are already known and
are not a new finding. Neither this correction nor the renaming of
calG_k is silently omitted from the argument.

## E12(d)-2: Both cross terms and the printed coefficient c0

Let c1=lPXQ0e and c2=lQ0XPe. Reversing a spin sequence leaves its
energy unchanged, so calG_1=calG_2 for the two-site chain. In the
spectral expansion their difference is (c2−c1)(λ−μ). Since λ≠μ,
we have c1=c2=c0. This proves why the two printed cross terms have
the same coefficient, a point not implied by diagonalization alone.

For N=1, expansion of lXe gives

    ahat+bhat+2c0=w^(−1)−w=−2zd.

From the already proved coefficients,
a−b=2δz+2(z−z³)/δ. Substituting ahat+bhat=−d(a−b)/δ gives

    2c0=−2zd+d(a−b)/δ=2dz(1−z²)/δ²,
    c0=(w−w^(−1))(1−z²)/(2v),

which is the printed coefficient called c. We consequently have
the complete site formula

    calG_k=ahat λ^(N−1)+bhat μ^(N−1)
           +c0 λ^(N−k)μ^(k−1)+c0 λ^(k−1)μ^(N−k).

This proof covers the coefficients as well as the powers of both
cross terms, including k=1,N and N=1.

## E12(d)-3: Averaging, the geometric sum, and the final limit

Each cross-term sum over k is the same finite geometric sum

    sum_(k=1)^N λ^(N−k)μ^(k−1)
      =(λ^N−μ^N)/(λ−μ)=(λ^N−μ^N)/(2δ).

The identity follows by multiplying by λ−μ and telescoping, so it
also holds when μ=0. Adding both cross terms, dividing by N and then
by G_N gives exactly the corrected finite-size average

    mean spin = [(ahat+c0λ/(Nδ))λ^(N−1)
                  +(bhat−c0μ/(Nδ))μ^(N−1)] / G_N.

The previous positive-a and dominant-eigenvalue arguments imply that
the limit is ahat/a=−d/δ. Substituting z=exp(−β) gives

    mean spin → sinh(βB)/sqrt(sinh²(βB)+exp(−4β)),

exactly the printed final answer. At B=0 every site generating
function is zero by global spin reversal, and the formulas give
d=c0=ahat=bhat=0. At β=0 the finite-size and limiting means are
zero. For N=1 the unsimplified numerator is w^(−1)−w, giving
tanh(βB), as it should. All denominators used above are nonzero on
the stated domain. These checks close the requested site quantity,
its average, and its asymptotic value separately.

## Small corroboration and limits of the saved check

The one nice15 run also tested five fixed instances: (N,z,B) equal to
(1,1/2,2), (2,1/2,−1), (5,1/2,0), (4,1,2), and (5,2,1). Direct sums
over their 86 configurations in total agree with G_N, its energy
derivative, every calG_k and the averaged formula. These instances
cover N=1, N=2, vanishing field, μ=0, and a negative μ. This is a
small targeted check of transcription and boundary arithmetic; the
general arguments above, not these examples, establish the formulas.
No large enumeration, parameter sweep, or restart was performed.
