# Spectral test: accepted review and dismissal of C0244

10 November 2026. Volume 2, third edition, first printing (1997).
Printed page p is file page p+12. The detailed 6 November reviews of
the spectral foundations, numerical examples, extensions, discrepancy,
and history have been read and accepted under the current review policy.
This accepts documented earlier work; it does not claim a new complete
reading of every original page or a rerun of the archived computations.

## C0244 was an audit misreading

Original printed pages 583–584 were read again, with page 584 inspected
visually in the scan. Its first paragraph explicitly compares two
different products; it does not identify their minimizers.

Here m is the modulus, a is the multiplier, and A is the largest partial
quotient of a/m. The preceding paragraph chooses q and p to minimize
q|aq-mp|; write q'=|aq-mp| for the second factor at that minimum.
The next paragraph chooses u to maximize r(u)r(u'), where u' is the
least positive absolute residue of au modulo m and
r(j)=1/(m sin(pi*j/m)) for 0<j<=m/2. The printed argument states

```
uu' >= qq',       A/m <= 1/(qq') <= (A+2)/m.
```

Together with r(j)<=1/(2j), these give exactly the printed chain

```
r_max <= 1/(4uu') <= 1/(4qq') <= (A+2)/(4m).
```

The earlier audit incorrectly attributed the interval for 1/(qq') to
1/(uu'). Its example m=49, a=15 has products 12 and 13 and is fully
consistent with the stated inequality 13>=12. No optimizer identity is
required. The lower bound uses the minimum-product witness and the
other sine inequality, as already explained in the accepted review.

C0244 is therefore **dismissed**, not an unresolved book defect.
Exercise 3.3.4–30 has no remaining gap from this candidate. The old note
and numerical files remain as historical evidence; no search was rerun.

## Coverage and precise exceptions

The accepted notes cover the rest of the main section, printed 101–118,
and answers 580–584. Answers 3.4.1–1 to 3 sharing page 584 were also
read directly and compared with `sequential-distributions-ab-2026-11-06.md`.
No unread portion of that shared page is being certified.

- C0042 remains a question about unspecified coarse rounding in Table 1,
  not a demonstrated incorrect lattice minimum.
- C0243 is read in the periodic-lattice setting explicitly introduced
  immediately afterward; it establishes no algorithmic error.
- Exercises 22, 23 and 31 contain research questions. Their statements
  and printed discussion were reviewed; their open general problems
  are not being solved or represented as solved.
- Historical benchmark timings, global multiplier searches, unrecorded
  experiments, and historical priority are not reproduced. In particular,
  claims on pages 102, 105 and 107 about typical intermediates, empirical
  tests and historical adoption retain those limitations.
- Previously checked finite numerical certificates and computations are
  reused. No new exhaustive search or independent proof of externally
  quoted standard theorems is claimed. Unavailable bibliography remains
  limited exactly as listed in the accepted history and numerical notes.

No new book error was found in this block. The next block is section
3.4.1 from printed page 119, with its paired exercises and answers.
