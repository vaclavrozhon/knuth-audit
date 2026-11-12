# The derivative limit has an exponent off by one

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–33(e), final displayed limit, printed 789.

The final equality in the displayed calculation is

```
lim_(x->0) ((x+y)^(n-1)-y^(n-1))/x = (n-1)*y^(n-1).
```

Differentiating the polynomial, or simply taking its coefficient of x, gives (n-1)*y^(n-2). For n=2,y=2 the left side is 1 and the printed right side is 2. The sum on the first line is likewise 1 in that example.

The corrected value is precisely what the recurrence needs. Multiplying the proposed recurrence term for q_n by n-1 reduces it to the displayed sum with y=n, so the corrected limit proves q_n=n^(n-2), the answer's intended and correct result.

Original typesetting inspected. No matching correction was found in the historical/current Volume 4A errata, refreshed Fascicle 4 errata or targeted public searches; see `../sources/tree-lattices-source-check.json`. Absolute novelty is not established.
