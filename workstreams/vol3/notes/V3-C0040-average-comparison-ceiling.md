# V3-C0040 — A worst-case ceiling is used as an average lower bound

Confirmed, low. Volume 3, second edition, first printing (1998),
exercise 5.3.1-23, printed p.196 / file p.207.

The introductory sentence says the average number of comparisons made
by any sorting method must be at least `ceil(lg(n!))`. The ceiling is
valid for the worst-case integer number of comparisons, not for the
average over equally likely permutations.

The book's own three-element comparison tree (Fig.34, p.181) has two
leaves at depth 2 and four at depth 3. Its mean is

```
(2*2 + 4*3)/6 = 8/3 < 3 = ceil(lg(3!)).
```

The value 16 for its external path length is also printed in the table
on p.193. The correct general elementary average lower bound is
`lg(n!)`; the stronger bound derived in (34) is also valid. Removing
the ceiling repairs this sentence. The intended distinction between
comparison sorting and distribution sorting, and the answer to the
exercise, are unaffected.

Original pages 181, 193 and 196 were inspected. The erroneous page is
saved as `images/bookwise-p196.png`. All five errata layers in
`sources/minimum-sorting-errata-review.json` and targeted public searches
were screened without a matching correction. No claim of absolute
priority is made; later physical printings were not inspected.
