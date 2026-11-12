# F191 — the simple-path recurrence may revisit its start

Volume4B, first edition, second printing (November2022), §7.2.2.1,
answer405, printed534 / file554.

Let v be the fixed starting vertex. A state (S,u) at level l records
the l vertices visited after v and the current endpoint u. The initial
state is (empty set,v). A simple path has no repeated vertex.
The printed transition requires a neighbor w of u with w not in S,
then adds the state (S union {w},w). It must also exclude w=v.

For a graph consisting of the single edge v—u, the printed recurrence
produces

```
level0: (empty set,v)
level1: ({u},u)
level2: ({u,v},v).
```

The last state represents v,u,v, which is not a simple path. There is
no simple path of length2 in this graph. The reason is that the start
vertex is not in S initially and is never inserted until the erroneous
return occurs.

Replace the transition condition by **w not in S union {v}**.
This corrects the subroutine requested in405. In its use as a necessary
feasibility filter in404, the error can admit extra candidates; it does
not by itself show that the final exact-cover solver accepts an invalid
Hamiltonian path.

The original recurrence was inspected in `images/bookwise-p534.png`.
The author's September2019 pre-fascicle, printed238, has the same
transition. The relevant current and historical errata contain corrections
to404 but none to this recurrence. Public searches found no matching
report, without establishing absolute priority; the search scope is in
`sources/bookwise-kenken-hidato-source-check.json`.
