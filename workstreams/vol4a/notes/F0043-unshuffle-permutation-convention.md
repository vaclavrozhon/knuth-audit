# V4A-F0043: The unshuffle example changes a component's internal order

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), proof of Theorem W, printed page 247 / file 264.
Original: `images/bookwise-p247.png`; convention: equation (91), page 236.

The book defines f^pi(x1,...,xn)=f(x_(1*pi),...,x_(n*pi)); therefore
i*pi is the testing position of the original variable xi. The
unshuffle is supposed to put variables 1 through k before the others
while retaining the testing order within each group.

For k=7 and the printed pi=(3,1,4,5,9,2,6,8,7), the original testing
order is

    2,6,1,3,4,7,9,8,5.

The stable separation of its two groups is

    2,6,1,3,4,7,5,9,8,

so the resulting permutation of positions must be

    sigma=(3,1,4,5,7,2,6,9,8).

The book instead prints (3,1,4,5,2,6,7,9,8), obtained by stably
separating the entries of pi itself. It puts x5 before x6, although
pi puts x6 before x5, and thus does not preserve the internal order.

Repair the example as above, or explicitly use inverse permutations
when describing/testing the stable separation. The notation of the
profile comparison in answer 166 likewise needs to distinguish
testing positions from original variable labels. This finding does
not refute Theorem W; it identifies the incorrect unshuffle in its
printed proof setup.

No matching correction was found in the relevant historical/current
Volume 4A or Fascicle 1 errata or in public searches for the example;
see `sources/bdd-readonce-source-check.json`. Absolute novelty is not
established. No computation was needed.
