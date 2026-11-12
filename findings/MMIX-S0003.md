# MMIX-S0003 — FSQRT treats negative NaNs as negative numbers

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX-ARITH §91, froot negative-input guard; source line 1734, rendered page 40.

A valid FSQRT instruction corrupts negative NaN payloads and reports an invalid event for quiet NaNs. A one-guard audit correction fixes every affected NaN while preserving numeric branches.

For the negative quiet NaN #fff8000000000001, both inspected releases return the canonical #fff8000000000000 and raise invalid. MMIX explicitly requires preserving that quiet NaN without an invalid event. Negative signaling NaNs also lose their payload.

## Publication review, 12 November 2026

The negative-input guard in froot precedes NaN dispatch. Negative quiet NaN #fff8000000000001 loses its payload bit and spuriously raises invalid, contrary to MMIX’s explicit NaN rule. The correction must exempt NaNs while still rejecting negative nonzero numbers and negative infinity.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md).

## Detailed arguments

- [MMIX-S0003-fsqrt-negative-nan.md](../workstreams/vol1-fasc1/notes/MMIX-S0003-fsqrt-negative-nan.md)
- [fp-square-root-recovery.md](../workstreams/vol1-fasc1/notes/fp-square-root-recovery.md)
- [mmix-software-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
