# Volume 2: completion under the agreed review scope

The review now covers all 774 available file pages of the 1997 third
edition, first printing: the 12 supplied frontmatter images and printed
pages 1–762. Text, exercises and answers have been read together.
The added Appendix C and registered errata exercises were also reviewed.
This is completion of the printed-argument audit defined in AGENTS.md,
not a claim to have solved the book's research problems or independently
proved every external theorem. Historical internal `partial` records
are preserved; the current page certification states their exact limits.

The 10 November continuation added C0252–C0263 (twelve finding cards),
and rejected C0244 after rereading its original inequality. No email or
external submission was made. Current official errata were refreshed
at takeover and matched the archived texts. Absolute novelty and later
physical printings remain unverified.

## Accepted existing work and completed gaps

| Material | Evidence and disposition |
|---|---|
| Frontmatter | `sequential-frontmatter-2026-11-06.md`: all supplied images and four introductory exercises; printed i and viii are missing from the supplied scan. |
| Main 1–100, answers 538–579 | `first100-completion-2026-11-07.md`: already accepted, with its page-specific exceptions retained. |
| Main 101–148, answers 580–591 | `bookwise-spectral-2026-11-10.md` and `bookwise-distributions-sampling-2026-11-10.md`: remaining spectral text and paired answers, then accepted distribution/sampling work. |
| Main 149–193, answers 591–604 | `sequential-distribution-foundations-2026-11-06.md`, `first-pass-randomness-2026-11-06.md`, `first-pass-summary-2026-11-06.md`, and their linked detailed mathematical notes. These are not accepted merely because a page was once marked read: the underlying selection, finite-randomness, cryptographic, generator and exercise arguments are retained. |
| Main 194–245, answers 604–617 | `first-pass-positional-2026-11-06.md`, `first-pass-floating-2026-11-06.md`, `first-pass-accuracy-2026-11-06.md`, the later `single-review-accuracy-2026-11-07.md`, and the linked detailed proofs/program checks. |
| Main 246–264, answers 617–623 | `double-precision.md`, `dekker-recursive.md`, `double-precision-context.md`, `benford-math.md`, `benford-context.md`, `benford-addition-experiment.md`: complete arithmetic/answer analysis and precisely scoped historical averages. |
| Main 265–333, answers 623–640 | The five `sequential-classical`, `sequential-modular`, `sequential-fast`, `sequential-radix`, and `sequential-fractions` notes dated 6 November, with their existing argument maps. |
| Main 333–379, answers 640–657 | `sequential-gcd-2026-11-06.md` and `sequential-euclid-2026-11-06.md`; forward references to averages and quotient frequencies are paired there. |
| Main 379–417, answers 657–671 | `sequential-factoring`, `sequential-factoring-cf`, `sequential-rsa`, `sequential-primality`, and `sequential-factoring-tail`, all dated 6 November. All 47 exercises are paired; the BBS backward reference to page 36 is covered. |
| Main 418–460, answers 671–690 | Existing `polynomial-basics`, `polynomial-division-basic`, `subresultants`, `sturm-cf`, `fast-sturm`, `berlekamp`, `sqrt-mod-prime`, `equal-degree`, `fast-factorization`, `integer-factorization`, `irreducibility` and their exercise/context notes as linked in coverage.json. All 5+27+41 exercises have recorded arguments. |
| Main 461–484, answers 690–697 | The existing powers/chain proof blocks and `powers-history.md`; the numerical 477–478/exercise-27 gap is closed by `bookwise-powers-gap-2026-11-10.md`. |
| Main 485–524, answers 697–719 | Existing polyeval basic/adaptation/chains/small-bounds work plus `bookwise-polyeval-main-2026-11-10.md` and `bookwise-polyeval-exercises-2026-11-10.md`. All 74 original exercises are now included. |
| Main 525–537, answers 719–725 | `bookwise-series-2026-11-10.md`; all 28 original exercises and the accepted added exercise 29. |
| Backmatter 726–762 and added Appendix C | `bookwise-backmatter-2026-11-10.md`; numerical certificates from Volume 1 reused after comparing the data. |

## Explicit limits retained from earlier records

The first-100, spectral, distribution and sampling certifications already
give their exact exceptions. They remain in force, including historical
seeds/graphs, the supplementary discrepancy bound, the global rejection
optimum and the exact sampling probe constant. The additional limits
below do not mean that the corresponding printed passages are unread.

- Section 3.5: external Loveland oscillation bound on 178, historical
  factorization timing on 176 and attribution on 158; research exercises
  17, 27 and 38 are audited as research questions, not solved here.
  Section 3.6 historical generator/TV-script experiments are not rerun.
- Sections 4.1–4.2: historical computer/source priorities and the
  specified interpretive candidates remain separate. The double-precision
  timing table and Sweeney data are workload-specific historical averages;
  no universal distribution of all program inputs is asserted.
- Section 4.3.1 exercises 20–21 are read with the upper-estimate context
  of Algorithm D; C0098 remains a wording candidate. Exercise 40's exact
  quotient construction and leading saving are covered, but a uniform
  O(n) lower-order cost for every fixed small radix is not independently
  certified. The missing shift is separately confirmed as C0099.
- Section 4.3.3 exercise 15: online optimality is a research question,
  and the exact algebraic-to-bit complexity specialization in the 2020
  addendum remains candidate C0107. Section 4.4 exercise 15's requested
  better general conversion bound is likewise not solved.
- Section 4.5.2: the precise Lehmer batch model on 346, all 40 digits
  of the binary-gcd constants, and the original million-input fits are
  not newly certified. Research in 31–33 and the additional asymptotic
  question in answer 40 are not solved. Morris's named external theorem
  is accepted within the domain recorded in `gcd-research.md`.
- Section 4.5.3: the stronger fixed-denominator assertion in answer 30,
  normalized empirical conjecture in 35, supplementary Kempner
  transcendence assertion in 41 and the exact optimality/practical
  threshold in 46 are not independently re-proved. The stated external
  spectral, Porter, Lochs and other analytic inputs retain their domains.
- Section 4.5.4: the AKS pretest simplification remains candidate C0155;
  historical benchmarks, world-record chronology and large external
  prime counts retain the limitations in the five sequential notes.
  Exercises 16, 21, the research extension of 24, 33 and the speed
  extensions of 40 are not solved. The fixed-word witness search in
  answer 27, optional early-stop interpretation in 37 (C0175), cited
  unconditional improvement in 45, and replacement 318-digit challenge
  in 47 retain their recorded limitations. No factorization run was
  restarted. Cryptographic hardness and physical security are hypotheses,
  not results established by this audit.
- Sections 4.6.1–4.6.3: external analytic density results, historical
  sources explicitly unavailable in `polynomial-history.md` and
  `factorization-history.md`, the original 1895 chain response, historical
  Russian-method attribution, external exhaustive chain minima and open
  Scholz-type questions are not newly resolved. Their printed use and
  the available arguments were reviewed.
- Sections 4.6.4–4.7: the new block notes specify external complexity,
  tensor-rank, analytic-asymptotic and historical limits. Open rank and
  optimality questions remain open. No implicit claim to independently
  reproduce every cited paper is made.
- Backmatter: missing frontmatter pages, source-level personal names,
  foreign-script spellings, the complete history of attributions, and
  every indexed occurrence are not independently certified. The index
  and glossary have nevertheless been read throughout.

Under the user's current instructions these are permitted, explicit
exceptions. There is no remaining unread range in the supplied Volume 2.
The next book is Volume 3, resuming after the existing Quicksort work.
