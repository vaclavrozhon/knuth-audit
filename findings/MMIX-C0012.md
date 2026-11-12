# MMIX-C0012 — GetReg timing omits marginal-register overhead

**Confirmed · low severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / §1.4.3′ answer 2, pp. 116–117; code on p. 80

The extra 6υ must apply to both local and marginal source registers. The routine still returns the correct zero value.

With rL=2,rG=32 and k=3, the register is marginal but GetReg takes its longer nonglobal path. The cost is μ+12υ, while the stated local-only indicator predicts μ+6υ.

## Publication review, 12 November 2026

The GetReg cost uses a local-register indicator where the additional path also occurs for marginal registers. With rL = 2, rG = 32, k = 3 the marginal path costs 12v rather than 6v.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0012.md](../workstreams/vol1-fasc1/notes/MMIX-C0012.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
