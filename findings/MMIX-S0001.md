# MMIX-S0001 — Epsilon comparison drops a nonzero low-order term

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX-ARITH §53, fepscomp long-shift branch; source line 958, rendered arithmetic page 22.

FCMPE returns 0 instead of +1; FEQLE can return 1 instead of 0. This can change a program’s comparison or branch result. The fascicle’s mathematical definition remains correct.

For 1 and -2^-55 with epsilon=1/2, both inspected MMIXware releases report similarity, although the exact distance exceeds both neighborhoods. The d>54 branch suppresses the test that should detect the lost positive fraction.

## Publication review, 12 November 2026

The fepscomp branch for exponent difference d > 54 sets oo = zf and suppresses the needed upward correction. For y = 1, z = -2^-55, epsilon = 1/2 it reports similarity although the exact difference exceeds the allowed radius; the corresponding FCMPE result is 0 instead of +1.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md).

## Detailed arguments

- [fp-comparisons-recovery.md](../workstreams/vol1-fasc1/notes/fp-comparisons-recovery.md)
- [MMIX-S0001-fepscomp.md](../workstreams/vol1-fasc1/notes/MMIX-S0001-fepscomp.md)
- [mmix-software-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
