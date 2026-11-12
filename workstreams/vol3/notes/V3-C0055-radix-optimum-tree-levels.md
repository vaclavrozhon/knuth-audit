# V3-C0055 — The radix-tree optimum argument shifts every level by one

Confirmed in volume 3, second edition, first printing (1998), answer
5.4.7-4, printed p.694, file p.705. The three level numbers in that
answer should be 1, 2, 3 instead of 2, 3, 4.

A node's level is its distance in edges from the root. The explicit
definition in volume 1, §2.3, printed p.308, places the root at level
zero. In volume 3's Ashenhurst tree (example 2 on p.344), the external
nodes for keys 0, 1, and 3 are therefore at level 2. Six external nodes
are at level 3, and the remaining one, for key 7, is at level 4. The
sum of their levels is

```
3*2 + 6*3 + 1*4 = 28,
```

which is exactly the stated 2.8 passes for ten equally frequent keys.
Thus the answer's opening assertion that a level-2 external node
precludes such a good tree is contradicted by the very tree whose
optimality the exercise asks to establish. It should exclude a
level-1 external node. The subsequent bounds of three and six short
external nodes concern levels 2 and 3, respectively.

This is a local error in the proof sketch's level labels. The claimed
optimum and the distribution schedule are not refuted. No exhaustive
search of strongly four-FIFO trees was needed for this counterexample.

The original tree and answer were visually checked and retained as
`images/bookwise-p344.png` and `images/bookwise-p694.png`; the definition
is retained as `images/bookwise-vol1-p308.png`. The five official
errata layers were screened in `sources/external-radix-errata-review.json`.
Targeted public searches for the Ashenhurst tree and the answer's
level wording found no matching report; this is not a priority claim.

The earlier block note incorrectly interpreted the root as level 1.
The explicit definition and the level convention in answer 5.4.9-12
prompted this correction to the audit's initial assessment.
