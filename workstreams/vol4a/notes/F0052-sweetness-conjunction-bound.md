# V4A-F0052: Wrong range in the sweetness recurrence

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), answer 7.1.4-247, printed 674 / file 691. Original:
`images/bookwise-p674.png`.

The recurrence tests sweetness, meaning that the BDD of a monotone
Boolean function is the same diagram as the ZDD of its family of
prime implicants. Its conjunction uses x_(2j+1) and x_(2i+2), with
the printed range

    0 <= i < j <= 2^(k-1),  i bitwise-and j = i.

Here k is undefined. There are 2^n input entries, partitioned into
2^(n-1) odd-indexed and 2^(n-1) even-indexed entries. Thus i and j
must range from 0 through 2^(n-1)-1. The upper bound should be
`2^(n-1)-1`, not `2^(k-1)`. Merely replacing k by n still allows
an index beyond the 2^n inputs.

The condition i < j encodes strict inclusion of the corresponding
subsets, as required by Theorem S. The separately displayed odd/even
arguments are naturally read as interleaved subsequences. The input
entries can encode membership in a prime-implicant family: for n=1,
the accepted vectors 00, 01 and 10 then represent the three sweet
functions. There is no additional finding about that base case or
about the printed enumeration totals.

No matching correction was found in the screened 4A/Fascicle 1
errata or targeted public reports. See `sources/zdd-tail-source-check.json`.
Absolute novelty is not established. No census was rerun.
