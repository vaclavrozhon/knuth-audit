# Recovery of §2.2.3–13: every bound, constant, count and research limit

The original question270/answer547, the2001 correction, the2018
reworded question and replacement answer, and every claim of the prior
`boolean-lattice.md` and `boolean-bound-extra-exp.md` were reviewed.
Both complete prior notes are accepted as mathematical evidence after
checking their exact domains. The originals270,547, errata-pre12/16
and prepre41 were viewed directly. Brightwell–Tetali's original PDF
pages2–3 and8–11 and Brouwer–Christensen's pages3–4 were also viewed
directly; the relevant full stored text and source-status entries were
read. This is a proof-scope recovery, not a new count computation or
a claim to solve every continuation of this research question.

Use natural logarithms below. Let a_n count linear extensions of the
Boolean lattice of all subsets of an n-element set, N=2^n,
b_i=binom(n,i), L_n=product b_i!, and U_n=product b_i^(b_i).
For n=0 the lattice has one element, not zero elements, and a_0=1.

## 1. Lower and upper bounds, with all probabilistic assumptions

The first two sections of `boolean-lattice.md` give complete independent
proofs of L_n≤a_n≤U_n. Sorting first by cardinality allows any
permutation within each layer, giving exactly L_n distinct extensions.
For the upper bound, a uniform random permutation of the n labels
defines a maximal chain by its prefixes. A given i-subset appears
with probability i!(n−i)!/n!=1/b_i, including i=0,n. A chain contains
at most one element of an antichain, so summing these indicator
expectations proves sum(S in A)1/b_|S|≤1 for every antichain A.

At any nonterminal stage of a finite topological ordering, the
available minima are a nonempty antichain. Select S among them with
probability w(S)/W, where w(S)=1/b_|S| and0<W≤1. The process ends
after N selections and its outputs partition its probability space
into the a_n possible extensions. For each such output the product
of transition probabilities is at least product_S w(S)=1/U_n.
Summing gives a_n/U_n≤1. All weights are positive, so every permitted
extension is supported and no undefined conditional probability occurs.
This proof includes n=0 directly and does not require the unavailable
Sha–Kleitman paper to supply any mathematical step.

## 2. Every step of the stronger bound has sufficient prior evidence

The complete section “Rekonstrukce důkazu silnější horní meze” in
`boolean-lattice.md` is accepted without recomputing it. Here is the
exact premise/step map, including the delicate quantifiers.

* P has k≥2 nonempty ranks of sizes n_j, N=sum n_j. Between consecutive
  ranks each lower element has u_(j−1)>0 upper neighbors and each upper
  element has d_j>0 lower neighbors. Counting edges gives
  n_(j−1)u_(j−1)=n_j d_j. The Boolean lattice meets every premise.
* f is uniform on the finite nonempty set of weakly isotone maps into
  {1,...,M}; constant maps ensure nonemptiness. For any fixed integer
  s≥1 take M through multiples of s, tending to infinity. Define B_x
  by the lowest block occupied by an upper neighbor, and set B_x=s
  on the top rank. Neighbor pairs y<x satisfy1≤B_y≤B_x≤s.
  Conditional on B_x=b,B_y=c, f(x) lies in the integer interval
  ((M/s)(c−1),(M/s)b], which contains exactly(M/s)(b−c+1) integers.
  This is why the divisibility restriction on M is useful.
* Entropy is finite. Its chain rule follows by factoring the joint
  probabilities; support-size bounds and conditioning monotonicity
  follow from concavity of−t ln t (equivalently Jensen/log-sum).
  For conditional Shearer, expand every selected coordinate subset
  in one common coordinate order. Conditioning on all earlier
  coordinates can only reduce each summand. Every coordinate appears
  in exactly d_j neighbor sets, so their entropy sum is at least
  d_j times the full rank entropy, also after common conditioning.
* The induction bounds the entropy of the first j ranks conditional
  on all higher ranks by(1/n_j)sum_x E ln Q_j(B_x), where

