# Bookwise review: searching an ordered table, 10 November 2026

Reviewed §6.2 and §6.2.1, printed pp.409–426, all 30 exercises and
the answers on pp.705–708. Shared pp.426 and 708 are deferred to
binary tree searching for certification.

Checked binary search's interval invariant and termination, the MIX
instruction counts, successful/unsuccessful path-length identities and
optimal balanced depths. Checked the uniform search increments and
sentinel requirements, asymmetric branch counts, macro-expanded code,
Shar's tree and all 16 rows of its small mean-comparison table.

Checked the Fibonacci-tree recurrence, the two register-swapped inner
loops, their boundary tests and exact average formulas, the extension
to arbitrary table length and the digit/path relation. Checked the
entropy expression for a fixed split ratio and the distinction between
averaging a size and inferring a search depth from that average.

Checked the final-equality variant, complete-tree memory layout,
generating-function variance relation, parallel-comparison lower
bound, corrected Thue-tree composition, involution lookup and the
implicit bit encoding. The earlier binary-insertion forward reference
is consistent with these comparison bounds.

New finding C0058: answer 2's loop example uses K_u where K_l is
needed to address a key that is present, as the exercise requires.
Known changes to the overflow note, index range, typography and Thue
axiom were screened and excluded. Source screen:
`sources/ordered-search-errata-review.json`.

Limits: exercise 6 requests a newly optimized hybrid MIX program and
has no printed answer; no new implementation/optimization was added.
Exercise 19's extended Fibonacci average analysis is not supplied and
was not newly derived. The interpolation-search bounds in exercise 22
were accepted as cited external results in their ordered-table model;
source proofs, empirical timings and historical priority claims were
not independently reproduced.

Next: §6.2.2, printed p.426 / file p.437.
