# Subset and superset subfamilies need an existential condition

Volume 4A, first edition, first printing (2011).
Appendix B, printed 826, the final two set-family entries.

A family is a set of sets. The subset operation selects the members S of a family F that are contained in at least one member T of a family G. The superset operation selects the members of F that contain at least one member of G.

The two set-builder descriptions on page 826 instead say, respectively, “T in G implies S subseteq T” and “T in G implies S superseteq T.” These are universal conditions, as in the nonsubset and nonsuperset entries immediately above them. They contradict both the complementary-operation equalities on the same lines and the correct existential definitions in answer 7.1.4–236(a), printed 669.

Take F={{1}} and G={{1},{2}}. The set S={1} belongs to both intended outputs, using T={1}. But both printed universal conditions fail at T={2}. Thus both set-builders give the empty family while the adjacent complementary-operation expressions give F.

Replace the two conditions by “S subseteq T for some T in G” and “S superseteq T for some T in G.” The symbolic complement equalities and answer 236(a) need no change.

Original pages 826 and 669 inspected. Screened historical/current Volume 4A errata, the related Fascicle 1 errata, and targeted public reports. The known arrow correction for minimal elements on page 826 is separate. No correction of these two quantifiers was found; absolute novelty is not established. See `../sources/front-appendices-source-check.json`.
