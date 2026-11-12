# F208: Preserve the visible stack prefix in the general-clause lookahead

Volume 4B, answer 7.2.2.2–175, printed 582 / PDF 602; modification of
routine (72) on printed 227.

The extension virtually shortens clauses and uses the R stack to undo
those changes when their truth degrees expire. Its new restoration loop
retains the prefix whose literals are still visible in context T. But
the unchanged first line of (72) then sets G←E←F, discarding that prefix
and allowing its entries to be overwritten. Later it cannot restore the
clause reductions belonging to those lost entries.

After the restoration loop, replace G←E←F by **E←G**, retaining G and
the visible prefix. Make the analogous change in (73) for double
lookahead. F remains the boundary of actual fixed assignments; G is the
end of the preserved, already processed local prefix.

A fixed example uses binary implications b→a and not-c→not-d, together
with the big clause

    not-a OR c OR d OR e.

A valid lookahead forest can begin with a,b,not-d,not-c at truth degrees
4,2,8,6, respectively. Looking at a shortens the clause from four to
three literals. Looking at b retains a as visible; but the printed reset
then overwrites a's stack entry with b. When the next tree starts with
not-d at degree eight, a expires without its shortening being undone.
The clause count drops from three to two, instead of four to three.
Finally not-c is examined below not-d: the algorithm enters its unit
case even though both not-a and e remain unfixed. Its assertion that
there is only one unfixed literal is false. Retaining the prefix restores
a at the right time and leaves the correct two-literal residual clause.

`check_bookwise_sat175.py` checks these four local queue transitions.
It applies the unconditional size-decrement repair from F209 in both
runs to isolate the prefix defect. It is not a complete SAT solver.

The original image and 2015 draft page 218 / PDF 226 contain the same
restoration instruction and omit the changed initialization. In contrast,
the official SAT11K change file explicitly replaces
`fptr=eptr=rptr` by its restoration routine followed by `eptr=fptr`
(lines 971–975), with an analogous change for double lookahead
(lines 1087–1092). No matching public erratum was found.
