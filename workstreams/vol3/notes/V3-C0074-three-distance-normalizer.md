# V3-C0074 — The interval normalizer uses the wrong continued-fraction tail

Confirmed in volume 3, second edition, first printing (1998), answer
6.4-9, printed p.729 (file p.740).

The answer defines theta_k as the continued-fraction tail beginning
with a_(k+1), and prints Q_k=q_k+q_(k-1)*theta_(k-2). The last index
must be k-1. Here q_k are the denominators defined in exercise 8;
Q_k is the common denominator in the three displayed interval lengths.

For a direct witness take theta=1/sqrt(2)=//1,2,2,...//. Then q_1=q_2=1,
theta_0=1/sqrt(2), and theta_1=sqrt(2)-1. Just before the second point
is inserted, k=2, r=1, s=0. The third interval has length theta.
The printed formula instead gives 1/(1+1/sqrt(2)). Replacing theta_0
by theta_1 gives the required 1/sqrt(2).

The common denominator cancels in the ratio used in the remainder of
answer 9, so the final classification of good breaks survives. The
two known 1998 corrections to exercise 8 concern the signs and the
positive fractional-part convention, not this denominator.

Original p.729 and enlarged crop inspected. No matching correction
located in the official layers or limited public searches documented
in `sources/hashing-errata-review.json`.
