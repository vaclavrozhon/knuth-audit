# MMIX-C0022 — SAVE makes local and global register renaming observable

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / §1.4.1′–10, p.114, second paragraph of the answer

Moving a variable between a local and global register across SAVE can change the result even when every stated exception is respected. The SAVE implementation and its context-restoration contract are correct.

The answer extends register equivalence to SAVE when its destination is global. Yet SAVE makes former locals marginal zero while retaining other global values. Two otherwise identical programs therefore return0 and5.

## Publication review, 12 November 2026

The answer explicitly extends local/global register equivalence to programs containing SAVE. SAVE sets rL to zero, so swapping a local register with a global register changes a subsequent read from 5 to 0 in the recorded witness. The original question excludes SAVE, but the separate extension in the answer does not.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0022-save-register-equivalence.md](../workstreams/vol1-fasc1/notes/MMIX-C0022-save-register-equivalence.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
