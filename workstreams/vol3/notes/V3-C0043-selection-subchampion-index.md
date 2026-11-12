# V3-C0043 — The maximum includes two unexamined subchampions

Confirmed in volume 3, second edition, first printing (1998), answer
5.3.3-21, printed p.663, file p.674, last two lines.

In Step j, the algorithm compares b to a_(k-t+j+1), then compares the
winner to a_(k-t+j+2), and so on through a_(k-1). The maximum obtained
must therefore be

```
c = max(b, a_(k-t+j+1), ..., a_(k-1)).
```

The printed formula starts instead at a_(k-t+j-1). It includes two
subchampions from the subtree A' that has not participated in these
comparisons. Change the minus sign immediately before the final 1 to
a plus sign.

For a concrete legal tournament, take k=t=3, j=1. Tree A has champion
a=8 and subchampions a_0=7, a_1=6, a_2=4. They can arise from sibling
groups {7}, {6,3}, and {4,2,1,0}. Let tree B have leaves {5,-1}, so its
champion is b=5. The stated comparison is only 5:4, and obtains c=5.
The printed formula instead gives max(5,7,6,4)=7.

This is a local definition/index error in the printed algorithm. The
example does not show an incorrect selected element: the first two
cases make the same structural update, although they have different
comparison accounting. The corrected index matches the stated
comparisons and intended cost argument.

The original was visually checked and saved as `images/bookwise-p663.png`.
The official errata screen is `sources/minimum-selection-errata-review.json`.
The first-edition replacement answer dated 25 August 1996 repeats the
same index; no correction of it was found in the five applicable layers
or targeted public searches. Absence from those sources does not establish
absolute priority.
