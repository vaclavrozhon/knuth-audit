# Wrong constant in the count of near-perfect paths

Volume 4A, first edition, first printing (2011), answer 7.2.1.3–33,
printed page 730, file page 747.

Let f(k) be the coefficients of F(z) = 1/(1-z-z^3), as defined in the
answer. Thus f(0)=f(1)=f(2)=1 and f(3)=2. The first paragraph claims that
the sum over endpoints `0 <= i < j < n` is

```
3 f(n) + f(n-1) + f(n-2) + 2 - n.
```

For n=3 this is 7, although the three endpoint pairs each admit one
path. Doubling the displayed expression would give 14 paths instead
of the six permutations of three positions. Every such permutation
is near-perfect and is in index-list genlex order when t=1.

The constant must be **-2**, giving, for n >= 2,

```
S_n = 3 f(n) + f(n-1) + f(n-2) - 2 - n.
```

Indeed, partitioning the endpoint pairs according to whether neither,
one, or both endpoints are boundary positions gives the generating
function

```
sum_{n>=2} S_n z^n
  = F(z) [z + 2z^3/(1-z) + z^5/(1-z)^2] - z
  = (3+z+z^2) F(z) - 1 - z - (2-z)/(1-z)^2.
```

The corrected formula gives the t=1 column 2,6,12,20,34 after doubling,
in agreement with the table below it. The printed formula overcounts
by eight after doubling.

There is also a reversed inequality in the same paragraph's explanation
of doubling: replace its final `j > i` by `j < i`. The former repeats
the endpoint condition already summed. Reversal gives the missing paths.

The original page image confirms both errors. The current and historical
4A and Fascicle 3 errata and targeted public searches contain no matching
correction found in this review. See
`../sources/chase-combinations-source-check.json`; absolute novelty is
not established.
