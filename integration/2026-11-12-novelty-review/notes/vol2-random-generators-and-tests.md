# Publication review: Volume 2, C0002–C0015

Reviewed on November 12, 2026. Each argument and its original typeset book
page or erratum was inspected individually. The current and historical
`all2-prepre`, `all2-pre`, `all2`, `err2`, and `err2.textxt` layers were
compared with the relevant pages and exercises. Their refreshed copies
match the archived sources. Existing reproducible calculations were reused
where the explicit counterexample already settles the issue.

All fourteen findings below remain supported. Searches found no matching
prior report of the particular TAOCP defect; this does not establish
priority. Known source results and partial earlier corrections are described
explicitly below rather than being claimed as new mathematics.

| Card | Independent assessment |
| --- | --- |
| V2-C0002 | The cycle detector on p. 540 allows parameters `m=2, g=3`. Even with the natural repair that its scale `b` is at least 1, no search occurs after initialization, so a constant sequence is missed. With `m=g=2`, a three-cycle is also missed. The Sedgewick–Szymanski–Yao paper requires `g<m` and starts with scale 1. Its online lower-bound qualification is itself not fully explicit; the report concerns the book's stated algorithm and bound, not a new cycle-detection principle. |
| V2-C0003 | The added 2005 answer on p. 542 gives probability `Theta(m^(k/2))`. For fixed positive `k` it grows beyond 1. Pemantle's cited preprint gives the negative exponent. This is an erratum typo, absent from the original 1997 page; severity reduced to medium. |
| V2-C0004 | On p. 543 the second inverse-generator formula needs a suitably lifted modular inverse. With modulus 8, multiplier 3, increment 1 and the permitted inverse 3, it returns 4 instead of the previous state 0 from state 1. The division is exact in this example. The issue is the missing condition on the chosen inverse, not impossibility of choosing a suitable inverse. The 2003 addition does not supply it. |
| V2-C0005 | The periodic extension on p. 546 changes only negative indices, while keeping the initial borrow. Input digit `x_-10=2`, all other initial digits zero, and borrow `b_0=1` gives `x_0=1`; the proposed periodic past instead requires `x_0=0`. The final radix identity remains valid. This is a proof-step defect; severity reduced to medium. |
| V2-C0006 | The 2016 replacement of an approximate equality by equality on p. 551 needs an outer floor. For the actual generator, indices 75–77 give the three quantized outputs `(6,16,3)`. The proposed exact relation forces an error term congruent to 11 modulo 20 although it lies strictly between -9 and 6. The issue survives the intended reading of the output index. |
| V2-C0007 | In answer 15 on p. 554, the additional gap-sequence bound fails for modulus 16, multiplier 5, increment 1 and the binary choice sequence: the gaps have least period 8, exceeding `m/4=4`. The principal output-period conclusion remains correct. |
| V2-C0008 | The universal-generator construction added in 2019 includes the all-maximal digit stream. In base 2 its initial approximation error is exactly 1/2, not strictly smaller, and in base 10 the subsequent error is 9/10. Nakazawa's primary patent explicitly excludes boundary inputs. The unavailable old preprint was not treated as read. Retain as a low-severity missing boundary exclusion. |
| V2-C0009 | The search in exercise 11(c), p. 37, need not terminate: the recurrence polynomial `1-z+z^2` has period 6 modulo every `2^e` for `e>=2`. This example also invalidates the discrepancy conclusion in exercise 26 under its stated hypotheses. Brent already describes the period phenomenon, so the report claims only these consequences for the book's exercise and bound. Brent's page 4 does not report either TAOCP defect. |
| V2-C0010 | The conjecture attributed to Reiser on p. 39 omits the primitive-polynomial hypothesis present in Reiser's paper. The fixed recurrence `X_n=4 X_(n-3)` with seed `(0,0,1)`, modulo `3^alpha`, has period `3^alpha` and `2*3^(alpha-1)` zeros. This defeats the printed square-root bound. Restoring primitivity excludes this example; no open conjecture is being solved. |
| V2-C0011 | The 2013 feedback mask `0x243F6A8885A308D3` has 27 set bits, so its degree-64 polynomial is divisible by `x+1`. The nonzero state `0xE3EAD987836107B1` is fixed by the printed shift/XOR operation, contradicting the required maximal period. Search results using the same hexadecimal digits as cryptographic constants do not report this feedback-generator defect. |
| V2-C0012 | The 2001 replacement on p. 556 uses the sum of the two component symbols modulo their product. For alphabet sizes 2 and 3 this produces `(0,2,2,1,1,3)`, missing symbols 4 and 5 and failing even the order-one recurrence requirement. A weighted encoding is needed. The unweighted sum was introduced by the erratum. |
| V2-C0013 | In answer 36 on p. 558, with `a=1, c=2, n=1`, the claimed factorization has left side 4 and right side 8. The second factor needs `q_(n-1)` in place of `q_(n+1)`, with the corresponding follow-through in the next sentence. The period conclusion survives this repair. |
| V2-C0014 | The 2005 correction changes the pole factor on p. 558 to `x+u`, but p. 559 still substitutes `x=u` instead of `x=-u`. The full-cycle example `F(x)=1+1/x` modulo 7 has its second-iterate pole at 6, not 1. Retain only the missed dependent substitution, explicitly acknowledging that the initial sign error was already corrected. |
| V2-C0015 | Answer 5 on p. 559 gives an 86-percent Kolmogorov–Smirnov level. From the printed data the relevant statistic is `D-=0.048`, with exact lower-tail probability `0.048*1.048^19 = 0.1169783813`. The opposite tail is about 88 percent, so neither convention gives 86. The acceptance decision is unaffected; low severity. |

Primary references checked in the existing evidence and during this review:
[cycle detection](https://sedgewick.io/wp-content/themes/sedgewick/papers/1982Cycles.pdf),
[Pemantle's preprint](https://arxiv.org/abs/math/0404103),
[Nakazawa's patent](https://patents.google.com/patent/US20100030829A1/en),
[Brent's paper](https://maths-people.anu.edu.au/~brent/pd/rpb133.pdf), and
[Reiser's report](https://ftpmirror.your.org/pub/misc/bitsavers/pdf/stanford/Stanford_CS_TR_Collection_2025-12-12/PDF/1977/CS-TR-77-601.pdf).
The full arguments, exact input data and original-page references remain in
the individual `workstreams/vol2/notes/C0002` through `C0015` notes.

Public searches used distinctive constants, formulas, exercise locations
and named algorithms. Query families included `TAOCP 543 inverse`,
`Knuth subtract borrow periodic extension initial error`, `Knuth random
mapping Pemantle exponent errata`, `Knuth shuffle return gap period k=2
error`, `243F6A8885A308D3 primitive`, `Knuth Nakazawa universal generator
error`, `Knuth inversive generator pole sign errata`, `Knuth Reiser
conjecture missing primitive`, `Knuth Sedgewick Szymanski Yao 540 error`,
`Knuth 551 floor errata random`, `Knuth 3.2.2 period error`, `Knuth complete
sequence errata sum`, and `Knuth Kolmogorov 86 559`. A GSL discussion
concerns a different implementation modulus, and generic discussions of
the underlying mathematics do not establish prior reports of these book
errors. No assertion of absolute novelty is made.
