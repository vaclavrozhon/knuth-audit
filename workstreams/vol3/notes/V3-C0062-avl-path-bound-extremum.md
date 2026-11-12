# V3-C0062 — The path-length argument needs a maximum over heights

Confirmed local proof defect in volume 3, second edition, first
printing (1998), answer 6.2.3-4, printed p.714 / file p.725.
The displayed `min_h` should be `max_h` over feasible tree heights.

Let N be the number of internal nodes and let h-1 be a tree's height,
as in the preceding paragraph of the answer. The Fibonacci-tree
extremal property supplies a bound of the displayed form

    path length <= h N - Theta(h phi^h) + O(N)

for that fixed height; phi is the golden ratio. To bound the path
length of all N-node AVL trees, whose heights differ, one must take
the largest of these bounds over the feasible heights. Taking the
smallest would require the fixed-height inequality to apply to a
tree at every other height, which the preceding property does not say.

The intended maximization is also what yields the next displayed
bound: balancing N against a term of order h phi^h places the maximum
at h = log_phi N - log_phi log_phi N + O(1). Thus the subsequent
asymptotic result need not change; the printed extremum is reversed.

The original formula was visually checked. The 7 October 1996
first-edition addendum on p.675 already contains the same minimum;
no subsequent correction was located in the official layers or the
limited public screen. Evidence: `images/bookwise-p714.png` and
`sources/balanced-trees-errata-review.json`.
