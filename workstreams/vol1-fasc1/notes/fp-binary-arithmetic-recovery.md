# FADD, FSUB, FMUL and FDIV: complete data paths and explicit remaining scope

2026-11-06. The printed page-12/13 obligation is that these instructions
compute the stated floating operations. This note proves their actual
MMIX-ARITH paths for every input class, including the caller invariants
needed by the previously proved packer. It does not infer implementation
correctness from the architectural definitions or from a few examples.

The code is `sources/mmix-arith-20250620.w`, lines 150–318 and 707–874.
The primary instruction contracts are `mmix-doc-20131017.w` 1217–1306;
the 2025 document is byte-identical. The four dispatcher cases, destination
write and exception merge in `mmix-sim-20250620.w` are identical to those
previously inspected in the 2013 simulator. The current source was extracted
from the already saved author archive, not downloaded or built again.

Assumptions: `tetra` is an unsigned 32-bit type, `int` can represent the
small exponents/limb indices and values through 131071, and ordinary valid
instruction/register state is provided by the already checked decoder.
The standard source uses the usual '+'/'-' character values for signs;
only equality to '-' determines the output sign. Arithmetic operands are
arbitrary 64-bit words, rA selects any of the four modes, and **arithmetic
trips are disabled for the final result/event claim**. Enabled-handler
replacement and external IEEE trap-format issues remain separate. No host
floating-point arithmetic is assumed.

The original fpack directed-overflow defect S0002 remains a counterexample
to unconditional correctness of every composed operation. What is proved is:

1. every pre-packing data path supplies the correct result information;
2. every non-overflow result and disabled-trip event is correct;
3. composition with the already proved S0002 audit-only packing correction
   gives the correct result for the entire disabled-trip domain.

This does not add another finding or claim that the official code has been
repaired. The old 2013 fplus d>53 threshold is a known repaired defect and
is not included in the current-code proof. No old test run was repeated.

## 1. Shared normalization, jam identities and complete NaN handling

The exact `funpack` proof in `fp-comparisons-recovery.md` gives, for every
nonzero finite value,

`|x| = F * 2^(e−1076),  2^54≤F<2^55,  F≡0 (mod 4),  −52≤e≤2045`.

Normal and subnormal inputs both satisfy these same hypotheses. The
normalizing loop terminates within 52 steps. `oplus`, `ominus` and logical
octa shifts implement their exact unsigned operations whenever the bounds
below exclude wraparound; no unproved native 64-bit signed arithmetic is
substituted for them.

For real t≥0 let J(t) be floor(t), with its least bit set if t is not an
integer. The previously proved guard/sticky lemma completely determines
rounding of t/4 and exactness from J(t). Two additional identities are
used here, for every even integer A and 0≤t<A in the subtraction case:

`J(A+t)=A+J(t)`, and `J(A−t)=A−J(t)`.

For integral t they are immediate. Otherwise write t=n+f, 0<f<1.
For n even, J(t)=n+1 and floor(A−t)=A−n−1 is odd; for n odd, J(t)=n
and floor(A−t)=A−n−1 is even and gets its low bit set. These are exactly
the second identity. Addition preserves the parity of floor(t), proving
the first. Jammed right shifts compose: `J(J(t)/2^k)=J(t/2^k)`, as already
proved. Jammed left shifts do **not** generally compose; the cancellation
branches below explicitly avoid assuming that false rule.

There are four operand classes (zero, nonzero finite, infinity, NaN),
so sixteen ordered class pairs. The shared NaN fragment covers exactly
the seven pairs with at least one NaN. It tests both signaling bits when
both operands are NaNs, raises I iff at least one is signaling, and returns
Z's NaN when present, otherwise Y's. Only the selected signaling NaN is
quieted in the returned copy; both original operands are unchanged. Thus
the specified payload/sign preference and I predicate hold in all seven
cases. No numeric invalid, Z, O, U or X branch is reached for those pairs.

## 2. FADD: all finite alignment and cancellation branches

The seven NaN pairs are handled above. For the other special pairs:

