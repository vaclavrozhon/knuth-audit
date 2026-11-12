# Distribution generation and sampling: accepted completed work

10 November 2026. Volume 2, third edition, first printing. The six
`sequential-*-2026-11-06.md` reviews for distributions (AB, normal,
DE, discrete, logistic and Wallace), and the three sampling reviews
(core, riffles/ordered and additions), were read and accepted under the
current printed-argument policy. They pair all of section 3.4.1's
33 exercises and section 3.4.2's 19 exercises, including errata additions.
This is reuse of documented work, not a fresh rereading of the whole
original text or a repetition of the archived mathematical computations.

Accepted coverage: printed main pages 119–148 and answers 585–591.
Page 592 contains the start of section 3.5's answers and is not newly
certified by this note. The sampling answer 16 on page 592 was directly
reread to identify the exact outstanding numerical claim.

The arguments cover inverse transforms, rejection sampling, normal
mixtures and ratio methods, continuous and discrete distributions,
reservoir and skip sampling, permutations, and the two added sampling
exercises. The mathematical model uses independent uniform random
inputs and the stated arithmetic costs; it does not certify arbitrary
pseudorandom generators or machine rounding as exact real arithmetic.

Precise exceptions retained:

- Printed 132 and answer 21 on 588: the reported global optimum of the
  rejection area near parameter -0.35 is not independently established.
  The printed construction, requested interior-area optimum, and existing
  error C0054 are covered. A new global optimization proof is outside this
  pass, and the extra optimum is explicitly unverified.
- Answer 3.4.2–16 on 592: the claimed average total below 5n/2 probes
  is not independently established for the stated finite-population,
  monotone-hash model. Correctness and expected linear cost are covered
  by the existing argument; the sharper constant is an explicit exception.
- Printed 130: C0246 remains an interpretive caption question. The
  accompanying area argument is correct; no generator failure follows.
- Printed 119: the historical dismissal of alternative direct generators
  is not a universal current assertion. Historical comparisons on 134,
  the recommendation of parameter 7/8 on 137, and reported Wallace tests
  on 132 are not newly reproduced measurements.
- Research questions, unavailable original bibliography, personal
  priority claims, and external results retain the exact limitations
  listed in the accepted notes. The large archived experiments are reused.

All five official Volume 2 errata files were retrieved on 10 November
and match the archived originals byte for byte. Retrieval metadata is
in `integration/2026-11-10-bookwise/errata/manifest.json` from the project
root. Existing findings are retained; none is counted as a new finding
of this block.
