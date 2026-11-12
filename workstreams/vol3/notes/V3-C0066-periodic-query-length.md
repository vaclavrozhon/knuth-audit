# V3-C0066 — The periodic-pattern query bound omits the pattern length

Confirmed in volume 3, second edition, first printing (1998), exercise
6.3-40, printed p.511, with its answer on p.727 (file pp.522 and 738).

The exercise permits an arbitrary n-bit query pattern but asks for a
query time O(N), where N is the period length of the fixed text. No
restriction n <= N is stated. The answer invokes Algorithm P, whose
final comparison must also inspect the query.

For the period 01, take a query (01)^t of length n=2t. It occurs at
exactly one starting position per period. Changing any one bit makes
the answer zero, for n >= 4. An exact algorithm must therefore inspect
every input bit on this matching query: an unread bit could have been
changed without affecting its execution. In the ordinary finite-word
model this cannot take time bounded only by the fixed N=2.

The intended query bound can be O(n), retaining O(N) storage. Patricia
tests strictly increasing bit positions, so at most n branching tests
are made, followed by a comparison of at most n bits. The SIZE field
in the supplied answer then gives the count without enumerating all
matching positions. Alternatively, a bound involving both N and n
would avoid the contradiction.

Original exercise and answer checked visually and retained. No matching
correction was located in the official layers or limited public
searches; see `sources/digital-searching-errata-review.json`.
