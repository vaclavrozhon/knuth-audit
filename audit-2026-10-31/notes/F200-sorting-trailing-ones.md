# F200: Wrong index in the trailing-ones substitution

Volume 4B, answer 7.2.2.2–64, printed page 560 (PDF page 580).

V_(x,j)^t denotes the value on wire j at layer t, numbered from the
left in x=x1...xn. Leading zeroes stay at the left and trailing ones
stay at the right in a comparator network.

The printed instruction replaces V_(x,j)^t by one when x has j trailing
ones. For x=001, j=1, this would set the first wire to one, although
the leading-zero rule sets that same wire to zero. The input is already
sorted, but the problem is not confined to inputs that can be omitted:
x=0101 has the same conflicting substitutions at wire 1.

Change the condition to **at least n+1−j trailing ones**, or replace
the indicated variable by V_(x,n+1−j)^t. The author's archived program
`sat-mintime-sort.w` correctly tests the low n+1−j bits with
`((x+1)&m[j-1])==0`, where m[k]=2^(n−k)−1.

The 2022 original typesetting and the September 2015 draft (page 196)
agree. Current 4B/Fascicle 6 errata contain no matching correction.
This is a book-text error; the inspected program implements the right
condition. No sorting optimality computation was rerun.
