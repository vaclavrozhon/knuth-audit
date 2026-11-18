# F242 — Three local errors in the 10-by-10 uniqueness argument

Confirmed in Volume4B, answer450, printed638/file658; author draft274.
The proposed unit clause is (not x_15), but it must be (x_15). With columns
in decreasing lexicographic order, the first row starts with all its1s.
To rule out a row with at least five1s, the SAT instance must require the
fifth position to be1. The printed negative unit does the opposite.

Indeed the 10-by-10 matrix printed just above, in answer449, satisfies
all the claimed constraints and the negative unit:

    1111000000
    1000110000
    1000001100
    1000000011
    0100101010
    0100000101
    0010100001
    0010010110
    0001100100
    0001011001

A direct fixed check verifies34 ones, at most one common1 in each pair of
rows, decreasing row and column lexicographic order, and x_15=0. Thus the
asserted unsatisfiability cannot hold with the printed sign. No new SAT
search was needed.

The same paragraph also says that exactly four points lie on the four
four-point lines. This should say that exactly four points lie on four
lines. The former statement is false: in the printed matrix the large
columns are1,5,8,10, and their union contains all ten points. The next
paragraph itself uses the correct notion of four-line points.

These two repairs preserve the uniqueness theorem and the subsequent incidence
argument. In fact, after the cited Z(9,10)=32 bound gives degree at least3
on both sides, a line with at least5 points is impossible directly: each
of its points lies on at least two other lines, giving at least10 distinct
other lines although only9 exist. The rest of the printed proof then
identifies the four large lines and the six pairwise intersection points.

Evidence: results/bookwise-sat450-fixed-matrix.json and images of both
original pages. Current/historical 4B and Fascicle6 errata and available
TeX sources contain no matching correction. Focused public searches found
no relevant report; absolute priority is not asserted. Details are in
sources/bookwise-hardness-designs-source-check.json.

## Additional line-label error found on November 17, 2026

The final paragraph contains another local error, grouped into this existing
card. A **quad** means two distinct lines containing the same two distinct
points; equivalently, their incidence matrix has four ones at the corners
of a rectangle. The construction is required to be quad-free.

The four named points are `a,b,c,d`. The other six point names are
`ab,ac,ad,bc,bd,cd`, where, for example, `ad` names the intersection point
of the two large lines `A` and `D`; it does not denote a product.
The answer prints

```text
A  = {a, ab, ac, ad},
C  = {c, ac, bc, cd},
AC = {a, c, ad}.
```

Consequently the lines `A` and `AC` both contain the points `a` and `ad`.
This is a quad, directly contradicting the required property.

The last point of `AC` must instead be `bd`:

```text
AC = {a, c, bd}.
```

Indeed, a line already containing `a` and `c` cannot contain any of
`ab,ac,ad,bc,cd`, since that would share two points with `A` or `C`.
Of the six intersection points, only `bd` remains. The analogous rule
for the six small lines is

```text
AB = {a,b,cd},  AC = {a,c,bd},  AD = {a,d,bc},
BC = {b,c,ad},  BD = {b,d,ac},  CD = {c,d,ab}.
```

These lines and the four large lines have the claimed 34 incidences and
no quad. Thus this additional correction also preserves the intended
uniqueness conclusion.

The original second-printing page 638 and the 2015 author-draft page 274
both print `ad`; their images were inspected again. Current and historical
Volume 4B and Fascicle 6 errata contain no corresponding correction.
The nearby Fascicle 6 change updates the result at the end of answer 448.
Focused public searches located no matching report, without establishing
absolute priority. See
[the additional source check](../results/focused-quad450-sources.json),
[the original page](../../integration/2026-11-17-focused-4b/sources/vol4b-p638.png),
and [the author draft](../../integration/2026-11-17-focused-4b/sources/fasc6a-answer450.png).
