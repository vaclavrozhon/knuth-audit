# Variable orders, local swaps and sifting

Main pages 239–246 through the end of dynamic reordering, exercises
133–159 and answers 643–650 were read together. Whole main pages
239–245, exercise pages 267–268 and answer pages 643–649 are
certified. Shared main 246, exercise 269 and answer 650 remain for
the following block. New findings are F0038–F0042.

The master profile chart assigns each subset/next-variable edge the
number of distinct residual functions depending on that variable.
Each variable order is a path, and its edge sum plus the sinks is the
BDD size. The shortest/longest-path recurrence in 133 processes
subsets in increasing bitmap order. The chart in 134 and its two
optimum paths were inspected; its complete local-optimum census was
not independently rerun. The uniquely thin construction in 135 has
a false dependency assertion (F0039); the conclusion itself was not
refuted or independently supplied with a replacement proof.

The median-of-medians count in 136 separates nonconstant rows from
rows already fixed to constants. The triangular count r$n is the
number of feasible nonconstant thresholds after r inputs. Summing
the row-by-row profile gives the product of the two squared half-size
parameters plus sinks. The stated normalization of arbitrary paths
was read as a proof sketch; its omitted cost inequalities were not
expanded. In 137, adding a separate clique changes the minimum
linear-arrangement cost by the sum of pairwise distances in that
clique, binomial(c+1,3); suitable c supplies both parity assumptions.
The subsequent exact BDD optimum is attributed to the cited paper
and is not independently proved in this audit.

In 138, the dependency bitmap of each QDD node counts the needed
master-chart edge weights. UNPACK groups nodes by their low child;
ELIM's timestamped high-child buckets remove duplicate pairs and
record old-to-new addresses. Jumping up copies the two cofactors,
reduces the copied levels from bottom to top, and then joins the
copies at the new first level. The rewritten parent addresses use
the final redirection map. Only dependency fields above the changed
interval are left stale, and the traversal never uses them again.
The subset-covering induction and the binomial call counts give
the stated O(n*3^n) bound. Inspection of the original resolved an
OCR ambiguity: the output index is y_(k+j)+1, not y_(k+j+1).
Restricting the construction to a window gives 139. The reduced
edge costs in 140 telescope, and max(q,n-|X|) is the proposed lower
bound when all variables are essential.

The threshold example in 142(a) has many distinct middle residual
thresholds in its original order; pairing large and small weights
in organ-pipe order leaves only linearly many residual thresholds
per level. In 142(b), matched complementary quadrants give m ones
in each row and column and separate the chosen prefix assignments.
The displayed total weight misses a factor m (F0041). Large profile
and optimum-order counts in 141,143–145 were read as reported
results. Part 146(a)'s necessary inequalities follow from possible
child pairs. Its converse is false because it omits reachability
constraints on level 2 (F0040).

The swap diagrams were checked as the four-entry transformation
abcd -> acbd. Solitary source nodes survive at the next level,
visible second-level nodes move up, hidden nodes disappear, and
new child pairs are interned. The source addresses remain fixed.
Theorems J+ and J- respectively count at most two descendants of
each previous bead and pairs of previous subfunctions. The known
factor correction in the quadratic-growth example was applied and
excluded from new findings.

Algorithm T's lists, temporary reference decrements, table removals
and variable mappings were traced. Its UNIQUE variant fails to
increment new nodes' children in U3; the three-variable example in
F0038 leaves a reachable node with zero reference count. The swap
example in 148 creates the sixteen listed new ordered pairs and
exceeds a factor of two. The geometric profile bounds in 149 and
the separated-support melding argument in 150 were checked. The
latter bounds the synthesis work by the result size, using the
previous linear-time synthesis sketch.

Algorithm J visits all insertion positions when it is not truncated;
the final reverse scan finds the best recorded size. Its initial
direction gives the stated roughly 2.5n upper bound on swaps. The
flag array in 151 follows variables through swaps and ensures that
each is sifted once. The optional early cutoffs and the reported
performance comparisons are empirical heuristics. Reversing the
known sequence of individually sifted variables explains answer154.
The multiplexer improvement in 157 is an application of answer128;
its omitted general strict-improvement algebra was not independently
expanded. In 158, the profile formulas need position indices rather
than original variable labels (F0042); the displayed fixed-g leading
orders are consistent after that correction. Life's rule in 159 has
eight interchangeable neighbor variables, reducing the possible
orders to the nine positions of the center; its node-count table
was not recomputed.

Next: finish shared main246 with read-once functions, exercises160
onward and answers650 onward. Exercise184 remains the pending
upper-bound dependency from TheoremK. No mathematical code or
exhaustive ordering census was run in this block.
