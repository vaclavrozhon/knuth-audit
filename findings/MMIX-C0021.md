# MMIX-C0021 — Repeated nonzero GREG values do not each allocate a register

**Confirmed · low severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / §1.4.1′–10, p.114, first sentence of the answer

The stated startup register threshold can be wrong. Count actual new global-register allocations; the assembler itself is correct.

The answer sets initial rG to255 minus the number of GREG operations. Two GREG declarations with the same nonzero initializer share register254, so rG is254 rather than253.

## Publication review, 12 November 2026

The initial rG formula counts declarations instead of distinct allocated registers. Nonzero GREG declarations with equal values coalesce: two GREG 1 declarations both allocate register 254, giving rG = 254 rather than 253.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0021-greg-coalescing-count.md](../workstreams/vol1-fasc1/notes/MMIX-C0021-greg-coalescing-count.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
