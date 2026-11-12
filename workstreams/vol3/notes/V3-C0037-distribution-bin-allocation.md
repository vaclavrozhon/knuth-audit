# V3-C0037 — The top-level distribution can address an unallocated bin

Confirmed, low. Volume 3, second edition, first printing (1998),
§5.2.5, printed p.176 / file p.187, final paragraph.

The proposed two-level distribution sort allocates floor(N/8) bins
and maps a key K in [0,1) to index floor(KN/8). For N not divisible
by8, that map can return floor(N/8), which requires one more bin.

For example, N=17 gives two bins, indexed0 and1. The valid key
K=33/34 maps to floor(33/16)=2. More generally, write N=8q+r with
1<=r<=7. Every key in [8q/N,1) maps to q, outside the q allocated bins.
This interval is nonempty for arbitrarily large N; the issue is not
restricted to a small-input base case.

Either allocate **ceil(N/8)** bins with the printed mapping, or use
floor(K floor(N/8)) with the printed bin count (and the usual small-file
base case). Both changes preserve the intended linear number of bins
and asymptotic result.

The original floor brackets were checked in `images/bookwise-p176.png`.
All five freshly matched errata layers were screened; see
`sources/distribution-errata-review.json`. No corresponding correction
was found. Targeted public searches for the p.176 bin formula and
errata found no matching report. Absolute priority and later printings
remain unverified. This report concerns the book's explicit allocation
and mapping, not a claim that Tamminen's original implementation fails.
