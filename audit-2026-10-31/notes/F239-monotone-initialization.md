# F239 — Negative input literals break the claimed monotone circuit

Confirmed in Volume 4B, answer 428(b), printed 634/file 654; author draft270.
An input x_ij indicates whether edge ij is present. A monotone Boolean
chain uses only monotone operations, as defined in exercise7.1.2–84:
raising an input from0 to1 cannot lower a signal. The printed initialization
sets g_(not x_ij,0)=not x_ij, so it needs a negation at the input. That signal
falls from1 to0 when the edge input rises. Although later rounds use only
AND and OR, this does not construct the monotone chain requested.
The final graph function is monotone; that fact does not make the printed
intermediate construction a monotone chain.

Repair the initialization to assert only present edges:

    g_(x_ij,0) = x_ij;
    every other g_(l,0) = 0.

Here g_(l,t) means that unit propagation has derived literal l after t
rounds. Leave absent-edge variables unassigned. Under those facts, y is
implied exactly when the graph consisting of the present edges has no
d-coloring: if it has a coloring, set every remaining edge to0 and use
that coloring with y=0; if it has none, adding edges cannot help. The
forcing property of G therefore still derives y in at most N rounds.
The partial assignment is always consistent, since y=1 and all color
variables zero extend it to a model. Consequently the unchanged recurrence
now gives a monotone circuit computing the required function.

All products omitting one literal of a clause can be shared through prefix
and suffix products, keeping one round within O(MN) binary operations and
the stated total O(MN^2). The lower-bound consequence is unchanged.
The known 2020 correction to the time range, 0<=t<N, is already incorporated
and is unrelated to the initialization error.

Original Volume 4B typesetting and the September 23, 2015 author draft were
inspected. Current and historical 4B/Fascicle 6 errata and their available
TeX sources contain no matching correction. Focused public searches found
no relevant correction; absolute priority is not claimed. See
sources/bookwise-forcing-source-check.json for the checked ranges.
