# V3-C0076 — Ordered hashing uses C_(N+1), not C_(N-1)

Confirmed in volume 3, second edition, first printing (1998), answer
6.4-66, printed p.741 (file p.752).

C_N denotes the expected probes in a successful search among N keys;
C'_N denotes the expected probes in an unsuccessful search among N
keys. The answer gives C_(N-1) for an unsuccessful ordered-hash search
with N stored keys. The correct index is N+1, under the same random
hash and key-order assumptions.

For example, with N=2, the printed value is C_1=1. But there is a
positive probability that the query and both stored keys hash to the
same position and the query is smaller than both keys. Ordered linear
probing then examines both keys and an empty cell: three probes.
Every search requires at least one, so the mean is strictly above 1.

The search path before inserting a fresh key is its successful search
path immediately after the ordered insertion. Among N+1 exchangeable
random keys this gives C_(N+1). For linear probing, Theorem K makes
the N=2 value 1+1/M+1/M^2, where M is the table size.

The same sentence also calls C'_N the insertion cost for the Nth
term. With the section's convention this is the (N+1)st term; or
retain 'Nth' and change that insertion index to N-1.

Original p.741 inspected. The historical bibliographic addition to
answer 66 does not correct these indices. No matching correction
located in the official layers or limited public searches; see
`sources/hashing-errata-review.json`.
