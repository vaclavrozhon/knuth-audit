# F197 — prefix bounds can address missing Sinz variables

Volume 4B, answer 7.2.2.2–29, printed page 553 / file page 573.

The auxiliary variable s_j^k of (18)–(19) exists only for
`1 <= j <= n-r`, `1 <= k <= r`, where r is the final bound.
Answer 29 assumes only nondecreasing prefix bounds r_i and then
requires s_(i-r_i)^(r_i+1) to be false. That index can lie outside
the declared rectangle.

Take n=6 and prefix bounds `(1,1,1,3,4,5)`. These satisfy all the
stated assumptions. Since r=5, only j=1 is available. The constraint
on the first three bits requires the nonexistent s_2^2.

This is not repaired by merely declaring that additional variable
and setting it to zero: x=`101000`, s_1^1=1 and every other auxiliary
zero satisfy all of (18)–(19) and all the listed extra unit clauses.
But the first three bits have sum 2, exceeding the required 1.
The short checker confirms precisely this assignment and encoding.

One repair is to normalize the caps further before setting up the
rectangle: start with r_0=0 and replace each r_i, in order, by
`min(r_i,r_(i-1)+1)`. This preserves the allowed bit strings and makes
the cap increments at most one. It changes the example to
`(1,1,1,2,3,4)`; now the referenced variable exists and excludes the
counterexample. In general i-r_i is nondecreasing, so its value cannot
exceed n-r_n. Vacuous constraints and the standard boundary values
are handled as in the original encoding. Alternatively the sequential
counter must be enlarged with the missing propagation clauses.

The original typesetting and the September 2015 author draft,
page 189, have the same omission. Relevant current/historical errata
and targeted public reports were checked without finding a correction.
The Japanese SAT tutorial found by search restates the exercise but
does not supply a correction to this answer. No absolute priority claim.

Evidence: `check_bookwise_sat29.py` and `results/bookwise-sat29.json`.
Only one fixed six-bit assignment in two encodings was tested.
