# Minimum-comparison sorting — 10 November 2026

Reviewed printed pp.180–197 through §5.3.1, original exercises 1–36
and answers 652–658, with the added exercise 37 and replacement answers
31–32 in the current errata. The next section's content on shared
pp.197 and 658 is not certified by this block. File pages are printed
pages plus 11. No census or new implementation was run.

The comparison-tree model, information bound, binary insertion count,
five-key construction, merge-insertion schedule and recurrences
(11)–(19) were read together. The bound on the main chain before each
insertion explains t_(k-1)+t_k=2^k; the first differences and closed
form in answers 13–15 agree with that recurrence. The efficiency
argument is adversarial: its smaller-efficiency branch cannot recover,
but reaching a chain on that branch alone would not prove an algorithm
(answer 18). The component product, interleaving sums (29)–(32), and
the matrix construction were inspected with the original diagrams.
The two comparison counts for the worked cross-component choice sum
to 69300 as required. The minimum external-path argument, its local
height conditions and the nonuniform three-key example were checked.

The ternary diagrams in answers 5, 7 and 8 were inspected as diagrams,
including impossible branches and the repeated all-equal outcomes.
The two recurrences in answer 10 and their closed form are consistent
with the initial conditions. The strong-sorting zero-one argument,
parity reduction, and comparison-exchange relabeling were read. The
weighted real-tree argument was reviewed in its intended x>=1 regime;
the terse necessity argument was not expanded into a new proof.

New findings are C0039 (invalid binary bound for ternary comparisons),
C0040 (ceiling in an average lower bound), and C0041 (wrong depths in
the six-key exercise). Their individual notes contain the exact
counterexamples. The “at least n lg n” wording in exercise 29 was read
as the asymptotic comparison lower bound intended by (2), (4) and its
answer S(n); it is not recorded as another mathematical finding.

Known corrections were kept separate: the logarithm label on p.183,
the descriptions of the five-key construction, the (b,e) matrix entry,
the component prime in (26), the updated small-n optimal values and
Sergeev bound, the changed exercise 35, the answer 7 multiplicity,
and the replacement comparison-exchange tree. The latter was inspected
in the author's err3 PDF, p.5. The detailed screen is
`sources/minimum-sorting-errata-review.json`.

Exact limits of this review:

- The 1649-graph census, the 91-graph restricted census, and external
  optimality results for larger n were accepted as cited results;
  neither graph census nor exhaustive comparison-tree search was rerun.
- Exercise 16 has no printed proof. Its Hwang–Lin inequality is accepted
  as the attributed result; no new all-n proof was constructed.
- The Paterson and Munro–Raman multiplicity bounds, Cesari and Kollár
  average optima, current Stappers results, and Stanley log-concavity
  theorem were not independently re-proved from their original papers.
  The replacement tree's asserted optimum average is explicitly only
  conjectural in the errata; no optimality search was performed.
- Exercise 19's experiment and the 873-line MIX program in answer 28
  were not reconstructed. The reported timing and its tentative
  optimality were not independently established.
- The sharp fixed-m asymptotic requested by exercise 11 remains
  unestablished by this review because its printed proof fails (C0039).
- Research exercises 34 and 36, and historical versions of 35, were
  not solved. Current errata were used for the resolved small-n cases;
  no survey of the present research frontier or historical priority
  was undertaken.

Next: §5.3.2, minimum-comparison merging, printed p.197, with its paired
exercises and answers.
