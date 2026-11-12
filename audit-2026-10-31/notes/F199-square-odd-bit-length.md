# F199: Square encoding excludes odd-length squares

Volume 4B, answer 7.2.2.2–45, printed page 556 (PDF page 576).

Let t be the number of output bits and let x and y be the two factors.
The answer allocates floor(t/2) bits to x and ceil(t/2) bits to y,
equates their common bits, and forces the extra bit of y to zero.
Consequently both factors have at most floor(t/2) bits.

For t=5, the perfectly valid square z=25 (binary 11001) is rejected:
the constraints make x=y at most 3, so xy is at most 9. This is not
an issue confined to a one-bit multiplier. More generally, if t=2k+1,
every square with a nonzero leading output bit is excluded, because
x=y<2^k implies xy<2^(2k).

Use m=n=ceil(t/2), equate all corresponding factor bits, and, when t
is odd, set the extra output bit z_(t+1) to zero. The product now has
2m output positions; this final zero constrains it to the given t-bit
range without restricting the square root prematurely.

The floor, ceiling and complemented y_n were inspected in the original
2022 PDF and in the author's September 23, 2015 draft, printed page 192.
The current 4B and Fascicle 6 errata contain no matching correction.
No solver run is needed for this direct size contradiction. The physical
printing has not been inspected, and no report has been sent.

Evidence: `images/bookwise-factor-576.png`,
`images/bookwise-fasc6a-factor-200.png`, and
`sources/bookwise-factor-learning-source-check.json`.
