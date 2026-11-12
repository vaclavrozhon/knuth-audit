# MMIX: instruction description and all 58 instruction exercises

The complete page maps for file 24–36 and answers 102–106 were reconciled
with the detailed arguments for exercises 1–24 and 25–40 and the accepted
7 November closure of exercises 41–58. The original printed page 18 and
question/answer pages 26 and 96 were read again at the exact remaining gaps.
All exercise parts and answer extensions are included. This block reuses the
accepted exact arithmetic and instruction traces; it starts no old verifier.

The fixed register transfers, interrupt priorities, valid SAVE/UNSAVE image
contract, register permissions, branch costs and architectural definitions
are supported by the existing clause-by-clause notes. The two complete
reference tables also retain their independently matched opcode, cost and
ASCII data. A declared instruction cost is the book's model, not a universal
latency guarantee for physical processors. The historical commercial-machine
comparisons and meta-simulator fidelity are retained as exact exclusions.

For exercises 1–24, the signed/unsigned cases, alias conditions, overflow
predicates and reciprocal-division arguments were read in full. The existing
499-divisor certificate establishes the answer's 189 failures without a new
census. For 25–40, the bytewise monus operations, parity/selection matrices,
field construction, loop invariant and branch alternatives were read in full.
The finite-field argument uses the already accepted primitive-polynomial
criterion from Volume 2; no new polynomial search is needed.

Exercise 33 is naturally read with the auxiliary constant available, as in
the neighboring matrix-instruction exercises and the answer's explicit
constant. Under that convention MOR performs the required permutation in one
instruction, and zero instructions cannot change all inputs. No claim about
the optimum cost of loading arbitrary initial constants is added. The answer
39 wording about winning permits a tie at an endpoint; the printed costs
already show that tie, so it is not promoted into a separate error.

The stored-operand discrepancy R0009 remains explicit. The tutorial and
simple simulator save the original store register, whereas the complete
MMIX description and pipeline implementation save the merged memory
octabyte. The existing signed-byte example with source 256 and zero memory
shows the difference without any experiment. The complete description's
introduction expressly distinguishes its implementation scope from the
tutorial, which omits exceptional details. This supports retaining a precise
compatibility qualification rather than deciding, without further evidence,
that one model is an unintended typo. The printed helper is internally
consistent with the book's rule. C0003's separate immediate-NEG error stays
confirmed and is not used to dismiss this store discrepancy.

Primary source checked online on 12 November 2026: the complete
[MMIX description](https://mmix.cs.hm.edu/doc/mmix-doc.pdf), sections 4,
34–35, still has the same distinction and store rule. The local source
and pipeline excerpts are retained with the earlier R0009 note.

Exact exceptions from the accepted 41–58 block remain: global optimality in
43/56, exhaustive equivalence/no-op exclusions in 48/52, the stated direct
user-mode effects in 52–55, historical performance and sharing assumptions
in 57, and the NNIX research/design project in 58. The stopped 256-opcode
draft is not accepted as a completed census. Quotation, source-priority and
hardware-prevalence claims are not independently authenticated.

No new book error is confirmed. Existing findings and source ambiguities
retain their precise scopes. All ordinary exercises in section 1.3.1 prime
and their printed answers are reviewed under the current agreed standard.
