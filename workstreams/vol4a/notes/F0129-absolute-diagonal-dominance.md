# Absolute values must be inside the off-diagonal sum

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–104(a), parenthetical on printed 806.

A positive semidefinite real symmetric matrix has x^T*C*x>=0 for every real vector x, equivalently all its eigenvalues are nonnegative. The parenthetical claims this follows from c_mm>=|sum_{j!=m} c_mj| for every row m.

Consider

    C = [ 1  2 -2 ]
        [ 2  1 -2 ]
        [-2 -2  4 ].

The absolute off-diagonal row sums are 0,0,4, so the printed condition holds. But for x=(1,-1,0), C*x=-x. Therefore C has the negative eigenvalue -1, and x^T*C*x=-2.

The intended sufficient condition is c_mm>=sum_{j!=m}|c_mj|. This is the usual symmetric diagonal-dominance bound with nonnegative diagonal. For graph Laplacians all off-diagonal entries are nonpositive, so the two expressions coincide and the surrounding proof of nonnegative graph aspects remains valid.

Original typesetting inspected. No matching correction was found in the historical/current Volume 4A errata, refreshed Fascicle 4 errata or targeted public searches; see `../sources/tree-spectral-source-check.json`. Absolute novelty is not established.
