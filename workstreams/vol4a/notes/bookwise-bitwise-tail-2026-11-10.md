# Remaining bitwise applications and exercises

Main pages 181–183, exercises 188–218 and added exercise 219, and
answers 615–621 were read together. Whole main pages 181–183, exercise
pages 199–201, and answer pages 615–620 are certified. Shared page
202 (beginning of BDDs) and answer page 621 remain for the next block.

New F0029–F0032 document the skipped CRC input word, an incorrect
nullity in the n=9 parity example, insufficient arithmetic width in
the subset-sum-gap algorithm, and an off-by-one UTF-8 surrogate filter.
Each has an original page image, short hand argument, errata screen
and targeted public-search record. No general verifier was run.

The branchless selections use a sign mask; the merge loop uses the
sign bit of the AND of three nonpositive offsets as its termination
test. Both candidate values are reloaded after the selected index
moves. The difference in exit-state bookkeeping and the final
lookahead loads are explicit limits, rather than a claim of drop-in
safety in every memory environment.

The graymap program accumulates per-byte populations without carries
between bytes; the added high bits stop its eight-byte output loop.
Its input stride, column reset, eight-row advance and immediate-size
bound agree with the declared dimensions. The transpose/rotation
steps exchange matching subblocks at each scale. The parity recurrence
is reversible on consecutive rows; first zero rows and reflection
explain the divisibility and perfect-pattern reductions. The polynomial
version follows the same Fibonacci recurrence. The doubling identities,
finite-field periodicity, corrected multiplicity step in 192(e), and
odd-grid refinement in 193 were followed. Nullspace elimination keeps
C=BA and strictly advances the low pivot after a dependency reduction.
The n=9 example has rank three, hence nullity two (F0030).

The six-byte historical encoding, UTF-16 splitting, and UTF-8 length
lookup were checked in their stated domains. The surrogate-excluding
addendum has the concrete false rejection in F0032. The distinction
between historical six-byte codes and modern scalar-value UTF-8 is
preserved; no claim about a current parser implementation is made.

The MOR and MXOR examples were read as bytewise Boolean/linear maps.
The original hexadecimal conversion and its 2018 replacement both
separate the nibbles before adding the digit/letter offsets. The
shuffle construction uses byte permutations, within-byte permutations
and a selection mask. The transpose follows its three exchange scales.
The suffix parity combines local byte prefixes with preceding-byte
parities. The four-instruction byte selection and Boolean upper-closure
matrix identities were followed, as was the characteristic-two
multilinear-transform observation. Polynomial multiplication uses two
triangular byte-convolution matrices; spaced ordinary products form
those matrices without overlapping carries.

The CRC invariant and the final eight-byte reduction agree with the
stated polynomial remainder. The assembly address update fails to
implement that invariant (F0029). Both the old inverse-matrix addition
chain and the 2020 shorter replacement have the stated final exponents;
the latter selects between X^(n-2) and X^(n-1) using X^(n-1)=I.
The divisibility-by-three trick tests the difference between populations
in even and odd bit positions. The subset-sum method groups inputs
by their leading bit and extends a covered initial interval, but its
precision sentence needs F0031. The modular logarithm/exponential
updates cancel one bit at a time; the corrected high-half table and
shortened loops use the linear form of the logarithm there. Added
exercise 219 deletes the first zero above the trailing run of ones,
preserving population until all the ones are packed at the right.

Known changes to 189, 196, 203, 192(e), 194, 214 and 218, and the
added exercise 219, were incorporated or explicitly distinguished.
Research/empirical and exact implementation limits are in the companion
exceptions file. Section 7.1.3 is now complete under those limits.
Next: Section 7.1.4, main page 202 / file 219, with its exercises
and answers beginning on page 621.
