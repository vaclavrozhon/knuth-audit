# V4A-F0033: The no-solution guard rejects the false function

Confirmed, low severity. Volume 4A, first edition, first printing
(2011). Answer 7.1.4-9, printed page 622: initial test of s.

The exercise asks for the lexicographically largest bit vector x with f(x)=0.
In the sequential representation on page 207, the identically false
function has s=1 and root 0; the identically true function has s=2 and
root 1, with the otherwise unused false sink retained.

The printed answer instead begins by declaring no solution for s=1.
For f=0, every vector is a solution and the required answer is the
all-ones vector. For f=1, s=2 passes the guard and the traversal reaches
node 1, although its only stopping test is k=0.

Replace the initial condition s=1 by s=2. Then the false-function case
sets the n variables to 1 in step (i) and stops at k=0 in step (ii).
This is an explicit reversal of the printed constant-case test, rather
than a demand for an unstated exceptional convention.

Original page images and the relevant current/historical Volume 4A and
Fascicle 1 errata were checked. No matching correction or public report
was located; absolute novelty is not established. See
`sources/bdd-basics-source-check.json`. The counterexample was checked
by hand; no general verifier or census was used.
