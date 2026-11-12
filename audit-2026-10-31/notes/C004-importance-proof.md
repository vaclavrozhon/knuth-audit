# C004: uncorrected proof steps after the known correction E002

Status: confirmed, low severity, under the original C004 identifier.
This is the worker's confirmation; independent root acceptance is not
claimed. The corrected exercise theorem remains true.

The official July15,2025 erratum E002 changes only the statement on p25:
the upper bound concerns expected absolute error. It does not amend the
proof on p390. The proof still uses a false signed decomposition, bounds
a sample term pointwise, and equates a random squared error with its
variance. These are residual proof errors, separate from the already
published statement correction.

## Exact witnesses within the corrected statement's domain

Take x=(15/16,1/16), y=(1/2,1/2), f=(0,-1), n=4.
Then 2^D=8/sqrt(15), c^4=sqrt(15)/2>1, and m^2=32/sqrt(15).
Thus 2<m<4, whereas the density ratios are8/15 and8, so the
truncated function g is identically zero. On the all-zero sample,
which has positive probability (15/16)^4, the printed first equality
reads1/2=-1/2. Adding an implicit outer expectation still cannot
repair the signed equality: its right-hand expectation is-1.

Take instead x=y=(1/2,1/2), f=(0,1), n=2.
Here D=0, c=2^(1/4)>1, m=sqrt(2), and g=f. The sample mean is
0,1/2,or1. Its squared error is1/4 or0, while its variance is1/8.
An expectation is required before the squared error.

For the claimed pointwise tail bound, change the first witness to
f=(0,1). The all-one sample has positive probability (1/16)^4 and
gives a tail sample term8, whereas the claimed bound is1/2.

All witnesses have positive common support, finite divergence and
second moment, and an integer sample size satisfying n=c^4 2^D.
They do not depend on the separate support issue F008.

## Repair and exact scope

Use the triangle inequality with absolute values on all three terms,
then take expectations. The two truncation terms each contribute at
most ||f|| sqrt(Delta). The centered sample term is bounded by the
square root of its variance, at most ||f||/c. The lower bound follows
from a union bound and Markov's inequality. Every step and boundary
case is proved in notes/sequential-mpr-ex124.md.

The original second-printing PDF p390/file410 and the author's
September11,2019 PS p47/file53 agree. All six official local errata
layers and three TeX sources were checked. E002 addresses p25 only;
no repair of these p390 steps was found.

The primary author paper, arXiv:1511.01437v3, Theorem1.1 and its
complete proof on pp21–22, uses the triangle inequality and expectations
correctly. Publisher metadata confirm the cited2018 journal article.
Only p390/file410 is an error location for C004. No old enumeration
was restarted, and no physical printed-copy inspection, priority or
reward is claimed.

