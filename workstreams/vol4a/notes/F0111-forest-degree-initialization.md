# The forest generator leaves its initial prefix undefined

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–21, step G1, printed 784.

Let n_j be the prescribed number of nodes of degree j, N their total, and f=N-sum(j*n_j) the number of roots. The loop in G1 writes exactly positions f through N-1, then the final assignments write b_0, b_N and c_0. Positions 1 through f-1 remain unassigned, although G2 immediately visits the whole array.

For example, take t=1, n_0=3 and n_1=2. All stated assumptions hold. The loop sets b_4=1 and b_3=1; the final assignment sets b_5=0. The first output is therefore `??110` instead of the required lexicographically first degree sequence `00110`, representing two isolated roots followed by a three-node chain. This is a nonempty, ordinary forest, not an empty-instance convention.

After the initialization loop, l=f. Add `b_1=...=b_(l-1)=0` before G2. The single-tree case f=1 already initializes every entry, which explains why the displayed example does not expose the omission.

Original typesetting inspected. Historical/current Volume 4A and refreshed Fascicle 4 errata and targeted public queries yielded no matching correction. See `../sources/tree-gray-generators-source-check.json`; absolute novelty is not established.
