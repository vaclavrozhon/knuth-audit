# The subtree removal vectors have the wrong sign

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–37, definition of f_j on 791 and C(n+e_j;j) identities on 792.

The unit vector e_j increments the number of degree-j nodes. Collapsing a degree-j node with its j leaf children to a leaf decreases n_j by one and n_0 by j-1. The decrement vector must therefore be

```
f_j = e_j + (j-1)*e_0,
```

not the printed e_j-(j-1)e_0. The printed sign does not preserve the number of roots and contradicts the falling-factorial ratio later on page 791.

For n_0=3,n_2=2, the two degree sequences are 20200 and 22000. Algorithm G has one easy transition, so C-E=1. The printed sum C(n-f_2) instead counts four leaves and one binary node, giving 3. The corrected vector gives two leaves and one binary node, giving 1.

The related identities on page 792 also need the full vector: C(n+f_j;j)=C(n)+D(n), where D sums trailing-zero counts minus one. Merely adding e_j changes the root count. In the same example, C=2 and D=(2-1)+(3-1)=3, while n+e_2 has three leaves and three binary nodes and admits no forest. The printed C(n+e_2;2)=C+D would say 0=5. Adding f_2 instead gives four leaves and three binary nodes, with the correct count 5.

The final inclusion-exclusion expression for C+D uses the same f_j symbols and should be read with the corrected definition.

Original typesetting inspected. Historical/current Volume 4A and refreshed Fascicle 4 errata and targeted public queries yielded no matching correction. See `../sources/tree-gray-generators-source-check.json`; absolute novelty is not established.
