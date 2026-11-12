# Volume 4A: genlex and Chase combination generation

Main 363–369 through near-perfect multiset permutations, exercises
7.2.1.3–28–48 and answers 729–733 were read together. Findings F0068
and F0069 concern a path-count formula (and explanatory inequality) and a worked example,
respectively. No mathematical code ran.

The prefix characterization of genlex order and the two-index-list
criterion in 28 agree. In 29, balanced ternary order prevents cycles;
negation reverses the local rewrites; the sign/preceding-position parity
invariant prevents repeated zero positions. The final-string count then
forces full chains. The recurrences in 30, the binary-tree count in 31(a)
and the multifactorial recurrence in 31(b) were checked. The homogeneous
endpoint recursion in 32 agrees with the proof of Theorem N.

Theorem N's joining cases give (34)–(38), including the degenerate
subtrees. The active-bit traversal (39) and answer 36 count one upward
step per binary branch node, including final termination. Algorithm C's
four transitions maintain the first-change position r; its activity
formula (40) agrees with the two recursion states. The index-list
expansions (42)–(44) yield the stated even-decreasing/odd-increasing order.

The counting constructions in 33–35, the lexicographic/revolving-door/
homogeneous adaptations in 37, and the reverse initialization and parity
change in 38 were examined. Answer 39's binomial sum is 2,390,131;
following the inverse recurrence in 40 gives the printed millionth
combination. The finite-word recurrence and Boolean expressions in 41
are consistent. For 42, the reset at a zero, the displayed C5-to-C4
pattern generating functions and the four asymptotic branch ratios
agree; the full operation table is excepted below. Answer 43's only
exception is x=1, and the shifted restriction in 44 agrees with the
recurrences.

The index-list Algorithm CC and dual Algorithm CB were checked against
the expansion and local moves, including sentinel/termination conditions
and the initial (s,t)=(3,3) trace. In CC4 the original condition is
x >= j, not the OCR's x > j. The multiset recursion and answer 47's
activity-bit implementation are consistent. Answer 48's fixed
permutation argument proves both completeness and the single-exchange
property; its nonhomogeneous example has F0069.

Whole pages certified: main 363–368, exercises 382–383, answers
729–733. Shared main 369 and exercise 384 remain gray. Continue with
perfect combination schemes at main 369/file 386, exercise 49 and
answer 734. Exact exceptions are in the accompanying JSON.
