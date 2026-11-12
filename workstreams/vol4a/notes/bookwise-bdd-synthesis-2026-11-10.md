# BDD synthesis, shared bases, quantification and composition

Main pages 220–233 through the end of functional composition, exercises
66–107, and answers 630–637 were read together. Whole main pages
220–232, exercise pages 263–265 and answer pages 630–636 are certified.
Shared main 233, exercise 266 and answer 637 remain for the size-bound
block. No new finding was confirmed in this block.

Algorithm S schedules the two descendant requests of each template at
their first active variable. The truth-table masks in find-level handle
both sinks and one constant input. The per-level hash area has enough
slots for all requests; its head fields can overlap templates because
new templates use the other fields until hashing finishes. Empty levels
still receive the appropriate LSTART boundary. During descending
reduction, RIGHT redirects children to their representatives; the first
bucket pass groups equal LO values and restores the children's clone
addresses. The second pass groups equal HI values, restores those marks,
and emits one clone per distinct pair. The worked eight-template
example, singleton-bucket shortcut, constant exit and memory checks
were followed. The smaller-table variant requires an additional growth
check. The bucket-sort alternative is a sketch, not a complete second
implementation.

The monotone-function recurrence separates even and odd truth-table
positions and then enforces the missing one-bit inequalities. Self-dual
functions replace the second half by complemented reverse entries;
regular functions additionally enforce the adjacent majorization step.
The earlier regularity definition was reread for this dependency. The
clutter transformation flips forced choices without changing future
forced supersets. In answer 77, consistent prefixes determine distinct
subfunctions; on the second half, complemented reversed forced vectors
supply the symmetric profile. The corrected index in the witness and
the identity c_k=b_(k+1)-b_k were used. The two half-profile formulas
also give the stated half of the branch nodes with a false LO child.
Graph-degree counting uses one threshold condition per vertex, and the
edge-probability weights are 2^(66-k)/3^66.

The unique table distinguishes node identity from the disposable memo
cache. Every returned result receives one temporary reference. U1
combines two references to the same child; U2 either removes temporary
child references already represented by a live node or transfers them
to a resurrected node. Cache resurrection recursively restores child
references, and assignment drops the previous external reference only
after the result is protected. Garbage collection removes dead keys
and results from the cache before recycling addresses. The multiplication
recurrence is the ordinary shift-and-add recurrence; its large census
and timing numbers were not reproduced.

The ternary Shannon recursion and its constant/duplicate cases were
checked, including the two examples where three-way conjunction avoids
large binary intermediates. In the second example, the three pairwise
intersections occur in different two-bit cases, while the triple is
empty. The original bars were inspected. Boolean quantification uses
OR, AND or XOR of the two cofactors. Formula (65) drops a quantified
variable absent from f, preserves variables absent from the quantifier
set, and combines the branches otherwise. Bottom-level quantification
reduces each processed node to a constant before its predecessor is
visited. The yes/no quantifiers characterize monotonicity.

Constrain chooses the first care-set point in XOR order, which gives
the printed recursive cases. Its order independence forces every
nonconstant coordinate of the care set to be fixed, hence a subcube.
The coloring reduction in answer 93 forces each distinct vertex
subfunction to carry the same 4n-variable OR chain. Four distinct
subfunctions would exceed the threshold, while a three-coloring gives
three chains and legal last-block choices. The implicit kernel graph
uses Hamming distance two; maximality forces such a swap to follow an
original edge. Endpoint and pair-component formulas then express their
stated degree conditions. Triangle color fixing removes the 24 color
permutations; the weighted color objective differs from its two-bit
encoding only by a constant.

Composition cache stamps retain right-hand suffix results and change
only affected prefixes. The master stamp is reused only before any
composition has consumed it; resetting all replacements to identities
can therefore discard that unused stamp. The equality-substitution
formula in answer 103 is logically equivalent to composition, without
implying equal computational cost. Comparison combines cofactor
relations. Unateness accumulates compatible polarities, and the Horn
and Krom recursions test closure under coordinatewise AND and majority.
Their terminal rules correctly exploit the sorting of constant node
addresses. Complexity/cache, source and census limitations are stated
in the companion exceptions file.

Next: main233/file250, worst and average BDD sizes, QDDs and hidden
weighted bits; exercises108 onward and answers637 onward. The earlier
forward dependencies from exercises47–48 remain pending there.
