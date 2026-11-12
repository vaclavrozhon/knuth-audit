# V4A-F0046: Support masks are compared with node indices

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), answer 7.1.4-197, printed page 659 / file 676. The original
image is `images/bookwise-p659.png`.

Here N[k,p] is a quasi-reduced decision-diagram node, d[k,p] is its
support bit mask, and zeta[k] is the index of the zero-function node
at level k, or -1 if that node is absent. A variable is supported
when some satisfying assignment sets it to one. The answer compares
d[k+1,h] with zeta[k+1] to decide whether the high child is zero. It
also tests d[k+1,l] = d[k+1,h] = zeta[k+1] to recognize a zero parent.
Both comparisons confuse a support mask with a node index.

The error already occurs at the last branching level. Both terminal
nodes have empty support, hence d[n,0] = d[n,1] = 0, while zeta[n] = 0.
For the ordinary function f(x1) = x1, its root has l=0 and h=1. The
printed first test fails, so the root receives support mask zero
instead of one. The second test succeeds and incorrectly labels
that root as the zero function. Thus this is not just a missing
optimization: the computed master-chart weights are wrong.

The two tests should instead be h != zeta[k+1] and
l = h = zeta[k+1]. The expressions using the child support masks to
form the new mask remain unchanged. A zero support mask alone cannot
distinguish the two terminal functions.

No matching correction was found in the relevant current and
historical 4A/Fascicle 1 errata or targeted public searches; see
`sources/zdd-basics-source-check.json`. This does not establish
absolute novelty. The counterexample was traced by hand.
