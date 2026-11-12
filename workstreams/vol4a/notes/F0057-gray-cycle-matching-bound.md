# V4A-F0057: The matching bound loses the cycle orientation

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), exercise 7.2.1.1-44, printed 313 / file 330. Originals:
`images/bookwise-p293.png`, `images/bookwise-p313.png`, and the
supporting answer in `images/bookwise-p686.png`.

On page 293, d(n) counts delta sequences of Gray cycles starting at
the all-zero vertex, with the direction distinguished. A delta
sequence lists the coordinate changed on each edge. The text gives
d(2)=2: the two sequences are 0101 and 1010.

Exercise44 asks for the bound d(n) <= binomial(M(n),2), where M(n)
counts perfect matchings of the n-cube. But the square has exactly
two perfect matchings, its two pairs of opposite edges. The claimed
inequality therefore reads 2 <= 1.

Alternating edges of a cycle give an unordered pair of perfect
matchings, as the answer observes. That pair determines the cycle's
edges but not its direction. For n>=2, the valid bound is

    d(n) <= 2 binomial(M(n),2) = M(n)(M(n)-1).

The weaker bound d(n)<=M(n)^2 also covers the book's one-bit case.
Use an ordered pair of alternating matchings, with the first one
containing the first edge out of zero, to make the injection explicit.
The asymptotic upper estimate in answer47 is unchanged by this repair.

No correction was found in the screened current/historical 4A and
Fascicle2 errata or targeted public reports. The 2009 Fascicle2
replacement introduces the same bound and does not repair this
orientation issue. See `sources/gray-cycles-source-check.json`.
Absolute novelty is not established. The square was checked by hand.
