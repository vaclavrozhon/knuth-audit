# Gray-code transitions need conjugation

**Location.** Volume 4A, first edition, first printing (2011), final
paragraph of answer 7.2.1.2–52, printed page 710 / file page 727.

The paragraph says that replacing the mixed-radix traversal of a Sims
table by Gray code makes all transitions the permutations tau(k,j)
or their inverses. With the permutation representations specified in
Algorithms G and H, a transition generally needs a conjugate of tau.
Here conjugating t by P means the product P t P^-1, using the book's
left-to-right convention for permutation multiplication.

For Algorithm G write the current product as A = P s Q, where s is
the factor being changed and P is the product of the preceding factors.
If Gray code changes s to s', the required new product is B = P s' Q.
Consequently the permutation that must premultiply A is

    B A^-1 = P (s' s^-1) P^-1 = P tau(k,j) P^-1.

Gray code does not force P to be the identity. The same calculation
applies to Algorithm H, with its inverted factors and its own definition
of tau. The correction does not prevent Gray-code traversal or change
the cycle structure of a transition; it changes which positions move.

**Three-element counterexample.** Take the valid Sims table

    sigma(1,0) = (),   sigma(1,1) = (0 1),
    sigma(2,0) = (),   sigma(2,1) = (0 2),   sigma(2,2) = (1 2).

In Algorithm G the reflected Gray control sequence (c2,c1) begins
(0,0), (0,1), (1,1). The corresponding permutations are

    012, 102, 120.

The second transition swaps positions 1 and 2. However the available
tau permutations from (15), together with their inverses, are only

    (0 1), (0 2), (0 2 1), (0 1 2).

None is (1 2). Applying the advertised tau(2,1) = (0 2) to 102 instead
gives 201. Following the unmodified tau updates through the whole
reflected control path gives 012, 102, 201, 021, 102, 012, with repeats.

**Suggested correction.** Say that transitions are *conjugates* of
tau(k,j) or its inverse, and identify the preceding-factor product P.
The aggregate reset permutations omega are unnecessary, but the
coordinate change cannot be discarded. The statement that the Sims
products can be traversed in Gray order remains valid.

The original page and the definitions (15), (17), (33) and (34) were
compared. Current and historical Volume 4A/Fascicle 2 errata contain no
matching correction in the screened ranges. Public search found the
same wording in an earlier Knuth draft. Independently, Mark C. Wilson's
[Random and exhaustive generation of permutations and cycles](https://www.cs.auckland.ac.nz/~mcw/Research/Outputs/Wils2006.pdf),
page 4, explicitly retains conjugation when changing a middle factor;
it is supporting algebra, not an explicit erratum to Knuth. That paper
is archived in sources with retrieval provenance. Absolute priority is
not established. No code was used for the counterexample.
