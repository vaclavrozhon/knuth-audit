# Two bounds are misstated in the Tamari meet-fiber proof

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–32, final line on 788 and semidistributivity paragraph on 789.

Let s_k and s′_k be the scope coordinates of F<=T F′. Index k is frozen when s_k<s′_k, and index 0 is frozen with s_0=n. The answer constructs the maximal forest F′′ satisfying F′ meet F′′=F by setting s′′_k=s_j-k+j, where j is the last frozen ancestor index.

The last line of page 788 correctly notes s_k<=s_j-(k-j), but then incorrectly concludes s′′_k<=s_k. It should conclude s′′_k>=s_k. For example, take F=F′ with scopes (1,0,0). Only index 0 is frozen, so the constructed scopes are (2,1,0), which are larger, not smaller. Equality at frozen coordinates is correct, and the following page correctly uses s_k<=s′′′_k<=s′′_k; its double-prime upper bounds were checked in an enlarged original image.

The final paragraph applies the interval result after replacing its lower forest by A=F meet G=F meet H. Its displayed hypotheses and conclusion nevertheless retain F as lower endpoint: F<=T G, F<=T H and F<=T G join H. These are not consequences of equal meets. For F the two-node chain and G=H the two-root forest, the meet hypothesis holds but F<=T G fails.

Use A<=T G<=T F′′ and A<=T H<=T F′′ instead; then A<=T G join H<=T F′′. The interval characterization proves the desired equality of meets, and duality gives the second semidistributive law. The construction and both laws remain valid.

Original typesetting inspected. No matching correction was found in the historical/current Volume 4A errata, refreshed Fascicle 4 errata or targeted public searches; see `../sources/tree-lattices-source-check.json`. Absolute novelty is not established.
