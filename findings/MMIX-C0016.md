# MMIX-C0016 — Program P assigns one memory operation to the wrong phase

**Confirmed · low severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / §1.3.2′, p. 37, Program P timing paragraph

Correct the two phase coefficients to 10037μ and 2803μ. Both oops counts and the combined total are unchanged; the prime table remains correct.

The table-generation phase executes 499 stores and 9538 loads, so its memory coefficient is 10037. The printing phase executes 2803 memory operations. The book instead gives 10036 and 2804.

## Publication review, 12 November 2026

Program P has 10037 and 2803 memory accesses in the two phases, not 10036 and 2804. The total 12840 and the printed operation counts are unchanged.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0016-program-p-mems.md](../workstreams/vol1-fasc1/notes/MMIX-C0016-program-p-mems.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
