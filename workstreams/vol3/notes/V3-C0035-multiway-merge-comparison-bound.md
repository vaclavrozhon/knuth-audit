# V3-C0035 — Multiway merging needs a ceiling in its comparison bound

Confirmed, low. Volume 3, second edition, first printing (1998),
answer 5.2.4-1, printed p. 646 / file p. 657, second paragraph.
It claims that floor(lg k) comparisons suffice each time after the
first minimum, when a selection tree is used for k-way merging.
Here lg is the logarithm to base 2. The standard bound is
**ceil(lg k)**; the printed floor is too small when k is not a power
of two.

Consider the complete selection tree with five external nodes. Number
all nodes in heap order, so that the leaves have indices 5,6,7,8,9.
Put the current winning key 0 at leaf8, and put a,b,c,d respectively
at leaves9,5,6,7. Choose distinct positive keys with c<d. Initial
tournament comparisons can establish only

```
0<a, 0<b, c<d, 0<c.
```

After outputting 0, replace it by the next key e>0 from its input
stream. To find the new winner we must determine min(e,a,b,c).
None of these four candidates is known to exceed another. Finding
the minimum of four such keys requires three comparisons in the
worst case, while floor(lg 5)=2. The three comparisons are precisely
the updates along the path from leaf8 to the root. The monotonicity
of each input stream only gives e>0 and supplies no missing comparison
among the four remaining candidates.

The same obstruction occurs at a deepest leaf of a balanced selection
tree for any non-power-of-two k. This is an error in an exact bound,
not in the merging algorithm or its O(log k) update complexity.
The later explanation of replacement selection on pp.252–254 correctly
describes updating the whole path and uses an approximate logarithmic
count rather than this floor bound.

Original p.646 was inspected and saved in `images/bookwise-p646.png`.
All five author errata layers were checked against the fresh matched
archives, including corresponding first-edition answer context:
`sources/merging-errata-review.json` and the volume3 fresh manifest.
No matching correction was found. Targeted public searches combining
Knuth, 646, 5.2.4, merging, floor/ceiling and errata found no matching
report; absolute priority and later physical printings remain unverified.
No computation was needed.
