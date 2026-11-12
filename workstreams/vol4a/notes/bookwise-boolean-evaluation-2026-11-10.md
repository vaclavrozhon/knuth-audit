# Boolean Evaluation: completion of Section 7.1.2

Main pages 101–133 and all 88 exercises with answers 561–581 were read
together. The first-100 review supplies main 96–100, answers 1–11, 49,
and the previously delimited treatment of 77. The present pass completes
the remaining printed arguments. Page 133 also starts the next section,
and page 581 starts its answers; those shared pages are left for the next
coverage record. No helpers or old computations were restarted.

Six new findings are recorded separately: F0011 (decoder input masking),
F0012 (multiple-output counting bound), F0013 (sorted threshold order),
F0014 (determinant product signs), F0015 (tic-tac-toe objective wording),
and F0016 (decomposability after flipping the extreme inputs). Each has
original typesetting, an argument, a source screen, and an English card.
Historical C0002 remains a terminology candidate: the coordinatewise
intersection proves the bipartite criterion on 120, although the cited
definition of generalized consensus is narrower. It is not promoted.

The main checks covered footprints, backwards minimum-memory steps,
the special-chain examples, simultaneous symmetric-function evaluation,
sideways addition, decoders, multiplexers, and the Shannon/Lupanov
counting and synthesis arguments. The input case splits check (18) and
(19). Exercises 16–17 were checked by the last nonaffine step and the
extra-register constructions. Prefix networks, conditional-sum addition,
and transducer composition were read with their recurrences and wiring
conventions. The corrected depth estimate in 29 and carry example in
42 were used. Sorting outputs are precisely where F0013 occurs.

The seven-segment truth tables and original 21-step circuit were checked
by hand using four-variable truth words. The replacement 19-step circuit
gives a,b,c,d,e,f,g = b7e3,f9e4,dff4,b6de,a2bf,8ff3,3eff. The corrected
11-step decimal circuit and the 12-step alternative in answer 57 also
match their stated truth words. The new 13-step circuit in answer 54
gives the six specified sets; the new 15-step S-box circuit in answer 59
gives 179a,63e8,5b26,3e29. The 14-step prime detector in answer 55 was
checked by its four x1,x2 cases, with the exceptional even prime 2.
OCR omissions of complement bars were resolved from the page images.

For functional decomposition, the column criterion, incompatibility
graph, Horn implications, and determinant/permanent expansions were
checked. Answer 71's probability formula follows by grouping the four
pairs into at most two types; its finite-population sampling formulas
use the number of good eight-point blocks. The disjoint-input cloning
construction in 76 telescopes correctly, with the known complexity
correction. The gate-elimination arguments in 78–81 were read together
with the corrected case in 80. Logical sentences 62–70, the shared-XOR
bound, legitimate families, and the corrected monotone triangle lower
bound were followed through their printed steps. The closure argument
in 86 uses the corrected union of error terms, coloring counts, and
final choice of r. Strassen's modular implementation in 87 is consistent
with its bit-cost bound.

The fresh official errata match the archived layers; see
`integration/2026-11-10-bookwise/errata/vol4a-manifest.json`. The relevant
historical and current 4A and Fascicle 0 layers were read. Known fixes
to 109, 117, 125, 131, 133 and answers 15, 20–21, 23, 28–29, 42, 51,
54–55, 57, 59, 62, 67, 69, 76–78, 80, 86 and 88 are not new findings.
The 2019 corrected median census replaces the original entries.

Exact limits are in `results/bookwise-boolean-evaluation-exceptions.json`.
In particular, this review does not rerun optimum-circuit censuses,
the complete tic-tac-toe case analysis, or external lower-bound proofs.
The only mathematical code in this block was exact integer arithmetic
for the single F0012 counterexample; no Boolean functions were enumerated.

Next: Section 7.1.3, printed 133 / file 150, with its exercises and answers.
