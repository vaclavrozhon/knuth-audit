# Volume 4A: BDD foundations, publication review

Reviewed on 12 November 2026 against the first edition, first printing
(2011). A binary decision diagram (BDD) represents a Boolean function
by successive variable tests. A quasi-reduced diagram retains redundant
tests; a zero-suppressed diagram (ZDD) omits a node with an impossible
high branch. The detailed notes define the remaining notation.

Original pages 207, 214–215, 227, 267–268, 622, 629, 633,
642–643, 647–648 and 660 were inspected as relevant. Seven findings
are retained. F0035 was separately dismissed: the alleged missing prime
is present in both the existing image and a fresh rendering of the book.

| ID | Reason for retaining the finding |
| --- | --- |
| V4A-F0033 | Answer 9, p. 622: the false function has s1=0 and s2=1, so the proposed s1 guard admits a function with no solutions. The guard must use s2. Page 207's terminal convention confirms the case. |
| V4A-F0034 | Theorem M, pp. 214–215: uniqueness of a complete network assignment does not make each cut's local response a function. With M1: u=v, M2: v=u XOR b and a=u, M3: b=a XOR x3 and f=a, the full network uniquely forces b=0 and a=u=v=x3, but the left side has both a=0 and a=1 when b=0. The asserted local A(b) is undefined. This is a proof gap, not a counterexample to the theorem. |
| V4A-F0036 | Answer 130(b), p. 642: the restriction omits edges within the middle k vertices. At m=8,k=2, isolate vertices 1,2, join 3,4 to 5 through 8, and put only edge 5--6 among the latter. The listed restrictions and the later two-clique hold, but the missing edge 3--4 prevents a four-clique. |
| V4A-F0037 | Exercise 131(a), p. 267: with fixed q=2, the exact expression in answer 131, p. 642, is 7p-2 rather than asymptotic to 4p. Their ratio tends to 7/4. The leading coefficient for fixed q is (q+2)*2^(q-1)-1. |
| V4A-F0038 | Answers 147 and 202, pp. 648 and 660: the swap modifications decrement references when old nodes disappear but do not increment the children when U3 creates new nodes. The small witnesses in the detailed note leave a reachable child with reference count zero. This concerns the printed modifications; Knuth's public bdd14 program already increments both children. |
| V4A-F0039 | Answer 135, p. 643: the recurrence for the purported uniquely thin example gives theta5 restricted to x1=0 as x5 AND x4 AND NOT x3, independent of x2. Thus the claimed dependency exception is not unique, and the indicated weight is one rather than two. The existence of other uniquely thin functions is not refuted. |
| V4A-F0040 | Exercise 146(b) and answer, pp. 268 and 647: b0=1,b1=2,q0=1,q2=5 meets the displayed inequalities, but one root after two binary tests has at most four distinct nodes. The converse needs an additional reachability bound, such as q2<=q0+b0+b1; this necessary condition is not asserted to be sufficient. |

## Official and public-source comparison

Compared the refreshed [prepublication changes](https://www-cs-faculty.stanford.edu/~knuth/all4a-pre.ps.gz),
[later changes](https://www-cs-faculty.stanford.edu/~knuth/all4a.ps.gz),
[current errata](https://www-cs-faculty.stanford.edu/~knuth/err4a.ps.gz),
and the two Fascicle 1 layers
([all4f1](https://www-cs-faculty.stanford.edu/~knuth/all4f1.ps.gz),
[err4f1](https://www-cs-faculty.stanford.edu/~knuth/err4f1.ps.gz)).
The 2012 McMillan credit and 2025 wording change to Theorem M do not
supply the missing local response. The 2011 corrections to exercises
130–131 and the 2012 indexed-variable change to answer 133 are different.
No matching correction appears in the corresponding Fascicle 1 entries.

New public searches combined Knuth/TAOCP with Theorem M, unique network
assignment, covering function 131, swap 147/reference count, uniquely
thin, quasi-profile 146, clique 130/errata, and the solution guards.
The [tamnd/brain solutions](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4/7.1.4)
for 9, 130, 131, 135, 146, 147 and 202 were individually screened.
They either repeat the issue, address different problems, or give general
algorithms without identifying the corresponding printed error.

For F0038, the primary [bdd14 source](https://www-cs-faculty.stanford.edu/~knuth/programs/bdd14.w)
was checked: its swap_find creation branch explicitly increments both
child reference counts. This is prior correct implementation of the
needed step, but does not identify the omission in the book. Ben Lynn's
[ZDD implementation notes](https://crypto.stanford.edu/pbc/notes/zdd/implementation.html)
also discuss reference counts without reporting this book defect.

No matching prior error report was found in these sources. This is
not a claim that the underlying correct methods are new; absolute
priority is not established.
