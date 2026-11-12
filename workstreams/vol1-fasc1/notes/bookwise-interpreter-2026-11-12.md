# MMIX: interpreter and all22 exercises

The complete retained reconciliations for files81–101 and124–134 were read,
including the later exercise5,12,13,14 and15–20 analyses. The complete
questions, relevant answer continuations and original pages130/134 were
checked. The already read trip-contract analysis is reused. Existing opcode
tables, finite program profiles, stack inverses, patched-program certificates
and scalar recurrence results were not rerun.

The virtual-memory lookup, complete register ring, operand and destination
installation, all displayed Info entries, host instruction insertion,
exception handling, instruction counts and bootstrap have substantive
arguments. Program P's printed interpreted time includes the exact omission
of the final Halt charge and of the artificial startup UNSAVE. The finite
host stack maximum is11, with both an upper bound and a reachable input in
the later exercise5 note. The correct SAVE/UNSAVE inverse uses the accepted
C0007 correction and valid saved contexts, not arbitrary malformed memory.

The later RESUME proof covers its complete declared operation families and
all exception bits. C0015 remains the operand-installation defect. C0023 is
independently accepted: mode2 replaces the original instruction by a register
assignment, so rejecting an otherwise ignored original opcode F9 is wrong.
The repair must also set the actual internal opcode to ORI so the resume
state clears. Both the statement and unconditional printed guard were
checked in the original. The separate store-trip metadata difference R0009
retains X0071's explicit compatibility qualification.

The I/O helpers have complete ordinary-case branch arguments. They assume
valid buffers, representable signed counts, successful host contracts where
stated, and sufficient free working space. Exercise16's temporary filename
requires the explicit contiguous scratch bound in its retained analysis;
no overflow/error-handling guarantee at exhausted arena capacity is claimed.
Exercise17's signed count domain is the natural interface interpretation
already adopted in X0072. These do not reopen an artificial unsigned request
of at least2^63 bytes. The book explicitly excludes late serious-read errors
in that helper. The binary loader proof distinguishes a syntactically valid
file from a valid executable SAVE image and covers overlapping groups.

C0010 is promoted from candidate to a confirmed error in the argument, with
no new finding ID. The upper recurrence counts chunks; comparing it against
2^61 bytes does not justify the claimed safe instruction bound. The original
page, correct node capacity and existing scalar certificate establish this
logical error. The actual failure depth and truth of the numerical conclusion
remain unresolved; no enormous recursive simulation or new memory model is
required to identify the flaw. The separate English argument records the
change in assessment and freshly checked errata/public sources.

For exercise22 the four-byte trace reconstruction and the printed strategy
were reviewed, retaining C0006. Building a complete efficient tracer with
transparent state restoration, every inserted RESUME and interacting trip
handler is an explicitly deferred substantial implementation exercise. Its
answer is a strategy, not a supplied complete program whose correctness has
been established. This exact exception is preserved instead of claiming a
new implementation or treating the task as open research.

Other exceptions are historical deep-simulation profiles, unavailable source
editions and quotation provenance, empirical speed comparisons, the informal
claim that this is the book's longest program, full physical hardware/OS
behavior, and the already stated source-contract qualifications. The small
UNSAVE counter-wrap issue and two offsetting cost-table cells remain retained
proof-note corrections, with no duplicate finding cards.
