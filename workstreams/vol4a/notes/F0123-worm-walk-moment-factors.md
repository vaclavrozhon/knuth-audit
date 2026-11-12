# Three intermediate binomial-moment formulas have incorrect factors

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–57, first paragraph, printed 796.

Define A_k=binom(2a,a-k)*binom(2b,b-k) and S_p(a,b)=sum_(k>=0) A_k*k^p, as in the exercise. All counterexamples below use positive parameters a=b=1, for which A_0=4 and A_1=1.

1. The displayed sum from k=a-m to a needs the denominator 2(a+b):

```
sum_(k=a-m)^a A_k*k
 = (m+1)(a+b-m)*binom(2a,m+1)*binom(2b,a+b-m)/(2(a+b)).
```

For a=b=1,m=0 the sum is 1 but the printed right side is 4. The correction follows by telescoping g(k)-g(k+1)=2(a+b)*k*A_k, with g(k)=(a+k)(b+k)*A_k.

2. The printed recurrence must read

```
b^2*S_p(a,b)-S_(p+2)(a,b) = 2b(2b-1)*S_p(a,b-1).
```

This follows termwise from (b^2-k^2)*binom(2b,b-k)=2b(2b-1)*binom(2b-2,b-1-k). For a=b=1,p=0, the left side is 5-1=4 and the printed right side is 2.

3. The third-moment expression must be

```
2*S_3(a,b) = binom(2a,a)*binom(2b,b)*a^2*b^2/((a+b)(a+b-1)).
```

The printed denominator (a+b)^2 gives S_3(1,1)=1/2 instead of 1. The corrected recurrence with p=1 and the correctly printed first moment give the repaired denominator directly. The displayed S_0, S_1, S_2, main formula (30), and the final odd-time worm-depth formula are correct; the latter follows from the corrected third moment.

Original typesetting inspected. No matching repair was found in the historical/current Volume 4A errata, refreshed Fascicle 4 errata or targeted public searches; see `../sources/tree-counting-source-check.json`. Absolute novelty is not established.
