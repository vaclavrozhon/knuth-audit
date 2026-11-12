# F178 — exponentially small remainder misses a term of order1/n

Volume4B, first edition, second printing2022, answer MPR140(a), printed396
(file416), final equation for the expected number of unmarked records.
The stated remainder O(q^n/n) after2q/p is false. For fixed0<p<1 the
correct expansion starts **2q/p + 2q/(p²n) + O(n⁻²)**.

This concerns the last remainder, not the earlier, valid binomial harmonic
sum for the marked records. The latter equals H_n+ln p+O(q^n/n).

A short independent contradiction uses p=q=1/2 and K, the number of marked
positions. Conditional on K=k, the k+1 gaps contain an expected
(n−k)/(k+1) unmarked entries each. Every entry in gap r remains a record
exactly when the first r permuted marks are the r smallest marks; this
has probability1/binom(k,r). Therefore the conditional expectation is

    U(n,k) = (n−k)/(k+1) * sum(r=0..k,1/binom(k,r)).

The two endpoint terms, counting k=0 only once, average to
2−(n+2)2⁻ⁿ. If n/4≤K≤3n/4 and n≥16, the two next-to-endpoint terms
are distinct and contribute at least2/(3n). Chebyshev gives probability
at least1−4/n≥1/2 for that event. Consequently

    E U − 2 ≥ 1/(3n) − (n+2)2⁻ⁿ ≥ 1/(4n), for n≥16.

Thus the remainder cannot be O(2⁻ⁿ/n). This is an all-n contradiction,
not an inference from a finite numerical test. The exact short confirmation
in results/first100-mpr140-145.json independently evaluates both the printed
double sum and the conditional-gap sum at n=4,8,16,32.

The cited authors' primary paper independently supplies the correction:
Banderier–Beier–Mehlhorn, Theorems2/4 in the
[April2003 author manuscript](https://lipn.univ-paris13.fr/~cb/Papers/smoothed.pdf),
pp5/12, gives the total expectation as
ln(pn)+gamma+2q/p+(1/2+2q/p²)/n+O(n⁻²).
Subtracting the marked-record term yields the expansion above.
The local source is sources/first100-banderier-2003.pdf.

Original typesetting: images/first100-p396.png. Statement MPR140 on
printed28 was read with the answer. Six official historical/current errata
layers and three TeX versions were searched; see
sources/first100-mpr140-145-novelty.json. No matching public correction
was found. No later physical printing was inspected, and absolute priority
is not asserted. No correspondence was sent.
