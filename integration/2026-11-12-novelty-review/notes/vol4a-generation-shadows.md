# Volume 4A: Gray cycles, permutations and shadows, publication review

Reviewed on 12 November 2026 against the first edition, first printing
(2011). All fifteen baseline-confirmed findings F0057–F0065 and
F0067–F0072 are retained. F0066 was already dismissed before this review
and is outside the baseline. A Gray traversal changes one coordinate
at a time; a set family's lower shadow consists of its subsets with
one element removed, and its upper shadow of supersets with one
additional element. Other notation is defined in the detailed notes.

The original relevant statements and examples were inspected on pages
293, 313, 319, 326–329, 335, 338, 341, 343–344, 351, 383, 686,
703, 710, 714–716, 718, 727, 730, 733 and 738–739. Small traces,
endpoint arguments and the displayed algebra were checked by hand.

| ID | Reason for retaining the finding |
| --- | --- |
| V4A-F0057 | Exercise 7.2.1.1-44, p. 313: the square has two directed delta sequences starting at zero and only two perfect matchings, so the bound reads 2<=1. An unordered pair loses the cycle's direction. For n>=2 multiply the binomial bound by two. |
| V4A-F0058 | Answer 7.2.1.1-45(d), p. 686: the inserted edge (u XOR 2)--(v XOR 3) changes two bits and duplicates the exposed v XOR 3 endpoint. Its second endpoint must be v XOR 2. The same error occurs in the 2009 replacement. |
| V4A-F0059 | Answer 7.2.1.2-5(a), p. 703: the reversal-swap average includes floor(n/2) swaps at the final descending permutation, where L2 already terminates. Subtract floor(n/2)/n!. At n=3 the actual average is 1/3, not 1/2; the limiting constant is unchanged. |
| V4A-F0060 | Answer 7.2.1.2-52, p. 710: changing a middle factor s in P*s*Q requires premultiplication by P*(s'*s^-1)*P^-1. The reflected Gray path need not make P identity. The three-symbol witness requires (1 2), absent from the advertised tau values and inverses. Conjugation is missing. |
| V4A-F0061 | Answer 7.2.1.2-72, p. 714: the fiber count (n-1)! is valid for the full symmetric group, not the stated arbitrary permutation group. The cyclic subgroup of order three has one element in each indicated fiber, not two. Replacing the factorial by the stabilizer size repairs the endpoint argument. |
| V4A-F0062 | Answer 7.2.1.2-74, p. 714: k(j) counts all alpha steps in a prefix, so periodicity of the choices gives k(j+r)=k(j)+k(r), not k(j+r)=k(j). In the order-three cyclic example r=1 and k(1)=1 while k(0)=0. The 2008 replacement repeats the defect. |
| V4A-F0063 | Answer 7.2.1.2-78, p. 716: lines 31–38 contain eight instructions at r=3, not 2r-1=5. The varying block is lines 34–38; the preceding three operations remain necessary. The final cost formula is already consistent with that correction. |
| V4A-F0064 | Program (45) discussion, p. 341: after every twenty nonzero codes an extra AND/probable-branch pair costs four nu, and pointer advance/load/taken branch cost mu+3nu. The recurring overhead is (mu+7nu)/20, not (mu+5nu)/20. This is not a startup or termination effect. |
| V4A-F0065 | Answer 7.2.1.2-91, p. 718: for n pairs, the penultimate summand divided by N is (2n-2)!!/(2n-1)!!=sqrt(pi)/(2sqrt(n))+O(n^(-3/2)). The others contribute O(1/n). The printed coefficient 2/sqrt(pi) is incorrect; the linear-time conclusion remains valid. |
| V4A-F0067 | Answer 7.2.1.3-17, p. 727: sqrt(x(x-1))=x-1/2-1/(8x)+O(x^-2) already disproves the printed positive 1/x term. The general coefficient is -(t^2-1)/24. The following inverse expansion is correct. |
| V4A-F0068 | Answer 7.2.1.3-33, p. 730: for n=3 the endpoint sum is three, not seven. Replace the constant +2 by -2; the resulting doubled counts agree with the table. The direction omitted by reversal is j<i, not the already counted j>i. |
| V4A-F0069 | Exercise 7.2.1.3-48, p. 383: the binary-mask exchange 0101 to 1100 sends 0102 to 2100, not 1200. The three middle example terms must be 2100,2001,0021. The general construction's fixed-permutation argument remains valid. |
| V4A-F0070 | Answer 7.2.1.3-74, p. 738: n=4,t=2,N=1 gives an upper shadow of size two, while the displayed formula gives four. The coefficient is n-1-n_t, not n+1-n_t; the excess is 2N. The 2025 parentheses correction is unrelated. |
| V4A-F0071 | Answer 7.2.1.3-78, p. 739: the final equality identifies a lower-shadow size with the initial family's own size. At t=2,M=N=1 these are three and two. Insert the missing shadow operator; the preceding argument then has the intended conclusion. |
| V4A-F0072 | Answer 7.2.1.3-80, p. 739: t=2,N=4 gives N0=1,N1=3 but kappa_2(N0)=2. The asserted equality N=N0+kappa_t(N0) fails. Use N=N0+N1 and N1>=kappa_t(N0); the Lovasz bound is unaffected. |

## Official and public-source comparison

Compared the refreshed [prepublication changes](https://www-cs-faculty.stanford.edu/~knuth/all4a-pre.ps.gz),
[later changes](https://www-cs-faculty.stanford.edu/~knuth/all4a.ps.gz),
[current errata](https://www-cs-faculty.stanford.edu/~knuth/err4a.ps.gz),
and relevant Fascicle 2 and 3 layers
([all4f2](https://www-cs-faculty.stanford.edu/~knuth/all4f2.ps.gz),
[err4f2](https://www-cs-faculty.stanford.edu/~knuth/err4f2.ps.gz),
[all4f3](https://www-cs-faculty.stanford.edu/~knuth/all4f3.ps.gz),
[err4f3](https://www-cs-faculty.stanford.edu/~knuth/err4f3.ps.gz)).
Fascicle 2's main-page offset is 280 and answer-page offset 602;
Fascicle 3's corresponding offsets here are 354 and 637. The relevant
replacement entries were read in full, not treated as resolved merely
because they mention the same exercise. The Gray-cycle bound/splice
and the cumulative-count equation remain defective in those replacements.
Other nearby entries concern d(6), new Hamiltonian-cycle results,
notation, line references, and separate shadow formulas.

Fresh searches combined Knuth/TAOCP with Gray cycles/perfect matchings
44, Sims/conjugation, cosh/swaps, k(j)/Hamiltonian, perfect matching
718, codewords 341, falling-factorial 727, near-perfect paths,
upper shadow, and Lovasz 739. No matching explicit report was found.

The public [tamnd/brain solutions](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4)
were screened for 7.2.1.1 exercises 44–45; 7.2.1.2 exercises 5, 52,
72, 74, 78, 91; and 7.2.1.3 exercises 17, 33, 48, 74, 78, 80.
Many are unrelated to the actual exercise or only discuss general
methods. None identifies the corresponding printed defect.

Wilson's [permutation-generation paper](https://www.cs.auckland.ac.nz/~mcw/Research/Outputs/Wils2006.pdf),
p. 4, explicitly retains conjugation when changing a middle factor.
The new live request timed out; the previously retrieved copy and its
provenance were checked locally. It supports the algebra, not a prior
report about the book. The [MMIX instruction table](https://mmix.cs.hm.edu/doc/instructions-en.html)
was reopened to confirm memory costs and the one/three-nu branch model
used in F0064. Neither source reports the corresponding book error.

No matching prior error report was found in these checked sources.
Absolute priority is not established.
