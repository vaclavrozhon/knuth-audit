# F180 — coefficient ratio multiplies over m instead of n

Minor mathematical typo. Volume4B, first edition, second printing2022,
answer MPR145, printed397/file417, ratio of multinomial coefficients.
The denominator is printed as product(j=1..m,(2k_j−1)!!); the upper limit
must be **n**, the number of coordinates.

For n=3, m=2, (k1,k2,k3)=(0,0,2), the actual ratio
c'(0,0,4)/c(0,0,2) is1. The printed denominator includes only the first
two factors, both(−1)!!=1, and gives3!!=3. The corrected denominator also
includes(2k3−1)!!=3 and gives1. If m>n the printed expression can even
refer to coordinates that do not exist. Khinchin's inequality is unchanged.

This follows immediately from the printed multinomial coefficients:

    c'(2k1,...,2kn)/c(k1,...,kn)
      = (2m−1)!! / product(j=1..n,(2k_j−1)!!).

Original typesetting: images/first100-p397.png. The statement on printed29
and the complete answer were read together. Six historical/current errata
layers and three TeX versions contain no matching correction; public
searches likewise found none. Details in
sources/first100-mpr140-145-novelty.json. No claim of absolute priority or
inspection of a later physical printing is made.
