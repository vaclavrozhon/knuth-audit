# Multiplication BDDs

Main247–249 through multiplication, exercises176–183 and answers
656–657 were read together. Whole main247–248, exercise271 and
answer656–657 are certified. Shared main249 and exercise272 remain
for ZDDs. New findings F0044 and F0045 concern a quantifier gap and
the terminal level in a quasi-profile bound.

TheoremX first fixes a variable order and splits the bits into P
and Q. Universal hashing bounds the sum of squared bucket sizes;
Cauchy–Schwarz then gives a hash image large for both sets. The
multiplier a selected at this stage depends on the order, so the
conclusion about a single multiplier's minimum over all orders is
unjustified (F0044). The cited Woelfel article's Theorem11 explicitly
selects a after fixing the order. The book's stronger fixed-multiplier
statement was neither refuted nor supplied with a new proof.

In exercise176 the shift b may be normalized modulo 2^(n-l), rotating
the output bins without changing image sizes. Original typography
confirms that Q'' uses a ceiling, not the floor suggested by OCR;
an initial rounding suspicion was therefore dismissed. The even
middle-bit representatives prevent low-bit carries from changing
the distinguishing bit. The proof's global quantifier passage is
not licensed by these local counting arguments, and its final
fixed-multiplier numerical assertion is not certified.

For TheoremA, after the low k bits of both factors are known, the
three residues x_low, y_low and the shifted low-part product each
need only n-k bits. When one further factor bit has been read, one
of those residues needs one fewer bit. These give the even/odd
branching-level bounds in177. The final QDD level has two sinks,
however, not the one permitted by the tail formula (F0045). Adding
one to the evaluated sum preserves the advertised coefficient19/7.
The five residue-class sums were read as geometric sums; the first
case was checked explicitly. The refinement in178 leaves the two
low bits unread and retains three possible carry values with six
joint patterns. Its partial sum omits the last four levels, whose
bounded contribution does not affect the improved leading constant.
The large exact profile and optimum-order tables were not rerun.

For TheoremY, when p<=n the carry modulo2^(p-k) determines the
remaining function. For p>n, the 2^(n-k) possible high parts give
two sets of transition points around the residue circle; between
successive points the residual function is constant as a function
of the low-part product residue. Thus q_k<=2^(n+1-k). Summing its
minimum with2^k gives the stated even/odd expression. The known
correction from3*2^(n/2) to3*2^((n+1)/2) was applied and excluded.
Combining constant-factor diagrams for all assignments to the
shorter operand yields CorollaryY. The leading-bit O(2^m*n) bound
in181 follows from the remaining threshold test. The exponential
lower bound in182 is an attributed external result.

For the infinite leading-bit example183, a prefix rectangle requires
a nonconstant residual precisely when it crosses the product
threshold. Its upper endpoints are excluded by the binary-expansion
convention. Counting admissible integer first coordinates by the
displayed ceiling/floor difference telescopes, with the nondivisors
of the power-of-two threshold supplying the remaining terms. The
known range correction was applied. No infinite-diagram construction
or new asymptotic research was attempted.

Next: ZDDs from main249 / file266, exercises184 onward and answers658
onward. Exercise184 will close the pending upper bound from TheoremK.
