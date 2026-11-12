# MMIX-C0007 — SAVE exits after storing the first global register

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / answer1.4.3′–11, p120, BNZ after INCL ss,8

The supplied SAVE implementation produces an incomplete saved context.

With rG=254, the first global-register iteration compares8×254 with8×28, leaving t=1. After storing $254, BNZ jumps to the exit, skipping $255, all required special registers and the final rG/rA octabyte. The branch must be BZ. Exact manual trace, original typesetting and relevant errata checked.

## Publication review, 12 November 2026

In the printed SAVE simulation the branch after incrementing s has the wrong polarity. With rG = 254, BNZ exits after the first global register; BZ is required at this test. This is a book-program error.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0007.md](../workstreams/vol1-fasc1/notes/MMIX-C0007.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
