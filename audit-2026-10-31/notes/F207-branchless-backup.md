# F207: Save the return position at branchless levels too

Volume 4B, Algorithm L step L3, printed 222 / PDF 242, used by L15 on 223.

BACKF[d] is the number of fixed variables to restore when returning to
search level d. Step L3 increments the level and returns to L2 when
its chosen literal l is zero. Only the other branch stores BACKF[d]
and BACKI[d]. However, L15 unconditionally reads BACKF[d] after moving
back one level, including a level with BRANCH[d]=-1 and no decision.
That value can be uninitialized or left over from a previous visit.

Move **BACKF[d] ← F, BACKI[d] ← I** before the `if l=0` test in L3.
DEC[d] and BRANCH[d] should still be set only for a nonzero decision.
BACKI is protected by the BRANCH test in L13; BACKF is the essential
missing save. Saving both matches the author’s implementation and
also supports the progress-printing routine in answer 142.

This path is real. A fixed input combines two independent components:
a 75-variable, 315-clause satisfiable component (included twice to
favor its heuristic scores) and a 100-variable, 430-clause component.
The resulting input has 175 variables and 1060 ternary clauses. The
current official SAT11 source makes decisions at levels 0–2, then
creates branchless levels 3 and 4. After exploring the later component,
it returns to level 4 with 75 fixed variables and reads the saved
position 74, then returns to level 3 and reads 71.

The source correctly saves its backup pointers before testing whether
`bestlit` is nonzero (lines 1400–1403). An instrumented copy, which only
prints branchless reads and otherwise leaves the solver unchanged,
completes with UNSAT. A second copy moves those saves under the book’s
nonzero test and adds a guard before any unsaved pointer read. It stops
with exit code 91 and diagnostic

    BOOK_L3_UNSAVED_BACKF level=4 current=75 branch=-1

This isolates the omitted save without invoking undefined memory
behavior. It is not a separately transcribed implementation of all
printed L/X/Y steps, and no false SAT/UNSAT result is claimed for an
unguarded program. The demonstrated defect is the missing current-level
backup and the reached read of it.

The original page image and the September 2015 author draft (page 38,
PDF 46) both place the saves in the nonzero branch. No matching correction
was found in current/historical 4B/Fascicle 6 errata. The input, two
instrumented source files, complete logs, guard result, and bounded
probe history are in `results/bookwise-sat-l3/`. The exploratory probes
were short targeted attempts to reach this particular control-flow
path, not a benchmark census; timeout cases are not claimed solved.
