# V4A-F0017: the outer permutation masks cannot be paired positionwise

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), answer 7.1.3-51(a), and the even-c branch of 51(b), printed
page 591 / file page 608. Original: `images/bookwise-p591.png`.

The network (71) applies swaps of distances 1,2,...,2^(d-1),...,2,1.
A mask bit at position j selects the exchange of bits j and j+delta
in a delta-swap. Positions are numbered from 0 at the right.
For the permutation j -> j XOR c, part (a) specifies the middle mask
and says that theta_k = c_k*mu_{d,k} XOR theta_hat_k, with theta_hat_k
an arbitrary submask of mu_{d,k}.

Take d=2, c=2, and the three masks

    theta_0 = 0001, theta_1 = 0011, theta_hat_0 = 0001.

They satisfy the printed conditions, because c_0=0, c_1=1,
mu_{2,0}=0101 and mu_{2,1}=0011. Applied to the input word 0001,
the three swaps give

    0001 --1-swap--> 0010 --2-swap--> 1000 --1-swap--> 1000.

The requested output is 0100: input bit 0 belongs in output position
2. The same masks are allowed by the even-c branch of part (b), since
it sets theta_0=theta_hat_0 arbitrarily and c'=c''=c/2. For d=2,c=2,
the cyclic permutation j -> (j+c) mod 4 is the same permutation, so
the same counterexample refutes that branch too.

The last outer mask must be paired with the first according to the
positions reached after the inner permutation. In this example,
theta_hat_0=0100 gives the required result, whereas theta_hat_0=0001
does not. Choosing all right-hand masks zero still gives the simple
valid construction described later in the answer. This finding does
not refute the general permutation network, the existence of such
mask sequences, or the numerical count of those sequences.

The current and historical 4A errata and both Fascicle 1 layers were
screened. The fresh official files match the archived sources. No
matching correction was found; targeted public searches found no
matching report. Absolute novelty is not established. See
`sources/permutation-mask-source-check.json`. The trace was checked
by hand; no permutation enumeration was run.
