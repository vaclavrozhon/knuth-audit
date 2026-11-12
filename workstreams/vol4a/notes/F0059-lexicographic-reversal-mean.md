# The exact reversal mean includes a step that is never executed

**Location.** Volume 4A, first edition, first printing (2011), answer
7.2.1.2–5(a), printed page 703 / file page 720, paragraph on step L4.

Let K be the number of comparisons in step L2, and let q_k = 1/k!
for 1 <= k <= n, with q_k = 0 for k > n, as in the answer. The
printed expression for the average number of swaps in L4 is

    sum_k floor(k/2) (q_k - q_(k+1)) = q_2 + q_4 + ... .

This includes floor(n/2) swaps for the final, completely descending
permutation. But step L2 terminates on that permutation, before L4.
The average per visited permutation should therefore be

    sum_(2h <= n) 1/(2h)! - floor(n/2)/n! .

For example, when n=3 the visited permutations are

    123, 132, 213, 231, 312, 321.

Step L4 makes one swap on each transition from 132 and 231, and none
on the other transitions; after 321 the algorithm stops in L2. Thus
its total is 2 and its average is 2/6 = 1/3. The printed expression
gives q_2 = 1/2. Even averaging over the five actual invocations of
L4 would give 2/5, so that interpretation does not recover the formula.

**Impact and correction.** This is a finite-size operation-count error;
Algorithm L and the limiting constant cosh(1)-1 remain correct. Subtract
floor(n/2)/n! from the exact expression, or explicitly describe a
modified algorithm that reverses the final permutation back to the start.
The analogous termination term is already handled in answer 38 on
page 708 for Ord-Smith's generator.

The original page was inspected, and current/historical Volume 4A and
Fascicle 2 errata were checked. Public searches located an earlier
Knuth draft with the same expression and unrelated results, but no
matching correction. This does not establish absolute priority.
See sources/permutation-basics-source-check.json. No code was needed.
