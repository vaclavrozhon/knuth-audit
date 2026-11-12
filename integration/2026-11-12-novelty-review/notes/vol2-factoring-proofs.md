# Publication review: C0171–C0186

Reviewed November 12, 2026. All 15 baseline-confirmed cards in this
range remain supported. The original pages 381, 399, 407, 414–417,
663, 665–671 and the relevant replacement passages were visually
checked. The four applicable official errata layers refreshed on
November 12 were compared. C0175 is a candidate outside this scope.

| Card | Assessment and limits |
| --- | --- |
| V2-C0171 | For n=7,a=3,b=1, sampling both coordinates from 1 through 6 yields counts 4,4,8,4,8,8 for the six nonzero norms; all gcd prechecks pass. Fact 2 counts all residue pairs, including zero coordinates, and cannot prove the claimed uniformity for this sample space. Sampling all residues with a suitable gcd branch repairs it. This does not by itself disprove efficiency. |
| V2-C0172 | The no-solution example modulo 8 is correct for x squared plus y squared, but false for the printed plus-or-minus: 2 squared minus 1 squared equals 3. Replacing the sign by plus preserves the intended illustration of the odd-modulus restriction. |
| V2-C0173 | The discrete-log reconstruction multiplies relation coefficients by e_jk instead of the original exponents n_i. The single relation 3 squared equals 2 modulo 7 gives the printed logarithm one instead of two. The coefficients must also be shared across coordinates: sum_i c_ik*e_ij+(p-1)t_jk=[j=k], followed by N_k=sum_i c_ik*n_i modulo p-1. The 1998 correction to the final modulus does not fix either issue. |
| V2-C0174 | Page 399 defines r as a floor, while the page 665 expansion has a vanishing remainder and silently drops its fractional part. The stored family with rho=k+1/2-o(1) and c tending to one disproves that precision. The resulting logarithmic timing error is t*(ln(m)-ln(rho))+O(1/rho), too large for the stated O(ln ln N) remainder. The own proof recovers the final optimized expression by choosing integer r first and tuning m; this remains an estimate within the book's heuristic model. |
| V2-C0176 | For n=35, s=5,s'=8,m=8 satisfies the stated initial binomial residues. The corrected Fibonacci update moves m to 11, whose new upper endpoint 14 has residue 20 modulo 35 rather than zero. The base is large enough to exclude coefficient carries. Restricting the search to the factorial-coprime interval repairs the invariant. This is a proof defect, not a claim that the trajectory ultimately returns a wrong factor or that Shamir's theorem fails. |
| V2-C0177 | In L2 the denominator for mu must contain v1, not v3. For N=14,r=1,s=3, the reachable pair (v1,v3)=(2,1), k=0 and sigma=-1 makes the printed formulas output 4 as a divisor of 14. The correct denominator instead gives mu=1/2 and rejects it. Direct quadratic elimination independently gives the correction. |
| V2-C0178 | The auxiliary assertion sqrt(lambda*mu*v)<=floor(sqrt(N/s)) fails for N=36,r=1,s=5 and lambda=mu=1: sqrt(5)>2. A ceiling makes the proof valid with the same asymptotic bound. Retain this inequality defect only; the stored small-input checks do not establish that keeping the floor causes a missing divisor. |
| V2-C0179 | The exercise sums complex integrals only over zeros in the upper half-plane and omits their real parts. The reread proof derives divergence i*log(T)/(2*pi*k)+constant+o(1) at x=p^k from Landau's unconditional formula and integration by parts. Thus an O(1) term cannot absorb the error. Take real parts before the limit or sum conjugate zeros symmetrically. The classical convergence theorem remains an explicitly cited external input. |
| V2-C0180 | The book counts primes with p<=x, explicitly giving pi(2)=1. Consequently its prime-power counting function is the symmetric explicit-formula value plus 1/(2k) at x=p^k, not minus. At x=2 the printed correction gives zero instead of one. The 2011 n-to-x correction is separate. This concerns the exact remainder description, not the unspecified O(1) bound. |
| V2-C0181 | Keller's article on pages 661–673 belongs to Mathematics of Computation volume 41 (1983), as its first-page heading confirms. The book groups it under volume 40 with a different article. The later citation to volume 45 and the historical candidate count are not disputed by this card. |
| V2-C0182 | G_j contains a product alpha_t*j*beta_t where alpha_t+j*beta_t is needed. The following floor identity already has the plus sign. The permitted exact m=209 example changes the floor from -1 to 0 and can reverse a vote. This is visible in the typesetting, not an OCR artifact. |
| V2-C0183 | Q_m explicitly includes nonunits, and uniformly squaring residues does not sample it uniformly. For m=209 the stored predictor succeeds on 31/60 of uniform Q_m but only 93/209 of the printed samples, so the majority in part (a) can favor the wrong answer. The gcd-based repair transfers advantage to units or finds a factor. Merely restricting samples to units without transferring the premise is insufficient. The existence of the intended reduction is not refuted. |
| V2-C0184 | Z_j compares the oracle with lambda(u) even when chi(u) is negative, although the canonical root then requires lambda(-u). The signed vote Y_j already handles this correctly. With a perfect oracle, the printed mean on units is nonpositive; for m=209 it is -2/45, while the repaired mean is 37/90. The known published correction about pairwise independence is a different issue. |
| V2-C0185 | The book's stages begin at zero and still predict two new bits there. Its subsequent geometric error sum begins at one. For r=8 the listed bounds over all actual stages sum to 19/18, exceeding 8/9. This invalidates the displayed derivation, not necessarily the true success probability. Constant-factor larger samples and a finer initial grid repair it. The cited paper starts its different RSA loop at one. |
| V2-C0186 | The original 1644 Latin visibly says saeculum integrum, an entire century or age, rather than all time. Replacing the book's translation by an entire century follows the original and the earlier Kravitz translation. This is a translation correction, not a new primality result or a claim to have reconstructed every historical detail in the paragraph. |

