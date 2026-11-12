# V3-C0059 — The 2022 AVL height bound fails for two nodes

Confirmed defect in the official volume 3 errata, `all3-pre`, PDF
p.8: the 1 January 2022 replacement of `N+2` by `N+1.063` in
Theorem 6.2.3A (book p.460). This is an errata finding, not a claim
that the original additive constant 2 is wrong.

Here N counts internal nodes and height counts edges from the root
to an external node. A root with one internal child is an AVL tree
with N=2 and height 2. After applying both the known 1998 coefficient
correction (1.4404 to 1.4405) and the 2022 additive correction, the
stated upper bound becomes

    1.4405 lg(2+1.063) - 0.3277 = 1.9986288010725617 < 2,

where lg is the base-two logarithm. Thus the corrected theorem fails
on a nonempty, ordinary two-node tree.

The accompanying Binet-formula argument has remainder
phi^(-4)/sqrt(5) = 0.06524758424985277, where
phi=(1+sqrt(5))/2. It does not justify replacing that remainder by
0.063. Restoring N+2 is sufficient. For nonempty trees, N+1.066 is
also a safe replacement: the displayed Binet bound applies for
height at least 2, and the one-node case is direct.

The original book page and the actual errata typography were viewed.
Evidence: `images/bookwise-p460.png` and
`images/bookwise-avl-errata-p8.png`. All five official errata layers
and targeted public searches were screened; no correction of this
2022 defect was located. See `sources/balanced-trees-errata-review.json`.
Absence from these searches is not a claim of absolute priority.
