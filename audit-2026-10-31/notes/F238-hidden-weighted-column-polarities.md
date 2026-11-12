# F238 — The column clauses encode the wrong hidden weighted bit

Confirmed in Volume 4B, answer 418, printed 633/file 653; author draft269.
For a bit vector v of length d and weight w=sum(v), the hidden weighted bit
is v_w, with v_0=0. The exercise requires this bit to be 1 in every row and
0 in every column. However, the printed column termination clauses copy
the row polarities and therefore require the column bit to be 1 as well.

In addition, the initial column unit must be c_(j,1,1), not c_(i,1,1).
After making just this unambiguous index repair, the all-ones 3-by-3 matrix
satisfies every printed clause, although its columns all violate the task.
Set each branching-program state on the path of its fixed input to 1;
all other states may be 0. The complete assignment is recorded in
results/bookwise-sat418-fixed-matrices.json and all 102 clauses are checked.

The printed encoding also rejects this valid matrix from answer419(a):

    1000
    0110
    1000

Its column weights are 2,1,1,0, and each selected column bit is zero.
Fixed-input unit propagation gives a conflict in the printed encoding.

Keep the transition clauses. Replace the column termination clauses by

    (c_(j,m+1,1)) and (not c_(j,m+1,m+1))
    (not c_(j,m+1,i+1) or not x_(i,j)),  1 <= i < m.

These allow weight zero, forbid weight m, and test the complement of the
selected bit at every interior weight. The same two fixed matrices are
rejected/accepted as required after the repair. The known 2016 correction
only changes the reference from equation174 to173; it does not fix these
polarities. The copied termination and accompanying index are recorded as
one finding about the column encoding, not as separate reports.

Original Volume 4B typesetting and the September 23, 2015 author draft were
inspected. Current and historical 4B/Fascicle 6 errata and their available
TeX sources contain no matching correction. Focused public searches found
no relevant correction; absolute priority is not claimed. See
sources/bookwise-forcing-source-check.json for the checked ranges.
