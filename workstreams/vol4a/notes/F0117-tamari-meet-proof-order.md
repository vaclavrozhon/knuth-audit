# The meet comparison uses a false order chain

Volume 4A, first edition, first printing (2011).
Answer 7.2.1.6–27(f), printed 787.

Write <=K and <=T for the Kreweras and Tamari orders. The Tamari order compares the scope coordinates, the numbers of proper descendants of each preorder-numbered node. Let M_K and M_T be the respective meets of F and F′.

The printed proof chains M_K <=K F <=T M_T and M_K <=K F′ <=T M_T. The second inequality in each chain is generally false: a meet is below its inputs. For the two-node chain F with scopes (1,0) and the forest F′ of two isolated nodes with scopes (0,0), M_T has scopes (0,0); F <=T M_T would require 1<=0.

The intended proof is short. Since M_K <=K F and M_K <=K F′, part (e) gives M_K <=T F and M_K <=T F′. Therefore M_K <=T M_T by the greatest-lower-bound property. The exercise's conclusion is correct.

Original typesetting inspected. No matching correction was found in the historical/current Volume 4A errata, refreshed Fascicle 4 errata or targeted public searches; see `../sources/tree-lattices-source-check.json`. Absolute novelty is not established.
