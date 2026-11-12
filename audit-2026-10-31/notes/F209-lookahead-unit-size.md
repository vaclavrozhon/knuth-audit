# F209: Decrement the virtual clause size in the unit case too

Volume 4B, answer 7.2.2.2–175, printed 581 / PDF 601, restored on 582.

The proposed update sets s←CSIZE(c)−1 but writes CSIZE(c)←s only when
s≥2. In contrast, its restoration loop increments CSIZE(c) for every
processed false literal. A shortening that reaches a unit or conflict
therefore gets undone even though it was never recorded in the count.

Set **CSIZE(c)←s immediately after s←CSIZE(c)−1**, before testing s≥2.
Only the heuristic weight increment belongs inside the s≥2 branch.
The same correction applies to the analogous double-lookahead update.

For a concrete local example, use the clause (a OR b OR c) and the
binary implication not-a→not-b. Looking ahead with not-a processes
not-a and not-b, then forces c. The first false literal changes the
count 3→2. The second has s=1, but the printed instruction leaves the
stored count at two. When a later higher truth context expires these
assignments, restoration increments for not-b and not-a, giving 2→3→4.
The original three-literal clause has acquired an incorrect count four.
The unconditional decrement instead gives 3→2→1, then 1→2→3 on undo.

The fixed trace in `check_bookwise_sat175.py` already preserves inherited
stack prefixes, so this defect is independent of F208. Results are in
`results/bookwise-sat175.json`. This is a local count-invariant witness,
not a claim about an unmodified whole solver's ultimate answer.

The original page image and 2015 draft printed 217 / PDF 225 have the
same conditional update. The official SAT11K code assigns the decremented
`cinx[c].size` before its `ls>=2` test, in both lookahead routines.
No corresponding correction was found in the inspected 4B/Fascicle 6
errata.
