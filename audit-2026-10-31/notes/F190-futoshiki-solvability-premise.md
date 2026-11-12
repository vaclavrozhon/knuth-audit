# F190 — the five-clue lower bound needs solvability

Volume4B, first edition, second printing (November2022), §7.2.2.1,
exercise394, printed175 / file195. The statement that every five-clue
5×5 futoshiki puzzle has at least four solutions must be restricted
to **solvable puzzles** (equivalently, allow zero solutions as well).

Here is a five-strong-clue counterexample, where a dot is an empty cell:

```
1 . . . .
2 . . . .
3 . . . .
4 . . . .
. 5 . . .
```

No row or column already has a repeated given entry. But column1
forces5 in its last cell, and row5 already contains5. Thus there is
no completion to a Latin square. These are precisely the allowed
strong clues; no weak clue is needed.

This is not a change to the intended positive-solution minimum.
The preceding exercises392 and393 explicitly count puzzles with no
solutions, so their use of “puzzle” does not itself exclude this example.
Adding the solvability premise makes the intended domain explicit.
The census and classifications in answer394 were not independently
recomputed by this check.

The original wording and preceding zero-solution questions were inspected
in `images/bookwise-p175.png`. The same statement occurs in the author's
September2019 pre-fascicle, printed111, also visible in its searchable
public copy. No matching erratum or public correction was found; the
scope is in `sources/bookwise-futoshiki-source-check.json`. This is not
a claim of absolute priority.
