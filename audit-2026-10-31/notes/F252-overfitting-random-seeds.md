# F252 — Fresh solver seeds do not provide fresh problem instances

Confirmed as a flaw in the justification in Volume 4B, answer 509,
printed 650/file 670; author draft 286. The exercise asks why using some
of the same benchmark problems for tuning and evaluation did not lead
to overfitting. The answer substitutes the randomness of solver seeds for
randomness in the selection of training examples. These are different
sources of variation: fresh seeds can check performance on fresh runs of
the same formulas while leaving specialization to those formulas intact.

For a concrete countermodel, let U be a fresh fair bit on each run. Let
configuration A cost 1+U on training instances and 100+U on new instances;
let configuration B cost 2+U on both. Even infinitely many fresh seeds
select A on the training set, although B performs much better on new
instances. Averaging out seed noise cannot repair this instance mismatch.

The cited ParamILS paper makes this distinction explicitly: its definitions
of training and test performance separate both instances and seeds, and
its experimental setup reserves half the instances for evaluation.
See Hutter et al., JAIR 36 (2009), p. 272, Definitions 3–4, and Section 5.1.2:
[official project PDF](https://www.cs.ubc.ca/labs/algorithms/Projects/ParamILS/papers/09-JAIR-ParamILS.pdf).

A corrected answer should say that fresh seeds mitigate overfitting to
particular random runs, while generalization to different formulas must
be assessed on held-out instances. Main pages 309–310 do discuss additional
instances, but several training/selection instances also appear in the
100-case comparison. This finding does not demonstrate that the reported
parameters actually overfit, or invalidate their measured performance;
it invalidates the stated reason for ruling that risk out.

Original Volume 4B typesetting and the corresponding September 23, 2015
author draft were inspected. Relevant current/historical 4B and Fascicle 6
errata contain no matching correction. Focused public searches found no
matching report, without establishing absolute priority. Details are in
sources/bookwise-closest-tuning-source-check.json.
