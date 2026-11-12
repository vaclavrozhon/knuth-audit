# MMIX-S0005 — Fwrite reports success after a failed final block

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX-IO §18, mmix_fwrite short-write return; source lines 275–292, rendered page 7.

A caller may accept a failed output as complete, or underestimate how many bytes are missing. The correction uses the actual host count; later flush failures remain separately open.

A one-byte write rejected by the host returns zero success instead of −1. In every short host block, the routine counts all requested bytes as written.

## Publication review, 12 November 2026

Fwrite subtracts the requested block length before checking a short host write, then returns the negated remaining request. A one-byte request with host fwrite returning zero is consequently reported as success zero instead of -1. The general discrepancy is exactly the unwritten portion of that block; ignored fflush errors are outside this claim.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md).

## Detailed arguments

- [MMIX-S0005-fwrite-short-count.md](../workstreams/vol1-fasc1/notes/MMIX-S0005-fwrite-short-count.md)
- [mmix-software-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
