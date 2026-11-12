# F213 — The Delayer's unequal-branch moves are reversed

Confirmed: Volume4B, SAT answer227, printed592/file612. The answer defines m
and m' as the minimum Horton–Strahler labels for F restricted by x and by not x,
respectively. It then chooses x=0 when m>m', claiming to guarantee m points,
and chooses x=1 when m<m', claiming to guarantee m' points.

Restriction by a literal sets that literal true. Therefore the first choice must
be x=1 and the second x=0. Swap these two printed values; the equal-label case
and the resulting theorem are unaffected.

A concrete witness is F={x, not x or y, not x or not y}. Its x=true restriction
is {y,not y}, with label m=1; its x=false restriction already contains the empty
clause, with label m'=0. The printed response x=0 ends the game immediately
with zero points, contradicting the promised one point. Choosing x=1 permits
the Delayer to answer '*' on y and obtain that point.

Original PDF inspected (bookwise-delayer-p592.png). The same reversal occurs in
the author's2015 draft, printed228/file236. No matching correction was found
in current/historical4B/F6 errata or the focused public search recorded in
bookwise-resolution-source-check.json. No claim of absolute priority is made.
