# MMIX-C0023 — Ropcode 2 wrongly rejects the ignored original RESUME opcode

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / §1.4.3′–14, p.122, final opcode guard in the RESUME answer

A permitted RESUME set operation terminates the interpreter. Correcting the guard also requires setting the actual internal opcode to ORI so AllDone clears the resume state.

A valid set operation with rX=#02000000f9f0f7f8 must write444 to global register240. The printed opcode guard exits instead, even though ropcode2 does not execute that opcode.

## Publication review, 12 November 2026

The simulated RESUME rejects an original opcode RESUME even for ropcode 2, where that opcode is ignored. The recorded legal set-register example is rejected. MMIX-PIPE has the correct ordering; MMIX-SIM shares the book defect. This remains one finding, not a duplicate software card.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [exercises-1.4.3-014-recovery.md](../workstreams/vol1-fasc1/notes/exercises-1.4.3-014-recovery.md)
- [MMIX-C0023-resume-set-opcode.md](../workstreams/vol1-fasc1/notes/MMIX-C0023-resume-set-opcode.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
