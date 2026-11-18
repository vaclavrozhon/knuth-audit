# Backtracking and selected exact-cover analyses

Revisited the original backtracking discussion on pp. 31–53, statements
on pp. 58–63, and selected answer arguments on pp. 398–415. Also read the
exact-cover analysis on pp. 99–106 and the corresponding arguments on
pp. 468–471, with statements on pp. 148–149. Earlier computation records
were accepted within their stated scope; none was restarted.

No additional finding was confirmed in this block. In particular:

- The Langford undo operations and omission handling in Algorithm C
  preserve their stated search invariants after the already recorded fixes.
- The omitted initial weight test in Backtrack 78 is already F098.
  The trie endpoint, minimum code size, second-moment cost, and binomial
  stopping-level errors are likewise already recorded.
- Backtrack 52(d) can be completed using the truncated estimator and
  Markov's inequality. Its displayed node count is not a deterministic
  bound on an individual estimate, but no such bound is explicitly stated.
  The omission alone is not promoted to a new error.
- The final sentence of DLX 189(c) uses `y = xi sin(theta) >= 3/2`.
  This makes its bound on `x` valid; replacing that premise by a bound
  on `theta` would manufacture an objection to a different statement.
- The apparent probability defect in DLX 200(b), permutation index in
  197, and series constant in 196 are existing findings, not additions.
- DLX 199's central asymptotic remains the interpretation-dependent C002.

C015 has a stronger, nondegenerate witness using the book's own four-queens
tree (4). Its six leaves have original final weights `8,8,4,4,8,8`.
The January 28, 2024 amendment to E5 changes these to `0,0,4,4,0,0`,
because four leaves are dead ends and two are solutions. Thus the
geometric mean of the amended final weights is zero, whereas Backtrack
57 asks for a lower bound of six. The published amendment and the
original exercise are incompatible unless the exercise's weights are
understood as the values before the final zeroing. This strengthens the
existing candidate; it does not establish the wording of exercise 57 in
the latest complete printing, which the available 74-page preview omits.
