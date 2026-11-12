# The extremal function in answer 82(c) is wrong for even n

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–82(c), printed 801.

Write nu(sigma) for the number of 1 bits, M_n=binom(n,floor(n/2)), and E(f) for the evaluations made by Algorithm H. Exercise 82(c) asks to maximize sum_sigma f(sigma), subject to E(f)=M_(n+1). The answer identifies (45), namely f(sigma)=[nu(sigma)>n/2].

For n=2 the pattern consists of the row `10` followed by `00 01 11`. The proposed function is AND, with only one value equal to 1. For OR, Algorithm H first queries `10`, obtaining 1. In the second row, H3 uses this known relative-complement value to set a=0,z=1; H4 then queries `00` and `01`, obtaining 0 and 1. Thus E(OR)=3=M_3, but sum OR=3>1=sum AND. AND also uses three evaluations, at `10`, `01`, and `11`.

The corrected maximizing function is [nu(sigma)>=n/2], equivalently [nu(sigma)>=ceil(n/2)]. This agrees with (45) for odd n. To see the upper bound, induct through the rows: if all earlier rows are zero below ceil(n/2), H3 cannot reduce z below ceil(n/2), since every tested relative complement of smaller weight is zero. In a row of size greater than one, reaching two evaluations therefore forces the first queried value at weight at least ceil(n/2)-1 to be zero. Thus the whole row is zero below ceil(n/2). Singleton rows, when present, are at weight n/2 and impose no contrary condition. The corrected threshold attains this pointwise upper bound and makes H4 query twice in every nonsingleton row.

Equation (45) still witnesses the main text's worst-case lower bound. Only its use as the maximizer in answer 82(c) fails.

Original typesetting inspected. No matching repair was found in the historical/current Volume 4A errata, refreshed Fascicle 4 errata or targeted public searches; see `../sources/tree-subset-chains-source-check.json`. Absolute novelty is not established.
