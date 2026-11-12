# The multiplicity threshold loses its dependence on k

Volume 4A, first edition, first printing (2011), Note after answer 7.2.1.4–50, Fristedt statement,
printed page 755, file page 772.

Let X_k be the number of parts equal to k in a uniformly chosen partition of n, and let C=pi/sqrt(6), as defined in this section. Removing r copies of k is a bijection from partitions with X_k>=r to partitions of n-kr. Thus

```
Pr(X_k>=r)=p(n-kr)/p(n).
```

For fixed positive k and x, equation (45) therefore gives

```
Pr(X_k>C*x*sqrt(n)) -> exp(-C^2*k*x),
```

with integer rounding of the threshold immaterial in the limit. This is not the printed exp(-x). To obtain exp(-x), the threshold must be **x*sqrt(n)/(C*k)**. For k=x=1, the printed threshold yields exp(-pi^2/6), rather than exp(-1).

The cited Fristedt article's publisher PDF returned HTTP 403 in this audit, so its text is not claimed to have been inspected. The correction above follows directly from the exact removal bijection and the book's own partition-ratio estimate; it does not depend on reproducing the external proof.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/partition-counting-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
