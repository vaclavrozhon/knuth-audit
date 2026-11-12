# The number of occupied diagonals need not decrease

Volume 4A, first edition, first printing (2011), Answer 7.2.1.4–70, continuation on page 761,
printed page 761, file page 778.

The proof first rotates cells within each northeast-to-southwest diagonal of the Ferrers diagram, then moves the newly introduced top row down to its sorted position. It claims that a nontrivial sorting move always decreases the number of occupied diagonals.

For the partition 43 of 7, the rotation produces row lengths (2,3,2). Sorting moves the top row below the row of length 3, giving the next partition 322. Both 43 and 322 occupy exactly four diagonals. Indeed, for cell (i,j), counted from the top left with i,j>=1, its diagonal index is i+j-1, and the maximum occupied index is respectively

```
max(4,3+1)=4,
max(3,2+1,2+2)=4.
```

Thus the asserted strict decrease is false. The same phenomenon occurs at triangular size 10: 541 becomes 433, with five occupied diagonals before and after.

A suitable repair is the potential `E=sum(i+j-1)` over all occupied cells. The initial diagonal rotation preserves E. Swapping a top row of length a downward past a longer row of length b changes E by a-b<0. Thus each nontrivial sorting operation strictly decreases E and cannot occur on a cycle. In the 43 example E decreases from 19 to 18. This repairs the proof's transition to the classification of cyclic states without changing the classification itself.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/partition-gray-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
