# F245 — The displayed numbering reverses the neighboring inequalities

Confirmed in Volume4B, answer472, printed641/file661; author draft277.
The displayed4-by-4 ranks are

    16 15  1  2
     4 14 13  3
     5  6 12 11
     9  7  8 10.

The text says that a vertex precedes both its right and lower neighbors
exactly when its coordinate residues belong to
{(0,0),(0,1),(1,1),(1,2),(2,2),(2,3),(3,3),(3,0)} modulo4.
For example (1,1) is in that set, but its rank16 exceeds both15 and4.
In fact all24 available neighbor comparisons are reversed in the figure.

Either reverse the two displayed inequality signs or replace every rank r
in the figure by17−r. The latter gives

     1  2 16 15
    13  3  4 14
    12 11  5  6
     8 10  9  7.

Every stated comparison now holds. Both rankings nevertheless induce the
nine intended even-odd domino flips: at the largest vertex of each square,
the smaller neighboring rank lies in the required matching orientation.
Thus this is a mismatch between the formula and its numerical illustration,
not a failure of the requested endomorphism construction. The fixed24-edge
and nine-square checks are in results/bookwise-sat472-fixed-numbering.json.

The original typesetting and the corresponding author draft were inspected.
Relevant current/historical 4B/Fascicle6 errata and their available TeX
sources contain no matching correction. Focused public searches found no
relevant report, without establishing absolute priority. Source details:
sources/bookwise-sweep-source-check.json.
