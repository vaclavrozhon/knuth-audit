# MMIX-S0002 — Directed overflow returns infinity instead of the finite limit

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX-ARITH §§31–35, fpack/sfpack overflow result; source lines 544 and 590, rendered pages 12–14.

Programs that rely on rounding toward zero, or on the inward directed bound, receive the wrong value after overflow. A separate audit correction handles both precisions; enabled handlers are outside the proved scope.

With arithmetic trips disabled, STSF stores +infinity for the finite value 2^128 in ROUND_OFF mode. The MMIX contract inherits the standard rule requiring the largest finite binary32 value. Both inspected releases have the same omission in their binary64 packer.

## Publication review, 12 November 2026

Both floating packers return infinity on directed overflow even when rounding requires the finite limit. With trips disabled, STSF of 2^128 in ROUND_OFF must store #7f7fffff, but stores #7f800000. The interpretation explicitly uses the adopted IEEE 754-1985 overflow contract; the O and X flags themselves are set.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md).

## Detailed arguments

- [MMIX-S0002-directed-overflow.md](../workstreams/vol1-fasc1/notes/MMIX-S0002-directed-overflow.md)
- [fp-overflow-contract.md](../workstreams/vol1-fasc1/notes/fp-overflow-contract.md)
- [fp-conversions-recovery.md](../workstreams/vol1-fasc1/notes/fp-conversions-recovery.md)
- [mmix-software-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
