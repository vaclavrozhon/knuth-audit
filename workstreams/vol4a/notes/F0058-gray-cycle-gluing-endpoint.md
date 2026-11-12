# V4A-F0058: A cycle splice uses the wrong endpoint

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), answer 7.2.1.1-45(d), Case2, printed 686 / file 703.
Original: `images/bookwise-p686.png`.

Here xor denotes bitwise exclusive-or. The vertices u and v are
adjacent in a coordinate above the two least significant bits. The
answer removes the edges

    (u xor 2)--(u xor 3),   (v xor 2)--(v xor 3)

from two cycles. It proposes to insert

    (u xor 2)--(v xor 3),   (u xor 3)--(v xor 3).

The first proposed edge changes two bits: the coordinate in which
u and v differ, and the lowest bit. It is therefore not a cube edge.
Moreover v xor 3 receives both inserted edges, while v xor 2 receives
neither, so the result cannot be a cycle even as an abstract splice.

The intended pair is

    (u xor 2)--(v xor 2),   (u xor 3)--(v xor 3).

Both are cube edges and each of the four exposed endpoints is used
once. Change the first occurrence of `v xor 3` in the inserted pair
to `v xor 2`. The preceding splice in part(b) is correct: its first
endpoint is u xor 2, as confirmed by enlarging the original.

No correction was found in the screened current/historical 4A and
Fascicle2 errata or targeted public reports. The same typo appears
in the 2009 Fascicle2 replacement. See
`sources/gray-cycles-source-check.json`. Absolute novelty is not
established. The endpoint and adjacency check was done by hand.
