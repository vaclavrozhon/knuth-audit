# Publication review: C0147–C0170

Reviewed November 12, 2026. All 21 baseline-confirmed cards in this range
remain supported, with the limits below. The original pages 389–390,
394, 397–398, 400, 405, 409, 412–415, 417, 658–661, 663–664 and 670
and the relevant replacement passages were visually checked. The four
applicable official errata layers were compared against the November 12
refresh. Candidates C0149, C0155 and C0164 are outside this recheck.

| Card | Assessment and limits |
| --- | --- |
| V2-C0147 | With N=2 and M=1, the table is empty after the 2001 corrections, but S1 sets j=1 and S2 accesses X[1]. The original version also outputs 3 outside the requested range. An early return for N<=3 or the appropriate table-size precondition fixes this minor boundary defect. |
| V2-C0148 | The journal volume for Mertens's 1874 article is 78, not 76. The original article's page 49 footer explicitly identifies volume LXXVIII; pages 46–62 and the year are correct. |
| V2-C0150 | The complementary product index must be r+1-k, not r-k. For r=2 the printed expression uses m1 squared and omits m2. The permitted N=31, m1=3, m2=5 example gives a different residue, so this is not a harmless reindexing. |
| V2-C0151 | A circular bit table occupies lcm(m,30)/30 MIX words. The prose restores an underflowed word index by the bit count lcm(m,30). For m=7 this produces index 209 instead of 6 in a seven-word table. The program's M constants already count words; retain as an explanatory-unit defect. |
| V2-C0152 | At 6144 million tests per second, 256 tests take 41.6667 ns, not 5.2 ns. Lukes's thesis confirms 32 chips, eight tests per chip per clock and a 24 MHz clock. The 5.2 ns figure instead corresponds to 32 tests. The separate AND correction does not repair the conversion. |
| V2-C0153 | The 2005 replacement's quantified integer is visibly z, although z is the polynomial indeterminate and the bound belongs to the integer a. Retain only this variable typo; this card does not certify all hypotheses of the abbreviated AKS theorem. |
| V2-C0154 | Multiplying both sides of a strict probability inequality by the nonprime indicator produces 0<0 when n is prime, for example n=3. Non-strict inequality repairs that displayed comparison. The intended overall probability bound is unaffected. |
| V2-C0156 | For n=9 and N=12, the claimed intermediate estimate gives 6<=21/4. The final incomplete witness row has zeros at 8,9,10. Retaining the minus one and bounding the incomplete block by min(b_n,r) repairs the estimate and proves the desired theorem. The exercise explicitly uses 1<n, also resolving the answer's extraneous n=1 row. |
| V2-C0157 | The stated generalized criterion permits k=1,n=1,N=3, but its base-three residue is zero, not minus one. Add N>3. The actual exercise's family 5*2^n+1 is unaffected; this is a boundary exception in the more general answer. |
| V2-C0158 | Algorithm E stores a convergent numerator reduced modulo N; that value cannot be substituted into the exact integer norm identity. In the printed N=197209 row, P=159316 and V=720 would force an impossible integer denominator square, whereas the full numerator 750943 and denominator 1691 satisfy the identity. The congruence and algorithm remain correct. |
| V2-C0159 | The completeness argument for Algorithm F needs factor-base elements relatively prime to N, a condition not imposed on Algorithm E's stated inputs. The stored six-row N=155,k=29 example causes F to discard its basis solutions despite a useful dependency yielding gcd(116-101,155)=5. The printed setup was checked for hidden preconditions. Removing base factors first repairs it. The associated probability answer also needs odd N and invertibility; these are present in the later Dixon setup, not the earlier claim. |
| V2-C0160 | The proposed Lucas precheck exception omits equality: P=1,Q=-1,N=5 gives gcd(QD,N)=N with abs(QD)=N. It also needs to handle QD=0. Use the actual gcd=N exception. This does not refute the main Lucas primality criterion. |
| V2-C0161 | The example asks the fixed-base-two method to recover a factor of 2^214+1, but its first-stage exponent is divisible by 428, making the residue one modulo the entire input. Even the stated remaining two-factor cofactor has order 428 at both primes, so every base-two gcd is trivial. The stored exact certificate and repair with base three support the finding; no new large factoring run was needed. |
| V2-C0162 | The discovery year for the Mersenne prime with exponent 216091 is 1985, not 1984. The discoverer's preserved 1996 announcement explicitly identifies 1985. Retain the year correction only; this card makes no day-level priority claim. |
| V2-C0163 | The 2019 erratum prints exponent 77232017 instead of 77232917. GIMPS's January 3, 2018 announcement gives the latter and the December 26, 2017 discovery date. The wrong exponent equals 19*29*140167 and therefore cannot define a Mersenne prime. |
| V2-C0165 | Congressus Numerantium volume 12 was published in 1975, as its publisher's archive confirms. The book gives the 1974 conference year as the publication year. The title and volume identify the intended proceedings. |
| V2-C0166 | For safe primes p=23,q=47 and exponent m=22, the root fraction is 44/1081, exceeding 1/253 although 253 does not divide m. The exact count is gcd(m,p-1)*gcd(m,q-1). The small product bound requires both individual large factors to be absent; their product merely failing to divide m is insufficient. |
| V2-C0167 | With N=55 and M=floor(cuberoot(N))=3, the branch x>=M leaves x=3 unpadded, and ciphertext 27 reveals its integer cube root. The 2004 correction to the padding range's upper endpoint is separate. The stored ceiling-and-disjoint-ranges repair addresses this particular low-message defect and is not a claim of modern cryptographic security. |
| V2-C0168 | Håstad's chapter in LNCS 218 was published in 1986, as the publisher record and original chapter footer/copyright show. The book uses the 1985 conference year. |
| V2-C0169 | The norm-composition identity needs a plus sign in x1*x2+a*y1*y2 when the second coordinate is x1*y2+x2*y1. With a=2 and both input pairs (1,1), the printed output has norm -7 instead of 1; the corrected output (3,2) has norm 1. The error appears both in the hint and Fact 2. |
| V2-C0170 | Fact 3's lattice estimate omits a factor abs(m), the lattice determinant's scale. With a=2,s=17,z=6,m=2, the minimum of (6u+2v)^2+2u^2 is 2, exceeding sqrt(8/3). The corrected bound is abs(m)*sqrt(4*abs(a)/3). After division by abs(m), the intended bound on t and the final theorem still follow. |

