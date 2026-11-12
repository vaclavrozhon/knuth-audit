# V3-C0058 — The binary-search loop example uses the wrong endpoint

Confirmed local proof defect in volume 3, second edition, first
printing (1998), answer 6.2.1-2(a,c), printed p.705, file p.716.
The loop condition should use `K > K_l`, not `K > K_u`.

Exercise 2 explicitly asks whether the modified binary search works
when the argument K is present in the table. In variants (a) and (c),
step B5 sets the lower endpoint l to the midpoint i instead of i+1.
The answer correctly says these variants can fail, but supports this
with the condition `l=u-1` and `K>K_u`.

When K is present, both variants preserve its inclusion in the current
interval [l,u]. Thus `K>K_u` cannot occur in the case the exercise asks
about. The printed sufficient condition for a loop is true, but is
outside the promised domain and does not justify that answer.

The intended witness is immediate with two keys `K_1<K_2` and argument
`K=K_2`. Initially l=1, u=2, so the midpoint is i=1. Since K>K_1,
the modified assignment l=i leaves the state unchanged. The same
comparison repeats forever. Changing the answer's subscript from u
to l makes its explanation cover this present-key witness.

This corrects the supporting example, not the answer's yes/no result
or the original unmodified Algorithm B. Original pp.423 and 705 were
visually checked and retained as `images/bookwise-p423.png` and
`images/bookwise-p705.png`. The official source screen is
`sources/ordered-search-errata-review.json`; targeted public searches
found no matching correction. No absolute priority is claimed.
