# Publication review: C0071–C0090

Reviewed November 12, 2026. All seventeen baseline-confirmed cards in
this range remain supported, with the qualifications below. C0081,
C0082 and C0088 were not confirmed and are outside this recheck. Original
typesetting and the four applicable current/historical errata layers were
compared. No matching additional repair or explicit prior TAOCP report
was found in the searches listed below. Priority is not established.

| Card | Assessment and limits |
| --- | --- |
| V2-C0071 | The congruence gives circular separation, not the asserted ordinary index distance. Seeds 0 and 2^29 permit indices 2^99-1 and 0 with the same block, although their distance is less than 2^99. The exponent difference is a multiple of the period 2^100-1. The overall stream separation conclusion survives with circular distance. |
| V2-C0072 | The 2002 warmup advances the state by 10 times 199 steps. Thus the answer's old seed phase H becomes H-1990 modulo 2^100-1. The stored bit-polynomial certificate distinguishes the old and warmed first words, 1028764519 and 58678820. Knuth's 2002 news already announces the changed initialization, but does not identify the stale exercise formula. |
| V2-C0073 | The literal 2002 replacement for p. 602 declares the double arrays u and ul but uses an undeclared integer array x. The instruction to rename references inside a loop does not declare x. Adding int x[199] repairs compilation and preserves the two stated test outputs. This is a defect in the printed replacement, not the current standalone rng-double.c. |
| V2-C0074 | The final discarded-bit index omits its n contribution. At k=2,n=1, with only initial bit X_27 equal to one, the printed relation predicts zero while X_201 is one. Replacing its X_126 by X_127 gives the correct relation. Retain as an index typo; the relation count is unaffected. |
| V2-C0075 | The displayed weighted sum is 0.49369628238894736. Its quoted count 14043 needs the additional factor 2^-100 times the sum of binomial(100,i), i=0,...,40, which is 0.0284439668204904. Their product times one million is 14042.6806757. This identifies a missing factor in the stated approximation, not an exact expectation under every adaptive sampling phase. |
| V2-C0076 | The universal recovery claim fails for modulus 2^32, multiplier 1, initial state 0, and increments 1 versus 3. Both generators have full period and their first 150 high-16-bit observations are all zero; their first differences differ. Additional hypotheses or ambiguous outputs are necessary. This does not establish cryptographic safety. |
| V2-C0077 | The two middle bits depend only on the state modulo 2^18. The full-period families a=5+u*2^18 and c=1+v*2^18, with 0<=u,v<2^14 and the same initial state, therefore give identical observations forever. Both a and the first difference vary. The claim about all sixteen retained bits is separate. |
| V2-C0078 | The epigraph's 1844 date conflicts with Note G on p. 722 of Scientific Memoirs volume III, whose title page is dated 1843. Both original source pages were re-inspected. This is a correction to the book's date, not a new historical discovery about Lovelace. |
| V2-C0079 | The digit set {2,3,4,5,6,52,53,54,55,56} cannot represent 3/2. A highest place at least zero gives at least 2; at most -2 gives at most 28/45; at -1 the leading small digits give at most 11/9 and the large digits give at least 5.2. The printed claim of all positive reals is false. |
| V2-C0080 | Zero is a square in the 2-adic integers but satisfies none of the stated nonzero residue conditions. Add the zero case or restrict n to be nonzero. Retain as a minor endpoint omission, not a failure of the nonzero square criterion. |
| V2-C0083 | The book's normalized representation includes zero with its minimum exponent. For base 10, eight digits, excess zero and epsilon=0.1, u=0 and v=0.1 satisfy the exponent-based essential-equality definition but violate the claimed relative bound with right side zero. Excluding zero, or using epsilon<1/base, repairs this endpoint. Lomont's 2005 discussion concerns symmetry and strict comparison at two zero operands, not this implication with one nonzero operand. |
| V2-C0084 | The claim for every base greater than two has the exception base 3, precision one, with ties to even or away from zero. Directly rounding twice after doubling and halving returns each representable value; monotonicity then places every computed midpoint between its endpoints. Ties to odd do not have this exception. The 2019 replacement was applied. |
| V2-C0085 | With base 2 and one digit, ties to odd at the pre-normalization rounding step violate the claimed drift identity. Starting at u=1,v=1/4 gives 1,1/2,1/2,1/4 after alternating addition and subtraction. Algorithm N explicitly resolves a tie before a possible carry and rescaling. The ordinary ties-to-even theorem remains valid. |
| V2-C0086 | Expansion of the corrected compensated-sum recurrence gives ten quadratic monomials at n=2, not eight. In general the count is 4n+2 for n>=2, with four at n=1. The 2021 correction to the returned value is included. The asymptotic O(n*epsilon^2) bound is unaffected. |
| V2-C0087 | The 2020 p. 238 replacement prints (26,.000602214), which has nine fractional digits and is ten times too small. Its later occurrence on the same errata page is correctly (26,.00602214). The SI Avogadro constant confirms the scale. |
| V2-C0089 | In the 2020 interval-sum replacement, the upper endpoint .60221408 is already exactly representable and the added upper endpoint is strictly positive. Directed upward rounding therefore requires .60221409. This concerns the specified interval operation; it does not claim that the narrower interval excludes the exact sum of the known physical constants. |
| V2-C0090 | The tentative attribution of the first half-to-even rule to Scarborough (1930) is contradicted by Woodward's 1906 title page and explicit rule on p. 42, and by Newcomb's rule on pp. 14–15 in a volume with 1882 copyright. The Newcomb copyright is not an independently established printing date. The earlier rule is already discussed publicly; retain only the correction to the book's historical statement, not priority for finding that rule. |

