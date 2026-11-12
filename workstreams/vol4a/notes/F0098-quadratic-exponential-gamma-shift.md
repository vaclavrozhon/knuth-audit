# The gamma argument is shifted by one

Volume 4A, first edition, first printing (2011), Answer 7.2.1.5–42, parenthetical continuation,
printed page 772, file page 789.

The answer's parenthetical analog of (22) is printed as

```
sin(pi*x/2)^2 / Gamma((x-1)/2).
```

For positive odd integers x=n it must agree with the coefficient of z^(n-1) in exp(z^2), namely `1/((n-1)/2)!`, correctly displayed just above. At x=5 this coefficient is 1/2, but the parenthetical expression gives 1/Gamma(2)=1.

The denominator must be Gamma((x+1)/2), which gives the required factorial at all positive odd integers. The integer saddle-point result itself is correct. This finding uses the integer specialization; no independent construction of the noninteger integration contour is claimed.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-saddle-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
