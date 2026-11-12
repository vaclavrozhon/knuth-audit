# V3-C0046 — The shuffle answer changes t to an undefined r

Confirmed in volume 3, second edition, first printing (1998), answer
5.3.4-13, printed p.667, file p.678. The network has 2^t lines, and its
shuffle rotates the t binary address bits. The displayed sequence of
exclusive-or masks is printed as

```
2^(r-1), 2^(r-2), ..., 1, 2^(r-1).
```

All three occurrences of r should be t. No r is defined in exercise 13
or its answer. In the original wire coordinates, the first adjacent
comparisons after the shuffle pair addresses differing in their most
significant bit; successive rounds rotate this mask through the t bits.
For example, at t=4 the masks are 8,4,2,1,8.

The original typography was visually checked, including an enlarged
crop; see `images/bookwise-p667.png`. This is not an OCR substitution.
The official change of "alternatively" to "alternately" in this answer
does not correct the parameter. All five errata layers were screened in
`sources/networks-errata-review.json`; targeted public searches found no
matching parameter correction. No absolute priority claim is made.
