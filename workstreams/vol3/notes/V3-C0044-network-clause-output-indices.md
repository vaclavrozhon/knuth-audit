# V3-C0044 — Two clause-output indices omit a factor n

Confirmed in volume 3, second edition, first printing (1998), answer
5.3.4-52, printed p.672, file p.683. The last sentences of parts (a) and
(b) identify the clause outputs with indices `2m+2n+j` and `2m+2n+k`.
They should be `2mn+2n+j` and `2mn+2n+k`.

Here n is the number of Boolean variables and m the number of clauses.
The circuit reserves 2n initial variable wires and another 2mn wires for
literal copies, so the m clause outputs come after wire 2mn+2n. The
comparators specified earlier in the same answer already use this
correct offset. For the displayed example with m=3 and n=5, the clause
outputs are wires 41,42,43; the printed concluding expressions instead
point to wires 17,18,19, which are literal-copy wires.

This is a local error in the explanatory indices. The actual comparator
construction uses the correct wires, and the reduction is not refuted.

Original p.672 and the circuit context on p.242 were visually checked;
see `images/bookwise-p672.png` and `images/bookwise-p242.png`. All five
official errata layers were screened in `sources/networks-errata-review.json`.
A targeted public search for Knuth, p.672, and the 2mn offset found no
report of this error. This limited screen does not establish priority.
