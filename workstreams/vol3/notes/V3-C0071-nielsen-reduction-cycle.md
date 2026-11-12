# V3-C0071 — The subgroup-membership procedure can cycle

Confirmed in volume 3, second edition, first printing (1998), exercise
6.3-41, printed pp.511–512 (file pp.522–523).

Use the free group on two letters a and b: words are reduced by
cancelling adjacent inverse letters. Let the subgroup have the single
generator theta=ab. It satisfies the stated Nielsen condition. In the
nonexcluded product theta theta, neither central letter is cancelled;
the inverse product is explicitly exempted from the condition.

The search keys are ab and b^(-1)a^(-1). Start the membership test with
the reduced word a. Its longest matching prefix selects ab uniquely.
The notation of the exercise has k=l=1, so the new word is not longer
and the procedure continues:

    a  ->  (ab)^(-1)a = b^(-1)
       ->  (ab)b^(-1) = a  ->  ...

At the second step the unique matching key is b^(-1)a^(-1), again with
k=l=1. Thus no ambiguity or increasing-length rejection applies. The
algorithm never terminates, although a is not a power of ab and hence
is not in the subgroup.

The stated claim that the Nielsen condition guarantees termination
needs an additional rule for length-preserving reductions. Merely
rejecting all such reductions would need a separate justification;
this note establishes the cycle without proposing an unproved general
replacement algorithm.

Original pp.511–512 checked visually and retained. The known grammar
correction to p.511 does not address this issue. No matching correction
was located in the official layers or limited public searches; see
`sources/digital-searching-errata-review.json`.