```
Q_1(b)=(M/s)^n_1 b^n_1,
Q_j(b)=s^(n_(j−1)/d_j)(M/s)^n_j
       max_(1≤c≤b) [(b−c+1)^n_j Q_(j−1)(c)].
```

  The base uses the just-proved support bound and subadditivity.
  In the step, let a=n_(j−1), d=d_j, u=u_(j−1). Shearer and insertion
  of B_y yield edge contributions with outer factor1/(du). The
  preceding induction term becomes(1/(au))sum_(y<x)E ln Q_(j−1)(B_y).
  Thus for fixed B_x=b the combined summand is

```
sum_c p_c ln(W_c/p_c),
W_c=(M/s)^u (b−c+1)^u Q_(j−1)(c)^(d/a),
p_c=P(B_y=c | B_x=b).
```

  Only b of positive probability need be considered, and p_c=0 terms
  have value0 by continuity. Jensen bounds this by ln(sum W_c),
  hence by ln(s max W_c). Each x occurs in d edges. The identity
  n_j/u=a/d changes the resulting bound precisely into the displayed
  Q_j recurrence; in particular the exponent on Q_(j−1) becomes1.
  B_x is determined by the higher ranks (or constant on the top rank),
  justifying every removal of conditioning in this argument.
* Unrolling at the top gives s^r(M/s)^N times the maximum of
  b_1^n_1(b_2−b_1+1)^n_2 ... (s−b_(k−1)+1)^n_k, with
  r=sum_(j=2)^k n_(j−1)/d_j. The k positive bases sum to s+k−1.
  Concavity of log, with weights n_j/N, bounds the product by
  (s+k−1)^N product(n_j/N)^n_j. This is a real relaxation of an
  integer maximum, not an assertion that a proportional integer
  maximizer always exists.
* Each extension together with N distinct chosen values gives a
  different isotone map, so O_M(P)≥a(P)binom(M,N). Divide by M^N
  and take the limit along the specified multiples; N is fixed and
  binom(M,N)/M^N→1/N!. The factor
  N! product(n_j/N)^n_j / product n_j! is a multinomial probability
  and hence≤1. Also(1+(k−1)/s)^N≤exp((k−1)N/s).
* Since0<r≤N and k−1≥1, s=ceil((k−1)N/r) lies between that positive
  real number and twice it. Substitution therefore gives exactly

```
a(P) ≤ (2e(k−1)N/r)^r product_j n_j! .
```

This proves the actual Theorem1.3 with all endpoint, rounding, rank
and limit assumptions. It does not rely on the specialized bipartite
Theorem1.4, whose independent audit is outside this exercise's scope.
The book's dimension n means k=n+1 and n_j=binom(n,j−1), d_j=j−1.
Consequently, for n≥1,

```
r=sum_(i=0)^(n−1) binom(n,i)/(i+1)
 =(2^(n+1)−2)/(n+1),
B_n=(2en2^n/r)^r L_n,
L_n≤a_n≤min(U_n,B_n).
```

The r identity follows term by term from
binom(n,i)/(i+1)=binom(n+1,i+1)/(n+1), omitting the two endpoint
binomial terms. n=0 uses a_0=1 separately, avoiding division by r=0.
The name B_n in this formula denotes the numerical upper bound;
it is not the Boolean poset notation used by Brouwer–Christensen.

## 3. Stirling, tails, moments and the exact asymptotic conclusion

The prior Stirling proof is accepted, with the following explicit
uniform bounds making its entire range reviewable. For a positive
integer b, ln(b!)=b ln b−b+(ln b+ln(2pi))/2+O(1/b), uniformly for
b≥1. Thus, if K is binomial(n,1/2),

```
ln L_n/N=E ln binom(n,K)−1+O(n^2/N).
```

Indeed sum_i b_i=N, sum_i b_i ln b_i=N E ln b_K, and the remaining
n+1 logarithmic terms have total O(n^2). Write X=K−n/2. On
|X|≤n/4, put p=1/2+X/n in[1/4,3/4]. Uniform Stirling for n!,K!
and(n−K)! gives nH(p)−(1/2)ln(2pi n p(1−p))+O(1/n).
Taylor's theorem on this fixed compact interval gives

```
ln binom(n,n/2+X)
 = n ln2 − (1/2)ln(pi n/2) −2X^2/n
   +O(1/n+X^2/n^2+X^4/n^3).
```

