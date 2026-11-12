# Bookwise review: multiway trees, 10 November 2026

Reviewed §6.2.4, printed pp.481–491, all ten exercises and answers
on pp.719–721. Shared answer p.721 is deferred to §6.3 for page coverage.

Checked multiway search ordering, ordinary B-tree insertion and root
splitting, minimum occupancy, the height and amortized split bounds,
B+ separators, overflow redistribution, B* three-way splitting and
its exceptional root capacity. Checked the worked insertions, ascending
insertion thresholds, variable-length split examples, deletion and
rank augmentation. Known split-count, wording, reference and 223/233
diagram corrections were excluded.

For exercise 8, checked the probability recurrences, matrix product,
the polynomials g_N and f_N, the characteristic equation, the location
and simplicity argument for its roots, the spectral coefficients, the
harmonic leading term, limiting page categories and resulting page
count. New C0064 concerns the quantity named in the subsequent variance
paragraph, not these calculations.

Limits: the cited variance phase-transition and height theorems, Yao's
B-tree occupancy result, and concurrent-access source protocols were
accepted as external results. No new million-key insertion experiment
or full implementations of the concatenation/concurrency sketches were
made. The exercise 4 root sentence gives a necessary condition ("only
when"), not an exact first-trigger implementation: a proposed objection
assuming an immediate split was not promoted to a finding. The
three-to-four redistribution and its minimum occupancy were checked.

Source screen: `sources/multiway-trees-errata-review.json`.
Next: §6.3, printed p.492 / file p.503, including the pending
cross-reference from exercise 5.2.3-37.
