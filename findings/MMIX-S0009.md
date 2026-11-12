# MMIX-S0009 — Long decimal integer parts lose their scale

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX-ARITH §§68,73–79, scan_const; source1397–1503, rendered pages30–33.

Valid long floating constants can be wrong by many powers of ten. Counting omitted integer positions repairs the demonstrated scaling defect; the broader decimal interface remains under review.

scan_const reads1 followed by769 zeros and e-769 as0.1, although the literal is exactly1. Both inspected releases lose the omitted decimal position.

## Publication review, 12 November 2026

scan_const fails to compensate the decimal exponent for significant integer digits discarded after its 769-digit buffer fills. The valid 775-character string 1 followed by 769 zeros and e-769 has exact value 1 but returns the nearest representation of 0.1. The independent review confirms the buffer/decimal-point invariant; the direct routine interface has no documented 769-digit limit.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md).

## Detailed arguments

- [MMIX-S0009-scan-constant-integer-length.md](../workstreams/vol1-fasc1/notes/MMIX-S0009-scan-constant-integer-length.md)
- [scan-constant-integer-length-contract.md](../workstreams/vol1-fasc1/notes/scan-constant-integer-length-contract.md)
- [mmix-software-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-software-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
