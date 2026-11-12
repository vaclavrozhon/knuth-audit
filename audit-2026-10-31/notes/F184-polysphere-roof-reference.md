# F184 — the wrong roof in answer 356(b)

Volume 4B, first edition, second printing (November 2022), §7.2.2.1,
answer 356(b), printed page 517 / file page 537. The final sentence of
the bracketed paragraph says that {i,j,n,o,p} packs S_(2×7) and S_(7×2).
Here R denotes an ordinary roof and S a stretched roof, as defined
in answer 356(a). The intended pair is **R_(2×7) and S_(2×7)**.

Piece i consists of four equally spaced collinear spheres. It cannot
fit inside S_(7×2), even by itself. To see this directly, use the three
coordinates of answer 356(a). A cell (A,B,C) of that roof has the form

```
(A,B,C) = (x+6−y, y+k, y),
0 ≤ k < 2, 0 ≤ x < 2−k, 0 ≤ y < 7−k.
```

Consequently A+C belongs to {6,7} and B−C belongs to {0,1}.
Along four equally spaced collinear cells both integer linear forms
must be constant. Their step (a,b,c) would therefore satisfy
a+c = b−c = 0, hence be a multiple of (−1,1,1).
But a nearest-neighbor step in the face-centered cubic lattice is
either a signed coordinate unit vector or a difference of two such
vectors. None is a nonzero multiple of (−1,1,1). Thus i cannot fit.
This also explains the contradiction with the table on the same page,
which reports no all-planar packing of S_(7×2).

For the corrected pair, explicit packings are given below; each triple
is a cell coordinate in the book's convention. Each row is a single
rigid piece, and the five rows partition the relevant 20-cell roof.

| Piece | R_(2×7) | S_(2×7) |
|---|---|---|
| i | 310 410 510 610 | 400 500 600 700 |
| j | 010 110 210 211 | 100 200 300 310 |
| n | 201 301 311 411 | 211 311 410 510 |
| o | 001 011 101 111 | 011 110 111 210 |
| p | 401 501 511 601 | 411 511 610 611 |

These witnesses were obtained by a small search that stops at its
first solution, in `check_bookwise_polysphere_cases.py`; results are in
`results/bookwise-polysphere-cases.json`. No global puzzle census was run.

The original typesetting was inspected in `images/bookwise-p517.png`.
The author's September 2019 [pre-fascicle](https://www.ioccc.org/2019/ciura/fasc5c.pdf),
printed page 221, also has the incorrect pair. The historical and current
Volume 4B/Fascicle 5 errata, freshly retrieved on 11 November 2026, do not
correct this sentence. The known correction of “planar places” on the
corresponding Fascicle 5 page 325 is separate. Public searches found no
matching report, without establishing absolute priority; see
`sources/bookwise-polysphere-source-check.json`.
