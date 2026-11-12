# V4A-F0027: The component splice writes through the null pointer

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), printed page 612 / file page 629.
Original: `images/bookwise-p612.png`.

In I4, suppose the absorbed node R has a nonempty child list. The
step stores its first child in Q-prime, sets R to Q-prime, and runs

    while R != Lambda:
        PARENT(R) <- P-prime
        R-prime <- R
        R <- SIB(R)
    SIB(R) <- Q

The last assignment uses R=Lambda. The intended link is from the
last transferred child to Q. In the original first printing, that
last child is still available in R-prime; use SIB(R-prime) <- Q.

This case is reached when the current tree has the chain
ROOT -> A -> B -> C and the next white row joins B to ROOT.
For a concrete bitmap, use seven columns and these four rows:

    1111111
    1000001
    1001001
    0000000

After the third row, A is the outer black component, B its enclosed
current white component, and C the isolated middle black pixel.
On the fourth row, the first I3 dispatch is case 0: Q=A, R=B, and
CHILD(B)=C. I4 transfers C to ROOT, reaches R=Lambda, and attempts
the null write. This trace assumes the independent missing child
initialization in F0026 has been supplied.

The 11 March 2012 erratum removes R-prime <- R from the loop but
leaves SIB(R) <- Q untouched, so it does not fix this defect. To use
the repair above, retain the last-child assignment as well. The
known erratum is documented, not counted separately as a new defect.

The original first-edition, first-printing page image was inspected.
Current and historical Volume 4A and Fascicle 1 errata were screened,
including the original PDF of all4a-pre page 28. No correction of this
defect was located. Targeted public searches found no matching report;
this does not establish absolute novelty. The source record is
`sources/graphics-source-check.json`. The calculations/traces here
were checked by hand; no general verifier or census was run.