This applies to both integral and half-integral X as required; it
does not assume n is even. The centered Bernoulli summands are
independent±1/2, hence EX^2=n/4 and
EX^4=n/16+6binom(n,2)/16=3n^2/16−n/8. Their moment generating
function is(cosh(t/2))^n. Since ln cosh u≤u^2/2, Markov with t=1
gives P(|X|>n/4)≤2exp(−n/8). The ignored tail contributions are
O(n exp(−n/8)), since0≤ln binom(n,K)≤n ln2 and the displayed
quadratic approximant is also O(n). Therefore

```
E ln binom(n,K)=n ln2−(1/2)ln(pi n/2)−1/2+O(1/n),
ln L_n/N=n ln2−(1/2)ln(pi n/2)−3/2+O(1/n).
```

Finally r/N=2(1−1/N)/(n+1)=O(1/n), and
2enN/r=en(n+1)/(1−1/N). Thus ln(B_n/L_n)/N=O(ln n/n).
Sandwiching a_n proves

```
ln(a_n)/2^n
 = n ln2 − (1/2)ln(pi n/2) −3/2 + O(ln n/n).
```

Equivalently a_n^(1/2^n) divided by
sqrt(2/pi)e^(−3/2)2^n/sqrt(n) tends to1. This is a sharp asymptotic
for that root, including the constant; it is not a relative asymptotic
for a_n itself. Exponentiating its error allows a multiplicative
factor exp(O(2^n ln n/n)), which need not tend to1. In particular
neither a_n/L_n→1 nor an exact closed form is established by this
argument. No assertion about the present literature status of such
stronger questions is being made.

For the superseded historical formula, subtraction of uniform
Stirling expressions gives

```
ln(U_n/L_n)
 = N−(n+1)ln(2pi)/2−(1/2)sum_i ln binom(n,i)
   +O(sum_i 1/binom(n,i)).
```

Uniformly in i, ln binom(n,i)=nH(i/n)+O(ln(n+1)), including
the endpoints by continuity. H increases and then decreases, so
its Riemann-sum error is bounded by its fixed total variation.
Since integral_0^1 H(t)dt=1/2, the sum is n^2/2+O(n ln n).
The reciprocal sum is at most n+1. Consequently

```
ln(U_n/L_n)=2^n−n^2/4+O(n ln n).
```

The original1997 lower-bound exponent n+O(1) misses the unbounded
−(1/2)log_2 n term; the2001 n+O(log n) replacement is correct.
The original ratio2^(2^n+O(n)) also has the wrong leading base.
Changing only the base to e in2001 still leaves an incorrect O(n)
remainder, because−n^2/4+O(n ln n) is not O(n). That entire ratio
claim disappeared in the2018 replacement. These are the already
recorded historical corrections/limitations, not a new active finding.
The claim that the lower bound was conjectured to give the correct
constant is corroborated by BT's introduction; its mathematics is
the just-proved constant, not the unchecked wording of the1987 paper.

## 4. Exact recurrence, termination, implementation and saved values

For every ideal I of the Boolean lattice, define F(I) to be the number
of valid suffixes after its elements have been output. F(full)=1 and

```
F(I)=sum_(x not in I, every immediate predecessor of x in I)
       F(I union {x}).
```

Immediate predecessors suffice: deleting one element at a time gives
a chain from every proper subset to x; since I is an ideal, containing
all immediate predecessors contains every proper subset. Conversely
any next output must have all these predecessors already present.
The summands classify suffixes disjointly by their first element.
Induction on N−|I| therefore proves the exact recurrence and a_n=F(empty).
Each recursive edge increases |I|, so it terminates; memoization
reuses only identical ideals. The number D_n of ideal states is finite,
at most2^N, and each has at most N outgoing choices. In an arithmetic
model with whole bit-mask operations the recurrence uses O(ND_n)
state tests/additions. The masks have N bits and counts at most N!,
so elementary bit operations give the safe upper bounds
O(D_n N^2 log N) time and O(D_n N log N) bits of stored masks/counts
for n≥1. No practical polynomial running time is claimed. The finite
recurrence can also be evaluated by decreasing ideal size, avoiding
any language's recursion-depth limit.

The old `boolean_extensions` code encodes subset x by its n bits
and the ideal by a bit mask on all N subsets. For every set bit i
of x it includes exactly x xor2^i in the predecessor mask. Its bit
test is therefore precisely the condition above. The terminal full
mask and its return1 are exact, including the n=0 one-element lattice.
The entire recurrence, the driver for n=0,...,5, and the saved result
records were read; no execution was repeated. The independently
computed values are

