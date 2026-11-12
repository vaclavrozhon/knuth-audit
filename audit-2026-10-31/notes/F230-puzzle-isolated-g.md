# F230 — An isolated G in the printed solution to SAT392(iv)

Confirmed in Volume 4B, answer392(a), printed627/file647, diagram(iv).
Rows and columns are numbered from the top and left, starting at1.

The G in row5, column11 has neighbors A above and to its left, and H below
and to its right. It is therefore an isolated one-cell component, separate
from the other25 G cells. The problem requires all occurrences of each letter
to be rookwise connected: joined through cells sharing a side.

Replace this G by A. The corrected grid preserves all20 givens on printed354
and has exactly one rookwise component for every letter A through J.
The fixed-grid check records both full grids, all givens and all components;
it performs no solution search. The other letters are connected even before
the correction. This is an erroneous extra G, not a misplaced given.

The same cell is G in the September23,2015 author draft, printed263/file271.
Original images of both versions were inspected. Current and historical
4B/Fascicle6 errata and their available TeX sources have no matching repair.
The known2024 correction to Grabarchuk's middle initial on this page is unrelated.
Focused primary-domain searches returned no relevant report; no absolute
priority or physical-copy verification is claimed.

Evidence: check_bookwise_sat392_iv.py; results/bookwise-sat392-iv.json;
images/bookwise-encoding-392iv-detail.png;
images/bookwise-encoding-392iv-question.png;
images/bookwise-fasc6a-392.png; sources/bookwise-graph-order-source-check.json.
