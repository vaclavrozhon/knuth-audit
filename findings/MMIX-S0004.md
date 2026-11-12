# MMIX-S0004 — Integerization silently drops the inexact event

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX-ARITH §§86–88, fintegerize rounding and fixit unpack; source lines 1631–1649 and 1668, rendered pages 37–38.

Programs that inspect rA cannot detect precision lost by integerization. A separate correction both detects discarded fractional bits and preserves the event through FIX/FIXU conversion.

For the exact input 1/2, FINT, FIX and FIXU return the correct zero but fail to set X. Both inspected MMIXware releases omit the required event for every finite nonintegral input.

## Publication review, 12 November 2026

FINT rounds nonintegral finite inputs without setting X; FIX and FIXU additionally erase exceptions through a second funpack. For +1/2 in nearest mode the numeric result zero is right but rA remains zero instead of recording X. This relies on the adopted IEEE 754-1985 integerization/conversion contract, not a reversal of the one-way phrase only if.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md).

## Detailed arguments

- [MMIX-S0004-integerization-inexact.md](../workstreams/vol1-fasc1/notes/MMIX-S0004-integerization-inexact.md)
- [fp-conversions-recovery.md](../workstreams/vol1-fasc1/notes/fp-conversions-recovery.md)
- [mmix-software-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
