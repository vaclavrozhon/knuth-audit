# V2-C0261: missing normalization in the induced-series proof

Confirmed proof error, low impact. Third edition, first printing,
answer 4.7-22(c), printed 723/file 735, paired with the question on
535. Both original pages inspected on 10 November 2026.

For a series U with nonzero constant term U0, its induced series
U^{alpha}=V is defined by V(z)=U(z*V(z)^alpha). Braces distinguish
this operation from iteration by composition. The answer proves the
coefficient identity first for infinitely many alpha, then says that
the coefficients of V(z)^x are polynomials in alpha. Under the stated
assumption U0!=0, that assertion is false.

Take U(z)=2+z and x=1. Comparing constant and linear terms in
V(z)=2+z*V(z)^alpha gives

    V(z)=2+2^alpha*z+O(z^2).

Its linear coefficient is exponential in alpha, not polynomial. The
example uses a positive real constant, so no branch ambiguity is
involved. An identity at infinitely many parameter values alone does
not supply the polynomial-identity argument printed in the answer.

The requested coefficient identity remains correct. Normalize before
using that argument: write U(z)=c*F(z), where c=U0 and F(0)=1, and let
G=F^{alpha}. Direct substitution gives

    U^{alpha}(z)=c*G(c^alpha*z),
    [z^n] U^{alpha}(z)^x
      = c^(x+n*alpha) * [z^n] G(z)^x.

The same factor c^(x+n*alpha) occurs on the other side of the claimed
identity. After cancelling it, both sides are polynomials in alpha,
so the proof works for F(0)=1 and then transfers back to U. The book
already performs the analogous normalization by V1^n in exercise
21(b); that correctly printed factor is not an error.

The original question and answer, all current/historical third-edition
errata and the second-edition changes were checked. No correction of
this proof step was found. Targeted public searches on the induced
function, polynomial-in-alpha claim and Knuth errata found no matching
report. Absolute priority and later physical printings are unverified.
No report sent; no computation needed.
