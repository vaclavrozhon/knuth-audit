# MMIX-C0001 — The golden-ratio constant is rounded, not a 64-bit prefix

**Confirmed · low severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / 1.3.1′, p. 8, paragraph after (7)

A mathematical description should say rounded to 64 fractional bits. The constant and multiplication example do not need changing.

The text calls #9e3779b97f4a7c16 the first 64 binary fractional bits of phi^-1. An exact integer inequality gives the prefix #9e3779b97f4a7c15. The displayed value is correctly rounded; the multiplication example and high-half identity remain correct. Original typesetting checked; no matching correction in the repository fascicle errata. Provisional for independent review.

## Publication review, 12 November 2026

The hexadecimal constant is the nearest rounded 64-bit value of phi inverse, not its first 64 fractional bits: the prefix ends in c15 and the printed constant in c16. The constant and its intended multiplication remain valid.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0001.md](../workstreams/vol1-fasc1/notes/MMIX-C0001.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
