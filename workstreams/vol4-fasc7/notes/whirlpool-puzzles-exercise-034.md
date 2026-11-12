# Whirlpool puzzles and their CSP/XCC encoding — exercise34

Sources: exercise34 p116/file131 and answer34 p166/file181. Both full original
layouts have been viewed, and every clue was transcribed by row/column. The
current primary/public errata have no change to34. The four completion counts
are1,0,2,1. The proof below includes a direct uniqueness argument for(i), a
short contradiction for(ii), and proof-producing propagation for(iii)/(iv).
The historical800-kilomem claim remains a separate partial.

## P34-1 — exact CSP and comparison relation

Each empty cell has a variable whose domain is the set of unused values from
1,...,25; all such variables must be different. Since there are as many empty
cells as unused values, they consequently use every unused value once. Given
cells are constants. For each adjacent pair define a comparison variable,
unless both cells are given and its comparison is already a constant. The
comparison is constrained to agree with the two cell values.

For a block `[[a,b],[c,d]]`, the four directed comparisons in the answer are
bottom[c<d], right[b<d], top[a<b], left[a<c]. The circular-ascent count is
[a<b]+[b<d]+[d<c]+[c<a]=2+top+right−bottom−left.
It is odd iff the XOR of these four comparison bits is1. By W31-0 this is
exactly the vortex condition. Thus the CSP is equivalent in both directions
to completing the puzzle; redundant comparison variables are uniquely
determined by the filled grid. Constants at given cells cause no exception.

## P34-2 — complete hand proof for puzzle(i)

Every unfilled interior value lies between11 and24, with17 and25 already
placed. Write the three interior rows as

`17,a1,a2,a3,a4; b0,b1,25,b3,b4; c0,c1,c2,c3,c4`.

The increasing top and bottom clue rows, all below these interior values,
force17>a1>a2>a3>a4 andc0>c1>c2>c3>c4 by the odd-ascent criterion.
The four a values therefore occupy four of the six values11,...,16.

We use one elementary consequence of the eight vortex orders. When an upper
pair decreases, an increasing lower pair must lie entirely below or entirely
above it; a decreasing lower pair must have its interval strictly inside or
strictly outside the upper interval. This follows by listing the four cyclic
orders compatible with the upper comparison, and remains true with the two
rows interchanged.

The block above(b1,25) forcesb1>a1. The block above(25,b3) forcesb3<a3.
The next block on the right then has only two possibilities:

1. b3<b4<a4<a3; or
2. a4<b4<b3<a3.

In either case b3,b4 are also among11,...,16. Together witha1,...,a4 they
use all six low values. The leftmost block, usingb1>a1, says either
17<b0<b1 or a1<b1<b0<17. The latter would need two further low values
that are no longer available, so17<b0<b1. All five c values are therefore
the remaining high values18,...,24 and in particular exceed bothb3,b4.
For the bottom-right block to be a vortex, its upper pair(b3,b4) must
increase, since its lower pair(c3,c4) decreases and lies entirely above it.
Thus only the first right-hand possibility remains.

Consequently all six low values form the forced chain
b3<b4<a4<a3<a2<a1 and are respectively11,12,13,14,15,16.
The block below(b1,25) forcesc1<b1. The block below(b0,b1) then forces
c0<b0: the alternative of both c values aboveb1 contradictsc1<b1.
Hence the seven high values form the chain
c4<c3<c2<c1<c0<b0<b1 and are18,19,20,21,22,23,24.
Every interior cell is now forced, giving exactly the printed solution.
The resulting full grid passes all16 vortex conditions and all-different.
This is a uniqueness proof; the fact that local propagation alone left a
larger domain fixpoint was not treated as proof of multiple completions.

## P34-3 — immediate impossibility of puzzle(ii)

LetX,Y be the leftmost/rightmost entries of its second row. The upper-left
block is `[[3,14],[X,6]]`; the circular-ascent criterion forces3<X<6.
Value5 is already a clue, soX=4. The upper-right block is `[[9,2],[5,Y]]`
and similarly forces2<Y<5. Value3 is already a clue, soY=4. Two different
cells cannot both contain4. This is precisely the pair of forced4s displayed
in the answer, independently of any solver run.

