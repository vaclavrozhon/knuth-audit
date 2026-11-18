# C008: a stable assignment need not be covering

Confirmed on November 17, 2026, under the existing candidate ID. The confirmed
scope is the terminology in the parenthesis of answer 7.2.2.2–361, printed
p. 619 (PDF file page 639), in the supplied first edition, second printing.

A **stable partial assignment** satisfies every clause or leaves at least two
unassigned literals in each unsatisfied clause (exercise 363, p. 349). An
assigned variable is **constrained** when it supplies the only true literal
of a clause whose remaining literals are false. A **covering assignment**
is stable and has every assigned variable constrained (exercise 364, p. 350).

Answer 361 correctly allows all stable assignments in its description of binary
fixed points with reinforcement messages. Its parenthesis then calls those
assignments “covering” and points to exercise 364. That identification is false.

## Two-variable witness

Take the single clause C = (x OR y) and assign x = y = 1. This is stable, but
neither variable is constrained: C has two true literals. Thus it is not a
covering assignment according to the explicitly referenced definition.

It really does occur among the fixed points requested in exercise 361. Write
eta_l for a reinforcement message, eta_(C->l) for a clause message, pi_l for
the flexibility coefficient in (154), and gamma_(l->C) for the bias in (156).
Choose

```text
eta_x = eta_y = 1,  eta_(NOT x) = eta_(NOT y) = 0,
eta_(C->x) = eta_(C->y) = 0.
```

Then (154) gives pi_x = pi_y = 0 and pi_(NOT x) = pi_(NOT y) = 1.
In (156) both bias messages are zero, with denominator 1. Equation (157)
therefore returns the same two zero clause messages. Both variable fields
are (truth, falsity, wildness) = (1, 0, 0). All messages are binary and all
denominators are defined. Even reinforcement update (158) fixes this state
when its strength kappa is 1.

Consequently the example cannot be excluded by the fixed-point equations or
by an implicit admissibility restriction. Replace “covering” by “stable” and
refer to exercise 363, or explicitly distinguish the covering subclass.
The equations and their fixed-point classification need no change for this
particular error. Severity is low: this is an incorrect identification of
two defined mathematical classes.

## Assessment change and source checks

The earlier C008 entry combined this issue with an omitted restriction on
reinforcement messages. That separate omission can reasonably be read as
implicit in (154); it is not the basis for confirmation. The two-variable
example already appeared in `SURVEY_NOTES.md`. This is a narrower reassessment
of existing direct evidence, not a claim that the example was newly found.

The original p. 619, the definition on p. 350, and the corresponding answer on
p. 255 of the author's September 23, 2015 draft were visually compared. The
same mistaken identification appears in both editions examined. The current
and historical 4B, Fascicle 5, and Fascicle 6 errata contain no matching
correction. The known change from strict to definite Horn clauses on p. 350
concerns exercise 363(g), not this issue. Targeted public searches did not
locate an earlier report. Absolute priority and a later complete printing
have not been established; no report has been sent.

Source-check record: `../results/focused-covering361-sources.json`.
