# F201: The last unused wire has no preservation clauses

Volume 4B, answer 7.2.2.2–64, printed pages 559–560 (PDF 579–580).

The six clauses for a comparator [i:j] correctly range over i<j.
The following two clauses preserve wire i when it is unused, but the
printed common range is again 1≤i<j≤n. It never supplies those two
clauses for i=n. They need their own range 1≤i≤n, at every layer.

A three-wire counterexample uses four layers: empty, [2:3], empty,
[1:3]. The actual input 110 evolves to 110, 101, 101, 101, and therefore
is not sorted. The printed clauses instead permit the trace

    110 -> 111 -> 111 -> 110 -> 011.

Only the last wire changes illegally, in the empty layers. Every
active comparator operates correctly, the other unused wires are
preserved, and the final vector is the sorted input. Direct evaluation
verifies all 144 printed clauses, including the comparator selection
tree. Adding the missing last-wire clauses rejects steps 1 and 3.

This also supplies a false network model for all inputs after prefix
[1:2]: its only unsorted outputs are 010 and 110; 010 is correctly
handled by the real suffix and 110 has the false trace above. The
already sorted inputs have constant traces. Thus this is more than
a harmless omitted condition in an otherwise correct transformation.

The author's `sat-mintime-sort.w` has a separate loop for all untouched
lines and is correct on this issue. The book and the 2015 draft both
use the insufficient common range; no current erratum was located.

Evidence: `check_bookwise_sat64_77.py`, `results/bookwise-sat64-77.json`,
`images/bookwise-sort-p559.png`, `images/bookwise-life-p560.png`,
`sources/bookwise-sat-mintime-sort.w`.
