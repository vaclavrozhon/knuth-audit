# V4A-F0050: Postorder changes the forest ZDD

Confirmed, low severity. Volume4A, first edition, first printing
(2011), answer7.1.4-224, printed667 / file684. Original:
`images/bookwise-p667.png`.

The answer identifies the ZDD's high pointers with first-child
links and its low pointers with next-sibling links. It then lists
preorder, postorder and level order as orders of the arcs that leave
this ZDD unchanged. Postorder visits children before their parent
and does not preserve the described diagram.

Take the directed tree with arcs a:s->r, b:r->u, c:r->v, where u and
v are leaves. Its source has out-degree one and its sinks have
in-degree one, as required in the main text. The path family is
{{a,b},{a,c}}. Write a node as (variable, low child, high child),
with0 denoting the empty family and1 the unit family.

In preorder a,b,c, the three nodes are

    C=(c,0,1), B=(b,C,1), A=(a,0,B), root A.

In postorder b,c,a, they are instead

    A=(a,0,1), C=(c,0,A), B=(b,C,A), root B.

The latter diagram has a shared nonsink A with two incoming edges;
the former's nonsink nodes form a tree. Even their shapes therefore
differ, not merely their variable labels. The stated correspondence
works for orders consistent with the child/sibling links, including
preorder and level order. Remove postorder from the examples.

No matching correction was found in the screened current/historical
4A/Fascicle1 errata or targeted public reports; see
`sources/zdd-dictionaries-paths-source-check.json`. Absolute novelty
is not established. Both tiny diagrams were traced by hand.
