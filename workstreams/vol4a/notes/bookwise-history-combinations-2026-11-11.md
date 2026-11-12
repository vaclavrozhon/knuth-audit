# Historical combination generation

Reviewed main 494 from Ramon Llull through the Narayana discussion on 500, stopping before Permutable poetry. Paired exercises 11–18 with answers 813–814 through 18. Shared main 500, exercise 512 and answer 814 remain pending for poetry material.

Checked the binomial counts, complete-graph and complete-bipartite interpretations in figures 64–66, and the 36-pair stair table. Decoded all twenty entries in the vertical table of figure 65, including the two defects already identified by answer 11. Case shift after t gives lexicographic 3-subsets of b,c,d,B,C,D.

Checked Schillinger's entire cycle against Poinsot's 013602561450346235124: the map x to 5x+2 modulo 7 gives exactly (13), so the universal-cycle property carries over. The additive 2 is the incorporated old erratum. Checked the divisor/product and binary-weight tables, the repeated-letter defect in van Schooten's tableaux, and both corrected tableaux in answer 13. Weights 1,4,12 encode the mixed radices 4,3,2.

Checked all groups of the 60 three-letter variations in answer 14 against the stated cyclic choice rule. Checked the prefix count binomial(m+n-j-1,n-1) in 15 and the known correction to its illustrative sum, 126+70+35+15+5+1=252. Checked the empty-combination discussion, the twelve multiset permutations in decreasing colex order and both combination representations attributed to Narayana.

Algorithm N generates bounded compositions in decreasing lexicographic order. N4 finds the last nonunit part; N5 decreases it and makes its released unit plus the removed suffix available to N2, which greedily fills the largest allowed suffix. The sentinel terminates exactly at the all-unit composition. The original N2 condition is r>=q, correcting the misleading OCR reading. Checked the 44 displayed compositions for n=7,q=3, grouped as 7+13+24 by first part.

For the nontrivial q>=2 analysis, each visit contributes one N4 test plus one for every trailing unit; hence X_n=sum(V_j,0<=j<=n). Checked its recurrence and weighted closed form. Each newly written q corresponds to a unique generated prefix, giving Y_n=X_(n-q); zero remainder corresponds to a composition ending in q, counted by V_(n-q). The generalized Fibonacci indexing and asymptotic order agree. Read the q=1 case directly as the single all-unit composition rather than applying the expression divided by q-1. Finally, 1666=MDCLXVI lists all seven Roman symbols in decreasing value.

No new finding. Next: Permutable poetry on main 500/file 517; exercises 19–22 on 512–513; answers 814/file 831 from 19.
