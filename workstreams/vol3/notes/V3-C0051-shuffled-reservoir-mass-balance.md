# V3-C0051 — The shuffled-reservoir analysis violates mass balance

Confirmed in volume 3, second edition, first printing (1998), answer
5.4.1-23, printed p.679, file p.690. The answer applies a uniform-snowfall
trajectory during a period when the recycled records have a nonuniform
key distribution. Its final run-length prediction is consequently wrong
even within the steady continuum model used by the exercise.

Use the answer's notation: P is the internal capacity, P'>P the reservoir
capacity, p=P/P', q=1-p, L the track length, and K the uniform snowfall
rate per unit length after the old reservoir is exhausted. The first
T_1 time units feed the remaining qP' old reservoir records. Fresh input
then continues until time T. Let g(x) be the old reservoir's density,
and put

```
a(t) = p + qt/T_1,
C = K(T-T_1).
```

The answer correctly gives `h(x,t)=a(t)g(x)` during the first period
and derives the constant height `h(x(t),t)=C` seen by the plow. Here
x(t) is its position and h is the density of records waiting on the
track. But it then asserts, for the entire journey,

```
x(t) = L(1-exp(-Kt/C)).
```

The P records ahead of the plow instead impose, for 0<=t<=T_1,

```
P = a(t) integral from x(t) to L of g(u) du.
```

Differentiate this equality and use `a(t)g(x(t))=C`. The necessary
velocity and its integral are

```
x'(t) = Pq / (C T_1 a(t)),
x(t)  = (P/C) ln(a(t)/p).
```

This is not the printed exponential trajectory. There is a local
contradiction already in the logarithmic derivative of the velocity
at t=0. The balance equation gives `-q/(pT_1)=-LK/P`, using the
answer's `LKT_1=qP'`; the printed trajectory gives `-K/C`. Equality
would force LC=P. Yet LC is the run length and exceeds P in this
nondegenerate steady regime.

The same balance laws give a short correction within this model. Write
x_1=x(T_1). Then `x_1=(P/C)ln(P'/P)`. On T_1<=t<=T the input really is
uniform, so `x'=K(L-x)/C`. Because T-T_1=C/K,

```
L-x(T) = (L-x_1)/e.
```

The old reservoir has no mass beyond x(T): those positions were only
passed during the previous instantaneous final sweep. Thus the density
there at time T is C, supplied by the fresh input, and the remaining
internal records satisfy `P=C(L-x(T))`. The printed `KT(L-x(T))` should
also have `K(T-T_1)` in place of KT. The resulting run length R=LC is

```
R = P(e + ln(P'/P)).
```

This is a correction to the **continuum approximation**, not an exact
finite-capacity expectation or a newly proved stochastic limit theorem.
For P'=2P it predicts R/P approximately 3.411429. The book's parametrized
formula instead predicts approximately 2.857335. A single short,
seeded confirmation with P=2000 and 32 runs gave 3.41075 over the last
24 runs. The simulation supports the calculation but is not its proof;
details are in `results/random-reservoir-local-check.json`. No broad
experiment or convergence study was run.

The original p.679 was visually checked and retained as
`images/bookwise-p679.png`. All five official errata layers were screened
in `sources/replacement-selection-errata-review.json`. Targeted public
searches found no matching correction; no absolute priority claim is
made. The ordinary FIFO-reservoir analysis and Table 2 are not affected
by this finding about a reservoir shuffled between runs.
