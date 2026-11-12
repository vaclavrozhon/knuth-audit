# V4A-F0051: A valid blocker identity is crossed out

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), answer 7.1.4-236(d), printed 669 / file 686. Originals:
`images/bookwise-p276.png` and `images/bookwise-p669.png`.

For a finite family f of sets, write f# for its blocker: the family
of inclusion-minimal sets that meet every member of f. Write f join g
for the family of unions A union B, with A in f and B in g, and min(f)
for the inclusion-minimal members of f. Exercise (xvi) asserts

    (f union g)# = min(f# join g#).

The left operation in the original is ordinary family union; the
right one is the square union symbol for join. The answer incorrectly
crosses out (xvi) and says it fails when either family is empty.

The identity holds for all finite families. A set hits f union g
exactly when it hits both families. It then contains a minimal hit
A of f and a minimal hit B of g, and A union B is itself a hit of
both. Taking minimal members on each side proves the assertion.
An empty family has blocker {empty set}, which is the join identity.
A family containing the empty set has empty blocker; in that case
both sides are empty. Neither case introduces an exception.

Remove (xvi) from the crossed-out list and remove its claimed
exceptions. This corrects the classification of a general algebraic
identity, not a proposed change of convention for an empty object.

No matching correction was found in the screened 4A/Fascicle 1
errata or targeted public reports. See `sources/zdd-tail-source-check.json`.
Absolute novelty is not established. The argument was checked by hand.
