# Merge sorting — 10 November 2026

Reviewed §5.2.4, printed 158–168, all 23 exercises and their answers
646–650. Original flowcharts, tables and MIX listing were inspected.
The previously reviewed selection exercises on shared pages158/646
are included in the page certification below.

Algorithms M, N and S were checked together with the overlap and short
run arguments. In N6/N10 the strict stepdown separates the two cursors;
in S the longer run's final key acts as the sentinel when a short run
has been artificially extended. The two-pass example in answer6 agrees
with accidental coalescence of runs. The list version L preserves
sublist signs, distributes complete output runs alternately, and handles
an unmatched last sublist at L8. Its stability is consistent with
merging contiguous groups of original positions, even though the two
initial linked lists contain odd and even positions.

The instruction-frequency sum matches answer13. Its N=16 numerical
substitution is 761u. The ordinary/special merge-size decomposition,
independence of random interleavings, tail probabilities in answer2,
mean costs and maximum-comparison formula were checked. The limiting
coefficient 12.5-6 alpha' is consistent with the rounded 4.92 in the
main text; all displayed high-precision digits were not recomputed.
Known corrections to the duplicated-loop optimization (18 copies,
variables p,q,s and 8N lg N) were applied.

The Kronrod construction in answer18 was checked through zone ordering,
the exchange-based merge and final cleanup. Its inversion statement
counts larger predecessors of a key; reading it instead as the number
of smaller successors would be a misinterpretation. The displayed
exchange example agrees with the claimed auxiliary-record permutation.
The stack construction in19 is a valid inductive merge construction.
For21, maintaining the number of unconsumed left-run records counts
cross inversions when a right-run key is selected; earlier levels count
the within-run inversions. The online binary-counter merge in17 and
the balanced-tree worst-case argument in23 agree with their recurrences.

New finding **V3-C0035**: the exact per-output comparison bound in
answer1 uses floor(lg k) where the selection-tree bound needs a ceiling.
The separate note gives a five-stream counterexample.

Explicit limits: no new MIX implementation for exercise9 or three-way
implementation for16 was constructed; the latter's speed comparison
remains model dependent. Answer10's safe-overlap merge was checked,
but its cited complete memory schedule was not reconstructed. The
bibliographic-only multiword-key algorithm in22 was not retrieved.
Research exercise20 is excluded. The cited Mellin-transform and limit
law results in23, historical priority claims and independent benchmark
reproductions are outside this review; the printed local recurrence
and worst-case reduction were checked. No broad calculation was run.

All five errata layers were screened, including the 2024 wording change
in answer18; see `sources/merging-errata-review.json`. Known corrections
do not create finding cards or red markers.
