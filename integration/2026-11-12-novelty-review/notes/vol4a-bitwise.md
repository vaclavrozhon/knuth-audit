# Volume 4A: bitwise findings, publication review

Reviewed on 12 November 2026 against the first edition, first printing
(2011), with the June 2016 replacement explicitly identified where it
is the defective source. All sixteen baseline findings are retained.

The original pages 155, 193, 202, 591, 593, 598, 600–604, 611–614,
618–620 and the original typesetting of the replacement answer 98 were
inspected as relevant. The existing detailed notes were read, and their
short computations and traces checked by hand. Broadword chains, in
these notes, mean the book's sequences of fixed-width arithmetic and
bitwise operations; a strong chain also has exactly those intermediate
values when interpreted without truncation on 2-adic integers.

| ID | Reason for retaining the finding |
| --- | --- |
| V4A-F0017 | Answer 51, p. 591: for d=2,c=2, the allowed masks 0001,0011,0001 send 0001 to 1000 instead of 0100. Pairing outer masks by position ignores the intervening permutation. Both part (a) and the even-c branch of (b) admit this example. |
| V4A-F0018 | Answer 66(d), p. 593: at n=192,u=1 the outgoing carry computed from the local prefix t becomes zero after the second word, losing the required third-word bit 129. It must use the completed word v_j. |
| V4A-F0019 | Answer 94, p. 598: x=0 and constant l=255 meet the two asserted low-byte conditions, but subtraction gives byte 1 and therefore no high-bit flag. The arbitrary-constant characterization lacks the upper bound 128 on the borrow magnitude. The ordinary zero-byte test remains correct. |
| V4A-F0020 | The June 30, 2016 replacement for answer 98, p. 598, expands flag 128 to 192 rather than 255 because it shifts by one instead of seven. With x=0,y=1 it consequently returns the wrong bytewise minimum and maximum. This is a defect in the replacement, not the original first-printing routine. |
| V4A-F0021 | Answer 113, p. 600: the copied NOR operation gives -1 on zero inputs as a 2-adic operation, instead of the two-bit result 3. The allowed operations on p. 155 include NOR and other complemented Boolean operations. These, and the subtraction branch's intermediate XNOR, require a bounded implementation. The existence claim itself is not refuted. |
| V4A-F0022 | Exercise 114 and its answer, pp. 193 and 601: a strong two-bit chain consisting of right shift by one does not act independently on packed fields. The packed input 0100 shifts to 0010 rather than 0000. The one-operation obstruction in the note also refutes the exact same-length claim, not only the proposed construction. |
| V4A-F0023 | Answer 132(d), p. 604, Q7: for closed neighborhoods (15,11,5,11), the update appends word 9 despite existing word 11 containing it. Equality must be replaced by containment. The intermediate maximal-family invariant fails; this example alone does not claim a wrong final clique list. |
| V4A-F0024 | Answer 183, p. 614: the maximum curvature of y=alpha*x^2 is 2*abs(alpha), not alpha/2. The corresponding translated and rotated numerical example has maximum curvature about 21.08, not 5.27. |
| V4A-F0025 | Answer 183, p. 614: the given endpoint (-5/2,-19/2) gives F=234 and rounds to (-2,-9), contradicting both the curve and stated rounded endpoint. Changing its second coordinate to 17/2 repairs both checks and preserves the required monotone arc. |
| V4A-F0026 | Answer 179, p. 613, I10: the new component's CHILD field is never initialized, though the subsequent traversal reads it. Two identical rows 010 reach that read. I1 initializes only the root; no blanket zero-fill premise is given. |
| V4A-F0027 | Answer 179, p. 612, I4: after traversing a nonempty transferred child list, R is null when SIB(R) is assigned. Rows 1111111,1000001,1001001,0000000 reach the case. The 2012 erratum removes the saved last-node pointer but leaves this null write unchanged. |
| V4A-F0028 | Answer 179, p. 613, I10: the run boundary is a_j=2*c_j-(j mod 2), so floor(a_j/2) records c_j-1 for a new black run. Page 611 numbers the pixels from one. The first column needs the ceiling already used for the area computation. |
| V4A-F0029 | Answer 213, p. 620: for 16 input bytes the two loads use offsets -16 and 0, skipping -8 and reading past the message. The explicit zero-message-with-final-01 example returns zero instead of the required CRC 0x8005. Moving the loop increment after the load repairs the indexing. |
| V4A-F0030 | Answer 194, p. 618: the five displayed vectors have rank three and nullity two. The example's r=0 contradicts the two displayed basis vectors and must be r=2. The earlier initialization r=0 is correct. |
| V4A-F0031 | Answer 216, p. 620: under the printed floor-logarithm premise, two n-bit words can be too short. With n=2 and inputs 1,2,3,3,3,3,3, the bucket sum is 17 and the first missing subset sum is 19, both above 15. This concerns the precision claim, not the linear-time algorithm with sufficient width. |
| V4A-F0032 | Answer 199, p. 619: the surrogate filter is zero at the valid UTF-8 prefix ED 80, causing rejection. The full sequence ED 80 80 represents U+D000. The subtraction constant must be hexadecimal 1F rather than 20. |

## Official and public-source comparison

Compared the refreshed [historical Volume 4A changes](https://www-cs-faculty.stanford.edu/~knuth/all4a-pre.ps.gz),
[later changes](https://www-cs-faculty.stanford.edu/~knuth/all4a.ps.gz),
[current errata](https://www-cs-faculty.stanford.edu/~knuth/err4a.ps.gz),
and both Fascicle 1 layers
([all4f1](https://www-cs-faculty.stanford.edu/~knuth/all4f1.ps.gz),
[err4f1](https://www-cs-faculty.stanford.edu/~knuth/err4f1.ps.gz)).
The old Fascicle 1 answer pages are roughly 434 pages earlier; the
relevant entries were compared by exercise number as well as location.
Nearby corrections to traversal next, I4, answer 181, the parity lcm
test, and answers 203, 214 and 218 do not repair these defects. The
April 2010 answer-216 entry changes only hyphenation of double precision.

New queries combined Knuth or TAOCP with 7.1.3 exercises 51, 66, 94,
98, 194, 213, 216; strong chains and shifts; parabola curvature;
SIB(R); CRC; eda0; and double precision. Most exact queries produced
no relevant report; broader results were also screened. The earlier
source-check records remain linked from each detailed finding.

The public [tamnd/brain bitwise solutions](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4/7.1.3)
were screened individually at exercises 51, 66, 94, 98, 113, 114, 132,
179, 183, 194, 199, 213 and 216. None identifies the corresponding
printed defect. In particular, the purported correction to exercise
114 concerns the generated solution's carry handling, changes the
representation, and still incorrectly dismisses general shift leakage;
it does not establish the single right-shift counterexample. Exercise
113 uses compound masked expressions and overlooks intermediate-value
requirements. Exercise 213 corrects its own byte-at-a-time recurrence,
not the book's load offsets. Exercise 216 is unfinished. These pages
are novelty leads, not evidence of mathematical correctness.

No matching prior error report was found in these checked sources.
Absolute priority is not established.

The cited [Eppstein subset-sum post](https://11011110.github.io/blog/2008/03/22/missing-subset-sum.html)
was also opened. Its word-width premise uses the real logarithm of the
number of inputs, which for an integral width implies the ceiling,
unlike the book's floor-logarithm function. The post and its short
comments do not report the book's precision defect.
