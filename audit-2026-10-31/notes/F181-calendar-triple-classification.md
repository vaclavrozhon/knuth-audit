# F181 — calendar-puzzle exclusion list contradicts its total and example

Volume 4B, first edition, second printing (2022), §7.2.2.1 answer 291,
printed page 491 / PDF page 511. The question on printed page 158 and the
answer were read together; original typesetting is preserved in
`images/first100-p491.png`.

The answer classifies triples of distinct pentominoes using an explicit
reject/restore rule. Its two initial rejected sets are disjoint: 55 triples
contain X, and 10 are drawn from {O,R,S,W,Z}. It then restores seven triples
of the form P?X, with ? in {O,Q,S,T,U,V,Y}, and three more triples ORS, OSW,
RSW. Finally it rejects RTZ and TWZ, neither of which was already rejected.
Consequently the printed rule excludes

    55 + 10 − 7 − 3 + 2 = 57

triples, leaving 163 of the 220 possibilities. The same paragraph says
that 53 are unsuitable and 167 remain. Independently, the rule rejects QTX
(it contains X and is not among the restored triples), although the answer
explicitly identifies QTX as a valid, particularly difficult choice.

This establishes an internal inconsistency without enumerating calendar
packings. **57 is the size of the printed exclusion list, not a claim about
the true number of unsuitable triples.** The list may be incomplete; the
text alone does not establish which changes repair the classification.
The numerical totals and the list should be reconciled, and QTX should
not be both rejected and presented as a valid choice.

The six historical/current errata layers all4b/err4b, all4f5/err4f5,
all4f6/err4f6 and their three TeX sources were searched by exercise, page,
calendar, and the distinctive triples. Their current downloads were
rechecked on 7 November 2026 and match the archived hashes. No correction
to this claim was found. Targeted public searches likewise found no
matching correction; a public copy of Knuth's September 2019 pre-fascicle
repeats the same inconsistent classification
([fasc5c.pdf](https://www.ioccc.org/2019/ciura/fasc5c.pdf)).
This does not establish absolute priority or the content of a later
physical printing. See `sources/first100-calendar291-novelty.json` and
`results/first100-calendar291.json` for the exact checks.
