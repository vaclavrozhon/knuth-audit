# MMIX-S0006 — Fgetws hides end of file as a successful empty read

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX-IO §§16–17, mmix_fgetws EOF return; source lines 225–272, rendered page 6.

A caller checking the documented negative result may fail to detect end of file and keep treating it as an empty successful read. The correction changes only EOF before any complete character.

With room for at least one wyde, a read at end of file returns zero success instead of −1. No character was read; the documented completion condition was not met.

## Publication review, 12 November 2026

Fgetws on an already empty noninteractive stream with size >= 2 returns zero after the first EOF, whereas the book and the C analogy both require -1 before any character. The finding deliberately excludes the separate ambiguity of a nonempty final line without a newline.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md).

## Detailed arguments

- [MMIX-S0006-fgetws-empty-eof.md](../workstreams/vol1-fasc1/notes/MMIX-S0006-fgetws-empty-eof.md)
- [mmix-software-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
