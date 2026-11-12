# Volume 2: factor bounds, addition chains, and polynomial evaluation

Review date: 2026-11-12. All 19 cards below are retained. Their reports,
supporting arguments, and original typesetting were checked against the
third edition and the refreshed `all2-prepre`, `all2-pre`, `all2`, and
`err2` layers (see `../sources/manifest.json`). No matching prior report
was found in this search; priority is not established.

| Card | Reassessment |
| --- | --- |
| V2-C0214 | The Graeffe limit on p. 683 lacks a leading sign or phase. Starting with 2x−1 gives 1−2^(2^t)x, whose normalization tends to −x. The root and Mahler-measure bounds are unaffected. |
| V2-C0215 | The weaker factor bound on p. 452 does not justify the constant-coefficient filter before checking the complementary factor. For u=(x+1)(x²+x+100), B=20 and modulus 41, the only degree-two choice has constant coefficient 18, which fails the divisibility filter, while its complement x+1 is a valid small factor. The version bounding every factor remains valid. |
| V2-C0217 | The Gaussian integral in answer 21(c), p. 684, needs pi to the number of variables, not to the degree. For one variable and u=z², the integral is 2pi and the printed normalization yields 1/pi instead of 1. |
| V2-C0218 | Beauzamy and Dégot's Differential identities appeared in Transactions AMS 347 (1995), 2607–2619, not volume 345 as printed on p. 683. The authors' publication record confirms this bibliographic typo. |
| V2-C0219 | The lower bound in the Perron proof, p. 690, needs absolute values on the powers of r. For u=x³+4x+1 and r=−1/2 the two sides of that algebraic inequality are 15/8 and 17/8. This r is a counterexample to the intermediate inequality, not a claimed root of u; the irreducibility theorem remains true. |
| V2-C0222 | The historical algorithm as described on p. 449 misses the root zero: gcd(x^(p−1)−1,x)=1. Say nonzero roots or remove factors x first. This review does not assert that Legendre's original algorithm was erroneous; the original historical publication was not independently inspected. |
| V2-C0224 | The strict binomial bound on p. 472 fails for zero ministeps: there is one empty choice, also for arbitrarily long doubling chains. Use a non-strict inequality and treat the zero parameter separately in the answer. This is an endpoint wording correction. |
| V2-C0226 | The signed binary weight count in answer 30, p. 696, undercounts n=7=8−1: it predicts three multiplications, but four are needed even when x and its inverse are available. The top signed-digit position can exceed the ordinary binary logarithm index by one. |
| V2-C0227 | The 5n/2+O(sqrt(n)) minimum-cost assertion on p. 696 needs n odd. For powers of two the minimum sum of chain terms is 2n−2. Zantema's original 1989 report explicitly restricts its lower bound to odd n and gives an upper bound for all n. This is a misstatement of a known result, not a new chain bound. |
| V2-C0228 | The reduced dual graph in answer 34, p. 696, ends with labels 2^(e0−1), n, not 2^e0, n. For n=3 its two surviving nodes have labels 1 and 3, with three parallel arcs. |
| V2-C0230 | The Newman parameter in answer 38, p. 697, is too small to deliver the claimed m+o(m) bound. Writing t=ln(m), u=ln(t), the printed expression gives r=(t/u)(1+a/u+O(1/u²)) with a=(ln 2)²/2<1, hence m²/K=m exp((1−a+o(1))t/u), not o(m). The theorem remains true with the repaired parameter in the original report. |
| V2-C0231 | The determinant exercise added in the 2024 errata uses n(n+1)/2 instead of n(n−1)/2. At n=1 and constant factors p=q=1, r=s=2 it gives 1=4. Triangular substitution matrices have diagonal powers indexed 0 through n−1. Gessel–Xin already give the correct scaling identity; the finding is the erroneous book exercise. |
| V2-C0232 | The Datta–Singh citation on p. 461 should point to volume I, p. 76, which discusses Pingala's halving procedure. Volume II, p. 76, concerns cubic equations. Both primary pages were inspected. |
| V2-C0233 | The Said(an) translation cited on pp. 198 and 461 was published in 1978, not 1975. The title/copyright pages and the publisher's book record agree. |
| V2-C0234 | The endpoint simplification in answer 6, p. 698, saves two divisions, not one multiplication and one division. Restoring the top coefficient removes one division; rewriting x^m(u0/x^m+w) as u0+x^m w removes the other while retaining the multiplication. The total operation saving is still two. |
| V2-C0235 | The two orientation descriptions on p. 702 are reversed. The large left semicircle, parametrized by increasing argument, is counterclockwise; the straight return segment contributes clockwise change. The diagram's arrows are already correct. |
| V2-C0237 | The final nonvanishing-coefficient claim in Theorem E's proof, p. 494, needs even degree. For u=x³+x all permitted choices leave the x² coefficient zero although q=W+1 is nonzero. In odd degree the leading coefficient itself proves the needed nonvanishing, so the theorem survives. |
| V2-C0238 | The asserted equality of result sets on p. 496 excludes valid zero intermediates even when they are never denominators. The chain x, x+x, a(x+x), with a=0, witnesses the failure. Restrict exclusions to actual denominators, or use the polynomial-identity continuation argument; the theorem survives. |
| V2-C0239 | The five-parameter formula on p. 704 needs alpha5 in its constant term, not alpha6. The preceding derivation uses alpha1 through alpha5; setting the first four to zero and alpha5=1 must produce x⁴+1. |

