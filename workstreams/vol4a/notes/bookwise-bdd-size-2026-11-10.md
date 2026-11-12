# BDD size bounds and hidden weighted bits

Main pages 233–238, exercises 108–132 and answers 637–642 were read
together. Whole main pages 233–238, exercise page 266 and answer
pages 637–642 are certified. Exercise page 267 also contains 133–135
and remains for the following block. Findings F0036 and F0037 concern
a missing clique restriction and a wrong fixed-parameter asymptotic.

The worst profile follows by taking the minimum of the number of
prefixes and the number of unequal-half truth-table strings. The
tail telescopes to formula (82), with its stated breakpoint. The
average profile uses the probability that a particular bead occurs
among independent equal-length truth-table blocks. The exceptional
constant functions do not affect the displayed rounded estimate.
Answer 108 counts labeled branching programs and divides by the
permutations of non-root internal labels; smaller programs can be
padded before this count. The union over variable orders in 109 is
negligible at the asserted scale. The construction in 110 covers
the strict intermediate range; the main text handles the endpoints.
Flipping the first bit of a repeated-half string makes it a bead
without duplicating an unchanged bead. The average-case tail bound
in 112 leaves at most two intermediate levels.

For a quasireduced diagram (QDD), which retains every variable level,
counting edges across a cut gives q_k <= N_k+1 and q_k <= B-N_k.
Consequently B >= 2*q_k-1, and summation gives equation (86).
This closes the dependency from exercise 47. The QDD maximum adds
the redundant levels omitted by the BDD; the multiplexer profile
in 117 has the stated triangular tail. The symmetric-function
embedding, population count and multiplexer construction in 118–119
were checked. The hidden weighted bit selects the input at the
position equal to the population count. Its cyclic interpretation
in 121 and the interval decisions in the free diagram of 122 were
read without extending them to a new general construction.

Theorem B counts distinct residual slates after assigning a prefix
of the variables. Its two adjacent index intervals cover the needed
range, and the tested-index condition in the definition of w' is
"at most k" in the original. The resulting binomial lower bound
and the QDD/BDD cut inequality give the asserted exponential bound.
This closes the dependency from exercise 48. It does not repair
the separate local-response gap in Theorem M (F0034).

Theorem K colors each accepting path at its kth positive decision.
Splicing two paths through the same colored node forces their
prefix row and column sets to agree. The ticket bound then sums
to m*2^(m-1). Its forward reference to exercise 184 for an upper
bound remains to be checked later. Algorithm H distinguishes the
interior slate from endpoints; its two families of non-beads are
removed in H3–H4, and H5 deduplicates the constant-interior slates.
The artificial index at zero handles the endpoint consistently.

The generating functions and characteristic-root coefficients in
125–126 were checked at the printed algebraic level. Their omitted
profile derivations and exact boundary corrections are limited as
specified in the exceptions file. The arbitrary-order multiplexer
count in 128 separates constant and surviving address blocks.

An initial suspicion about B(S_m)=m^3+2 in answer 129 was dismissed:
S_m tests population exactly m, not population at least m. For N
variables its BDD has (m+1)*(N-m+1)+1 nodes; putting N=m^2 gives
the printed value. The conjunction bound therefore yields the
claimed order of magnitude. The distinction was checked before
any finding was recorded.

In answer 130(a), the exclusions leave k vertices containing the
first disagreeing edge, while preventing the other partial graph
from completing a k-clique. Part (b) needs the extra middle-clique
condition documented in F0036. Answer 131's row and column profiles
give its exact counts; part (a) contradicts the stated fixed-q
asymptotic (F0037). The paired complementary x variables in part (c)
give distinct residual functions at the chosen cut. The function
censuses and optimum orders in 132 were read as reported results.

Next: main 239 / file 256, variable orders and local reordering;
exercises 133 onward and answers 643 onward. No mathematical code
or exhaustive census was run for this block.

Update2026-11-11: The exercise184 upper-bound dependency is closed; see
bookwise-zdd-basics-2026-11-11.md for the checked BDD/ZDD profiles.
