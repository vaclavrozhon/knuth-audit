# The restricted-growth maximum is off by one

Volume 4A, first edition, first printing (2011), Answer 7.2.1.5–38(b), first sentence,
printed page 771, file page 788.

Part (b) asks for sigma-cycles whose entries k_i are at most m. Under the correspondence in part (a), these are restricted growth strings using at most m distinct digits, hence with maximum digit **less than m**. The answer instead prints a maximum at most m.

For n=3,m=2, the printed condition includes the string 012. Its corresponding cycle is 333, since sigma_3^3 is the identity, but its entries exceed 2. The allowable cycles are 111,122,212,221, giving four cases. This agrees with the answer's final sum of Stirling numbers through m blocks, which is already correct; only the preceding digit-bound statement needs changing.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-counting-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