The second-edition June 1997 amendment to answer 33 on p. 638 changes a
coefficient in a related Newman formula. It is recorded in the existing
`powers-squares.md` investigation; it does not repair the third-edition
formula. Without the original second-edition page, this review does not
identify which of its repeated occurrences was intended. The June 1999
correction on p. 493, the 2019 wording change on p. 496, and the 2004 Pingala
dating correction address different issues. The 2024 determinant addition
still contains the positive-sign exponent in the latest errata.

## Public-source cross-check

Searches combined Knuth/TAOCP with Graeffe limit, trailing coefficient
factor bound, Beauzamy–Dégot, Bombieri Gaussian integral, Zantema odd cost,
signed chains and p. 696, Newman and p. 697, Gessel–Xin determinant erratum,
Saidan 1978, Datta–Singh volume, Eve proof, result sets and p. 496,
divisions and p. 698, dual reduced graphs, Legendre zero root, ministeps,
clockwise and p. 702, and alpha6 on p. 704.

Primary references inspected or checked against the retained original
source images:

- [Beauzamy's publication record](https://scmsa.eu/cvbb.pdf), item 74,
  and [the article](https://www.scmsa.eu/BB_Publications/BB_Degot_Differential_Identities.pdf).
- [Zantema's 1989 report](https://ics-archive.science.uu.nl/research/techreps/repo/CS-1989/1989-15.pdf), p. 3.
- [Gessel–Xin, Electronic Journal of Combinatorics 13, R53](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v13i1r53),
  p. 14, which has the exponent binomial(n,2).
- [Datta–Singh, combined volumes](https://www.dbraulibrary.org.in/RareBooks/History%20of%20Hindu%20Mathematics.pdf),
  the separate printed p. 76 of each volume.
- [The Arithmetic of Al-Uqlidisi, publisher record](https://link.springer.com/book/10.1007/978-94-009-9772-1), ©1978.

A public search also returned the recent
[fast-polynomials implementation](https://github.com/thomasahle/fast-polynomials/blob/main/website/README.md).
Its Knuth–Eve implementation description was inspected: it is not a report
of either of the two specific proof defects above. Correct identities or
algorithms in earlier literature establish the correction, but do not by
themselves establish an earlier report of the erroneous book passage.
