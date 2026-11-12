# The first row gap is two cells too large

Volume 4A, first edition, first printing (2011), Answer 7.2.1.5–29(b), row-gap term in text and displayed sum,
printed page 769, file page 786.

The unchosen rows strictly between selected rows i_1 and i_2 number i_2-i_1-1. In the answer's count of free cells in unchosen rows and selected columns, and again in the following displayed exponent, this gap is printed as **i_2-i_1+1**.

For m=3 and r=2, choose rows i_1=1 and i_2=3. The only unchosen row is row 2; among the two selected columns it has one free cell, in the column of the rook above it. The printed expression gives 3 instead of 1.

Over all choices of two rows from three, the correct weights sum to `1+y+y^2`. The printed exponents instead give `y^2+y^3+y^4`, contradicting the Gaussian-binomial evaluation immediately below. Changing +1 to -1 in both places repairs the derivation; the final rectangular-board formula is correct.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-counting-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
