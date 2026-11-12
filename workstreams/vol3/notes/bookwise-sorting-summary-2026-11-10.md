# Bookwise review: sorting summary and history, 10 November 2026

Reviewed §5.5, printed pp.380–391, all five exercises and the printed
answers on pp.701–702. Shared answer p.702 is deferred to §6.1.

Compared the algorithm classifications, stability, storage and leading
time estimates with the sections already reviewed. The table explicitly
qualifies its measurements and assumptions; the radix average retains
the appropriate large-N leading terms despite C0036's empty-pile issue.
Checked the six-buffer overlap invariant in the historical account.

For answer 3, checked that the reversals restore the order within each
median block, leaving two subproblems of size at most N/2. This yields
stable merging in O(N log N) time and the stated sorting bound, with
O(log N) index words, hence O((log N)^2) bits. Checked answer 4 against
the actual insertion and list-merge comparison branches; list merging
starts with singleton runs, not a redundant natural-run prepass.

No new finding. Known changes to the bubble-sort assessment, hybrid
wording, empirical shellsort exponent, history and merging hint were
screened and excluded. Source screen:
`sources/sorting-summary-errata-review.json`.

Limits: the historical bibliography, priority claims, benchmark timings
and complete MIX timing table were read but not independently sourced
or rerun. The cited optimal stable in-place algorithms were accepted
as external results; their full proofs were not reconstructed.
Exercise 5 asks for a research benchmark and was not newly solved.

Next: chapter 6, printed p.392 / file p.403.
