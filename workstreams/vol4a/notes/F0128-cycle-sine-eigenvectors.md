# Cycle eigenvectors need a corrected sine argument

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–106(b,c), printed 807.

An aspect here is an eigenvalue of the graph Laplacian: its diagonal entries are vertex degrees, and its off-diagonal entries are minus the edge multiplicities. The answer sets theta=j*pi/n. Its cosine vectors are cos(2k*theta), for 0<=j<ceil(n/2), but its proposed additional vectors are sin(k*theta), for ceil(n/2)<=j<n.

Take the four-cycle, j=3 and theta=3*pi/4. On vertices k=1,...,4 the proposed vector is x=(sqrt(2)/2,-1,sqrt(2)/2,0). The claimed eigenvalue is 4*sin(theta)^2=2. However, (L*x)_1=sqrt(2)+1, whereas 2*x_1=sqrt(2). Thus this is not the asserted eigenvector.

Keeping the printed ranges, replace the sine vector by sin((2k-1)*theta). It satisfies the recurrence and periodic boundary conditions, and supplies an independent vector for each repeated cosine mode. For even n it also supplies the alternating mode at j=n/2. Merely changing the argument to 2k*theta while retaining the printed ranges would leave a zero vector at that index. Alternatively, standard sine and cosine vectors with argument 2k*theta work if the j=n/2 mode is moved into the cosine range.

The stated cycle eigenvalues and the final cylinder and torus tree-count products are correct.

Original typesetting inspected. No matching correction was found in the historical/current Volume 4A errata, refreshed Fascicle 4 errata or targeted public searches; see `../sources/tree-spectral-source-check.json`. Absolute novelty is not established.
