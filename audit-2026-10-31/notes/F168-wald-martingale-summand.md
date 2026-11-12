# F168 — The preliminary Wald martingale repeats the last summand

Status: confirmed in the saved sources. Severity: low.
Location: Volume4B, Mathematical Preliminaries Redux, first line
of answer83, printedp.382, file page402.

The printed definition is

    Z_n=Σ_{k=1}^n(X_n−E X_n).

Both random-variable subscripts in the summand are n, although
the bound summation index is k. The expression consequently
equals n(X_n−E X_n), and generally is not a martingale.

A complete two-outcome counterexample satisfies all exercise
hypotheses. Let X₁ be0 or1 with equal probability, and let
X₀=X₂=X₃=…=0. These variables are mutually independent,
nonnegative and bounded. The printed sequence has

    Z₀=0, Z₁=X₁−1/2, Z₂=0.

Hence E(Z₂|Z₀,Z₁)=0, whereas Z₁ is either−1/2 or1/2.
The martingale condition fails on both outcomes. It also fails
relative to the full X history, so this is not a filtration
interpretation issue.

Replace both subscripts n inside the summand by k:

    M_n=Σ_{k=1}^n(X_k−E X_k).

Each new increment has conditional mean0 by independence,
and the finite sum is integrable when its constituent
expectations are finite. This proves the repaired martingale.
The independent direct proof of Wald's identity printed below
it remains valid. A full derivation of both proof routes,
every infinite-sum step, stopping-rule endpoint and degenerate
case is in sequential-mpr-ex083.md. No calculation was run.

The original4B page and the author's11September2019
Pre-Fascicle5A answerp.39/file45 were directly viewed;
both contain the same first-line indices. The original
questionp.20/file40 is correct and is not mapped as an error.

All six saved errata layers (err4b/all4b, err4f5/all4f5,
err4f6/all4f6) and three corresponding TeX sources were
contextually checked in mpr-083-wald-errata.json.
The known16August2020 correction to historicalp.194
changes the next stopping-rule description and S_n to S_N.
Those two corrections are already incorporated in4B;
they do not change the first-line summand. They are retained
only as known erratum E127, without a finding card or map color.

No applicable correction to these summand indices was found.
The saved all4b snapshot is dated16April2026. No live refresh,
physical-copy inspection, priority claim or independent
coordinator acceptance is asserted.

