# V3-C0049 — The 2005 Dedekind-number erratum has a false leading term

Confirmed in the official **errata**, `all3-prepre`, PDF p.34, entry dated
1 November 2005 replacing the last three lines of answer 5.3.4-31 on
volume 3 p.669. The original 1998 answer has a correct leading asymptotic
and is context only, not the error location.

Let delta_n be the book's number of distinct nonconstant functions made
from n Boolean variables using AND and OR. These are the nonconstant
monotone Boolean functions: changing an input coordinate from 0 to 1
cannot change the output from 1 to 0. The replacement asserts

```
delta_(2m) = exp( binom(2m-1,m) ln 2
                  + binom(2m,m+1)/2^(m+1)
                  + (m-1)sqrt(m/pi)/16 + O(m^(-1/2)) ).
```

Its leading coefficient is too small by a factor of two. This follows
from an elementary lower bound, independently of the cited article.
Write `B=binom(2m,m)`. For each nonempty family F of m-element subsets
of `{1,...,2m}`, form the function

```
f_F(x) = OR over S in F of (AND over i in S of x_i).
```

This is nonconstant. At the Boolean vector having ones exactly in an
m-element set T, its value is 1 exactly when T belongs to F: containment
between two sets of equal size forces equality. Consequently all
`2^B-1` nonempty families give distinct functions, and

```
delta_(2m) >= 2^B-1,
ln delta_(2m) >= B ln 2 + o(1).
```

But `binom(2m-1,m)=B/2`; every other term in the replacement exponent is
o(B). The replacement therefore predicts
`ln delta_(2m)=(B/2)ln 2+o(B)`, contradicting the lower bound.
The original answer's limit `lg(delta_n)/binom(n,floor(n/2)) -> 1`
also contradicts the replacement directly.

At minimum the leading binomial must be changed. This note does not
endorse the lower-order terms or propose a complete replacement formula.
The cited source is A. D. Korshunov, *Monotone Boolean functions*,
Russian Mathematical Surveys 58 (2003), 929–1001,
[DOI 10.1070/RM2003v058n05ABEH000667](https://doi.org/10.1070/RM2003v058n05ABEH000667).
The bibliographic record and an indexed passage were accessible, but
attempts to obtain the full original PDF on 10 November 2026 returned
an access error or redirected to the journal portal. No claim about the
full source theorem or its proof is needed for the contradiction above.

The official formula was visually checked in the full PDF page and an
enlarged crop, retained as `images/bookwise-dedekind-errata-p34.png` and
`images/bookwise-dedekind-errata-formula.png`. The five official errata
layers were screened in `sources/networks-errata-review.json`; none
corrects this entry. Targeted public searches for the p.669 Dedekind
formula and its leading binomial found no matching report. Absolute
priority and the contents of later physical printings are not asserted.
