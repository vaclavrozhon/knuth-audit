# The exponential in the integrand uses x instead of z

Volume 4A, first edition, first printing (2011), Answer 7.2.1.5–48, first displayed sum,
printed page 773, file page 790.

Here z is the integration variable and x is the real parameter. Expanding exp(exp(z)) gives `sum(exp(k*z)/k!, k>=0)`. The first line instead uses exp(k*x); the next line already uses the correct exp(k*z).

At the integer parameter x=1, the erroneous integrand is a constant times z^-2, whose closed contour integral is zero. The original integral gives the coefficient of z in exp(exp(z)), which is e. Thus the displayed equality fails even in the elementary integer case. Changing x to z repairs the derivation and preserves the final Dobinski-type series.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-saddle-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
