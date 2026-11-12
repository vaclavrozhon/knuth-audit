# The Newton denominator has the wrong exponent sign

Volume 4A, first edition, first printing (2011), Answer 7.2.1.5–55, Newton iteration,
printed page 775, file page 792.

Put c=alpha*exp(-alpha), and let beta in (0,1) solve beta=c*exp(beta). Newton's method for f(b)=b-c*exp(b) gives

```
b_next = (1-b)*c*exp(b) / (1-c*exp(b)).
```

The numerator agrees with the answer, but the printed denominator is `1-c*exp(-b)`. At the desired root, this printed update equals

```
beta*(1-beta)/(1-beta*exp(-2*beta)),
```

which is strictly less than beta for every beta in (0,1). Thus the desired root is not a fixed point, and the stated convergence is impossible as printed. The corrected Newton iteration restores the intended computation.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-probability-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
