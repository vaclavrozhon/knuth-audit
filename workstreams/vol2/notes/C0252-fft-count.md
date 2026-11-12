# V2-C0252: radix-four FFT multiplication count is two too large

Confirmed mathematical counting error, low impact. Read on 10 November
2026 in the third edition, first printing (September 1997), printed
page 700, file page 712, answer 4.6.4-14. The original page and an enlarged
crop were inspected; this is not an OCR error.

Let n be the exponent in the transform size N=2^n. The answer explicitly
omits multiplications by +1, -1, +i and -i. After combining adjacent
passes, it states, for even n, the exact count

    B(n) = (3n-2) 2^(n-3) - 5 floor(2^(n-1)/3).

Already n=2 gives B(2)=2, although the four-point transform uses only
additions and the free quarter-turns. In the displayed four-input
transformation its twiddle factor zeta is 1, and there are zero counted
multiplications. This is an error in the exact operation count, not in
the computed transform or its asymptotic complexity.

For the general count, put h=n/2. In a radix-four stage with block size
m=4^r, the three products have exponents j, 2j and 3j, for
0<=j<m/4. For r=1 all are free. For r>=2 the three j=0 products and
the product with exponent 2j at j=m/8 are free; there are no others.
Thus each block uses 3m/4-4 products, and there are N/m blocks. Summing
the stages r=2,...,h gives

    M(n) = sum_r (N/4^r)(3*4^r/4-4)
         = (9n-26)N/24 + 4/3
         = B(n)-2,                         n>=2 even.

For n=2,4,6,8 the counts are 0,8,76,492, whereas the printed expression
gives 2,10,78,494. The targeted integer-exponent check
`../repro_C0252_fft_count.py` confirms the stage count through n=12;
its output is `../results/C0252-fft-count.json`. It tests this concrete
discrepancy, without rerunning any earlier audit computation.

The minimal correction is to append `-2` to the displayed count. The
radix-two count and the complex addition count in the same answer are
correct. The mistake propagates to answer 53 on printed page 710:
its 1024-point radix-four comparison gives 10936 real multiplications
and 25948 real additions, using four real multiplications and two
real additions per complex multiplication. Those totals should be
10928 and 25944, respectively. The underlying complex count is 2732,
and the 10240 complex additions cost 20480 real additions.

Novelty screening: checked all2-prepre, all2-pre, all2 and err2, together
with current err2.textxt (fresh official copies and hashes in
`integration/2026-11-10-bookwise/errata/manifest.json`), and the older
second-edition errata for context. The relevant page-700 amendments
update answer 12 and add an in-place-layout comment to answer 14; none
correct this expression. Public searches for Knuth/TAOCP, page 700,
answer 4.6.4-14, FFT, radix-four, and the expression found no matching
report. This does not establish absolute priority or verify a later
physical printing. No report has been sent.
