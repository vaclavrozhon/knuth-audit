# F187 — reflection filter rejects a rectangle's self-image

Volume 4B, first edition, second printing (November 2022), §7.2.2.1,
answer 371(b), printed page 522 / file page 542.

A rectangle is represented by q=(a,b,c,d), meaning [a,b) × [c,d).
Reflection in the main diagonal gives d(q)=(c,d,a,b); reflection in
the other diagonal gives e(q)=(n−d,n−c,n−b,n−a).
Part (b) correctly observes that an orbit can contain two rectangles
when one of these reflections fixes q. Its rejection rules nevertheless
exclude those cases by treating a self-image as an overlapping distinct
rectangle.

Take the answer's own two-rectangle example, n=4 and q=(0,1,3,4).
Its distinct images are (0,1,3,4) and (3,4,0,1): the single cells p_03
and p_30. They are disjoint and have distinct horizontal and vertical
intervals. All preceding boundary and lexicographic tests pass, and
the centered-square acceptance test does not apply. The instruction
to reject when b > n−d rejects this option, since 1 > 0. But e(q)=q;
there is no second rectangle intersecting it.

Likewise, the test b > c wrongly rejects rectangles fixed by d.
Indeed every room at the top-left corner of a diagonally symmetric
dissection must be a square fixed by d (otherwise its reflected room
would overlap it). The literal test rejects each such proper corner
square, preventing the algorithm from generating a nontrivial dissection.

After the preceding lexicographic and centered-square steps, correct
these two overlap conditions to

```
(b > c   and q != d(q))
or
(b > n−d and q != e(q)).
```

The separate motley tests a+b=n and c+d=n remain. More generally,
one can test pairwise overlap and interval compatibility among the
**distinct** rectangles of the reflection orbit before merging.
No claim is made that the printed census numbers were generated with
the erroneous filter; they were not independently recomputed.

The original was inspected in `images/bookwise-p522.png`. The same
filter and contradictory example occur in the author's September 2019
pre-fascicle, printed page 226. No matching erratum or public report was
found in the sources recorded in `sources/bookwise-motley-source-check.json`;
absence there does not prove absolute priority. The two-cell example
and its preceding tests are checked in `check_bookwise_motley371.py`,
with output in `results/bookwise-motley371.json`.
