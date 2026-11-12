# V3-C0056 — The striped-merge buffer formula has the wrong gcd term

Confirmed in volume 3, second edition, first printing (1998), answer
5.4.9-24, printed p.700, file p.711. The final input-buffer count
should end with `-gcd(P,D)/2`, not `+gcd(P,D)/2-1`.

Here P is the number of input runs, D is the number of disks, and
`g=gcd(P,D)` is their greatest common divisor. For offsets x_k of the
runs on the disks, the preceding page defines

```
s_d = sum over k=1,...,P of ((d-x_k) mod D).
```

It derives the worst number of waiting blocks as
`I_max=P(D-1)-min_d s_d` and shows that the optimal offsets attain

```
min_d s_d = ((P-1)(D-1)+g-1)/2.
```

Consequently its total of `I_max+D+P` input buffers is

```
PD/2 + 3D/2 + P/2 - g/2.
```

The expression printed on p.700 is instead

```
PD/2 + 3D/2 + P/2 + g/2 - 1.
```

It overstates the count by `g-1` whenever P and D are not coprime.
For example, take P=D=2 and the stated optimal offsets x_1=0, x_2=1.
Then s_0=s_1=1, so I_max=1 and the total is 1+2+2=5 buffers. The
printed closed form gives 6. This discrepancy uses exactly the
answer's buffer accounting, including its separate P merge buffers;
it does not rely on the optional linked-storage saving mentioned on
p.699.

The earlier optimization and offset construction are not refuted.
The error is the final algebraic simplification; for coprime P,D the
printed formula happens to agree with the correct one.

Original pp.699–700 were visually checked and retained as
`images/bookwise-p699.png` and `images/bookwise-p700.png`. The official
errata screen is `sources/disks-errata-review.json`. Targeted public
searches for exercise 5.4.9-24, gcd and buffer errata found no matching
report. This does not establish absolute priority.
