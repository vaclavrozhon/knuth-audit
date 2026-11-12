# V4A-F0031: Double precision can be one bit too short for the subset-sum gap

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), printed page 620 / file page 637.
Original: `images/bookwise-p620.png`.

The lambda function is floor(log2 x), as defined on page 142.
The exercise assumes n>=lambda(m). Take n=2, m=7, and the seven
2-bit inputs

    1, 2, 3, 3, 3, 3, 3.

The assumption holds because lambda(7)=2. Subsets of 1 and 2 cover
0 through 3, and adjoining each additional 3 extends the covered
interval by three. Thus every value from 0 through 18 is attainable,
and the least missing positive value is y=19.

The printed algorithm puts s_0=1 and s_1=17. Starting from y=1,
it adds those two sums and obtains 19. Both s_1 and y exceed the
maximum 15 representable by two unsigned 2-bit words. If those
additions are performed modulo 16, it instead returns 3, which is
already one of the inputs.

This is not confined to tiny words: for n=8, use the eight powers
1,2,4,...,128 and 503 copies of 255 (m=511). The first missing sum
is 128521, requiring 17 bits rather than 16.

One extra magnitude bit suffices for the stated premise, since
m<2^(n+1) and each input is below 2^n. Alternatively require
m<=2^n (equivalently n>=ceil(log2 m)) for the two-word unsigned
magnitude bound. This finding concerns the explicit precision claim,
not the linear-time method with adequate arithmetic width.

The original page image and the relevant current/historical Volume 4A
and Fascicle 1 errata were checked. No matching correction or public
report was located; absolute novelty is not established. See
`sources/bitwise-tail-source-check.json`. The short calculation above
was checked by hand, without a general verifier or census.