The own reports and detailed proofs were reread, including the witness
matrix repair, the factor-base counterexample and the exact Pollard
certificate. This is a review of the listed claims, not a claim that all
historical hardware performance or every proposed cryptographic use has
been independently reproduced.

Public checks included combinations of Knuth/TAOCP, the page or exercise,
and: sieve empty range, sieve pair index, sieve word wrap, 6144, 5.2,
41.7, AKS quantified variable, primality error indicator, witness matrix,
Proth three, reduced convergent norm, factor-base coprimality, Lucas gcd,
23528569104401, 41231, Mersenne 216091, 77232017, Selfridge Wunderlich,
RSA root density/padding, Håstad year, Fact 2 norm sign and Fact 3 lattice.
No matching public report of these particular book/erratum errors was
found. Absolute priority is not established.

Primary sources used or cross-checked:

- [Knuth's current Volume 2 errata](https://www-cs-faculty.stanford.edu/~knuth/err2.ps.gz),
  [older layer](https://www-cs-faculty.stanford.edu/~knuth/all2.ps.gz),
  [earlier layer](https://www-cs-faculty.stanford.edu/~knuth/all2-pre.ps.gz),
  [earliest third-edition layer](https://www-cs-faculty.stanford.edu/~knuth/all2-prepre.ps.gz).
- Mertens's 1874 original, locally inspected page 49; Lukes's 1995
  thesis, printed pages 38 and 41, and the 1996 pseudosquares paper,
  printed page 366. Source identifiers remain in the original card notes.
- [Noll's preserved prime announcement](https://www.isthe.com/chongo/tech/math/prime/prime_press.html).
- [GIMPS announcement for exponent 77232917](https://www.mersenne.org/primes/?press=M77232917).
- [Congressus Numerantium publisher archive](https://combinatorialpress.com/cn/archive/).
- [Håstad's publisher record](https://link.springer.com/chapter/10.1007/3-540-39799-X_29).
- [Hellman's 1995 lecture notes](https://www-ee.stanford.edu/~hellman/pkc.pdf),
  page 8, discuss a suspected complexity-constant error on page 383 of
  the second edition. The passage concerns optimizing a subexponential
  factoring bound, not the integer norm identity, invertibility condition
  or fixed-base Pollard example reviewed here. It is not a duplicate of
  C0158, C0159 or C0161.
