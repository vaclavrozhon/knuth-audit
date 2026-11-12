# V2-C0254: missing constant term in Motzkin's quadratic factor

Confirmed local algebraic error, low impact. Third edition, first
printing (September 1997), printed page 705, file page 717, answer
4.6.4-39. The question on 519 and answer on 705 were both inspected
in the original typesetting on 10 November 2026.

The question defines the intermediate polynomials by

    w1(x) = x(x+alpha1)+beta1,
    wk(x) = w_(k-1)(x) (w1(x)+gamma_k x+alpha_k)
            + delta_k x+beta_k.

In the answer, u_r and v_r are the coefficients of wm and w_(m-1),
respectively. It sets a=alpha1+gamma_m and b=alpha_m, then uses the
coefficients of the reciprocal quadratic to claim v_r=f(r+2), where

    f(r) = sum_(i,j>=0) (-1)^(i+j) binom(i+j,j) u_(r+i+2j) a^i b^j.

But the factor multiplying w_(m-1) is

    x^2 + a x + (beta1+alpha_m).

Thus **b must be beta1+alpha_m**, rather than alpha_m. The constant
beta1 in w1 has been omitted.

A minimal explicit counterexample uses m=2, alpha1=gamma2=alpha2=0,
beta1=1, and delta2=beta2=0. These obey all stated parameter
restrictions, and give

    w1=x^2+1,   w2=(x^2+1)^2=x^4+2x^2+1.

The printed a=b=0 yields f(2)=u2=2, whereas v0=1. With the corrected
b=1, the same formula gives f(2)=u2-b*u4=1. This is an error in the
printed coefficient calculation; it does not refute Motzkin's
representation theorem. The free parameter alpha_m can absorb the
shift by beta1.

Checked all2-prepre, all2-pre, all2, err2 and current err2.textxt;
none contains a corresponding correction on 519 or 705. The older
second-edition errata for the neighboring answers and public searches
for Motzkin, Knuth, page 705 and exercise 4.6.4-39 also yielded no
matching report. Absolute priority and later physical printings are
unverified. No report has been sent. The counterexample is a direct
expansion; no numerical search is needed.
