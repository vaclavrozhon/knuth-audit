# The Eulerian-circuit product omits all factors involving vertex zero

Volume 4A, first edition, first printing (2011), Answer 7.2.1.3–107, determinant formula,
printed page 745, file page 762.

An Eulerian circuit uses every edge exactly once. The answer counts circuits in the complete graph on vertices 0,...,2m, up to cyclic rotation but distinguishing reversal. Its determinant is the 2m by 2m matrix on indices 1,...,2m, with off-diagonal entries -1/(z_j^2+z_k^2) and diagonal entries summing 1/(z_j^2+z_k^2) over all other vertices k, including zero.

The factor multiplying this determinant is printed as a product over `1<=j<k<=2m`. It must be over **0<=j<k<=2m**.

For m=1 set d_jk=z_j^2+z_k^2. The determinant is

```
1/(d_01*d_02) + 1/(d_01*d_12) + 1/(d_02*d_12).
```

The printed product supplies only d_12, leaving a rational function homogeneous of degree -2, from which the intended coefficient of z_0^2 cannot be obtained. The full product d_01*d_02*d_12 gives `d_01+d_02+d_12 = 2(z_0^2+z_1^2+z_2^2)`. Its z_0^2 coefficient is 2, correctly counting the two orientations of the triangle.

More generally the printed expression has total degree 4m^2-6m, whereas the requested monomial has degree 4m^2-2m. The missing 2m quadratic factors account exactly for this difference.

The cited [McKay–Robinson paper](https://users.cecs.anu.edu.au/~bdm/papers/euler.pdf), section 2 and section 6, equation (8), takes its product over every pair among all graph vertices. Its matrix-tree determinant omits one root vertex only from the matrix, not from that product. Reindexing the root to zero and factoring out the squared variables gives the repaired book formula. The paper was inspected in its original PDF; a local copy and retrieval hash are in sources/mckay-robinson-euler-1998.*. This confirms the repair, without independently rerunning the large circuit enumerations.

Original typesetting inspected. Errata and public-source screening:
`../sources/combination-applications-source-check.json`. No matching correction was found in the sources searched;
absolute priority is not established.
