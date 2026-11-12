# A false equality in the proof of the real-binomial shadow bound

Volume 4A, first edition, first printing (2011), answer 7.2.1.3–80,
printed page 739, file page 756.

The answer splits the degree-t combinatorial representation of N by
Pascal's identity into N=N_0+N_1. In its next displayed calculation
it asserts `N=N_0+kappa_t(N_0)`. The function kappa_t gives the
smallest lower-shadow size of a family of t-element combinations.
The assertion need not hold: N_1 can exceed kappa_t(N_0).

Take t=2 and N=4=choose(3,2)+choose(1,1). The answer's definitions give

```
N_0 = choose(2,2) + choose(0,1) = 1,
N_1 = choose(2,1) + choose(0,0) = 3,
kappa_2(N_0) = kappa_2(1) = 2.
```

Hence N_0+kappa_2(N_0)=3, not N=4. Both N and N_0 are positive;
this counterexample does not rely on an empty family.

The proof can retain N=N_0+N_1 and use N_1>=kappa_t(N_0). For
N_0>0 its induction gives N_1>=choose(y,t-1), where
N_0=choose(y,t); this is the inequality needed to infer x>=y+1.
If N_0=0, choose y=t-1 and use N_1=N>=1 directly. The subsequent
argument then gives the stated bound for nonempty families. The
Lovasz bound itself is unaffected by the false intermediate equality.

The original equality and the definitions were inspected at full
resolution. See `../sources/shadows-source-check.json` for errata and
public-search screening. No matching correction found; absolute
novelty is not established.
