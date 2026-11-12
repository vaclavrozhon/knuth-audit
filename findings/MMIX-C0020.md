# MMIX-C0020 — Timer resets can make the traffic-light delay wait forever

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / §1.3.2′–34, pp.111–112, Delay entry and polling loop

The controller can remain on its initial light state indefinitely despite a waiting request. An additional positive-target example shows that changing the entry branch to include equality is insufficient.

When the first interval-counter value equals the requested delay, the routine sets its target to zero. A prompt timer handler can reset the counter before any user read sees zero, so the loop never returns.

## Publication review, 12 November 2026

Delay can loop forever under legal prompt resets of rI. With ref_time = 0 and every observed counter value in (0,2^63), its signed comparison always continues. The finite native trace illustrates the invariant; the infinite-loop claim follows from the repeating legal state schedule, not from a timeout. The known delay-to-delta correction is already applied.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0020-delay-reset-loop.md](../workstreams/vol1-fasc1/notes/MMIX-C0020-delay-reset-loop.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
