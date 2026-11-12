# MMIX instruction effects and exercises 41–58 — reviewed

7 November 2026. Read the printed questions on 27–28 together with answers
97–98, the instruction-table context on 20, and the retained detailed checks.
The original answer page 97 was also inspected visually. This completes the
selected instruction-effects block under the user's printed-argument review
standard. It does not certify the whole MMIX booklet or its software.

The equivalences, absolute-value and bit-count programs, high-tetra arithmetic,
instruction encodings, program49 trace and its 4μ+34υ cost agree with the saved
step-by-step checks. The timing count includes both executions of XOR/PBOD.
The printed no-op families preserve the program-visible state with the stated
global-register choice. The already recorded omissions in answer52 remain
MMIX-C0011; they are not counted as a new finding in this review.

The rH/rA/rL lists were read against the direct-instruction-effect convention
and the completed 54–55 recovery. Later handler instructions are not effects
of the opcode that transfers control to them. The four immediate floating
conversions are exact; the ellipsis in answer54 is read as the relevant
arithmetic families, without creating a finding solely from its notation.
The user-mode/privileged LDVTS distinction in answer55 is retained explicitly.
The three x^13 constructions, their representable input range and their
space/time comparisons agree with the existing derivation. No new execution,
opcode census, proof of global optimality or hardware benchmark was run.

The ordinary intended context is used for the serial-number assignment on20
and the sharing/cache discussion in57. The latter concerns sharing the same
unchanging instruction image; it is not a theorem forbidding coordinated
self-modification, private copies or all possible operating systems. ProgramM's
opening on28 is covered by the existing assembly-program review.

Explicit exceptions, also attached to the relevant UI pages:

- 43 and56: global shortest/fastest/minimum-space claims over all MMIX programs
  and constant-preservation conventions are not independently established.
  The displayed constructions and their individual costs are checked.
- 48 and52: the listed positive cases and the supported omissions are checked.
  Exhaustive exclusion of every other opcode pair/no-op operand pattern is
  not claimed. The paused full256-opcode draft remains a draft; its proposed
  `opcode-noop-052.json` was not produced or used as evidence.
- 52–55: use the book's program-visible state and valid direct instruction
  effects, excluding autonomous clocks/profiling and later handlers. The
  user-mode boundary of55 is explicit; privileged LDVTS adds two forms.
- 57: historical empirical performance and universal process-sharing
  impossibility are not certified. 58 is the explicitly excluded NNIX book/
  operating-system project, not an unfinished ordinary exercise.
- Original quotation attribution and implementation-wide IEEE/cache/OS
  correctness are outside this block. No previously gray floating-point or
  software page is promoted by this completion.

Evidence: `exercises-1.3.1-041-058.md`,
`exercises-1.3.1-054-055-recovery.md`, `recovery-pages-024-033.md`,
`recovery-pages-034-036.md`, `independent-arguments-028-032.md`,
`MMIX-C0011.md`, and the corresponding original pages20,27,28,97,98.
The retained edition/errata checks apply to the 2023 digital third printing.
No additional book error was confirmed in this closure.
