# F248 — An unconditional quenching clause can eliminate every solution

Confirmed in Volume 4B, answer 485, printed 645/file 665; author draft 281.
A q_k move deletes the left vertex of the adjacent pair at positions k,k+1;
a s_l move captures position l with position l+3 and brings the latter to l.
Both require an edge between the two participating vertices. Write t'=t+1.
The last allegedly unconditional interchange is

    (s_(t,l), s_(t',l))  <->  (q_(t,l+3), s_(t',l)).

For consecutive vertices a,b,c,d,e starting at l, both sides finish at
(e,b,c). Their edge requirements differ: the left needs a--d and d--e;
the right needs d--e and a--e. Neither implies the other. In particular,
the printed clause

    (not q_(t,l+3) or not s_(t',l))

is unsound without a guard for a--d.

A five-vertex counterexample has ordered vertices (1,2,3,4,5) and edges
{15,23,25,45}. Its only winning sequence is

    q_4, s_1, q_1, q_1:
    (1,2,3,4,5) -> (1,2,3,5) -> (5,2,3) -> (2,3) -> (3).

The printed clause for t=0,l=1 forbids its first two moves. To see uniqueness,
the initial legal moves are q_2, q_4 and s_2. Starting with q_2 or s_2
leaves a dead position; after q_4, the only successful next move is s_1,
followed by q_1 twice. The fixed-graph check records this entire tiny search
in results/bookwise-quenching485-fixed-graph.json. No graph census was run.

This is also a defect for card graphs: add edge 12 to the same example.
The graph is realized by the five cards

    ace of hearts, king of hearts, king of clubs, queen of diamonds, queen of hearts.

It still has precisely the same unique winning sequence, also excluded by
the printed clause. This does not assert that a particular printed 18-card
UNSAT instance was misclassified.

Move this interchange into the conditional group and replace its clause by

    (not q_(t,l+3) or not s_(t',l) or not x_(t,l,l+3)).

Here x_(t,l,l+3) is exactly the missing a--d edge. When the right-hand
sequence and this edge exist, the preferred left-hand sequence is legal
and reaches the same ordered graph. The replacement reduces the first
move's index, so it fits the decreasing order used by the other reductions.
The two other conditional interchanges printed in the next paragraph
already contain their required guards.

The archived official SATexamples program has the same defect in
sources/bookwise-sat-graph-quench-noncomm-latebinding-random.ch: the loop
starting j=i+3 emits the unguarded Q/S clause. Its first iteration should
be guarded; the disjoint cases j>=i+4 remain unconditional. Provenance and
archive hash are in the source-check record. Both explicit 18-card winning
paths in answer 486 were separately traced and remain valid; reported
UNSAT benchmarks were not rerun.

The original Volume 4B typesetting and the September 23, 2015 author draft
were inspected. Relevant current/historical 4B and Fascicle 6 errata,
including available TeX sources, contain no matching correction. Focused
public searches found no matching report, without establishing absolute
priority. See sources/bookwise-quenching-symmetry-source-check.json.
