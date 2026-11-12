# V4A-F0025: The parabola example has an endpoint off the curve

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), printed page 614 / file page 631.
Original: `images/bookwise-p614.png`.

The example specifies

    Q(x,y) = 9*x^2 + 6*x*y + y^2 - y,
    F(x,y) = Q(x+1/2,y+1/2),
    (xi-prime,eta-prime) = (-5/2,-19/2),
    (x-prime,y-prime) = (-2,9).

But F(-5/2,-19/2)=Q(-2,-9)=234, not zero. Rounding eta-prime
according to (164) gives -9, not the printed +9.

Replace eta-prime by 17/2. Then Q(-2,9)=0 and rounding gives
(-2,9), as required. This also preserves a monotonic arc from the
other stated endpoint (-5/12,-1/4): the parametrization

    xi(t) = (t-t^2)/3 - 1/2,  eta(t) = t^2 - 1/2,
    1/2 <= t <= 3,

decreases in xi and increases in eta. This is a correction to the
specific example, not a refutation of the general algorithm.

The original first-edition, first-printing page image was inspected.
Current and historical Volume 4A and Fascicle 1 errata were screened,
including the original PDF of all4a-pre page 28. No correction of this
defect was located. Targeted public searches found no matching report;
this does not establish absolute novelty. The source record is
`sources/graphics-source-check.json`. The calculations/traces here
were checked by hand; no general verifier or census was run.
