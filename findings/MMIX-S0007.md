# MMIX-S0007 — MMIXAL rejects nearby targets across the signed-address boundary

**Confirmed · low severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIXAL §§126 and 131, known YZ/XYZ relative-address calculation; source lines 2984–3005 and 3080–3101, rendered pages 50 and 52.

Valid relative instructions cannot be assembled consistently near #8000000000000000. Forming the displacement before scaling fixes both fields while retaining the exact range restrictions.

An address one tetrabyte away across bit63 is accepted as a future reference but rejected when already defined. Both known-address paths shift too early.

## Publication review, 12 November 2026

MMIXAL shifts source and target separately using signed arithmetic before subtracting. A known target #8000000000000000 from location #7ffffffffffffffc is incorrectly rejected although its relative displacement is +1 instruction. The equivalent future reference succeeds; GETA witnesses that execution across the user/kernel boundary is not an assumption.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md).

## Detailed arguments

- [MMIX-S0007-relative-address-boundary.md](../workstreams/vol1-fasc1/notes/MMIX-S0007-relative-address-boundary.md)
- [recovery-pages-046-048.md](../workstreams/vol1-fasc1/notes/recovery-pages-046-048.md)
- [mmix-software-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
