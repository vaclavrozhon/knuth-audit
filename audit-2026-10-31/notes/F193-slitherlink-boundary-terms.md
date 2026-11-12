# F193 — two finite bounds omit the grid boundary

Volume4B, first edition, second printing (November2022), §7.2.2.1,
answer416, printed537 / file557. Two finite inequalities in the density
argument need correction. The limiting density conclusions are unchanged.

First, let S be the set of clues, all equal to3, on an n×n board.
The claimed bound |S|≤n²/2 is false for odd n. This3×3 puzzle is valid:

```
3 3 3
. . .
3 3 3
```

It has six clues, exceeding9/2. The three clues in the top row force
a zigzag from the left side to the right side; the bottom row forces
its reflected zigzag. The two side edges join them into the unique
loop. With grid-vertex coordinates from0 through3, that loop is

```
(1,0),(0,0),(0,1),(1,1),(1,2),(0,2),(0,3),(1,3),
(2,3),(3,3),(3,2),(2,2),(2,1),(3,1),(3,0),(2,0),(1,0).
```

Partitioning the board into2×2 blocks proves the printed bound when
n is even. For general n it gives n²/2+O(n), which is enough for the
limiting upper density1/2.

Second, in the zero-clue argument the answer says at least n²+2n of
the2n(n+1) grid edges must be eliminated to leave only one cycle.
The2×2 puzzle with just a zero in its upper-left cell disproves this:

```
0 .
. .
```

The zero eliminates four edges, not at least8. Among the remaining
eight edges there is exactly one cycle, the four edges around the
lower-right cell; the other edges form two attached paths. Thus this
is a valid, nonempty-clue puzzle too.

The general counting argument should use (n+1)² grid vertices. A graph
with only one cycle has at most that many edges, so at least
2n(n+1)−(n+1)²=n²−1 edges must be removed. Each zero removes at most
four, yielding the intended asymptotic lower bound on the number of
clues. Neither correction changes the stated limiting densities.

The two particular puzzles, including uniqueness, were checked by
`check_bookwise_slitherlink416.py` in7 and3 search nodes respectively;
the actual loops are saved in `results/bookwise-slitherlink416.json`.
No general puzzle census was run.

Original: `images/bookwise-p537.png`. Both finite bounds also appear
in the author's September2019 pre-fascicle, printed241. Relevant
historical/current errata and public searches have no matching correction;
see `sources/bookwise-slitherlink-source-check.json`. No claim of
absolute priority is made.
