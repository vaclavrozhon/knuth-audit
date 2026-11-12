# F167 — The last stated Ace Now transition requires an undefined ratio

Status: confirmed in the saved sources. Severity: low.
Location: Volume4B, Mathematical Preliminaries Redux, exercise82(a),
printed p.19, file page39. Only this question location is mapped.

The question defines

    Z_n=(4−X₁−⋯−X_n)/(52−n)

and asks that it satisfy(28) for0≤n<52. Equation(28), printedp.6,
is E(Z_{n+1}|X₀,…,X_n)=Z_n. Thus the stated range includes the
transition n=51 and requires Z₅₂. Every complete deck contains four
aces, so the displayed formula for Z₅₂ is identically0/0. It does
not define a real random variable on any outcome.

This is not an exceptional null event. Moreover, simply setting
0/0=0 would not repair the claimed equation. After51 cards, Z₅₁
is the indicator that the sole remaining card is an ace. It equals1
with probability4/52=1/13. An identically zero Z₅₂ would have
conditional expectation0 on that positive-probability event,
contrary to Z₅₁=1.

The ratio is defined for0≤n≤51. Its valid transitions are0≤n≤50:
if A aces remain among C≥2 cards, then

    (A/C)(A−1)/(C−1)+(1−A/C)A/(C−1)=A/C.

Thus replace the transition range0≤n<52 by0≤n<51.
Alternatively explicitly extend the sequence by Z_n=Z₅₁ for
n≥51. This extension preserves the finite martingale and makes
the endpoint equation valid; it is not an evaluation of the
displayed0/0 ratio.

The game always stops before drawing the last card, so its stopping
index is at most51. Both remaining exercise conclusions are valid:
E Z_N=1/13 and the expected net profit is0. The full finite proof,
the generalized urn addition and all feasibility conditions are
in sequential-mpr-ex082.md; no computation is needed.

Evidence: the original4B PDF question, equation(28), game rules
and answer were directly viewed, as were the author's
11September2019 Pre-Fascicle5A questionp.19/file25 and
answerp.39/file45. The same endpoint is present in the author source.
The six saved errata layers err4b/all4b, err4f5/all4f5,
err4f6/all4f6 and three corresponding TeX sources were checked;
no applicable correction was found. The audit manifest is
results/sequential/mpr-080-082-martingales-errata.json.
The saved all4b snapshot is dated16April2026; no live refresh,
physical-copy check, priority claim or independent coordinator
acceptance is asserted.

The answer's current-state expectation notation is explicitly
interpreted conditionally in the full analysis. It is not counted
as a separate finding. The valid main-text game and answer are
not assigned this question's error location.

