# Bookwise review: multiway merging and replacement selection

Reviewed volume 3 printed pp.248–267 through the end of §5.4.1,
the four §5.4 exercises and all thirty §5.4.1 exercises with their
answers on pp.676–680. Shared pages 267 and 680 begin polyphase merging
and remain for certification with that next block.

The balanced-merge pass counts, bank choice and five-run examples agree
with their stated tape model. The loser-tree representation and
Algorithm R were checked both in the original form and in the 2009
replacement, including initialization, empty input, run changes, the
P=1 extension and the artificial-infinity issue. The adaptive partition
into independent input subsequences in Theorem K supports the stated
replacement-selection generating-function factorization. The run
reconstitution argument correctly uses all m simultaneously buffered
blocks to bound the next block's minimum.

Checked the snowplow balance laws for ordinary replacement selection,
natural selection with equal/smaller reservoirs, first and final runs,
and the piecewise solution for larger FIFO reservoirs. The polynomial
generating function in exercise 22 has the derivative and boundary
relations needed by the displayed solution; its final time interval has
the endpoint typo C0050. The different, shuffled-reservoir model in
answer 23 has a substantive balance error, C0051. A small targeted
simulation supported the independently derived contradiction.

For changing run directions, checked the transition kernel,
normalization, quadratic stationary density, contraction-kernel bound,
and mean 6P/(3+p). Checked the associated-Stirling decomposition and
first-run mean in exercise 26. The host-tree assignment and its lower
bound in exercises 29–30 use the correct level sizes and component-edge
count. Known errata concerning R, descending-key strictness, answer 15,
and the independence notation were incorporated without new cards.

Limits: the fluid models are approximate steady-state descriptions,
not proofs of convergence of the stochastic finite-capacity systems.
The cited Espelid and Dobosiewicz approximations and empirical table
accuracy were not independently reproduced. Exercise 12's detailed
execution-frequency analysis remains a research task. Exercise 25
supplies integral recurrences without a printed derivation; their
structure and first-run mean agree with exercise 26, but their full
general derivation and McKenna's numerical limiting value were not
independently reconstructed. No new proof or numerical fixed-point
solver was written for that omission. Historical performance claims
were not remeasured.

New findings: C0050 (local endpoint) and C0051 (shuffled reservoir).
Official-source screen: `sources/replacement-selection-errata-review.json`.
Next: §5.4.2, printed p.267 / file p.278.
