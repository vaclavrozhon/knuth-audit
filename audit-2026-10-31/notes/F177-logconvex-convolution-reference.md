# F177 — the convolution proof points to the wrong preceding part

**Minor proof cross-reference.** Volume4B, first edition, second printing
(2022), answer MPR125(e), printed391/file411. The original page visibly
says “apply (c)”. It should refer to **(d)**, closure of log-convex sequences
under addition. The convolution theorem itself remains valid.

The printed Pascal decomposition writes c_n as the sum of two binomial
convolutions of left-shifted input sequences. The induction hypothesis
supplies log-convexity of each of these two sequences. The step that
combines them is precisely part(d), which proves that the sum of two
log-convex sequences is log-convex. Part(c) instead gives a separated-index
inequality for one log-concave sequence (with an analogous convex variant
mentioned in its answer); it is not the stated sum-closure result.

This is a one-letter internal-reference correction, not a counterexample
to preservation of log-convexity, and not a request for a replacement proof.
The old paused note identified the reference for investigation; this review
resolves it by matching the actual induction step to the neighboring parts.

Original evidence: `images/sequential/ref-045.png` (statement) and
`images/sequential/ref-411.png` (answer). Six historical/current errata
layers all4b, err4b, all4f5, err4f5, all4f6, err4f6 and their three TeX
versions were searched by pages,125,log-convexity,Davenport and Pólya.
No corresponding correction was found. On7November2026 all nine official
files were fetched and their hashes matched the retained sources exactly.
See `sources/mpr125-errata-refresh-2026-11-07.json` for URLs and hashes.
[Official TAOCP source index](https://www-cs-faculty.stanford.edu/~knuth/taocp.html),
[current4B errata](https://www-cs-faculty.stanford.edu/~knuth/err4b.textxt).
Five targeted public searches found no matching report. That does not
establish absolute priority or author acceptance. No correspondence sent.
