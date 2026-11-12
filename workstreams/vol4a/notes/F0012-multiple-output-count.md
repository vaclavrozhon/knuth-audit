# V4A-F0012: the multiple-output counting bound is too small

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), answer 7.1.2-47, printed page 570 / file page 587.
Original: `images/bookwise-p570.png`.

Let c(m,n,r) count the ordered m-output Boolean functions of n input
bits that can be computed jointly in at most r binary Boolean steps.
The proposed extension of Theorem S states

    (r-m)! c(m,n,r) <= 2^(2r+1) (n+r-1)^(2r).

This inequality fails for n=256 and m=r=4. Each pair of distinct input
variables supports ten Boolean functions that depend on both variables:
of the sixteen binary truth tables, six are constant or depend on just
one argument. Functions supported on different pairs are distinct.
Consequently A = 10 binom(256,2) = 326400 distinct scalar functions
can each be computed in one step. Every ordered four-tuple of these
functions can be computed in at most four steps.

Even if the four component functions must be distinct, this gives

    c(4,256,4) >= A(A-1)(A-2)(A-3)
               = 11349915205231040601600,

whereas the asserted upper bound is

    2^9 * 259^8 = 10367357475042936177152.

The left factorial is 0! = 1. Thus the finite counting inequality is
false even with four nontrivial, distinct output functions. One exact
integer calculation checks these numbers; no circuits were enumerated.
See `results/bookwise-multi-output-bound.json`.

The proof retains the factor 2 used to undo normalization of one output
in Theorem S, although m outputs can be complemented independently.
The stated leading asymptotic lower bound is not disproved by this
counterexample. A corrected counting proof must also specify how it
handles trivial outputs, repeated outputs, and unused gates; this note
does not assert that changing one factor alone proves every case.

The current and historical Volume 4A errata and both Fascicle 0 layers
contain no matching correction. Targeted public searches located no
matching report; absolute novelty is not established. See
`sources/multiple-output-source-check.json`.
