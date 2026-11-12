# The partition polynomial uses n as its family index

Volume 4A, first edition, first printing (2011), Answer 7.2.1.4–31, first solution,
printed page 752, file page 769.

The answer introduces polynomials f_(k,r), one for each residue r modulo k!, to count partitions of n into exactly k parts. The following equality instead uses `f_(n,n mod k!)(n)`. Its first subscript must be **k**.

For a concrete check, take n=3,k=2. There is one partition of 3 into two parts. The printed expression instead asks for f_(3,1)(3). The degree-2 constituent for three parts and residue 1 modulo 6 is `f_(3,1)(x)=(x^2-1)/12`, as follows also from the three-part formula in the next paragraph. Its value at 3 is 2/3, not 1. The corrected f_(2,1)(3) is 1. The polynomial-counting method itself is unchanged.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/partition-counting-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
