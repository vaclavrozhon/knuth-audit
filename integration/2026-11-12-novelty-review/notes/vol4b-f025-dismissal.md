# F025 withdrawn: the printed blocking graph has the correct orientation

Publication review, 2026-11-12. The November 2022 second-printing PDF,
printed p. 579, answer 7.2.2.2-162, defines the edge **l' -> l** when
every clause containing the complement of l also contains l'. The
earlier audit transcribed it as l -> l'. A fresh 220 dpi rendering of
PDF page 599 makes the prime unambiguous. This is an audit error.

With the actual definition, all incoming neighbors of a nonpure l
occur in any clause containing its complement. There are at most k-1
such neighbors from different variables in a kSAT formula. The printed
in-degree bound is therefore correct. For a proposed binary clause
(p or q), the edge -p -> q means that every clause containing -q also
contains -p. This is precisely blocking on q. The other printed edge
handles blocking on p. Both directions in the book agree with resolution.

The alleged five-clause counterexample is

```
(x or y or z), (-x or z), (-x or -z), (-y or z), (-y or -z).
```

It has the unique solution (x,y,z)=(0,0,1), but neither required edge
-x -> y nor -y -> x exists in the printed graph. The book does not
permit adding (x or y). The earlier test implemented the transposed
graph and thus tested a different statement.

The revised `check_blocking_graph.py` checks the actual definition
against direct resolution on the previous witnesses. Its earlier
version and output are preserved in the local review backup. F025 is
dismissed in the ledger, card, and location data. The old shared prose
and unsent report have a withdrawal banner so their historical claim
cannot be mistaken for the current assessment.

F026 remains separate and valid. For (a or -b or c) and
(-a or b or -c), the printed graph has a strongly connected component
containing all six literals. Reversing every edge preserves strong
components. This component is inconsistent and cannot be an autarky,
which is a consistent partial satisfying assignment. The corrected
script verifies this witness in the book's orientation.
