# Reused finding F007: mixture weights in MPR123

The original finding is retained under its original ID. In the model,
A selects Y and has prior probability a. Therefore

    Pr(Z=t)=a y(t)+(1-a)x(t).

The printed mixture uses a x(t)+(1-a)y(t). The old exact counterexample
uses x=(3/4,1/4), y=(1/4,3/4), a=1/4: the correct mixture is (5/8,3/8),
whereas the printed expression gives (3/8,5/8). All probabilities are
strictly positive.

Original second-printing PDF p25/file45 and September11,2019 author
PostScript p25/file31 agree. The 2026-11-07 complete review of exercise123
checks all six local official errata layers and three available TeX
sources; none contains this repair. The nearby p25 erratum concerns124.

The complete Bayes and expected-log-odds argument, including zero
likelihoods, nondegenerate priors and infinite divergence, is in
notes/sequential-mpr-ex123.md. The answer's Bayes formula is valid when
z_k denotes the corrected mixture. Thus only the statement on p25 is an
error location; p390 is not an additional F007 location.

Publisher-deposited Crossref metadata confirm the cited1951 article.
The historical claim about the authors' original motivation is an
explicit bibliography exception because the original full text was not
quickly available. No calculation was repeated. This does not claim a
physical printed-copy inspection, historical priority or a reward.

