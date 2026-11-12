# The odd-product spectrum is missing a minus sign

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–105(h), printed 806.

For regular graphs G prime and G double-prime, let n prime and n double-prime be their orders, d prime and d double-prime their degrees, and alpha prime_j and alpha double-prime_k their Laplacian eigenvalues, indexed with alpha_0=0. The notation [j=0] means 1 when j=0 and 0 otherwise.

The answer gives the odd-product eigenvalues as

    d + (d' - alpha'_j n'[j=0]) (d'' - alpha''_k)
      + (d' - alpha'_j) (d'' - alpha''_k - n''[k=0]),

where d=d'(n''-d'')+(n'-d')d''. The first factor must instead be

    d' - alpha'_j - n'[j=0].

For a concrete counterexample take G'=K3 and G''=K2. Their parameters are (n',d',alpha')=(3,2,(0,3,3)) and (n'',d'',alpha'')=(2,1,(0,2)); hence d=3. The printed expression gives eigenvalues {-1,2,2,3,6,6}. In particular j=0,k=1 gives -1, impossible for a graph Laplacian. The odd product in this case is the triangular prism K3 square K2, with eigenvalues {0,2,3,3,5,5}, exactly as the corrected formula gives.

To see the missing sign directly, let A', A'' be adjacency matrices and J', J'' the all-ones matrices. Odd adjacency is A' tensor (J''-A'') + (J'-A') tensor A''. Subtracting this from d times the identity gives the corrected expression on a common adjacency/all-ones eigenbasis.

The identical missing minus occurs in the official Fascicle 4 addendum dated 5 April 2007, page 101, new paragraph (h) for answer 105. That addendum introduces the formula; it does not correct this defect. Both the book and addendum originals were inspected.

Original typesetting inspected. No matching correction was found in the historical/current Volume 4A errata, refreshed Fascicle 4 errata or targeted public searches; see `../sources/tree-spectral-source-check.json`. Absolute novelty is not established.
