# V2-C0001: an already acknowledged typo in the 2026 division erratum

Reviewed on November 12, 2026. The mathematical counterexample is valid, but
this finding must not be presented as a new report.

In the replacement Theorem B on page 271, the necessary condition uses the
second digit `v_1` instead of the leading digit `v_(n-1)`. For base `b=3`,
length `n=3`, dividend `u=45` and divisor `v=16`, the true quotient digit is
2 and its estimate is 5. The leading digit is 1, but `v_1=2`. The seven
incorrect subscripts remain visible in the current public correction files;
the November 12 refresh agrees with the archived copies. The original
typeset correction was inspected again.

However, Novak Kaluđerović's first-person article
[A long division story](https://kolja.rs/algorithm-d/), dated August 13,
2026, explicitly identifies this very subscript typo and states that it has
already been acknowledged. The surrounding account distinguishes the
original division defect, the May 14 correction, its June 9 publication,
and this typo in the correction. This is an exact prior public match, not
an inference from a related division bug.

Decision: retain the argument as historical evidence; classify the finding
as previously publicly discussed and remove its new-finding card and red
page marker. The public article establishes a prior report even though the
downloadable correction has not yet been updated. No private communication
was used or sent.

Searches included `Knuth Algorithm D erratum v1 vn-1`, the article title,
and the article's explicit discussion of the correction typo. The primary
article was opened and read in context; a repost was not used as independent
evidence.
