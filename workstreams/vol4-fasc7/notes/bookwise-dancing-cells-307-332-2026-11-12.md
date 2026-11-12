# Dancing cells, branching and exercises 307–332

Read main printed 61–68, questions 307–332 and complete answers 225–230
together. The start of main 69 and later questions/answers on shared pages
are not certified by this block. The corrected qualification on main 63,
I3's s=ACTIVE+1, the tie-breaking correction in 320, LS[0]=0 in B1,
the item-name corrections in 326, and both corrections to 331 were applied.

Table 3 matches the five options (113), including colors, spacers and the
inverse ITEM/POS and SET/LOC relationships (114)–(116). The sibling loop
(117) wraps at the trailing spacer and visits exactly the other nodes.
The primary/secondary tests by item address and by option-list address
agree for nonspacers, as answer 309 specifies.

In hide and Algorithm C, the chosen item's list stays fixed while its
options are removed from the other lists. C5 saves the sizes after that
common removal; C11 restores exactly the active prefix and sizes needed
for the next sibling. Changes at deeper levels are covered by the earlier
trail segment. Previously purified secondary items are skipped; an inactive
uncolored secondary item cannot occur in a remaining option. Early failure
can stop midway because the size trail suffices for restoration. FLAG=-1
in C4 deliberately suppresses early failure for items covered together.
The main-63 erratum correctly qualifies its no-empty-list statement.

The short Table-3 run in 314 was followed: q is chosen; its first option
fails when purifying y would empty r; the second option removes p x:B and
leaves only p r x:A y for p. The displayed final sparse permutations and
sizes agree with these deletions. The zero-size and early-tie qualifications
in 312, 315–316 and 320 are explicit, not undisclosed defects.

For C+, forced items are queued only on the transition to size one, stale
inactive entries are skipped, and failure clears the queue. A forced level
does not need a trail segment because it has no alternative; a preceding
choice's segment restores all effects when that forced chain fails. The
initial scan collects forced items before normal branching. Exercise 319's
extra conditional can indeed change pipeline behavior without changing
the mem count's definition; its timing is a historical measurement.

Algorithm B moves the common hide operation into the selected option's
commitment, as binary branching requires. Its descending option-list scan
does not skip swapped entries: a swapped last entry has already been
processed. The current option is excluded, and inactive purified secondary
items are ignored. LS records the current branching level of each stage;
backtracking restores a whole stage's saved sizes before purging its chosen
option. The corrected initialization of LS[0] is necessary. Purging a
nonforced option cannot directly empty a primary list because all active
primary domains had size at least two at that decision.

The WTD update increases the weight of the item whose domain was wiped
out. FRB instead updates the attempted item's empirical failure fraction;
with m attempts and f failures it is (f+1/2)/(m+1), giving the displayed
odd numerators. The binary updates in 329 occur once per attempt. The
published correction to 331 likewise moves TRY's increments to each
success/failure outcome, rather than incrementing once before a d-way loop.
The printed WT(ITEM[i]) typo in 331 is also already corrected to ITEM[k].
Forced-size tests are understood to use SIZE, with h used to rank the
remaining choices; this is the natural meaning of substituting a heuristic.

The queens-and-knights encoding in 325 uses row/column colors to join
consecutive knights and cell items to keep all occupied squares distinct.
It has 21 primary and 104 secondary items, and 64+5*336 options for the
8-by-8, five-knight example. Board bipartiteness proves impossibility of an
odd knight cycle. The initial eight queen choices in 326 satisfy the row,
column and diagonal conditions, and its weight comparison has the stated
direction. The long search history is not independently replayed.

The construction in 328 gives a contradictory pigeonhole core. An early
failure raises a pigeon weight, and the parity color then keeps remaining
pigeon domains smaller than the decoy domains, so WTD focuses on the hard
core. For the asymptotic example take sufficiently large even n, as in the
displayed n=20 instance. The duplicate # choice preserves learned weights
for the second visit and defeats the d-way variant. This explains the
printed separation without constructing another solver or runtime census.

No new finding. Exact exceptions: all measured timings, memory-update
totals and solution censuses in (119)–(125), the detailed long run and final
weights in 326, numerical comparisons in 327/330/332, and the measured
costs in 319/323/328 are not rerun. The claimed exponential behavior of FRB
on the final 328 construction is stated without a proof and is not supplied
with a new one here. External implementation, priority and benchmark
authentication are outside this printed-argument check.
