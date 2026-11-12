# V4A-F0024: The parabola curvature is understated by a factor of four

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), printed page 614 / file page 631.
Original: `images/bookwise-p614.png`.

Let curvature mean the reciprocal of the radius of the osculating
circle. For a graph y=f(x), its magnitude is

    kappa(x) = abs(f''(x)) / (1 + f'(x)^2)^(3/2).

For f(x)=alpha*x^2 with alpha>0, the maximum occurs at x=0 and
is 2*alpha. In particular y=x^2 has maximum curvature 2, not 1/2.

The next numerical claim, about Q(x,y)=(3*x+y)^2-y, has the same
factor-of-four error. Use orthonormal coordinates

    u = (3*x+y)/sqrt(10),  v = (-x+3*y)/sqrt(10).

Then Q=0 becomes

    v = (10*sqrt(10)/3)*u^2 - u/3.

A translation removes the linear term. Its maximum curvature is
20*sqrt(10)/3, approximately 21.08, rather than approximately 5.27.
The translation between F and Q does not change curvature. The
printed sufficient condition that maximum curvature be less than 2
is not itself refuted here; the incorrect formula can cause a reader
to apply that condition to an ineligible curve.

The original first-edition, first-printing page image was inspected.
Current and historical Volume 4A and Fascicle 1 errata were screened,
including the original PDF of all4a-pre page 28. No correction of this
defect was located. Targeted public searches found no matching report;
this does not establish absolute novelty. The source record is
`sources/graphics-source-check.json`. The calculations/traces here
were checked by hand; no general verifier or census was run.
