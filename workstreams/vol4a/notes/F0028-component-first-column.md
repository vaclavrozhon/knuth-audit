# V4A-F0028: The first black pixel is recorded one column too far left

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), printed page 613 / file page 630.
Original: `images/bookwise-p613.png`.

The answer numbers image pixels x_1,...,x_N and defines

    a_j = 2*c_j - (j mod 2).

For a new black run, j is odd and c_j is its first column. Step I10
stores COL(Q)=floor(a_j/2)=c_j-1. The promised first-pixel location
is therefore one column too far left. For example, row 010 has its
single black pixel at column 2, with a_1=3; the step stores column 1.
White-run boundaries have even j and do not have this discrepancy.

Use COL(Q)=ceil(a_j/2). This agrees with both colors and with the
ceiling-based run lengths already used for AREA in the same step.
The error affects the recorded location; by itself it does not
change the component count or the tree topology.

The original first-edition, first-printing page image was inspected.
Current and historical Volume 4A and Fascicle 1 errata were screened,
including the original PDF of all4a-pre page 28. No correction of this
defect was located. Targeted public searches found no matching report;
this does not establish absolute novelty. The source record is
`sources/graphics-source-check.json`. The calculations/traces here
were checked by hand; no general verifier or census was run.
