# F7: Volume 4, Fascicle 7: Constraint Satisfaction

Published fascicle · Digital release 1 · 2025. Literature review as of **2026-11-12**.

25 entries. [Index and status meanings](README.md) · [Terms and notation](GLOSSARY.md).

Page numbers refer to the supplied edition. These short paraphrases locate questions; consult the book for complete hypotheses and algorithm definitions.

| Location | Research question | Book rating | Literature assessment |
| --- | --- | --- | --- |
| §7.2.2.3, printed p. 23 | [Random graceful labelings](#f7-t-random-graceful) | Unrated passage | Open-ended project |
| §7.2.2.3, printed p. 24 | [Graceful tree conjecture](#f7-t-graceful-tree) | Unrated passage | Partial results |
| §7.2.2.3, printed p. 27 | [Graceful tournaments](#f7-t-tournament) | Unrated passage | Resolution not located |
| §7.2.2.3, exercise 37, printed p. 116 | [Realizing signed cubic skeletons](#f7-7-2-2-3-37) | [HM46] | Resolution not located |
| §7.2.2.3, exercise 48, printed p. 117 | [Realizability of Huffman–Clowes networks](#f7-7-2-2-3-48) | [M46] | Resolution not located |
| §7.2.2.3, exercise 66, printed p. 119 | [Weak realizability of line drawings](#f7-7-2-2-3-66) | [HM46] | Resolution not located |
| §7.2.2.3, exercise 81, printed p. 121 | [Graceful labelings of K_n × P_4](#f7-7-2-2-3-81) | [46] | Partial results |
| §7.2.2.3, exercise 84, printed p. 121 | [Gracefulness of K_4 × P_r](#f7-7-2-2-3-84) | [46] | Partial results |
| §7.2.2.3, exercise 96, printed p. 121 | [Graceful cubic graphs](#f7-7-2-2-3-96) | [46] | Resolution not located |
| §7.2.2.3, exercise 106, printed p. 122 | [Counting graceful trees](#f7-7-2-2-3-106) | [HM46] → [HM43] | Partial results |
| §7.2.2.3, exercise 119, printed p. 125 | [Other labelings of complete bipartite graphs](#f7-7-2-2-3-119) | [M46] | Resolution not located |
| §7.2.2.3, exercise 138, printed p. 127 | [Weak digracefulness](#f7-7-2-2-3-138) | [46] | Resolution not located |
| §7.2.2.3, exercise 147, printed p. 128 | [Rainbow-graceful forests](#f7-7-2-2-3-147) | [46] | Resolution not located |
| §7.2.2.3, exercise 231, printed p. 136 | [Resolution complexity of Sierpiński graph colorings](#f7-7-2-2-3-231) | [M46] → [M30] | Resolved |
| §7.2.2.3, exercise 474, printed p. 155 | [Algorithms exploiting a Maróti pair](#f7-7-2-2-3-474) | [M48] | Resolution not located |
| §7.2.2.3, exercise 476, printed p. 155 | [Polynomial-delay enumeration of CSP solutions](#f7-7-2-2-3-476) | [M46] | Partial results |
| §7.2.2.3, answer 63, printed p. 173 | [Are the linear realization constraints sufficient?](#f7-a-lp-realization) | Unrated passage | Resolution not located |
| §7.2.2.3, answer 93, printed p. 178 | [Smallest graceful regular graphs](#f7-a-regular) | Unrated passage | Resolution not located |
| §7.2.2.3, answer 155, printed p. 192 | [Are minimally non-Hamming graphs planar?](#f7-a-mnh) | Unrated passage | Resolution not located |
| §7.2.2.3, answer 206, printed p. 202 | [Induced knight-grid asymptotics](#f7-a-knight-grids) | Unrated passage | Partial results |
| §7.2.2.3, answer 227, printed p. 208 | [Largest removable sets in Sierpinski graphs](#f7-a-sierpinski-edges) | Unrated passage | Resolution not located |
| §7.2.2.3, answer 233, printed p. 209 | [Largest removable edge sets in flower-snark line graphs](#f7-a-flower-edges) | [40] | Resolved |
| §7.2.2.3, answer 245, printed p. 211 | [Explaining anomalous encoding runtimes](#f7-a-encoding-runtime) | Unrated passage | Resolution not located |
| §7.2.2.3, answer 281, printed p. 218 | [Janson's chain-CSP probability asymptotics](#f7-a-janson) | Unrated passage | Partial results |
| §7.2.2.3, answer 357, printed p. 237 | [Nonattacking queens with no three collinear](#f7-a-no-three-queens) | Unrated passage | Resolution not located |

<a id="f7-t-random-graceful"></a>

## Random graceful labelings

**§7.2.2.3, printed p. 23** · Question in the main text · Unrated passage · `F7-T-random-graceful`

Enumerate and understand the distribution of the random graceful labelings in the fascicle, including connectedness, planarity, bipartiteness, triangle-freeness, regularity and the proposed asymptotic three-colorability.

**Open-ended project.** This groups several distributional and enumerative questions about the random-labeling model. The 2026 counting result for graceful trees does not establish the stated typical planarity, connectivity or coloring claims.

Evidence: [Li, Rainbow maps and the number of graceful labelings of trees (2026)](https://arxiv.org/abs/2610.34877).

[Recorded searches](SEARCHES.md): [S65](SEARCHES.md#s65), [S67](SEARCHES.md#s67), [S68](SEARCHES.md#s68), [S70](SEARCHES.md#s70).

<a id="f7-t-graceful-tree"></a>

## Graceful tree conjecture

**§7.2.2.3, printed p. 24** · Question in the main text · Unrated passage · `F7-T-graceful-tree`

Can every tree with m edges be assigned distinct vertex labels from 0 to m so that its absolute edge differences are exactly 1 through m?

**Partial results.** Special tree classes, finite checks and graceful-supertree embeddings are known. A November 2026 preprint gives a smaller graceful supertree containing any input tree; this does not make the input tree itself graceful. No generally accepted proof of the full conjecture was verified.

Evidence: [Okechukwu, Graceful supertrees with at most 2m−diam(T) edges (2026)](https://arxiv.org/abs/2611.01340).

[Recorded searches](SEARCHES.md): [S65](SEARCHES.md#s65).

<a id="f7-t-tournament"></a>

## Graceful tournaments

**§7.2.2.3, printed p. 27** · Question in the main text · Unrated passage · `F7-T-tournament`

For which orders does the fascicle's graceful labeling of an oriented complete graph exist, including the general construction linked to skew Hadamard difference sets?

**Resolution not located.** No primary publication settling this precise question was located in the recorded searches. This is an unverified current status, not evidence that the question remains open.

[Recorded searches](SEARCHES.md): [S65](SEARCHES.md#s65).

<a id="f7-7-2-2-3-37"></a>

## Realizing signed cubic skeletons

**§7.2.2.3, exercise 37, printed p. 116** · Exercise · [HM46] · `F7-7.2.2.3-37`

Is it decidable whether a given signed cubic graph is the signed skeleton of a trihedral polyhedral object of the kind defined in the fascicle?

**Resolution not located.** No decision procedure or undecidability proof was located for the exact geometric model of this exercise. Complexity results for fixed line drawings or stronger coordinate assumptions are not interchangeable with it.

[Recorded searches](SEARCHES.md): [S47](SEARCHES.md#s47).

<a id="f7-7-2-2-3-48"></a>

## Realizability of Huffman–Clowes networks

**§7.2.2.3, exercise 48, printed p. 117** · Exercise · [M46] · `F7-7.2.2.3-48`

Is it decidable whether a labeled line-drawing network satisfying the Huffman–Clowes rules has a geometric realization?

**Resolution not located.** No decision procedure or undecidability proof was located for the exact geometric model of this exercise. Complexity results for fixed line drawings or stronger coordinate assumptions are not interchangeable with it.

[Recorded searches](SEARCHES.md): [S47](SEARCHES.md#s47).

<a id="f7-7-2-2-3-66"></a>

## Weak realizability of line drawings

**§7.2.2.3, exercise 66, printed p. 119** · Exercise · [HM46] · `F7-7.2.2.3-66`

Is weak realizability of Huffman–Clowes networks decidable under the fascicle's weaker geometric interpretation?

**Resolution not located.** No decision procedure or undecidability proof was located for the exact geometric model of this exercise. Complexity results for fixed line drawings or stronger coordinate assumptions are not interchangeable with it.

[Recorded searches](SEARCHES.md): [S47](SEARCHES.md#s47).

<a id="f7-7-2-2-3-81"></a>

## Graceful labelings of K_n × P_4

**§7.2.2.3, exercise 81, printed p. 121** · Exercise · [46] · `F7-7.2.2.3-81`

Count graceful labelings of the Cartesian product of a complete graph on n vertices and a four-vertex path.

**Partial results.** Knuth's research notes record computed examples and constructions for Cartesian products of complete graphs and paths. No formula or general construction answering the complete exercise was verified.

Evidence: [Knuth, Selected Combinatorial Research Problems (coups)](https://cs.stanford.edu/~knuth/papers/coups.pdf).

[Recorded searches](SEARCHES.md): [S47](SEARCHES.md#s47).

<a id="f7-7-2-2-3-84"></a>

## Gracefulness of K_4 × P_r

**§7.2.2.3, exercise 84, printed p. 121** · Exercise · [46] · `F7-7.2.2.3-84`

Is the Cartesian product of a four-vertex complete graph and every finite path graceful?

**Partial results.** Knuth's research notes record computed examples and constructions for Cartesian products of complete graphs and paths. No formula or general construction answering the complete exercise was verified.

Evidence: [Knuth, Selected Combinatorial Research Problems (coups)](https://cs.stanford.edu/~knuth/papers/coups.pdf).

[Recorded searches](SEARCHES.md): [S47](SEARCHES.md#s47).

<a id="f7-7-2-2-3-96"></a>

## Graceful cubic graphs

**§7.2.2.3, exercise 96, printed p. 121** · Exercise · [46] · `F7-7.2.2.3-96`

Is every connected 3-regular graph graceful? The answer also conjectures gracefulness of disconnected cubic graphs except disjoint unions of two or more copies of K_4.

**Resolution not located.** Finite computational checks and special classes do not settle the conjecture for every connected cubic graph. No general proof or counterexample was verified.

[Recorded searches](SEARCHES.md): [S48](SEARCHES.md#s48).

<a id="f7-7-2-2-3-106"></a>

## Counting graceful trees

**§7.2.2.3, exercise 106, printed p. 122** · Exercise · [HM46] → [HM43] · `F7-7.2.2.3-106`

Determine the asymptotic growth of the function counting graceful tree labelings introduced in exercise 105.

**Partial results.** The October 2026 official amendment gives log(tau(n)/n!) = n log(2/pi) + O((log n)^4); Li supplies a corresponding preprint and formalization. This establishes the exponential constant. A sharp multiplicative asymptotic equivalent, or the smaller conjectural error term in the old answer, is not established by this statement.

Evidence: [Knuth, Fascicle 7 amendments, answer 106 and added page 283 (2026)](https://www-cs-faculty.stanford.edu/~knuth/err4f7.textxt); [Li, Rainbow maps and the number of graceful labelings of trees (2026)](https://arxiv.org/abs/2610.34877).

Book amendment, 2026-10-10: The leading exponential constant is established; the amended answer states an error of order (log n)^4 in the logarithm. [Official record](https://www-cs-faculty.stanford.edu/~knuth/err4f7.textxt).

[Recorded searches](SEARCHES.md): [S67](SEARCHES.md#s67), [S68](SEARCHES.md#s68), [S70](SEARCHES.md#s70).

<a id="f7-7-2-2-3-119"></a>

## Other labelings of complete bipartite graphs

**§7.2.2.3, exercise 119, printed p. 125** · Exercise · [M46] · `F7-7.2.2.3-119`

Do complete bipartite graphs have graceful labelings outside the two families constructed in exercises 117 and 118?

**Resolution not located.** Enumeration of alpha-graceful labelings is available, but it does not by itself classify all graceful labelings or settle whether the two families in the exercise are exhaustive.

Evidence: [Beluhov, One Curious Identity Counting Graceful Labelings (2022)](https://ecajournal.haifa.ac.il/Volume2022/ECA2022_S2A6.pdf).

[Recorded searches](SEARCHES.md): [S48](SEARCHES.md#s48).

<a id="f7-7-2-2-3-138"></a>

## Weak digracefulness

**§7.2.2.3, exercise 138, printed p. 127** · Exercise · [46] · `F7-7.2.2.3-138`

Can every undirected graph be made graceful as a directed graph by orienting each edge one way or both ways?

**Resolution not located.** No primary publication settling this precise question was located in the recorded searches. This is an unverified current status, not evidence that the question remains open.

[Recorded searches](SEARCHES.md): [S48](SEARCHES.md#s48).

<a id="f7-7-2-2-3-147"></a>

## Rainbow-graceful forests

**§7.2.2.3, exercise 147, printed p. 128** · Exercise · [46] · `F7-7.2.2.3-147`

Is every forest rainbow graceful under the cyclic edge-difference labeling convention of the fascicle?

**Resolution not located.** No primary publication settling this precise question was located in the recorded searches. This is an unverified current status, not evidence that the question remains open.

[Recorded searches](SEARCHES.md): [S48](SEARCHES.md#s48).

<a id="f7-7-2-2-3-231"></a>

## Resolution complexity of Sierpiński graph colorings

**§7.2.2.3, exercise 231, printed p. 136** · Exercise · [M46] → [M30] · `F7-7.2.2.3-231`

Do the stated clauses expressing 3-uncolorability of the Sierpiński graphs require exponentially long resolution refutations?

**Resolved.** The proposed exponential lower bound is false: Knuth's September 2026 amendment gives a linear-length resolution refutation and points to its proof on added page 285.

Evidence: [Knuth, Fascicle 7 amendments, answer 231 and added page 285 (2026)](https://www-cs-faculty.stanford.edu/~knuth/err4f7.textxt).

Book amendment, 2026-09-08: A linear resolution refutation is available. [Official record](https://www-cs-faculty.stanford.edu/~knuth/err4f7.textxt).

[Recorded searches](SEARCHES.md): [S49](SEARCHES.md#s49).

<a id="f7-7-2-2-3-474"></a>

## Algorithms exploiting a Maróti pair

**§7.2.2.3, exercise 474, printed p. 155** · Exercise · [M48] · `F7-7.2.2.3-474`

Find a constraint-solving procedure that exploits the two ternary operations of a Maróti pair, analogous to the algorithms for individual polymorphisms.

**Resolution not located.** Related algebraic algorithms exploit Maltsev operations and quotient structure, but no implementation meeting the exercise's requested general compact-representation scheme for a Maróti pair was verified.

Evidence: [Maróti, Maltsev on top](https://www.fields.utoronto.ca/programs/scientific/11-12/constraint/algebra/maroti1.pdf).

[Recorded searches](SEARCHES.md): [S49](SEARCHES.md#s49), [S50](SEARCHES.md#s50).

<a id="f7-7-2-2-3-476"></a>

## Polynomial-delay enumeration of CSP solutions

**§7.2.2.3, exercise 476, printed p. 155** · Exercise · [M46] · `F7-7.2.2.3-476`

Characterize finite constraint languages for which all solutions can be enumerated with polynomial delay between consecutive outputs.

**Partial results.** Polynomial-delay enumeration is characterized in important restricted settings, including Boolean languages, and structural homomorphism results give further classes. No full classification for the finite languages asked about here was verified. The answer also asks separately for lexicographic output and highlights languages whose many easy solutions can mask hard ones.

Evidence: [Enumerating all Solutions for Constraint Satisfaction Problems (2006)](https://drops.dagstuhl.de/storage/16dagstuhl-seminar-proceedings/dsp-vol06401/DagSemProc.06401.6/DagSemProc.06401.6.pdf); [Bulatov et al., Enumerating Homomorphisms (2009)](https://arxiv.org/abs/0902.1256).

[Recorded searches](SEARCHES.md): [S49](SEARCHES.md#s49), [S50](SEARCHES.md#s50), [S68](SEARCHES.md#s68).

<a id="f7-a-lp-realization"></a>

## Are the linear realization constraints sufficient?

**§7.2.2.3, answer 63, printed p. 173** · Question in an answer · Unrated passage · `F7-A-lp-realization`

Does feasibility of the displayed linear inequalities ensure realization by a trihedral visible polyhedron (3VP), in the precise geometric model defined in the fascicle?

**Resolution not located.** No primary publication settling this precise question was located in the recorded searches. This is an unverified current status, not evidence that the question remains open.

[Recorded searches](SEARCHES.md): [S65](SEARCHES.md#s65).

<a id="f7-a-regular"></a>

## Smallest graceful regular graphs

**§7.2.2.3, answer 93, printed p. 178** · Question in an answer · Unrated passage · `F7-A-regular`

Determine the smallest graceful r-regular graphs for larger degrees, including the unknown edge-count/degree pairs (147,14), (192,16) and (243,18).

**Resolution not located.** No primary publication settling this precise question was located in the recorded searches. This is an unverified current status, not evidence that the question remains open.

[Recorded searches](SEARCHES.md): [S66](SEARCHES.md#s66).

<a id="f7-a-mnh"></a>

## Are minimally non-Hamming graphs planar?

**§7.2.2.3, answer 155, printed p. 192** · Question in an answer · Unrated passage · `F7-A-mnh`

Is every graph that cannot be embedded as an induced subgraph of a Cartesian product of complete graphs, but all its proper induced subgraphs can, planar?

**Resolution not located.** No primary publication settling this precise question was located in the recorded searches. This is an unverified current status, not evidence that the question remains open.

[Recorded searches](SEARCHES.md): [S66](SEARCHES.md#s66).

<a id="f7-a-knight-grids"></a>

## Induced knight-grid asymptotics

**§7.2.2.3, answer 206, printed p. 202** · Question in an answer · Unrated passage · `F7-A-knight-grids`

Determine the asymptotic maximum widths of two-row and three-row grid graphs embedded as induced subgraphs of the knight graph of a square board, including the conjectured positive quadratic-growth constants. The answer also asks for the exact four-row extremal sequence when extra knight edges are allowed.

**Partial results.** Exact small embeddings and solver experiments appear in Trimble's dissertation. No proof of the proposed asymptotic constants for induced two-row and three-row grids was verified. The exact non-induced four-row sequence is likewise not settled by the cited bounds.

Evidence: [Trimble, dissertation, section 5.8.3 Knight's Grid Instances (2023)](https://theses.gla.ac.uk/83350/2/2023TrimblePhD.pdf).

[Recorded searches](SEARCHES.md): [S66](SEARCHES.md#s66).

<a id="f7-a-sierpinski-edges"></a>

## Largest removable sets in Sierpinski graphs

**§7.2.2.3, answer 227, printed p. 208** · Question in an answer · Unrated passage · `F7-A-sierpinski-edges`

Does Stappers's recursive construction give all largest edge sets whose deletion preserves the specified non-three-colorability of the Sierpinski graph, for every level n?

**Resolution not located.** No primary publication settling this precise question was located in the recorded searches. This is an unverified current status, not evidence that the question remains open.

[Recorded searches](SEARCHES.md): [S66](SEARCHES.md#s66).

<a id="f7-a-flower-edges"></a>

## Largest removable edge sets in flower-snark line graphs

**§7.2.2.3, answer 233, printed p. 209** · Question in an answer · [40] · `F7-A-flower-edges`

How many edges can be removed from the line graph of a flower snark J_q, for odd q greater than 3, while it remains impossible to color its vertices with three colors?

**Resolved.** The official September 2026 answer reports independent proofs by Shisheng Li and Aaron Windsor: nine edges can be removed, while deleting any ten makes the graph 3-colorable.

Evidence: [Knuth, official Fascicle 7 amendments, answer 233 (2026)](https://www-cs-faculty.stanford.edu/~knuth/err4f7.textxt).

Book amendment, 2026-09-25: Maximum nine edges; deleting any ten is sufficient for 3-colorability, for odd q>3. [Official record](https://www-cs-faculty.stanford.edu/~knuth/err4f7.textxt).

[Recorded searches](SEARCHES.md): [S77](SEARCHES.md#s77).

<a id="f7-a-encoding-runtime"></a>

## Explaining anomalous encoding runtimes

**§7.2.2.3, answer 245, printed p. 211** · Question in an answer · Unrated passage · `F7-A-encoding-runtime`

Explain the unusually good direct-encoding and poor prefix-encoding performance on the specific graph-coloring benchmarks in the answer.

**Resolution not located.** No published explanation of the specific runtime anomalies was located; performance of an encoding depends on the solver and the precise instance family.

[Recorded searches](SEARCHES.md): [S67](SEARCHES.md#s67).

<a id="f7-a-janson"></a>

## Janson's chain-CSP probability asymptotics

**§7.2.2.3, answer 281, printed p. 218** · Question in an answer · Unrated passage · `F7-A-janson`

In the random chain dependency graph, every vertex i > m independently chooses two distinct earlier predecessors. Let c_(m,n) be the probability that every vertex is reachable from vertex n by following predecessor edges. For fixed m, is c_(m,n) = (rho + o(1))^n with a constant rho < 1?

**Partial results.** Janson establishes the asymptotic number of descendants and moment results. The exponential-rate conjecture concerns the much rarer event that all vertices are descendants; no proof of that assertion was verified.

Evidence: [Janson, The number of descendants in a random directed acyclic graph (2024)](https://doi.org/10.1002/rsa.21195).

[Recorded searches](SEARCHES.md): [S67](SEARCHES.md#s67).

<a id="f7-a-no-three-queens"></a>

## Nonattacking queens with no three collinear

**§7.2.2.3, answer 357, printed p. 237** · Question in an answer · Unrated passage · `F7-A-no-three-queens`

Do n nonattacking queens with no three on any straight line exist for infinitely many board sizes n, and how many such arrangements exist asymptotically?

**Resolution not located.** Knuth’s OEIS record provides finite counts through board size 26. No proof of the requested general existence or asymptotic statement was located; finite enumeration does not establish it.

Evidence: [Knuth and contributors, OEIS A365437](https://oeis.org/A365437).

[Recorded searches](SEARCHES.md): [S67](SEARCHES.md#s67), [S80](SEARCHES.md#s80), [S86](SEARCHES.md#s86).
