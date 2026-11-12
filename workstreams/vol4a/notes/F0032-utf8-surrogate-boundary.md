# V4A-F0032: The surrogate filter rejects the valid UTF-8 prefix ED 80

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), printed page 619 / file page 636.
Original: `images/bookwise-p619.png`.

The added clause is ANDed into a value whose sign determines whether
a UTF-8 prefix is accepted. For the two leading bytes

    a1 = 0xED, a2 = 0x80,

all three earlier validity conditions hold. But the added term is

    0x20 - (0xED80 xor 0xEDA0) = 0x20 - 0x20 = 0.

ANDing with zero makes the final result nonnegative, so the prefix
is rejected. Yet ED 80 80 encodes U+D000, outside the excluded
surrogate interval U+D800 through U+DFFF. Varying the final byte
from 80 through BF gives 64 legitimate scalar values.

The undesired prefixes are exactly ED A0 through ED BF, for which
the XOR is between 0 and 31. The sign test must accept XOR values
at least 32. Replace 0x20 by 0x1F in the added subtraction: then
the factor is negative precisely when the XOR is at least 32.

The original page image and the relevant current/historical Volume 4A
and Fascicle 1 errata were checked. No matching correction or public
report was located; absolute novelty is not established. See
`sources/bitwise-tail-source-check.json`. The short calculation above
was checked by hand, without a general verifier or census.
