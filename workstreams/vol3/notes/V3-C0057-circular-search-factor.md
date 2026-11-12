# V3-C0057 — The circular-search cost change is missing a factor of two

Confirmed in volume 3, second edition, first printing (1998), answer
6.1-20, printed p.704, file p.715. The displayed change in average
search time should have a factor 2 before the sum.

Exercise 18 defines the average cost as the sum of `p_i*p_j*d(i,j)`
over all ordered pairs (i,j). Exercise 20 uses the symmetric circular
distance `d(i,j)=min(d_|i-j|,d_(N-|i-j|))`. The proposed rearrangement
places the smaller of each mirrored pair of probabilities on the left.

Take four records with probabilities

```
(q_1,q_2,r_2,r_1) = (1,4,2,3)/10,
```

and distances d_1=1, d_2=2. Here k=2, m=h=0, the index sets in the
answer are A={1} and C={2}, and the rearrangement is `(1,2,4,3)/10`.
The actual old and new costs are

```
old = 2*(4+8+6+3)/100 + 4*(2+12)/100 = 49/50,
new = 2*(2+8+12+3)/100 + 4*(4+6)/100 = 9/10.
```

Their difference is 2/25. But the single term in the answer's displayed
sum is

```
(q_1-r_1)*(q_2-r_2)*(d_1-min(d_2,d_2)) = 1/25.
```

The factor 2 accounts for the two directions of each pair. It is
already present in the corresponding linear-array calculation in
answer 18 on the same page. The sign of the improvement is unchanged,
so this does not refute the optimum-arrangement conclusion.

The original page was visually checked and retained as
`images/bookwise-p704.png`; the cost definition is on p.407. A single
exact rational check is saved in
`results/circular-search-factor-local-check.json`. The five official
errata layers were screened in `sources/sequential-search-errata-review.json`.
Their known correction to answer 19 is a separate issue. Targeted
public searches found no matching report; no absolute priority is claimed.
