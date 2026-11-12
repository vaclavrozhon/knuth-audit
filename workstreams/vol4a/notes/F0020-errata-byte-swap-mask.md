# V4A-F0020: the replacement bytewise min/max routine expands its mask incorrectly

Confirmed, medium severity. This is a defect in the official errata,
not in the original first-printing routine. The entry dated 30 June
2016 replaces answer 7.1.3-98 on printed page 598 / file page 615.
It appears on page 27 of `errata/pdf/all4a-pre.pdf`; the original
typesetting is preserved in `images/bookwise-errata-answer98.png`.

The replacement first sets the high bit of each byte of t for
which x_j < y_j. It then gives

    t = (t - (t >> 1)) + t,
    v = (x XOR y) & t,
    z = x XOR v,
    w = y XOR v.

The goal is z_j = max(x_j,y_j) and w_j = min(x_j,y_j). But the
mask expansion changes a flagged byte #80 into #c0, not #ff.
Consequently only the top two bits are available for the swap.

Take the 64-bit words x = 0 and y = 1. The comparison correctly
produces t = #80. The next line yields

    t = (128 - 64) + 128 = 192,
    v = 1 & 192 = 0,
    z = 0, w = 1.

The requested least significant bytes are z_0 = 1 and w_0 = 0.
All other bytes are zero, so this is also a complete word-level
counterexample without interactions between neighboring bytes.

Replace the shift by `t >> 7`. Then each flagged byte becomes
(128 - 1) + 128 = 255, while an unflagged byte remains zero.
Neither arithmetic operation causes a carry or borrow between
bytes. This preserves the replacement's stated operation count.

The current official `all4a-pre.ps.gz` was freshly retrieved and
matches the archived source. The subsequent Volume 4A errata and
both Fascicle 1 layers contain no later correction to this line.
Targeted public searches found no matching report; absolute
novelty is not established. See
`sources/errata-byte-swap-source-check.json`. The counterexample
and repair were checked by hand.
