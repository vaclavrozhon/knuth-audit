# The probability coefficients count zeros, not the stated ones

Volume 4A, first edition, first printing (2011), Answer 7.2.1.3–101(a), definition of N_t,
printed page 744, file page 761.

The exercise defines F(p) as the probability of a Boolean function being true when each input bit is independently 1 with probability p. The weight of a binary string is its number of 1 bits.

The answer displays `F(p)=N_0 p^n+N_1 p^(n-1)(1-p)+...+N_n(1-p)^n`, while saying that N_t counts satisfying strings of weight t. With that definition the exponents must instead be `p^t(1-p)^(n-t)`.

For example, a conjunction of four variables has just one satisfying string, of weight 4. The stated definition gives N_4=1 and the printed formula gives (1-p)^4, instead of p^4.

The minimal repair consistent with part (b), which associates a string with its set of zero positions, is to change the definition to strings of weight **n-t**. The printed G(p) and H(p) computations use that corrected convention and are valid.

Original typesetting inspected. Errata and public-source screening:
`../sources/combination-applications-source-check.json`. No matching correction was found in the sources searched;
absolute priority is not established.
