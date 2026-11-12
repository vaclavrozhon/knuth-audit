# The crossing and nesting pairs must be consecutive in their blocks

Volume 4A, first edition, first printing (2011), Answer 7.2.1.5–27, crossing/nesting definitions,
printed page 768, file page 785.

The answer defines a crossing or nesting using only the endpoint inequalities and the requirement that the two endpoints belong to the same block. The tableau construction, however, uses the links between **consecutive** elements of each block.

Here is a counterexample to the definitions as printed. Let Pi=15|234 be a partition of {1,...,5}. Its shape loop, with 0 denoting the empty shape, is

```
0,0,1,1,2,1,2,1,1,0,0.
```

Transposing every shape gives

```
0,0,1,1,11,1,11,1,1,0,0,
```

which corresponds to Pi^D=135|24. These loops can be read directly from the active links: Pi has links (1,5),(2,3),(3,4), and Pi^D has (1,3),(2,4),(3,5).

At the cut l=2, Pi has no 2-crossing even under the printed broad definition: a pair starting at 1 must end at 5, and a pair starting at 2 ends at 3 or 4, so their right endpoints cannot be increasing. Yet Pi^D has the printed 2-nesting (1,5),(2,4), since 1<2<=2<4<5. The pair (1,5) skips 3 within the block 135; it is not a link and is exactly the spurious pair that the missing condition admits.

The correction agrees with the cited primary paper: Chen, Deng, Du, Stanley and Yan, [Crossings and Nestings of Matchings and Partitions](https://arxiv.org/pdf/math/0501230), preprint page 3, defines both statistics using arcs in the standard representation, joining consecutive block elements. Only that definition passage was used here; the article was not independently audited in full. The local copy and retrieval provenance are in `../sources/chen-crossings-nestings-2005.*`.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-counting-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
