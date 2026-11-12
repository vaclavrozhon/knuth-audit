# The shadow count kappa_3(5) is eight

Volume 4A, first edition, first printing (2011), Answer 7.2.1.3–101(b), last paragraph,
printed page 744, file page 761.

For N t-combinations, kappa_t(N) is the size of the shadow of the first N combinations, obtained by lowering both binomial indices in the degree-t combinatorial representation of N.

For N=5,t=3 that representation is `5=choose(4,3)+choose(2,2)`. Therefore

```
kappa_3(5)=choose(4,2)+choose(2,1)=6+2=8.
```

The answer prints 7. Its application still works: 8 is greater than the available five degree-2 faces, so the displayed probability polynomial cannot come from a monotone function of five variables. The six-variable comparison is unaffected.

Original typesetting inspected. Errata and public-source screening:
`../sources/combination-applications-source-check.json`. No matching correction was found in the sources searched;
absolute priority is not established.
