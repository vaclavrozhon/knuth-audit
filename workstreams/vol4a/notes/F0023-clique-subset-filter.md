# V4A-F0023: the maximal-element update filters equality instead of containment

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), answer 7.1.3-132(d), step Q7, printed page 604 / file page 621.
Originals: `images/bookwise-p603.png` and `images/bookwise-p604.png`.

The update promises to replace the maximal elements of C_(k-1) by
the maximal elements of C_k. Here C_k is the family obtained by
intersecting, for each of the first k vertices, either its closed
neighborhood or the complement of that vertex. A set is represented
by an integer whose bit j indicates membership of vertex j.

Consider the graph on {0,1,2,3} with edges

    {0,1}, {0,2}, {0,3}, {1,3}.

Its closed-neighborhood words are (15,11,5,11). Processing vertex 0
does nothing because its neighborhood is all four vertices. After
vertex 1, the correct maximal family C_2^+ is

    {11,13} = {{0,1,3}, {0,2,3}}.

Now process vertex 2, so v = 4 and p_2 = 5. Partitioning these two
words puts 11 in the lower part and 13 in the upper part. For u=13,
subroutine Q first retains

    u' = u & p_2 = 5.

Step Q7 then forms

    w = u & ~v = 9 = {0,3}.

The lower part contains only 11. The printed test asks whether
w equals an entry there. Since 9 != 11, it appends 9, and M4
returns the three words 11,9,5. But 9 is a proper subset of 11.
The promised maximal family C_3^+ is only {11,5}.

Q7 must test containment, `w & w_q == w`, rather than equality.
This counterexample refutes the claimed maximal-element update
and its invariant. It does not by itself assert an incorrect final
clique list for this graph: a later stage can remove the redundant
entry. No complete enumeration or timing claim was tested here.

The current and historical Volume 4A and Fascicle 1 errata were
screened; no matching correction was found. Fresh official files
match the archived sources. Targeted public searches found no
matching report, which does not establish absolute novelty. See
`sources/clique-subset-source-check.json`. The four-vertex trace
was checked by hand.
