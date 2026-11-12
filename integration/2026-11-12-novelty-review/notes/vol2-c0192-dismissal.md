# V2-C0192: dismissed after checking the printed coefficient

Publication review, November 12, 2026. The proposed coefficient correction
in answer 4.6.1–2 on page 672 is a false positive. Both the existing page
image and a fresh rendering directly from the inventoried DjVu clearly
print `x^3+3x^2+4x+6`. They agree with the coefficient list `(1,3,4,6)`.
The earlier report incorrectly attributed `x^3+2x^2+4x+6` to the book.

The arithmetic in the old report correctly distinguishes those two
polynomials, but cannot establish which polynomial was printed. The
verification script encoded the misreading as a constant rather than
checking the source. The actual printed gcd divides both inputs and has
the stored Bézout certificate modulo 7.

The original source is `books/taocp-vol2-ed3-print1-1997.djvu`, SHA-256
`97f20229e4e06ef20e67ad30c7564dde1943611259a7fe72f2551c900b910cd1`.
File page 684 is printed page 672. The fresh rendering used `ddjvu`
at 180 percent scale. The original evidence remains
`workstreams/vol2/images/vol2-p672.png`.

The ledger/UI card is dismissed and its finding marker removed. The
old report and note receive explicit supersession notices. The script
and the affected small example result are corrected; unrelated passed
enumerations are retained without rerunning them. Copies of the five
superseded files are retained under the task's `before/c0192` directory.

The four relevant official errata layers were checked in the surrounding
polynomial block. Public searches for Knuth/TAOCP, page 672, polynomial
gcd and the coefficient strings do not override this direct source
evidence. No novelty judgment can turn the misread statement into a
book error.
