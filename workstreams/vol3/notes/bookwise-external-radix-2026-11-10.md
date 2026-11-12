# Bookwise review: external radix sorting, 10 November 2026

Reviewed §5.4.7, printed pp.343–348, all seven exercises and their
answers on p.694. Shared pages 348 and 694 continue into two-tape
sorting and are deferred to that next certification block.

Checked the eight-key and ten-key distribution schedules, their
trees and weighted pass counts (3.5 and 2.8 respectively). The FIFO
restrictions and reverse-time correspondence use the same tape
discipline as §5.4.4; the exceptional requirement to preserve the
original input is explicitly acknowledged. The Fibonacci rule uses
the representation of F_n-1-K, so decreasing digit order gives
increasing keys. The displayed 21-key distribution agrees with this
choice. The mixed-radix answer alternates P and T-P as required.

Examined Mauchly's tree and checked the stability parity in answer 6:
tens digits 0,1,2,3,5 reverse the ones order, while 4,6,7,8,9 preserve
it. The recursive distribution construction and multireel duality
were read together with their stated practical qualifications.
The three possible short output branches and six next-level branches
explain the path-length count in the answer-4 optimum sketch. A later
cross-check against answer 5.4.9-12 and the explicit definition in
volume 1, §2.3, p.308 corrected this audit's initial interpretation:
the root is at level zero. The three level labels in answer 4 are
therefore all one too high; see V3-C0055 and its direct counterexample
from the book's own Ashenhurst tree.

New finding: V3-C0055. The official clarification of reverse time on p.345,
the wording change on p.344, and the mixed-radix terminology change
were screened and excluded.

Limits: exercise 3's research extension was not solved. Answer 4's
short optimum argument was not supplemented by an independent census
of all strongly four-FIFO trees. Historical source algorithms and
comparative hardware performance were not independently reproduced.

Source screen: `sources/external-radix-errata-review.json`.
Next: §5.4.8, printed p.348 / file p.359.
