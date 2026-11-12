# MMIX-C0004 — A permitted null byte discards the rest of the input line

**Confirmed · medium severity.** Published fascicle · Digital release 3 · 2023.

Location: MMIX / 1.4.2′, p. 68, NextChar line 21

The example loses non-whitespace input that follows a permitted null byte. Track the buffer length separately, or explicitly exclude null bytes from the input specification.

The coroutine specification ignores every input byte at most #20, including #00. Under the book’s Fgets contract, the input a NUL b . LF c . LF must produce ab. LF. NextChar treats the internal NUL as the end of its buffer, refills immediately, and instead produces ac. LF. The short manual trace and original typesetting were checked; no matching correction was found in the relevant repository errata.

## Publication review, 12 November 2026

The NextChar routine uses zero as an end-of-buffer sentinel, although the stated input convention accepts NUL as whitespace. An embedded NUL discards the unread suffix of the fetched line. Either track its length or exclude NUL explicitly.

Decision: `retained`. No matching prior report was found in the checked sources; absolute priority is not established.

[Review record](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md).

## Detailed arguments

- [MMIX-C0004.md](../workstreams/vol1-fasc1/notes/MMIX-C0004.md)
- [mmix-book-publication-review.md](../integration/2026-11-12-novelty-review/notes/mmix-book-publication-review.md)

Books and full-page scans are not included. Original arguments retain their source language; the current review above governs any historical status headings.
