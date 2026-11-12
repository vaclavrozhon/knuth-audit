# V4A-F0013: sorted threshold outputs are listed in reverse order

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), answer 7.1.2-38(a), printed page 567 / file page 584.
Original: `images/bookwise-p567.png`; question: `images/file144.png`.

The exercise on page 127 asks about a network that sorts its n Boolean
inputs in ascending order. The answer says that, from top to bottom,
output f_k is S_{>=k}, the indicator that at least k inputs are 1.

These thresholds decrease as k increases, so their stated order is
descending. For example, sorting the input (1,0) gives (0,1), while
(S_{>=1},S_{>=2}) is (1,0). The network convention in Volume 3,
Section 5.3.4, page 221, puts the smaller output on the upper line.

Replace S_{>=k} by S_{>=n+1-k}, or replace “top to bottom” by
“bottom to top.” The set of output functions and the subsequent cost
and depth bounds are unchanged.

The current and historical Volume 4A errata and both Fascicle 0 layers
contain no matching correction. The 2025 change to the wording of
exercise 38(b) does not address this direction error. A targeted public
search located no matching report; absolute novelty is not established.
See `sources/multiple-output-source-check.json`. No computation was
needed.
