# F163 — an undefined extra variable in the final conditioning list

Confirmed local index typo, low severity, in Volume4B, answerMPR38,
printed p.376 (file396). The question and the derived numerical
formula are correct.

The question defines a restricted growth string X₁…Xₙ and asks for
E(Xₖ|X₁,…,Xₖ₋₁). The answer defines M from precisely this prefix,
counts its possible extensions, but starts the conditioning list
in its final expectation with X₀. This variable is not defined.
The cited definition in Volume4A, 7.2.1.5–(4), also starts at index1.
The correction is to start the final conditioning list at X₁.

An arbitrary additional variable cannot safely be inserted there.
For n=2, the two restricted growth strings are00 and01, each with
probability1/2. At k=2, M=1 and the printed right side equals

    (binom(1,2)t₁,₀+1·t₂,₀)/t₁,₁=(0+1)/2=1/2.

The requested E(X₂|X₁) is indeed1/2. If one supplied X₀=X₂, however,
then E(X₂|X₀,X₁)=X₂, which differs from1/2 at both positive atoms.
A specially chosen constant X₀ would be harmless, but no such
variable is specified. This is an index correction, not a failure
of the conditional counting formula.

The full proof of that formula is in the accompanying Czech audit:
an old-block choice has t_M,n−k extensions, a new-block choice
t_M+1,n−k extensions, and their sum is t_M,n+1−k. Every endpoint,
the Bell-number convolution and the generating function are proved.

Source checks, 7 November2026:

- The original question p.15/file35 and answer p.376/file396 were
  viewed in full. The extra index0 is present in the answer.
- The author's Pre-Fascicle5A, p.33/file39, has the same index.
- The original Volume4A p.416 explicitly defines a₁…aₙ, a₁=0.
- All six saved errata layers and three raw TeX sources were checked
  by page, exercise number and content. No applicable correction was
  found. Other answers37/38 in the errata concern other sections.
- The all4b snapshot is dated16April2026. A live refresh, physical
  printing, priority and independent coordinator review are not claimed.

Evidence relative to repository root:

- `audit-2026-10-31/notes/sequential-mpr-ex037-038.md`
- `audit-2026-10-31/results/sequential/mpr-037-038-prefix-claim-map.json`
- `audit-2026-10-31/results/sequential/mpr-037-038-prefix-errata.json`
- `audit-2026-10-31/images/sequential/file-035.png`
- `audit-2026-10-31/images/sequential/ref-396.png`
- `audit-2026-10-31/images/sequential/fasc5a-39.png`
- `audit-2026-10-31/images/vol4a-p416-for-dlx123.png`

Only file396 is a finding location. No numerical computation or
external report was made.
