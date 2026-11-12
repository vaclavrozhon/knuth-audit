# F195 — missing factor two in the kakuro block count

Volume 4B, first edition, second printing (November 2022), answer
7.2.2.1–434, printed page 544 / file page 564.

After the result of 38 blocks for the 9 by 9 diagram, the answer gives
the asymptotic maximum as `n^2/3 - O(n)`. The leading term should be
`2 n^2/3`. A block is a maximal horizontal or vertical run of blank
cells, as defined in exercise 430; both directions count.

The answer's own periodic construction makes cells with
`(i+j) mod 3 = 0` black, apart from boundary changes. In each interior
row this creates one horizontal two-cell block per three positions;
the same holds for vertical blocks in each column. Thus it has
`n^2/3 + O(n)` blocks of each orientation, or `2 n^2/3 + O(n)` in total.
Changes confined to a boundary strip affect only O(n) blocks and
cannot account for the missing quadratic term.

The matching leading upper bound is elementary: in a row each block
requires at least two blank cells and a distinct preceding black cell,
so at most floor(n/3) horizontal blocks fit. Count columns as well.
This confirms the factor being counted, without reproducing the
9 by 9 census or a new detailed boundary construction.

The original typesetting and the author's September 2019 draft,
printed page 248, both have the coefficient 1/3. Current and historical
4B / Fascicle 5 errata and targeted public searches yielded no matching
correction. No absolute priority is claimed.
