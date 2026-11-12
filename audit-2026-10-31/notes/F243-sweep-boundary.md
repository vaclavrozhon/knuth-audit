# F243 — The sweep recurrence cannot start from negative infinity

Confirmed in Volume4B, answer459, printed639/file659.
Write S(i,j) for the largest sum along a strictly downward/rightward
diagonal in the first i rows and j columns. For binary matrices, the
printed recurrence is

    S(i,j)=max(x_ij+S(i−1,j−1), S(i−1,j), S(i,j−1)).

The book initializes S(i,0)=S(0,j)=−infinity. Consequently every value
computed by this recurrence is −infinity, by induction on i+j. Even
X=[1] should give1 instead. For the binary/nonnegative setting here,
the boundary values must be0. The September23,2015 author draft, page275,
already has precisely that correct initialization; this is a later defect.

The fixed10-by-10 matrix on main292 has51 ones and sweep3 with the repaired
boundary, but −infinity with the printed boundary. Its other claimed
properties, zero applicable tau1/tau2 moves and eight tau3 moves, were also
checked in results/bookwise-sweep-fixed-matrix.json. No matrix search was run.

If one instead defines sweep using only nonempty diagonals of arbitrary
signed matrices, keep the −infinity boundary but add x_ij itself as a
fourth candidate in the maximum. That separate convention does not rescue
the three-term recurrence as printed. The following binary SAT encoding460
uses the intended thresholds and does not inherit this initialization bug.

The original typesetting and the corresponding author draft were inspected.
Relevant current/historical 4B/Fascicle6 errata and their available TeX
sources contain no matching correction. Focused public searches found no
relevant report, without establishing absolute priority. Source details:
sources/bookwise-sweep-source-check.json.
