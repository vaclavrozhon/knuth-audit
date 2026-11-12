# V4A-F0053: The vector-addition loop never advances

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), answer 7.1.4-255(b), printed 675 / file 692. Original:
`images/bookwise-p675.png`.

The answer represents integer-valued vectors by families f_k and g_k
of positions whose kth bit is 1. It initializes the carry family c
to empty and the bit index k to 0, then, while k < m, sets the sum
family h_k and the next carry c. Neither assignment changes k, and
there is no increment in the loop.

For every m > 0, the guard therefore remains true and the algorithm
repeatedly processes bit zero. Insert `k <- k+1` after the two
assignments. Then each iteration computes one sum bit and propagates
the carry to the next bit. The bit formulas themselves have the
ordinary full-adder meaning and were checked by hand.

No matching correction was found in the screened 4A/Fascicle 1
errata or targeted public reports. See `sources/zdd-tail-source-check.json`.
Absolute novelty is not established.
