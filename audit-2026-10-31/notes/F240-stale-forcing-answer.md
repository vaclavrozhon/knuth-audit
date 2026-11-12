# F240 — Answer432 refers to removed encodings and uses an obsolete counterexample

Confirmed in Volume4B, answer432, printed634/file654. The answer distinguishes
404(a) and404(b), but the 2022 replacement of404, already incorporated in this
volume, has only one encoding. Its clauses, for order bits x^j=[x>=j] and
y^j=[y>=j] with 0<=x,y<d, are

    (not x^j or x^(j+a) or not y^j or y^(j+a)), 0<=j<=d−a,

with the constant endpoint literals omitted. The old alleged failure,
a=2 and not x^2 failing to imply y^2 by unit propagation, no longer holds:
the j=0 clause is exactly (x^2 or y^2), so it immediately implies y^2.
The historical draft does have two encodings, explaining the stale text.

The correct answer to the current exercise is still no in general, but it
needs a different example. Set d=4,a=2, and assume x^1=1,y^3=0. Numerically,
x is in{1,2,3} and y in{0,1,2}; the only pairs satisfying |x−y|>=2 are
(2,0),(3,0),(3,1). Thus x^2 must be1. Yet the complete residual formula,
including the order axioms, consists of five binary clauses:

    (not x^3 or x^2)  (not y^2 or y^1)
    (x^2 or y^2)      (x^3 or not y^1)      (not x^2 or not y^2).

There is no unit clause, so propagation derives nothing further.
The fixed clause reduction and nine possible numerical pairs were checked
in results/bookwise-sat432-433-fixed-check.json. Replace the obsolete
paragraph by this answer, or retain the old comparison only with the old
encodings explicitly restated. This reports the stale answer432, not the
already published 2022 correction to404 itself.

Original typesetting and the corresponding September23,2015 author draft
were inspected. Relevant current/historical 4B and Fascicle6 errata, including
available TeX sources, contain no correction of this answer. Focused public
searches found no relevant report; absence is not a guarantee of priority.
See sources/bookwise-automata-source-check.json.
