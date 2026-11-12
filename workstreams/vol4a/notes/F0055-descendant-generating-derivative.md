# V4A-F0055: Incorrect intermediate generating-function derivative

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), answer 7.1.4-267, printed 678 / file 695. Original:
`images/bookwise-p678.png`.

The answer defines Z(w,z) as the sum of w^zeta(T) z^|T| over ordered
trees T, where zeta is its auxiliary ZDD-size statistic. It gives
the functional equation

    Z(w,z) = wz + w^2 z Z(w,z)/(1-Z(w,wz)).

Set s=sqrt(1-4z). The printed derivative is
`Z_w(1,z)=z/s+z/s^2`. Its coefficient of z is 2. But the unique
one-vertex tree has zeta=1, so that coefficient must be 1.

Differentiating the displayed functional equation gives instead

    Z_w(1,z) = z/s + z/(4s^2) - z/4.

Indeed, with T=Z(1,z)=(1-s)/2, A=Z_w(1,z), and Z_z(1,z)=1/s,
the differentiated equation reduces to

    s A/(1-T) = z + 2T^2 + T^3/s.

This simplifies to the corrected expression. Its first coefficients
are z+3z^2+10z^3+36z^4, consistent with the auxiliary recurrence.

The corrected derivative produces the answer's final forest first
moment `z/(1-4z)+2z/s`. The printed average and its asymptotic form
therefore need no change on account of this intermediate error.
The separate extrema errors are recorded as V4A-F0054.

No matching correction was found in the screened 4A/Fascicle 1
errata or targeted public reports. See `sources/zdd-tail-source-check.json`.
Absolute novelty is not established. Differentiation was checked by hand.
