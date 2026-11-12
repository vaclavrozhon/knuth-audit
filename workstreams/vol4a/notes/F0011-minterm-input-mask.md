# V4A-F0011: masking decoder inputs loses the prefix condition

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), answer 7.1.2-33, printed page 565 / file page 582.
Original: `images/bookwise-p565.png`.

A minterm is the indicator of one complete assignment of the input
bits. The first N minterms here include the all-zero assignment (see
the decoder definition on 109). For N much smaller than 2^n, the answer
proposes forming P = NOT(x1) AND ... AND NOT(xk), ANDing P into the
remaining variables, and then reducing to n-k variables.

Take n=4, N=3. The printed choice floor(log2 N)=n-k-1 gives k=2.
The reduced inputs are y3=P AND x3 and y4=P AND x4. Both original
inputs 0000 and 1000 produce (y3,y4)=(0,0). Yet their required first
minterm values are respectively 1 and 0. No decoder using only those
two reduced inputs can distinguish them. In particular, its zero
minterm NOT(y3) AND NOT(y4) incorrectly returns 1 at 1000.

The claimed bound N+O(sqrt(N))+O(n) is not refuted. A repair is to
keep P as an enable condition in the minterm construction. Split the
remaining O(log N) bits into two halves; compute their minterms and
AND P into every minterm of one half, then form the N required pair
products. The extra masking costs O(sqrt(N)) gates, and forming P
costs O(n). Simply masking the raw variables does not do this.

The current and historical Volume 4A errata, and both Fascicle 0
layers, were screened. The listed corrections near this answer concern
23, 28, 29 and 31, not this construction. Two targeted public searches
found no matching report. This is a limited source screen, not proof
of absolute novelty. See `sources/minterm-mask-source-check.json`.
No mathematical computation was needed.
