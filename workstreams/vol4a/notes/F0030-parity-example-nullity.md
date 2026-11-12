# V4A-F0030: The parity example reports zero instead of two basis vectors

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), printed page 618 / file page 635.
Original: `images/bookwise-p618.png`.

Here r is the number of independent vectors returned by subroutine N.
The example displays five vectors gamma_1,...,gamma_5, with

    gamma_1 = 111101111,
    gamma_2 = gamma_3 = 010101010,
    gamma_4 = 000000000,
    gamma_5 = 001010100.

The first, second and fifth are independent: gamma_1 alone has its
outer bits, and gamma_2 and gamma_5 are distinct nonzero vectors.
Thus their rank is three and the nullity is 5-3=2. Indeed, the text
immediately displays the two independent answers

    theta_1 = 011000110, theta_2 = 000101000.

Replace the example's r=0 by r=2. The earlier instruction to initialize
r to zero before running the subroutine is correct and stays unchanged.
The first zero-row indices c_1=c_2=5 still exclude a perfect 9x9 pattern.

The original page image and the relevant current/historical Volume 4A
and Fascicle 1 errata were checked. No matching correction or public
report was located; absolute novelty is not established. See
`sources/bitwise-tail-source-check.json`. The short calculation above
was checked by hand, without a general verifier or census.
