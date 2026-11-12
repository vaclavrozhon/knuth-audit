# F236 — Independently relaxing the internal full-adder gates is unsound

Confirmed in Volume 4B, answers 410–411, printed 632/file 652.
A full adder takes three input bits t,u,v and should produce a carry c and
low bit z with 2c+z>=t+u+v for the proposed upper-bound encoding.
Answer 410 replaces this by five inequalities on auxiliary bits s,p,q:

    s >= t xor u; p >= t and u;
    z >= v xor s; q >= v and s; c >= p or q.

Set t=u=v=s=p=q=c=1 and z=0. All five inequalities hold, but
2c+z=2<3. In an exact full adder, p and q cannot both be 1. The relaxation
loses that invariant and then merges two carries using OR.

This is also visible in the displayed eight-stage circuit. At x=7,y=0,
all 44 gate clauses admit w=91, although the sum they claim to bound is
13*7+8*7=147. The full assignment is recorded in the fixed-witness file.
However, adding the final high-bit units for this particular exercise
still gives the correct yes/no answer on all 64 three-bit input pairs.
That bounded comparison is recorded explicitly; no false decision for
that particular numerical inequality is claimed.

The proposed reuse in answer 411 does fail as an inequality encoding.
For the 3-by-3 FIFO bin reduction of answer 41, take x=y=7, so every
partial product is 1. The three half adders and three full adders, relaxed
as instructed, admit the output w=37 instead of 49. The fixed trace records
every gate and verifies all its clauses. Setting z=w then satisfies the
lexicographic comparison z>=w but falsely certifies xy<=z.

One local repair is to add (not p or not q) to each relaxed full adder.
Then t+u+v <= 2p+s+v <= 2(p+q)+z <= 2c+z. Exact sums retain an extension,
so this repair restores the intended relation. Alternatively, use the
direct ternary-parity and majority clauses of answer 42 with the correct
inequality directions; seven clauses per full adder suffice. The stated
9mn/11mn upper bounds can still be attained with that valid construction.
The problem is the printed gate relaxation, not impossibility of the goal.

Evidence: check_bookwise_order_witnesses.py and
results/bookwise-order-fixed-witnesses.json. The current 2022 errata for410
fix different indices and the final high-bit constraints; those fixes are
included in the circuit checked here. Draft page 268 has the same unsafe
full-adder relaxation and its reuse in411.

The original Volume 4B typesetting and the corresponding September 23, 2015
author draft were inspected. Relevant current and historical Volume 4B and
Fascicle 6 errata, including their available TeX sources, have no matching
correction. This is not a claim about absolute priority or a physical copy.
Source details are in sources/bookwise-order-arithmetic-source-check.json.
