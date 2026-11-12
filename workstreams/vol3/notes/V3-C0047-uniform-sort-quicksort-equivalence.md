# V3-C0047 — Uniform sorting does not compare the same pairs as Algorithm Q

Confirmed in volume 3, second edition, first printing (1998), exercise
5.3.4-64, printed p.246, and answer p.675; file pp.257 and 686.
The claimed equivalence to Algorithm 5.2.2Q, after redundant comparisons
are suppressed as in exercise 5.2.2-24, fails because Q's partition
changes the order of the remaining records.

Use distinct input keys `(4,2,1,3)` and the permitted cutoff M=1.
Ignore sentinel comparisons and repeated comparisons whose outcomes are
already known, exactly as required in the exercise.

Algorithm Q first uses pivot 4, comparing it with 2,1,3. Its pivot exchange
leaves `(3,2,1,4)`. The next pivot is 3, which is compared with 2 and 1;
the pivot exchange then leaves `(1,2,3,4)`. Finally the two-element
subproblem compares 1 with 2. Thus all six unordered pairs of real keys
are compared. Each of these six comparisons is undetermined by the
comparisons preceding it.

Uniform sorting instead retains the original key identities and considers
the original-index pairs in lexicographic order. Its comparisons are

```
original indices: (1,2) (1,3) (1,4) (2,3) (2,4)
key values:       (4,2) (4,1) (4,3) (2,1) (2,3).
```

The remaining pair (3,4), namely keys 1 and 3, is skipped because
`1<2<3` is already known. This is a path of length two, so the same
counterexample applies to both restricted and unrestricted uniform
sorting. Uniform sorting makes five comparisons, whereas Q makes six.

The induction in the printed answer overlooks the reordering caused by
Q's partition. The asserted pair equivalence can instead be formulated
for a quicksort variant that chooses the earliest original record in
each recursive part as pivot, for example by preserving original order
within the parts. The specific reference to Algorithm Q is false.
The independent average-comparison calculation in exercise 65 is not
refuted by this example.

The algorithm, the exercise, and the answer were checked against the
original images, including `images/bookwise-p116.png`,
`images/bookwise-p246.png`, and `images/bookwise-p675.png`.
All five official errata layers were screened in
`sources/networks-errata-review.json`; public searches for the claimed
uniform-sorting/quicksort equivalence found no report of this example.
That limited search does not establish absolute priority.
