# V3-C0060 — The AVL search count must always include the root

Confirmed local counting-definition error in volume 3, second edition,
first printing (1998), §6.2.3 p.470, equation (15), with the frequency
annotations of Program A on pp.464–465.

The parameter D is defined as the number of encountered nodes with
nonzero balance factor. But the program's root initialization executes
line 13 once even when the root's balance factor is zero. Thereafter
lines 12–13 execute exactly when a nonroot node has nonzero balance.
Consequently the displayed frequencies D-1 and D, and equation (15),
need D to mean one plus the number of such nonroot nodes.

For a concrete example, take the three-node tree with root key 2 and
children 1 and 3, and search for 2. All balance factors are zero.
With the printed definition, C=C1=S=1 and D=0. Equation (15) gives
10 time units. The actual instruction sequence is

    04,05,06,07,13,14,15,16,17
    2 +1 +2 +1 +1 +1 +2 +1 +1 = 12 time units.

The frequency D-1 printed beside line 12 would even be negative.
Defining D as one plus the number of encountered nonroot nodes with
nonzero balance factor fixes both annotations and equation (15).
Alternatively, retain the definition and add 2 time units to (15)
whenever the root is balanced.

This affects the exact count, not the search algorithm or logarithmic
complexity. Original pp.464, 465 and 470 were visually checked.
All official layers and targeted public searches yielded no matching
correction; source screen `sources/balanced-trees-errata-review.json`.
