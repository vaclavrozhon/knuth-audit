# Implicational and semilattice constraints; exercises 363–379

Read main printed 79–83 and the opening semilattice paragraph of 84,
questions 363–379, and complete paired answers 238–241. Original pages
148 and 239 were inspected for formulas and the finding. Applied the
reversal in 363(c), both corrections to the path argument in 365(b),
and the good-component qualification and correspondence wording in
the proof of Theorem I.

The shift gadget in 363 copies the indicated overlapping coordinates.
After the published reversal, the last coordinate of x^(i) is equated
to the penultimate coordinate of y^[j], namely x_i=y_j. The other
auxiliary coordinates remain free. Fresh copies of the auxiliaries avoid
additional equalities in (d). Concatenating the relation tables in 364
then gives the stated satisfiability equivalence, including the three
identifications in its eight-coordinate example. Its final polynomial-time
description is false for unbounded input size: F7-C0018 gives the direct
exponential output-size family. The equivalence itself is accepted.

For 365, two edges of an oriented path cannot cross in the coordinatewise
order, giving min and max closure. A directed three-edge run pins the
exceptional run in a homomorphism; following the preceding/following
110 blocks gives the corrected contradiction when the run positions
differ. The map u -> u-2[u>=3i+3] folds precisely the extra two vertices
in (c), and its step directions agree with the target. The small final
counterexample R110111 maps to the indicated later-run paths and not
the initial-run path. The bibliographic assertion about the cited paper's
exact sentence was not independently authenticated.

Removing a leaf variable in 366 retains exactly the supported values of
its neighbor, with all compatible leaf values recoverable afterwards.
The 18 excluded two-by-three relations in 367 split into the stated
three six-case families; all two-by-two relations are implicational.
The intersection cases in 368 preserve the complete, matching or two-fan
forms after empty supports are removed. Figure 119 and the four domain
intersections in 369 give (135), and the implication arcs give (136)–(138).

For Theorem I, restricting the domains preserves solutions. Bad strong
components and their predecessors cannot contribute to a solution. The
corrected reverse-path property (140) uses an alternative binding in a
good component: for a correspondence its inverse remains available,
and for a two-fan the reverse implication forces the opposite center.
This proves the sink-order arguments in 370: assigning one variable of
a component assigns all of them, and a violated later constraint would
have required an already processed different assignment. A solution's
bindings all survive the bad-component deletion, so a variable left
unassigned certifies unsatisfiability.

The sorted-list alignment in 371 advances pointers monotonically and
agrees with the intersection representation. Once the cyclic alignments
stabilize, every list has the same head value; after output, advancing
each pointer prevents duplication. The total work is charged to input
pointer advances and one round per output, with at most the summed
list lengths plus the initialization. This supplies the domain-reduction
step in the stated linear-time representation of Theorem I; the existing
Tarjan review supplies the strong-component step.

For max closure, (141) and the indicator functions in 374 prove (142).
The witness (3,1,2),(3,2,1) disproves max closure of x^2>=4yz, while
x^2<=4yz has the required monotone orientation. In 372 the missing entry
is indeed row 3, column 6 (zero-based) of the right matrix; the left
matrix already has the required maxima. Reversing the Boolean order
gives the Horn-clause correspondence in 375. Joining the coordinatewise
maximum-support tuples proves 376.

The algebraic and order definitions of a semilattice in 377 agree by
idempotence, commutativity and associativity. In 378, unary domains and
projections remain join-closed during consistency propagation, so each
finite domain's join is still present. Joining support tuples proves that
the simultaneous assignments satisfy every constraint. In 379 the tuple
domain uses componentwise max, and its coordinate projections preserve
that operation. Ordinary values and hidden tuple variables use their
respective domain operations; no extra common-domain representation is
needed for this argument.

Only F7-C0018 is new in this block. Standard Gaussian elimination,
Tarjan's accepted prior proof and the cited general Horn/semilattice
results are reused; no new theorem proof, external archival audit or
large computation was undertaken.
