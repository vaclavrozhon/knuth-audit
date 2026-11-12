# MMIX: programming exercises 21–35

The complete retained exercise analyses were read together with the printed
questions on pages 47–51 and answers on pages 104–113. The complete Delay
code and its operating-system assumptions were checked against the page
images. Existing programs, output certificates and exact arithmetic results
were reused; no old simulator run, census or verifier was repeated.

The Farey-neighbor determinant argument, bounded-array implementation,
alignment cases for memory clearing and string copying, pair-frequency
counting, Fibonacci rounding analysis, odd-order magic square, both Josephus
implementations, rounded harmonic sums, calendar programs and crossword
renderer all have substantive retained arguments. These cover the printed
claims and answers under their stated domains. Existing results are not
merely isolated successful executions. The calendar's finite implementation
domain is distinguished from the general period/frequency argument.

C0019 remains an interpretation-dependent candidate: an exact equality at
one cost boundary does not automatically refute an approximate performance
claim. The character-frequency thresholds, physical pipeline measurements,
and global speed superlatives have explicit qualifications below. The
already accepted calendar findings V1-C0025/C0026 are repeated occurrences,
not new MMIX findings. Known corrections to rounded sums and delay/delta
are applied before assessing the algorithms.

C0020 is independently accepted in this root review. If the first timer
read equals the requested delay, the saved reference time is zero. A legal
handler can reset the timer before the user program ever reads a nonpositive
value. Every later signed-positive read then repeats the normal polling
loop forever. This satisfies the book's quick-handler and sufficiently-large
reset assumptions. The retained positive-reference example also rules out
the proposed one-branch boundary repair. No fresh long execution is needed.
Checking this incorrect printed routine does not require designing a new
operating-system timing protocol. The separate sensor event at the amber
transition remains a precisely documented interpretation issue.

Three errors in the audit's own prose were corrected: signed MUL does not
update rH, and integer-overflow trips in two address-arithmetic discussions
are V, not floating-overflow O. These were not errors in the book and do not
change the associated algorithm proofs or finding count.

Exact exceptions are physical pipeline/cache timing, unavailable historical
benchmark and bibliographic details, unqualified global speed optimality,
and the stated timer/I/O/sensor assumptions. The old demand to implement a
fully repaired Delay routine is outside this printed-argument audit. File121
contains the last part of answer34, which was read here, but is certified
only with its following subroutine answers in the next block. No new book
finding is added.
