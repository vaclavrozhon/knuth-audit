# V4A-F0037: The covering-function asymptotic loses a leading term

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), exercise 7.1.4-131(a), printed page 267 / file 284.
Originals: `images/bookwise-p267.png` and `images/bookwise-p642.png`.

The exercise concerns a Boolean covering function with p rows and q
columns. With variables tested row by row, it asks for a BDD node
count asymptotic to p*q*2^(q-1), for fixed q as p tends to infinity.
Here asymptotic equivalence means that the ratio tends to one.

The printed answer on page 642 instead correctly gives the exact size

    (p*q + 2*p - 2*q + 2)*2^(q-1) - p + 2.

For fixed q, its coefficient of p is (q+2)*2^(q-1)-1. The omitted
term p*(2^q-1) has the same order as the claimed leading term.
In particular, for q=2 the exact size is 7*p-2, whereas the exercise
claims asymptotic equivalence to 4*p; their ratio tends to 7/4.

Replace the asymptotic expression in part (a) by
p*((q+2)*2^(q-1)-1). The exact answer and part (b) do not need this
correction. The known deletion of "however" in part (c) is separate.

Current and historical Volume 4A and Fascicle 1 errata were screened;
no matching correction or public report was located. See
`sources/bdd-size-source-check.json`. Absolute novelty is not
established. No computation was needed.
