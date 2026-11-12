# V2-C0257: incorrect indices and orders in the improvable-tensor construction

Confirmed construction errors, medium impact. Third edition, first printing,
answer 4.6.4-67, printed 716–717 (file 728–729), paired with the question
on printed 523. Original typesetting inspected on 10 November 2026.
The stated border-rank conclusions are not refuted; the formulas used to
establish them need the following repairs.

A tensor realization of length r consists of matrices A, B, C with
t_ijk = sum_l a_il b_jl c_kl. In part (c), D is the diagonal matrix of
nonzero scalars d_l; the construction assumes A D B^T = 0. The new
q by q output slice, where q=r-m-n, is supposed to be the identity
matrix, representing the dot product T(1,q,1).

1. Part (d) gives a length mn+1 realization of T(m,1,n), with columns
   numbered 1 through mn+1. For l<=mn it prints

       a_il = [floor(l/n)=i-1],  b_jl = [l mod n=j],
       b_(ij),l = [l=(i-1)n+j].

   Here [S] is 1 when statement S is true, and 0 otherwise. The first
   two expressions use incompatible zero-based and one-based indices;
   the third expression must define C, not B. For m=n=2, the second
   row of B is zero in the first four columns, since l mod 2 never
   equals 2. The fifth column of C is zero. Consequently all tensor
   coefficients involving the second B variable vanish, although the
   required products x_i*y_2 do not vanish. The purported improvability
   condition fails as well: those entries of A B^T equal -1.

   Replace these three expressions by

       a_il = [floor((l-1)/n)=i-1],
       b_jl = [(l-1) mod n=j-1],
       c_(ij),l = [l=(i-1)n+j].

   Each pair (i,j) then occurs in exactly one of the first mn columns.
   The unchanged final column (a_ir=1,b_jr=-1,c_(ij),r=0) cancels its
   contribution to A B^T without changing the represented tensor.

2. Parts (c) and (g) print the extra slice as a power of u times
   [i>m][j>n]. This is an all-ones block, whereas their constructed
   matrices give an identity block. Replace that factor by
   [i-m=j-n>0]. Indeed the displayed V,W satisfy V D W^T=D2, and the
   subsequent division by d_(m+i) normalizes the block to I_q.
   The distinction matters for q>1: the two blocks have ranks 1 and q.

3. Part (g) starts with an approximate realization
   sum_l a_il b_jl c_kl = u^d t_ijk + O(u^(d+1)). It multiplies the
   old C entries by u^(d+e+2). Therefore the old tensor block becomes

       u^(2d+e+2) t_ijk + O(u^(2d+e+3)),

   not the printed u^(d+e+2) t_ijk + O(u^(d+e+3)). The two new rows
   contribute u^(d+1) each and f(u)g(u)/p has leading term u^e;
   their extra slice likewise starts at u^(2d+e+2), with the identity
   factor from point 2. Both claimed leading orders and the remainder
   order need the additional d. This discrepancy already occurs with
   constant nonzero d_l, so it does not depend on a choice of how to
   clear variable denominators. No claim about an optimal approximation
   degree is made here.

There are two nearby editorial errors in the same answer. Part (a)
restricts the flattening matrix to the mn **columns**, not rows, with
k=k'=1. In part (c), the undefined U in U D V^T must be W. The
matrices W=(W1,I,0), V=(0,I,V3) immediately give W D V^T=D2.

All2-prepre, all2-pre, all2, err2, current err2.textxt and the older
second-edition list were checked. The known question-67 parenthesis
correction and the historical exponent update at the end of answer 67
do not address these errors. Targeted public searches for the exercise,
improvable tensors and Knuth errata found no matching report. Absolute
priority and later physical printings remain unverified. No report sent.
