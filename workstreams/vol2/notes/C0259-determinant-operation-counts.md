# V2-C0259: incompatible exact operation counts for determinants

Confirmed exact-count errors, low impact. Third edition, first printing,
answers 4.6.4-69 and 70, printed 717–718/file 729–730. The algorithms'
division-free character and O(n^5), O(n^4) orders are unaffected.
Original typesetting inspected on 10 November 2026.

Answer 69 explicitly stops the recursive construction at a 2 by 2
determinant and says that redundant computations are suppressed.
Nevertheless its claimed exact addition count is

    20 binom(n,5) + 8 binom(n,4) + 4 binom(n,3)
       + 24 binom(n,2) - n.

At n=2 this is 22 additions. The specified base case is a*d-b*c,
which uses one subtraction; the answer expressly avoids subtracting
1 from the last two diagonal entries. Its multiplication formula
correctly gives 2 for this same base case. Thus the purported exact
addition count is inconsistent with the described algorithm. This
note does not propose a general replacement polynomial or contest
the asymptotic bound.

Answer 70 gives the exact multiplication count for all coefficients
of an n by n characteristic polynomial as

    M(n) = 6 binom(n,4) + 7 binom(n,3) + 2 binom(n,2),

then claims that requesting the determinant alone saves
3 binom(n,2)-n+1 multiplications. At n=2 these are both 2, so their
difference says that a generic 2 by 2 determinant can be computed
with **zero** multiplications and no divisions. That is impossible:
starting with four independent entries, addition, subtraction and
constant scaling can only yield affine functions, while a*d-b*c is
quadratic. More directly, the two products a*d and b*c used for the
constant coefficient of the characteristic polynomial are still
needed when that coefficient alone is requested. Computing the trace
uses one addition and no multiplication, so omitting it cannot save
the two multiplications. The subtraction claimed in this paragraph
therefore needs correction; no optimal general savings formula is
asserted here.

Both errors survive comparison with all2-prepre, all2-pre, all2,
err2 and current err2.textxt. The older second-edition errata introduce
these very expressions as new answers 66 and 67 on page 655; they do
not mark them as erroneous. The known 1998 change on page 718 concerns
Kaltofen's asymptotic result, not these exact counts. Public searches
for the page, exercises and determinant operation counts found no
matching report. Absolute priority and later physical printings are
unverified. No report sent.
