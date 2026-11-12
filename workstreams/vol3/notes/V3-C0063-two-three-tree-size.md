# V3-C0063 — The 2–3 search estimate counts keys, not internal nodes

Confirmed size-parameter mismatch in volume 3, second edition, first
printing (1998), exercise 6.2.3-27 on p.480 and its answer on p.718
(file pp.491 and 729).

The exercise specifies N internal nodes, but the answer's estimate
2 lg(N+2)-2 uses the number of keys. A node of a 2–3 tree can contain
either one or two keys, so these parameters differ.

Consider this valid height-two 2–3 tree (each bracket is one internal
node, and all omitted external children are on the same level):

              [2,5]
             /  |  \
           [1] [3,4] [6]

There are four internal nodes and six keys. An unsuccessful search
for 3.5 uses two comparisons to select the middle child of the root
and two more in [3,4], regardless of which key is compared first
within either two-key node. Thus four comparisons are necessary in
the usual node-by-node search. Substituting the stated N=4 gives
2 lg 6-2 < 4. Substituting the key count N=6 gives exactly 4.

Changing the exercise to N keys makes its parameter match the answer.
The example drawn in the answer has the same mismatch: it has eleven
internal nodes but fourteen keys, giving six comparisons under the
intended worst-case arrangement.

Original pp.480 and 718 were checked visually and retained. No matching
correction was located in the five official layers or limited public
searches. See `sources/balanced-trees-errata-review.json`.
