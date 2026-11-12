# The change-count variable is not the claimed tail statistic

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–36, sentence introducing h, printed 790.

The answer defines h as the number of degrees b_j changed between visits, then claims h>x in C_(n-x)^(t) cases. This literal statistic does not have that tail count.

For ternary trees with n=2 internal nodes, Algorithm T visits

```
3003000 -> 3030000 -> 3300000.
```

Each of the two transitions changes two degree entries. Thus h>1 occurs twice, whereas C_1^(3)=1. No initialization or termination convention removes those two actual transitions.

The intended variable is the one used in the main-text analysis of Algorithm P on page 450: h-1 counts loop-body executions in T4, and the count includes the final attempt that terminates the algorithm. With that definition, the stated easy-case frequency and mean number of T4 assignments follow. This is an error in the explanatory statistic, not in the leading 4/23 cost for ternary trees.

Original typesetting inspected. Historical/current Volume 4A and refreshed Fascicle 4 errata and targeted public queries yielded no matching correction. See `../sources/tree-gray-generators-source-check.json`; absolute novelty is not established.
