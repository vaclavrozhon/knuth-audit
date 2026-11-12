# V4A-F0056: A QDD is not yet the minimum automaton

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), answer 7.1.4-261, printed 676 / file 693. Original:
`images/bookwise-p676.png`.

A QDD is the level-preserving decision diagram: even a constant
subfunction is represented at each required remaining input level.
The answer identifies it with the minimum-state deterministic finite
automaton accepting the length-n binary words on which f is true.
That identification overlooks the equivalence of rejecting residual
languages at different levels.

Take f(x1,x2)=x1 AND x2. Its QDD has five nodes: the root (truth
table 0001), the two level-two nodes (00 and 01), and the sinks 0
and 1. The minimum complete DFA for the language {11} has four
states: start, after one 1, accepting after 11, and a dead state.
The QDD node 00 and its 0 sink have the same residual language,
namely the empty language, and must be merged in a minimum DFA.
The four DFA states are distinct because their residual languages
are respectively {11}, {1}, {empty word}, and empty.

Correct the identification by merging all zero-subfunction nodes
into one rejecting state and adding the missing terminal transitions.
For nonzero residuals, the required remaining word length prevents
cross-level merging. The relationship between the uniqueness
theorems remains valid after this qualification. A convention using
partial automata instead removes the dead state; it still does not
make the unmodified QDD the minimum automaton.

No matching correction was found in the screened 4A/Fascicle 1
errata or targeted public reports. See `sources/zdd-tail-source-check.json`.
Absolute novelty is not established. The example was traced by hand.
