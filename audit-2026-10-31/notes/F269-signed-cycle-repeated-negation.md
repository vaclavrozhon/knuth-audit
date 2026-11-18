# F269 — A repeated negated literal in exercise 494(iii)

**Location:** Volume 4B, first edition, second printing (2022), exercise
7.2.2.2–494(iii), p. 365 (PDF page 385). The September 2015 Fascicle 6A
draft has the same expression on p. 181 (PDF page 189).

Write `!i` for the negated literal corresponding to variable `i`. A signed
permutation must send opposite literals to opposite literals:
`sigma(!i) = !sigma(i)`. A cycle `(a b c)` sends `a` to `b`, `b` to `c`,
and `c` to `a`.

The printed third case is

```
(i !j !k)(!i !j k).
```

The second cycle should be the complement of the first. Instead, `!j`
appears twice and `j` is absent. These are not disjoint cycles of the
required signed permutation. Interpreting them as a product of overlapping
cycles does not help: the product fixes `j` but moves `!j`, violating the
opposite-literal condition.

Remove the bar from `j` in the second cycle:

```
(i !j !k)(!i j k).
```

This gives the intended order-three signed permutation. It is also
consistent with answer 494(iii), whose restrictions are
`(!x_i OR !x_j) AND (!x_j OR x_k)`. The correction is local to the
question's notation; it does not change those answer clauses.

The original page, an enlarged rendering of its cycle line, and the draft
page were inspected. The six current/historical errata lists and three
author TeX errata files contain no matching correction. The July 17, 2018
Fascicle 6 erratum for answer 494 changes its reference to exercise 475(d),
not this cycle; that reference correction is already present in the book.
The nearby February 16, 2024 book erratum concerns the attribution in 495.
Six focused public searches found no matching prior report. Absolute
priority and later physical printings are not established.

Source hashes and the exact errata blocks and search queries are recorded
in `results/focused-signed494-sources.json`. No solver, census, or new
mathematical program was needed.
