# The proof equates a shadow size with the size of the family

Volume 4A, first edition, first printing (2011), answer 7.2.1.3–78,
printed page 739, file page 756, first paragraph.

The proof's last equality is `kappa_t(M+N) = |P_{|A|,t}|`.
Here P_{|A|,t} is an initial family of |A|=M+N combinations, whereas
kappa_t(M+N) is the size of its lower shadow, the family of subsets
with one element removed. A shadow operator is missing on the right:

```
kappa_t(M+N) = |shadow(P_{|A|,t})|.
```

For t=2 and M=N=1, the left side is kappa_2(2)=3, while the printed
right side is 2. For instance A={{0,1},{2,3}} satisfies this split.
Adding the shadow operator restores the intended conclusion of the
induction. The preceding inequality chain and Theorem K remain valid.

Original inspected, including the missing symbol. Errata and public
search screening are recorded in `../sources/shadows-source-check.json`.
No matching correction found; absolute novelty is not established.
