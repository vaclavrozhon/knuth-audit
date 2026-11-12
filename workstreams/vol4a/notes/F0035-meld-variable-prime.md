# V4A-F0035: The final melding case needs v prime

**Withdrawn on 12 November 2026.** The first-printing source already
prints `v' = v'''` in the last case. A fresh rendering of file page 646
confirms the prime. The alleged unprimed variable below was a reading
error; the example satisfies the actual printed equality. The historical
assessment is preserved below, but this is not a book error. See
`../../../integration/2026-11-12-novelty-review/notes/vol4a-f0035-dismissal.md`.

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), answer 7.1.4-58, printed page 629 / file 646.
Original: `images/bookwise-p629.png`.

The input nodes in (37) are alpha=(v,l,h) and alpha'=(v',l',h').
Answer 58 compares their meld with beta meld beta', where beta has
variable v'' and beta' has variable v'''. In the last case, v''>v''',
it states v=v'''. The correct equality is v'=v'''.

For example, take alpha=beta=(2,0,1) and alpha'=beta'=(1,0,1), the
ordinary BDD nodes for x2 and x1. The melds are equal by construction,
and this is the last case because 2>1. The printed conclusion would
assert 2=1. Replacing v by v' gives the correct 1=1 and agrees with
the accompanying recursive equalities, which split l' and h'.

This is a local typographical error in the proof, not a counterexample
to the fact that melding reduced ordered diagrams produces a reduced
diagram. The original and current/historical Volume 4A and Fascicle 1
errata were screened; no matching correction or public report was
located. See `sources/bdd-basics-source-check.json`. Absolute novelty
is not established. No computation was needed.
