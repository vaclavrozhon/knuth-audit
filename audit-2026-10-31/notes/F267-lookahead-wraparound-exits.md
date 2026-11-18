# F267 — Disabling wraparound jumps beyond the candidate arrays

**Location:** Volume 4B, first edition, second printing (2022), exercise
7.2.2.2–173(ii), printed page 331 (file page 351). Compare Algorithms X
and Y on pages 228 and 230.

The exercise proposes disabling repeated passes through the lookahead
candidates by changing the end-of-pass cases in X7 and Y4 to go directly
to X6 and Y3. Both destinations immediately read an array entry whose
index has just reached the array's length.

The arrays `LL` (candidate literals) and `LO` (truth offsets) have entries
indexed `0 <= j < S`, as explicitly stated in X4. In X7, after incrementing
the index from `S-1` to `S`, the proposed jump to X6 executes

```text
l = LL[S]
T = BASE + LO[S]
```

Those entries are not defined. In exactly the same way, Y4 increments
its index `j_hat` to `S`, and the proposed jump to Y3 immediately reads
`LL[S]` and `LO[S]`. Neither step performs an end test before the reads.

This boundary is an ordinary end of a candidate pass, not an empty-input
case. For example, a single ternary clause `x OR y OR z`, initially with
no assigned variables, has six singleton candidate components and no
contradiction. During its first X pass, the recorded last-change index
cannot equal the newly incremented index before the end of that pass.
The proposed change therefore reaches the invalid index 6. No full
solver execution is needed to verify these control-flow destinations.
The boundary error remains after correcting the independent X2
initialization subscript defect already recorded as F206.

**Correction:** On the first `j=S` in X7, terminate Algorithm X normally.
On the first `j_hat=S` in Y4, go to Y6. The Y6 finish step must still run:
it installs the learned binary implications and restores the context
used by Algorithm X. Resetting the indices to zero and continuing would
retain the wraparound that the exercise asks to disable.

This is an error in the exercise's implementation instructions. The
unmodified Algorithms X and Y have the required boundary handling. The
historical timing results in answer 173 have not been rerun or refuted.

Original pages 228, 230, and 331 were inspected. The September 23, 2015
Fascicle 6A draft has the same erroneous destinations on page 147 (file
page 155). The archived author's `sat11.w` also uses the bounded scans
`looki < looks` and `dlooki < looks`, and a separate double-lookahead
finish path; it was read, not executed.

All six current/historical errata text layers and the three official TeX
sources were checked. Published changes to the neighboring algorithms
and exercise 176 do not repair this instruction. Focused public searches
returned the original passage and unrelated material, but no matching
correction. Absolute priority is not established. Source hashes and
searches are recorded in `../results/focused-wraparound173-sources.json`.
