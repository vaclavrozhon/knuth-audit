# V3-C0053 — The reverse-generation argument omits simultaneous empty tapes

Confirmed in volume 3, second edition, first printing (1998), answer
5.4.2-28, printed p.684, file p.695. Its opening claim says every
six-tape distribution sortable within n merge-until-empty phases is
obtained from (1,0,0,0,0) by n operations, each choosing one entry x
and adding x to all four other entries. This exact-generation claim
fails when several tapes become empty at the same time.

For example, start with counts (2,2,1,1,1) on five tapes and a sixth tape
empty. One five-way merge consumes one run from each input tape. Two
input tapes then have one run each, and the output tape has one merged
run. A three-way merge of these runs completes the sort in a second
phase. Thus this is an admissible two-phase distribution, with seven
initial runs and all five initial counts positive.

It cannot be obtained by the printed reverse rule. One operation raises
the sum of the entries by 4x. Starting at sum 1, every obtainable sum is
therefore congruent to 1 modulo 4, whereas seven is congruent to 3.
In particular, two operations can give totals only 1,5,9.

The upper bound being proved is not refuted. The proof can be repaired
by allowing a reverse operation to add x only to the tapes that were
active in that phase, or by saying that the generated full distributions
**dominate** the actual distributions component by component. Adding x
to every other entry then provides the upper bound used by the printed
induction. It does not describe every actual distribution exactly.

Original p.684 was visually checked and retained as
`images/bookwise-p684.png`. The five official errata layers were screened
in `sources/polyphase-errata-review.json`; a targeted public search found
no matching correction. No absolute priority claim is made.
