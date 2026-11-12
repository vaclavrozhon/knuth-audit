# FSQRT: every input class and the complete integer square-root recurrence

2026-11-06. Source: `mmix-arith-20250620.w` 1723–1767, identical in the
2013 version; primary definition `mmix-doc-20131017.w` 1217–1238 and
1321–1331. The exact input/unpack/packing proofs are in
`fp-comparisons-recovery.md` and `fp-conversions-recovery.md`.
This note completes the finite recurrence, instead of treating the special
value counterexample as evidence for unexamined numerical branches.

Permitted instruction states have a valid rA, Y∈{0,1,2,3,4}, and any
64-bit operand Z. Y=0 takes rA's mode; Y=1,2,3,4 selects that mode
explicitly. The dispatcher rejects other Y values, which are outside the
valid instruction domain. The C model has unsigned 32-bit tetra and at
least 32-bit two's-complement int; thus `ze&1` expresses exponent parity
also for negative normalized exponents. All native shifts below have
nonnegative counts at most 30.

## Special values, including the exact known failure

The four unpacked classes and two signs give eight disjoint cases, with
NaN additionally split by its quiet bit:

* ±0 returns the same signed zero without an arithmetic event.
* +infinity returns +infinity without an arithmetic event.
* Negative nonzero finite values and −infinity return the canonical
  negative quiet NaN and I, as the MMIX definition requires.
* Positive quiet NaN returns unchanged; positive signaling NaN returns
  with its quiet bit set and all other bits preserved, with I.
* Negative NaNs are misclassified in both originals: S0003 gives the exact
  full-family disproof and the complete correction of the type guard.

After that audit-only guard correction, the last two cases have the same
proper quieting/payload rule for either sign. All positive finite values
follow the numeric recurrence below. The original's NaN defect is kept
separate from the mathematically correct book definition.

## Normalize the radicand and identify every digit supplied to the loop

For positive finite Z, the proved unpack invariant is

`Z = F * 2^(e−1076),  2^54≤F<2^55,  F≡0 mod 4,  −52≤e≤2045`.

Let p=e mod 2∈{0,1}, and D=F*2^p. The code makes precisely this
one-bit shift when e is odd. D is in [2^54,2^56), fits exactly in octa,
and is divisible by four. The leading base-four digit
`a=floor(D/2^54)` is 1, 2 or 3. The initialization `xf=2`, `rf=a−1`
therefore represents n=1=floor(sqrt(a)) and remainder a−1.

The 53 loop iterations append the following base-four digits, from most
to least significant:

* k=53,…,43: eleven pairs of D's high tetra, at bit offsets 20,…,0;
* k=42,…,27: sixteen pairs of its low tetra, at offsets 30,…,0;
* k=26,…,1: twenty-six zero pairs.

The first 27 pairs supply all 54 bits below the initial leading digit;
the final 26 pairs append 52 zero bits. Thus the complete integer whose
root is extracted is exactly **S=D*2^52**, with no omitted or repeated
input bits. Counts and shifts are valid at both split boundaries 43/42
and 27/26.

## Loop invariant, both decision branches, and fixed-width bounds

After any prefix has been processed, let s denote that base-four prefix.
The invariant is

`s=n^2+r,  n=floor(sqrt(s)),  0≤r≤2n,  xf=2n,  rf=r`.

It holds at initialization. Appending digit a∈{0,1,2,3} changes s to
`4s+a=(2n)^2+(4r+a)`. The next root digit is 1 exactly when
`4r+a≥4n+1`, since `(2n+1)^2=(2n)^2+4n+1`.
The source first sets rf to 4r+a and xf to 4n; its two-tetra comparison
is exactly the unsigned comparison `rf>xf`. Equality correctly takes
the zero digit. On the one-digit branch it subtracts xf+1, then adds
two to xf in total, obtaining root 2n+1 and its exact remainder.
On the zero-digit branch it leaves root 2n and remainder 4r+a.
In either branch the remainder is nonnegative and below the gap to the
next square, so the invariant is preserved. No approximate real root is
used to make the decision.

At the end, S<2^108 and n<2^54, so xf=2n<2^55. Before any final
iteration n<2^53 and r≤2n, hence 4r+a<2^56. All intermediate octa
values therefore fit far below 2^64, and subtraction is nonnegative on
the branch where it is performed. The two direct `xf.l++` operations
cannot lose a carry into xf.h: just before them xf is 4n, so its two low
bits are zero and its low tetra is at most #fffffffc. Adding one and
then one reaches at most #fffffffe. The final sticky increment starts
with an even low tetra, at most #fffffffe, and reaches at most #ffffffff.
It also cannot overflow the low tetra. These bounds justify the actual
half-word updates, not just an abstract unlimited integer recurrence.

The loop always executes exactly 53 steps; it has no data-dependent exit.
Unpacking was already proved to need at most 52 normalization shifts.

## Exact final rounding information and exponent

The invariant gives n=floor(sqrt(S)) and r=S−n^2. If r=0, xf=2n is
exactly 2sqrt(S). If r>0, 2sqrt(S) lies strictly between 2n and 2n+2;
the required jam value J(2sqrt(S)) is 2n+1, whether the fractional
part is below or above the intervening odd integer. The code's final
`xf.l++` produces exactly that value. There is no appeal to a potentially
invalid left-shift of previously jammed data.

The exponent is
`xe=floor((e+1022)/2)`. Its shifted argument is positive (970–3067),
so the native right shift is ordinary floor division. With e=2h+p,
xe=h+511, and the exact pre-jam fraction is
`2sqrt(S)=sqrt(F)*2^(p/2+27)`. Therefore

`2sqrt(S) * 2^(xe−1076) = sqrt(F) * 2^((e−1076)/2) = sqrt(Z)`.

Moreover S∈[2^106,2^108), so the delivered normalized fraction lies in
[2^54,2^55). The exponent xe is between 485 and 1533, inclusive; even
a rounding carry stays far inside the normal finite binary64 range.
Thus fpack needs no underflow or overflow branch, and the separate S0002
defect is unreachable here. The proved guard/sticky lemma supplies every
nearest-even and directed rounding decision for all four modes.

For exactness, S is an integer divisible by 2^54. If S is a square,
n is divisible by 2^27, so xf=2n has both rounding bits zero and no X
is raised. If it is not a square, the final jam value is odd and fpack
raises X. These are exactly the representable-root and inexact-root
cases: a rational square root of an integer is integral, while every
binary64 root at this scale would give such an integral root of S.
There is no I on the positive finite path and no Z/O/U on any valid
square-root path. The only extra original event is S0003's erroneous I
for negative quiet NaNs.

## Instruction composition and limits

The dispatcher has already copied the source and optional rounding operand
before the result store, so destination/source aliasing is harmless. The
valid Y check and selected mode are explicit. Helper events are merged
into the instruction accumulator and, with arithmetic trips disabled, into
the rA event bits as previously proved. The declared architectural cost
is 40υ; the 53 fixed extraction steps are software implementation work,
not a replacement timing model.

This completes all result and disabled-trip event branches of FSQRT after
the single S0003 guard correction. It separately records which complete
input family contradicts the official originals. It does not establish
arbitrary enabled-handler behavior or a blanket IEEE-library theorem.
