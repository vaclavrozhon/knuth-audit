# The final ballot-area formula omits the diagonal case

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–55, final displayed equality, printed 795.

The exercise asks for C_pq prime at 1, the total area of the ballot paths of exercise 46. The answer writes q=p+r without excluding r=0. On that diagonal C_pp(x)=C_p(x), the area polynomial of ordinary Catalan paths.

With the usual empty-sum convention, the last displayed expression at r=0 becomes

```
2^(2p-1) - binom(2p+1,p).
```

For p=2 it is 8-10=-2, but C_22(x)=1+x has derivative 1. This is the principal Catalan specialization, not an empty-tree exception. Answer 54 supplies the correct value

```
C_pp prime at 1 = 2^(2p-1) - (3p+1)*C_p/2.
```

The missing diagonal correction is binom(2p,p)/2. The coefficient extractions in the preceding two lines work for r=0; the simplification subsequently applies the formula for C(z)^s/(1-4z) to s=r-1, outside its nonnegative range. Qualifying the last equality by r>=1, or explicitly adding [r=0]*binom(2p,p)/2, repairs it.

Original typesetting inspected. No matching repair was found in the historical/current Volume 4A errata, refreshed Fascicle 4 errata or targeted public searches; see `../sources/tree-counting-source-check.json`. Absolute novelty is not established.
