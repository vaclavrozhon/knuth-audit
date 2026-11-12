# V4A-F0022: a strong chain's right shift leaks between packed fields

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), exercise 7.1.3-114, printed page 193 / file page 210, and its
answer, printed page 601 / file page 618. Originals:
`images/bookwise-p193.png` and `images/bookwise-p601.png`.

The exercise requests a chain of the same length r that evaluates
an n-bit strong chain simultaneously on m packed n-bit fields.
The answer copies each operation, broadcasting constants except
for shift counts. Being strong means that the original operations
also give their n-bit intermediate values without truncation; it
does not prohibit a right shift from discarding low bits.

Take n = m = 2 and the strong one-step chain f(x) = x >> 1.
Pack the two inputs 1 and 0 into X_0 = (01 00)_2 = 4. The answer
produces

    X_1 = X_0 >> 1 = (00 10)_2 = 2,

but the requested result is (f(1) f(0))_4 = (00 00)_2 = 0.
The discarded low bit of the first field enters the second field.
The shift amount here is a fixed constant, as required.

In fact the same-length assertion itself fails in this example.
The required four-bit function is (X >> 1) & 5: its bit 0 is
input bit 1, and its bit 1 is always zero. A single bitwise
Boolean, addition, or subtraction step has its bit 0 determined
by input bit 0 and constants, so cannot compute this function.
A left shift has bit 0 zero. A right shift must be by 1 to obtain
the correct bit 0, but then its bit 1 is input bit 2, not zero.
These exhaust the allowed one-step operations.

For this example a right shift followed by a field mask is enough.
More generally, right shifts need boundary masks (or stronger
conditions that ensure the discarded bits are zero), with a
constant-factor allowance in the chain length. The qualitative
statement on page 155 about essentially simultaneous evaluation
is not refuted by this example.

The five relevant errata layers were screened, including the
definition and answer pages. No matching correction was found;
fresh official files match the archived copies. Targeted public
searches found no matching report, which does not establish
absolute novelty. See `sources/strong-chain-source-check.json`.
The two-field trace and the one-step obstruction were checked by
hand; no census was run.
