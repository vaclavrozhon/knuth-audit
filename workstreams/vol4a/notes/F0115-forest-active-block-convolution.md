# The active-block sums use the complementary vector in the wrong factor

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–37, displayed formulas for K,L,Z, printed 792.

The answer defines D(n) as the sum of “number of trailing zeros minus one” over forests of degree specification n. Write f(n)=|n|-||n|| for the number of roots, with the two norms defined in the answer. Its summation range requires f(n′)=f(n) and at least two fewer internal nodes in n′. Thus n-n′ is nonempty but has zero roots. There are no such forests, and every printed summand D(n-n′) is zero.

The claimed formula Z(n)=sum D(n-n′) therefore incorrectly gives Z=0 identically. Here Z counts the executions of c_1=0 in G5. A concrete example uses n_0=4,n_2=3. Algorithm G visits

```
2020200, 2022000, 2200200, 2202000, 2220000.
```

The transition from 2022000 to 2200200 executes G5 with j=2 and b_j=0, so Z=1. All other transitions are easy except final termination. This example is a single tree throughout and does not depend on the missing forest-prefix initialization.

In the stated summation range, n′ is the remaining forest, whereas n-n′ describes the active block and its attached zeros. The insertion argument in the preceding paragraph gives the corrected formulas

```
K(n) = k(n) + sum D(n′)*k(n-n′),
L(n) = l(n) + sum D(n′)*l(n-n′),
Z(n) = sum D(n′).
```

The summation constraints may be retained. In the example, the only contributing remaining forest is 200, whose D is 1, recovering Z=1. These corrections are separate from the sign of f_j on page 791.

Original typesetting inspected. Historical/current Volume 4A and refreshed Fascicle 4 errata and targeted public queries yielded no matching correction. See `../sources/tree-gray-generators-source-check.json`; absolute novelty is not established.
