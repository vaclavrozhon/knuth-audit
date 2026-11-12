# Volume 4B: F149–F172 publication review

Reviewed on 2026-11-12. All 24 cards are retained after rereading their
arguments and the original first-edition, second-printing typesetting.
Existing exact certificates and proofs were reused; no large enumeration was
restarted. The earlier notes' statements that a new live refresh had not been
done refer to their original dates: this review uses the November 12 manifest.

| Card | Rechecked reason |
| --- | --- |
| F149 | Four dashed USA graph edges have endpoints already joined by solid two-edge paths: AL–TN–MS, SD–NE–WY (twice), IN–IL–KY. The diagrams therefore omit internal edges of the induced components. Restoring them preserves every partition and the correctly stated costs. |
| F150 | Exercise 248: LEN(i) counts options containing item i, not distinct items. The printed phrase should say options. The first sentence and answer agree on that meaning. |
| F151 | The exact formula in answer 255 gives the leading term N*F_(N+1)/sqrt(5), not N*F_(N+1)/5. Indeed 1+2/phi=sqrt(5), where phi is the golden ratio. This coefficient error is independent of the one-node discrepancy F079. |
| F152 | Answer 260: the six explicit families of residual states total 6n-9 including the empty state, not 6n+9. The small n=4 instance has 15 memos rather than 33. The printed node count is correct; the update formula needs n>=4, with 46 updates at n=3. |
| F153 | Figure 123 sends 01111011 to 00101101, thereby reintroducing already covered item 6. Covering the pair {2,4} should produce 00101011. The archived vector comparison identifies precisely this wrong edge. |
| F154 | Answer 261(c): n=2 has two paths, while the printed product gives five. Its upper index must be n-1. The quoted value for P16 is actually P17; the corrected P16 is 10606175914819584. The source note uses n paths in a square of side n+1, explaining the shift. |
| F155 | Answer 262(a): one blue path follows a horizontal domino's top edge instead of its diagonal. Moving its bend from (13.5,1) to (13.5,2) repairs the local motif and preserves the rest of the path. The enlarged original was inspected. |
| F156 | Answer 262(b): the first-column entries in rows 4–7 are one too small for the displayed middle tiling. The projection from the rhombus coordinates gives 3,5,5,6, not 2,4,4,5. Both arrays separately satisfy the plane-partition inequalities; only their claimed correspondence is wrong. |
| F157 | Answer 263(g): the two Algorithm C memory entries use MB where KB is intended. The actual node and item structures give conservative bounds 904708 and 950204 bytes, below 1 MB. The precise rounded 509 and 537 KB values were not independently reproduced. |
| F158 | Answer MPR77: a process Z0=0, Zn=xi for n>=1, with xi a fair sign, is a martingale in its own history but cannot be one relative to a time-constant auxiliary sequence. Adaptedness would reveal xi already at time 0, contradicting its conditional mean zero then. |
| F159 | Answer MPR84(a) explicitly equates conditioning on the Z history with conditioning on its transformed history. For f(z)=z^2 and atoms (-1,-1),(1,0),(1,2) of probabilities 1/2,1/4,1/4, the first conditional expectation is 1 or 2, while the second is 3/2. Conditioning Jensen's inequality once more repairs the proof; the theorem is true. |
| F160 | Page 9 permits arbitrary predictable interval widths in the displayed Azuma bound. The three-atom bounded fair-increment example has tail probability 4/5, exceeding even the average of the proposed random bound. A fixed upper bound on the sum of squared widths repairs the statement. The ordinary fixed-width applications remain valid. |
| F161 | Answer MPR90(e): each individual exponential needs denominator 8, not 4. With c=sum(c_k^2)/2, the printed product's constant is exp(c*t^2/2), not exp(c*t^2/4). This is separate from the predictable-width error. |
| F162 | Answer MPR11 confuses equal distances with equal values. Independent fair signs at alpha=0 make the displayed sides 1 and 3/4. Replacing the equality by an inequality, or using the correct equal-distance event, repairs the otherwise valid argument. |
| F163 | Answer MPR38 introduces an undefined X0 in the final conditioning list, although the strings and requested prefix start at X1. The counting formula itself is correct; remove the extra variable. An arbitrary added variable could reveal the next symbol and change the conditional expectation. |
| F164 | Answer MPR68(d): the exact preceding tail formula is binom(2k,k)/4^k with k=floor(n/2), hence its asymptotic is sqrt(2/(pi*n)), not 1/sqrt(pi*n). The integral bounds in the stored proof establish the missing factor without numerical estimation. |
| F165 | Answer MPR67(c) sums Y0 through Yn, counting n+1 bets for the profit after n bets. Two initial losses make the purported one-bet profit -3 instead of -1. Sum only through n-1. Both the intended process and its shifted version are martingales. |
| F166 | Answer MPR74: the distribution is A(n+1,r-1)/(n+1)!, where A is the Eulerian number, rather than A(n,r-1)/n!. At the explicitly labelled level 1, the diagram gives 1/2,1/2 while the printed formula gives 1,0. |
| F167 | Exercise MPR82(a) asks for the transition at n=51, which requires the undefined ratio Z52=0/0. The valid transition range ends at n=50; alternatively define an explicit constant continuation. The game itself stops before that problematic transition. |
| F168 | Answer MPR83 repeats Xn-E(Xn) inside a sum indexed by k. A fair X1 in {0,1} and all later Xn=0 already violate the asserted martingale property. Both summand indices should be k. The historical correction to the subsequent stopping rule does not fix this line. |
| F169 | Answer MPR96 uses an uncentered binomial window. For the stated head count X, P(X<sqrt(n)) tends to zero, contradicting Theta(1). Replace X by X-n/2 in the window. The final classification is unchanged. |
| F170 | Answer MPR103(b): the first successor of state 012 under bit 1 is 122, not 112. The marked output-2 coefficient at two steps is 1/4 on the left and zero in the printed recurrence. The final generating function already uses the correct transition. |
| F171 | Answer MPR109(c) deletes x_i to x_j arcs from a network whose middle arcs are x_i to y_j. The target must be y_j; otherwise a full crossed flow on a two-element chain need not respect the required order. |
| F172 | The same answer needs the lower closure of the complement of J, not its upper closure. On the two-element chain with marginals (3/4,1/4) and (1/4,3/4), the printed inequality chain becomes 5/4 >= 1/2 >= 1. Reversing the closure and adjusting the subsequent closure identity repairs the cut proof. |

