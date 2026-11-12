# F244 — The induction advances through m rows, not n columns

Confirmed in Volume4B, answer463, printed640/file660; author draft276.
The matrix is m-by-n. The proof has established the form of rows1 through i
and then says that if i<n it can increase i to i+1. The condition must be
i<m, because the induction is over rows. As printed it stops too early
when m>n or goes beyond the available rows when m<n. All column bounds
using n in the same sentence are correct, and the resulting extremal
formula k(m+n−k) is unchanged.

The original typesetting and the corresponding author draft were inspected.
Relevant current/historical 4B/Fascicle6 errata and their available TeX
sources contain no matching correction. Focused public searches found no
relevant report, without establishing absolute priority. Source details:
sources/bookwise-sweep-source-check.json.
