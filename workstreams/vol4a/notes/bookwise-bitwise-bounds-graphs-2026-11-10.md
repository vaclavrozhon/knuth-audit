# Bitwise lower bounds, graph algorithms, and data representations

Main pages 156–167, exercises 115–153, and the corresponding answers
601–607 were read together. Whole pages 156–167, exercise pages
193–195, and answer pages 601–606 are certified with the explicit
limits below. Exercise page 196 and answer page 607 also contain
the next topic and remain for its coverage record.

F0023 is the new finding: Q7 in the maximal-clique update tests equality
instead of containment and can retain a strict subset in the purported
maximal family. The four-vertex trace is in its separate note. It
establishes the broken intermediate invariant, without claiming that
this particular graph's final clique list is incorrect.

The shift-set recurrences, Lemmas A and B, the shift-free characterization,
and the ruler/reversal counting arguments were followed. Theorem R uses
the corrected empty-intersection display. Answer 124 starts with the
corrected set of powers of two. The monus lower bound in answer 118
uses two even inputs with the same underflow outcomes; their first
different bit contradicts a right shift. The indicator construction
in 119, the multi-input count in 120, and the odd-cycle obstruction
and shift construction in 121 are consistent. The regular-language
argument uses finite carry state and closure under reversal of the
input-reading direction. Exact limits on the compressed RAM proofs
and multiplier argument are recorded rather than silently certified.
Research questions 117, 126, and 128–130 were not pursued.

The reachability invariant keeps processed vertices inside the reachable
set, and each iteration adds one processed vertex. The MMIX bitset and
circular-list implementations were read against that invariant. The
clique intersection identities in 132(a–c), the partition in M2, and
the two branches of subroutine Q were followed; the lower-family
filter gives F0023. Complementing the graph and then the output gives
the two reductions in 133.

For ternary representations, the 24 injective encodings reduce to three
cube-symmetry classes; the 36 ambiguous encodings split into three
eight-element and three four-element classes. The displayed product,
max/min and Lukasiewicz operations were checked on their legal codes,
including the shared don't-care choices. The packed formula in answer
137 cannot carry between fields because its legal input codes are
00,01,10. The balanced-ternary adder uses separate positive/negative
counts, followed by the displayed eight-step transformation. The Ulam
update maintains the zero/one/multiple-representation states; its
current empirical addendum was read without reproducing the census.
The subcube containment and consensus formulas were checked under both
encodings, resolving complement bars in the original. The knight masks
have the correct row/column boundaries; the MMIX matrices are the
one- and two-column adjacency matrices of the eight-position path.

The sideways-heap parent, children, interval, ancestor and nearest-common-
ancestor formulas were checked together. Algorithm V uses the common
height before intersecting routing masks, then the nearest available
lower routing level and the stored parent pointer. The dummy-vertex
case is selected by its preorder rank zero. The preprocessing's two
traversals compute preorder/subtree intervals and then routing masks;
the initial logarithm value is -1, reset after traversal. The Cartesian
tree construction in 150 maintains the left spine, and the shortened
Euler sequence in 151 gives the correct range-minimum reduction.
Answer 153's pointer endpoint is the sum of ruler values, j-popcount(j).
The beginning of the hyperbolic-plane discussion and Fig. 13 were read;
its substantive algorithms and exercises belong to the next block.

The relevant historical/current Volume 4A and Fascicle 1 errata were
screened. Known changes to 157, 602 and the Ulam empirical paragraph,
and the added navigation-pile citation, are not new findings. The
source files still match the fresh official manifests. No mathematical
program, helper, census, or old computation was started in this block.

See `results/bookwise-bitwise-bounds-graphs-exceptions.json` for the
precise proof, external-result and computational limits. Next: main
page 168 / file page 185, hyperbolic cells and the later bitwise
applications; exercises 154 onward and answers from page 607.
