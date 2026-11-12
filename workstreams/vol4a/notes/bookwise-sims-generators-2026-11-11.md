# Volume 4A: Sims tables and general permutation generators

Main pages 326–336 (with the Algorithm C conclusion on 337), exercises
7.2.1.2–35–54 and answers 708–711 through 54 were read together.
F0060 corrects the missing conjugation in the Gray-code remark of
answer 52. No mathematical code was run.

Lemma S's stabilizer induction, membership reduction and multiplication
convention agree. The displayed four-cube table has group order 384;
the orbit sizes, alternative numbering in 35 and table counts in 35–37
are consistent. The tic-tac-toe twists in 36 preserve the line classes
and supply the displayed orbits. The Euler-sum estimate in 37 gives
the claimed leading logarithm. In contrast to answer 5(a), the exact
flip mean in 38 includes its termination term correctly.

Algorithm G's reset/update product preserves (17), and its reverse-colex,
Ord-Smith and Heap specializations agree with the stated cycles. The
pruned traversal maintains that invariant by undoing exhausted factors;
the worked trees 39–41 agree with the indicated rejected branches.
The divisibility cutoffs and leading-zero tests are sound. Algorithm X
preserves its sorted available list and restores removed links on return.
Its predecessor indices 45–46, exact visit counts 47 and mean memory
cost 48 agree. The left-to-right bounding tables in 49 select the
remaining signatures correctly and use the rearrangement bound from 25.

The modified Heap construction for r-variations in 41 has the stated
base cycles and images of k. Construction 42 has only transpositions
and three-cycles. The three residue cases of 43 were checked by the
cycle products: with W=(k-3,k-2,k-1), its interior factors are
sigma(k,j)=(k,k-3-j) W^j for 1 <= j <= k-3. The last three steps send
k successively to k-1, k-3 and k-2, ending at
sigma(k,k)=(k-3,k,k-2); multiplying by W gives the asserted omega(k).
The small initial cases agree.

Dual factorization 50 follows by inversion, while 51 correctly warns
that inverting individual table entries need not give a Sims table.
Algorithm H's update preserves its dual product. The impossibility
argument for all-single-transposition dual updates on four elements is
valid. The Ives construction 53, its small trace, block recursion and
factorial operation count agree. The cyclic-shift generator and its
arbitrary-cycle variant 54 are valid. The preceding-factor product
cannot be omitted from arbitrary Gray transitions in 52: see F0060.

Known corrections to the Sims bibliography, Algorithm X attribution,
Algorithm C reference/termination wording, and earlier Fascicle 2
formulas were screened and excluded. Source evidence for F0060 is in
sources/sims-generators-source-check.json. Historical timing exceptions
are recorded in results/bookwise-sims-generators-exceptions.json.

Whole pages certified: main 326–336, exercise page 347, answers
708–710. Shared main 337, exercise 348 and answer 711 await Ehrlich's
method and exercises 55 onward. Main 337–340 has been read ahead;
the earlier shared main/exercise page 344 remains uncertified.
Next: main 337/file 354, exercise 55 and answer 711.
