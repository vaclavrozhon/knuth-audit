# Retained frontmatter findings: presentation reconciliation

This note supplies an English account of the retained C0001 argument and
the qualified C0002 candidate. It does not add a new finding or repeat the
earlier calculations. The original notes, images and subsequent argument
review remain the evidence of the earlier work.

For F7-C0001 (preface xi, file 12), a perfect matching must cover every
vertex. Algorithm H permits unequal numbers of girls and boys. With one
girl adjacent to two boys, any maximum matching covers the girl and only
one boy. Thus the absence of a free girl proves optimality here but not
perfection. Removing “perfect and”, or adding equality of the two side
sizes for that assertion, repairs the sentence. The original evidence
includes files 10–12 and the definition of a perfect matching in Volume 4B.
The current errata reconciliation leaves this finding unchanged.

F7-C0002 (printed 19, file 34) is only a candidate about the convention
for isolated vertices in the reverse model. NAME assigns vertex names or
an unused-position marker to labels, and LO locates each required edge.
The constraints force every edge, and therefore every nonisolated vertex,
to occur. Under the preceding necessary check n <= m+1, where n is the
number of vertices and m the number of edges, all omitted isolated vertices
can be placed injectively in the remaining NAME positions. Consequently
there is no decision-equivalence counterexample under that natural
preprocessing convention. The old example with one edge and four vertices
does not pass this check and must not be presented as a counterexample to
the preprocessed model.

The narrower unresolved point is whether NAME states differing only by an
unused marker versus an isolated vertex are intended to be identified for
counting. In a triangle with one isolated vertex, these states complete to
the same labeling. Printed page 23 gives the relevant unused-label convention.
The retained record is not a confirmed error in a counting theorem or an
implementation. It remains a qualified interpretation candidate, separate
from red book-error markers. The detailed argument is in
`graceful-usa-models-and-exercise-071.md`, G19-1, and the dated addendum to
`F7-C0002.md`.
