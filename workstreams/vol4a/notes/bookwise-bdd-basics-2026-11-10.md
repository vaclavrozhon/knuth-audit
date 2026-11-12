# BDD foundations, applications, reduction and melding

Main pages 202–219, exercises 1–65 and answers 621–630 were read
together. Whole main pages 202–219, exercise pages 259–262 and answer
pages 621–629 are certified. Shared exercise 263 and answer 630 remain
for the synthesis block. New F0033–F0035 concern the false-solution
guard, the functional-response step in Theorem M, and a missing prime
in the melding proof. No general verifier or census was run.

The bead decomposition identifies each essential first-variable
subfunction with exactly one BDD node and gives the canonical reduced
ordered diagram. The examples and complements were read against the
original diagrams. Sequential numbering deliberately retains the false
sink for the true constant; this distinguishes the cases in F0033.
Counting multiplies by a power of two for every skipped variable;
weighted optimization inserts exactly the positive skipped weights.
The corresponding reconstruction, random-solution selection, recursive
enumeration and equality test preserve those invariants. The cycle
independent-set and kernel recurrences agree with the Lucas/Perrin
correction; their state interpretations were followed.

The connectedness example was read with its frontier construction in
answer 55. Maximal independence explains why kernel paths cannot skip
variables on accepting branches. Minimal connected edge sets are trees,
which explains the eight selected edges in the grid example and the
spanning-tree optimization reduction. Reliability is multilinear
interpolation; its finite-field hash bound follows by conditioning on
a variable of a nonzero multilinear polynomial. Abstract distributive
operations recover truth tables, generating functions, probabilities,
maxima and first/second moments. The one-changed-weight pair product
tracks exactly one exceptional contribution. FBDD reachable-variable
sets test freedom; absent variables can be inserted for commutative
products. The evaluation at -1 gives the evasiveness criterion.

The canalizing-variable algorithm eliminates incompatible branch
values and variables skipped on nontrue arcs. Threshold and adjacent
condensation bounds were checked through their distinct subtables;
the nonadjacent counterexample was verified. Symmetric diagrams depend
on prefix population, giving the two equal-sum sizes. The symmetric
maximum construction was read through its two maximal-length feedback
sequences, complement relation and nonconstant sliding windows; the
displayed d=3 example was checked by hand. Theorem M has the exact
local-response failure documented in F0034. Its three-in-a-row example
has acyclic port dependencies, so that particular construction avoids
the problem. The hidden-weighted-bit network carries prefix/suffix
sums and the accumulated selected bit. Forward references in answers
47–48 remain explicitly recorded for later closure.

The shared addition diagrams were read in both bit orders; counting
the carry, complemented-carry and sum nodes gives the displayed size
formulas. The junction function introduces one distinct selector node
per dummy variable and supplies any missing sink. Algorithm R first
marks reachable nodes and groups them by variable. Descending levels
redirect deleted children, remove equal-child branches, bucket on LO,
and use the children's AUX fields to identify duplicate HI values.
The two cleanup passes restore the temporary marks. The seven-node
example and the truth-table construction were traced. The compact
output variant stores each surviving child's new index in its HI
field after that field's last cleanup use. The restriction extension
marks reachability before rebuilding the level lists.

Melding represents ordered pairs of subfunctions. Distinct component
pairs remain distinguishable and equal children are impossible at the
first active variable; the printed final case needs F0035. The
separated-variable and interleaved-variable sizes follow from copies
and pairs of beads/subtables. The indegree argument assigns each
predecessor to a pair of component predecessors. The shifted
multiplexer construction has a bijective selector map; equal selectors
are exactly the all-zero odd positions, explaining its collapsed
branches and quadratic tail. Ternary combinations lie within the
three-way meld; substitution uses two restrictions and the replacement
function. The three-multiplexer example explains why a product of only
the original two sizes is not a general substitution bound.

Known wording, attribution and answer changes were distinguished from
new findings. Specific computational, external and forward-reference
limits are in the companion exceptions file. Next: main page 220 /
file 237, synthesis Algorithms S/U and their exercises from 66 onward.

Update: the QDD equation (86) and Theorem B dependencies from exercises 47–48 were checked and closed in V4A-X0135. The separate F0034 gap remains.
