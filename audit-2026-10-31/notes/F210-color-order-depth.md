# F210: An extra q multiplies the search depth in answer 178

Volume 4B, answer 7.2.2.2–178, printed 582 / PDF 602.

The color-first ordering in the question lists the color-one variables
of the six vertices in block 1, then those of block 2, and so on. Its
prefix covering k blocks therefore has **6k** variables, not the printed
6kq. Delete the extra q. At k=q, the whole first color layer has 6q
variables and its independent-set count has growth Omega(10.2^q),
consistent with answer 177 and the intended comparison.

This is not merely a different convention for depth: there are only
18q Boolean variables in the whole instance. For example, q=5,k=4
would make the printed prefix 120 levels long, exceeding the entire
90-variable search. The intended prefix has 24 variables.

The typo does not invalidate the intended exponential separation of
the two variable orderings, and the reported benchmark runtimes were
not independently reproduced. Original image
`images/bookwise-snark-p582.png` and the author's 2015 draft printed
218 / PDF 226 both show 6kq. No matching correction was found in the
inspected current/historical 4B and Fascicle 6 errata.
