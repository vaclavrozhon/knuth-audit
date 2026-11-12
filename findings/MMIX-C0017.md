# MMIX-C0017 — Identical global definitions do not trigger an assembler error

**Confirmed · low severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / §1.3.2′, p. 35, point 4

Qualify the diagnostic claim: a conflicting definition causes an error. Existing program examples and local-label rules remain correct.

The book says a global label appearing twice is diagnosed. Both original assemblers accept repeated definitions when their value and pure/register type are unchanged, as shown by two identical X IS 1 lines.

## Publication review, 12 November 2026

MMIXAL accepts a repeated global definition when both its value and type agree with the previous definition. Thus the book statement that every repeated global label is diagnosed is too strong. Both the 2013 and 2025 implementations allow X IS 1 twice.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0017-identical-global-definition.md](../workstreams/vol1-fasc1/notes/MMIX-C0017-identical-global-definition.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
