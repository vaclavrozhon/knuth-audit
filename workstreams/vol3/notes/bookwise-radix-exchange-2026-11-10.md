# Radix exchange and the remaining exchanging-sort material

Reviewed pp.123–134, exercises33–40 and45–54, and paired answers634–638.
Earlier detailed bubble/cocktail/Batcher evidence is retained for
pp.105–114,128–130 and exercises1–16,43–44; the new Quicksort-variant
note completes28–32,41–42,55–56. Thus all56 original exercises in5.2.2
have been paired with their answers under the current review standard.

For Algorithm R, checked the single-inspection scan invariant, crossing
indices, all-one/all-zero/single-zero cases, increasing bit index and
implicit left boundary on popping. Each stack entry has a distinct
pending bit depth, giving the stated m-1 bound. The code's difference
registers track the stated indices; the published correction to a comment
does not change the instructions. Summing its instruction costs first
gives 11A+16S+8B+8C-7G+2K-L-3R-X+13, which reduces to the printed
formula using S=A-G-K-L-R. Table3's22 stages have total subfile length82
and17 exchanges; the displayed transitions and stopping bit7 agree.

Checked the balanced full-key case and the binomial split recurrences,
the transform involution and self-dual generating-function description,
and the special-case frequencies in answers35–38. The known correction
to X_N=A_N/2 is required; it is not a new finding. The insertion cutoff
and equal-key test in40 give the intended termination behavior.

For the asymptotic section, checked the finite sum to positive-scale
series, the two error ranges and bounded dyadic sum, gamma contour
orientation, omitted poles in45, interchange of absolutely convergent
series, double-pole coefficient and periodic term, and the nonzero
remainder exposed by the doubling identity. The zero average of the
oscillation is understood over a logarithmic period, not as a statement
about uniformly sampled integers. Existing **C0013** covers the omitted
exact remainder in answer46; the corrected asymptotic use in47–49 is
consistent. The current corrections to49 and the numerical oscillation
bounds in50 were applied rather than recorded as findings.

Read the zeta/gamma residue steps in51–52, the biased binomial transform,
the special golden-ratio roots in53, and Rice's contour/finite-difference
formula in54. Existing **C0014** covers the pole exclusion and spectral
normalization in53. New **C0033** is a local sign error in the Stirling
correction in52; the displayed final divisor-sum asymptotic is unaffected
at its requested precision. Existing **C0028** in44 and **C0029** in16
remain covered by their detailed earlier arguments; those computations
were not rerun.

Explicit limits: no historical machine benchmark or priority claim was
independently replicated. The cited Wang mean-of-three threshold result
(1.082 N lg N), empirical interval-exchange performance and predictions
about its analyzability are treated as attributed external/historical
statements. General geometry and convergence of the biased complex-root
sum in53 are not re-established; the exact counterexample in C0014 uses
the simple p=q=1/2 case. Standard gamma/zeta facts and contour machinery
are accepted with their usual domains, not proved anew. The research
exercise9 stays an explicit exception, as previously adjudicated.

Fresh official errata are identical to the archived sources. No new
large computation or proof inventory was started. Next:5.2.3, sorting
by selection, beginning on the shared printed page138.
