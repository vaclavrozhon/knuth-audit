# V3-C0050 — The last snowplow interval ends at kappa T

Confirmed in volume 3, second edition, first printing (1998), answer
5.4.1-22, printed p.678, file p.689. In the first sentence, the second
time interval is printed as `(kappa-1)T <= t <= T`. Its upper endpoint
should be `kappa T`.

Here kappa=k+theta is the parameter defined in the exercise, and T is
the separation between successive snowplow departures. The first plow
operates until time kappa T. During its last T units of ordinary motion,
there is no preceding plow still on the track, and the balance law is
`h dx = K(L-x) dt`, exactly as stated in the answer. Thus this law applies
on `[(kappa-1)T,kappa T]`. The answer subsequently evaluates the plow's
position at kappa T and gives a solution defined up to that time.

For example, at kappa=2 the printed second interval consists only of
t=T, omitting the entire final segment T<t<=2T. At kappa>2 it is empty.
This is a local endpoint typo; the subsequent piecewise solution and
the final run-length formula are not refuted.

The original p.678 was visually checked and retained as
`images/bookwise-p678.png`. All five official errata layers and limited
public searches were screened in
`sources/replacement-selection-errata-review.json`; no matching
correction was found. Absolute priority is not claimed.
