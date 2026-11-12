# MMIX-S0008 — Ftell loses the high half of large file positions

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX-IO §22, mmix_ftell; source lines 364–375, rendered page9.

Programs receive a false current position for large binary files. Preserving the high half fixes all successful positions while retaining both error returns.

A successful binary-file position of 2^32 becomes zero on LP64 hosts because MMIX-IO clears the high tetra.

## Publication review, 12 November 2026

On a supported LP64 host, Ftell stores a successful long result only in the low 32-bit tetra and sets the high tetra to zero. A legal successful position 2^32 is returned as zero. The existing reproduction models this legal host state; it is not a claim that a real 4 GiB file was tested, and it does not apply to 32-bit long hosts.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md).

## Detailed arguments

- [MMIX-S0008-ftell-high-tetra.md](../workstreams/vol1-fasc1/notes/MMIX-S0008-ftell-high-tetra.md)
- [mmix-software-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
