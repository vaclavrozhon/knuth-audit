# V3-C0072 — The Bernoulli expansion of tanh(z/2) is missing a factor of two

Confirmed proof error in volume 3, second edition, first printing
(1998), answer 6.3-33, printed p.727 (file p.738).

The last displayed series for f(z)=tanh(z/2) omits an overall factor
2. Its printed coefficient of z is

    B_2 (2^2-1)/2! = (1/6)*3/2 = 1/4,

where B_2 is the second Bernoulli number. But f'(0)=1/2. The preceding
expression 1-2 z^(-1)(z/(e^z-1)-2z/(e^(2z)-1)) is correct and gives
the missing factor when expanded.

Multiply the series by 2. Equation (18), which the answer is intended
to derive, is consistent with the corrected expansion. The May 2026
replacement concerns answer 34 and does not alter this line.

Original p.727 and an enlarged crop checked and retained. No matching
correction was located in the official layers or limited public
searches; see `sources/digital-searching-errata-review.json`.
