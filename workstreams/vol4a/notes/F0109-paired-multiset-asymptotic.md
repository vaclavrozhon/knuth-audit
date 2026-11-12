# The paired-multiset estimate drops dominant terms

Volume 4A, first edition, first printing (2011), answer 7.2.1.5–76,
printed page 779, file page 796, last displayed asymptotic equality.

Let P(0,n) count partitions of a multiset containing two copies of each of n distinct elements, and let B_j denote the jth Bell number. The answer replaces the full umbral expression (B^2+B)^n by B_(2n)+n*B_(2n-1), claiming relative error O((log n)^3/n). The omitted positive terms are larger than the retained expression.

In ordinary notation, the full expression is

```
R_n = sum(binomial(n,j)*B_(2n-j), j=0,...,n).
```

The recurrence in answer 73, or its polynomial generating function with nonnegative coefficients, implies `2^n*P(0,n)>=R_n`. In particular, the omitted j=2 term is a lower bound for 2^n*P(0,n).

Let xi*exp(xi)=2n. The fixed-shift Bell ratios already established in the section give

```
n*B_(2n-1)/B_(2n) ~ xi/2,
binomial(n,2)*B_(2n-2)/B_(2n) ~ xi^2/8.
```

Consequently the omitted j=2 term, divided by the proposed leading expression B_(2n)+n*B_(2n-1), is asymptotic to xi/4 and tends to infinity. The claimed relative error instead tends to zero. This contradiction needs no multiset census or new saddle-point analysis.

Retain the full positive sum R_n in the preceding estimate. Equivalently, answer 73 identifies R_n with the Peirce-triangle entry w_(2n+1,n+1). Truncating it to its first two Bell terms is invalid. The known 2010 erratum repairs only the final cross-reference from exercise 75 to exercise 73.

Original typesetting inspected. Errata and public-source screening:
`../sources/multiset-partition-source-check.json`. No matching repair was found
in the sources searched; absolute novelty is not established.
