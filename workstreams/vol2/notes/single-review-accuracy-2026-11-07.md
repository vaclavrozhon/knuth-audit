# §4.2.2 — printed-argument review completed

7 November 2026, single reviewer. Scope: printed 229–245, exercises 1–31
plus added 32, and their answers 613–617. The registered recovery already
covers the complete exposition and the difficult earlier answers. Its
sound results are reused, without rebuilding proofs or rerunning tests.

The previously unfinished queue was compared with the question/answer text:
19 (compensated summation), 21–23 (exact product, drift and fractional part),
26–31 (positive sums, reciprocal stability, inverse functions, calculators,
Pell examples) and the existing added-32 evidence. Original answer images
616–617 were inspected, including the nested parentheses and rounding signs
lost in OCR. The 1998 correction to the parentheses in 27 and the 1999
exponent-index correction in 21 are known changes, not new findings.

The printed steps agree with the retained analysis: product splitting gives
an exact residual under the assumed exponent range; multiplication/division
stabilizes after the possible initial changes (the printed 19,55 example
has 19,1000,18,990,18,...); the modulo exception depends on the prescribed
halfway rounding; the positive-sum estimate excludes cancellation. The
reciprocal argument uses monotone rounding and consistent ties. The Pell
identity in 31 explains the exact result 1 despite catastrophic floating
cancellation. No new error was found in these steps.

For 19, retain C0086: the stated second-order term count is wrong, while
the advertised first-order error bound survives. `accuracy-compensation.md`
and `C0086-kahan-quadratic-count.md` supply the accepted argument; the newer
unregistered recovery draft is additional evidence, not a requirement to
recreate its expansion. Existing C0083–C0090 dispositions are unchanged.

Explicit limits: no overflow/underflow of intermediate values in the exact
transforms; historical source/priority gaps from `accuracy-context.md`;
C0088's leading-zero convention in unnormalized division remains an
interpretive observation; no reproduction of old calculator hardware or
historical performance percentages; no fresh proof of the cited external
inverse-function theorem in 28. Existing `accuracy-diamond.md` is retained
within its original scope. The experiment in 30 is read, not performed on
an unspecified historical calculator.

Whole-page certification: file 241–257 (printed 229–245) and 625–628
(printed 613–616, including the already checked preceding answer on 613).
The §4.2.2 part of 617 is checked, but no new whole-page certification is
issued for that shared page because it also contains §4.2.3.
Other first-pass pages remain gray unless separately supported.

Evidence: `first-pass-accuracy-2026-11-06.md`, registered recovery notes
through X0227, `accuracy-product-mod.md`, `accuracy-iterations.md`,
`accuracy-compensation.md`, `accuracy-diamond.md`, `intervals.md`,
`accuracy-basic.md`, and the four recorded errata layers all2-prepre,
all2-pre, all2, err2. No new finding and no mathematical execution.
