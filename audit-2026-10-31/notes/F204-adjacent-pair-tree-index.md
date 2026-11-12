# F204: Adjacent-pair clauses mix the sequence length and leaf count

Volume 4B, answer 7.2.2.2–117(b,c), printed page 572 (PDF page 592).

The exercise has n input bits x1,...,xn. Its adjacent-pair counter has
L=n−1 leaves, indexed L,...,2L−1. Consequently leaf q represents
x_(q−L+1) x_(q−L+2). At a node k with two leaf children, the three
input positions are therefore 2k−n+2, 2k−n+3, 2k−n+4.

The printed replacements instead use 2k−n+1 through 2k−n+3. They
retain the old leaf-count indexing while n still denotes the input
length. Similarly the three-leaf case has 2k=n−2, not 2k=n−1.
Increase the displayed input subscripts by one in both two-leaf cases,
and correct that three-leaf identity. An alternative is to introduce
L explicitly and use 2k−L+1 through 2k−L+3 throughout.

For a counterexample with neither a zero bound nor a tiny special case,
take n=6, r=3 and x=011111. There are four adjacent 11 pairs. The
five-leaf tree has internal nodes 2,3,4. The printed formulas make
nodes 3 and 4 count respectively (x1x2,x2x3) and (x3x4,x4x5), while
node 2 adds x1x2 to node 4. Thus x1x2 is counted twice and x5x6 is
missed. The root sees only three pairs and accepts the input.

All thirteen generated clauses hold with

    (b2_1,b2_2,b2_3,b3_1,b3_2,b4_1,b4_2) = (1,1,0,1,0,1,1).

The corrected indexing rejects this input for every assignment of
the seven auxiliary bits. The check considers only these 128 choices
for each of the two encodings, not a general input census.

The instruction to replace n by n−1 in (20)–(21) gives the correct
tree size, but the newly displayed replacement clauses also need that
substitution. The author's `sat-tomography-2nd.ch` clarifies the likely
source of the mismatch: its helper parameter n explicitly counts
adjacent pairs, and the caller passes the input length minus one.
Its local indices then have the correct meaning. This observation does
not certify every other part of that program.

The original PDF and September 2015 draft (page 208) have the same
subscripts. Current 4B/Fascicle 6 errata contain no matching correction.
Evidence: `images/bookwise-runs-p572.png`, `check_bookwise_sat117.py`,
`results/bookwise-sat117.json`, and `sources/bookwise-sat-tomography-2nd.ch`.
