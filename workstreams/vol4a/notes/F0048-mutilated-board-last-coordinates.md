# V4A-F0048: The last two coverage counts have the wrong parity

Confirmed, low severity. Volume4A, first edition, first printing
(2011), answer7.1.4-213, printed663 / file680. Original:
`images/bookwise-p663.png`; context main252.

The 62-cell board has two opposite corners removed. Only the first
60 column sums are constrained to be one. The answer says the last
two sums must be (2,1) or (3,2). Each selected domino row contributes
exactly two ones, so the total of all62 column sums must be even.
The printed alternatives instead total63 and65.

In the row-by-row cell order, column61 is the black cell (8,6) and
column62 is the white cell (8,7). The first60 cells contain29 black
and31 white cells. If their remaining coverage counts are a and b,
equal black/white incidences imply 29+a=31+b, hence a=b+2. The black
cell has only three available domino neighbors. Therefore the
possible pairs are (2,0) and (3,1), replacing (2,1) and (3,2).

The impossibility of a complete covering and the main text's
assertion that column61 has at least two incidences remain correct.
The large count of partial coverings was not recomputed.

No matching correction was located in the relevant current and
historical 4A/Fascicle1 errata or targeted public searches; see
`sources/zdd-algebra-covering-source-check.json`. Absolute novelty
is not established. The parity check is independent of enumeration.
