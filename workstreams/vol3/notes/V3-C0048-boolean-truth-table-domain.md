# V3-C0048 — A t-variable truth table has domain D_t

Confirmed in volume 3, second edition, first printing (1998), answer
5.3.4-32, printed p.669, file p.680. The domain of the represented
function `f(x_1,...,x_t)` is printed as `D_(2t)`. It should be `D_t`.

The book defines D_n to be the set of n-component 0–1 vectors. An element
of G_t is a string of 2^t bits, one bit for each t-bit argument. The
answer's own correspondence evaluates f at `(x_1,...,x_t)` using the
entry indexed by that t-bit address. For t=2, there are four entries
indexed by 00,01,10,11, not the sixteen arguments of D_4.

The original subscript was visually checked; see
`images/bookwise-p669.png`. Existing errata correct G_T to G_t and other
notation in the same answer, but leave this domain unchanged. The five
official layers were screened in `sources/networks-errata-review.json`.
A targeted public search found no report of this domain correction;
absolute priority is not claimed.
