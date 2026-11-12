# MMIX-C0003 — A NEG trip saves the immediate Y operand in rY

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / §1.3.1′, p. 18, trip context paragraph

The description gives a handler the wrong saved operand. The author’s frozen MMIXware source explicitly confirms the immediate value; the NEG operation itself is correct.

The text says every non-store trip saves register $Y in rY. For NEG, Y is an immediate operand. With $1=123 and $2=-2^63, NEG $3,1,$2 traps on overflow and saves rY=1, not 123.

## Publication review, 12 November 2026

The blanket statement rY = $Y on a trip fails for NEG, whose Y operand is immediate. NEG $3,1,$2 with $2 the minimum signed octabyte trips with rY = 1, independently of $1.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0003.md](../workstreams/vol1-fasc1/notes/MMIX-C0003.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
