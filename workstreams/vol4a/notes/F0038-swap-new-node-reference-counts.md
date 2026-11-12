# V4A-F0038: Swapping omits the new child's reference increments

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), answer 7.1.4-147, printed page 648 / file 665, the UNIQUE
modifications after Algorithm T. Originals: pages 647–648, with
Algorithm U on 227 and answer 82 on 633.

A BDD node (v,l,h) tests variable v and follows l on zero, h on one.
REF counts incoming references from live nodes or external roots.
The swapping algorithm removes references in T1–T2. It then calls
UNIQUE to install the new children in T4. The answer changes U1 and
U2 from answer 82 but leaves U3, creation of a new node, unchanged.
In answer 82, U3 sets the new node's count to one; its children already
have temporary references from the recursive computation. No such
temporary references exist in Algorithm T.

Take a single externally referenced root r and these nodes:

    a = (3,0,1), q = (2,a,0), r = (1,q,1).

Initially REF(a)=REF(q)=REF(r)=1. Swap levels 1 and 2. T1 lowers
REF(q) to zero. T2 recognizes q as hidden and lowers REF(a) to zero.
T4 creates two new nodes (2,a,1) and (2,0,1), then makes them the
children of r. Neither existed before. Following the stated U3
leaves REF(a)=0 even though the first new node points to a.
Thus the final assertion that every remaining node is alive fails;
subsequent garbage collection can reclaim a reachable node.

For the UNIQUE variant used by T4, creation in U3 must additionally
increment the reference counts of both children. These increments
are direct, matching the direct decrements in T1–T2; the temporarily
zero lower-level nodes have not had their descendants recursively
dereferenced. The new node still receives REF=1.

No matching erratum or public report was located in the screened
sources; see `sources/bdd-order-source-check.json`. Absolute novelty
is not established. The example was traced by hand, without code.

The ZDD adaptation in answer202, printed660 / file677, inherits the
same omission. For a valid ZDD witness take a=(3,0,1), q=(2,a,1),
r=(1,q,1), with only r externally referenced. T1–T2 again hide q
and reduce REF(a) to zero. T4 creates a child whose LO is a and
whose HI is the unit-family sink. The new-node case still leaves
REF(a)=0. The separate change to ZUNIQUE's reduction case in202
does not repair creation in U3. This is the same defect, not a
second finding; the relevant660/Fascicle1-226 errata were screened.
