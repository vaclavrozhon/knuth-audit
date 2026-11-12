# F214 — The boundary argument names V instead of clause C

Confirmed: Volume4B, SAT answer243(d), printed594/file614. In the boundary-
variable argument, replace the V in “hence V must contain v or v-bar” by C.
The proof has just chosen a clause C; the notation V(F') denotes a set of
variables, and no standalone clause V has been defined. It is C that must
contain each boundary variable, in order to conclude the claimed width bound.

This is a notation typo, not a false theorem. The intended step is sound:
flipping the unique-occurrence variable satisfies the remaining violated axiom,
so if neither signed literal occurred in C, C would remain false, a contradiction.
Original PDF image bookwise-boundary-p594.png inspected. The same V occurs in
the2015 draft, printed230/file238. Relevant current/historical4B/F6 errata and
focused public searches yielded no matching correction; absolute priority is
not asserted. See bookwise-resolution-source-check.json.
