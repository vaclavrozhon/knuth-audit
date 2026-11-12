# F205: Update the size exponent when doubling a BIMP block

Volume 4B, answer 7.2.2.2–134, printed 574 / PDF 594.

The allocator stores ADDR (block address), BSIZE (used entries), CAP
(capacity), and K (the base-two capacity exponent), with CAP = 2^K.
The resizing paragraph assigns k = K and CAP = 2^(k+1), but never
updates the stored K. Add **K ← k+1** after saving the old value in k,
or when completing either resizing branch.

Starting with CAP=4 and K=2, the first resize produces CAP=8 but K=2.
When eight entries have been filled, the next resize again uses k=2:
it looks for the buddy at ADDR xor 4 and requests capacity eight,
instead of the required sixteen. The old invariant already failed at
the first resize, and the ninth entry cannot fit in that requested block.
This is an omitted stored-field update, not a choice of allocator policy.

The page image confirms the omission. The author’s September 23, 2015
draft, printed 210 / PDF 218, has the same text. In contrast, the current
official SAT11 source ends `resize` by setting both `alloc=s+s` and
`k=k+1` (source line 1261). Thus the author’s implementation already
contains the required operation. No corresponding correction was found
in the inspected current/historical 4B and Fascicle 6 errata.

Evidence: `images/bookwise-buddy-p574.png`, `sources/fasc6a.pdf`,
`sources/bookwise-sat11.w` and its provenance manifest,
`check_bookwise_sat134_x2.py`, `results/bookwise-sat134-x2.json`.
The small check only evaluates the two successive capacity requests;
it is not an implementation-wide allocator test.
