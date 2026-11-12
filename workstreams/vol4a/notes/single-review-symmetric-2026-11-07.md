# Boolean structure, thresholds and symmetric functions — reviewed

7 November 2026. Accepted completed work on printed 72–77 and the paired
threshold/symmetric exercises through 115. The sole zero-coordinate/empty
graph convention on 72–74 is excluded under the user's explicit policy;
it no longer blocks otherwise complete pages. No graph enumeration is run.

The unfinished exercise 116 was read with its original statement on 94 and
answers 556–557, including visual inspection of 557. The implicant test
matches its reachable weight interval; maximal one-runs give the stated
multinomial count. For S3,4,5,6 with nine variables the count is
9!/(3!3!3!)=1680. The saved ten-row dynamic program and its last-run recurrence
confirm 1698 for 1101111011; that witness has run contributions 9+1680+9.
No rerun or truth-table enumeration was made.

The printed Stirling asymptotic has the expected balanced-trinomial leading
term 3^(n+3/2)/(2πn). The saved separation argument makes other runs
exponentially smaller. The existence claim in part(e) uses runs with
proportions approaching (1/4,1/4,1/2); applying the standard Stirling formula
is sufficient and its proof is not rebuilt. The displayed n=9 example
S0,2,3,4,8 and its complement both have 766 prime implicants: respectively
1+756+9 and 9+756+1.

Explicit exception: the stronger universally optimized closed recurrences
in answer116(c),(e), the claim that they globally maximize the smaller of
the two counts, the full 13-value sequence, and its exact parity-dependent
constant have not been independently established. Completing those missing
lower/upper-bound arguments was already substantially longer than an
ordinary exercise review. They are retained as a named exception, not
silently declared proved. Original historical references in116 are not
independently checked. No new mathematical error was found.

Questions112–116 on94 and the entire answer page556 have been reviewed
using the accepted prior112–115 evidence plus this116 check. Answer557 is
not newly certified as a whole: it also contains117–118, outside this block.
Main78 remains gray for its unreviewed canalizing/classification material;
reading its parity continuation alone does not complete that page.

Evidence: `proof-099-symmetric-threshold-parity.md`,
`proof-100-symmetric-primes-WIP.md` (preserved as historical draft),
`results/symmetric116-n9-dp.json`, accepted threshold/Chow proof notes,
and original images `proof-file573.png`, `proof-file574.png`, `file111.png`.
All4a-pre/all4a/err4a/all4f0/err4f0 checks from the saved draft are retained.
The old demand to register a separate new proof item for every step is
superseded by the printed-argument review standard.
