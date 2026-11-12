# Bookwise review: disks and drums, 10 November 2026

Reviewed §5.4.9, printed pp.356–379, all 31 exercises and their
answers on pp.696–701. Shared answer p.701 continues into §5.5 and is
deferred to that certification block.

Checked the seek, rotational-latency and transfer model; replacement
selection and merging examples; the dynamic recurrence for merging
trees with cost alpha*D+beta*E; the convexity argument and balanced
ternary constructions in Theorem L; and the smallest-subtrees
transformation in Theorem M. Its degree bound uses a ceiling, as the
original typesetting confirms. Checked the square-root allocation
of unequal buffers and its cost comparison.

Read SyncSort with the official replacement paragraphs, followed by
superblock striping, the Gilbreath construction and randomized
striping. Checked the lookahead-key requirement in answer 22, the
input/output-buffer accounts and the chronological inversion count
in answer 24. New finding C0056: the final optimal-buffer formula
mis-simplifies the gcd term. The preceding argument and construction
remain valid.

Checked the elevator potential argument, the configuration-counting
bound and its average-case extension, the backwards replacement
selection explanation for keysorting, the cyclic-occupancy generating
function, the optimized tail bound, the marked-block grouping argument
and its asymptotic estimate. Manually followed the eleven-stop sequence
in answer 16. The answer-12 tree-level convention prompted a cross-check
of the preceding radix section, resulting in C0055 and a correction to
that block's initial assessment.

Known corrections were excluded: the figure reference on p.356,
the qualification on p.360, the formula reference in Theorem M,
the SyncSort replacement and later grammar repair, the parallel-I/O
qualifications, h_1 on p.371, the subscript in exercise 7, the cyclic
occupancy wording, the symbols in answer 9 and the qualification in
answer 15. Source screen: `sources/disks-errata-review.json`.

Limits: historical hardware timings and the full numerical tables
were not independently reproduced. The cited external optimum and
I/O-complexity theorems were accepted as cited; their source proofs
were not reconstructed. The parity-constrained tree census, the
partitions in answer 14 and the impossibility of a ten-stop solution
in answer 16 were not independently enumerated. Exercises 28 and 31
are research questions, not newly solved. The lookahead mechanism
closes the forward reference from 5.4.6-12(a), but its claim of an
exact minimum without lookahead remains the explicitly recorded
unexpanded argument from the tape-merging block.

Next: §5.5, printed p.380 / file p.391.
