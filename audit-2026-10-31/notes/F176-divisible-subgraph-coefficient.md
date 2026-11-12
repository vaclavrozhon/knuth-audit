# F176 — Wrong sign of the top coefficient in MPR116

Status: locally confirmed, low severity. Location: Volume4B,p389,
answer to MPR116,file page409 only. The statement onp24 remains valid.

The displayed polynomial is

    f=product_v(1−g_v^(p−1))−product_e(1−x_e).

Its first product has total degree at most(p−1)n<m. Consequently,
the coefficient of product_e x_e is **(−1)^(m+1)**, whereas the answer
prints **(−1)^m**. The missing outer minus comes from subtracting the
second product.

An exact counterexample to the printed coefficient is p=3, two vertices
and five parallel edges between them. Here m=5>4, and both vertex
degrees are5<6, so even the regular-subgraph corollary's degree condition
holds. With S=x_1+…+x_5, the first product is(1−S²)² and has degree4.
The actual coefficient of x_1…x_5 is1; the printed coefficient is−1=2
in F_3. No enumeration or numerical approximation is involved.

Change the exponent to m+1. Both the wrong and correct values are
nonzero, so the polynomial argument and the requested existence theorem
remain valid. The complete audit additionally states the preceding
degree as an upper bound, covering isolated vertices and zero loop
incidence forms in characteristic2; this small qualifier is recorded
with the same local proof note, without an additional finding card.

Original4Bfile409 and the author's11September2019 Pre-Fascicle5A,
p45/file51, have the same sign. Six official local errata layers and
three TeX sources contain no corresponding correction. Alon's primary
Combinatorial Nullstellensatz,Theorem6.1,p10, prints the correct |E|+1.
No physical copy or root-agent acceptance is claimed.

Full argument and all boundaries:
`notes/sequential-mpr-ex116.md`.
Source/errata record:
`results/sequential/mpr-116-divisible-subgraph-errata.json` and
`sources/mpr116-references.json`.
