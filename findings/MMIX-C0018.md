# MMIX-C0018 — Both saddlepoint averages miscount instruction paths

**Confirmed · low severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / §1.3.2′–20, p. 104, both running-time formulas

The first discrepancy tends to a nonzero constant; the second grows linearly along square matrices. Neither fits its stated vanishing error term. The search routines and both printed all-zero costs remain correct.

The first formula misses 2υ at the final branch. The second omits Phase2 memory work and understates its instruction costs. Complete path profiles and independent probability proofs give corrected expectations for both printed programs.

## Publication review, 12 November 2026

Both saddlepoint timing answers omit costs. The first misses two units for the final unsuccessful predicted branch (constant 13, not 11). The second counts only phase-one memory accesses and omits phase-two costs of linear expected size on square arrays. The programs and the already applied 2012 branch correction remain valid.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0018-saddlepoint-average-cost.md](../workstreams/vol1-fasc1/notes/MMIX-C0018-saddlepoint-average-cost.md)
- [recovery-pages-054-110-112.md](../workstreams/vol1-fasc1/notes/recovery-pages-054-110-112.md)
- [exercises-1.3.2-020-distinct-recovery.md](../workstreams/vol1-fasc1/notes/exercises-1.3.2-020-distinct-recovery.md)
- [exercises-1.3.2-020-binary-recovery.md](../workstreams/vol1-fasc1/notes/exercises-1.3.2-020-binary-recovery.md)
- [exercises-1.3.2-020-third-recovery.md](../workstreams/vol1-fasc1/notes/exercises-1.3.2-020-third-recovery.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
