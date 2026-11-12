# V4A-F0010 — bent-function generalization permutes the wrong half

Confirmed, medium. Volume 4A, first edition/first printing (2011), printed
page 560 / file page 577, answer 7.1.1–132(b), final parenthesis.
The original image was checked at full readable resolution:
`images/first100-answer560-large.png`.

Write u=(x1,x3,x5), v=(x2,x4,x6). The proposed generalization has the
form g(u)·v XOR h(v), with g an arbitrary permutation. This need not
be bent. The issue persists after repairing the separate inconsistent
dimension notation in that parenthesis.

Take the involutive permutation

    g(a,b,c)=(a,b,c XOR ab),       h(v1,v2,v3)=v1 v2.

The resulting six-variable function is

    f=x1 x2 XOR x3 x4 XOR x5 x6 XOR x1 x3 x6 XOR x2 x4.

It agrees with the affine function x5 at **40 of 64** inputs. A bent
six-variable function may agree at no more than **36** points, by the
definition in the exercise. Thus the supplied construction fails.

A short exact check of these 64 inputs and of the eight permutation
images is saved in `results/first100-bent-generalization.json`. No search
over candidate permutations or functions was run. The independent short
algebraic check is as follows. In the Walsh coefficient at x5, sum first
over x5: only x6=1 survives and contributes a factor 2. The remaining
exponent is x1 x2+x3 x4+x1 x3+x2 x4=(x1+x4)(x2+x3).
Of the sixteen assignments to these four variables, twelve have exponent
zero and four have exponent one. The Walsh coefficient is therefore
2(12−4)=16, giving (64+16)/2=40 agreements.

The valid generalization is **u·g(v) XOR h(v)**. Alternatively, keep
g(u)·v and change the final term to h(u). The permutation and the arbitrary
extra function must use the same half. With 2m total variables the
permutation acts on m-bit vectors; with n total variables it acts on
n/2-bit vectors. The printed x_(2n−1), x_(2n), and “2^(n/2)-bit” wording
is dimensionally inconsistent as well. These are recorded with the same
correction, not counted as additional findings. The exercise's original
identity-permutation construction remains valid.

Novelty check, 7 November 2026:

- Fresh byte comparisons of all4a-pre, all4a, err4a and current err4a TeX
  match the archive; see `integration/2026-11-07-first100/errata-recheck.json`.
- All five relevant 4A/Fascicle0 correction layers were searched. The
  existing 8 August 2011 correction adds y0 to the first part of 132(b);
  it does not change the parenthetical generalization. The 2021 addition
  concerns the odd-dimensional discussion on page 561.
- Public searches for Knuth/TAOCP with 560, 132, bent, permutation and
  Maiorana did not locate a report of this error. This is a limited
  search, not a guarantee of priority or an inspection of later printings.
- The standard form is also stated by the authors of
  [On cubic-like bent Boolean functions](https://link.springer.com/article/10.1007/s10801-025-01415-5).
  The counterexample and its verification above are independent of that citation.

Only the answer page receives the error marker. No message was sent.
