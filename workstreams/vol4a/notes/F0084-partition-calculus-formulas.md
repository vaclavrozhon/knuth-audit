# The preliminary calculus formulas need a constant and a range

Volume 4A, first edition, first printing (2011), Answer 7.2.1.4–25(a), preliminary integral and derivative,
printed page 751, file page 768.

The answer defines `f(x)=-log(1-exp(-tx))`, with t>0, and uses Li_2 for the dilogarithm, whose series is sum(u^j/j^2,j>=1). It prints

```
integral_1^x f(s) ds = -Li_2(exp(-tx))/t.
```

The right side is an antiderivative, but the specified lower limit contributes a constant. The correct formula is

```
integral_1^x f(s) ds
    = (Li_2(exp(-t))-Li_2(exp(-tx)))/t.
```

At x=1 the printed left side is zero while its right side is negative. This also prevents treating the displayed formula as a definite-integral identity without a correction.

The neighboring formula for f^(n)(x), using the Eulerian numbers with upper index n-1 and an exp(tx) numerator factor, is valid for n>=2. At n=1 it gives `-t*exp(tx)/(exp(tx)-1)`, whereas direct differentiation gives `f'(x)=-t/(exp(tx)-1)`. State n>=2 and supply f' separately. These local repairs do not alter the final asymptotic estimate to its stated O(1) accuracy. The known 2021 Bernoulli-factor correction is in part (b) and is a different issue.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/partition-counting-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
