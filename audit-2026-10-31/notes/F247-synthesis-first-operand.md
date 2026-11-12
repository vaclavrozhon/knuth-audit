# F247 — The first-use symmetry clauses omit the first operand position

Confirmed in Volume 4B, answer 478, printed 642/file 662.
The selection variable s_ijk means that gate i uses operands j < k.
For interchangeable inputs p < q, the text says its clauses ensure that
p is used before q, allowing their first uses at the same gate. However,
the displayed clause family only handles s_ijq: q as the second operand.
It omits gates s_iqk, where q is the first operand.

A complete two-gate counterexample uses n = 3, p = 1, q = 2:

    x4 = x2 AND (NOT x3)
    x5 = x1 AND x4.

The output x1 AND x2 AND (NOT x3) is invariant under swapping inputs 1
and 2, and under no other ordinary input transposition. Input 2 is first
used at gate 4; input 1 first appears at gate 5. Nevertheless both selected
pairs, (2,3) and (1,4), avoid the displayed antecedents with second operand
2. All those clauses are satisfied. The pairs are already in colexicographic
order, both gates are nontrivial normal gates, every gate is used, and no
operand is reapplied. Thus the other optional restrictions do not remove
the example.

Let E(i,p) be the disjunction of all selection variables for gates before
i that use operand p. Besides the printed clauses, add

    (not s_iqk or E(i,p))  for q < k < i.

This excludes the counterexample and covers the missing operand position.
The printed family remains a sound, weaker symmetry restriction; it can
leave avoidable search work but does not invalidate SAT/UNSAT answers.

Original Volume 4B typesetting and the September 23, 2015 author draft,
answer page 278, both contain this defect. Relevant current and historical
4B/Fascicle 6 errata were checked, including available TeX sources. Focused
public searches found no matching report; this does not establish absolute
priority. See sources/bookwise-synthesis-source-check.json.
