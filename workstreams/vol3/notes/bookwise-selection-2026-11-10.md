# Selection sorting, heaps and priority queues — 10 November 2026

Reviewed §5.2.3, printed 138–158, exercises 1–38 and answers 639–646,
with the original diagrams, algorithms and MIX programs. This continues
the accepted earlier work and completes the selection section. The
pages shared with the next section are certified when their remaining
content has been read.

The straight-selection argument, inversion/cycle maximum, remembered
maxima improvement and instruction costs were checked. Tournament
and heap diagrams agree with their descriptions. Algorithm H maintains
the heap invariant while building subheaps and removing maxima; its
MIX register offsets and branch cases agree with the prose. Summing
its instruction frequencies gives 7A+14B+4C-2D+12P+8N+3 floor(N/2)-4;
substitution of P=N+floor(N/2)-2 gives the printed total. Table 2's
successive heap states were inspected against these operations. The
example's exact 1068u total was not separately counted instruction by
instruction.

Theorem H's backwards correspondence gives the stated uniform heap
distribution. The special/nonspecial subtree sizes, build-time mean
and variance, heap deletion/insertion, and the printed worst/average
promotion arguments were read together with their exercises. The
known changes to answers 21, 23, 25, 26 and 30 were applied. The
priority-queue sieve and insertion construction were checked with
the published corrections, including the 2022 correction to answer16.

The interval-heap inequalities, leftist merge with reversed right
links, DIST repair after deletion, LRU list and subtree-size recurrence
were checked. Exercise29 supplies a hint rather than a full answer:
merging the sorted rows of coefficient products with a priority queue
and combining equal exponents provides the indicated construction.
No separate implementation was needed.

New finding **V3-C0034**: answer34 mixes external-leaf and record-node
counts, producing incompatible generating functions and the wrong
prefactor. Its separate note includes a short coefficient contradiction,
original images and primary-source confirmation.

Explicit limits: Yao's selection-sort variance theorem, historical
performance/priority claims, the detailed empirical fluctuation of
D'_N, and high-precision constants were not independently reproduced.
The full asymptotic enumeration proof in the cited leftist-tree papers
is accepted as external work; its normalization was checked. The
external rare worst-case constructions mentioned after answer32 were
not reconstructed. Answer37's reduction to digital search trees was
read; its exact asymptotic formula is a forward dependency on §6.3,
Eq.(13) and exercise28, to be revisited there. The precise implementation
speed comparison of ternary heaps is not a machine-independent claim.

Known corrections were screened in all five layers, including first
edition context; see `sources/selection-errata-review.json`. They are
not new findings or red markers. No broad calculation, new claim
inventory, or full program verifier was run.
