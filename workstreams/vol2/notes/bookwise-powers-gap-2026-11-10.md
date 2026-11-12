# Addition-chain gap: exercise 27 and the numerical tables

10 November 2026. Original printed pages 477–478, exercise 27 on 483,
and its answer on 695 were read; page 695 was also inspected visually.
This supplements the existing reviewed addition-chain section.

An addition chain starts at 1 and forms each later term as a sum of two
earlier terms. Let l(n) be its minimum length, lambda(n)=floor(log2(n)),
and s(n)=l(n)-lambda(n) the minimum number of small steps. The table's
c(r) is the smallest n with l(n)=r; d(r) counts all n with that length.

The answer's reduction is correct. The c(r) increase, since a first
integer requiring more than r steps has a predecessor requiring r
steps: adjoining 1 increases chain length by at most one. Thus for
c(r)<=n<c(r+1), l(n)<=r and lambda(n)>=lambda(c(r)). This gives
s(n)<=s(c(r)), exactly the intended printed comparison. The listed
first targets for one through six small steps are 3, 7, 29, 127, 1903,
and 65131.

The scan has a missing closing parenthesis in l(c(r)). This is already
publicly noted on [Clift's c(r), d(r) page](https://additionchains.com/crdr.html),
which also reproduces the numerical tables. It is a known correction,
not a new finding and not a red marker. That source gives c(28)=4169527
with seven small steps, consistent with the original tentative remark.

All original c(r) entries through r=27 and d(r) entries through r=25
agree with that primary computational source. Their exhaustive
optimality calculations are accepted as external numerical results,
not repeated. The 2022/2024 official amendments expand the table and
clarify that proving minimality is the difficult computation; they are
already published changes. Historical counts of backtracking cases,
global minimality of the numerical examples, and empirical fits are
not newly reproduced. The displayed chains can be checked directly;
they supply upper bounds, not independent optimality certificates.

The asymptotic comment on page 478 follows by substituting c(r) into
the already reviewed asymptotic chain-length bounds. The Scholz
discussion and later corrections have the separate accepted review
`powers-open.md`; no research conjecture is being solved here.

Exercise 27 is now reviewed with these source limitations. Pages
477–478 are covered in this sense. This note alone does not certify
other exercises sharing pages 483 or 695.
