# The duality identity uses the wrong shadow degree

Volume 4A, first edition, first printing (2011), Answer 7.2.1.3–97(d), final identity,
printed page 743, file page 760.

Here kappa_d(N) is the size of the lower shadow of the first N d-element combinations, and lambda_d(N) is the corresponding maximum number of (d+1)-element combinations allowed by N d-element faces. The dual size vector is `bar N_j = choose(n,j)-N_(n-j)`.

The first inequality on the last line of part (d) correctly uses `kappa_(n-t+1)(bar N_(n-t+1))`. The identity later on that line drops the +1 from the kappa index. It must read

```
kappa_(n-t+1)(bar N_(n-t+1))
    = choose(n,t)-lambda_(t-1)(N_(t-1)).
```

For a concrete nonempty complex on ground set {0,1,2,3}, take the empty face and the three vertices 0,1,2. With n=4,t=2 we have N_1=3 and bar N_3=1. The printed left side is kappa_2(1)=2, whereas the right side is 6-lambda_1(3)=6-3=3. The corrected left side is kappa_3(1)=3.

Original typesetting inspected. Errata and public-source screening:
`../sources/combination-applications-source-check.json`. No matching correction was found in the sources searched;
absolute priority is not established.
