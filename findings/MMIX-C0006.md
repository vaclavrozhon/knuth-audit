# MMIX-C0006 — The jump-trace address sequence uses a one-byte step

**Confirmed · low severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / 1.4.3′–22, p.93, first paragraph

Change y₁+1 to y₁+4 in the exercise description. No implemented tracer is claimed to fail.

Exercise 1.4.3′–22 lists sequential instruction locations as y₁, y₁+1, …, x₂. MMIX instructions occupy four bytes and Fetch advances by four. A normal instruction at #100 followed by a jump at #104 visits those two addresses, not #101 through #103. Original typesetting checked; no matching repository erratum.

## Publication review, 12 November 2026

The jump-trace addresses advance by four bytes per instruction. The printed y1,y1+1 sequence uses the wrong address unit.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0006.md](../workstreams/vol1-fasc1/notes/MMIX-C0006.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
