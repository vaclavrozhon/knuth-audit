# The ballot-number specialization has too many leaves

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–37, parenthesis after the first displayed formula, printed 791.

The answer says that the forest count C(n) specializes to the ballot number C_pq^(t) of answer 36 when n_0=(t-1)q+1 and n_t=p. Here n_0 counts leaves and n_t counts nodes of degree t.

There are q zero degrees in the ballot word, with one final zero appended to obtain the forest degree sequence. Thus n_0 must be q+1. Direct substitution into the displayed forest formula gives

```
C(q+1,0,...,0,p) = (q-(t-1)*p+1)/(q+1) * binomial(p+q,p),
```

exactly the formula in answer 36. For t=3,p=1,q=2, that ballot number is 1. The printed substitution instead has five leaves and one ternary node, giving 3 forests. This numerical contradiction is independent of the initialization omission in answer 21.

Original typesetting inspected. Historical/current Volume 4A and refreshed Fascicle 4 errata and targeted public queries yielded no matching correction. See `../sources/tree-gray-generators-source-check.json`; absolute novelty is not established.