* zero+finite and finite+zero call fpack with the original exact unpacked
  value and ROUND_OFF; this is independent of the current mode because
  there is nothing to round. A subnormal may produce raw U, which is
  suppressed by the disabled-trip dispatcher when X is absent.
* equal-sign infinities, and one infinity plus a finite or zero value,
  return that signed infinity, with no arithmetic event.
* opposite-sign infinities produce quiet NaN(1/2) with Z's sign and I.
* zero+zero preserves a common sign. With differing signs it gives −0
  exactly in ROUND_DOWN, otherwise +0. Equal-magnitude opposite nonzero
  finite words have the same zero/sign rule. The raw-word cancellation
  test is exact because nonzero finite magnitude encodings are unique.

That covers every special pair and exact cancellation. In the remaining
finite case, exchange operands if needed so the magnitude of Y is larger.
Write A=Y's fraction, B=Z's fraction, d=eY−eZ≥0. Lexicographic exponent/
fraction order is exact for the normalized values. The output sign is
Y's sign; for equal signs this is shared, and for different signs the
larger magnitude dominates. The desired positive fraction is
`T=A+B/2^d` or `T=A−B/2^d`, at exponent eY.

### d=0,1,2: alignment is exact

B is divisible by 4, so the right shift by d discards no information.
Addition is exact and lies below 2^56. If it reaches 2^55, a right shift
by one with jam and exponent increment supplies J(T/2); otherwise T is
already normalized.

Subtraction is an exact positive integer. For d=0 its minimum is 4,
since exact cancellation was removed; at most 52 left shifts normalize it.
For d=1 its minimum is 2, so at most 53 left shifts suffice. For d=2,
`T≥2^54−(2^55−4)/4>2^53`, so at most one shift is needed. Every left
shift is of an exact integer, not of a jammed approximation; it preserves
value when the exponent is decremented. The final fraction is in
[2^54,2^55), and no intermediate approaches 2^64.

### 3≤d≤54, equal signs

The code computes J(B/2^d). Since A is even, adding it yields exactly
J(T). The threshold test at the even integer power 2^55 chooses the same
normalization branch as exact T: a positive number just below that power
cannot jam upward across it, and one at or above it cannot jam below it.
A required one-bit right shift uses the composition identity. Thus the
packer receives the complete guard/sticky information, including ties.

### 3≤d≤54, different signs

Before alignment the code doubles A and decrements the exponent, while
changing the shift count to d−1. The exact fraction at this new exponent is

`T'=2A−B/2^(d−1)`.

Because d≥3, `T'≥2^55−(2^55−4)/4>2^54`; also T'<2^56. The subtraction
identity gives `2A−J(B/2^(d−1))=J(T')`. The strict lower bound proves
that this already jammed value is never shifted left. If it reaches
2^55, a single jammed right shift and exponent increment normalize it;
otherwise it is ready. This is the required proof for the extra guard
bit, not merely the example in the source comment.

### d>54: the deliberately special far-tail branch

Here `0<t=B/2^d<1`; d is at most 2097. The source replaces the tail by
1 without performing a potentially huge shift. For addition A+1=J(A+t)
and it remains below 2^55. For subtraction A−1=J(A−t), and it is
normalized unless A=2^54, since the next possible A is 2^54+4.

In that sole boundary case the code shifts A−1 left once, obtaining
`2^55−2` at exponent eY−1. This value is **not generally J of the exact
fraction** `2^55−2t`. However, it is equivalent for every required rounding
decision: the exact fraction lies strictly between 2^55−2 and 2^55.
After division by 4 it is strictly above the midpoint of the two adjacent
representable values. The code is exactly at that midpoint; nearest-even
still selects the upper endpoint because its significand is the even
integer 2^53. Directed modes select the same lower/upper endpoints for
both numbers, for either sign, and both indicate X. Since eZ≥−52 and
d≥55, eY≥3 and eY−1≥2. No later subnormal shift can invalidate this
round-equivalence argument. This handles the branch that a blanket
“the packer always receives J(T)” claim would miss.

### FADD composition, signs and events

