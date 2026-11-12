# MMIX-C0010 — The recursive-simulation guarantee compares chunks with byte capacity

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / answer1.4.3′–21, p126, second paragraph

The printed lower-bound argument is invalid. The actual failure depth and whether the numerical conclusion is false remain unresolved.

The recurrence bounds a number of chunks. The proof compares it with2^61 bytes instead of the capacity559670633304293 nodes, each occupying4120 bytes. This does not justify the claimed100^6065 instruction guarantee.

## Publication review, 12 November 2026

The recursion simulation capacity argument compares a count of 4120-byte chunks with a byte capacity. The claimed 100^6065 guarantee does not follow. A corrected recurrence bound fits through depth 4640, but this is not a demonstrated maximum depth or a complete replacement theorem.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0010.md](../workstreams/vol1-fasc1/notes/MMIX-C0010.md)
- [MMIX-C0010-bookwise-proof-review.md](../workstreams/vol1-fasc1/notes/MMIX-C0010-bookwise-proof-review.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
