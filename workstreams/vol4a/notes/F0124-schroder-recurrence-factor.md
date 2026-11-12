# The Schroder recurrence has n-1 instead of n+1

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–67, notes near the bottom of printed 798.

Here S_n counts n-node binary trees whose nonnull right links are independently colored black or white. The exercise explicitly gives S_0=1, S_1=1, S_2=3 and S_3=11.

The answer prints

```
(n-1) S_n = (6n-3) S_(n-1) - (n-2) S_(n-2).
```

At n=2 this asserts 3=9. The correct recurrence is

```
(n+1) S_n = (6n-3) S_(n-1) - (n-2) S_(n-2),  n>=2.
```

It follows directly from the correctly printed generating function S(z)=(1+z-sqrt(1-6z+z^2))/(4z), or from its differential identity

```
z(1-6z+z^2) S'(z) + (1-3z) S(z) = 1-z.
```

The generating function, the counts in exercise 66, and the Schroder triangle formulas continuing on page 799 are unaffected.

Original typesetting inspected, including an enlarged detail. No matching repair was found in the historical/current Volume 4A errata, refreshed Fascicle 4 errata or targeted public searches; see `../sources/tree-random-generators-source-check.json`. Absolute novelty is not established.
