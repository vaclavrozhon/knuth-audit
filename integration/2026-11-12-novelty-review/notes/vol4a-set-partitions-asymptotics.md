# Volume 4A: set partitions and asymptotic estimates, publication review

Reviewed on 12 November 2026 against the first edition, first printing
(2011). All sixteen baseline-confirmed findings F0089–F0104 are retained.
B_n below is the number of partitions of an n-element set, and xi is the
positive solution of xi*exp(xi)=n. A cumulant is a coefficient of the
logarithm of the moment-generating function, with factorial normalization.
The individual notes define the other notation.

Inspected the original statements on pages 423, 425, 434, 437, 768–769
and 771–775. Rechecked the small examples and the algebra of the stated
corrections. Existing targeted symbolic results for the Bell and
involution expansions were read and checked against the printed
coefficients; no new large computation was needed.

| ID | Reason for retaining the finding |
| --- | --- |
| V4A-F0089 | Exercise 7.2.1.5-24, p. 434: at p=3,e=1 the hint asserts x^3-x=x^9-x^3 modulo 3 as polynomials. The exponent defining g_j must be p^(j-1), not p^j. This restores the induction's base case without changing the Bell-period result. |
| V4A-F0090 | Answer 7.2.1.5-27, p. 768: crossing/nesting endpoint pairs must be consecutive within their blocks. Under tableau transposition, the partition with blocks {1,5},{2,3,4} maps to {1,3,5},{2,4}. At the cut 2, the latter has the printed broad nesting (1,5),(2,4) while the former has no corresponding crossing. The pair (1,5) skips the middle element 3 and is not an arc. |
| V4A-F0091 | Answer 7.2.1.5-29(b), p. 769: rows i1 and i2 leave i2-i1-1 intervening rows, not i2-i1+1. With selected rows 1 and 3 the first gap contributes one free cell, not three. Both the prose and exponent need the sign change; the final Gaussian-binomial formula is correct. |
| V4A-F0092 | Additional identity after answer 7.2.1.5-29(c), p. 769: one row of length one shows a missing factor 1/(1-z) on the right. Shape (2,1) shows that the product offset must be a_j+j-m+t, not a_j+m-j+t. These are defects in the additional identity, separate from the known correction to the exercise's factorization. The upper summation index should be m. |
| V4A-F0093 | Answer 7.2.1.5-36, p. 771: the generating function for exactly k unordered blocks is S(z)^k/k!, not S(z)^k. For two pairs on four elements the printed expression counts six instead of three. The outer exponential formula is correct. |
| V4A-F0094 | Answer 7.2.1.5-38(b), p. 771: entries bounded by m correspond to restricted growth digits strictly below m. For n=3,m=2 the printed non-strict bound admits 012 and hence the forbidden cycle 333. The final Stirling-number sum is correct. |
| V4A-F0095 | Answer 7.2.1.5-40, p. 771: Stirling's formula for c^(n-1)/(n-1)! gives multiplier 1-1/(12n)+O(n^-2), not the diverging 1+n/12+O(n^-2). The leading factor and saddle point are correct. |
| V4A-F0096 | Equations (29)–(30), p. 423: replacing the exact first corrections by -xi/(12n) discards terms asymptotic to 11/(24n) and -1/(24n). Neither fits the printed O((log(n)/n)^2) remainder. Retain the exact coefficients or weaken the remainder to O(1/n). |
| V4A-F0097 | Answer 7.2.1.5-46, p. 772: the factor should have exponent k-1. At k=1 the entry is exactly B_n, whereas the printed exponent k leaves relative discrepancy xi/n, larger than O(1/n). The weaker later k=n estimate is not refuted by this change. |
| V4A-F0098 | Answer 7.2.1.5-42, p. 772: at x=5 the parenthetical expression gives 1/Gamma(2)=1, although the integer coefficient is 1/2. The gamma argument must be (x+1)/2, not (x-1)/2. |
| V4A-F0099 | Answer 7.2.1.5-48, p. 773: expanding exp(exp(z)) requires exp(k*z), not exp(k*x). At x=1 the erroneous closed-contour integral is zero, while the correct coefficient is e. The next line already uses the correct variable. |
| V4A-F0100 | Exercise 7.2.1.5-45, p. 437, and answer 52, p. 774: b2prime=xi^2/288+O(xi), so after the first correction the remainder is not O(n^-2). The scale is O((log(n)/n)^(m+1)). In answer 52, b1prime asymptotic to -xi/12 likewise makes the leading Gaussian relative error order log(n)/n, not O(1/n). |
| V4A-F0101 | Answer 7.2.1.5-51, p. 774: sigma^2+sigma=n+1 implies exp(sigma+sigma^2/2)=exp((n+1+sigma)/2). The intermediate prefactor omits sqrt(e). Its correction tends to one and cannot absorb the loss. The final expanded formula is correct. |
| V4A-F0102 | Answer 7.2.1.5-52, p. 774: extracting coefficients gives exp(xi)*sum(S(j,k)*xi^k), with j above k in the Stirling number, not reversed. At j=1,xi=1/2 the printed value is twice the mean. The specialization giving e*B_j is xi=1, not xi*exp(xi)=1. The case (b) notation also needs kappa_j in place of kappa=j. |
| V4A-F0103 | Answer 7.2.1.5-55, p. 775: Newton's denominator is 1-c*exp(beta), not 1-c*exp(-beta). Substitution of the desired positive root into the printed update gives a strictly smaller value, so the root is not even a fixed point. |
| V4A-F0104 | Equation (41), p. 425: Taylor's formula requires a plus before the sum of higher derivatives. The printed minus reverses every term of order at least three. At sigma=log(2) the third derivative is nonzero. The later normalized expansion and first correction use the correct signs. |

