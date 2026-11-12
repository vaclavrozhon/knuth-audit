# Publication review: statistical-test findings C0016–C0035

Reviewed November 12, 2026. C0017 was already a candidate and is outside
the requested confirmed-card review. All other nineteen cards in this
range remain supported, with the qualifications below. The individual
notes were reread, the decisive original pages were viewed again, and
all four historical/current correction layers plus the current TeX source
were checked. No matching additional correction or prior public report
was found. This is a bounded search result, not proof of priority.

| Card | Assessment and limits |
| --- | --- |
| V2-C0016 | Pearson's own p. 45 explicitly describes obtaining published roulette records from Le Monaco; his p. 54 table links them to the 1900 article. TAOCP p. 55 describes personal experience of these observations. Retain the source-attribution correction, without claiming Pearson never visited Monte Carlo or that the source history itself is newly discovered. |
| V2-C0018 | With two uniform points, the first labeled circular spacing is their absolute difference, whose probability of exceeding 1/2 is 1/4. The printed formula gives 1/2. The origin-containing final gap is size-biased; starting labels at a designated observation repairs the joint distribution. The unordered gaps and many subsequent test results survive. |
| V2-C0019 | At zero arguments the exponential moment must be 1, but the displayed expression on p. 565 gives `2^(-n/2)`. For `n=3`, the cyclic correlation is identically -1/2, contradicting the next displayed first and second moments. The concluding variance formula is correct. Dixon's original paper remains unavailable; the mistake is attributed only to the book's formulas. |
| V2-C0020 | The actual cell mean after rounding the number of cells is `n/ceil(1/delta)`. The note's sequence of sample sizes makes the claimed lower bound approach that mean in standard-deviation units, giving failure probability tending to 1/2. The concentration assertion therefore fails for a fixed parameter, not just for a poorly chosen varying constant. The main variance asymptotic has a separate valid proof. |
| V2-C0021 | The explicitly floating-point collision algorithm can sum its probabilities to `1+2^-52` in binary64 for `n=2, m=10` or `m=10018`. It then emits a negative probability and a literal inner loop passes the final threshold. An immediate global stop avoids the latter, but not the former. This is a numerical-guard issue, not a counterexample in exact arithmetic. |
| V2-C0022 | The count of at most `k-1` small gaps includes zero. The missing `G_0` on p. 566 gives 1/2 instead of 1 for `n=k=2, s=1/4`. The subsequent final distribution formula already has the correct value. |
| V2-C0023 | Distinct irrational coordinates `(a/3,5a/6,1-7a/6)`, `a=sqrt(2)/4`, map to `(a,a,1-2a)`. Thus the next strict-order digit on p. 567 is undefined. The exceptional set has measure zero, but contains irrational points. A tie rule or a condition excluding ties in every iterate is needed. |
| V2-C0024 | For two birthdays in three days the two circular gap lengths are always different, so the probability of no repetition is 1. The printed difference on p. 568 gives 1/3. The two disjoint contributions must be added; the numerical table in the main text is already correct. |
| V2-C0025 | After applying the global 2021 Bernoulli convention and local corrections, the Euler derivative still has `j!` instead of `(j-1)!` and the wrong sign on the regular sum. With `n=1,j=2`, its leading term is twice the true double pole and its constant term has the opposite sign. The final partition asymptotics are unaffected. |
| V2-C0026 | The 2004 change from `j>=8` to `j>=3` is itself wrong: the cubic coefficient is `1/(3 sqrt(n))+O(n^(-9/2))`, not `O(n^-3)`. This is explicitly a defect in the erratum, not the uncorrected original threshold. |
| V2-C0027 | Quasipolynomial continuation gives `q_n(m)=(-1)^(n-1) p_n(-m)`. For `n=2,m=3` the two quantities printed as equal are 1 and -1. The missing factor cancels another sign when obtaining the correct final asymptotic. |
| V2-C0028 | Replacing the partition integrand by its distinct-parts version adds `N log z`, where `N=n(n+1)/2`. On the stated contour its linear coefficient increases by `N delta`, of order `n^-1/2`; the printed increment is of order `n^1/2`. The exact substitution settles this independently of the derivative typo. |
| V2-C0029 | For a degree-two primitive binary recurrence and a window of one sign, the third moment is 1/3. The intermediate formula on p. 572 gives 1 because its first term lacks division by the period. The exercise statement and following numerical example are correct. |
| V2-C0030 | The generating function for words avoiding `ab` and `bc` has numerator 1. The printed `1+z` already counts `m+1` one-letter words over an `m`-letter alphabet. The asymptotic constants and subsequent test calibration correspond to the correct numerator. |
| V2-C0031 | The first coefficient on p. 571 counts the opposite tail; the linear term of the stated logarithm has the opposite sign; the normalized Gaussian integral needs reciprocal `sqrt(2 pi)`; and the final remainder needs `m+3n`, not `m-3n`. The first contour identity through +1 is correct. These are four defects in one derivation, not four cards or a refutation of its final asymptotic. |
| V2-C0032 | The Cauchy bound needs `sigma(1,k,0)^2` on its right. Taking `h=2,k=5,c=1` makes the printed version demand `9/25<=0`. The exercise conclusion is correct. |
| V2-C0033 | The Fibonacci table on p. 576 gives tail probabilities while the adjacent formula and comparison row give exact run lengths. The first five exact probabilities are `1/2,1/6,7/30,7/120,41/1560`. The geometry and general formula support these without a new numerical census. |
| V2-C0034 | The admissible full-period sequence 0,1 has no strictly decreasing triple. The formula gives 1/8 because two zero-state positions coincide. Retain as a low-severity period-two exception. |
| V2-C0035 | The stated integer multiplier includes 1. The map `x -> (x+theta) mod 1` decreases with probability `theta`, not 1/2. The 2005 uniform-input clarification does not exclude it. Retain as a low-severity missing hypothesis; the preceding correlation formula remains valid. |

Original images re-inspected: pp. 55, 71, 78, 92, 564–569, 571–576;
Pearson 1897 p. 45; and the 1999/2004 and 2021 partition corrections.
The earlier independent exact calculations and general proofs in the
individual notes were accepted; large finite enumerations were not rerun.

Public search families combined Knuth or TAOCP with Pearson/Le Monaco/1892,
circular spacings/exercise 26/origin/irrational coding, Dixon/serial
correlation/moments/p. 565, concentration/p. 564, collision/Algorithm S/
rounding/negative probability, birthday/partition/p. 569/errata,
monkey/p. 571, Gaussian/p. 571, third moment/p. 572,
Dedekind/Cauchy/p. 573, Fibonacci/run/1/6/errata and 3.3.3/exercise 22/error.
Queries and results were inspected on the review date. Searches returned
book reproductions, standard formulas, related implementations and
unrelated corrections, but no exact prior report of these defects.

One relevant primary result, Tsang et al.,
[Tuning the Collision Test for Stringency](https://i.cs.hku.hk/~cisc/projects/va/tuning.pdf),
was opened. Its discussion and C implementation concern computation time,
test power and a normal approximation; they do not identify the rounded
sentinel problem of C0021. A result about Fibonacci sorting concerns
Volume 3's Shellsort attribution, not C0033. These were not silently
counted as independent confirmations of novelty.
