# F172 — The cut proof uses the upper closure instead of the lower closure

Confirmed in the local source set; low severity. Volume4B,
printed p386/file406, answer MPR109(c). The original PDF and
the author's11September2019 Pre-Fascicle5A p43/file49 both define

`A={x: x≽a for some a∉J}, B=P\A`.

The assumed stochastic-order condition says `p(U)≤q(U)` for
every upper set U. The printed proof nevertheless uses
`p(A)≥q(A)` with this upper set A.

An exact counterexample has P={1<2}, marginal laws
`p=(3/4,1/4), q=(1/4,3/4)`, and blocking pair `I=P,J={1}`.
The upper-set condition holds: its only nontrivial inequality
is1/4≤3/4. Every allowed path is blocked because I=P. The printed
sets are A={2},B={1}; its displayed chain becomes

`5/4 ≥ 1/2 ≥ 1`.

The second inequality is false. A separate two-element check
also refutes the claimed general inclusion A⊆I: I={1},J={2}
is a blocking pair, but the printed upper closure of P\J={1}
is all of P.

Use the lower closure

`A=(P\J)↓={x: x≼a for some a∉J}`.

Then A⊆I by the blocking property, B⊆J by reflexivity, and
`A=A↓`, `B=B↑`. Part(b) gives `p(A)≥q(A)`, so all steps of
the cut-capacity bound follow. The accompanying closure statement
should accordingly be `A=A↓` or `B=B↑`. The printed `B=B↓`
is true for the original wrong A, but does not support the needed
probability inequality and must change with the repair.

This is a local proof error. The main finite ordered-coupling
theorem remains valid, with a complete independent proof in
`audit-2026-10-31/notes/sequential-mpr-ex109.md`.

Original PDF/PS evidence is in
`images/sequential/ref-406.png`, `images/sequential/fasc5a-49.png`,
`images/sequential/mpr109-answer-detail.png` and
`images/sequential/mpr109-ps-detail.png`, all under
`audit-2026-10-31/`. The manifest
`results/sequential/mpr-109-order-coupling-errata.json` records
all six official errata text layers and three TeX sources with
hashes and contexts; none repairs this direction.

Only file406 contains this error. No numerical run, independent
coordinator acceptance, discovery priority or physical-copy check
is claimed. F171 concerns a different vertex label earlier in the proof.
