# F185 — incorrect quarter-turn cycle

Volume 4B, first edition, second printing (November 2022), §7.2.2.1,
answer 371(a), printed page 521 / file page 541.

A tuple (a,b,c,d) denotes the rectangle [a,b) × [c,d) in an n × n
square. The quarter-turn map is correctly defined in the question as
rho(a,b,c,d) = (c,d,n−b,n−a). The answer's displayed second and third
iterates are incorrect. The full cycle is

```
(a,b,c,d)
→ (c,d,n−b,n−a)
→ (n−b,n−a,n−d,n−c)
→ (n−d,n−c,a,b)
→ (a,b,c,d).
```

For the answer's own n=4 example (0,1,2,4), these are
(0,1,2,4), (2,4,3,4), (3,4,0,2), (0,2,0,1).
The printed formula instead gives (3,2,3,4) as the second iterate,
which is not even a rectangle with increasing endpoints.
The correction is needed before applying the subsequent lexicographic
test and merging the orbit's options. It does not establish an error
in the independently reported enumeration results.

The original is visible in `images/bookwise-p521.png`; the same error
occurs in the author's September 2019 pre-fascicle, printed page 225.
The historical/current Volume 4B and Fascicle 5 errata have no matching
entry. Source and public-report search scope is recorded in
`sources/bookwise-motley-source-check.json`; no absolute priority claim
is made. `check_bookwise_motley371.py` checks only these explicit tuples,
with output in `results/bookwise-motley371.json`.
