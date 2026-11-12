# V3-C0065 — Successful digital searches are charged three extra MIX units

Confirmed in volume 3, second edition, first printing (1998), answer
6.3-9, printed pp.722–723 (file pp.733–734).

The printed cost is 10C-3S+4, where C counts comparisons and S is one
for success and zero for failure. A search for the root key executes
only LDX, LD1, JMP, CMPX, JE, costing 2+2+1+2+1 = 8 units. Here C=S=1,
but the formula gives 11.

The full instruction sum is

    5 + (C-1) + 3C + 3(C-S) + 3(C1+C2)
      = 10C-6S+4,

because C1+C2=C-S. The terms account respectively for initialization,
ENT1, comparison and success test, binary shift and direction test,
and link load and null test. Thus replace -3S by -6S. The successful
asymptotic timing in the table changes from 14.4 ln N-6.17 to
14.4 ln N-9.17 under the same rounding; the unsuccessful timing is
unchanged.

Original pages checked visually and retained. No matching correction
was located in the official layers or limited public searches; see
`sources/digital-searching-errata-review.json`.
