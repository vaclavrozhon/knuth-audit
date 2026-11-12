# F196 — wrong number of seven-clause totalizer nodes

Volume 4B, answer 7.2.2.2–25, printed page 553 / file page 573.

For the tree encoding with r=2, the answer counts ceil(n/2) nodes
that contribute seven clauses each. This should be floor(n/2)-2.
There are n-2 internal nodes other than the root. Of these, floor(n/2)
cover two leaves and n mod 2 cover three leaves, leaving
`n-2-floor(n/2)-(n mod 2) = floor(n/2)-2`.

For example, n=7 has three two-leaf nodes (4,5,6), one three-leaf node
(3), and one four-leaf node (2). The clause total is
`3*3 + 1*5 + 1*7 + 2 = 23 = 5n-12`. The printed intermediate counts
instead sum to 44. The final 5n-12 total and comparison with Sinz's
encoding are correct.

Original page 553 and author draft page 189 were inspected. Fresh 4B
and Fascicle 6 errata and public searches yielded no matching
correction. No claim of absolute priority.
