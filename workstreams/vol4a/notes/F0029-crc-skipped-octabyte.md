# V4A-F0029: The CRC loop skips its second input octabyte

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), printed page 620 / file page 637.
Original: `images/bookwise-p620.png`.

The code starts with nn=-n, and data points just after the input.
For n=16, the first LDOU reads data-16. The following ADD changes
nn to -8. At label 1H, the next ADD changes nn to zero before the
second LDOU, so that load reads data rather than data-8. The second
input octabyte is never read.

Choose a 16-byte message with fifteen zero bytes followed by 01,
and let the eight readable bytes after the message be zero. Both
loads made by the printed routine then yield zero, so every matrix
operation and the finishing code yield CRC zero. Formula (180)
requires the remainder of x^16 modulo x^16+x^15+x^2+1, namely
x^15+x^2+1, represented by hexadecimal 8005.

Move the ADD inside the loop to immediately after its LDOU. Keep the
initial ADD in place. The next unconsumed word is then loaded before
nn advances, and the loop-end sign test still counts the remaining
words correctly. This changes no matrix constants or operation count.

The original page image and the relevant current/historical Volume 4A
and Fascicle 1 errata were checked. No matching correction or public
report was located; absolute novelty is not established. See
`sources/bitwise-tail-source-check.json`. The short calculation above
was checked by hand, without a general verifier or census.
