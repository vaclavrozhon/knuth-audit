# F158 — a nonconstant martingale need not work with constant information

Status: confirmed mathematical discrepancy, local to the parenthetical
assertion in answer MPR77, Volume4B, printed p.382, file page402.
The main assertion of exercise77 and its preceding proof remain valid.

The answer says that a martingale is also a martingale with respect to,
for example, a constant sequence. Definition(28) on printed p.6 requires
both adaptedness — Zn must be a function of X0,…,Xn — and
E(Zn+1|X0,…,Xn)=Zn. The parenthetical assertion is false under either
natural interpretation of a constant sequence.

Use two atoms with probability1/2 each. Let ξ take values−1 and1, and set

```
Z0 = 0,
Zn = ξ for every n≥1.
```

This is an integrable martingale with respect to its own history:
E(Z1|Z0)=Eξ=0=Z0; for n≥1 the history already gives ξ, so
E(Zn+1|Z0,…,Zn)=ξ=Zn. It is bounded and neither atom is null.

If the auxiliary sequence is deterministic, say Xn=0 for every n,
Z1 is not a function of its history. Also
E(Z2|X0,X1)=Eξ=0, whereas Z1 takes values±1.

Even if “constant sequence” means Xn=Y for a fixed *random* variable Y,
the claim cannot hold for this martingale. Adaptedness at time1 would
make ξ a function of Y. Then E(Z1|X0)=E(ξ|Y)=ξ, contradicting the
required value Z0=0. Thus replacing “deterministic” by “constant in
time” does not rescue the printed assertion. This stronger witness
avoids the ambiguity of a martingale that itself is constant in time.

The precise general fact is that an adapted martingale for an unchanged
information set must be constant in time: Zn+1 is already measurable
with respect to that information, so its conditional expectation is
Zn+1, and the martingale equality forces Zn+1=Zn. It may still be
random if the unchanged information contains its initial value.

Deleting the parenthetical example, or replacing it by the actual
auxiliary sequence (Zn) itself, repairs this local error. It remains
correct that an arbitrary auxiliary sequence need not preserve the
martingale property. The proof immediately preceding the parenthesis
correctly passes from a finer adapted history to the martingale's own
history using the tower property.

Original source checks on 6 November2026:

- The 4B original page382 was visually inspected, including the full
  parenthesis. Definition(28) on original p.6 was also inspected.
- The author's Pre-Fascicle5A, printed p.38, file page44, has the same
  assertion. Its page is dated11 September2019.
- All six local public errata layers err4b/all4b, err4f5/all4f5 and
  err4f6/all4f6 were searched by page, exercise and wording. The
  historical Fascicle5 corrections on pp.193–194 concern answers72
  and83, and do not correct answer77. The current4B list has no
  correction to p.381 or382. Exact hashes and matches are archived.

Evidence relative to the repository root:

- `audit-2026-10-31/images/sequential/file-026.png`
- `audit-2026-10-31/images/sequential/ref-402.png`
- `audit-2026-10-31/images/sequential/fasc5a-44.png`
- `audit-2026-10-31/sources/fasc5a-manifest.json`
- `audit-2026-10-31/results/sequential/mpr-077-084-witnesses.json`
- `audit-2026-10-31/results/sequential/mpr-077-084-errata.json`

This establishes the mathematical discrepancy in the checked digital
typesetting. A physical printing and priority of the report were not
verified. No report was sent.
