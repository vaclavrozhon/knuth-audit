# V4A-F0018: the distance-three prefix XOR loses an incoming carry

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), answer 7.1.3-66(d), printed page 593 / file page 610.
Original: `images/bookwise-p593.png`.

The requested transformation is

    v = u XOR (u << 3) XOR (u << 6) XOR ...,

truncated to n bits. The answer processes n = 64m bits as words
u_0, ..., u_(m-1), starting at the least significant word. Within
word j it first computes the local prefix XOR t, then sets

    v_j = t XOR c,
    c = (t >> 61) * #9249249249249249.

All these operations are on 64-bit words. The second assignment
discards the incoming carry c, even though its high bits may have
to propagate to the next word.

Take n = 192 and u = 1, so that (u_0, u_1, u_2) = (1, 0, 0).
Writing P = #9249249249249249, whose set bits are 0, 3, ..., 63,
the printed algorithm gives

    j = 0: t = P, v_0 = P, c = #4924924924924924;
    j = 1: t = 0, v_1 = c, c = 0;
    j = 2: t = 0, v_2 = 0.

But the required 192-bit result has a set bit at every position
0, 3, ..., 189. In particular its bit 129 is 1, whereas the
algorithm returns 0 there. Its third word should be
#2492492492492492.

Replace the carry assignment by

    c = (v_j >> 61) * #9249249249249249.

The outgoing carry must use the completed word v_j, including the
incoming carry. Its last three bits are exactly the three values
that continue the recurrence v_i = u_i XOR v_(i-3) into the next
word. Multiplication by P repeats these values in the three
residue classes modulo 3, with 64-bit truncation.

The historical and current Volume 4A errata and both Fascicle 1
errata layers were screened; fresh official copies match the
archived files. No matching correction was found. Targeted public
searches also found no matching report; this does not establish
absolute novelty. See `sources/prefix-xor-carry-source-check.json`.
The three-word trace was checked by hand; no exhaustive computation
was used.
