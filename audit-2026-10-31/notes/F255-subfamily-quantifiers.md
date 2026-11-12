# F255 — Repeated subset/superset quantifier error

**Location:** Volume4B, first edition, second printing (2022), Appendix B,
printed664 / PDF684, final two entries. This is another occurrence of
the issue recorded as Volume4A F0133, not a separate mathematical defect.

A family is a set of sets. The subset operation selects S in F when
S is contained in **some** T in G; the superset operation selects S
when S contains **some** T in G. The printed conditions instead use
“T in G implies ...”, requiring the inclusion for **every** T in G.
This contradicts the complement equalities on the same two lines.

For F={{1}} and G={{1},{2}}, the member {1} belongs to both intended
outputs, using T={1}. Both printed universal tests fail at T={2}.
Replace the conditions by “S subseteq T for some T in G” and
“S superseteq T for some T in G”. The adjacent symbolic equalities
need no change. The correct main definitions are in Volume4A answer
7.1.4–236(a), p.669, already checked for F0133.

The original 4B page was visually inspected. Relevant current and
historical 4B errata and targeted public reports contain no matching
correction; the earlier4A source screen is retained. Absolute novelty
is not asserted.
