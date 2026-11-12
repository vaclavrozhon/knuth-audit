# Domain representations and exercises 298–306

Read main printed 57–60, questions 298–306, and their complete answers
223–225 together. The original pages 142, 223, 224 and 225 were inspected
where figures, subscripts or the new finding required it. Known corrections
to 299, 305, 306's question, G3 and the asymptotic commentary were applied.

Figure 117's trail and stamp changes restore the displayed states; keeping
stamps monotone explains why repeated parent updates can produce multiple
trail entries. In 299, reusing a depth as the stamp loses the y=5 restoration,
whereas fresh node stamps plus restoration of both value and stamp work.
The corrected separators in its example are 1 and 5, not 5 and 7.

The bit masks (95)–(100), ordered circular lists (101)–(105), inverse sparse
permutations (106)–(110), and their four operations were checked. Deletion
swaps a live element into the suffix and preserves both inverse identities;
restoring SIZE recovers the set without restoring order. The deleted suffix
also provides the recent deletions used by 305. For 300, deleting a live
successor cannot move NEXT(a) past another still-live a'. The initializations
and minimum queries in 301–302 follow from these representations. The extra
leading digit in 303 when e divides d is naturally zero by (111); this is
not promoted as a finite-array indexing objection.

The two-ended partition in Algorithm R changes only out-of-place indices,
trails changed nonzero words and the prefix length, and restores the logical
set correctly. Its deliberate lazy treatment of inactive words is compatible
with active-prefix scans. It is incompatible with the later unchecked
residual cache: F7-C0015 gives a direct two-word counterexample. Apart from
that shortcut, 305's two masks remove exactly the invalid tuples, and a
single filtering pass suffices because removing an unsupported value cannot
invalidate any surviving tuple. The published singleton correction is needed
for empty-table failure detection.

For 306, s is one plus the lowest intervening level since the preceding
backward visit at that level, or zero when no such visit exists. This reading
checks the displayed table and explains the interval update: a new valley
creates an interval, upward steps lower its left end, and equal left ends
coalesce. The path in (c) realizes the six intervals in 53 steps; the sum of
their lengths is 20 and the final left endpoint is 14. Both paths in (d) have
the stated support-history values and sum 107. With corrected G3 (k=s_t),
G2 reuses a failure only within the unchanged prefix, while G4 tests every
newly relevant relation. A successful mark j does not masquerade as a
cached failure. No new algorithm defect was found here.

In 298 the 9+4+7 classification and the illustrated placement were read
with the earlier Volume 4B symmetry discussion. The encoding example and
the factor-eight symmetry restriction agree with that discussion. The
complete shape enumeration, detailed cell-by-cell transcription of all
twenty placed pieces, the 16928 count and uniqueness search were not
independently repeated. These are explicit finite-census/figure exceptions,
not claims of a new exhaustive packing verification.

Further exact exceptions: the 306(e) Catalan-weighted numerical census,
the new asserted 6m^2/11+O(m) maximum, million-sample statistics in 306(f),
and the external general asymptotic results are accepted as cited results
or recorded computational claims, not independently reconstructed. No
random experiment or search census was launched. The newly supplied
generating-function supplement is addressed when reviewing the appendices.
Historical priority and the full external Compact-Table survey are outside
this printed-argument check.

Only complete pages 72–75, 157 and 238–239 are newly certified in this block.
Answers 306 on file 240 are reviewed, but that page also contains later
answers and remains gray until those are reviewed. File 158 similarly
contains questions 307 onward. The completed first-half review supplies
the already covered answers 296–297 on file 238.
