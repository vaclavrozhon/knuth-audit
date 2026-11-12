# Volume 4A: MMIX permutation programs and topological sorts

Main 339–344 from Faster, faster, exercises 7.2.1.2–77–94 and answers
715–719 through 94 were read together. F0063 fixes a line range;
F0064 the packed-codeword overhead; F0065 the matching-cost coefficient.
F0066 was dismissed after the original (49) confirmed inverse-position
primes missing in OCR. No mathematical code ran.

The cached-register Heap program preserves the memory/register
invariant, including its final register permutation. Direct symbolic
instruction counting gives the printed formula in 78 after correcting
the line reference. The doubled-array rotation trick gives each
permutation once. The packed transitions in (45), the seven-instruction
swap, and the alternative MXOR construction in 80 work with the
stated convention; its reversed coordinate interpretation is explicitly
acknowledged. The codeword overhead omits a repeated AND/PBNZ pair.

Langdon's packed routine and continuation 81 were traced through the
six three-element permutations; the zero nybble and ascending prefix
give the general carry rule. The main-loop and carry-loop counts
give the exact formula in 82. The sigma/tau instruction blocks in 83
implement their stated transformations. Mixed-radix partitioning in
84 and the rank/unrank updates in 85 preserve the active-list and
inverse-position invariants, including the variation extension.

Algorithm V's insertion/reset invariant, inverse updates and counts
(51) agree. The two relabeling examples (52)–(53), transitive-edge
redundancy 86, inversion-table order 87 and partition constraints 88
are correct. The skipped trivial levels and queue labeling in 89
give the doubling bound; the sharper Fibonacci argument and its
weighted telescoping identity agree, with the published clarification.
The known 2022 warning that this relabeling can increase a particular
M is retained and is not a new finding.

The Fibonacci count and self-inverse description in 90 agree. The
double-factorial prefix counts in 91 are correct, but their stated
asymptotic coefficient needs F0065. Its inversion-table note is correct:
the constraints (49) already use inverse positions. The double count
in 92 correctly gives n!Qn/Pn.
The two-dummy-element interpretation of 93 and the reflected mixed-radix
matching sequence 94 agree with their cited constructions. The short
matching list and its endpoint were checked; no census was rerun.

Known 4A/Fascicle 2 corrections in this range were screened. Whole
pages certified: main 339–344, exercise page 352, answers 715–718.
Shared exercise 353 and answer 719 await 95 onward. Main text of
section 7.2.1.2 is complete. Continue with exercises 95–113 on
353–355 and answers 719 onward, then combinations at main 355.
