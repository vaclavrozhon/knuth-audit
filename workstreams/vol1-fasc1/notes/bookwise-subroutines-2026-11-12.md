# MMIX: subroutines and exercises 1–16

The complete retained page reconciliations for files60–74 and all16 exercise
analyses were read, including every continuation and extension in answers
121–123. The questions and answers were also inspected directly. The page122
image confirms the two existing findings described below. Existing stack,
SAVE/UNSAVE, program-output and cost arguments are reused without reruns.

All maximum routines, GO and PUSH/POP calling conventions, memory frames,
local/marginal/global register cases, prefix directives, metadata directives,
recursive and iterative Fibonacci routines, and nonlocal returns have complete
arguments within ordinary valid-memory and representable-input assumptions.
The cost comparisons use the book's nominal instruction model. Small-input
exceptions are already reconciled with the text's approximate/asymptotic
wording. No additional physical timing theorem is inferred.

The methodological discussion recommends stepwise design, interface checking
and diagnostic testing. It does not promise universal program correctness or
termination of repeated redesign. Its historical and empirical qualifications
are retained explicitly. The coroutine introduction on file74 and the start
of answer1 on123 are also read: the relevant distinction is between distinct
suspension locations, not the total number of dynamic calls.

C0021 is independently accepted: repeated equal nonzero GREG initializers may
share one global register, so subtracting the number of GREG statements gives
the wrong initial rG. C0022 is independently accepted: a valid SAVE clears the
current local register set but preserves other globals. The two retained
programs have corresponding zero initial values, the same rG, a global SAVE
destination, and no PUSH/POP. Their different results therefore refute the
claimed extension of register equivalence, independently of the separate
question about how nonzero initialization should be renamed.

For the elementary equivalence claim in answer10, the natural interpretation
compares corresponding initial values and consistently renamed interfaces.
Simply changing an operand while keeping a conflicting nonzero initializer
is not promoted to another finding. Full equivalence for arbitrary external
services or self-inspecting programs is not asserted. The documented SAVE
counterexample already establishes the actual erroneous extension.

Exceptions: historical prevalence of libraries/calling styles, workload
frequency of spills, physical hardware/OS timings, the stated guard-page and
abort policy, inaccessible bibliographic/quotation details, autobiographical
and productivity claims, and the informal UNIX directory analogy. No new
book finding or new implementation project is added. The prior semaphores
answer on121 is covered by X0073 and its precise exceptions.
