# F261: drain deferred units inside the propagation loop

Confirmed in answer 7.2.2.2–175, printed p. 581 / PDF page 601, in the supplied
first edition, second printing. The faulty insertion is the temporary-stack
processing placed immediately before the final line of routine (72).

Routine (72), p. 227, maintains a queue R of assigned literals. E is its end,
and G points to the next literal whose effects on nonbinary clauses need to be
processed. Binary propagation, routine (62), appends new assignments to R.
The loop continues while G < E. Its final line, outside the loop, adds the
binary implications discovered during the lookahead.

Answer 175 adapts this routine to clauses of arbitrary length. A clause that
has only one unassigned literal left puts that literal on a temporary stack.
The answer postpones processing this stack until after the queue loop. Binary
propagation of these deferred units can increase E, but the loop has already
finished. Consequently their effects on nonbinary clauses are missed. This
can make step X9 incorrectly classify an assignment as a conditional autarky:
an assignment safe to impose whenever its parent literal is true.

The repair is to clear the temporary stack and conflict flag for each processed
literal L, scan all clauses containing NOT L, and then handle the flag and
drain that stack **inside the G < E loop**, before its next iteration. The
resulting new queue entries will then be processed. This is how the author's
SAT11K implementation is organized.

## Seven-variable counterexample

Use Boolean variables a,b,c,d,e,u,v, with 0 meaning false and 1 meaning true.
An OR expression below is one clause; all ten clauses must hold:

```text
(a OR NOT b)
(NOT a OR NOT b OR c)

(NOT c OR d     OR e)
(NOT c OR d     OR NOT e)
(NOT c OR NOT d OR e)
(NOT c OR NOT d OR NOT e)

(a OR u     OR v)
(a OR u     OR NOT v)
(a OR NOT u OR v)
(a OR NOT u OR NOT v).
```

The last four clauses force a=1. The middle four force c=0. The second clause
then forces b=0; the first is satisfied. Conversely a=1,b=0,c=0 satisfies
every clause for any values of d,e,u,v. Thus there are exactly 16 solutions.

The only initial binary clause gives b => a. A valid lookahead forest therefore
has a as the parent of b. Visit a and then b at truth degrees 4 and 2, so that
a's assignment remains visible while examining b. Disable optional double
lookahead. In this witness apply the earlier independent repairs F208 and F209:
retain the processed queue prefix, and always decrement the virtual clause
size. Neither earlier defect is needed here.

1. Looking at a shortens (NOT a OR NOT b OR c) from three literals to two.
   Its weight is K_2=1, so the recorded score is H(a)=1. No unit is found.
2. Looking at b retains a. The same clause now has only c left, so c is put on
   the temporary stack. There is no other affected nonbinary clause at this
   point. The newly accumulated weight w is zero.
3. At the end of the queue loop, the printed placement makes c true. The queue
   is now R=(a,b,c), with G=2 and E=3. The loop is not resumed, so the four
   clauses containing NOT c are never processed during this lookahead.
4. Step X9 sees w=0 and H(b)=H(a)=1. It consequently adds
   (b OR NOT PARENT(b)), which is (b OR NOT a).

That new clause contradicts every original solution, since all of them have
a=1,b=0. The alleged satisfiability-preserving reduction has turned a
satisfiable formula into an unsatisfiable one.

With the corrected placement, c is processed in the same queue loop. Each of
its four clauses contributes K_2=1, yielding w=4 and H(b)=5. Step X9 therefore
does not add the invalid clause. This is more than an inaccurate heuristic:
the missing propagation invalidates the test used to prune solutions.

## Evidence and scope

`check_focused_sat175_deferred.py` reproduces just these two local lookaheads
and checks all 128 assignments of the fixed seven-variable input. Both versions
include F208 and F209's repairs. It confirms w=0 versus w=4, G<E versus G=E,
and 16 versus zero solutions after the X9 clause. The short check ran with
nice 15. It is not a full transcription of Algorithms L/X/Y, and no incorrect
result is claimed for the author's SAT11K program.

The original p. 581, routine (72) on p. 227, and X9 on p. 228 were visually
inspected. The September 23, 2015 author draft, p. 217 / PDF page 225, contains
the same misplaced instruction. The official [SAT11 base program](https://www-cs-faculty.stanford.edu/~knuth/programs/sat11.w)
places the clause-update block inside its queue loop; the official
[SAT11K change file](https://www-cs-faculty.stanford.edu/~knuth/programs/sat11k.ch)
puts the temporary-stack drain inside that block, after scanning the clauses
for the current literal. Fresh copies and retrieval metadata are archived.

Current and historical 4B, Fascicle 5, and Fascicle 6 errata, including the
three current TeX sources, contain no matching correction. Earlier changes
to (71), X2, X3, and X7 are separate. Targeted public searches found no prior
report of this placement error. Absolute priority and a later complete
printing are not established; no report has been sent.

Results: `../results/focused-sat175-deferred.json` and
`../results/focused-sat175-deferred-sources.json`.
