# Bookwise review: reading tape backwards, 10 November 2026

Reviewed §5.4.4, printed pp.299–311, all 26 exercises and their
answers on pp.685–691. Shared pages 311 and 691 continue into the
oscillating sort and are deferred to that next certification block.

Checked the alternating-direction distributions and merge-number
recurrences, the run-vector model, the forbidden LIFO configurations,
and their connection with growing the most recently formed leaf.
The diagrams on pp.304–307 and the small seven-run example were
examined in the original scan. Karp's preorder construction and its
answer-12 proof use the special tape name only on a leftmost branch;
this excludes the remaining external-branch crossover. The external
path-length lower bound follows from the stated complete-tree result.

Read the six tree species and recurrences in answer 15 together with
the staged construction, parity restrictions and the additive linear
bound. The induction is used in its stated range n >= 4. Checked the
even-pass cascade distribution in answer 17 with the known correction
to its first column. The FIFO and strong-FIFO forbidden configurations,
the replacement condition in answer 22, and the stage/phase
majorization proofs in answers 23–25 were checked. In particular,
the latter maximize the component sums by consuming the largest
available output counts; they do not assert that every optimum has
the displayed special form.

No new finding. Known corrections include the growth-step wording
on p.305, polyphase's path length 180 (not 176) in answer 7, the
last summand in the answer-17 recurrence, the list of intermediate
vectors in answer 23, and the reference to exercise 23(c) in answer 25.

Limits: the optimum table K_T(n), the assertion of the first Fibonacci
improvement, and the complete list of undominated strategies for
T=4,5,6 were not independently enumerated. The large trees in answers
7 and 21 were inspected, not transcribed into an exhaustive checker.
Exercises 10, 14, 16 and 26 are computational/research projects and
were not solved. The tape-reversal lower bound in answer 18 is a
sketch; its bounded-memory path-count premise is retained for checking
against the explicit model in §5.4.8, without inventing a new lower-bound
proof. Historical performance comparisons were not reproduced.

Source screen: `sources/backwards-errata-review.json`.
Next: §5.4.5, printed p.311 / file p.322.
