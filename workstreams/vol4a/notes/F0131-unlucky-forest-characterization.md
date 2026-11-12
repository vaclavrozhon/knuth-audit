# Forests without unlucky nodes need an alternating reversal

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–117, printed 809.

In prepostorder, a node at even depth is visited before its children, while a node at odd depth is visited after them; the roots have depth 0. Exercise 116 calls a node unlucky when the next node is three edges away, with an imaginary parent above all roots used as the final successor. A degenerate binary tree has at most one nonempty child at each node. The left-child/right-sibling representation uses a node's first child as its binary left child and its next sibling as its binary right child.

The answer says that forests without unlucky nodes are precisely those with a degenerate binary representation. Consider the ordered four-node tree

    r
    |-- a
    |   `-- b
    `-- c

Its prepostorder is r,b,a,c. Including the last transition to the imaginary parent, the distances are 2,1,2,2, so no node is unlucky. But a has binary left child b and binary right child c, so the binary tree is not degenerate.

The converse fails too. Reverse the two children of r, obtaining first c and then a with child b. The binary representation is the chain r--left-->c--right-->a--left-->b and is degenerate. Its prepostorder is r,c,b,a; the transition c to b has length 3.

The numerical answer 2^(n-1), for nonempty n-node forests, can be retained. Algorithm Q shows that no unlucky transition occurs exactly when every nonleaf node at even depth is its last sibling and every nonleaf node at odd depth is its first sibling. Reverse the child list of each even-depth node. This involution preserves depths and changes that condition into: every nonleaf node is its last sibling. The latter is exactly the condition for a degenerate left-child/right-sibling representation. Thus the conversion needs this alternating reversal before invoking the 2^(n-1) count from exercise 31.

Original definitions, exercise 31, exercise 117 and answer 117 inspected. No matching correction was found in the historical/current Volume 4A errata, refreshed Fascicle 4 errata or targeted public searches; see `../sources/tree-quasi-gray-source-check.json`. Absolute novelty is not established.
