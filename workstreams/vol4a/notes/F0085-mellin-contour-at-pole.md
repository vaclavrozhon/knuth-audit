# The Mellin contour passes through the pole at one

Volume 4A, first edition, first printing (2011), Answer 7.2.1.4–25(b), Mellin inversion contour,
printed page 751, file page 768.

The Mellin argument writes the inversion integrals on the line from 1-i infinity to 1+i infinity. After summing over the positive integers m,n, its integrand becomes

```
zeta(z+1)*zeta(z)*t^(-z)*Gamma(z).
```

Here zeta is the Riemann zeta function and Gamma is the gamma function. The integrand has a simple pole at z=1 with nonzero residue zeta(2)/t. The printed contour therefore passes through its pole; the ordinary improper contour integral is undefined. Moreover the separate sum of m^(-z) used to justify the interchange converges only when Re(z)>1.

Choose a vertical line Re(z)=c with **c>1**, for example c=2, in both inversion displays. Then the interchange is valid and shifting the line left picks up the residue at 1, as the answer intends. The final asymptotic expansion remains valid, with the separately known 2021 correction B_2*B_1*t/2.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/partition-counting-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
