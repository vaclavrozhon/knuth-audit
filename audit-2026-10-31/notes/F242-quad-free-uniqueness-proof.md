# F242 — Two local errors in the 10-by-10 uniqueness argument

Confirmed in Volume4B, answer450, printed638/file658; author draft274.
The proposed unit clause is (not x_15), but it must be (x_15). With columns
in decreasing lexicographic order, the first row starts with all its1s.
To rule out a row with at least five1s, the SAT instance must require the
fifth position to be1. The printed negative unit does the opposite.

Indeed the 10-by-10 matrix printed just above, in answer449, satisfies
all the claimed constraints and the negative unit:

    1111000000
    1000110000
    1000001100
    1000000011
    0100101010
    0100000101
    0010100001
    0010010110
    0001100100
    0001011001

A direct fixed check verifies34 ones, at most one common1 in each pair of
rows, decreasing row and column lexicographic order, and x_15=0. Thus the
asserted unsatisfiability cannot hold with the printed sign. No new SAT
search was needed.

The same paragraph also says that exactly four points lie on the four
four-point lines. This should say that exactly four points lie on four
lines. The former statement is false: in the printed matrix the large
columns are1,5,8,10, and their union contains all ten points. The next
paragraph itself uses the correct notion of four-line points.

Both repairs preserve the uniqueness theorem and the subsequent incidence
argument. In fact, after the cited Z(9,10)=32 bound gives degree at least3
on both sides, a line with at least5 points is impossible directly: each
of its points lies on at least two other lines, giving at least10 distinct
other lines although only9 exist. The rest of the printed proof then
identifies the four large lines and the six pairwise intersection points.

Evidence: results/bookwise-sat450-fixed-matrix.json and images of both
original pages. Current/historical 4B and Fascicle6 errata and available
TeX sources contain no matching correction. Focused public searches found
no relevant report; absolute priority is not asserted. Details are in
sources/bookwise-hardness-designs-source-check.json.
