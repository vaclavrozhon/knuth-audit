# F232 — The broadcast clause count uses an undefined n

Confirmed in Volume4B, question394, printed354/file374.

The at-most-one encoding has p inputs and l=ceil(lg p) auxiliary bits.
Its displayed number of clauses is nl+n-2^l. Both occurrences of n should be p:

    p*l + p - 2^l.

Indeed, the clauses assigned to input j have count floor(lg(2p-j)),
so the total is the sum of floor(lg k) for p<=k<2p. The number of depth-l
leaves is 2p-2^l, and the other 2^l-p leaves have depth l-1. Their total
depth is p*l+p-2^l. For the printed p=3 example this gives five clauses.
The clauses themselves correctly enforce at most one true input, because
the binary suffixes of p,...,2p-1 are distinct prefix-free leaf addresses.

The original question and September23,2015 draft page170 have the same n typo.
Relevant current/historical4B and Fascicle6 errata and available TeX sources
contain no matching correction. The later n in Langford(n) is a separate
problem-size parameter and does not define the input count of this encoding.

Evidence: images/bookwise-encoding-q354.png; images/bookwise-fasc6a-394.png;
sources/bookwise-graph-order-source-check.json.