All nonzero finite paths now satisfy either the exact J invariant or the
explicit four-mode boundary equivalence. The fixed-width bounds and finite
loop limits above cover every branch. Packing supplies the correct result
unless its already accepted directed-overflow defect S0002 applies; with
that audit correction, all result values are covered.

Every finite binary64 input is an integer multiple of 2^−1074. Their sum
or difference is too. If a nonzero exact result is below 2^−1022, it is
therefore an exactly representable subnormal. Consequently FADD has no
inexact underflow with trips disabled. Raw exact U is filtered as specified.
X is set exactly for a nonrepresentable rounded finite sum or for overflow;
O is the packer's proved overflow condition. I occurs only in the sNaN
and opposite-infinity cases described above. No Z is generated. The zero
branches do not manufacture an underflow event from exact cancellation.

## 3. FSUB: exact reduction, including NaN signs

The simulator copies Z to a temporary, calls the already proved fcomp to
classify it against zero, and flips only its sign bit when it is not NaN.
For finite values, infinities and signed zeros this is exact negation; it
preserves all remaining fields. For either kind of NaN the entire word,
including sign and payload, is retained. It then calls fplus with Y and
this temporary. That is the exact primary FSUB definition, not an
unconditional NaN-sign flip. Source registers remain unchanged even if X
aliases Y or Z: operands were copied before the destination write.
The preceding FADD proof consequently covers every FSUB class pair,
cancellation sign, rounding mode and event, with the same explicit S0002
and enabled-handler limitations.

## 4. omult: the actual complete unsigned multiplication kernel

Let b=2^16. Unpacking produces digits u_i,v_i∈[0,b), i=0,…,3,
with `U=Σu_i b^i` and `V=Σv_i b^i`. At the start of outer iteration j,
the initialized words w_0,…,w_(j+3) represent exactly

`P_j=U Σ_(h<j) v_h b^h < b^(j+4)`.

Initially P_0=0 and w_0,…,w_3 are initialized to zero. If v_j=0,
the next high word w_(j+4) is zero and the invariant persists. Otherwise
the inner loop adds `U*v_j*b^j` in four base-b columns. At each column,
`t=u_i*v_j+w_(i+j)+carry`, with all three digits/carry in [0,b), so
`0≤t≤(b−1)^2+2(b−1)=b^2−1`. The 32-bit unsigned type holds t exactly.
Writing t mod b and passing floor(t/b) preserves the partial product
identity and carry range. All read w cells were initialized by the prior
row or the current row; no uninitialized high word is read. Writing the
final carry to w_(j+4) gives P_(j+1).

Four outer rows, at most sixteen inner columns, therefore give exactly
U*V in eight digits. Pairwise packing of two 16-bit digits cannot overflow
a 32-bit word; the returned octa and aux are the low and high halves.
This is a proof of the concrete code and its zero-row branch, not an
unsupported appeal to Algorithm 4.3.1M.

## 5. FMUL: product scaling and all special pairs

For finite nonzero operands, let their fractions be A,B. The input B<<9
to omult is exact because B<2^55, hence B*2^9<2^64. The kernel returns
the exact product `P=A*B*2^9`, with aux=floor(P/2^64) and low remainder.
Thus aux=floor(A*B/2^55), and the low result is nonzero exactly when
A*B/2^55 is not integral.

If aux≥2^54, ORing its low bit on a nonzero remainder gives
`J(A*B/2^55)`. The exponent `eY+eZ−1021` makes its exact represented value
`A*B*2^(eY+eZ−2152)`, the required product. This fraction is below 2^55.

If aux<2^54, its value is at least 2^53. The code doubles it and
decrements the exponent. Write A*B/2^55=q+r, 0≤r<1. The required new
fraction is 2q+2r. Its J value is 2q when r=0, otherwise 2q+1, exactly
the doubled aux with sticky OR. No forgotten high remainder bit is
needed: whether 2r is below, at or above 1, that position is precisely
the sticky position at this scale. Again the normalized fraction lies
in [2^54,2^55). Exponents are between −1126 and 3069, safely representable.

