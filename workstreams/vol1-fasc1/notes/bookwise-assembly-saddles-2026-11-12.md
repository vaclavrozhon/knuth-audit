# MMIX: assembly language and programming exercises 1–20

The complete retained reconciliations for files 37–54 and paired answers
107–112 were read with their later corrections and supporting exercise notes.
The printed I/O contract on pages 41–42 and question page 46 were read again.
Program M, Program P, the language grammar, assembly examples, complete
numeric tables and all parts of exercises 1–20 are covered. Existing code
traces and finite certificates were reused; no build, census or old test ran.

The maximum routine's suffix invariant, tie convention, call interface and
cost agree with the accepted argument. Program P's prime-generation and
decimal-output invariants cover every branch and table address. Existing
C0016 corrects the split of memory costs between its phases; C0017 retains
the precise repeated-global-label counterexample. Both remain separate from
the correct arithmetic, loader XOR convention and single-pass fixup method.
The already documented assembler boundary defect S0007 remains a software
finding and does not turn the book's correct relative-address definition red.

I/O is read on valid buffers and representable signed return counts, with
positive capacity for the string-input services. R0007's proposed extension
to an unsigned request of at least 2^63 bytes is not imposed as the natural
domain of the elementary signed-return interface. The arithmetic n−size and
the serious-error distinction are correct in the stated natural domain.
R0008 remains a precise model qualification: the book's incomplete-EOF prose
and the external C fgets analogy differ for a nonempty unterminated final
line. This block does not assert that all external I/O implementations have
identical completion rules, count widths or flushing guarantees. Existing
S0005/S0006/S0008 remain valid at their independently established scopes.

Exercises 1–16 include the complete hand assembly, all displayed Arabic
numeral groups, floating-point prime-test variants, exact instruction costs
and the unexecuted mystery-program trace. The conditional 'unless' performance
statements in answer 14 are not incorrectly read as equivalences. PL/MMIX in
16 is an explicitly excluded language-design project. Exact Arabic title
translation and historical authenticity remain linguistic/source exceptions.

Exercise 17 explicitly defines validity through the opcode's restrictions on
its operand bytes. The accepted mask proof covers all printed table cells
and all byte values, with the additional PUT test. The answer openly records
its SAVE and jump-target limitations. The intended static-format task is
reviewed; no full state-sensitive validator or global optimality proof is
added. This is distinct from the stopped no-op census for instruction52.

Both saddle-point routines in 18, the minimax equivalence, the two probability
models in 19, and the entire later analysis of 20 were read. In particular,
the original partial flags predate the completed distinct, binary and third-
method notes. These later arguments have actual loop counts and expectations;
they are not merely empirical timings. The C0018 proof of the erroneous
printed asymptotic costs is accepted: the second formula omits unavoidable
second-phase memory work, while the first omits a final two-unit branch miss.
The completed third-method comparison is reused without inventing another
algorithm or rerunning its exact arithmetic. Its advantage in expectation
is not asserted for every individual input or against all possible programs.

Exact exceptions: historical trials and physical cache/pipeline comparisons,
the inaccessible original saddle-point article, priority/quotation details,
the language-design project, and the I/O/static-validation qualifications
above. No new book finding is added. The beginning of answer21 on file112
will be certified with the following Farey block, so this block certifies
only complete answer pages107–111 despite having read answer20 on112.