The detailed own arguments for the floor estimate, residue-class
algorithm, explicit formula and BBS reduction were reread. Existing
large successful enumerations were not repeated. The short counterexamples
above establish the individual defects independently of those enumerations.

Public searches combined Knuth/TAOCP and the relevant exercise/page with
norm uniformity, discrete-log reconstruction, Lenstra denominator,
Fibonacci/Shamir invariant, factoring floor, Riemann real part and minus
half-jump, BBS/Fischlin errors, Keller volume, and the Mersenne phrases
“all time would not suffice” and “saeculum”. No matching prior report of
these particular book errors was located. The translation is repeated in
other books and lectures; repetition is not a prior report of the error.
No absolute priority or unseen later physical printing is certified.

Primary sources and resolved leads:

- [Current Volume 2 errata](https://www-cs-faculty.stanford.edu/~knuth/err2.ps.gz),
  [all2](https://www-cs-faculty.stanford.edu/~knuth/all2.ps.gz),
  [all2-pre](https://www-cs-faculty.stanford.edu/~knuth/all2-pre.ps.gz),
  [all2-prepre](https://www-cs-faculty.stanford.edu/~knuth/all2-prepre.ps.gz).
  The 1998 changes on 670/671, 2000–2001 changes on 416/668/669,
  2002 update on 666, 2004 change to answer 35 and 2011 change on
  663 were specifically distinguished from these findings.
- [Fischlin–Schnorr, 2000](https://link.springer.com/content/pdf/10.1007/s001459910008.pdf),
  original pages 226–227 and 241 freshly inspected. Page 227 credits
  Knuth with finding a lack of pairwise independence in earlier error
  variables. The book already enlarges the bad event to the boundary
  strips; C0184 is the separate missing sign. Page 241 uses unit
  quadratic residues and explicitly reverses the bit for a negative
  square class. Page 226 starts the RSA loop at one, unlike the book's
  BBS loop. The theorem and standard reduction are not claimed new.
- [Lenstra, Divisors in Residue Classes](https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1984b/art.pdf),
  primary source preserved and analyzed in the existing note.
- [Shamir's original report](https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TM-091.pdf),
  whose binomial test is restricted to the relevant factorial interval.
- [Gonek's statement of Landau's formula](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/8-landau-form.pdf),
  first page freshly inspected; no Riemann hypothesis is needed there.
- [Von Mangoldt's original](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0114/LOG_0020.pdf),
  pages 295 and 299–301 freshly inspected: midpoint convention,
  paired contributions, and their integral branches.
- [Keller, 1983](https://doi.org/10.1090/S0025-5718-1983-0717710-7),
  original first page freshly inspected.
- [Mersenne, 1644, library copy](https://doi.org/10.3931/e-rara-15453),
  [original scan 28](https://www.e-rara.ch/i3f/v20/3294247/full/1800,/0/default.jpg)
  freshly inspected at the end of section XIX.
- [Hellman's lecture notes](https://www-ee.stanford.edu/~hellman/pkc.pdf),
  page 8, question an optimization constant for the second-edition
  main-text bound. That is distinct from C0174's omitted floor and
  claimed vanishing remainder in answer 36.
- A search hit in Flajolet–Gourdon–Panario's *The complete analysis of a
  polynomial factorization algorithm over finite fields* corrects error
  terms in another paper's Theorems 1 and 2. The indexed passage does
  not report C0174. Full follow-up access was intermittent; no stronger
  claim about that paper is made here.
