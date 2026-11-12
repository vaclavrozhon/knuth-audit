# F246 — A simplified gate clause uses column 1 instead of column t

Confirmed in Volume 4B, answer 477, printed 642/file 662.
Here x_it denotes the value of gate i in truth-table column t, and s_i12
selects input variables 1 and 2 as that gate's operands. For every
0 < t < 2^(n−2), both operands are zero. A normal gate must therefore give
x_it = 0. The example should be

    (not s_i12 or not x_it),

but prints x_i1 in place of x_it. For n = 4, for example, columns 1, 2,
and 3 have the same zero first two input bits; repeating the condition on
column 1 says nothing about columns 2 and 3. The local assignment
s_i12 = 1, x_i1 = 0, x_i2 = 1 satisfies the printed simplified clause and
violates the required zero output at column 2.

The general five-literal encoding immediately above is correct and would
simplify to the intended clause. This finding concerns the explicit
simplification example, not a defect in that general encoding.

Original Volume 4B typesetting and the September 23, 2015 author draft,
answer page 278, both contain this defect. Relevant current and historical
4B/Fascicle 6 errata were checked, including available TeX sources. Focused
public searches found no matching report; this does not establish absolute
priority. See sources/bookwise-synthesis-source-check.json.