| n | a_n | Saved ideal states |
|---|---:|---:|
|0|1|2|
|1|1|3|
|2|2|6|
|3|48|20|
|4|1680384|168|
|5|14807804035657359360|7581|

The first values also admit direct checks. For n=2 only the two
singleton positions can be exchanged. For n=3 choose the first two
singletons in6 ways. Then either the third singleton is next, leaving
3!=6 orders of the pairs, or their common pair is next, then the
third singleton, leaving2 pair orders. Including the forced empty
and full subsets gives6(6+2)=48.

The source table's n=6 and7 values agree digit for digit with the
stored OEIS b-file. The n=7 integer has138 digits and begins630470...,
hence rounds to6.305×10^137 as the replacement answer says. These
two values are source-checked, not independently recomputed here.
Brouwer–Christensen's exact recurrence removes a maximal element
instead of adding a minimal one; classifying extensions by their
last element proves it. Canonicalizing ideals under label permutations
is safe because a permutation preserves inclusion and bijects their
extension sets; memoizing isomorphic states reuses a common value,
while each candidate removal still contributes its own summand.
Their recorded procedure enumerates permutations compatible with
isomorphism-invariant signatures before choosing a canonical form.
The two reported independent implementations and their runtimes are
the authors' evidence, not an inspection or rerun of unavailable C
programs. Expensive independent n=6/7 reproduction remains explicitly
skipped under the user's instruction.

## 5. C0036 and exact source/errata scope

The full accepted `boolean-bound-extra-exp.md` proves the existing
C0036 at its correct location: the2018 replacement answer in
all1-pre file16, not original1997 p547. Its outer exp gives exp(B_n)
where primary Theorem1.3 gives B_n. Since B_n≥1, exp(B_n) is still a
valid upper bound. The false part is its attribution as that theorem
and its alleged improvement of U_n.

For completeness the accepted comparisons cover every dimension:
for n≥4, factorials give L_n≥2^(2^n−n−1)>n2^n ln2≥ln U_n.
The strict middle inequality holds at4 and its left/right ratio
increases thereafter by the factor2^(2^n−1)n/(2(n+1))>1.
For n=1,2,3 the values U_n=1,4,729 and L_n=1,2,36 verify the
same exp(B_n)>U_n conclusion directly. Conversely at n=16 the
integral factorial bound gives ln(U_n/L_n)>65247 while
ln(B_n/L_n)<53977, using e<3 and ln2<0.7. Thus B_16<U_16<exp(B_16).
This is a true contradiction to the claimed improvement, independently
of large integer computation. It does not falsely assert that B_n
beats U_n for every small dimension.

The four historical/current errata layers and current TeX are searched
again in the accompanying snapshot by270/547 and Sha, Kleitman,
Brightwell, Tetali, Boolean, A046873 and the quoted asymptotic/counting
topic. The2001 and2018 entries are distinguished; no later correction
of the outer exp is present in these frozen layers. C0036 stays
confirmed with no additional finding. Physical-print verification
and priority are not claimed.

The exact Sha–Kleitman1987 attribution/conjecture wording remains an
explicit bibliography skip after the stored unsuccessful source
attempts. The mathematical inequality has its independent full proof
in §1, and BT's accessible primary introduction corroborates the
historical account. The accepted BT proof is its general ranked-poset
theorem, not an unreviewed appeal to an entire paper. The OEIS snapshot
is evidence for the values quoted in the book; it is not presented as
a live claim that no later terms are known.

## 6. Scope of the research wording

The original M48 question asks for the count as a function of n; its
2018 HM48 replacement asks to try for a “sharp” asymptotic estimate.
The exact finite recurrence above and the sharp normalized-logarithm
formula are established results. They explain every mathematical
claim in the old and replacement answers, subject to C0036 and the
explicit source/reproduction limits. They do not give a simple exact
closed form, a relative asymptotic for the entire count, or closure
of arbitrary further research. Any status attached to this review
must retain this precise distinction; the word “sharp” is not a
license to silently replace the proved logarithmic conclusion by
one of those stronger statements.
