# MMIX-C0011 — Three omitted no-op opcodes

**Confirmed · low severity.** Published fascicle · Digital release 3 · 2023.

Location: §1.3.1′–52 answer, printed97 (file105)

The answer gives an incomplete classification. For example, ZSNZ $255,$255,$255 always preserves its operand, and $255 is always global.

The answer to exercise1.3.1′–52 omits ZSNZ, CSZI and PUTI, although each has operands that preserve every permitted program state.

## Publication review, 12 November 2026

The claimed no-op opcode classification omits ZSNZ, CSZI and PUTI: ZSNZ $255,$255,$255, CSZI $255,$255,0 and PUTI rL,255 preserve state. The finding establishes these omissions, not a new exhaustive classification.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0011.md](../workstreams/vol1-fasc1/notes/MMIX-C0011.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
