# Terms and notation

Read this alongside the [catalogue](README.md). Each entry's book section and
exercise or page is the reference for its precise definitions. Named algorithms
such as X, K and L are local names in those sections; the same letter elsewhere
can mean a different algorithm. A question's parameters and computational model
are also local to that entry.

## Locations and assessments

- **TAOCP**: Donald Knuth's *The Art of Computer Programming*.
- **Fascicle**: a separately published installment of a volume. **F7** denotes
  the supplied Constraint Satisfaction fascicle.
- **MPR**: *Mathematical Preliminaries Revisited*, the introductory mathematical
  material in Volume 4B; its answers have their own exercise numbers.
- **MIX and MMIX**: Knuth's illustrative computer architectures. An instruction
  count on one is not automatically a complexity bound for the other.
- **Research rating**: the number beside an exercise. The mathematical prefixes
  M and HM are part of the book's rating, not current literature assessments.
- **Amendment**: an official update to the book, including improved results and
  changed exercises. It need not represent an error in the original text.
- **Reported resolution**: a publication or computation claims the target has
  been settled, but this review has not independently certified it. See the full
  [assessment definitions](README.md#reading-the-assessments).

## Growth, probability and complexity

- **Asymptotic**: describing behavior as a size parameter tends to infinity.
  O(g(n)) is an upper bound up to a constant factor; Omega(g(n)), also written
  Ω(g(n)), is a corresponding lower bound; Theta(g(n)), or Θ(g(n)), means both.
  The constant must not depend on n. Its other permitted dependencies matter.
- **Asymptotic equivalent**: f(n)/g(n) tends to 1. Knowing only the order of
  growth, or the leading term of log f(n), is weaker.
- **o(1)**: a quantity tending to zero. **Amortized time** averages cost over a
  whole operation sequence; it is not necessarily average time on random inputs.
- **Bit complexity**: counting operations on individual bits. **Word complexity**
  counts operations on machine words; the word size and allowed operations matter.
- **Polynomial time**: a running-time bound n^c for a fixed constant c, up to
  constant factors. **Exponential time** typically has a factor a^n with a > 1.
- **P and NP**: decision problems solvable in polynomial time, and decision
  problems whose yes answers have polynomial-size, efficiently checkable
  certificates, respectively. NP-complete problems can encode every problem in NP.
- **#P-complete**: a corresponding hardness classification for counting
  efficiently checkable witnesses. It does not by itself prove that no fast
  counting algorithm exists.
- **Uniform versus nonuniform**: a uniform algorithm works for every input size
  by one fixed procedure. Nonuniform circuits may be separately chosen for each
  size. Restricted uniform sorting has its own specialized book definition.
- **Competitive ratio**: the worst-case factor comparing an online algorithm's
  cost with an optimum algorithm that may know the entire request sequence.
- **Stationary distribution**: a probability law unchanged by one transition
  of a random process. **Covariance** measures dependence through centered products.
- **Discrepancy**: deviation from a target distribution or balance; the sets over
  which deviations are measured differ between the catalogue's questions.
- **Equidistribution modulo 1**: fractional parts occupy every subinterval of
  [0,1) with limiting frequency equal to its length.
- **Normality of a number**: every fixed-length digit block has the expected
  limiting frequency in a specified base. **Benford's law** instead describes a
  logarithmic distribution of leading significant digits.

## Arithmetic, circuits and data structures

- **Addition chain**: a sequence starting at 1 in which each later integer is
  the sum of two earlier entries. Its length counts the additions.
- **GCD**: greatest common divisor. Binary-GCD algorithms use subtraction and
  powers of two; different update rules require different analyses.
- **Mersenne prime**: a prime of the form 2^p − 1. **Fermat prime**: a prime of
  the form 2^(2^m) + 1, with a nonnegative integer m.
- **RSA**: a public-key construction using modular exponentiation with a
  composite modulus. Recovering messages and factoring the modulus are different
  computational tasks; their relationship is itself a research question.
- **Tensor rank**: the smallest number of simple tensor products whose sum gives
  a tensor. **Border rank** permits a limit of such sums. The coefficient field
  matters in both definitions.
- **Permanent**: the matrix sum resembling the determinant with all permutation
  signs replaced by +1.
- **Boolean function**: a function of binary inputs with a binary output.
  A **Boolean circuit** or **chain** combines specified logical operations;
  its **size** counts gates and its **depth** is the longest dependency path.
- **Threshold function**: its output tests whether a weighted sum of its inputs
  exceeds a threshold. **Self-dual** means complementing all inputs complements
  the output. **Symmetric** means the output depends only on the number of 1-bits.
- **Prime implicant**: a minimal conjunction of literals that forces a Boolean
  function to be true. A **literal** is a variable or its negation.
- **BDD**: binary decision diagram, a shared directed graph of binary tests.
  **OBDD**: a BDD with a fixed variable order along every path. **ZDD**:
  zero-suppressed decision diagram, a related representation particularly suited
  to families of subsets. Their reduction conventions differ; see §7.1.4.
- **Broadword operations**: operations acting on many bits of a word together,
  such as bitwise logic and shifts. **Population count** is the number of 1-bits;
  **parity** is that count modulo 2; **majority** tests whether it exceeds half
  the word length. The allowed arithmetic is part of the model in §7.1.3.
- **2-adic arithmetic**: arithmetic organized by powers of two, allowing infinite
  expansions toward more significant bits. The book's chain model specifies the
  permitted operations; ordinary real-number intuition does not define it.
- **Deque**: a queue allowing insertion and deletion at both ends.
- **Splay tree**: a binary search tree reorganized by rotations after access.
  Dynamic optimality asks whether splaying has a constant competitive ratio;
  the complete conjecture is located in Volume 3, §6.2.3, p. 478.
- **2–3 tree**: a balanced search tree whose internal nodes have two or three
  children. **Fringe analysis** studies distributions of small subtrees near leaves.
- **Open addressing**: hashing that stores entries directly in table slots and
  resolves collisions by probing other slots. Success and failure search costs
  are different objectives.
- **Sorting network**: a fixed arrangement of pairwise compare-and-swap
  operations. Its size is its number of comparators; its depth counts parallel
  layers. An **alphabetic tree** preserves the given order of its leaves.

## Graphs and combinatorial generation

- **Graph**: vertices joined by edges. A **directed graph** has oriented edges,
  also called arcs. **Girth** is the length of a shortest cycle.
- **Graph coloring**: assigning vertex labels so adjacent vertices receive
  different labels. The minimum number of colors is the **chromatic number**.
  Radio coloring imposes additional distance-dependent separation constraints.
- **Regular graph**: every vertex has the same number of incident edges.
  **Cubic** means degree three. **Planar** means drawable without edge crossings.
- **Hamilton path or cycle**: a path or cycle visiting each vertex exactly once.
  A **spanning tree** connects every vertex without a cycle. An **arborescence**
  is the corresponding rooted, consistently oriented directed tree.
- **Hypercube**: the graph on binary strings of a fixed length, adjacent when
  they differ in one bit. A **line graph** has a vertex for each original edge,
  with adjacency for edges sharing an endpoint.
- **Linear extension**: a total ordering consistent with a given partial order.
  For a directed acyclic graph, this is a topological ordering.
- **Gray code**: an enumeration in which successive objects differ by a
  prescribed small change. A change in one representation need not be a small
  change in another. **Revolving-door order** usually exchanges one component.
- **Universal cycle**: a cyclic encoding in which every target object appears
  exactly once as a fixed-length window, under the specified representation.
- **Restricted growth string**: an encoding of a set partition that labels blocks
  in order of first appearance. **Zaks sequence**: the tree encoding used in
  Volume 4A, §7.2.1.6; the unit-change requirement refers to that encoding.
- **Tamari lattice**: parenthesizations ordered by directed associativity moves.
  A maximal chain follows successive covering moves from bottom to top.
- **Latin square**: an array in which each symbol occurs once in each row and
  column. Squares are **orthogonal** when their superimposed symbol pairs never
  repeat. A **transversal** selects one cell from every row and column with
  distinct symbols.
- **Graceful labeling**: distinct vertex labels chosen from 0 through the edge
  count so that absolute endpoint differences give each positive edge label
  exactly once. The variants “digraceful,” “rainbow-graceful” and weak gracefulness
  have separate definitions in Fascicle 7, §7.2.2.3.
- **MNH**: minimally non-Hamming, in the graph-representation sense defined at
  the Fascicle 7 entry's locator; minimality refers to the allowed reductions.
- **Arctic curve**: a limiting boundary separating random-looking and frozen
  portions of a random tiling. A **lozenge** is a rhombus made of two adjacent
  lattice triangles; dominoes are two adjacent squares. The two tiling models
  have different boundaries.

## Constraint problems and proofs

- **SAT**: satisfiability of a Boolean formula. A **clause** is a disjunction of
  literals; **k-SAT** restricts clause width. A threshold asks where random
  instances change from usually satisfiable to usually unsatisfiable.
- **Resolution**: an inference rule combining clauses with opposite literals
  of one variable. A **refutation** derives the empty clause. Tree-like proofs
  restrict reuse, unlike general directed proof graphs.
- **CDCL**: conflict-driven clause learning, a SAT-solving technique that learns
  consequences from failed partial assignments. The precise algorithm matters
  for running-time comparisons.
- **ETH and SETH**: the exponential time hypothesis and its strong version.
  They assert particular exponential lower bounds for SAT; deterministic and
  randomized formulations must be distinguished.
- **CSP**: constraint satisfaction problem, assigning values to variables subject
  to permitted relations. A **polymorphism** is an operation preserving those
  relations, helping identify tractable cases. A Maróti pair is the specific
  algebraic structure defined in Fascicle 7, §7.2.2.3, near exercises 474–476.
- **Polynomial delay**: an enumeration algorithm takes polynomial time before
  its first output and between consecutive outputs, including termination.
- **Exact cover**: selecting sets so that every required item is covered exactly
  once. Algorithm X is Knuth's backtracking procedure for this problem.
- **Tomography**: reconstructing a discrete image from prescribed line sums.
- **Conway's Life**: the binary square-grid cellular automaton whose next state
  depends on the eight neighboring cells. Boundaries, population limits and
  allowed initial regions are essential parts of each catalogue question.
