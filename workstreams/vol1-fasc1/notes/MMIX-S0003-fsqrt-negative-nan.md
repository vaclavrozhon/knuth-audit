# MMIX-S0003 — FSQRT misclassifies negative NaNs before NaN dispatch

**Confirmed, medium, companion program only.** Both original MMIX-ARITH
sources, 2013-10-17 and 2025-06-20, raise invalid for every negative quiet
NaN and replace negative NaN payloads by the canonical payload. The
correct architectural definition in the book is not a book finding.

## Exact MMIX contract and admissible state

The primary `mmix-doc-20131017.w`, lines 1217–1238, expressly applies its
standard floating conventions to square root. A quiet NaN operand Z is
returned unchanged; a signaling NaN is quieted while preserving the other
fraction bits and raises I. The FSQRT-specific text at 1321–1331 specifies
invalid for a negative infinity, normal or subnormal, and permits −0.
It does not redefine NaNs as negative numbers. The 2025 document is identical.
This contradiction therefore follows from MMIX's own explicit contract,
without importing an unspecified IEEE NaN-payload policy. The online
[primary instruction description](https://mmix.cs.hm.edu/doc/instructions/farith.html)
states the same rule.

Take rG=32, rL=0, rA=0 (nearest, all arithmetic trips disabled),
$254=#fff8000000000001, and `FSQRT $253,0,$254` (encoding #15fd00fe).
Both register indices are global and the rounding operand is valid.
The input has sign=1, exponent=2047 and fraction=2^51+1: it is a **quiet
NaN**, not a negative finite number or infinity. Required result:
$253=#fff8000000000001, with no new arithmetic event.

The actual source `froot`, lines 1723–1745, first calls funpack, which
returns `zt=nan`, `zs='-'` and exceptions=0. It then tests

```c
if (zs=='-' && zt!=zro) exceptions|=I_BIT, x=standard_NaN;
```

This is true, so the `case nan` clause is never reached. standard_NaN is
#7ff8000000000000; the final sign insertion gives **#fff8000000000000**
with internal I_BIT=#1000. The unchanged dispatcher calls froot, merges
exceptions, and writes its returned result. With disabled trips it records
the **rA I event #10**. It performs no subsequent NaN repair.

Thus the input both loses its low payload bit and incorrectly sets invalid.
For canonical negative quiet NaN #fff8000000000000 the value happens to
match, but I is still wrong. For negative signaling NaN #fff0000000000001,
I is appropriate but the required quieted payload #fff8000000000001 is lost.

## Whole failing family and complete guard correction

For sign=1, E=2047 and any F∈[2^51,2^52), the operand is a quiet NaN.
The first guard takes the same branch for every such F and raises I
spuriously. It preserves the value only when F=2^51. For every signaling
F∈[1,2^51), I belongs but all original payload bits are discarded.
This argument covers all negative NaN bit patterns and all rounding modes;
the mode is not examined on this path.

The audit-only change file `sources/audit-fsqrt-nan.ch` replaces the guard by

```c
if (zs=='-' && (zt==num || zt==inf))
  exceptions|=I_BIT, x=standard_NaN;
```

This leaves every negative finite value and −infinity unchanged. Positive
inputs and both zeros take precisely their old branches. Negative NaNs now
reach the existing NaN branch: its quiet-bit test sets I and adds the quiet
bit iff signaling, returns the original sign and other fraction bits, and
returns a quiet NaN unchanged without I. These disjoint type/sign cases
prove the correction on the entire changed domain and show that no numeric
branch changes. The positive finite square-root recurrence is separately
proved in `fp-square-root-recovery.md`; it is not assumed correct merely
because the ten reproduction cases pass.

## Original and public correction layers

The original digital MMIX-ARITH page 40, §§91–92, was rendered and visually
inspected: `images/mmix-arith-review-file040.png`. Its early negative guard
and subsequent NaN clause agree with both archived source bodies. This is
the companion program's original typesetting, not a claim about a physical
MMIXware book printing. Source hashes/provenance are in
`sources/fp-primary-metadata.json`.

`results/errata-S0003.json` records all eight inspected layers with hashes:
original and current Fascicle 1 errata, cumulative errata, the author's
MMIXware errata/current distribution page, the community bug list, the
community arithmetic-rounding report, and its warnings change file.
The matches concerning froot mini-index entries, rounding-mode installation,
and explanatory NaN wording do not alter this guard. No matching correction
was found in those layers. The existing sfpack/fplus repairs are separate.
This is not a claim of worldwide novelty or priority.

## Bounded reproduction

One run of `nice -n 15 python3 workstreams/vol1-fasc1/verify_fsqrt_nan.py`
tangled and compiled each original module and the 2025 module with only the
audit guard change. Ten selected cases were called once per build, **30
short calls total**, without running a simulator or enumerating floats.
Expected bit patterns come directly from the MMIX NaN/sign contract and
the exact identity sqrt(4)=2; no host floating-point oracle is used.

Each original has the three specified failures (negative payload qNaN,
canonical negative qNaN event, negative sNaN payload) and passes seven
controls (positive qNaN/sNaN, −0, −infinity, −1, +4, +infinity). The audit
change passes all ten. Exact rows and build logs are in
`results/fsqrt-nan.json` and `results/fsqrt-nan-build.json`.

The finding concerns wrong visible result/event behavior under a valid
instruction state. It does not assert correctness of arbitrary enabled
handlers, other library routines, or the entire IEEE implementation.
