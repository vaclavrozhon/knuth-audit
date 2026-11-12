# V3-C0068 — Two forest recurrences omit the other branches' multiplicity

Confirmed in volume 3, second edition, first printing (1998), answer
6.3-24, printed p.725 (file p.736).

In both reductions from the multinomial recurrence to a binomial
recurrence, the summand lacks (m-1)^(n-k). The correct expressions are

    x_n = a_n + m^(1-n) sum_k binom(n,k)(m-1)^(n-k) x_k,
    y_n = b_n + m^(1-n) sum_k binom(n,k)(m-1)^(n-k) y_k.

Here m is the alphabet size, x_n counts forest nodes on average, and
y_n counts the specified right-link operations over all searches.
Once k keys have been assigned to one branch, each remaining key can
go into any of the other m-1 branches. Equation (4) on p.502 includes
this same factor correctly.

For a concrete check, take m=3. The n=2 recurrence gives x_2=5/2.
For n=3, a_3=19/9. The printed binomial formula then gives
x_3=19/9+(3x_2+x_3)/9=53/16. The multinomial formula on the preceding
line instead gives x_3=19/9+(6x_2+x_3)/9=17/4. Thus the two displayed
equalities cannot both hold. They agree in the binary case m=2, which
hides the omission. The later result x_N=A_N+N-1 uses the correct form.

Original p.725 and an enlarged formula crop checked and retained.
No matching correction was located in the official layers or limited
public searches; see `sources/digital-searching-errata-review.json`.
