# V3-C0075 — The replacement carry formula is shifted by one position

Confirmed error in the official 5 January 2002 replacement for answer
6.4-32, printed p.734: `all3-prepre`, PDF p.38. This is an errata
finding; the superseded book proof is not counted as a new finding.

Equation (44) defines carries by c_j=max(0,b_j+c_(j+1)-1), with
subscripts read cyclically modulo M. The b_j are nonnegative integers
with sum less than M. The replacement defines

    s_j = sum(k=0..j) (b_(k mod M)-1)
    c_j = max(k>=j) (s_k-s_j).

The differences on the second line start with b_(j+1), not b_j.
For M=3 and b=(2,0,0), the actual solution is c=(1,0,0), while the
replacement produces (0,0,1). In particular its c_0=0 contradicts
max(0,2+c_1-1)=1.

Repair the upper summation limit in the definition of s_j to j-1,
with s_0=0. Then the stated maximum is the maximum nonnegative excess
in a block beginning at j. The negative drift ensures the maximum
is finite and gives the intended recurrence. Alternatively retain
the printed s_j and replace c_j by c_(j+1).

Original errata typography inspected and retained. Later official
layers and limited public searches yielded no correction to this
replacement; see `sources/hashing-errata-review.json`.