## Official and public-source comparison

Compared the refreshed [early Volume 4A changes](https://www-cs-faculty.stanford.edu/~knuth/all4a-pre.ps.gz),
[later changes](https://www-cs-faculty.stanford.edu/~knuth/all4a.ps.gz),
[current errata](https://www-cs-faculty.stanford.edu/~knuth/err4a.ps.gz),
[Fascicle 3 changes](https://www-cs-faculty.stanford.edu/~knuth/all4f3.ps.gz)
and [Fascicle 3 errata](https://www-cs-faculty.stanford.edu/~knuth/err4f3.ps.gz).
The relevant nearby entries concern cross-references, a boundary in
answer 43, bibliography and the exercise's rook-factorization offset.
They do not repair the listed defects. The page-423 change from (29)
to (26) in a later reference does not change equations (29) or (30).

Fresh searches combined Knuth/TAOCP with rook 769, Bell 423 errata,
771 factorial, cumulants error, Peirce exponent, involutions 774,
7.2.1.5-55 Newton, Bell remainder, crossings/consecutive, and
7.2.1.5 exercises 24 and 36. The public
[tamnd/brain solutions](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4/7.2.1.5)
were screened for exercises 24, 27, 29, 36, 38, 40, 42, 45, 46, 48,
51, 52, 55 and 58. Many are unrelated to the questions. Exercise 46
does use k-1, but with a weaker asymptotic equivalence and no report
of the book's stronger erroneous bound. Exercise 52 gives the correct
cumulant indices; its explicit typo discussion concerns a different,
malformed transcription of part (b). Exercise 58 uses the ordinary
Taylor sign. These are public related formulas, not identified prior
reports of the corresponding book defects.

Chen et al.'s [crossings and nestings paper](https://arxiv.org/pdf/math/0501230),
p. 3, confirms that standard arcs join consecutive block elements.
Hwang's [paper on two saddle-point contours](https://pdfs.semanticscholar.org/12c8/a43d99c2327396958cd9ccff9f2db045a18b.pdf),
Section 2.1, explicitly discusses Knuth pp. 422–423 and the n versus
n+1 saddle choice. The passage does not report the missing 1/n terms
or erroneous remainder at issue here. The
[Analytic Combinatorics errata](https://ac.cs.princeton.edu/errata/)
cite Knuth exercise 51 to repair their own page-559 inequalities;
that is not a report of Knuth's missing sqrt(e) prefactor.

No matching prior error report was found in the checked sources.
Absolute priority is not established.
