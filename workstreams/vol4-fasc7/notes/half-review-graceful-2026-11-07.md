# First-half review: graceful graph arguments22–27, exercises81–137

7 November2026, main reviewer only. Read printed22–27 (file37–42), questions
81–137 (file136–141), and their paired answers176–189. Answer189 also begins
138–140, so its whole page is not certified by this block alone.
The original figures and correction layer were consulted where notation,
overbars, directions or geometric incidence mattered.

The KC edge count, LemmaO/parity corollary, reverse model and TheoremS are
consistent. All12 four-edge LO strings match the drawn graph types and labels.
The m!/2 complement convention is explicit for m>=2; isolated vertices are
treated as unused labels. Anick104's component/residue argument, both bounds
on available forest edges and its factorial lower bound check out. The
apparently missing first-edge exception is already fixed by the4September
erratum m>k>=m/2. The matrix-tree/sign-extraction argument105 has the correct
factor2^(n-2), and the n=4 cofactor agrees with the displayed polynomial.

For81–89, the corrected82 matrices and the Fig108/88 witnesses were checked
as fixed graphs in `results/half-graceful-witnesses.json` (one run, nine
matrices, no search). The general83 construction splits vertex parities and
edge differences as claimed, including both parities of r. The KC symmetry
exception n=r=3, the odd-degree pruning in87, and the corrected four-edge
exception in89 were accounted for. All eight displayed103 witnesses give
the edge set1..16: this includes the examples with Y labels0,15,16,5,12.

For90, the mixed-radix recurrence is correct; irrationality rules out the
ambiguous terminating expansion. The20 component/isolate counts and the
bipartite cases were traced from the actual edges. A separate fixed-example
check in `half-pi90.json` resolves precision loss in the20 digits and supplies
planar embeddings for the20 graphs. The small cyclic cores permit the stated
three-colorings; this says nothing about the separate10,000-case report.

For91–100, reversible union-find and parity pruning, regular-degree pruning,
cycle-component generating functions and the isomorphism-invariant hash are
consistent with their advertised roles. A hash is not treated as a proof of
nonisomorphism beyond the author's finite experiment. The100 arrays were
read with the three published corrections. Its two shifted edge masks have
disjoint supports below/above the assigned label, so their printed addition
is valid. All three branching cases cover the next unassigned edge; rooted
random restarts in102 are a heuristic with the stated restriction, not a
complete existence test. The9-odd-label observation101 follows also from
LemmaO and the two omitted labels of the22 available interval positions.

For107–118, the binomial-tree bit formula, corrected Gray-code induction109,
parallomino coordinate/sum construction, alpha-label complement, ordered
bipartite packing/product, and caterpillar-net label recurrences were read
step by step. In114 the rotation is45 degrees and the corrected corners are
used. The caterpillar recurrence gives consecutive disjoint edge intervals;
the displayed T-pentomino witness116 has sums0..15 and separated vertex
ranges. Its1824 total and uniqueness of U's decomposition are not proved.
The real factorization117(b) uses ceiling(m/2)-1, as the original confirms.
The palindromial argument, coefficient contradiction, interval factorization,
prime-operation commutations and generating function all agree. The118
constructions partition the required edge lengths without duplicate labels.

For the directed text24–27 and120–137, the modular differences, affine actions,
automorphisms, converse action and four-array representation were checked.
Fig109(c–e) matches the stated vertex permutations; (f)=7(e)+5 mod13.
The corrected equivalent-orbit count is1872, not156. All12 LO entries of44
encode the12 arcs in43; FIRST/NEXT visit each outgoing neighbor exactly once.
The125 list-building and126 transformations preserve their sentinel and
head/tail meanings. TheoremH's telescoping obstruction and both even
path/cycle constructions130 agree with the two different moduli.

The normalization123 works for composite q: count d'phi(r), distinguished
by an arc of label1. The124 mergers respect the named symmetries.
The corrected127 d=2 and d=4 classes are pairs. Burnside129 counts fixed
LO entries on multiplication orbits; in its converse formula the two possible
signs of the final l term give the same gcd divisibility test because the
odd orbit implies gcd(a^s-1,q) divides2l. No false sign error is reported.
The131–133 extension labels cover multiples and nonmultiples separately.
The135 parity obstruction and136 independent reversal pairs work also for
the self-complementary arc. The137 difference-set equivalence and explicit
order9 witness were checked: its four difference orbits partition1..36.
The displayed order4/5 LO witnesses define the claimed complete tournaments.

Exceptions, located by exercise/text rather than a blanket unread scope:

- Main22–24,81/82/84/87/88/91–99/101/103/108: exact enumeration totals,
  completeness or uniqueness claims and performance/Monte Carlo figures
  are not independently reproduced. For99 this includes the assertion of
  absence of every rooted labeling; for101 the band-restricted census and
  assertion that both10 and20 are mandatory. Updated95/101 illustrations
  are acknowledged published replacements, not new error reports.
- Research84/96/106/119/134: no original solution or new proof. The October
  update supplies a proof outline for106; it is not mislabeled still open.
- Exercises113(b)/116/122/124/127/128/129(c)/137(a–c): the printed methods,
  formulas, transformations and stated witnesses are reviewed; full finite
  classifications and uniqueness counts are accepted as reported calculations,
  not rerun as new searches. The large128 run and asymptotic totient result
  are specifically excluded. The known128 arrow reversal is applied.
- Cited external graph theorems, priority/history and benchmark costs are
  not separately proved or researched. Printed internal reasoning is covered.

Known corrections were checked in the fresh official7November snapshot,
including82/85/89/92/94/95/97/100/101/104/106/109/111/114/115/116/120/127/128/137.
No new supported error emerged in this block.
