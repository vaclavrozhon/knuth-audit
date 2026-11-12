# MMIX: preliminaries and architecture through printed page 15

The existing complete page reconciliations for file pages 1–16 and 17–23
were read and accepted at their actual scope. They cover every displayed
arithmetic example, character code, address and instruction-field convention,
integer operation, Boolean matrix identity and immediate/branch format in
this range. The original preface on file 6 and floating-point summary on
files 20–21 were read directly again to resolve the remaining scope questions.
No old computation or opcode inventory was restarted.

The preface discusses the historical Mixmaster extension and its standard
calling convention. It is not naturally a universal impossibility assertion
over all future compatible extensions, alternative calling conventions or
new I/O devices. The existing MIX-context checks are sufficient for that
reading. R0001 is retained as the historical record of a stricter proposed
interpretation, not promoted into a defect or a new architecture-design task.
The dated history and rhetorical assessments remain author-reported.

The Boolean matrix products and their transpose conventions, byte-reversal
example, field decompositions and binary32/binary64 classes agree with the
accepted detailed arguments. A row of the left factor or a column of the
right factor with at most one nonzero entry permits at most one nonzero
summand, which is exactly the stated condition making OR, XOR and ordinary
products coincide. The arithmetic and conversion instructions are definitions
in a deliberately abbreviated architectural summary; the text expressly
delegates special values and details to MMIXware and Volume 2, section 4.2.

The extensive earlier floating-point arithmetic, comparisons, conversions,
remainder, square-root, single-precision and decimal-output work is retained.
The corrected precision-control assessment is accepted: IEEE section 4.3
does not add the previously demanded universal double-input operation.
The two epsilon interpretations at negative zero and positive infinity are
explicitly described in `fp-contract-boundaries.md`; no unambiguous book
defect follows. The actual program behavior is already documented there.

Exact exceptions: this block does not certify all decimal-input cases or the
enabled-trap IEEE interface of the external MMIXware implementation. The
book's broad conformance statement is accepted as a reference to that
specification, with those implementation limits visible, not converted into
a new software-conformance project. Existing software findings S0001–S0009
remain separate and do not make correct book definitions erroneous.
Quotation origins, historical dates and performance/prevalence claims,
the complete supplement's correctness, all language-coverage claims and the
precise Chinese translation remain outside independent verification.

All supplied pages in this range have been read and reconciled. Under the
current printed-argument standard these exact limitations do not leave an
unread page. Existing C0001/C0002 are retained; no new finding is added.
The corresponding instruction exercises are handled with their printed
answers in the next block, together with the already completed 41–58 block.
