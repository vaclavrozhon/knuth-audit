# Wrong coefficient in the upper shadow of an initial segment

Volume 4A, first edition, first printing (2011), answer 7.2.1.3–74,
printed page 738, file page 755.

P_Nt is the first N t-element combinations in the book's decreasing
index-list lexicographic order. Its upper shadow consists of all
(t+1)-element sets containing one of those combinations, within the
n-element universe. Let n_t be the leading upper index of the
degree-t combinatorial representation of N, equation (57).

The answer gives `(n+1-n_t) N + choose(n_t+1,t+1)` for that shadow's
size. The coefficient must be **n-1-n_t**.

For example, take n=4, t=2 and N=1. Then P_Nt consists of {0,1},
n_t=2, and its upper shadow is {{0,1,2},{0,1,3}}, of size 2.
The printed expression gives `(4+1-2)+choose(3,3)=4`.

For n_t<n, the correct count follows by splitting the upper shadow
according to its maximum element. Every (t+1)-set within
{0,...,n_t} occurs, giving choose(n_t+1,t+1) sets. For each maximum
from n_t+1 through n-1, the remaining t-set can be any member of
P_Nt, giving n-1-n_t copies of N. When N=choose(n,t), the same
formula reduces to choose(n,t+1) by Pascal's identity.

Thus the printed formula overcounts by 2N. This is separate from the
known September 2025 correction adding parentheses around the symbol
10 in the preceding line.

Original formula inspected at full resolution. Source screening:
`../sources/shadows-source-check.json`. No matching public correction
was found; absolute novelty is not established.
