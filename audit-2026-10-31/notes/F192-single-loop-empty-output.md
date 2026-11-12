# F192 — the single-loop modification still accepts no loop

Volume4B, first edition, second printing (November2022), §7.2.2.1,
answer413, printed536 / file556.

The construction of412 gives each vertex an option with no incident
selected edges. For a puzzle containing only zero clues, choose those
options everywhere and the all-zero option for each clue. This covers
all primary items and assigns color0 consistently to every edge.

The modification in413 changes what happens when an edge receives
color1. None of those checks runs for this completed all-zero assignment.
Its fragment count F and loop-closing edge E remain0, so the original
AlgorithmC completion step still visits it as a solution. It is not
a single loop.

This applies directly to the book's own5×5 puzzle410(a), which has
only zero clues and a unique actual loop. Answer412 explicitly reports
two weak solutions for that puzzle, differing by the center4-cycle:
one is the empty edge set. The modification must remove that weak
solution as well as solutions with multiple loops.

At a completed exact cover, **visit the solution only when E is nonzero**.
Equivalently, enforce that at least one edge is selected. The existing
fragment rules then supply the at-most-one-loop part. This does not
dispute the reported puzzle census numbers or show which separate
completion checks the author's implementation may already contain.

Original: `images/bookwise-p536.png`. The historical23December2019
Fascicle5 replacement for413 and the current2023 unpurify correction
contain no such completion check. Public searches found no matching
correction; scope is in `sources/bookwise-slitherlink-source-check.json`.
Absolute priority is not asserted.
