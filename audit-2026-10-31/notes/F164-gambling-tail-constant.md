# F164 — Missing factor sqrt(2) in the tail asymptotic of MPR68(d)

The original Volume4B answer68(d), p.380/file400, and the author’s
Pre-Fascicle5A, p.37/file43, state P(N>=n) ~ 1/sqrt(pi*n).
The correct equivalent is sqrt(2/(pi*n)). This is a local constant
error of low severity; the conclusion E(N)=infinity remains true.

## Exact contradiction, without a numerical approximation

Put q_k=binom(2k,k)/4^k. The exact probability formula in68(c),
proved independently in notes/sequential-mpr-ex067-068.md, is
P(N>=n)=q_floor(n/2).

Here is a complete proof of the needed coefficient asymptotic.
Let I_j=integral from0 to pi/2 of sin(t)^j dt. Integration by parts
for j>=2 gives I_j=(j-1)I_(j-2)/j: the boundary product
sin(t)^(j-1) cos(t) vanishes at both endpoints and cos²=1-sin².
Together with I_0=pi/2 and I_1=1, this gives, for k>=1,

    I_(2k)   = (pi/2) q_k,
    I_(2k+1) = 1/((2k+1) q_k),
    I_(2k-1) = 1/(2k q_k).

Since0<=sin(t)<=1, we have I_(2k+1)<=I_(2k)<=I_(2k-1).
Multiplying by the positive q_k and rearranging yields

    2/(pi*(2k+1)) <= q_k² <= 1/(pi*k).

Thus sqrt(pi*k) q_k tends to1. With k=floor(n/2), n/k tends to2,
so sqrt(pi*n) P(N>=n) tends to sqrt(2), whereas the printed
asymptotic would require the limit1. Both parities give the
same contradiction. No Stirling formula or numerical experiment
is assumed.

The lower bound also proves divergence of the tail sum. The
independent generating-function derivative in the full exercise
proof gives the same infinite expectation. Exact formulas in
68(b,c,e,f) are unaffected.

## Source and errata checks, 7 November2026

The full original question and answer were viewed in
images/sequential/file-038.png and ref-400.png, and compared with
fasc5a-24.png and fasc5a-43.png. The symbol n is the number of bets
before the first positive profit in both versions.

The hashed results in results/sequential/mpr-067-068-gambling-errata.json
cover all six saved layers err4b/all4b, err4f5/all4f5, err4f6/all4f6
and all three raw TeX sources, searched by page, section, exercise
and content. No applicable correction was found. Exercise68 hits
in later Life/puzzle sections and the Feller index-name correction
do not address this statement. The all4b snapshot is dated16April2026;
this is not a live refresh.

Only p.380/file400 is a finding location. The question on p.18 and
the valid visit-count result on p.381 are not error locations.
No computation, census restart or external report was made. Physical
printing, priority and independent coordinator approval are not claimed.
