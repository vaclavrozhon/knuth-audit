# F101: published counterexample predates this audit

Review date: 12 November 2026. The mathematical discrepancy is valid,
but the card must not be presented as a previously undiscovered error.

[Perrin and Reutenauer](https://arxiv.org/abs/1609.05438), submitted
18 September 2016 and published in Discrete Mathematics 341 (2018),
232–243, explicitly distinguish the Eastman and Scholtz codeword sets.
Example 17 gives exactly the length-33 word used in our card and the
different cyclic representative selected by the other construction.
The article's sections 4 and 6 define the compared procedures.

Our existing `COMMAFREE_NOTES.md` already acknowledges this source.
Checking the example computationally adds verification, not novelty.
Although the paper does not call the later 4B sentence an erratum,
the specific mathematical counterexample was already public. No matching
official erratum was found in the refreshed author lists.

Decision: keep correctness confirmed; mark novelty
`previously_publicly_discussed` and exclude F101 from the new-finding view.
