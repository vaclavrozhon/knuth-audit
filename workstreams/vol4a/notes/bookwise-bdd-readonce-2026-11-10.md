# Read-once, skinny and thin functions; Life exercises

Main pages 246–247 through read-once functions, exercises 160–175,
and answers 650–656 were read together. Whole main page 246,
exercise pages 269–270 and answer pages 650–655 are certified.
Shared main247, exercise271 and answer656 remain for multiplication.
F0043 records the incorrect unshuffle example in Theorem W.

For Life, tameness adds the one-cell outer boundary to the local
constraints; more distant cells cannot activate in a single step.
The wild-predecessor count is the difference between the interior
and tame counts. The still-Life and alternating-pair constraints
use the same local rule; the lexicographic condition counts each
nontrivial pair once. The escape recurrence E_(k+1)(X) restricts X
to tame states and quantifies over its uniquely determined next
state Y in E_k. Hence it counts the first escape time correctly.
The large numerical counts, optimal weights and specific grids are
reported computations, not independently reproduced censuses. The
known A0/symmetry correction was screened and excluded as a finding.

For a read-once function split into disjoint variable blocks, the
AND-type recurrence attaches the second BDD to the first one's true
sink. Complementing the whole function requires a separate first
block and the complemented second block. For XOR-type composition,
both polarities of the second block are needed. These constructions
give (112)–(113), including the shared sink deductions. The extremal
recurrences in164 and the simultaneous Fibonacci recurrences in165
agree with their base values and the two composition cases.

Theorem W uses a stable separation of the two blocks, followed by
comparison of residual functions in each block. The printed
permutation example separates ranks instead of the testing order
(F0043). Answer166 is read with the intended testing-order convention:
in the AND case one chooses the block containing the last tested
variable as the second block and chooses prefix assignments that
leave it nonconstant; in the XOR case the block containing the first
tested variable is first. This is the intended witness comparison,
not a certification of every literal permutation subscript in that
answer. No new general proof or formalization was supplied.

Answer167 recursively computes the optimum single-function and
two-polarity sizes together and chooses the cheaper block order.
The permutations should be stored as lists so concatenation is
constant time per internal node. In168, x=c'/2-1 and y=c-c'/2-1
turn the two size recurrences into the stated pair operations.
The reflection exchanges the two operations. The norm proof first
equalizes the second coordinates, encloses the result in an ellipse,
and bounds its largest norm by r^2+(sqrt(5)+1)*r*r'+r'^2. The
remaining inequality is exactly the cited monotonicity of f_t(a)
for a>=2; that external analytic result was accepted as attributed.
The open extremal question in169 was not pursued.

A skinny BDD has one node per essential variable and a sink branch
at each node. Its four choices per nonfinal node and two choices at
the last node give 2^(2n-1) functions. The monotone half-choices
give 2^(n-1); their binary threshold representation supplies the
dual, shortest DNF and shortest CNF in170. In171 the corrected
read-once/regular hypotheses allow induction on the two blocks.
If neither has a one-literal prime implicant, replacing the first
variable of the second block's first prime implicant by the preceding
variable contradicts regularity. The Horn sign-choice recurrence in
172 gives 3^n-2^(n-1), and the two-polarity condition gives 2^(n+1)-2.
Run-length automorphisms in173 lead to the weak-order count and the
2^n independent choices of signs.

For thin BDDs,174(a) sends a repeated child label to the corresponding
unused high label; reachability supplies exactly enough labels for
that replacement. The inverse Dellac bounds give the alternating
up/down constraints in the Genocchi derangement of (b). Following
inverse cycles until reaching a label at least k gives (c)'s pistol
and its fixed-point criterion. The displayed path, transition strings,
derangement, Dellac permutation and final BDD were traced together.
All omitted general inverse proofs and the complete additive census
are limited as specified in the exceptions file. The Bernoulli and
tangent generating functions agree with the initial values.

In175, adding b new nodes chooses b distinct ordered child pairs.
Exactly t old sources must be covered, so inclusion-exclusion over
these sources gives the coefficient expression for c(b,s,t,N).
The exponential generating function is the same inclusion-exclusion
sum. The new source count is s_old+b-t, which gives the recurrence
for T; its one-variable base includes zero, one or both literal nodes.
No new enumeration program was run.

Next: multiplication from main247 / file264, exercises176 onward,
answers656 onward. TheoremK's exercise184 upper-bound dependency
remains pending.
