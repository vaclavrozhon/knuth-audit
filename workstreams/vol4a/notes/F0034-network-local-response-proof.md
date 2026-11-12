# V4A-F0034: Global uniqueness does not supply the local response used in Theorem M

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011). Theorem M proof, printed pages 214–215: existence of A(b) in (31).

The hypothesis on page 214 requires exactly one consistent assignment
of all wire signals for each external input. It does not require the
port-dependency graph to be acyclic or each isolated part to have a
unique response to arbitrarily fixed boundary inputs.

Here is a network of three modules meeting the stated hypothesis.
All variables below are bits and xor denotes exclusive OR. Let u run
from M1 to M2, v from M2 to M1, a from M2 to M3, and b from M3 to M2.
Define the module outputs by

    M1: u = v                       (x1 is unused)
    M2: v = u xor b,  a = u          (x2 is unused)
    M3: b = a xor x3,  f = a.

Every module computes Boolean functions of exactly its available
inputs; unused external inputs are permitted. The first two equations
force b=0. The remaining equations then force a=u=v=x3. Thus for every
(x1,x2,x3), all wires have exactly one consistent assignment.

Cut between M2 and M3. The left side has fixed inputs (x1,x2). For the
same backward signal b=0, it admits both a=0 and a=1, and these two
possibilities are actually selected by x3=0 and x3=1, respectively.
Consequently there is no function A of b, determined solely by the
left inputs, that gives the boundary value a for both external inputs.
With b=1 the isolated left side has no consistent assignment at all.

This contradicts the step introducing A(b)=a in (31), on which the
truth-table transmission on page 215 relies. It does not contradict
the asserted BDD-size bound: this example computes f=x3, whose BDD is
small. A sufficient extra premise for this step is acyclic dependence
of output ports on input ports; alternatively the proof would need to
handle relations, including missing and multiple responses. No claim
is made here that the theorem is false or that its best repair has
been determined.

Original page images and the relevant current/historical Volume 4A and
Fascicle 1 errata were checked. No matching correction or public report
was located; absolute novelty is not established. See
`sources/bdd-basics-source-check.json`. The counterexample was checked
by hand; no general verifier or census was used.
