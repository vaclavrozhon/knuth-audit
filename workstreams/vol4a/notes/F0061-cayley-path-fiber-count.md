# The Cayley-path proof uses the full symmetric-group count

**Location.** Volume 4A, first edition, first printing (2011), answer
7.2.1.2–72, printed page 714 / file page 731. The exercise on page 351
concerns a Cayley graph for a permutation group G; the definition on
page 338 expressly allows any such group.

The answer asserts that a Hamiltonian path contains (n-1)! permutations
taking y to x and the same number fixing x. Those counts apply to the
full symmetric group, not to an arbitrary G. A Hamiltonian path is a
path visiting every group element exactly once.

For example, let n=3, G={(), (1 2 3), (1 3 2)}, and use the single
generator (1 2 3), with x=1 and y=2. The path

    () -> (1 2 3) -> (1 3 2)

contains only one element taking 2 to 1 and only one fixing 1.
The answer claims two of each. The endpoint assertion itself is true.

**Correction.** Replace (n-1)! throughout by h, the number of elements
of G fixing x. Multiplication by the inverse of any one generator
gives a bijection from elements fixing x to elements taking y to x,
so both sets have size h. Each nonfinal vertex of the latter set is
followed by a vertex fixing x. Since the initial identity already fixes
x, all h such vertices cannot have successors of that kind. Thus the
last vertex takes y to x, exactly as the exercise requires.

The original pages were inspected. No corresponding correction was
found in the current/historical 4A errata or the Fascicle 2 lists.
Targeted public searches found the same count in an earlier Knuth
draft, but no explicit correction. Absolute priority is not established.
See sources/cayley-generators-source-check.json. No code was needed.
