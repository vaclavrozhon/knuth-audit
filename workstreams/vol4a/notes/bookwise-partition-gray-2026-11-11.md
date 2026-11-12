# Partition Gray codes, majorization and applications

Reviewed main 405 from the Gray-code subsection through Theorem S on 407, exercises 54–73 on 412–415, and answers 755–761 through answer 73. Section 7.2.1.4 is complete under the audit's stated exceptions.

Checked the Gray recursions by partitioning their outputs according to the largest parts and checking their endpoints. The L(4,6) obstruction, shortened path and L(3,5) replacement agree with the proof. All eight patches in answer 60 restore the omitted partitions using single-dot moves at both splice boundaries. Read the conjugation symmetry argument and the displayed small paths.

Checked the majorization meet/join formulas, reversed conjugate order, part counts, cover description, rim rules and minimal-partition characterization. The normal-form potential and the triangular formulas agree; precise omitted-proof exceptions are listed separately. Algorithm M's successor and majorization updates were checked with zero-extended input partitions and t_j=0 beyond u_1, as specified by the preceding definition of t. M1 does not separately print assignments for that zero tail; this was not promoted to a finding because it depends on treating the mathematical table definition as an initialization convention. Its t_1=0 assignment is an intentional termination sentinel.

Checked Gale–Ryser's necessary sums and one-transfer sufficiency step, the Muirhead symmetrized difference, the binary-partition recursion and K's nine detailed cases, finite-abelian-group factorization construction, P-partition descent offsets and generating function, perfect partitions by mixed radices, maximum-product transfers, and the sum/product sieve's parameter identity. Checked the Bulgarian-solitaire diagonal action and cycle classification with the corrected potential, the predecessor criterion, and the occurrence-swapping bijection in answer 73.

F0087 corrects the parity test in K5's explanatory sentence; F0088 corrects the decreasing quantity in the Bulgarian-solitaire proof. Relevant historical and current errata were screened; known changes to answers 54, 55, 64, 70, 72 and 73 are not new findings. No mathematical program or large census was run.

Next: section 7.2.1.5 on printed 415/file 432, paired with exercises and answers from printed 761/file 778. These two shared pages remain uncertified until their new-section material is reviewed.
