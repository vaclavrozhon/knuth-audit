# C046 — The one-coordinate boundary of MPR answer8

Status: candidate, pending contextual interpretation. This is not a confirmed
erratum. Original question: Volume4B p13/file33. Original answer: p372/file392.
Both were directly viewed, as were the author's Pre-Fascicle5A pp13 and29
(files19 and35).

The question assigns each binary vector x the probability
`(2+(-1)^popcount(x))/2^(n+1)`. For every n≥2, each proper marginal is
uniform, while the full joint distribution differs from the product of its
fair one-bit marginals. The answer's conclusion is correct in that range.
The full proof, including all patterns and normalization, is in
`sequential-mpr-ex008-009.md`.

For n=1 the given probabilities are P(X1=0)=3/4 and P(X1=1)=1/4.
This is a valid probability distribution. A family consisting of one random
variable is independent: its joint probability is its own single marginal.
Thus the answer's final claim of non-n-wise independence does not cover this
boundary literally.

The unresolved issue is scope, not the calculation. Question8 does not
explicitly say n≥2, but earlier exercise6 does, and the whole block concerns
nontrivial higher-order independence. If that dimension restriction is
understood to carry over, this is a context note and should be dismissed.
Otherwise add n≥2 or state the n=1 exception. Do not classify this as a
confirmed error merely because the isolated boundary exists.

All six local errata layers and their three available TeX sources were
reassessed for the exact pages; no applicable change was found. This does
not establish priority or a discrepancy in a physical printed copy. Only the
answer location is proposed for the candidate map; the valid theorem for n≥2
is not itself a finding.
