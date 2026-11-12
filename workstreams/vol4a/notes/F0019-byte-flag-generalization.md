# V4A-F0019: the byte-flag characterization fails for an arbitrary constant

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), answer 7.1.3-94, second paragraph, printed page 598 / file
page 615. Original: `images/bookwise-p598.png`.

Formula (90) computes

    t = h & (x - l) & ~x,    h = #8080808080808080,

using 64-bit words. The second paragraph of the answer allows l
to be any word, with bytes l_j, and asserts that byte t_j is
nonzero exactly when the prefix (x_j ... x_0) is smaller than
(l_j ... l_0) and x_j < 128. Bytes are numbered from the right.

Take x = 0 and l = #00000000000000ff. For j = 0 the two asserted
conditions hold: 0 < 255 and 0 < 128. But the least significant
byte of x - l is 1, so

    t_0 = #80 & #01 & #ff = 0.

The incoming borrow b_j satisfies b_j in {0,1}, and the actual
byte of the difference is (x_j - l_j - b_j) mod 256. Thus the
correct general condition is

    x_j < 128 and 1 <= l_j + b_j - x_j <= 128.

The printed prefix inequality accounts for the lower bound but
not the upper bound. A large borrow can leave the byte's high
bit clear. This finding concerns the claimed arbitrary-constant
generalization; it does not refute the original zero-byte test,
whose constant has every byte equal to 1.

The five relevant errata layers were screened, including the
adjacent replacements for answers 96 and 98. No correction to
this paragraph was found. Fresh official files match the archived
copies. Targeted public searches found no matching report, which
does not establish absolute novelty. See
`sources/byte-flag-source-check.json`. The counterexample is a
single-byte calculation, checked by hand.
