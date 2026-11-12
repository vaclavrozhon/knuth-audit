# V2-C0256: sum of ranks printed instead of rank of the sum

Confirmed notation error, low impact. Third edition, first printing,
printed page 711, file page 723, answer 4.6.4-56, final paragraph.
Original typesetting inspected on 10 November 2026.

Let T be the tensor of the original bilinear forms and let R be its
embedding into quadratic forms, as defined in the answer. Let R^swap
denote R with its first two indices interchanged. The argument needs

    rank(R + R^swap) >= rank(T).

Deleting the indicated rows of the first two realization matrices
does prove this: it restricts R+R^swap to T. Combined with the previous
paragraph's lower bound of half rank(R+R^swap), it gives the exercise's
claimed lower bound of half rank(T) on chain multiplications.

Instead, the printed line has

    rank(R) + rank(R^swap) >= rank(T).

That inequality is true, but does not supply the needed comparison
with rank(R+R^swap). The following prose already names the correct
sum tensor, so this is a local misplaced-parentheses error, repaired
by moving the sum inside a single rank. The theorem remains correct.
The question's separate `x_i x_k` typo is already officially corrected
to `x_i x_j` and is excluded from this finding.

Checked all four relevant official errata lists and current TeX, plus
the older second-edition list. No corresponding answer-56 correction
was found. Public searches on the exercise, tensor rank and the
printed rank-sum expression found no matching report. Absolute
priority and later physical printings are unverified. No report sent.
