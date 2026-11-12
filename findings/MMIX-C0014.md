# MMIX-C0014 — PUT rL truncates a large operand before taking the minimum

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / §1.4.3′ answer 9, p. 118, PutL

The simulator discards all local registers for a legal PUT rL operand. Compare before converting the value to bytes.

With rL=1 and $255=2^61, PUT rL,$255 must leave rL unchanged. The answer shifts the operand left by three first; it wraps to zero and incorrectly sets simulated rL=0.

## Publication review, 12 November 2026

PutL shifts its operand left by three before comparing it. A value 2^61 wraps to zero and incorrectly changes rL = 1 to zero, whereas the instruction must leave rL unchanged. The primary C simulator compares the full value before shifting.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0014.md](../workstreams/vol1-fasc1/notes/MMIX-C0014.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