Original TAOCP pages re-inspected: 189, 193, 213, 215, 217, 233–234,
237–241, 599–600, 602, 604, 608, 614–615. The relevant 2002 and 2020
replacement pages were inspected as images to settle declaration scope,
the rounding examples and the extra zero. The previous short certificates
were read and checked against these pages; no large census was rerun.

Errata: `all2-prepre`, `all2-pre`, `all2`, `err2`, as refreshed in this
review's source manifest. Nearby corrections to 4.1-31(c), to the bound
following (36), to compensated summation, and to bibliography do not fix
the separate claims here.

Public searches covered the card-specific phrases and locations: seed
phase 1990; ran_start warmup; the undeclared rng-double array; 150 high
bits and two middle bits; discarded-bit indices and 14043; the unusual
digit set; 2-adic square zero; essential equality at zero; ternary
midpoints; one-digit odd rounding drift; four-n terms in compensated
summation; the Avogadro and interval endpoints; Lovelace 1844 versus
1843; and Scarborough, Newcomb and Woodward. Search results containing
the same printed claim were not counted as a prior correction.

Sources investigated beyond the official errata:

- [Knuth's 2002 news](https://www-cs-faculty.stanford.edu/~knuth/news02.html): known generator changes, distinct from C0072's stale phase and C0073's missing declaration.
- [Lomont, Taming the Floating Point Beast](https://lomont.org/papers/2005/CompareFloat.pdf), pp. 1–2: nearby zero-comparison discussion, not C0083's counterexample.
- [BIPM definition of the mole](https://www.bipm.org/en/si-base-units/mole): independent scale check for C0087.
- [Lovelace's original notes](https://www.hist-math.fr/textes/Lovelace1843_SketchAnalytical.pdf), Note G, p. 722, and the archived Scientific Memoirs III title page: primary support for C0078.
- [Woodward, p. 42](https://archive.org/details/probabilitytheor00wooduoft/page/42) and [Newcomb, pp. 14–15](https://archive.org/details/logarithmicother00newcrich/page/n24): originals inspected for C0090.
- [2010 rounding discussion](https://stackoverflow.com/questions/3840793/rounding-standards-financial-calculations/3841008): prior awareness of the 1906 rule, without an identified correction to this TAOCP passage. Historical background is not claimed as novel.

Modern uses of the name “round-to-odd” often mean a different operation
that changes every inexact result, rather than changing only ties. Those
results do not resolve C0085's precise tie-breaking convention.
