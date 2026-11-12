# MMIX-C0008 — GetArgs uses the internal address to find a virtual chunk boundary

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / answers1.4.3′–16/17, p124, GetArgs

Simulated input can lose bytes at chunk boundaries; the shared output routine is affected too.

GetArgs masks internal address x instead of virtual address z. A valid17-byte read starting16 bytes before a virtual chunk boundary is treated as fitting in one chunk; the seventeenth byte lands in internal padding. The node layout gives an exact address counterexample. Change AND zz,x,Mem:mask to AND zz,z,Mem:mask. Original typesetting and errata checked.

## Publication review, 12 November 2026

GetArgs masks the internal translated address x when computing bytes left in the chunk. It must mask the original virtual address z. At virtual offset #ff0 the printed code permits 4056 bytes instead of 16 and can write into allocation padding.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0008.md](../workstreams/vol1-fasc1/notes/MMIX-C0008.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
