# K5 tests the wrong quantity for evenness

Volume 4A, first edition, first printing (2011), Answer 7.2.1.4–64, Algorithm K, step K5,
printed page 759, file page 776.

Write a binary partition, whose parts are powers of two, using distinct sizes p_1<...<p_t and their multiplicities c_1,...,c_t. Step K5 says to remove `c_t-[t is even]` copies of the largest part, perform K3, and restore them. The bracket is 1 when its statement is true, and 0 otherwise. It must instead be **[c_t is even]**.

Take n=4. The algorithm starts with 1111, and K3 reaches the odd visit 211. Here t=2 and c_t=1. The printed introductory rule removes zero copies of 2, so K3 splits that 2 and returns to 1111. But the next partition must be 22, as both the displayed B(4) on page 758 and detailed case (1c1) specify.

The corrected rule removes the one copy of 2, applies K3 to 11 to merge it to 2, and restores the removed 2, giving 22. More generally it leaves zero copies of the largest size when c_t is odd, or one when c_t is even, exactly as the nine cases require. The error is in the explanatory transformation, not in those detailed cases.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/partition-gray-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
