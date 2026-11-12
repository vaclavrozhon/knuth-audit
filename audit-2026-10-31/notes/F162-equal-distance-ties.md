# F162 — equal distances are not the same as equal values

Confirmed local proof discrepancy, low severity, in Volume 4B,
answer MPR11, printed p.372 (file392). The exercise's conclusion
remains true for every stated discrete distribution.

The answer uses the identity

    P(|X₂−α|≤|X₁−α|)=(1+P(X₁=X₂))/2

for independent, identically distributed X₁,X₂. Exchangeability
instead gives the exact identity

    P(|X₂−α|≤|X₁−α|)
      =(1+P(|X₁−α|=|X₂−α|))/2.

Distinct points on opposite sides of α can have equal distances.

For an exact finite witness, take α=0 and let X₁,X₂ be independent
fair signs. The four pairs (−1,−1), (−1,+1), (+1,−1), (+1,+1)
each have probability 1/4. Both absolute values always equal 1,
so the left side of the printed identity is 1. Equality X₁=X₂
has probability 1/2, so its printed right side is 3/4.

The smallest repair is to change this one equality sign to ≥.
Equality of the variables implies equality of their distances;
therefore

    P(|X₂−α|≤|X₁−α|)≥(1+P(X₁=X₂))/2>1/2.

For a discrete law with atom masses p_x, independence gives
P(X₁=X₂)=Σ p_x²>0. At least one atom has positive mass, including
for a countably infinite law. No finite mean or variance is needed.
Alternatively, retain equality and replace the tie event by the
correct equality of distances.

Every other proof step is valid. The triangle inequality makes
{|X₂−α|≤|X₁−α|} a subset of
{|X₁+X₂−2α|≤2|X₁−α|}. For general n, the averages of the first
and last n variables are independent and identically distributed
discrete variables; their average is the average of all 2n values.
Applying the corrected two-variable argument proves the original
strict probability bound. In the witness, the original event has
probability 1, so the exercise itself is not contradicted.

Source checks, 6 November 2026:

- The whole original question p.13 and answer p.372 were viewed.
  The erroneous tie expression and equality are present in the PDF.
- The same expression appears in the author's Pre-Fascicle 5A,
  printed p.29, file35, also viewed together with its full context.
- All six local errata layers and three raw TeX sources were searched
  by both locations and content. No applicable correction was found.
  The answer11 change on Fascicle6 p.186 concerns SAT triples;
  it is unrelated. The saved all4b snapshot is dated 16 April 2026.
- The historical attribution to T. M. Cover is explicitly unverified;
  no mathematical assertion here depends on that attribution.
- This checkpoint has been sent to the coordinator; no independent
  coordinator review of F162 is claimed yet.

Evidence, relative to repository root:

- `audit-2026-10-31/notes/sequential-mpr-ex011.md`
- `audit-2026-10-31/results/sequential/mpr-011-mean-witness.json`
- `audit-2026-10-31/results/sequential/mpr-011-mean-errata.json`
- `audit-2026-10-31/images/sequential/file-033.png`
- `audit-2026-10-31/images/sequential/file-392.png`
- `audit-2026-10-31/images/sequential/fasc5a-19.png`
- `audit-2026-10-31/images/sequential/fasc5a-35.png`

A physical printing, live errata refresh and report priority were not
verified. No report was sent. Only file392 is the finding location;
the valid exercise statement on file33 is not marked.
