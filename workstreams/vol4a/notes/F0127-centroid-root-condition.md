# The centroid equivalence must specify vertex 0

Volume 4A, first edition, first printing (2011).
Exercise 7.2.1.6–90(a), printed 481.

A centroid of a finite tree is a vertex whose deletion leaves no component larger than half the original tree. A canonical forest is the ordered representative obtained by sorting rooted subtrees by their level codes; this does not force the added vertex 0 to be a centroid.

Part (a) states that a canonical n-node forest corresponds to a free tree with a single centroid if and only if every forest component has at most floor(n/2) nodes. The forward implication needs the additional condition that this centroid is vertex 0.

Take the canonical parent sequence 011, one of the examples immediately preceding the exercise. Its edges are 0--1, 1--2, 1--3. The free tree is a four-vertex star with unique centroid 1, but the forest obtained by deleting vertex 0 has a component of size 3, exceeding floor(3/2)=1. The same free tree is encoded by 000 when vertex 0 is chosen as its centroid.

Replace the condition by: the associated free tree has vertex 0 as its unique centroid. Deleting vertex 0 then gives exactly the components of the forest, and uniqueness requires their sizes to be strictly less than (n+1)/2, equivalently at most floor(n/2). The answer's statement that vertex 0 is the centroid reveals the intended interpretation, and the generation algorithms in (b) and (c) use that interpretation correctly.

Original typesetting inspected. No matching correction was found in the historical/current Volume 4A errata, refreshed Fascicle 4 errata or targeted public searches; see `../sources/tree-oriented-source-check.json`. Absolute novelty is not established.
