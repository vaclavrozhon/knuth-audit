# F173: Sketch values need not belong to the original sets

Status: confirmed locally; low severity. TAOCP4B, first edition,
second printing PDF, printed page387/file407, answer MPR111(b).
The physical copy has not been checked. Independent root acceptance
is not asserted here.

The first sentence of the answer puts both sketch values in A union B.
But the exercise defines S_A as the minimum of the permuted values aπ.

Take n=2 and choose uniformly from the family {12,21}. This family is
minwise independent: each singleton necessarily wins, and each member
of {1,2} has the smaller image in exactly one of the two permutations.
Let A=B={1}. For π=21, S_A=S_B=2, although A union B={1}.
Thus the printed membership claim is false with probability1/2,
using only nonempty sets and fully defined finite values.

Replace the union by its image under π, or apply π inverse to the two
sketch values. To finish the proof, let W be the unique element of
A union B with minimum image. Equality of the two sketches holds
exactly when W belongs to A intersection B. Each union element is W
with probability1/|A union B|, giving the stated collision formula.
The three-set formula and all numerical results remain valid.

The same sentence is visible in the original book PDF and the author's
11September2019 Pre-Fascicle5A, printed page43/file49. All six local
official errata layers (4B, Fascicle5, Fascicle6, both short and full)
and their three TeX sources were searched by page, exercise and topic.
No applicable correction was found. The nearby Fascicle5 correction
on page23 belongs to exercise112 and does not repair this sentence.

Evidence: `sequential-mpr-ex111.md`, the full claim map and errata
record, original images `ref-043.png`, `ref-407.png`, `fasc5a-29.png`,
`fasc5a-49.png`. Only file407 is an error location; the valid main
claims on file43 are not error locations.