For the nine non-NaN class pairs: zero*zero and zero*finite in either
order give zero; finite*infinity in either order and infinity*infinity
give infinity; zero*infinity in either order gives quiet NaN(1/2) and I;
finite*finite is the proved data path. Signs are XOR throughout these
non-NaN pairs, including signed zero and the invalid result. The expression
`ys+zs-'+'` equals '-' exactly for differing signs; the other two outcomes
are treated as positive by both the final bit insertion and fpack.

No normal finite path introduces I or Z. Correct X/U/O decisions and
non-overflow results follow from the proved caller invariant plus fpack
and the disabled-trip event filter. Directed overflow is precisely the
existing S0002 shared-packer failure, and the already proved correction
closes this whole result domain without a new multiplication patch.

## 6. odiv: complete proof on the precise FDIV input domain

FDIV calls `odiv(A,0,B<<9)` with 2^54≤A,B<2^55 and multiples of four.
The divisor V=B*2^9 satisfies 2^63≤V<2^64; A<V, so the routine's fallback
branch is unreachable. In base b=2^16 this always has **n=4 and d=0**:
the leading divisor digit is at least b/2 and the normalization shift
does nothing. All eight dividend and four divisor digits are initialized;
all array subscripts below stay in their declared ranges. No correctness
claim for unused n=1/2/3 or shifted-normalization branches is imported.

At quotient position j=3,2,1,0 the active five-digit window W satisfies
`0≤W<bV`. Initially it is `floor((A*b^4)/b^3)=bA<bV`. After a step the
next window is b times a remainder below V plus the next digit, hence
the same invariant. Let q=floor(W/V), so 0≤q<b.

The exact upper-quotient and second-digit lemmas from
`../../vol2/notes/division.md`, section “D3 a jedna korekce zbytku”, were
read in full before reuse. Their hypotheses match here: nonnegative
window below bV, n≥2, and normalized divisor. The following specialization
also checks the actual bounded C expressions and the test `h==b`.

Put a=v_3≥b/2, c=v_2, T=floor(W/b^3), s=floor(W/b^2) mod b,
`h=floor(T/a)`, `r=T−h*a`. Since a*b^3≤V, h≥q. Also

`W<(q+1)V<(q+1)(a+1)b^3`, hence `h<q+1+(q+1)/a≤q+3`.

Thus h≤q+2≤b+1. Define the two-digit estimate
`Q=floor(floor(W/b^2)/(ab+c))`. The cited lemma gives q≤Q≤q+1;
its proof uses `V<(ab+c+1)b^2` and ab+c≥b. The comparison
`h*c>r*b+s` is exactly h>Q. If h=b+1, Q≤b, so this second comparison
is necessarily true even though the code's first comparison is only
h==b. If h=b the first test reduces it. Each decrement occurs above q.

The initial r<a<b. All evaluated products fit exactly in unsigned
32 bits: h*c≤(b+1)(b−1)=b^2−1, r*b+s≤b^2−1, and the two-digit T
is below b^2. After increasing r by a the code breaks before re-evaluating
a shift if r≥b. Such a break cannot leave h=b: a preceding h=b+1 would
give new r=T−ba<b from W<bV and T<b(a+1). Otherwise h<b already, and
r≥b makes the second comparison automatically false because h*c<b^2.
Therefore termination gives **q≤h≤q+1 and h<b**. There are at most two
decrements, not an unbounded correction loop.

The actual subtraction loop maintains a nonnegative borrow k<b and computes

`t = w_i+(b^2−b)−k−h*v_i`.

Its exact minimum is zero and maximum b^2−1, because w_i,k,h,v_i are
digits. There is no hidden unsigned wrap. With w=w_i−k−h*v_i, writing
t mod b writes w mod b, and
`b−1−floor(t/b)=−floor(w/b)` is exactly the next borrow. Thus after four
columns the true difference W−hV is represented by the four low digits
and top coefficient `old_top−k`. As h=q or q+1, this coefficient is
0 for a nonnegative result and −1 for a negative one. The source's test
`old_top!=k` consequently detects exactly the needed correction.

