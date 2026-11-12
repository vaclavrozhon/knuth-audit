# C045 — a zero-mass fiber in the pointwise formula for conditional expectation

Status: **dismissed**, contextual clarification. Location: Volume 4B,
printed p.3, Eq.(13), file page23. Reassessed on 6 November 2026.

The earlier zero-event convention already completes the pointwise
definition. The text introduces the random-variable notation as a
rewriting of Eq.(11), rather than as a replacement of the earlier
conditional expectation. There is no textual basis for discarding that
convention in Eq.(13). The fully explicit reading is the quotient on
positive-mass fibers and EX on zero-mass fibers. It is consistent on
every atom and proves the tower identity. No candidate card is retained.

The book permits atoms with probability zero in Eq.(1). It defines a
random variable as a function on every atom. At the top of p.3, it
explicitly sets E(X|A)=EX when P(A)=0. Later on the same page, Eq.(13)
gives E(X|Y)(ω) as the weighted sum over the fiber Y=Y(ω), divided by
the probability of that fiber, without repeating a nonzero condition.

Consider Ω={a,b}, with p(a)=1 and p(b)=0, and X(a)=Y(a)=0,
X(b)=Y(b)=1. The earlier convention gives

```
E(X | Y=1) = EX = 0.
```

At ω=b, however, the numerator in the displayed quotient is 0 and its
denominator P(Y=1) is 0. Thus the raw quotient is 0/0, not a defined
real number. At ω=a the quotient is correctly 0. This is an exact
two-atom example; no numerical computation or sampling is involved.

The initial suspicion isolated the quotient from its defining context.
Applying the earlier zero-event convention to Eq.(13) gives the correct
pointwise conditional expectation. In addition, because Ω is
countable, the union of all zero-mass fibers has probability zero;
arbitrary finite values there do not change any expectation. The tower
identity (12) and the positive-support bit-vector example (14) remain
valid. There is no counterexample here to the underlying theorem.

A fully explicit transcription of the existing definition uses the quotient when
P(Y=Y(ω))>0 and EX otherwise, consistently with the convention already
printed on the page. Repeating the condition could improve readability,
but its omission here is not sufficient grounds for an erratum.

Both the original 4B PDF page and the author's Pre-Fascicle5A printed
p.3 show this same wording. The draft page is dated 11 September2019.
The six local public errata layers err4b/all4b, err4f5/all4f5 and
err4f6/all4f6 were searched; no matching correction was found. The
nearby known amendment to Eq.(9) on p.2 does not address this question.
This is not a claim of novelty, priority, or examination of a physical
copy.

Evidence, relative to the repository root:

- `audit-2026-10-31/images/sequential/file-021.png`
- `audit-2026-10-31/images/sequential/file-023.png`
- `audit-2026-10-31/images/sequential/fasc5a-09.png`
- `audit-2026-10-31/sources/fasc5a-manifest.json`
- `audit-2026-10-31/results/sequential/mpr-001-003-errata.json`
- `audit-2026-10-31/notes/sequential-mpr-001-003.md`
