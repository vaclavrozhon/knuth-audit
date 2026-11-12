# V3-C0034 — Leftist-tree generating functions use incompatible size conventions

Confirmed, medium. Volume 3, second edition, first printing (1998),
answer 5.2.3-34, printed p. 645 / file p. 656. The exercise on p. 157
counts actual record nodes, excluding null links. The answer mixes this
convention with the number of external leaves, which is one larger.

Let t_N count the trees requested in the exercise, with t_0 = 1, and let
T(z) = sum(t_N z^N) be their ordinary generating function. Its beginning is

```
T(z) = 1 + z + z^2 + 2z^3 + 4z^4 + 8z^5 + ... .
```

For example, the two trees with three nodes are a chain of left children
and a root with two children. Both satisfy the leftist condition: at each
node, the shortest path to a null link in the left subtree is at least as
long as the corresponding path in the right subtree.

The printed auxiliary recurrences start with L_1(z) = z and imply

```
L(z) = z + z^2 + z^3 + 2z^4 + 4z^5 + ... = z T(z).
```

They therefore count external leaves, not record nodes. The auxiliary
index is also shifted: these L_m enumerate ordinary DIST = m-1, where
DIST is the book's shortest distance to a null link. In particular,
L_1 = z represents the empty tree with one external leaf; it cannot
represent all trees of DIST = 1.

There is an immediate contradiction even without choosing a convention
for the empty tree. The answer sets G(z) = z L(z) and then states
G(z) = z + G(z G(z)). The recurrences give G(z) = z^2 + O(z^3), whereas
the latter equation requires coefficient 1 on z. These two statements
cannot both hold.

A consistent repair uses F(z) = z T(z) in place of L(z) throughout the
Kemp recurrences, and then states F(z) = z + F(z F(z)) directly. The
constant a in the exercise's node-count asymptotic must also change.
Kemp's leaf-count constant alpha is about 0.250363429, with exponential
base b about 2.749487902. Since t_N counts trees with N+1 external leaves,

```
t_N ~ alpha * b^(N+1) * (N+1)^(-3/2)
    ~ (alpha*b) * b^N * N^(-3/2).
```

Thus the requested a is about 0.68837122, not 0.25036. The exponential
base and exponent -3/2 remain correct.

The original exercise and answer were inspected and saved in
`images/bookwise-p157.png` and `images/bookwise-p645.png` relative to the
volume workstream. All five author errata layers were checked against
fresh matching downloads on 2026-11-10; see
`sources/selection-errata-review.json`. The first-edition replacement
answer dated 15 March 1995, p. 620, already contains the incompatible
formulas. No matching correction appears in the later layers.

Primary-source cross-checks:

- Rainer Kemp, *A note on the number of leftist trees*, Information
  Processing Letters 25 (1987), 227–232. The indexed original abstract
  explicitly counts leaves and gives alpha and b above:
  https://oeis.org/A006196/a006196_1.pdf . Full PDF retrieval failed;
  no claim of a full independent review of this paper is made.
- P. Nogueira, *On the combinatorics of leftist trees*, Discrete Applied
  Mathematics 109 (2001), 253–278,
  https://doi.org/10.1016/S0166-218X(00)00250-X . Pages 254–257 distinguish
  actual nodes from null links and give the node-count generating
  function and its shifted functional equation. Proposition 9 on
  p. 263 gives the prefactor 0.68837122. The author-repository PDF is
  saved as `sources/nogueira-2001-leftist-trees.pdf`.

The contradiction and size shift above are direct checks of the book;
we do not reprove the cited singularity analysis. Targeted public
searches found no report explicitly correcting this answer. The
correct convention and constant are already in the literature; no
absolute priority for noticing the book's error is claimed.
