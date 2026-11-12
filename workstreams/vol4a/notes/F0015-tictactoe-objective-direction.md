# V4A-F0015: the all-good-moves exercise reverses the objective

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), exercise 7.1.2-67, printed page 130 / file page 147.
Original: `images/file147.png`.

The all-good-moves exercise specifies moves that “minimize” X's
worst-case outcome. Its context on page 115 requires X to take a
forced win when possible and avoid defeat when possible. Answer 66
on page 574 explicitly describes that objective as maximizing the
worst-case final outcome. Exercise 67 is intended to return all moves
with that same optimal value, rather than choose only one of them.

Change “minimizes” to “maximizes” to agree with the stated convention.
The examples and intended circuit problem make the intended meaning
clear; this is a wording inconsistency, not evidence that the supplied
818-gate construction computes bad moves.

The wording was introduced by the Fascicle 0 erratum dated 7 March
2010 for page 130, exercise 67, and carried into this printing of 4A.
Neither current nor historical 4A errata, nor the two Fascicle 0 layers,
provide a subsequent correction. A targeted public search found no
matching report; absolute novelty is not established. See
`sources/determinant-tictactoe-source-check.json`. No computation was
needed.