The current and cumulative official 4B/Fascicle 5 sources were searched by
page, content, and the historical page offsets. The MPR answer offset is 189;
the dancing-links answer offset is 192. Applicable nearby entries were read:
MPR83's 2020 stopping-rule correction, MPR101's 2022 proof amendment,
MPR104's March 2026 distributions, DLX261(b)'s source/sink index correction,
and the April 2026 arctic-circle reference update. None repairs these cards.
The earlier six-layer records also disambiguate Fascicle 6 exercises with the
same numbers.

Public searches combined Knuth/TAOCP with constant-information martingales,
Azuma predictable bounds, Friedman urn errors, Wald's summand, equal-distance
ties, Ace Now and 52, the gambling tail constant, g012/g112, ordered coupling
109, circular memo counts 260, and the exact path-product number
992340657705109416. No matching prior report was found.

The [MPR study/discussion guide](https://cracked.guide/guide/knuth-w116-0)
has no discussion posts. The public
[tamnd/brain volume directory](https://github.com/tamnd/brain/tree/main/content/en/practice/maths/taocp/vol4)
has no MPR section. Its DLX answers 248, 255, 260–263 were inspected:
248 repeats the items/options typo without flagging it; 260 gives a different,
incorrect generic cycle analysis without the memo-count correction; 261 does
not identify the product shift; 262 and 263 do not identify the picture or
memory-unit errors. These pages are not evidence of prior discovery.

The primary [Knuth path note](https://cs.stanford.edu/~knuth/papers/noncr-conj.pdf)
already archived with F154 uses a different square-size parameter and does
not explicitly report the later book's shift. A new web-tool fetch failed, so
it was not counted as a newly retrieved full text. The cited mathematical
results underlying the probability corrections are established facts; what
is being reviewed for novelty is the specific discrepancy in this edition.

No physical copy or private reports were checked. The conclusion is limited
to no matching prior report found in the available public sources, with no
absolute-priority claim.
