# V3-C0077 — The double-hash comparison halves the cost of extra probes

Confirmed in volume 3, second edition, first printing (1998), answer
6.4-18, printed p.731 (file p.742), compared with Program D and
modifications (30), (31) on pp.530–531.

The answer charges 3(A-S1) extra time units for modification (31)
but credits only 4u times the difference in expected probe counts.
Here u is the MIX time unit, A counts nonempty first probes, S1 counts
successful first probes, and C is the total probe count. Program D
has an 8C term, as the book's explicit total on p.531 correctly states.
Both modifications replace only the calculation of the second hash;
neither changes that probe loop.

Let deltaC=E[C_30]-E[C_31] and deltaB=E[B_31]-E[B_30], where B counts
the wraparound increment in Program D. Under the comparison's common
values of E[A] and E[S1], subtraction of the two instruction totals gives

    E[T_31-T_30]/u = 3 E[A-S1] - 8 deltaC + deltaB.

Thus the contribution of fewer probes is 8u times deltaC. The wraparound
term must be treated separately; it does not change the loop's coefficient
to 4. A further unsuccessful nonfinal probe executes instructions
15,16,18,19,20,21 at costs 1+1+2+1+2+1=8, before any wraparound.

The stated 94%/71% thresholds and maximum half-unit saving consequently
cannot be justified by this calculation. This finding does not propose
universal replacement thresholds: the distribution and range of the
second hash affect B and the accuracy of the probing models.

Original pp.530, 531 and 731 inspected. The first-edition errata already
give the 8C total, but do not repair answer 18. No matching answer
correction located in the screened sources; see
`sources/hashing-errata-review.json`.
