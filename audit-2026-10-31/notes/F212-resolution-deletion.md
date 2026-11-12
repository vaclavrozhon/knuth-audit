# F212 — Deleting a literal from both clauses need not preserve satisfiability

Confirmed in Volume 4B, SAT answer 217, printed page 590 (file page 610).
The question allows arbitrary simultaneously satisfiable clauses A and B and an
arbitrary literal l; it asks whether C=(A union B) minus {l,not l} is satisfiable.
The answer says true unless A or B contains both opposite literals.

Take A=B={l}. Both clauses are simultaneously satisfied by l=true, neither is
tautological, and C is the empty clause, hence unsatisfiable. The question does
not require distinct clauses. The answer's proof also has a separate, visible
failure with distinct clauses: A={l,a}, B={l,b}, and the satisfying literal set
L={l}. Its claim that L minus {l,not l} still covers C is false: that set is empty,
while C={a,b}. This second example invalidates the proof step, although C itself
is satisfiable.

The answer to the question as posed should be false, with the unit-clause
counterexample. The usual resolution conclusion is valid under the complementary
pivot hypotheses used in the main text. Those hypotheses are mentioned in the
answer's final paragraph, but are not assumptions of its preceding general claim.

The original page was inspected visually, as was the exact wording of the
question on page 336. The same answer occurs in the 2015 author draft,
page 226/file 234. Current and historical 4B/F6 errata contain no matching
correction, and focused public searches found no matching report. No stronger
claim of novelty is made. See bookwise-complexity-source-check.json.
