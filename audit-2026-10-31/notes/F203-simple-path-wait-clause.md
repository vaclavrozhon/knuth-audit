# F203: Deleting a waiting clause permits illegal jumps

Volume 4B, answer 7.2.2.2–92, printed page 567 (PDF page 587).

The answer correctly excludes repeated global states when searching
for a simple path. It then recommends deleting the entire clause for
Bob's waiting branch at B1. This loses the branch's guard: Bob can
jump to any other state when the light is on, rather than wait.

Write a state as (Alice's program counter, Bob's program counter, light).
The following path consists of distinct states and starts at the
specified initial state:

    (0,0,0) -> (1,0,0) -> (2,0,0) -> (3,0,1) -> (3,1,1) -> (3,3,1).

The first three steps bump Alice, and the last two bump Bob. The final
step is illegal: B1 with light=1 must remain at B1. Yet this path
satisfies all the other transition clauses, all one-state constraints,
and the distinctness condition. Its sole violated original clause is
exactly the one the answer says to delete. It even reaches simultaneous
critical states in five steps; the real programs require at least six.

Remove only the successor literal B1_(t+1), obtaining

    @t OR NOT B1_t OR NOT l_t.

This guard rejects scheduling Bob while he would merely wait. Equivalently,
keep the original waiting clause and let the distinctness constraints
exclude the self-loop. Deleting the whole implication does neither.

The original typesetting and the author's 2015 draft (page 203) agree;
no matching current 4B/Fascicle 6 erratum was located. The fixed-path
checker evaluates all 150 original transition clauses and identifies
the unique failure, while the modified 145 clauses all hold. No general
protocol-state enumeration was performed.

Evidence: `check_bookwise_sat92.py`, `results/bookwise-sat92.json`,
`images/bookwise-protocol-p567.png`, and the D237 source-check manifest.
