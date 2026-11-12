# Bookwise review: sorting networks, 10 November 2026

Reviewed volume 3 §5.3.4, printed pp.219–247, all exercises 1–68, and
their printed answers on pp.666–676. The shared answer page 676 also
begins §5.4 and is left for the next certification block. Original
figures and suspect formulas were inspected, with all five official
errata layers in `sources/networks-errata-review.json`.

Checked the threshold argument for the zero–one principle; odd–even
merging, the three zero-count parity cases, comparator recurrences and
delay formulas; Floyd's merger lower bound and its normalization;
bitonic splitting and the odd-size obstruction; and the selection
network potential argument. Checked the exercise arguments concerning
shuffle masks, network normalization, monotone Boolean functions,
order-preserving comparator maps, primitive networks, path lower bounds,
multiset extensions, the satisfiability reduction, multiway sorting
stages, merge costs, multihead passes, uniform sorting, and the
nonreversible one-register bound. These checks follow the printed
arguments, rather than reprove the external theorems on which they rely.

New findings C0044–C0049 have separate arguments and original-source
images: two clause-wire indices, reversed saturated-block values, an
undefined shuffle parameter, a false equivalence between uniform sorting
and the particular Algorithm Q, a truth-table domain subscript, and a
false leading asymptotic in the 2005 errata themselves. The last issue
is assigned to the errata PDF, not to the correct original book page.
The four-key counterexample to exercise 64 is a manual trace; no census
was run. Exercise 65's mean remains independently valid.

Known corrections were incorporated without creating findings: updated
network figures and optimum tables; the 7-by-4 merger; the AKS-era
asymptotic update; the new Green selection construction; G_T and the
cut-window subscript; the tableau example; the Rost time/tail bounds;
the exercise-66 counterexample and exercise-67 update. The newly faulty
Dedekind replacement was checked separately from those accepted changes.

Precise limits of this review:

- Optimal-size/delay tables, computational nonexistence claims, and
  literature results attributed to AKS, Alekseev, Miltersen–Paterson–Tarui,
  Korshunov/Sapozhenko, Rost, Kalai and others were not independently
  reproduced. Research problems 41,43,44,47 and other open extensions
  were not solved. No historical benchmark or exhaustive census was rerun.
- The displayed large networks, including Figs.49/51 and exercise 34,
  were inspected in the source and corrected diagrams. Their complete
  input-by-input correctness was not independently enumerated or given
  a new full proof. The special Waksman example in answer 7, the Green
  general construction in updated answer 20, and the eight-switch
  permutation network in answer 55 were not exhaustively certified.
- Answer 26's lifting argument, the general middle-third argument in
  answer 39, and the last three heads of the 23-head construction in
  answer 61 remain at the detail of the printed sketches. The relevant
  inequalities and stated reduction ideas were checked; omitted case
  analyses were not expanded into new proofs.
- The Edelman–Greene correspondence in answer 38 and related tableau
  enumerations, and the full multiset-algebra axiomatization in answer
  50, are accepted external results. Their printed applications and
  local examples were checked.
- The source PDF cited by the faulty Dedekind erratum could not be
  obtained; C0049 instead supplies an elementary contradiction. No
  claim that its lower-order terms have been repaired is made.

Next: §5.4, external sorting, printed p.248 / file p.259, with its paired
exercises and answers. The earlier forward dependency from 5.2.3-37 to
§6.3 Eq.(13) and exercise 28 remains queued for that section.
