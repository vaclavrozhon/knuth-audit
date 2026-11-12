# V2-C0262: the online composition route needs a nonzero linear coefficient

Confirmed missing algorithmic precondition, low impact. Third edition,
first printing, answer 4.7-11, printed 720/file 732, second paragraph.
Question on printed 533. Original typesetting inspected on
10 November 2026.

The exercise asks to compose arbitrary power series U(V(z)) with
V(0)=0. Its first, offline algorithm works in that domain. The
subsequent online construction says to normalize V1 to 1 by replacing
U_k with U_k*V1^k and V_k with V_k/V1, revert V by Algorithm L, and
feed the inverse into Algorithm G. This route requires V1!=0, an
assumption not made in the exercise or that paragraph.

For example U(z)=1/(1-z) and V(z)=z^2 are valid inputs, and their
composition is 1/(1-z^2). The proposed normalization divides by zero,
and V has no compositional inverse as an ordinary power series. If
H(0)=0, every nonzero term of H(z^2) has even degree, so H(V(z))
cannot equal z. Thus the inverse-based route does not handle these
inputs. The restriction is substantive for this algorithm, even
though the original composition problem and the first algorithm
remain valid.

Qualify the online paragraph with V1!=0, or provide a separate method
for the zero-linear-coefficient case. This note does not assert that
the stated online time or storage bounds are impossible by another
method. In the first paragraph, the explanatory sentence also prints
T(z)=V(z)^N where the loop invariant is T(z)=V(z)^n at the start of
iteration n, on the coefficient range being used. Its N should be n;
the update itself is correct.

All four third-edition errata lists, current TeX and the older
second-edition list were checked. The earlier double-reversion
notation correction on second-edition page 657 is unrelated. Public
searches on composition, this page and Knuth errata found no matching
report; a public implementation of the first offline algorithm does
not address the online restriction. Absolute priority and later
physical printings are unverified. No report sent; no computation
needed.
