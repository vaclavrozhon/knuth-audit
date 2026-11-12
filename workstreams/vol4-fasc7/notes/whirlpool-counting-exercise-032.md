# Whirlpool counting representation — exercise32

Scope: exercise32 p115/file130 and answer32 p164–165/files179–180. Originals
have been viewed. The21 September2026 primary erratum replaces the state
indices, falling-factorial counts, rank representation and extension examples.
The entire replacement is proved here. Its superseded indexing mistakes are
known corrections, not findings. The huge5×5 census and historical10Gμ remain
explicit partials; no enumeration or benchmark was launched.

## W32-1 — order relations, states and the two numerical examples

Four distinct entries have4!=24 relative orders. Any order-dependent
quaternary relation is a subset of those24 possibilities, so there are2^24
such relations. A different one may be imposed on each adjacent block.

Normalize a partial assignment of the firstt row-major entries by replacing
its values by their relative ranks0,...,t−1. Every order-only constraint is
preserved. The AlgorithmQ frontier consists of the finalh=n+1 positions,
whose values are an ordered choice ofh distinct elements. There are exactly
t falling h =t(t−1)...(t−n) possible states. Before update(i,j), t=in+j;
after appending its new entry, t increases by one. The ordinary/seam schedule
and frontier sufficiency are those proved in Q28-2, with the same input
qualificationm≥2,n≥1; the intended5×5 case is within scope.

After(2,2) for n=5, t=13, giving
13·12·11·10·9·8=1235520 states. After the final(4,4), t=25, giving
25·24·23·22·21·20=127512000. This proves both corrected displayed values
and which side of an update they describe.

## W32-2 — suffix rank code and its inverse

For a permutationx0,...,x_(t−1) of0,...,t−1, define y_j as the number of
earlier entries smaller thanx_(j−1), for1≤j≤t. Necessarily0≤y_j<j. It is
also x_(j−1) minus the number of later smaller entries, proving the relation
to the original inversion description.

The last h values ofx determine the last h values ofy without knowing the
earlier order: subtract, from eachx, the smaller values in its known suffix.
Conversely, start with the sorted available set{0,...,t−1}. Recover the last
entry as the y_t-th smallest available value, remove it, then recover the
preceding entry as the y_(t−1)-th smallest remaining value, and so forth for
h steps. At each stage j values remain and0≤y_j<j, so this inverse always
exists and is unique. It proves that suffix x tuples and suffix y tuples
are bijective, independently of any preceding constraints. The Cartesian
product of their digit ranges has size t falling h, as required.

For t=8,n=3, suffix3142 has numbers of later smaller entries2,0,1,0,
giving code1132. Conversely code3142 decodes backward by selecting
2, then5, then1, then6 from the shrinking available set, yielding suffix6152.
These are exactly the two corrected examples; no unstated preceding values
are needed to derive either one.

## W32-3 — append transition and counting proof

Choose a new final valuev from0,...,t. Replace each old entryx by
x+[x≥v] and appendv. This gives a permutation of0,...,t, and every such
permutation has a unique inverse obtained by deleting its last value and
subtracting1 from all remaining larger values. Hence every old permutation
has exactlyt+1 children, with no duplicate or missing child globally.

All comparisons among old entries are unchanged, so their prefix-rank digits
y1,...,yt are unchanged. The new digit y_(t+1) equalsv, because exactlyv
preceding entries are smaller. The new frontier is therefore the previous
lastn y digits followed byv. This proves every extension described in the
replacement, including its nine choices0,...,8 at t=8.

For each old state, decode its frontier, append/rerank as above, and test the
new local order relation. Discard forbidden children and add the old count
to the new frontier's count for each allowed child. Previously completed
relations remain true because they depend only on preserved relative order.
The discarded oldest position cannot appear in a later relation. Initial
states at lengthh are all h! permutations, each counted once. Induction on
the prefix length thus proves the count invariant for all stages. Summing
the final frontier counts counts each full permutation once.

There are exactly sum_(t=h)^(mn−1) (t+1)·(t falling h) candidate state/value
transitions before relation pruning. The maximal number of count slots is
(mn falling h); arithmetic needs integers as large as(mn)!, rather than a
silently fixed machine word. This finite bound and the increasing prefix
length prove termination. They do not reproduce the book's10Gμ measurement.

## W32-4 — why an in-place memory arrangement exists

The answer specifically claims that old counts need not be destroyed. Here
is a complete proof of the recursive address construction used in the official
source, with notation kept distinct from the book's prefix length. LetT be
the last zero-based position, so a state has digits z_(T−n),...,z_T with
0≤z_j≤j. Its size isS_T=(T+1) falling(n+1). LetL_T be ordinary mixed-radix
ranking with the first digit least significant; the radix of z_j isj+1.
This ranks the states bijectively from0 toS_T−1.

Define an addressM_T as follows. If the last digitd=z_T is at leastT−n,
useL_T. Otherwise putd first, rotate the remainingn digits right, and use
M_(T−1) on that tuple. AtT=n the first condition always holds, so recursion
terminates. The rotated tuple has exactly the correct smaller digit bounds:
the moved digit is at mostT−n−1 and every other digit keeps its bound.

Prove bijectivity by induction. The recursive branch is in bijection with
all states atT−1 and therefore occupies exactly[0,S_(T−1)). In the direct
branch the leading mixed-radix digitd ranges fromT−n toT. Each fixed d
occupies a block of A=T falling n consecutive addresses. Its first block
starts at(T−n)A=T falling(n+1)=S_(T−1), and its last ends atS_T−1.
Thus the two branches partition all addresses without overlap or gaps.

Now fix the middle n digits while replacing the old first digit by a new
last digitd duringT→T+1. For d≤T−n the recursive rule says the new address
is exactly the old address whose first digit wasd. Those are the old fiber's
own cells. For larger d, the new address lies at leastS_T and is previously
unused. Compute all new sums for this fiber before overwriting its old cells.
Different fibers have disjoint old cells, and bijectivity makes their new
addresses distinct. No write therefore destroys a count still needed by
another fiber. This proves the claimed in-place safety for arbitrary local
relations, not just vortices. AnO(mn)-sized temporary sum vector suffices.

The recursion uses at mostT−n+1 reductions and one mixed-radix evaluation;
a cyclic coordinate pointer implements each rotation without copying the
tuple. This is an explicit finite addressing algorithm, so the existence
claim does not rely on trusting a large successful run. The full optimized
linked-list implementation and its particular measurements are outside this
limited address proof.

## Remaining count/method limits and primary source

The exact stated5×5 count2179875344187129600 and the10Gμ runtime remain
partial. The current official source is saved as `sources/whirlpool-count.w`
with retrieval hash in `sources/whirlpool-primary-manifest.json`.
Its address construction is identified and proved above; that does not
certify every line of the source or its overflowing-machine-integer limits.
No claim is made that its large census has been rerun.
