# Volume 4A: remaining partition estimates and tree generation

Publication review, 2026-11-12. All sixteen findings below are retained.
The source is the January 2011 first printing, checked in the original
typesetting on pp. 427, 450, 472, 776–779, 784–785, 787–793, and 795.
Notation and fuller derivations remain in the individual finding notes.

| Finding | Independent reason and scope |
| --- | --- |
| V4A-F0105 | Answer 7.2.1.5-56(c), p. 776: the printed upper bound is negative, although its middle expression is asserted positive. Parts (a) and (b) give 0 < (-sigma)^(n+1) g^(n+1)(sigma) < n! (1-beta/alpha). Restore the missing power and the sign of this bound. |
| V4A-F0106 | Answer 7.2.1.5-61, p. 777: the saddle parameter (n+1)/(n-r) has first correction (r+1)/n. For r=1 and epsilon=1/4, substitution gives alpha=1+2/n+O(n^-2), beta=1-2/n+O(n^-2), and the intermediate normalizing quantity N=2+O(1/n), rather than 1. The claimed n^-3/2 error does not cover this. The final leading estimate with its larger O(1/r) allowance is not disproved. |
| V4A-F0107 | Equations (50)–(51), p. 427: writing A=k*xi*(k*xi+k+1)/(2*(xi+1)^2*n), the normalized Bell ratio is exp(A+error), not uniformly 1+A+O(k^3/n^2). At k=floor(sqrt(n)), the former tends to exp(1/2), the latter to 3/2. Even for k=1 the next coefficient grows like -xi/12, so the printed O(n^-2) omits a logarithm. The final weaker bound in (51) survives. |
| V4A-F0108 | Answer 7.2.1.5-65, p. 778: let X_k count blocks of size k and lambda=xi^k/k!, where xi*exp(xi)=n. At k=floor(xi), the exact factorial moments imply Var(X_k)/lambda=1-1/sqrt(2*pi*xi)+o(xi^-1/2). Taking epsilon=1/8 contradicts the printed uniform relative O(n^-1/2) error. The exact moment formula and leading equivalence remain valid. |
| V4A-F0109 | Answer 7.2.1.5-76, p. 779: in the positive sum R=sum_j binom(n,j)*B_(2n-j), the term j=2 divided by the printed truncation B_(2n)+n*B_(2n-1) grows like xi/4. Since 2^n*P(0,n) is at least R, the claimed relative o(1) truncation cannot hold. The full sum must be retained. |
| V4A-F0110 | Answer 7.2.1.6-44, p. 793: expanding the stated memory cost C_(n+1)+4*C_n+2*sum_(j=1)^(n-1) C_j+O(n), using p. 450 equation (20), yields first correction -14/(3n), not -10/(3n). The leading coefficient 26/3 is correct. |
| V4A-F0111 | Answer 7.2.1.6-21, p. 784: step G1 leaves b_1,...,b_(f-1) undefined for a forest with f roots. With three leaves and two unary nodes the first output must be 00110; the first two entries have not been assigned. Initialize this prefix to zero. The single-tree case is unaffected. |
| V4A-F0112 | Answer 7.2.1.6-37, p. 791: the ballot specialization needs n_0=q+1, not (t-1)*q+1. At t=3,p=1,q=2 the intended count is one, while the printed substitution gives three. |
| V4A-F0113 | Answer 7.2.1.6-37, p. 791: the unary-forest combination example needs n_0=r+1, not m+r+1. For m=2,r=1 the printed forest class contains ten objects rather than the intended three. The later fixed-r lower-bound discussion survives. |
| V4A-F0114 | Answer 7.2.1.6-37, pp. 791–792: removing a degree-j node changes the composition by f_j=e_j+(j-1)e_0, not by subtracting the leaf contribution. At n_0=3,n_2=2, C-E is one rather than the printed three. The later C(n+e_j;j) also requires n+f_j; the same composition gives C+D=5 instead of zero. |
| V4A-F0115 | Answer 7.2.1.6-37, p. 792: the convolution constraint f(n')=f(n) makes the complementary composition a nonempty zero-root forest, forcing its D value to zero. The printed Z sum therefore vanishes. For n_0=4,n_2=3, the listed degree words 2020200,2022000,2200200,2202000,2220000 have Z=1. The corrected sums use D(n')*k(n-n'), D(n')*l(n-n'), and D(n') respectively. |
| V4A-F0116 | Answer 7.2.1.6-36, p. 790: h cannot mean the number of changed degree entries. In 3003000 -> 3030000 -> 3300000, both transitions change two entries, while the asserted count for h>1 is one. The intended statistic is one plus the number of T4 loop executions, including the final termination attempt, consistent with the analysis on p. 450. The leading 4/23 proportion remains correct. |
| V4A-F0117 | Answer 7.2.1.6-27(f), p. 787: the printed chain reverses the direction of the inequality for a meet, the greatest common lower bound. The scope vectors 10 and 00 already contradict that direction. The proof should use the greatest-lower-bound property; the conclusion is true. |
| V4A-F0118 | Answer 7.2.1.6-32, pp. 788–789: the upper fiber bound has s'' >= s, not s'' <= s. When both inputs have scope vector 100, the maximum vector in the fiber is 210. The subsequent semidistributivity argument also needs the actual lower endpoint A=F meet G where the inherited interval notation uses F. The construction and lattice laws remain valid. |
| V4A-F0119 | Answer 7.2.1.6-33(e), p. 789: the limit of ((x+y)^(n-1)-y^(n-1))/x as x tends to zero is (n-1)*y^(n-2). At n=2,y=2, the true value is one and the printed value is two. The corrected recurrence still gives q_n=n^(n-2). |
| V4A-F0120 | Answer 7.2.1.6-53(c), p. 795: the mean leftmost depth is 2-2^(1-n), not 2-2^(-n). For n=2 the mean is 3/2, not 7/4. Part (d)'s distribution agrees with this correction; E(2^X)=n+1 is unchanged. |

## Prior-report screen

Compared the refreshed official `all4a-pre`, `all4a`, `err4a`, `all4f3`,
`err4f3`, `all4f4`, and `err4f4` layers at the book pages and the fascicle
offsets. Nearby entries concerning the p. 778 modal partition, p. 788
answers 30–31, p. 789 permutation notation, and p. 795 answer 53's wording
do not repair the retained defects. The 2025 notation changes were also
checked. The source manifest records URLs, timestamps, and hashes.

Fresh public queries combined Knuth, the relevant page or section, and
Bell ratios, block-count variance, paired multisets, Zaks initialization,
Zaks–Richards forests, binary-tree memory, Tamari bounds, or degenerate
leftmost depth with error/errata. No matching prior report was found.
The [public exercise archive](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4)
was screened for 7.2.1.5 exercises 56, 61, 64, 65, 76 and 7.2.1.6 exercises
21, 27, 32, 33, 36, 37, 44, 53. Many files describe unrelated problems;
they are not independent verification. Its answer 7.2.1.5-56 gives the
correct derivative identity and positive bound, but does not identify or
discuss the erroneous printed answer. The correct inequality is already
in the book's main text. A correct solution is not evidence of a prior
report of this particular defect.

The retained novelty assessment means no matching prior report was found
in this screen; it does not establish priority. Existing detailed proofs
and targeted algebra were reused without broad enumeration.
