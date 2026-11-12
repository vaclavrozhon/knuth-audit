# V2-C0067: dismissed after checking the printed counting convention

Publication review, November 12, 2026. The proposed empty-prefix
counterexample is invalid for the actual text of exercise 3.5–39,
Volume 2, third edition, first printing, p. 183.

The original image clearly defines `nu_n(u)` as the number of
**nonnegative integers `j <= n`** with `U_j < u`. The report and the
earlier verification note silently replaced this by `j < n`. Thus
`nu_0` is not identically zero: it counts the first point.

For the alleged counterexample `N=1`, choose `n=0` and
`u=(1+U_0)/2`. Because `0 <= U_0 < 1`, this is an allowed value
with `U_0 < u < 1`. Consequently `nu_0(u)=1`, and the printed strict
inequality is `1 > c log(1)=0`, which holds for every positive `c`.
The proposed counterexample therefore fails for every allowed sequence.

The standard discrepancy convention usually counts `j<n`, but it cannot
be substituted for an explicit definition when accusing the text of a
boundary error. This dismissal concerns C0067; it does not claim to
audit every consequence of the book's shifted convention.

The archived report, note and JSON calculation are superseded for this
card. Their numerical check only encoded an empty count and did not
verify its correspondence to the source. The ledger and UI status are
changed to dismissed, and the page no longer receives a finding marker
from C0067. The history is retained rather than deleted.

All four relevant errata layers were searched again; the 2016 change
only changes the exercise rating. Public searches for TAOCP/Knuth,
exercise 3.5–39, discrepancy, empty prefix and the quoted counting
definition found no reason to override the original typesetting.
