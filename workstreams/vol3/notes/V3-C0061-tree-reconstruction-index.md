# V3-C0061 — Recursive tree reconstruction loses the parent index

Confirmed algorithm error in volume 3, second edition, first printing
(1998), answer 6.2.3-10, printed p.715 / file p.726.

The routine TREE(hmax) reconstructs a tree from balance factors listed
in symmetric (inorder) order. Its index k is shared by recursive calls;
only h, h-prime and Q are declared local. After the call that constructs
the right subtree, it sets Q to X_k. That call may have advanced k,
so X_k need no longer be the parent being constructed.

Take three nodes X_1, X_2, X_3 with balance factors 0,0,0. Their unique
AVL tree has root X_2 and children X_1 and X_3. The printed procedure
first constructs X_1. At k=2 it attaches X_1 on the left and invokes
TREE(1) to construct the right subtree. That call consumes X_3 and
returns it with the shared index k=3. The outer assignment Q=X_k then
sets Q to X_3, and the routine returns X_3 instead of X_2.

This failure remains even if the target of the right-link assignment
is evaluated before its recursive right-hand side, the most favorable
interpretation. Evaluating that target afterward can also set X_3's
right link to itself.

Save the current node in a local pointer R=X_k before recursing. Use
R for both link assignments and set Q=R afterward; k should remain
global to record the consumed input. This is a local repair to the
printed routine, not a counterexample to the reconstruction theorem.

Original p.715 was viewed and retained as `images/bookwise-p715.png`.
The 18 February 1995 first-edition replacement (p.675) has the same
shared-pointer defect; it is not a correction of it. No repair was
located in the other official layers or targeted public searches.
See `sources/balanced-trees-errata-review.json`.
