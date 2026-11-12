# V1-C0010: mathematically supported, already publicly reported

Rechecked on 12 November 2026. The missing convergence hypothesis is real,
but it is not a new finding from this audit.

The question on [Math Stack Exchange](https://math.stackexchange.com/questions/1461642/a-statement-about-harmonic-numbers-from-knuths-the-art-of-computer-programming)
explicitly identifies TAOCP Volume 1, third edition, page 79, exercise 20.
On 2 October 2015, Eric Tressler supplied a positive-coefficient example
using a_n = 1/(n (log n)^2), for n >= 2: the original series converges at
1 but multiplication by the harmonic numbers makes it diverge. Will Jagy
then gave the sufficient repair of placing the argument strictly inside
the convergence disk. Chappers's answer also explicitly identifies the
failure at the boundary. These are public observations of the same missing
hypothesis, rather than merely a citation of the book's formula.

The audit's retained example is stronger in one respect: its right-hand
integrand is continuous while its left-hand series still diverges. That
does not establish novelty of the underlying defect. The earlier argument
and evidence remain archived, but the card is excluded from the new-finding
UI and its original-book error marks. No author acceptance is asserted.

The five relevant official correction layers were refreshed on 12 November
and match the saved corpus. No official correction was located; the reason
for exclusion is the dated public report, not an author-issued erratum.
