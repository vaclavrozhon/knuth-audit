# F211 — The search-profile asymptotic omits the endpoint regime

Confirmed in Volume 4B, SAT answer 215, printed page 590 (file page 610).
The question on page 335 asks for fixed clause density alpha without a lower bound.
Here P_l is the expected number of nodes at depth l, and t=l/(2n), so 0<=t<=1/2.

The answer maximizes f(t)=2t+alpha log_2(1-t^3) by imposing
`ln 4 = 3 alpha t^2/(1-t^3)` and then uses a full Gaussian sum about L=2t_alpha n.
But the right side is increasing on [0,1/2], and its maximum is 6 alpha/7.
Thus an interior maximum exists only when alpha > (7/6) ln 4.
For the ordinary positive density alpha=1, there is no stationary point in the
allowed interval: f is increasing and its maximum is at t=1/2 (depth n).
The proposed stationary depth lies beyond the end of the search tree.

Restrict the printed interior asymptotic to alpha > (7/6) ln 4 and treat the
endpoint regimes separately. At equality the Gaussian is one-sided, so its
leading factor is half the displayed full Gaussian factor. Below the threshold,
the dominant levels are within a constant distance of n, rather than a band of
width sqrt(n). The exact finite-n profile and the numerical example alpha=4
are unaffected. This finding does not question the standard saddle-point method.

The original PDF image was inspected. The 2015 author draft, page 226/file 234,
already places the unrestricted stationary point outside its stated domain.
The 2018-07-09 erratum replaces the local Gaussian expansion, but does not add
the missing restriction or endpoint cases; its replacement is incorporated in
the current book. Current/historical 4B and F6 errata checked, with no matching
correction. Focused public searches found no matching report; this is not a
claim of absolute priority. See bookwise-complexity-source-check.json.
