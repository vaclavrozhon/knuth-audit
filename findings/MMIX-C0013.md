# MMIX-C0013 — The StackRoom stack count is understated

**Confirmed · low severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / §1.4.3′ answer 5, p. 117; code p. 81

The described call chain has 11 stack entries rather than 10. The interpreter’s functional behavior is unchanged.

At line 097, res is $2 and rL=1. PUSHJ makes marginal $2 local before pushing three entries. The answer incorrectly treats it like the global-register case and counts only two.

## Publication review, 12 November 2026

The cited PUSHJ path pushes three stack entries after promoting the marginal register. Its StackRoom count is 3+3+3+2 = 11, not 10. This establishes the stated path discrepancy, not a separately proved global worst case.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0013.md](../workstreams/vol1-fasc1/notes/MMIX-C0013.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
