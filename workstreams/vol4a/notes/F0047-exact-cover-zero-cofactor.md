# V4A-F0047: A zero cofactor is subtracted when none exists

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), answer7.1.4-211, printed663 / file680. Original:
`images/bookwise-p663.png`.

The answer asserts b[k] >= q[k]-1 >= z[k] for an exact-cover matrix
without zero rows. Here q[k] counts distinct residual Boolean
functions after the first k row choices, b[k] counts BDD branch
nodes on the next variable, and z[k] counts ZDD branch nodes there.
The second inequality assumes that the zero function occurs among
those residuals. That need not happen.

Take six distinct nonzero rows, listed by the columns they cover:

    r1={a,b}, r2={c,d}, r3={a}, r4={b}, r5={c}, r6={d}.

The exact covers are {1,2}, {1,5,6}, {2,3,4}, and {3,4,5,6}.
After testing x1, the two residual families are

    {{2,3,4},{3,4,5,6}} and {{2},{5,6}}.

Both are nonempty, distinct, and support row2. Thus q[1]=2 and
z[1]=2, contradicting q[1]-1 >= z[1]. This failure is at an internal
level, with neither empty rows nor duplicate rows. The printed
inequality also fails at the root of every nonempty instance.

Let q'[k] count only nonzero residuals, as in main250. Then the
correct comparison is b[k] = q'[k] >= z[k]. A nonzero exact-cover
residual cannot be independent of a nonzero remaining row: toggling
that row while fixing every other choice changes a covered column
sum. This repairs the proof of Z(f) <= B(f); its conclusion remains
valid under the stated nonzero-row assumption.

The original typography, relevant 4A/Fascicle1 errata and targeted
public searches were checked without locating this correction.
See `sources/zdd-algebra-covering-source-check.json`. Absolute
novelty is not established. No mathematical code was used.
