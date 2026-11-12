# V4A-F0026: A new component has an uninitialized child pointer

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), printed page 613 / file page 630.
Original: `images/bookwise-p613.png`.

CHILD(Q) denotes the first child of component Q, or Lambda when Q
has no child. Step I10 allocates NODE(t) and sets PARENT, DORMANT,
HEIR, ROW, COL, AREA and SIB, but never sets CHILD. There is no
initialization of the whole node array; I1 initializes only ROOT.

Take N=3 and two identical input rows 010. Including the specified
white margins, each row is 00100. Its modified run boundaries are
(a1,a2,a3)=(3,6,9). On the first row I10 creates a new black node Q
as ROOT's child. On the second row I11 first reaches (Q,Q), and
a subsequent I11 calls next(Q,Q). The definition on page 612 reads
CHILD(Q) to determine whether this is a leaf. That field has never
been assigned.

Add CHILD(Q) <- Lambda to the initialization in I10. The node is a
new childless component. This omission is independent of the known
correction to the definition of next, and of the splice defect in
F0027. An implementation that zero-fills storage can happen to mask
it when Lambda is zero, but the printed algorithm has no such premise.

The original first-edition, first-printing page image was inspected.
Current and historical Volume 4A and Fascicle 1 errata were screened,
including the original PDF of all4a-pre page 28. No correction of this
defect was located. Targeted public searches found no matching report;
this does not establish absolute novelty. The source record is
`sources/graphics-source-check.json`. The calculations/traces here
were checked by hand; no general verifier or census was run.
