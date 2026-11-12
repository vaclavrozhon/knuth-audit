# FREM: complete exact-remainder, parity and termination proof

2026-11-06. The primary contract is `mmix-doc-20131017.w` 1308–1318:
the result is Y−nZ, where n is the nearest integer to Y/Z and ties choose
even n; zero inherits Y's sign. Standard NaN conventions have priority.
The actual dispatcher calls `fremstep(y,z,2500)` in both saved simulator
versions. This note proves that actual instruction call for every 64-bit
input pair and every valid rA mode, with arithmetic trips disabled for the
final event claim. It does not require a proof of the uncalled partial-step
API for other delta values.

Source: both saved MMIX-ARITH versions, lines 1779–1848, have identical
remainder code. The unsigned-octa helpers, normalization and exact packing
lemmas were proved in `fp-comparisons-recovery.md` and
`fp-conversions-recovery.md`; the complete shared NaN fragment is also
reconciled in `fp-binary-arithmetic-recovery.md`, section 1. Here tetra is
unsigned 32-bit and int has at least the range of a 32-bit signed integer.

## 1. Every exceptional operand class

The seven pairs containing at least one NaN use the established shared
fragment: Z's NaN has preference, otherwise Y's; the selected payload and
sign are preserved, its quiet bit is set when needed, and I is raised
iff at least one input is signaling. A quiet NaN combined with a numeric
otherwise-invalid operand does not bypass the standard NaN priority rule.

Of the remaining nine pairs, zero/zero, finite/zero, infinity/zero,
infinity/finite and infinity/infinity return canonical quiet NaN with
Y's sign and I. The three pairs zero/finite, zero/infinity and
finite/infinity return Y unchanged and have no arithmetic event. This
preserves either zero sign and every finite subnormal exactly. The sole
remaining class pair is nonzero finite/nonzero finite, proved below.

## 2. The actual instruction never returns an incomplete remainder

For the two finite nonzero inputs the unpacked invariant gives fractions
A,B∈[2^54,2^55), each divisible by four, and exponents a,b∈[−52,2045].
The maximum exponent difference is 2097. Consequently

`thresh=max(a−2500,b)=b`

for every such input pair. The while loop thus reduces until the current
exponent is below b or explicitly selects the complement/zero exit.
The subsequent branch that would set E_BIT and return an incomplete result
is unreachable: its condition is the condition whose negation ended the
loop. No hidden external interrupt result is accepted as the instruction's
final value.

## 3. Exact magnitude and parity invariant during reduction

Let Y0=|Y| and Z0=|Z|. During reduction maintain the mathematical state

`Y0 = q Z0 + R`, where `R=F*2^(e−1076)>0`, `q≥0` is an integer,
`2^54≤F<2^55`, `F≡0 (mod 4)`, and `odd=q mod 2`.

The integer q is a proof variable; it is never stored in the program and
can be very large. Initially q=0, F=A, e=a and odd=0. The original Y sign
is left unchanged throughout; the divisor's sign is immaterial to the
magnitude reduction.

When F=B and e≥b, R=2^(e−b)Z0 is an exact integer multiple. The immediate
zero exit is therefore correct even when e>b, and preserves the original
Y sign. No parity is needed for an exact zero.

When F<B and e=b, the current R is already strictly between 0 and Z0,
so the code goes directly to the final complement comparison. When F<B
and e>b, first replacing (F,e) by (2F,e−1) preserves R. This ensures
the fraction is now strictly greater than B: F≥2^54 and B<2^55 imply
2F>B, so a zero subtraction cannot create an infinite normalization loop.

In every other reduction path F>B at an exponent e≥b, so subtracting B
from F subtracts precisely `2^(e−b)Z0` from R. This preserves the displayed
identity with `q←q+2^(e−b)`. The difference is positive. If the input
fraction was not doubled, it is below 2^54. If doubled, its new difference
2F−B is less than the old F (because F<B), hence below 2^55. In both
cases it is a positive multiple of four, and no octa wraparound occurs.
Left normalization, accompanied by e decrements, preserves R and restores
the interval [2^54,2^55), in at most 52 shifts.

