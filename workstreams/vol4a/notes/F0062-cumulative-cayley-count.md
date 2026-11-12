# A cumulative step count is not periodic

**Location.** Volume 4A, first edition, first printing (2011), final
paragraph of answer 7.2.1.2–74, printed page 714 / file page 731.
The same defect occurs in the replacement for Fascicle 2, page 112,
answer 74, dated 11 October 2008 (all4f2, PDF page 14).

The answer defines k(j) as the number of alpha steps in the first j
steps of the chosen Hamiltonian cycle. Write r=g/c, where g is the
group's size and c is the order of gamma=alpha beta^-1. The printed
relation k(j+r)=k(j) cannot describe this cumulative count.

Take the cyclic group of order three with alpha=(1 2 3) and
beta=(1 3 2). These generators commute, gamma=(1 3 2), and r=1.
The Hamiltonian cycle that always uses alpha is

    () -> (1 2 3) -> (1 3 2) -> ().

It has k(0)=0 and k(1)=1, directly contradicting the displayed relation.
Both generators are distinct and nonidentity.

**Correction.** The preceding coset argument makes the *choice of the
next step* periodic with period r. Its cumulative count therefore obeys

    k(j+r) = k(j) + k(r).

In particular k(qr)=q k(r). The displacement after q blocks is
gamma^[q(t+k(r))], where beta^r=gamma^t. Consequently the stated
coprimality criterion for a Hamiltonian cycle follows as intended.
The criterion itself does not need correction.

The original book page and the original typeset
[Fascicle 2 errata](https://www-cs-faculty.stanford.edu/~knuth/all4f2.ps.gz)
were inspected: the erratum repeats the false relation rather than
correcting it. Current/historical 4A errata contain no further fix in
the screened range. Public searches found an earlier draft with a
correct verbal repetition argument, but no explicit report of this
later cumulative-count error. Absolute priority is not established.
See sources/cayley-generators-source-check.json. No code was needed.
