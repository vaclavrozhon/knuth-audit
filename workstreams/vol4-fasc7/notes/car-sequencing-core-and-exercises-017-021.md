# Car-sequencing core and exercises 17–21

Sources: first digital p. 7–8 (files 22–23), exercises p. 114 (129),
answers p. 160–161 (175–176). Original figures and pages were inspected.
This note does not close exercises 22–25 or the rest of either answer
page. The official [CSPLIB problem 001](https://www.csplib.org/Problems/prob001/)
is indeed Car Sequencing; its specification is saved with retrieval/hash
metadata in `sources/csplib-prob001-manifest.json`. Historical launch
date, ECAI1988 benchmark performance, and the 2005 competition results
on the following page remain explicit bibliographic/performance
exceptions. No historical search benchmark is rerun.

## CS-P01: Capacity windows and their interpretation

Use integer slots i and feature-w jobs occupying the half-open interval
[i,i+q_w). At an arrival, the still-active jobs are precisely those
started in the previous q_w−1 slots together with the new job. Hence
no more than p_w jobs overlap exactly when every window of q_w slots,
including truncated boundary windows, contains at most p_w feature
requests. Necessity is immediate from p_w available installers. For
sufficiency, assign each arriving request to a free installer. If none
were free, p_w earlier jobs plus the new one would be active in that
window, contradicting the bound. Each assignment lasts q_w slots and
releases its installer at the right endpoint, so induction over arrivals
proves that this greedy interpretation never creates a delay.

For a nonempty sequence with t≥q_w, every shorter boundary window is
contained in a full q_w window and thus is also bounded by p_w.
Therefore the full-window inequalities (17) suffice in that usual
input range. The printed instance has t=10 and q_w≤5. The range
q_w>t is explicitly separated below; it must not silently inherit
the truncated-window interpretation from (17), whose index set is
then empty. All divisions by p_w below use p_w≥1. A feature with zero
capacity needs immediate rejection if requested, or deletion if unused.

## CS-P02: Every feature in (16), the figure, and its bad suffix

The checkboxes of (16), in feature order moonroof, LED, audio, heated,
sport, give

| Model | Feature bits | Multiplicity |
|---|---|---|
| A | 01000 | 3 |
| B | 10100 | 2 |
| C | 01100 | 2 |
| D | 10010 | 1 |
| E | 11001 | 1 |
| F | 01110 | 1 |

The respective (p_w,q_w) are (2,5),(2,3),(1,2),(1,3),(1,5).
Thus the feature totals are r=(4,7,5,2,1), and the text's B example
is exactly 10100. These are direct transcriptions of every checkbox,
not inferred from the solution. The ten illustrated models, read in
production order from the older leftmost car to the new rightmost
one, spell ABABACDCEF. The depicted right-side entry convention is
consistent with the final F entering after C and E.

All 37 full feature windows of this word are listed in
`results/car-sequencing-core.json`. The only violation is the LED
window starting at slot 7: C,E,F give 111, above capacity two in
three slots. The other feature windows obey their bounds. Thus the
description “almost correct” and the specific delay in Fig. 100 are
verified, including the claimed responsible feature and suffix.

## CS-P03: The channelling model and the exact 151200 count

For each slot i there is a model variable x_i. For each individual
vehicle there is an inverse position variable; vehicles of each model
are strictly ordered. Each inverse value j imposes x_j equal to that
vehicle's model. These one-way conditions already prevent every
collision: two same-model vehicles cannot share a position because
of strict order, and two different-model vehicles cannot share a
position because x_j cannot equal two distinct labels. The t inverse
variables therefore occupy t distinct members of a t-element slot
set, hence cover all slots. It follows that the slot variables have
exactly the required model multiplicities.

Conversely, from a slot sequence with those multiplicities, give the
first vehicle of each model its first occurrence position, the next
vehicle its next position, and so on. This is the unique inverse
assignment satisfying both channel and order conditions. Therefore
the stated constraints on the twenty example variables are in
bijection with multiset permutations. Starting with 10! permutations
of distinguishable vehicles, forgetting identities among the three
As, two Bs and two Cs identifies exactly 3!2!2! permutations per
sequence. The count is 10!/(3!2!2!)=151200, with no extra factorial
from choosing inverse values.

Adding tm Boolean feature variables f_iw determined by the complete
table of model bits adds no choices: each x_i fixes all its feature
bits and conversely the channels merely require those bits. There
are t+t+tm=t(2+m) variables in this formulation. Each left-hand side
of (17) counts exactly the feature requests in its window, so the
constraints characterize the full-window model. This proves the
claimed sufficiency and variable count in the stated input range.

## CS-P04: Redundant prefix constraints and every example parameter

Fix w and a positive integer ell with ell q_w≤t. Partition the final
ell q_w slots into ell disjoint windows of length q_w. Each contains
at most p_w requests by (17), so the suffix contains at most ell p_w.
Since the total is r_w, the preceding prefix contains at least
r_w−ell p_w. This is exactly (18), with prefix indices
0,…,t−ell q_w−1. Values ell for which this lower bound is nonpositive
add no information, so it suffices to use
0<ell<ceil(r_w/p_w). For integer ell this is the same as ell<r_w/p_w.

At ell q_w=t the prefix is empty; the condition is 0≥r_w−ell p_w
and follows from the same window partition. For t≥q_w and ell q_w>t,
the sequence can be covered by at most ell full q_w windows: use
floor(t/q_w) consecutive windows and, if needed, a final overlapping
one. Nonnegative counts then give r_w≤ell p_w. Consequently an ell
in the selected positive-lower-bound range with ell q_w>t already
certifies infeasibility. It may be rejected before forming an indexed
constraint, or represented by an empty-sum contradiction; it does
not require accessing negative feature indices.

For the example, feature 1 has r_1=7,p_1=2,q_1=3. At ell=3 the
prefix is just slot 0 and its lower bound is one, forcing f_01=1.
Exactly B and D lack LED lights, so these are the two excluded first
models. The nine informative prefix bounds of all five features,
with their prefix lengths and zero-count complements, are saved in
the result JSON; they are reused in E21 below.

## CS-boundary: The short-sequence convention remains partial

The full-window formula (17) has no inequalities for a feature with
q_w>t. If it is meant to represent installer capacity for short
sequences too, or the later “q or fewer” convention of exercise 24,
one must impose the total-request bound for that feature. Otherwise
take t=2,p=1,q=3 with both cars requesting it: (17) is vacuous, while
two jobs overlap and the truncated-window capacity fails. Also (18)
would have ell=1, an empty prefix and a positive lower bound, so it
would not be redundant relative to the bare (17) in that domain.
The standard q_w≤t instance convention or explicit preprocessing
resolves this. The text's intended admissible input range is not yet
settled, so this is a partial scope item, not a confirmed finding.
The printed example, all following finite witnesses here and the
positive-capacity proofs above satisfy the stated assumptions.

## E17: A complete hand proof of the unique sequence up to reflection

The valid sequences FABABACDCE and ECDCABABAF have already been
checked against every model count and all 37 capacity windows in
`results/F7-C0003-evidence.json`; that exact fixed check is reused,
not rerun. It remains to exclude any other solution.

F requests both audio and heat. Its immediate neighbor cannot be
B or C (audio capacity 1/2), nor D (heat capacity 1/3); the only
possible neighboring models are A or E. Both request LED lights.
If F were internal, its two neighbors and itself would therefore
make a forbidden three-LED window. Hence F is at an endpoint. Reverse
the sequence if necessary and put F in slot 0.

There are seven LED-requesting cars and three non-LED cars B,B,D.
No run of LED ones can have length three. The three zeros split the
seven ones into at most four runs of length at most two. All four
runs must therefore be nonempty, with lengths a permutation of
(1,2,2,2). F's neighbor is A or E, so the initial run has length two.
The only possibilities for zero positions are consequently
{2,4,7}, {2,5,7}, {2,5,8}. The zero at slot 2 cannot be D, which
would violate the heat window containing F in slot 0; it is B.

Exactly five cars request audio: F,B,B,C,C. Their positions are
pairwise nonadjacent. After choosing the position of D in the other
two zero positions, this determines or narrowly restricts the audio
positions as follows. The possible E positions are the leftover
non-audio positions after placing A,A,A; E also requests moonroof.

| LED-zero positions | D position | Audio positions or obstruction | E restriction |
|---|---:|---|---|
| 2,4,7 | 4 | 0,2,5,7,9 | Candidates 1,3,6,8 all violate moonroof capacity |
| 2,4,7 | 7 | 0,2,4,6,8 or 0,2,4,6,9 | Moonroof constraints require E at 9 |
| 2,5,7 | 5 | 0,2,4,7,9 | Candidates 1,3,6,8 all violate moonroof capacity |
| 2,5,7 | 7 | Cannot place both remaining Cs nonadjacently | No solution |
| 2,5,8 | 5 | 0,2,4,6,8 | Candidates 1,3,7,9 all violate moonroof capacity |
| 2,5,8 | 8 | 0,2,5,7,9 | Candidates 1,3,4,6 all violate moonroof capacity |

To verify each audio row directly, remove the chosen B,F positions,
their immediate neighbors, and the D position; the two Cs must lie
in the remaining positions and be nonadjacent. For the moonroof
column, B,B,D already request that feature. Every rejected E position
lies within a span of four slots of two of those three requests, so
the corresponding five-slot window would contain three. For example,
when the zeros are 2,4,7 and D=4, E at 1 or 3 conflicts with requests
2,4, while E at 6 or 8 conflicts with requests 4,7. The other rejected
rows follow from pairs (2,5) or (5,7), pairs (2,5) or (5,8), and pairs
(2,5) or (5,8), respectively.

In the surviving row, requests at 2,4,7 rule out E at 1,3,5,6,8;
only slot 9 remains. Thus the audio choice using C at 9 is excluded,
and C occupies 6 and 8. The As occupy 1,3,5. This forces exactly
F A B A B A C D C E. Its reverse is the other solution already checked.
This proves the uniqueness claim as well as the displayed answer.

## E18: Reflection and the odd-multiplicity alternatives

Reflection sends slot i to t−1−i and takes each contiguous capacity
window to a window of the same length with the same count. It also
preserves model multiplicities, so it maps solutions to solutions.
For t=10, a sole F at f≥5 moves to 9−f<5; if it is already below 5,
its mirror is above. Thus f<5 keeps exactly one member of each pair.
The same argument works for the unique D or E. For A, whose three
positions are a_0<a_1<a_2, reflection takes the median position to
9−a_1, so a_1<5 is another valid symmetry choice.

More generally, for even t and a model of odd multiplicity 2h+1, the
counts in the first and second halves cannot be equal. Reflection
interchanges them. Requiring at least h+1 occurrences in the first
half therefore selects exactly one orientation. A palindrome of
even length has even multiplicity for every model, so it is not a
fixed point when an odd-multiplicity model is present. The assertion
that F is “probably harder to place” is a heuristic observation,
not needed for the symmetry proof.

## E19: Logical implication does not imply propagation redundancy

For nonnegative ell′,ell″ with the indicated middle interval, the
left ell′q slots contain at most ell′p requests and the right ell″q
slots contain at most ell″p. Subtracting both from the exact total r
gives the proposed middle lower bound. A direct derivation using
(18) uses its prefix bound for ell=ell″ and subtracts the left upper
bound; when ell″=0 the total r supplies that prefix bound. Thus the
new inequalities hold for every complete solution. The answer labels
its initial “No” reasoning as wrong; its rejection is essential.
Neither logical implication nor the displayed discarded index
argument proves that an extra constraint is useless on partial data.

Here is an explicit propagation example for the text's own LED
parameters t=10,p=2,q=3,r=7. Fix f_6=f_7=f_8=0 and f_9=1, leaving
f_0,…,f_5 unknown. The original prefix bounds are

    sum_(i=0)^6 f_i≥5,  sum_(i=0)^3 f_i≥3,  f_0≥1.

After setting f_0=1, every remaining unknown has both values supported
in each individual original inequality that contains it: the first
bound requires at least four ones among five unknowns, the second
requires at least two among three, and the upper window starting at
0 requires at most one among f_1,f_2. Every other upper window is
similarly individually supported. No original inequality alone
removes another value or detects contradiction, even after repeating
such domain filtering.

The new middle constraint for ell′=1,ell″=0 is
sum_(i=3)^9 f_i≥5. Its maximum under these domains is only four,
so it rejects the partial state immediately. This proves a concrete
strict benefit of adding the logically redundant inequality to the
feature-constraint subsystem. Other channels or stronger combined
reasoning could also reject it; no claim of universal speedup or
exclusive detection is made. The construction explains precisely
the printed example of information known only in the right half.

## E20: Full MCC encoding, including the corrected concrete option

Create an exact-once primary item for each slot i and an exact-count
primary item for each model, with multiplicity equal to its required
number of vehicles. There is an option for each pair (i,model),
containing both corresponding items. A selection meeting these
conditions is exactly a sequence with the required model counts,
and each such sequence selects its unique set of these options.

For each full feature window starting at j, introduce u_jk with
allowed multiplicity [0,p_k]. Put u_jk into precisely those options
(i,model) where j≤i<j+q_k and the model requests feature k. The total
selected occurrences of u_jk are then exactly the left-hand side
of (17). This proves both directions of the MCC reduction, with no
colors needed. A [0,1] item has ordinary at-most-once secondary-item
semantics, in accordance with the public “should be secondary”
wording amendment.

For slot 2 and model B=10100, the moonroof windows containing it
start at 0,1,2; the audio windows containing it start at 1,2. Thus
the option is

    2 B u00 u10 u20 u12 u22,

exactly the public 5 September 2026 correction. It contains no heated
seat item, because B does not request heat. The first sentence on
p. 161 calling these initial slot/type entities “options” should say
“items”: this local terminology error is independently confirmed as
F7-C0003, whose closed evidence is reused. It does not invalidate the
intended reduction just proved.

## E21: Complementing prefix sums and the entire corrected option

For prefix length L=t−ell q_k≥0, define fbar_ik=1−f_ik. Then

    sum_prefix f_ik ≥ r_k−ell p_k
    iff sum_prefix fbar_ik ≤ L−r_k+ell p_k = s_ell,k.

This follows by substituting sum fbar=L−sum f, including an empty
prefix. Introduce v_ell,k with allowed multiplicity [0,s_ell,k], and
include it in every option in that prefix whose model lacks feature
k. Its chosen multiplicity is exactly the complemented sum, proving
the proposed encoding. If s<0 the instance is infeasible and should
be rejected before encoding a negative upper multiplicity. If s=0,
every option containing the item is forbidden and may be removed.

For the ten-car example, all relevant (ell,L,s) triples are

    feature0: (1,5,3);
    feature1: (1,7,2), (2,4,1), (3,1,0);
    feature2: (1,8,4), (2,6,3), (3,4,2), (4,2,1);
    feature3: (1,7,6);
    feature4: none.

For feature1 at ell=3, only slot 0 is in the prefix and s=0; the
non-LED models B,D there must therefore be removed, exactly as the
answer says. Option (2,B) already requests features 0 and 2, so it
gains no complementary items of those features. It lacks feature1
and lies in its ell=1,2 prefixes but not ell=3, so gains v11,v21.
It lacks heat and lies in feature3's sole prefix, so gains v13.
There is no feature4 prefix item. The complete option is therefore

    2 B u00 u10 u20 v11 v21 u12 u22 v13,

matching every item and index of the public correction. Middle
interval bounds from E19 can use the same complement identity and
option-incidence construction, with that interval's length replacing
L. This verifies the last sentence's generalization too.

## Evidence and remaining scope

The only new calculation for this block checked the 37 windows of
the single printed bad sequence and formed the nine explicit prefix
bounds; it ran with nice15. Valid-sequence window certificates are
reused from F7-C0003. The uniqueness argument is by hand, not a
permutation enumeration. The earlier physical-boundary convention
q_w>t remains partial; historical performance/attribution exceptions
are stated explicitly. The p. 161 public changes to the example
options are applied and never counted as findings. Exercises22–25
and their additional counts and formulas remain the next block.
