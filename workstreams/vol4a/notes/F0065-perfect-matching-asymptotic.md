# Wrong square-root coefficient in the perfect-matching cost

**Location.** Volume 4A, first edition, first printing (2011), first
line of answer 7.2.1.2–91, printed page 718 / file page 735.

Use n for the number of pairs, as in (49). There are 2n elements.
The answer correctly gives t_j=(j-1)(j-3)...(2 or 1), the number of
topological sorts on the first j elements. Equation (51) therefore gives

    N = t_(2n) = (2n-1)!!,
    M = sum(j=1..2n) t_j.

Here the double factorial denotes the product of positive integers
of the same parity down to 1 or 2. The next-to-last summand satisfies

    t_(2n-1)/N = (2n-2)!!/(2n-1)!!
               = 4^n / (2n binom(2n,n))
               = sqrt(pi)/(2 sqrt(n)) + O(n^(-3/2)).

The remaining summands total O(N/n), by applying
t_(j-2)=t_j/(j-1) separately to the even and odd subsequences.
Consequently the correct result is

    M = (1 + sqrt(pi)/(2 sqrt(n)) + O(1/n)) N.

The printed coefficient 2/sqrt(pi) is wrong. If n is instead taken
to denote the total number of elements, the correction is
sqrt(pi/(2n)); that convention does not validate the printed formula
either. The linear-time conclusion M=O(N) is unaffected.

The original answer, (49) and (51) were inspected. No matching
correction was found in the relevant 4A/Fascicle 2 errata or public
searches; an earlier draft has the same formula. Absolute priority
is not established. See sources/mmix-topological-source-check.json.
This calculation needs no numerical experiment.