Every subtraction at e>b adds an even multiple of Z0 and preserves odd=0.
At e=b it adds one and the code sets odd=1. Such an odd addition can occur
at most once: its resulting R is less than Z0. If normalization leaves
e=b, the next comparison has F<B and exits to the complement step; if it
lowers e, the while loop ends. Thus `odd=1` is correct here; replacing it
by a toggle is unnecessary, and no preceding odd addition can have been
forgotten.

Every nonterminating outer iteration decreases e by at least one. An
undoubled difference needs at least one normalization shift; a doubled
case already decreased e before subtraction. A step at e=b then exits or
falls below b. There are at most max(0,a−b+1)≤2098 iterations. Bounds on
thresh and normalized exponents are small signed integers, not unbounded
machine counters.

## 4. Both completion paths and every tie

If the loop ends with e≤b−2, then

`R/Z0=(F/B)2^(e−b)<2/4=1/2`.

The nearest quotient is q, so R with Y's original sign is already the
required answer. The code returns it with exact packing.

If it ends with e=b−1, dividing F by two aligns the remainder at exponent
b. This is an exact integer shift because F is divisible by four; the
aligned C=F/2 is divisible by two and satisfies 0<C<B. The other entry
to `try_complement` already has e=b and F<B, so set C=F there. Both
entries therefore mean exactly

`Y0=qZ0+C*2^(b−1076)`, with `0<C<B` and the proved parity odd.

The alternative magnitude is D=B−C, with opposite sign. The code chooses
C when D>C, because the fraction is below one half; it chooses D when
D<C, corresponding to the quotient q+1. At equality it chooses C iff
odd=0; otherwise it chooses D. Thus a half tie selects the even one of
q and q+1, in both parity cases. This is precisely the nearest-even integer
quotient in the IEEE remainder definition, not truncation or a remainder
using the current floating rounding mode.

The selected magnitude is min(C,B−C)≤B/2<2^54 and is positive. It is an
integer multiple of two; at least one left-normalization shift therefore
restores divisibility by four. At most 53 shifts suffice even for the
minimum possible integer magnitude two. No zero reaches this loop.
The exact exponent/fraction representation is preserved throughout.

For negative Y, nearest-even rounding of Y/Z negates the corresponding
quotient for its absolute value, up to the divisor sign; changing the
divisor sign negates n and leaves nZ unchanged. Hence the chosen output
sign is exactly Y's sign for C and its opposite for D, as the source sets
`xs`. The q-parity rule is unaffected by negating q. The explicit zero
exit uses Y's original sign. This proves all four input sign combinations.

## 5. Exact representability, events, state and declared cost

Every binary64 input is an integer multiple of 2^−1074. Every reduction
subtracts an integer multiple of the divisor, so each positive R is such
a multiple and at least 2^−1074. It also remains no larger than Y0.
The final complement is a difference of the same kind. All normalized
fractions above have at most 53 significant bits (they are divisible by
four); if the value is subnormal, its multiple-of-2^−1074 property guarantees
that the subnormal packing shift discards no bit. The final remainder is
therefore exactly representable as a binary64 value in every branch.

Also `|remainder|≤|Z|/2` in the finite/finite case, so it cannot overflow.
The exact-input return for an infinite divisor cannot overflow either.
Consequently S0002's directed-overflow branch is unreachable. Packing with
ROUND_OFF preserves the exact result independent of the current rA mode.
There is no X or O; raw exact U, if supplied by fpack for a tiny result,
is suppressed by the already proved disabled-trip event merge. No Z event
occurs: a zero divisor is an invalid operation I, as classified above.

Both operands were copied before the final destination store, so all
permitted input/output alias cases are covered. The standard destination
allocation rule and the existing rA-event OR rule apply. No memory access
is performed by the arithmetic operation itself. Its stipulated timing is
4υ in the printed table; the finite software reduction loop and its bound
are not substituted for that architecture cost. The companion source
explicitly discusses why a hardware remainder may have a long latency.

This closes the actual FREM result and disabled-trip event obligation for
all input words. No new finding or execution run was needed. The smaller
delta API, arbitrary enabled handlers and unrelated IEEE-global assertions
are outside this instruction proof; none is silently marked proved.
