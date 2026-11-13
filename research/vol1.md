# 1: Fundamental Algorithms

3rd edition · 1st printing · 1997. Literature review as of **2026-11-12**.

9 entries. [Index and status meanings](README.md) · [Terms and notation](GLOSSARY.md).

Page numbers refer to the supplied edition. These short paraphrases locate questions; consult the book for complete hypotheses and algorithm definitions.

| Location | Research question | Book rating | Literature assessment |
| --- | --- | --- | --- |
| §1.2.1, exercise 14, printed p. 20 | [Automatic program verification](#v1-1-2-1-14) | [50] | Open-ended project |
| §1.2.4, exercise 40, printed p. 44 | [Replicative functional equations](#v1-1-2-4-40) | [HM46] | Partial results |
| §1.3.2, exercise 12, printed p. 159 | [Average cost of saddle-point searches](#v1-1-3-2-12) | [M47] → [HM42] | Resolved |
| §2.2.1, exercise 13, printed p. 243 | [Counting deque permutations](#v1-2-2-1-13) | [M48] | Resolved |
| §2.2.3, exercise 13, printed p. 270 | [Linear extensions of the Boolean lattice](#v1-2-2-3-13) | [M48] → [HM48] | Partial results |
| §2.2.3, exercise 25, printed p. 271 | [Topological sorting on tapes](#v1-2-2-3-25) | [47] | Resolution not located |
| §2.5, exercise 30, printed p. 455 | [Average behavior of the buddy allocator](#v1-2-5-30) | [M48] | Resolution not located |
| §2.5, exercise 32, printed p. 455 | [A random storage-request process](#v1-2-5-32) | [HM47] → [HM46] | Resolution not located |
| §2.5, exercise 40, printed p. 456 | [Optimal storage fragmentation constants](#v1-2-5-40) | [HM50] | Resolution not located |

<a id="v1-1-2-1-14"></a>

## Automatic program verification

**§1.2.1, exercise 14, printed p. 20** · Exercise · [50] · `V1-1.2.1-14`

Build a program verifier that infers missing assertions and uses them to prove the supplied program correct.

**Open-ended project.** Automatic assertion discovery and verification have substantial implementations, including property-directed invariant generation. The exercise does not specify a single completeness or performance criterion, so it is not a binary solved/open conjecture.

Evidence: [Bradley and Manna, Property-Directed Incremental Invariant Generation](https://theory.stanford.edu/~arbrad/papers/pdiig.pdf); [Software Verification with PDR: Implementation and Empirical Evaluation (2019)](https://arxiv.org/abs/1908.06271).

[Recorded searches](SEARCHES.md): [S03](SEARCHES.md#s03).

<a id="v1-1-2-4-40"></a>

## Replicative functional equations

**§1.2.4, exercise 40, printed p. 44** · Exercise · [HM46] · `V1-1.2.4-40`

Classify functions satisfying Knuth's replication identities, including continuous solutions and the more general identities with scale-dependent coefficients.

**Partial results.** Regularity-restricted classifications were already known to the book: its answer gives the continuous case and cites Yoder (1975). Lucht develops related systems of functional equations. This is not a claim to classify all unrestricted functions in every generalized identity.

Evidence: [Lucht, Arithmetical sequences and systems of functional equations (1997)](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356261603_0053/PPN356261603_0053.pdf).

[Recorded searches](SEARCHES.md): [S02](SEARCHES.md#s02).

<a id="v1-1-3-2-12"></a>

## Average cost of saddle-point searches

**§1.3.2, exercise 12, printed p. 159** · Exercise · [M47] → [HM42] · `V1-1.3.2-12`

Compare the three proposed matrix saddle-point search algorithms under both random distinct entries and random binary entries.

**Resolved.** Hofri and Jacquet analyze Knuth's three saddle-point search algorithms. The official amendment lowers the exercise to HM42; detailed machine-instruction accounting still depends on the chosen implementation.

Evidence: [Hofri and Jacquet, Saddle Points in Random Matrices: Analysis of Knuth Search Algorithms (1998)](https://doi.org/10.1007/PL00009237).

Book amendment, 1997-04-24: Rating lowered after average-case analysis. [Official record](https://www-cs-faculty.stanford.edu/~knuth/all1-prepre.ps.gz).

[Recorded searches](SEARCHES.md): [S04](SEARCHES.md#s04).

<a id="v1-2-2-1-13"></a>

## Counting deque permutations

**§2.2.1, exercise 13, printed p. 243** · Exercise · [M48] · `V1-2.2.1-13`

Count the permutations obtainable using a deque, a queue that permits insertion and removal at either end.

**Resolved.** Elvey Price and Guttmann give exact enumeration through functional equations. This settles enumeration in that sense; it is not a closed elementary formula or a rigorous full asymptotic expansion.

Evidence: [Elvey Price and Guttmann, Permutations sortable by deques and by two stacks in parallel (2015)](https://arxiv.org/abs/1508.02273); [Elvey Price, Permutations sortable by deques and two stacks in parallel share the same growth rate (2019)](https://arxiv.org/abs/1912.00056).

[Recorded searches](SEARCHES.md): [S01](SEARCHES.md#s01), [S04](SEARCHES.md#s04).

<a id="v1-2-2-3-13"></a>

## Linear extensions of the Boolean lattice

**§2.2.3, exercise 13, printed p. 270** · Exercise · [M48] → [HM48] · `V1-2.2.3-13`

Count the orders of all subsets of an n-element set that respect inclusion; the amended exercise requests a sharp asymptotic estimate.

**Partial results.** Brightwell and Tetali determine the leading logarithmic asymptotics for the number of linear extensions. That does not give an asymptotic equivalent with ratio tending to one, as requested by the amended sharp-asymptotic question.

Evidence: [Brightwell and Tetali, The Number of Linear Extensions of the Boolean Lattice (2003)](https://doi.org/10.1023/B:ORDE.0000034596.50352.f7).

Book amendment, 2018-03-15: The request is sharpened to a sharp asymptotic estimate. [Official record](https://www-cs-faculty.stanford.edu/~knuth/all1-pre.ps.gz).

[Recorded searches](SEARCHES.md): [S01](SEARCHES.md#s01).

<a id="v1-2-2-3-25"></a>

## Topological sorting on tapes

**§2.2.3, exercise 25, printed p. 271** · Exercise · [47] · `V1-2.2.3-25`

Design the most efficient topological sorting algorithm when the graph exceeds internal memory and all external storage is sequential magnetic tape.

**Resolution not located.** External-memory topological-sorting algorithms were located, but block I/O and semi-external algorithms do not establish optimality in this exercise's sequential-tape model. No resolution of that exact optimization question was located.

Evidence: [Engineering Algorithms for Solving Geometric and Graph Problems, Chapter 8](https://dalspaceb.library.dal.ca/server/api/core/bitstreams/bbaca9de-d37b-434c-9a1e-8e87560f3d5e/content).

[Recorded searches](SEARCHES.md): [S01](SEARCHES.md#s01), [S05](SEARCHES.md#s05).

<a id="v1-2-5-30"></a>

## Average behavior of the buddy allocator

**§2.5, exercise 30, printed p. 455** · Exercise · [M48] · `V1-2.5-30`

Analyze the average behavior of the binary buddy system's allocation and release algorithms under suitable random request models.

**Resolution not located.** Stochastic models and partial buddy-system analyses exist, including Purdom–Stigler as discussed in the book. No general average analysis matching both of the specified algorithms and a fully specified request model was located. The answer depends on that model.

[Recorded searches](SEARCHES.md): [S04](SEARCHES.md#s04), [S05](SEARCHES.md#s05).

<a id="v1-2-5-32"></a>

## A random storage-request process

**§2.5, exercise 32, printed p. 455** · Exercise · [HM47] → [HM46] · `V1-2.5-32`

Determine whether the mean in Knuth's recursively defined, capped random storage-request process converges, and determine its limit.

**Resolution not located.** No primary resolution of the precise capped stochastic recurrence was located. Use the officially corrected initial condition and bound, not the first-printing statement.

Book amendment, 2002-11-09: Initial condition and lower bound corrected; rating lowered by one. [Official record](https://www-cs-faculty.stanford.edu/~knuth/all1-prepre.ps.gz).

[Recorded searches](SEARCHES.md): [S02](SEARCHES.md#s02), [S05](SEARCHES.md#s05).

<a id="v1-2-5-40"></a>

## Optimal storage fragmentation constants

**§2.5, exercise 40, printed p. 456** · Exercise · [HM50] · `V1-2.5-40`

Determine the optimal asymptotic storage factors for maximum block sizes 3 and 4, and the limiting growth of that factor as the maximum block size increases. The answer also raises Robson's harmonic-number conjecture.

**Resolution not located.** Later competitive-allocation bounds do not by themselves determine the exact constants N(3), N(4), or the conjectured harmonic asymptotics. No matching resolution was located.

Evidence: [Luby, Naor and Orda, Tight Bounds for Dynamic Storage Allocation (1996)](https://doi.org/10.1137/S089548019325647X).

[Recorded searches](SEARCHES.md): [S02](SEARCHES.md#s02), [S03](SEARCHES.md#s03), [S05](SEARCHES.md#s05).
