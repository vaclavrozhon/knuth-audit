# V4A-F0054: Both descendant-family extrema are wrong

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), answer 7.1.4-267, printed 678 / file 695. Original:
`images/bookwise-p678.png`.

For an ordered forest F on n preorder-numbered vertices, d(F) is
the family of inclusive descendant sets of its vertices. Z(d(F))
counts all nodes of its reduced ZDD, including the two sinks.
The answer gives minimum n and maximum floor(n^2/4)+2n+1.

Every vertex appears in d(F), so the diagram has at least n
nonsink nodes. Both sinks are needed for this nonempty family of
nonempty sets. A forest of n isolated vertices attains n+2 nodes.
Thus the minimum is n+2, not n.

For n=2, both possible ordered forests give four nodes, whereas the
printed maximum is six. More generally the answer's stated extremal
comb with n=2m-1 vertices has Z=m(m+1), not the printed value. Its
own auxiliary recurrence yields the corrected maximum

    floor(n^2/4)+n+1   for n >= 2;   3 for n=1.

For completeness, the short bound follows directly from that
recurrence. Write zeta(T) for the auxiliary quantity defined in the
answer. Induction gives zeta(T) <= floor(n^2/4)+n for an n-vertex
tree. With one child, the required inequality is
`1+floor((n-1)^2/4) <= floor(n^2/4)`. With at least two children,
combine the sizes of all but the last into a >= 1, and write b >= 1
for the last size. The required inequality is

    1+a+floor(a^2/4)+floor(b^2/4)
      <= floor((a+b+1)^2/4).

It holds at b=1 with equality and its right-minus-left difference
does not decrease as b grows. Combining child sizes is valid since
the sum of their squared-size floors is at most the floor for their
combined size. The forest formula in the answer then gives the
same upper bound, including its extra indicator for a last singleton.
Start from the two- or three-vertex extremal tree and repeatedly add
a new root whose first child is the old tree and whose last child
is a leaf. This attains the bound in each parity, including the
stated odd comb. No forest enumeration is needed.

No matching correction was found in the screened 4A/Fascicle 1
errata or targeted public reports. See `sources/zdd-tail-source-check.json`.
Absolute novelty is not established.
