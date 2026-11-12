# F202: One clause is missing from the eater boundary conditions

Volume 4B, answer 7.2.2.2–77, printed page 564 (PDF page 584).

Here f,g,h,i are four consecutive cells in column 5. The three stated
conditions are f+g+h≠2, g+h+i≠2 and h+i≠2. Their proposed conversion
to four binary clauses omits **NOT g OR NOT h**.

For (f,g,h,i)=(0,1,1,0), all four printed clauses hold, but both of the
first two sums equal two. Adding the missing clause gives an exactly
equivalent conjunction, as is also immediate by splitting on whether
g or h is one. Direct checking of all sixteen assignments confirms
that this is the sole extra assignment allowed by the printed clauses.

The tuple is compatible with a still life in the indicated gray area:
the 2x2 block in rows 6–7 and columns 5–6 of the 8x8 board has precisely
these column values. Thus the still-life condition alone does not
repair the stated simplification. This example is used only to refute
the local equivalence; it is not claimed to be a four-step eater.

The missing clause is visible in both the 2022 original and the 2015
author draft, printed page 200. Current 4B/Fascicle 6 errata contain no
matching correction. No broad Life search was performed.

Follow-up source inspection: the author's `sat-life-grid-eater.ch`,
retrieved in `sources/bookwise-sat-life.tgz`, repeats the same four-clause
simplification in its explanation and emits precisely those four clauses.
Its loop does not emit the missing NOT g OR NOT h. This supports the
textual diagnosis; no full eater search with that program was rerun.

Evidence: `images/bookwise-life-584.png`, `check_bookwise_sat64_77.py`,
`results/bookwise-sat64-77.json` and the source-check manifest for D236.
