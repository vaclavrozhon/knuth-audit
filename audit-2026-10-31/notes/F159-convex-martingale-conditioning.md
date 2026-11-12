# F159 — a proof identifies two different conditional expectations

Status: confirmed mathematical discrepancy in answer MPR84(a),
Volume4B, printed p.382, file page402. The requested theorem that a
convex function of a martingale is a submartingale remains true.

After applying conditional Jensen, the answer identifies

```
E(f(Zn+1) | Z0,…,Zn)
```

with

```
E(f(Zn+1) | f(Z0),…,f(Zn)).
```

These random variables need not be equal: applying f can erase
information about the next conditional distribution. The reference
to answer77 justifies *conditioning again*, not deleting information
from an existing conditional expectation without that extra step.

Here is a finite, bounded martingale with no null atoms:

| atom probability | Z0 | Z1 | Zn for n≥1 |
|---:|---:|---:|---:|
|1/2|−1|−1|−1|
|1/4|1|0|0|
|1/4|1|2|2|

Given Z0=−1, the next value is−1. Given Z0=1, the next values0 and2
are equally likely, with mean1. Thus E(Z1|Z0)=Z0. After time1 the
process is fixed, so all later martingale identities also hold.

Take the convex function f(z)=z² on the interval[−1,2]. At n=0,

```
E(Z1² | Z0) = 1 when Z0=−1, and 2 when Z0=1.
```

But f(Z0)=1 on all three atoms, and hence

```
E(Z1² | f(Z0)) = E(Z1²) = (1/2)·1+(1/4)·0+(1/4)·4 = 3/2.
```

The printed identification is false on every atom. All expectations
exist and both values of Z0 have positive probability, so this is not
a question about versions on null sets, integrability or endpoints.

The proof is repaired by an extra conditional-expectation step. Write
Hn=(Z0,…,Zn) and Gn=(f(Z0),…,f(Zn)). Conditional Jensen gives

```
f(Zn) ≤ E(f(Zn+1) | Hn).
```

Now condition **both sides** on Gn. The left side is already a
function of Gn; because Gn is a function of Hn, the tower property
turns the right side into E(f(Zn+1)|Gn). This proves the desired
submartingale inequality. The example indeed has 1≤3/2, so it does
not disprove that theorem or the main-text statement on printed p.8.

Original source checks on 6 November2026:

- The original4B answer was visually inspected; the linking phrase
  explicitly identifies the latter expression, without an outer
  expectation.
- The same statement appears in the author's Pre-Fascicle5A,
  printed p.39, file page45, also visually inspected.
- The six local public errata layers and original TeX were checked.
  No matching correction to this step was found. Nearby historical
  corrections to answers72 and83 do not alter answer84(a).

Evidence relative to the repository root:

- `audit-2026-10-31/images/sequential/file-028.png`
- `audit-2026-10-31/images/sequential/ref-402.png`
- `audit-2026-10-31/images/sequential/fasc5a-45.png`
- `audit-2026-10-31/sources/fasc5a-manifest.json`
- `audit-2026-10-31/results/sequential/mpr-077-084-witnesses.json`
- `audit-2026-10-31/results/sequential/mpr-077-084-errata.json`

Only the displayed proof step is the finding location. The exercise
statement, the valid convex-transformation theorem, and the separate
Gilat bibliographic remark are not classified by this discrepancy.
A physical printing and priority of the report were not verified.
No report was sent.
