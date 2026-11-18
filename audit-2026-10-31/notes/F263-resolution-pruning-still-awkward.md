# F263 — One pruning step need not remove awkwardness

Confirmed in SAT answer 225, printed p. 592 (file 612), first edition,
second printing (November 2022). The definition and construction begin on
p. 591. The regularization theorem asked for in the exercise is correct.

A *resolution step on x* derives A OR B from x OR A and NOT x OR B.
A resolution tree records such steps, with its input clauses at the leaves.
It is *regular* when no variable is resolved on twice along a path. Answer
225 calls a tree for a clause A *awkward* if some resolution variable also
occurs in A.

The first paragraph claims that its construction immediately derives B1
with a non-awkward tree smaller than the original tree T. The size claim
holds, but the non-awkwardness claim need not. Consider these four distinct
ternary input clauses:

```
D1 =  x OR  y OR  z       D2 =  x OR NOT y OR  z
D3 = NOT x OR  y OR  z    D4 = NOT x OR  y OR NOT z.
```

Use the following seven-node tree:

```
D1       D2              D3       D4
  \     /                  \     /
 resolve y                resolve z
  x OR z                 NOT x OR y
       \                   /
             resolve x
              y OR z
```

The tree is regular: its paths resolve on y then x, or z then x. Both
proper nontrivial subtrees are non-awkward. Their respective conclusions
are x OR z and NOT x OR y, which do not contain their own pivots y and z.
The whole tree is awkward because its conclusion A = y OR z contains
both y and z. Thus the example satisfies exactly the assumptions at the
start of the printed construction.

Choose the left branch, with the book's indices

```
p = 2,   x1 = x,   x2 = y,
A0 = y OR z,   A1 = x OR z,   A1' = NOT x OR y,
A2 = D1,       A2' = D2.
```

The recipe sets B2 = A2 and resolves it with A1', giving

```
B1 = resolve_x(D1, NOT x OR y) = y OR z.
```

The proof tree for A1' still resolves D3 and D4 on z. Consequently the
new five-node tree is still awkward: it resolves on z, and z occurs in
B1. Choosing the symmetric branch first leaves the y-resolution instead,
so the other possible choice does not fix the problem in one step either.

A further pruning does work here: resolve D1 directly with D3 on x.
That three-node tree concludes y OR z and is non-awkward. This shows the
precise missing step: the printed construction gives a **smaller regular
tree**, after which size induction or further pruning is needed before
claiming non-awkwardness.

The next paragraph has the same omission when it says that resolving the
two non-awkward child trees produces the desired non-awkward tree. Take
its extra clause B to be empty and use the two children above. The result
is the original awkward seven-node tree. The preceding pruning lemma
must be applied if the combined regular tree is awkward. These are two
uses of the same missing cleanup, recorded as one finding.

The exact statement, not just extracted text, was checked on the original
book pages and in the author's September 23, 2015 draft, p. 228 (file 236).
The six current/historical errata layers and three current TeX sources
contain no matching correction. The April 19, 2020 correction on draft
p. 228 concerns answer 231's final axiom index, not this proof.
Focused public searches found no matching prior report; this does not
establish absolute priority. A later complete printing was not checked
and no report has been sent.

Evidence: `results/focused-resolution225-sources.json` and the page images
listed there. The displayed resolutions suffice; no solver, proof
enumeration, or new formalization was needed.
