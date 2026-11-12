# F165 — The sum in MPR67(c) counts one extra trial

The question on p.18/file38 defines Z_n as the net profit after n
trials. The answer on p.380/file400 takes independent uniform bits
T_j and writes

    Y_j=(-1)^T_j * 2^j * T_0 ... T_(j-1),
    Z_n=Y_0+...+Y_n.

The empty product at j=0 is1. Therefore Y_0 is the outcome of the
first one-dollar bet, Y_1 is the second two-dollar bet if the first
lost, and so on. The printed sum counts n+1 trials.

## A positive-probability witness

On T_0=T_1=1, an event of probability1/4, Y_0=-1 and Y_1=-2.
For n=1 the printed formula gives Z_1=-3, although the profit after
one losing trial is-1. This discrepancy does not rely on including
time0 in the question.

The entire one-trial distribution is P(+1)=P(-1)=1/2. In contrast,
the printed Y_0+Y_1 has P(+1)=3/4 and P(-3)=1/4. At time0 there
is also a mismatch: the actual profit is0 but Y_0 is a fair sign.

With the Y_j definition unchanged, the correction is

    Z_n=sum from j=0 to n-1 of Y_j, with Z_0=0.

After n trials this is1 if a win has occurred, and1-2^n otherwise.
These are exactly the outcomes of the stated strategy.

## Limited impact and contextual assessment

The printed sequence is a one-step shift of the intended sequence;
it is also a martingale. The exercise’s martingale assertion is true,
and both the conditional-expectation proof and all other parts of
67 are supplied in notes/sequential-mpr-ex067-068.md. Severity is low.

Reindexing explains the typo but does not make the displayed equality
true for the random variable explicitly defined in the question.
The next exercise68 uses its one-based increments and the sum from1
to n consistently; it does not redefine the trial count in67(c).

## Source and errata checks, 7 November2026

Both the original book and the author’s Pre-Fascicle5A have the same
question wording and the same sum through Y_n. The full pages were
viewed in images/sequential/file-038.png, ref-400.png,
fasc5a-24.png and fasc5a-43.png.

The hashed manifest results/sequential/mpr-067-068-gambling-errata.json
covers all six saved errata layers and three TeX sources; no applicable
67(c) correction was found. Only p.380/file400 is marked, where the
incorrect identification occurs. The valid question on p.18 is not
an error location. The local snapshot does not establish a live
refresh, physical printing, priority or independent coordinator
approval. No numerical run or census restart was made.
