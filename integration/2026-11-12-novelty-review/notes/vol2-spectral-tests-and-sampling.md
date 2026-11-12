# Publication review: spectral tests and sampling, C0036–C0056

Reviewed November 12, 2026. All twenty confirmed cards in this range
remain supported; C0042 was already outside the confirmed-card scope.
The reports and decisive original pages were reread, together with all
four historical/current correction layers and the current TeX source.
No matching additional repair or explicit prior report was found. This
is a bounded search result, not a claim of absolute priority.

| Card | Assessment and limits |
| --- | --- |
| V2-C0036 | The July 2003 replacement of the last lines of p. 577 omits a binary family of potency-two exceptions. For `m=8q,a=4q+1,c=1`, the dual vector `(1,0,-1)` has squared norm 2; for `q=1` the full orbit is `0,1,6,7,4,5,2,3`. Padding with zero also gives the four-dimensional exception. The complaint concerns the replacement text, not the superseded original typo. |
| V2-C0037 | For `m=131,a=97`, the largest continued-fraction quotient is 5, while the dual vector `(5,4)` has squared norm 41. Hence the asserted strict bound would require `41/131>10/31`, which is false. The multiplier is primitive: its powers at exponents 65, 26 and 10 are 130, 89 and 80 modulo 131. The proposed weaker bound with denominator `A+2` is consistent with the proof. |
| V2-C0038 | The number of parallel hyperplanes meeting the unit cube can change when the increment changes, although their spacing does not. For `m=4,a=1` and normal `(1,-1)`, the unshifted lattice has one such plane and the increment-one translate has two, both occupied. The full-period example `m=256,a=137,c=1` versus `c=187` also has 19 versus 20 occupied planes for normal `(18,-2)`. |
| V2-C0039 | The stated version of Minkowski's theorem includes an arbitrary convex symmetric set of volume equal to `2^t`. The open cube `(-1,1)^t` disproves that formulation. Require closedness at equality or strict volume. The subsequent application to balls can be repaired by a limiting argument, so this is a qualification of the theorem statement, not failure of the final spectral bound. |
| V2-C0040 | Exercise 13 refers to quadratic form (19), but the quadratic form is (17); (19) is the duality relation. Retain as a cross-reference typo. |
| V2-C0041 | The proposed hexagonal basis has determinant `2/(sqrt(3)m)` instead of `1/m`. Its length must be `sqrt(2/(sqrt(3)m))`. The stated Hermite constant and separate three-dimensional construction remain correct. |
| V2-C0043 | The two displayed Gaussian-integer products are interchanged: the products are `-4983+75820i` and `35825-67008i`. A unit/sign is also required in the printed absolute-value identification. The eventual chosen vector and multiplier are correct. |
| V2-C0044 | The coordinate bound in answer 16 must use `f(X)`, where `f(X)=norm_1(XU)`, rather than `f(Y)` for `Y=XU`. With rows `(1,-1),(0,2)` and `X=(4,3)`, the printed bound implies `3<=2`. Norm updates also belong in S4/S5, not S4/S7. These repairs preserve the intended unshifted-lattice algorithm; the wrong step reference alone is not claimed to produce a demonstrated wrong numerical result. |
| V2-C0045 | The off-diagonal scalar product for `V=mI+yJ`, `y=(1-m)/3`, is `(1-m^2)/3`, not its negative. At `m=64` it is -1365. The test uses its absolute value, leaving the example's conclusion intact. |
| V2-C0046 | For `m=16,a=3`, the odd-seed orbit is `1,3,9,11`. Its difference lattice has dual condition `u+3v=0 mod 8`, with minimum squared norm 8. The proposed reduction modulo `m/4=4` instead gives 2. Reflecting alternate coordinates does not put all starting states in one class modulo 4. The 2005 seed-residue correction does not repair this distinction. The displayed RANDU minima happen to agree and are not themselves counterexamples. |
| V2-C0047 | The exercise explicitly includes dimension two, but the answer changes only S9, which is never reached there. For `m=5,a=2` the two independent minimum pairs are both required. The additional uniqueness statement fails in dimension six for the table's `a=2^18+1,m=2^35`: `(1,-1,0,0,-1,1)` and `(1,0,-1,-1,0,1)` are distinct endpoint-nonzero minimum vectors of squared norm 4. The numerical table remains valid. |
| V2-C0048 | The allowed case `m=2,a=c=1` yields the constant sampled triple `(0,0,1/2)`. Its periodic difference lattice is `Z^3`, whereas the displayed basis has determinant 2. Replace 4 by `gcd(4,m)` or require `m>=4`. Retain as a small-modulus exception. |
| V2-C0049 | Subtracting `1/(pi x)` from the cosecant summand gives the asymptotic `(log M+gamma+log(2/pi))/pi+O(1/M)`. The integral estimate omits the nonvanishing `gamma/pi` term, so its claimed error is false. The leading logarithm is correct; the constant is standard and is not presented as newly discovered mathematics. |
| V2-C0050 | The Gauss-sum equality requires a nontrivial character. At frequency zero the sum is -1, of magnitude 1 rather than `sqrt(m)`. The upper bound needed for the discrepancy argument survives. |
| V2-C0051 | The premise is `v^2>=k>=2`, not `v>=k>=2`, because `v` is Euclidean length and `k` counts nonzero integer coordinates. The vector `(1,1)` already distinguishes them. The final product inequality follows from the corrected premise; an attained coordinate-box optimizer is unnecessary. |
| V2-C0052 | If `m=3k` with even `k`, uniform reduction modulo `k` gives probability 1/2 of landing below `k/2`, not 2/3. The example needs `k` near `2m/3`. The 2001 correction to the rejection comparison addresses a different expression. |
| V2-C0053 | The printed logistic-map density integrates to `sqrt(pi/2)`, not 1. The normalized density is `1/(pi sqrt(x(1-x)))`. The recurrence and angle-doubling explanation are unaffected. |
| V2-C0054 | Even after the 2005 factor-of-two correction, the ratio-of-uniforms exterior-area formula omits a second horizontal interval for positive `x`. At `x=1`, the intersections occur at `r` and `1-r`, where `r=(1-sqrt(1-2/e))/2`; the true area is twice the printed result. An integral of the positive part over the whole unit interval repairs it, or the domain can be restricted. The actual negative-parameter timing example is unaffected; no new global optimizer is asserted. |
| V2-C0055 | The recycled-uniform average for Brent's method is approximately 1.37746, not 1.37446. The earlier certified forty-term interval is `(1.377460505889,1.377460505893)`, with a tail below `4*2^-40`. Brent's original paper already contains both the wrong value in equation (4) and the correct value in a program comment on the same page. Retain only the erroneous TAOCP transcription/value, explicitly acknowledging that the correct number was already published. |
| V2-C0056 | The continuous-binomial integral uses an undefined exponent parameter `n`; the other factors and the definition use `t`. Replacing `n-x` by `t-x` recovers the stated binomial cumulative distribution at integer arguments. |

Original typesetting re-inspected: pp. 98, 102–103, 109, 115–117, 130,
140, 577–584 and 588; the relevant July 2003 replacement and 2005
corrections; and Brent's original p. 705. Existing exact proofs and
certified calculations were checked and reused without a new large run.

Public searches paired Knuth/TAOCP and error/errata with spectral tests,
`131 97`, potency, hexagonal scale, Minkowski p. 579, translated
hyperplane counts, the Gaussian-product coordinates, L1/S7, scalar-product
signs, `3 mod 8`, all shortest vectors, stride four/modulus two, Gauss sums,
norm squares, cosecant constants, modulo bias p. 584, logistic density,
ratio-of-uniforms p. 588, the continuous-binomial formula and both Brent
decimal values. Results were inspected on the review date; book copies,
standard theory and unrelated corrections were not treated as independent
reports of these exact book defects.

For C0055, the primary [Brent paper](https://maths-people.anu.edu.au/brent/pd/rpb023.pdf)
and [author's publication page](https://maths-people.anu.edu.au/~brent/pub/pub023.html)
were opened. The latter has no explicit erratum for the two decimal
values. The source's correct program comment is a necessary qualification
of novelty, even though no explicit prior TAOCP correction was found.
