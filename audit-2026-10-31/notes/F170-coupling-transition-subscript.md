# F170 — Wrong successor state in the first recurrence of MPR103(b)

Status: confirmed in the local source set; low severity. Volume4B,
first edition, second printing(2022), printed p385/file405, first
line of answer103(b). The original PDF and the author's
11September2019 Pre-Fascicle5A p42/file48 both print

`g012 = (z/2)(g001 + g112)`.

Here `g_s` marks the probability of a specified final output and the
number of further steps until coalescence from the function table s.
The algorithm starts with a=(0,1,2) and appends f_0=(0,0,1) or
f_1=(1,2,2) on the right. Therefore its first successor is001 or122,
with probability1/2 each. The correct recurrence is

`g012 = (z/2)(g001 + g122)`.

An exact two-bit contradiction isolates the wrong printed intermediate.
Choose the marked output j=2. From012, the word11 gives
012→122→222. It has probability1/4, so `[z²]g012=1/4`.
From001, the two one-step successors are000 and011; from112 they
are111 and122. Neither state can output2 in one step. Consequently
the printed right-hand side has coefficient `[z²]` equal to0.

This is a local subscript error. With g122 restored, the complete
transition system gives the printed final expression

`g012 = ([j≠1]+[j=1]z)z²/(4−z²)`.

The uniform output law, EN=3, VarN=2 and all subsequent conclusions
in103 remain valid. The known corrections of103(e) and104 concern
different expressions and do not repair this recurrence.

Evidence:

- `audit-2026-10-31/images/sequential/ref-041.png` — original algorithm.
- `audit-2026-10-31/images/sequential/ref-405.png` — original wrong index.
- `audit-2026-10-31/images/sequential/fasc5a-48.png` — matching author PS.
- `audit-2026-10-31/notes/sequential-mpr-ex103-104.md` — complete
  transition table, all marked generating functions and every subpart.
- `audit-2026-10-31/results/sequential/mpr-103-104-coupling-errata.json`
  — six official text layers and three original TeX sources, with hashes
  and relevant contexts. No matching correction was found in the local
  snapshots, including all4b dated16April2026.

No new numerical computation, enumeration, PRNG test or old-run restart
was performed. Independent coordinator acceptance, discovery priority
and a physical printed-copy comparison are not claimed. Only file405
contains this error; the valid question on file41 is not an error location.
