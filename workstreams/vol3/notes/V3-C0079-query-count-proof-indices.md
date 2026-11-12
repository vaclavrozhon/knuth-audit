# V3-C0079 — The query-count proof changes dimension in its exceptional case

Confirmed in volume 3, second edition, first printing (1998), answer
6.5-8(a,b), printed p.745 (file p.756).

The function f_t(s,m) is the minimum number of basic queries with t
specified bits that meet a set of s binary records of length m. Thus
its size argument satisfies 0<=s<=2^m. The proof abbreviates
g_t(s)=f_t(s,m-1) and h_t(s)=f_t(s,m-2).

In the exceptional case s_0=2k+1, s_1=2k-1, the final comparison uses
h_t(2k+1)+2h_(t-1)(2k) and then h_t(2k)+2h_(t-1)(2k). These are at
the wrong dimension. For example m=4, s_0=7, s_1=5 is a permitted
case, but it requires h_t(7)=f_t(7,2), although only four distinct
2-bit records exist. The intended balanced split must be compared
using g, not h. In particular the desired final expression is
g_t(2k)+2g_(t-1)(2k). The printed h expressions do not complete that
induction even when their arguments happen to be in range.

There is a second size-index typo in (b). For S={0,...,s-1}, split
by the last bit, S_0 has ceil(s/2) elements. The answer says
ceil(s_0/2), where s_0 already denotes the size of S_0. For s=4,
S_0={0,1} has size 2, not ceil(2/2)=1.

The claimed minimum and the final subcube generating function are
not refuted. The finding concerns the displayed proof: keep the
exceptional comparison at dimension m-1 and remove the subscript
zero from the size in (b).

Original p.745 and enlarged crop inspected. The 1997 first-edition
replacement contains the same two defects; no subsequent correction
was located in the official layers or limited public searches. See
`sources/secondary-keys-errata-review.json`.
