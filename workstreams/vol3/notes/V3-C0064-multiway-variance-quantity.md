# V3-C0064 — The variance paragraph changes the meaning of storage utilization

Confirmed quantity mismatch in volume 3, second edition, first printing
(1998), answer 6.2.4-8, printed p.721 (file p.732).

The preceding calculation gives the number of pages and then the
asymptotic storage utilization 2(H_(M+1)-1)/M, a fraction of occupied
key positions. The next paragraph attributes a variance of order N
(and, for larger M, a superlinear variance) to this storage utilization.

Let S_N be the number of allocated pages, each having M key positions,
after N keys have been inserted. The utilization fraction is
U_N = N/(M S_N). Since 0 <= U_N <= 1, its variance is at most 1/4.
It therefore cannot have the stated growth as N increases. This already
contradicts the linear assertion for any fixed 2 <= M <= 25; no limiting
calculation or exceptional empty structure is needed.

The cited primary article is H. M. Mahmoud and B. Pittel, *Analysis of
the space of search trees under the random insertion algorithm*,
J. Algorithms 10 (1989), 52–75. Its abstract explicitly identifies the
random variable as the space occupied by the tree, with linear variance
for branching factors 3 through 26 and superlinear variance above 26.
Its branching factor is m = M+1 in the book's notation.
[Publisher's abstract](https://www.sciencedirect.com/science/article/pii/0196677489900230).

Change the paragraph's quantity to the number of pages (space occupied),
retaining the cited phase transition. This note does not claim a new
asymptotic formula for the variance of the utilization fraction.

Original p.721 was checked visually and retained. All five official
errata layers and limited public searches were screened; no matching
correction was located. See `sources/multiway-trees-errata-review.json`.
