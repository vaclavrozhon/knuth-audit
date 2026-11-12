# V3-C0069 — The general-alphabet successful-search expansion has two omissions

Confirmed in volume 3, second edition, first printing (1998), answer
6.3-28, printed p.726 (file p.737). Let C_N denote the book's barred
C_N, the expected total digit inspections for successful searches in
an M-ary digital search tree. Let U_N and alpha_M have the meanings
used in that answer and the preceding derivation.

First, C_N/N is equated to U_(N+1)-alpha_M+1+O(1/N), without dividing
U_(N+1) by N. U_N has order N log N, whereas a single search has order
log N. This already contradicts the immediately preceding binary
calculation in answer 27.

Second, the subsequent expanded expression retains the binary term
(log_M N)/N for every M. Its coefficient must be 1/(M-1). A corrected
expression, to the requested precision, is

    C_N/N = log_M N + (gamma-1)/ln M + 1/2 - alpha_M
            + delta_(-1)(N) + (log_M N)/((M-1)N) + O(1/N).

Gamma here is Euler's constant, and delta_(-1) is the small periodic
function already defined in exercise 19. The error in the coefficient
cannot be absorbed into O(1/N) for fixed M>2.

This follows directly from the product form used to obtain (14).
Put u_j=M^(-j), P_j=product_(r>=1)(1-M^(-j-r)), and
F_j=((1-u_j)^N-1+N u_j)/u_j. The generalized product identity gives
C_N=sum_(j>=0) F_j P_j, while U_N=sum_(j>=1) F_j.
Expanding the convergent product and summing the geometric series
gives alpha_M=sum_(j>=0)(1-P_j), in agreement with the answer's series.
Consequently

    C_N-U_N-(1-alpha_M)N
      = -1 + sum_(j>=0) [1-(1-u_j)^N](1-P_j)/u_j.

For fixed M, (1-P_j)/u_j=1/(M-1)+O(u_j). The O(u_j) terms have bounded
sum, and sum_(j>=0)[1-(1-u_j)^N]=log_M N+O(1), the standard sum already
used in the chapter. Hence the displayed difference is
(log_M N)/(M-1)+O(1), proving the corrected coefficient. Combining
this with the book's expansion for U_N gives the formula above.

A short evaluation for M=3 confirms the predicted half coefficient;
see `results/digital-generalization-local-check.json`. This numerical
check supports the algebra and is not used as its proof. The
unsuccessful-search expansion, including the pending reference from
5.2.3-37, is unaffected at its stated O(1/N) precision.

Original p.726 and an enlarged crop checked and retained. No matching
correction was located in the official layers or limited public
searches; see `sources/digital-searching-errata-review.json`.
