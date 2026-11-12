# The unary example specifies the wrong number of leaves

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–37, unary example beginning “if t=1”, printed 791.

A forest with n_0 leaves and m unary nodes is a sequence of n_0 nonempty chains. Its count, also obtained from the formula at the top of the page, is binomial(n_0+m-1,m).

Consequently the printed choice n_0=m+r+1 gives binomial(2m+r,m), not the stated binomial(m+r,r). For m=2,r=1 there are ten forests, not three: the two 1s can occupy any two of the first five positions of a six-symbol degree sequence ending in 0.

Set n_0=r+1 instead. Then C(n)=binomial(m+r,r), and the subsequent sum K-Z=binomial(m+r,r+1) is consistent with the preceding subforest identity. In particular it exhibits the claimed linear-in-m overhead for fixed r.

Original typesetting inspected. Historical/current Volume 4A and refreshed Fascicle 4 errata and targeted public queries yielded no matching correction. See `../sources/tree-gray-generators-source-check.json`; absolute novelty is not established.
