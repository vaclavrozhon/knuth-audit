# MMIX-C0009 — MemFind timing swaps miss and allocation indicators

**Confirmed · low severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / §1.4.3′ answer 2, p. 117; definitions on p. 116

The two misses add 10μ+28υ, giving 15μ+148υ with the stated base cost. The program itself still finds the correct memory location. Historical averages were not reproduced.

The definitions and direct path counts require C=U=2,A=0 for two misses on existing chunks. The next page uses C=A=2 and adds the wrong penalty. The printed empirical means also violate A≤U with the stated definitions.

## Publication review, 12 November 2026

The MemFind timing paragraph interchanges the miss and allocation indicators. With U denoting a key miss and A a new allocation, their coefficients are (3mu+6v)U and (2mu+11v)A. The reported averages also violate A <= U if read with the printed labels; their empirical values were not recomputed.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0009.md](../workstreams/vol1-fasc1/notes/MMIX-C0009.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
