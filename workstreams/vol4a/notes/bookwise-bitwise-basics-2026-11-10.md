# Bitwise Tricks and Techniques: arithmetic, permutations, and broadword basics

Main pages 133–155, exercises 1–114 on pages 184–193, and their answers
on pages 581–601 were read together. The previous quick pass was used
for navigation and illustrations, not as a substitute for this argument
review. Whole pages 133–155, 184–192, and 581–600 are now certified;
the shared exercise page 193 and answer page 601 await the next block.

Six new findings are recorded separately: F0017 (outer permutation
masks), F0018 (a lost prefix-XOR carry), F0019 (the arbitrary-constant
byte-flag claim), F0020 (a faulty mask in the official replacement
min/max routine), F0021 (complemented operators in the strong-chain
conversion), and F0022 (right shifts leaking between packed fields).
Each has original typesetting, a short counterexample, an errata/public
source screen, and an English UI card. No mathematical code was needed.

The review followed the two's-complement identities, packing conventions,
rightmost-bit operations, ruler and binary-logarithm methods, sideways
addition, reversal, delta-swaps, the recursive permutation network,
zip/unzip, compression and expansion, sheep-and-goats operations,
scattered arithmetic, and bytewise arithmetic. The alternating-cycle
argument for the network was checked including double bonds. The
compression invariant tracks gaps divisible by successive powers of two.
The original and corrected byte comparisons were checked by their
high/low-bit cases and the average identity. Formula (94)'s multiplication
collects the eight flags into a byte without collisions.

Exercises 1–19 were followed through the mex, nim-field, branching-map,
animating-function, and monadic-logic arguments. The known missing nim
product in answer 10 and missing hypothesis in answer 13 were applied.
The Paley rearrangement question includes the required nonnegative
entries. The analytic pattern in answer 18 is x = 64 sqrt(j), not the
OCR's apparent quotient. Standard cited field and decidability results
were accepted as cited, with the limits below.

For exercises 20–50, the current parenthesis convention and replacement
successor formula were checked by their suffix pattern; the duplicated
four-instruction prefix in the replacement MMIX listing is redundant,
not a different computed answer. The two-stage shift correction in
answer 22 avoids an overflowing shift count. The sieve's state and
bit indices, transposed five-bit packing, NAF transformation, generating
functions, weighted population count, and ternary displacement arguments
were read. The known corrected ruler generating function was used.

Exercises 51–87 cover the network's mask choices, matrix-coordinate
permutations, Omega-network routing, cycle generating functions,
polynomial bit operations, compression, stable/Gray routing, ordered
duplication, subset loops, scattered shifts, Morton addressing, and ASCII
conversion. The Omega proof uses k > 0, and the gather-flip argument
uses the corrected sorting-network reference. The inverse compression
uses the shifted mask from the erratum. The final word in answer 75
uses the restored duplicate x_3. The displayed subset loop tests x >= 0.

Exercises 88–111 were checked with the main formulas: independent-byte
subtraction, the three nonzero base-four divisors, odd-rounded averages,
alpha interpolation, zero/comparison flags, compiler selection, decimal
and mixed-radix corrections, packed arithmetic modulo 5, unary updates,
the date test, sorting through min/max, and broadword logarithms. The
constants in answer 99 agree with the original weak inequality x_6 <= 168.
The complement bars in answer 102(b) are essential and were checked in
the image. The Fredman–Willard construction gathers nonzero-field flags,
selects the highest field, then counts the threshold flags. Brodal's
replication and compression preserve the position of each flag even
when the number of fields is not a power of two. Answer 110's minterm
construction was followed through its stretch, conjunction, and final
selection stages. The pattern detector (98) was read with answer 111's
candidate-bit and interval-mask argument, including the short left field.

Exercise 112 remains an open research question; its printed reduction
to leading-bit extraction was read. Exercises 113–114 were checked
against the exact definition of a strong chain, yielding F0021–F0022.
The O(r) conversion and the qualitative simultaneous-evaluation claim
are not refuted by those findings; the printed constructions and the
same-length assertion are the defective parts.

All five relevant errata layers were screened. Fresh official files
match the archived sources; see the Volume 4A and Fascicle 1 manifests
in `integration/2026-11-10-bookwise/errata`. The new six-step comparison
and ceiling-average derivation are valid. Its associated replacement
min/max mask is the separate defect F0020. Known corrections and
improvements are not counted as new findings.

Exact limits are in `results/bookwise-bitwise-basics-exceptions.json`.
They include numerical censuses and timings, long explicit masks,
external results, and the date validator's implicit input-domain caveat.
No helpers, old computations, or broad enumerations were started.

Next: lower bounds, printed page 156 / file page 173, with exercises
115 onward and answers continuing on page 601.
