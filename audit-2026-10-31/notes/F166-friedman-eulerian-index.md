# F166 — One-step index error in the Friedman-urn distribution

Status: locally confirmed against the original PDF, the author's PostScript,
and all six saved errata layers plus their three available TeX sources.
Coordinator review, physical-copy verification and priority are not asserted.

Location: TAOCP Volume4B, Mathematical Preliminaries Redux, answer74,
printed p381, file page401. The question and diagram on p19/file39 are valid.

Let A(N,k) denote the Eulerian number counting permutations of N elements
with exactly k descents. This is the convention explicitly defined in
Volume3, Section5.1.3, p35/file46, and used in its recurrence on p36/file47.
The original pages were displayed; A(1,0)=1 and A(1,1)=0 follow immediately.

Answer74 prints the probability of node (r,n+2−r) on level n as

    A(n,r−1)/n!.

The urn starts at (1,1) on level0. A fair first draw is replaced and adds
a ball of the opposite color, so each level1 node, (1,2) and (2,1),
has probability1/2. The printed formula instead gives1 and0.

This is not a different level convention: the original diagram explicitly
labels its root level0 and the two children level1, while the answer
explicitly writes (r,n+2−r). Both the PDF and the 2019 PostScript contain
the same formula.

The correction is

    P(R_n=r)=A(n+1,r−1)/(n+1)!,    1≤r≤n+1.

Here is a complete proof. Associate a permutation of n+1 elements with
r equal to its number of ascending runs. Starting with (1), insert each
new maximum in a uniformly chosen position. The new maximum retains
the run count in exactly r positions: after the end of each old run.
Inserting at the beginning or inside an ascent increases the run count
by one; these are the other n+2−r positions. Thus the probabilities
of retaining r and increasing it are r/(n+2) and (n+2−r)/(n+2),
exactly the opposite-color urn transitions.

Deleting the largest element gives each permutation a unique predecessor.
Consequently every permutation of n+1 elements has probability1/(n+1)!,
and precisely A(n+1,r−1) have r runs. This proves the corrected formula
including the root. It also proves the valid permutation explanation
already printed immediately after the erroneous formula.

For every n≥1 the discrepancy is visible at the rightmost node:
the printed probability is A(n,n)/n!=0, but the successive additions
of red balls have probability (1/2)(1/3)···(1/(n+1))=1/(n+1)!>0.
No numerical computation is required.

All twenty displayed diagram edge labels were checked separately.
The first four correct probability rows are
(1), (1,1)/2, (1,4,1)/6, and (1,11,11,1)/24.
The diagram, the urn model, the permutation correspondence, and the
martingale in answer75 remain valid.

The six-layer search covers err4b/all4b, err4f5/all4f5 and err4f6/all4f6,
including shifted historical pages and the terms Friedman/Eulerian,
with the available TeX sources checked as well. Matches concern other
sections or the already incorporated neighboring exercise72 wording.
No applicable correction was found in the saved snapshots.

Evidence:
- notes/sequential-mpr-ex073-076.md: complete73–76 arguments and diagram table.
- results/sequential/mpr-073-076-urn-errata.json: hashes and contextual matches.
- images/sequential/ref-401.png: original Volume4B answer.
- images/sequential/file-039.png: original valid question and level labels.
- images/sequential/fasc5a-44.png: author's PostScript answer, printed p38.
- images/sequential/vol3-ref035.png and vol3-ref036.png: Eulerian convention.

Suggested severity: medium, since the principal requested probability
distribution is wrong, even though the repair is a local index shift.

