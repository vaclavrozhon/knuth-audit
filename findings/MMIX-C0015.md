# MMIX-C0015 — RESUME ropcode 1 overwrites the saved Y operand

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / §1.4.3′ answer 14, p. 123, line 168

The simulator computes the wrong result when resuming an instruction with saved operands. Preserve rY and rZ through operand installation.

For a legal resumed ADDU with rY=1, rZ=2 and $254=100, the result must be 3. The branch to Install_Y reloads $254 and instead produces 102.

## Publication review, 12 November 2026

The BOD resuming,Install_Y branch reinstalls an ordinary Y operand during ropcode 1, which must use the saved rY/rZ operands. The recorded ADDU example produces 102 instead of 3. A complete repair also handles immediate-Y operations; changing this branch alone is insufficient.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0015.md](../workstreams/vol1-fasc1/notes/MMIX-C0015.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
