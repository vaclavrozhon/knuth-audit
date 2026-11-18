# F262 — Delete the lifted clause in the minimality proof

Confirmed as a local notation error in SAT answer 206, printed p. 588
(file 608), first edition, second printing (November 2022). The theorem in
exercise 206 remains correct.

Let F and F' be clause sets on disjoint variables. Exercise 205 forms their
join G by introducing a fresh variable x, replacing selected clauses C of F
by x OR C, and selected clauses of F' by NOT x OR C'. At least one clause
on each side is replaced. A formula is *minimally unsatisfiable* if it has
no satisfying assignment but deleting any one of its clauses makes it
satisfiable.

The last sentence of answer 206 tries to infer minimality of F from
minimality of G. Starting with a redundant clause C of F, it writes the
deletion in G as

```
G \ (C | NOT x).
```

The conditioning operation `|` was defined on p. 211: setting a literal
true deletes satisfied clauses and removes its opposite from other clauses.
Since x is fresh, C contains neither x nor NOT x. Thus C conditioned on
NOT x is just C. If C was one of the replaced clauses, however, G contains
x OR C instead. The printed deletion can therefore remove nothing at all.
It does not supply the one-clause deletion needed to contradict minimality.

For a concrete nonempty example, take

```
F  = {a, NOT a},       F' = {b, NOT b},
G  = {x OR a, x OR NOT a, NOT x OR b, NOT x OR NOT b},
C  = a.
```

Here G is minimally unsatisfiable. For x=0 its first two clauses conflict;
for x=1 its last two clauses conflict. Each individual deletion is
satisfiable. For example, deleting x OR a permits x=0, a=0, with either
value of b. But `C | NOT x` is a, which is absent from G. Deleting that
expression leaves all four clauses and hence leaves the contradiction.

This example distinguishes the two deletion operations; it is **not** a
counterexample to the theorem or to the conditional assertion that a
redundant C leaves an unsatisfiable formula. The defect is the attempted
use of the wrong deletion to establish minimality.

A precise repair is to name the clause of G that arose from C:

```
C_hat = x OR C, if C was replaced; otherwise C_hat = C.
If F \ C is unsatisfiable, then G \ C_hat is unsatisfiable.
```

Indeed, a satisfying assignment to the latter formula would satisfy
F minus C when x=0, or F' when x=1. Both possibilities are excluded at
this point in the proof. Since C_hat is a clause of G, the contradiction
with minimality now follows. Merely replacing the printed expression by
x OR C in every case would overlook clauses that were left unmodified.

The operator and complemented x were visually checked in the original
book and in the author's September 23, 2015 draft, p. 224 (file 232). The
relevant definition and the partially replaced join on p. 334 were also
read. The six current/historical errata layers and the current TeX sources
contain no matching correction. The p. 588 update dated July 22, 2024 is
about answer 205's research reference, not answer 206's deletion.
Focused public searches found no matching report. Absolute priority and
the text of a later complete printing have not been established; no report
has been sent.

Evidence: `results/focused-minimality206-sources.json` and the original-page
images named there. No computation was needed for this three-variable
example.