## P34-4 — complete finite propagation proofs for(iii) and(iv)

`results/whirlpool-puzzles.json` records an ordered certificate of every
necessary domain deletion. There are two permitted inference rules:

* A vortex is one of eight strict increasing chains, obtained by choosing a
  cyclic boundary start and direction. To test a cell value, fix it and try
  each chain. Choose the smallest available value exceeding the previous
  one at each position. This greedy test succeeds iff the chain has any
  realization: inductively its chosen prefix is no larger at each position
  than that of any possible realization, so it leaves the largest possible
  choices for the remaining suffix. The certificate records the greedy
  prefix and failing position for all eight orders whenever a value is
  deleted. No compatible tuple is discarded merely because it was not
  sampled.
* For an all-different deletion, tentatively fix the proposed cell value.
  The certificate gives a setS of cells whose union of current permitted
  valuesN(S) is smaller thanS. Pigeonhole then proves that fixing impossible.
  The generating matching calculation is only a way to find this Hall
  witness; the witness's explicit sets prove the inference independently.

Starting domains are exactly the unused numbers or given singletons. Each
deletion is therefore necessary by induction over the stored trace. The
process is finite because it only deletes domain values; it never branches
on assignments. These rules close(iv) to singleton domains, giving the
printed matrix uniquely. For(iii) every cell becomes a singleton except
the first-column cells in rows2 and5 (one-based), each with domain{7,8}.
All-different leaves exactly their two swaps. Both full grids satisfy every
clue and every vortex constraint, proving there are exactly two completions.

The saved run also records a propagation contradiction for(ii), agreeing
with the short proof above. For(i) its domain fixpoint is not complete, and
the solution/count comes from P34-2 instead. The proof certificate explicitly
distinguishes that manual closure from the propagation closures. No full
assignment tree,25! census, or large exhaustive search was used. Every
printed witness is compared entry by entry with the saved complete grid.

## P34-5 — exact XCC construction and72/44/1808

For puzzle(iv) there are13 given cells and12 unknown cells/unused values.
Use primary items for the12 unknown cells and12 unused numbers. An option
choosing a value for a cell covers those two primary items and includes a
secondary item for that cell colored by its value. There are12·12=144
such options.

There are40 adjacent cell pairs. Eight vertical pairs have two given
endpoints and hence fixed comparisons: two in the leftmost column, four
in the middle column, two in the rightmost. The remaining32 comparisons
each receive a primary item and a colored secondary item. For each allowed
endpoint assignment, its comparison option covers that primary item, colors
the unknown endpoint-cell items by their values, and colors its comparison
item by the resulting strict sign. Each pair with one unknown endpoint has
12 options; each with two has12·11, since equal values are excluded.
Among horizontal pairs there are18 of the first kind and2 of the second;
among nonconstant vertical pairs there are4 and8. Therefore comparison
options total22·12+10·12·11=1584.

Each of the16 blocks receives a primary item. A block option specifies an
odd-XOR pattern of its comparison bits, matching any fixed comparison and
coloring each nonconstant comparison item appropriately. Twelve blocks have
one fixed edge comparison, leaving4 sign patterns each; the other four
have none, leaving8 each. This gives12·4+4·8=80 block options.

The totals are

* Primary items:12+12+32+16=72.
* Colored secondary items:12 cell values+32 comparisons=44.
* Options:144+1584+80=1808.

Every completed grid selects exactly one cell-value, comparison and block
option for each corresponding primary item, and all shared colors match.
Conversely primary exactness chooses one value per unknown cell and uses
each unused number once; color agreement makes comparison choices agree
with those values and block patterns agree with their comparisons. Every
block is then a vortex. This proves the encoding in both directions and
the exact counts, not just the final puzzle solution. The reported800
kilomems is source-specific historical performance and remains partial.
