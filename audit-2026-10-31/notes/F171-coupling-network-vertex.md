# F171 — The forbidden coupling arcs have the wrong target vertex

Confirmed in the local source set; low severity. Volume4B,
printed p386/file406, first sentence of answer MPR109(c).
The same text appears in the author's Pre-Fascicle5A,
11September2019, printed p43/file49.

The network in the question has distinct vertices
`s,x1,…,xn,y1,…,yn,t` and middle arcs `xi→yj`. The answer
instructs the reader to remove `xi→xj` when `i` is not below `j`.
There are no such `x→x` arcs. The target must be `yj`.

The distinction matters to the stated proof. On the two-element
chain1<2 with both marginal laws(1/2,1/2), every upper-set
condition holds with equality. Removing nonexistent `x→x` arcs
leaves the flow `c12=c21=1/2,c11=c22=0` available. It has value1
and the prescribed marginals, but assigns probability1/2 to
`X=2,Y=1`. Thus an arbitrary full flow in the unchanged network
does not establish the required order constraint.

Replace `xi→xj` by `xi→yj`. With the correct allowed arcs,
the complete finite flow argument proves the desired coupling.
The existence theorem itself is true; this is a local vertex-label
error, separate from the order-closure error F172 later in the proof.

Original evidence:

- `audit-2026-10-31/images/sequential/ref-042.png` — network definition.
- `audit-2026-10-31/images/sequential/ref-406.png` and
  `images/sequential/mpr109-answer-detail.png` — printed wrong label.
- `audit-2026-10-31/images/sequential/fasc5a-49.png` and
  `images/sequential/mpr109-ps-detail.png` — matching author PS.
- `audit-2026-10-31/notes/sequential-mpr-ex109.md` — full corrected
  proof, every cut condition and all exercise parts.
- `audit-2026-10-31/results/sequential/mpr-109-order-coupling-errata.json`
  — six official text layers and three TeX sources; no matching correction.

Only file406 is an error location. The valid question on file42
is not marked. No new numerical run, coordinator acceptance,
discovery priority or physical-copy comparison is claimed.
