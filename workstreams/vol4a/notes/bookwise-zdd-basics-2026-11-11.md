# ZDD definitions and basic operations

Main249–250, exercises184–202 and answers658–660 through202 were
read together. Main251–255 was also read ahead; its applications
are not certified by this block. Whole main249–250, exercise272 and
answers658–659 are certified. Shared exercise273 and answer660 await
family algebra. Finding F0046 concerns the support algorithm in197.

A ZDD represents a family of sets. A skipped element is absent;
the two sinks represent the empty family and the family containing
only the empty set. The zero-suppression rule, truth-table zeads,
nonzero quasi-profile inequalities and the BDD/ZDD size comparisons
were checked. All16 diagrams in187 were individually compared with
the families in188. The functions with identical BDD/ZDD structures
and the equality cases for quasi-reduced diagrams in189–190 agree
with the two reduction rules. The corrected wording on249 and the
known notation/reference errata in185/198 were applied and excluded.

Exercise184 closes the pending TheoremK upper-bound dependency.
For row i and column j, the two BDD node types record either i used
columns including a column before j, or i-1 used columns leaving
a column at or after j available. Their counts give the printed
profile and total (2m-3)*2^m+5. A ZDD node exists precisely when
the current row is still empty and column j is unused. Choosing
the other i-1 used columns gives C(m-1,i-1), independently of j,
and hence m*2^(m-1)+2 nodes. The earlier ticket argument charges
only such nodes and supplies the matching ZDD lower bound.

For symmetric functions, a weight-table substring is a zead unless
it is all zero or begins with one followed only by zeros. This gives
the maximum in185 via the de Bruijn construction already used in44.
The grammar in191 gives l[n+1]=l[n]*(l[n]+1); the precise asymptotic
constant and remainder are accepted from the stated Concrete
Mathematics references. The Z-transform in192 exchanges equal halves
with zero right halves, is involutive, and exchanges beads with
zeads. Its17-bit example was traced, as was the exact-weight to
threshold transformation in193. The unrestricted-pistol count194
uses the earlier accepted correspondence without a new census.

For196, the selector tree has 2^m-1 nodes and its elementary-family
leaves add2^m nodes. For the complement, the data suffixes distinguish
the excluded singleton, the excluded empty set, and the full family;
counting those gives the printed quadratic total. Exact optimized
multiplexer counts and orders in195 were not independently rerun.
In197, the support definition is suitable, but its zero-child tests
compare masks with indices (F0046).

The AND/OR/XOR/difference/MUX recursions in198–200 were checked by
separating sets according to their least supported element. Missing
high branches represent the empty family. The terminal cases,
skipping rules and extra reference for an unchanged high child agree
with those recursions. Projection functions201 need a fixed universe;
their prefixes and shared tautology tails give C(N+1,2) additional
nodes. The swap changes202 use a zero missing high branch and preserve
the appropriate tautology root. They inherit F0038's missing child
reference increments when a new node is created; a ZDD witness was
added to that finding. No complete toolkit was implemented or run.

Next: family algebra203 onward, answers660 onward, then the already
read applications from main251 with their paired exercises.
