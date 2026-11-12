# F237 — The recursive order sum uses twice the stated leading auxiliary count

Confirmed in Volume 4B, answer 407(b), printed 630/file 650.
The described construction has 2d lg d+O(d) auxiliary Boolean variables,
rather than the printed d lg d+O(d). Its clause count remains as stated.

At a merge of two variables with d values, the order encodings of the
new sums u and v have a total of 2d−2 bits. Two are identified with endpoint
bits of z. Therefore this level introduces 2d−4 auxiliary bits. This agrees
with the answer's explicit d=7 count of ten new bits.

For d=2^t+1, both recursive subproblems have 2^(t−1)+1 values. If B_t
counts their auxiliary bits, the construction gives

    B_t = 2*B_(t−1) + 2^(t+1) − 2.

Using the original method at d=5 gives B_2=0 and hence, for t>=2,

    B_t = 2t*2^t − 9*2^(t−1) + 2.

Any fixed base threshold changes only the O(d) term. In particular the
leading coefficient is 2, while the corresponding clause recurrence gives
3t*2^t+O(2^t), as printed. No claim is made that a different optimized
encoding could not use fewer auxiliary bits; the correction concerns the
recursive construction actually described.

The recurrence and fixed sample counts are recorded in
results/bookwise-order-fixed-witnesses.json. Draft page 266 has the same count.

The original Volume 4B typesetting and the corresponding September 23, 2015
author draft were inspected. Relevant current and historical Volume 4B and
Fascicle 6 errata, including their available TeX sources, have no matching
correction. This is not a claim about absolute priority or a physical copy.
Source details are in sources/bookwise-order-arithmetic-source-check.json.
