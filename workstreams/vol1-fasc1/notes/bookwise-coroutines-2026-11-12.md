# MMIX: coroutines and all seven exercises

The complete retained page75–80 analysis and both later exercise6/7 proofs
were read with the questions and printed answers. The continuation-register
invariant, full decoder and output-buffer layout, every termination branch,
initialization, nominal costs, and all seven exercises are covered. The
retained inverse encoder includes a lower bound for each maximal character
run and a construction attaining it; its code proof covers all allowed bytes.
No old run or finite enumeration was repeated.

The accepted C0004 remains the actual reader error: a permitted NUL byte is
mistaken for the end of the input buffer. The conditional proof of the other
code does not certify that reader for all input. R0008 retains the previously
documented incomplete-EOF difference between the tutorial contract and the
external C fgets analogy. Ordinary successful I/O and the declared loader
initialization are explicit assumptions.

The exercise6 switching protocol preserves both independent register-stack
contexts through valid SAVE images and disjoint stack areas. Its reserved
global roles, continuation address, initialization and destructive UNSAVE
reuse rule are all specified. Thus the old partial flags for6/7 no longer
represent missing constructions. The two simpler linkage protocols and the
first-character loss under reversed initialization are also fully covered.

The pass/coroutine discussion is read in its natural streaming sense. Its
impossibility example concerns a downstream stage needing information that
has not yet arrived; it is not a theorem forbidding storage and replay of an
entire input. Similarly, the speed comparison describes avoided intermediate
file operations and immediately notes that memory effects may reverse it.
No universal inequality over all I/O, batching and scheduling models is
certified. These are precise qualifications to an informal comparison, not
new confirmed findings or new research projects. Historical usefulness and
psychological ease remain empirical exceptions.

Files81 and124 were read through the coroutine material; they will be
certified with the interpreter text and answers sharing those pages. No new
book finding is added.