If correction is needed, decrementing h and adding V to the four low
digits gives the exact remainder in [0,V). Each addition is at most
2b−1, so carry is 0 or 1. Exactly one final carry cancels the borrowed
b^4 and may be discarded. The obsolete top digit is never read again:
the next window uses the four just-corrected low digits. Otherwise the
nonnegative difference is already the proper remainder.

After all four quotient digits, N=(A*2^64)=Q_total*V+R with 0≤R<V.
The d=0 unnormalization leaves R unchanged and clears no needed digit;
the output packing is exact. The quotient fits in 64 bits because A<V.
This completes every executed branch of odiv on its actual FDIV domain,
including trial-estimate b+1, correction, carry and array bounds. It does
not rely on any old brute-force run from the other workstream.

## 7. FDIV: scaling, rounding and all special pairs

The kernel has just proved an exact quotient Q and remainder R for
`T=A*2^55/B`, with `2^54<T<2^56`. When Q<2^55, setting its low bit iff
R≠0 gives J(T). Otherwise the code shifts Q right once and increases
the exponent. It ORs the discarded low bit of Q into the remainder's
nonzero test. That yields exactly J(T/2), whether the fractional tail
comes from odd Q, nonzero R, or both. The resulting fraction is always
in [2^54,2^55).

The raw exponent eY−eZ+1021 satisfies
`T*2^(eY−eZ+1021−1076)=(A/B)*2^(eY−eZ)`, precisely |Y/Z|.
The possible exponent interval, including the one-bit normalization,
is contained in [−1076,3119]; no signed integer overflow occurs.

The seven NaN pairs were fully covered in section 1. Among the remaining
nine pairs, zero/finite, zero/infinity and finite/infinity return zero;
finite/zero returns infinity and Z; infinity/finite and infinity/zero
return infinity with no Z; zero/zero and infinity/infinity return quiet
NaN(1/2) and I; finite/finite uses the proved kernel. The sign is XOR in
every non-NaN branch, exactly as required, including infinity/zero's
explicit exception-free contract. Finite/finite has no I or Z.

Packing and the event filter now prove the non-overflow result and every
disabled-trip X/U/O decision. The existing S0002 overflow correction proves
the remaining result values in this same domain. No corrected general
enabled-handler implementation is asserted.

## 8. State preservation, declared costs and outstanding obligations

The simulator installs both old operands before invoking these routines,
so all destination/input alias cases are covered. Helpers mutate only their
local copies and arithmetic auxiliaries; a final destination store obeys
the already established local/global/marginal register rules. Each funpack
clears the helper exception accumulator before classification; subsequent
NaN tests examine both saved raw inputs, so the second unpack does not lose
a signaling event. `exc|=exceptions` then merges the completed instruction's
events. With all enable bits zero, exact U is suppressed and the remaining
bits are ORed into rA's event byte; preexisting event bits are retained.

All loops have explicit bounds: unpack at most 52 shifts per operand,
FADD normalization at most 53 shifts, omult four rows and at most sixteen
columns, odiv four quotient digits with at most two estimate decrements
and one four-digit correction each. All other transformations are bounded
octa shifts/assignments. These C operation counts are **not** substituted
for the book's architectural timing model. The declared costs are 4υ for
FADD, FSUB and FMUL and 40υ for FDIV; their table cells have already been
fully reconciled.

These four arithmetic leaves can leave the old undifferentiated partial
state: their complete current-code data paths are proved and their sole
remaining result contradiction in this domain is linked to the accepted
shared software finding S0002. Current-code non-overflow/disabled-trip
scope and corrected-overflow scope are separate structured fields.

Still open: FREM's reduction/parity state,
the FINT/FIX inexact-event interpretation, exceptional epsilon-domain
wording, and any explicitly claimed enabled-handler/complete-IEEE contract.
FSQRT's complete digit recurrence is now separately proved in
`fp-square-root-recovery.md`, with its negative-NaN defect recorded as S0003.
The whole page and the whole library remain partial. This note neither
adds tests nor repeats earlier reproductions; it supplies the missing
general invariants and exact source-to-contract reasoning.
