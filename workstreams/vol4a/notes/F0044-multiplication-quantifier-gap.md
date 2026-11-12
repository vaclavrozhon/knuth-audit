# V4A-F0044: The multiplier is chosen after the variable order

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), Theorem X and proof on printed page247 / file264, completed
by answer7.1.4-176(d) on page656 / file673. Originals are saved.

Write B_pi(a) for the BDD size of the middle bit of multiplication
by a, using variable order pi. The theorem asserts that some a
satisfies min_pi B_pi(a) >= (5/288)*2^floor(n/2)-2. In logical form,
one multiplier a must work for every order pi.

The proof first fixes pi and uses it to split the input bits into
the sets P and Q in (118). Answer176(a) then chooses a and b by
applying the hash-family estimate to those particular sets. Thus
a can depend on pi. The subsequent distinct-subfunction argument
applies only to that fixed order. The passage to B_min(Z_(n,a))
in answer176(d) is not justified.

The argument has the quantifier order "for each pi, choose a", not
"choose a that works for every pi". It therefore does not establish
the fixed-multiplier theorem as printed. This is a proof gap, not a
counterexample to the theorem's numerical claim. A statement with
the former quantifier order is the appropriate form of this argument;
its precise constant must also be justified by the counting steps.

The cited primary source explicitly has the former quantifier order:
Woelfel's Theorem11 fixes an arbitrary order before selecting the
multiplier. Section3 repeats this dependence. See the author's
[paper](https://cspages.ucalgary.ca/~woelfel/paper/OBDD-MUL/obdd-mul-journal.pdf),
PDF pages12 and14, archived with provenance in
`sources/woelfel-obdd-mul-source.json`.

No matching correction or report was located in the current and
historical Volume4A/Fascicle1 errata or public searches. See
`sources/bdd-multiplication-source-check.json`. Absolute novelty is
not established. No computation was needed.
