# The additional rook identity needs an offset and a factor

Volume 4A, first edition, first printing (2011), Answer 7.2.1.5–29(c), additional generating-function identity,
printed page 769, file page 786.

Write `[u]_y=(1-y^u)/(1-y)` and `[k]!_y=product([j]_y,j=1,...,k)`. Let R_s(a) be the coefficient of x^s in the rook polynomial for shape a=(a_1,...,a_m).

The additional identity in the note after part (c) has two independent defects. Its product uses a_j+m-j+t, although the preceding factorization requires **a_j+j-m+t**. Its right side is also missing **1/(1-z)**. A corrected version is

```
sum(z^t * product([a_j+j-m+t]_y,j=1,...,m), t>=0)
 = 1/(1-z) * sum([k]!_y * z^k
       / product(1-y^j*z,j=1,...,k) * R_(m-k)(a), k=0,...,m).
```

Two small checks separate the defects:

- For one row of length 1, the printed left side is `1/((1-z)(1-y*z))`, while its printed right side is `1/(1-y*z)`. Thus the factor 1/(1-z) is needed even where the offset issue disappears.
- For shape (2,1), the constant term in z of the printed left side is `[3]_y[1]_y=1+y+y^2`; that of the right side is R_2(2,1)=1. The corrected offsets give `[1]_y[1]_y=1`.

The corrected identity follows by summing the preceding part (c) over t and using `sum([t]!_y/[t-k]!_y*z^t,t>=0)=[k]!_y*z^k/product(1-y^j*z,j=0,...,k)`. The June 2010 Fascicle 3 erratum corrected the offset in the exercise itself (now page 435); it does not correct this separate additional identity on page 769 or its missing denominator. The upper summation index in the repaired formula is m.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-counting-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
