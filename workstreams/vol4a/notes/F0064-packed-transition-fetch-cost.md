# Packed-transition decoding omits two instructions of overhead

**Location.** Volume 4A, first edition, first printing (2011), paragraph
after program (45), printed page 341 / file page 358.

The amortized cost attributed to fetching codewords is (mu+5 nu)/20.
Here mu is the unit memory-access cost and nu is the ordinary
instruction cost in the book's MMIX model. The full overhead beyond
the stated 10 nu per permutation is instead **(mu+7 nu)/20**.

Each codeword supplies 20 nonzero transition codes. Besides the 20
successful AND/PBNZ pairs that dispatch those transitions, decoding
executes one additional pair with t=0. Its cost is 1 nu + 3 nu:
the probable branch is not taken. Advancing and loading the next
nonzero word then executes ADD, LDO and the taken PBNZ, costing
mu+3 nu. Thus the extra cost per 20 transitions is mu+7 nu.

For a table of B full codewords followed by its zero sentinel, put
N=20B. Excluding Visit, permutation initialization and the external
continuation, the relevant instruction counts are:

| Instructions | Count or cost |
| --- | --- |
| Seven-instruction swap and SRU | 8N nu |
| AND t,c,#1c | (N+B) nu |
| PBNZ t,1B | N nu + 3B nu |
| ADD p,p,8 | B nu |
| LDO c,p,0 | (B+1)(mu+nu) |
| PBNZ c,2B | B nu + 3 nu |

These give (B+1)mu+(10N+7B+4)nu, plus the one-time LDA and JMP.
In particular the two missing units recur at every codeword; they
are not a startup or termination effect. The algorithm and the
qualitative conclusion that its cost is just above 10 nu remain valid.

The original code and prose were inspected. The branch convention
agrees with the primary [MMIX description, section 17](https://www.mmix.cs.hm.edu/doc/mmix-doc.pdf)
and the [instruction timing table](https://mmix.cs.hm.edu/doc/instructions-en.html).
No matching correction appeared in the screened 4A/Fascicle 2 errata
or targeted public searches. Absolute priority is not established.
See sources/mmix-topological-source-check.json. No simulation was needed.
