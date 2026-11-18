# F271 — Wrong cell in the overlap example

**Confirmed; low severity.** Volume 4B, first edition, second printing (2022), answer 7.2.2.1–370, printed p. 521 / PDF page 541, the example for case (v).

The two rectangles given there overlap in **p12 and p22**, not p22 and p23. Here `pij` denotes the unit cell in row i and column j, as defined in answer 360. The four-tuple `(a,b,c,d)` denotes the half-open rectangle `[a,b) × [c,d)`.

For the printed rectangle and its half-turn image in a 4 by 5 board, the cell sets are

```text
R  = (1,3,1,3): {p11, p12, p21, p22}
R' = (1,3,2,4): {p12, p13, p22, p23}
R intersect R' = {p12, p22}.
```

In particular, p23 is outside R. Replacing the printed pair `p22 and p23` by `p12 and p22` repairs this statement. The overlap rejection itself remains valid. The example also satisfies the earlier rejection case (ii); this pre-existing observation is not counted as an additional finding or as a defect in the algorithm.

Both the supplied original page (`audit-2026-10-31/images/bookwise-p521.png`) and the September 11, 2019 pre-fascicle 5C, printed p. 225 / PDF page 231 (`integration/2026-11-17-focused-4b/sources/fasc5c-p225-overlap.png`), were visually inspected and show the same indices. This is not an OCR error. It is separate from the two incorrect interval-item examples in answer 371 recorded as F186.

The six current/historical errata texts and three current TeX sources were searched by location, answer number and relevant cell names; the neighboring Fascicle 5 corrections were read. No matching correction was found. Six focused public queries did not locate a prior report. Absolute priority and the state of every later printing are not established. Source hashes and the exact search queries are in `results/focused-motley370-sources.json`.
