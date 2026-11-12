# F186 — incorrect secondary items in two merged-option examples

Volume 4B, first edition, second printing (November 2022), §7.2.2.1,
answer 371(a,b), printed page 522 / file page 542.

In the encoding of answer 365, a rectangle [a,b) × [c,d) contributes
the secondary items x_ab and y_cd. These items forbid distinct rectangles
from using the same pair of horizontal or vertical boundaries.
Two example strings in answer 371 give the wrong item:

* In part (a), the component covering cells p_30 and p_31 is the
  rectangle [3,4) × [0,2). Its items must be **x_34 y_02**,
  rather than the printed x_34 y_24.
* In part (b), the first component of the third example covers only
  p_02, the rectangle [0,1) × [2,3). Its items must be
  **x_01 y_23**, rather than the printed x_34 y_23.

Both erroneous tokens duplicate another secondary item of the same
merged option while omitting the item for the actual rectangle.
These are local corrections to the examples, separate from the
rotation-cycle error F185 and reflection-filter error F187.

The original was inspected in `images/bookwise-p522.png`. Both tokens
also occur in the author's September 2019 pre-fascicle, printed page
226. No matching correction was found in the relevant historical/current
errata or the public searches recorded in
`sources/bookwise-motley-source-check.json`. This is not a claim of
absolute priority. The actual orbit rectangles are recorded in
`results/bookwise-motley371.json`.
