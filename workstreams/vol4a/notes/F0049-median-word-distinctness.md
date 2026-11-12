# V4A-F0049: The median-word definition omits a required exclusion

Confirmed, low severity. Volume4A, first edition, first printing
(2011), exercise7.1.4-223, printed275 / file292. Original:
`images/bookwise-p275.png`; compare answer223 on666–667.

The definition requires exactly two of three input words to agree
with the resulting word mu at each position. It does not require
mu to differ from each input. Part(a), however, claims that the
three Hamming distances must be {1,1,3} or {1,2,2}. Hamming distance
is the number of positions in which two words differ.

Take mu=while and the three distinct input words

    alpha = while
    beta  = whale
    gamma = stiff

At positions1,2,4,5, alpha and beta agree with mu; at position3,
alpha and gamma agree with mu. Thus the printed definition holds
at every position, but the distances are {0,1,4}.

The coordinate condition proves only that the distances sum to five.
Adding mu != alpha, mu != beta, mu != gamma makes all three positive
and yields the two partitions asserted in(a). This is also the
intended condition explicitly imposed by the algorithm in answer(b)
on666, and by the phrase about three other words on667. Its numerical
census was not recomputed. The proposed repair is to put that
exclusion into the exercise's definition.

The original, current/historical 4A/Fascicle1 errata and targeted
public reports were checked; no matching correction was located.
See `sources/zdd-dictionaries-paths-source-check.json`. Absolute
novelty is not established. No dictionary census or code was needed
for this ordinary-word counterexample.
