# Recovery of all of §2.2.2–18 and completion of the section evidence review

The original initialization paragraph and G/R on248–250, the guarantee
on251, question18 on254 and the complete answer544 were read directly.
The entire earlier initial-amortization note and independent review are
accepted for their exact conditional scope. The following proof checks
every hypothesis, charge and endpoint; it preserves C0035 as candidate
because the phrase `as before` on248 has no explicit formula number.
This is completion of the evidence review, not a declaration that the
unqualified original theorem has been resolved.

## 1. Cost model and exact interval definitions

There are n≥1 stacks and M=L_infinity−L0 integer cells, with M≥n².
We count executed insertion/deletion operations, and take m to be their
finite number. The implicit constants in the requested bound are
independent of n,M and the operation sequence. Setup of the initial
arrays is excluded, as in the ordinary operation count; the work inside
a first operation remains included. Invalid deletion can terminate with
O(1) cost; for the principal proof the sequence has legal deletions and
successful insertions. A final failed insertion is addressed below.

The basic recovery proves G/R cost at most bN'+cn when the next
repacking has N' occupied cells including its pending insertion, for
fixed positive b,c. G scans the n tables a fixed number of times, R
scans them and copies each relocated old word at most once. Actually
at most N'−1 old words are present before the pending write, so bN'
is a harmless upper bound. Ordinary insertion/deletion costs are bounded
by fixed a,d. This is the book's arithmetic/word model, not Python
Fraction bit complexity or the experiment's copying-only measurement.

Consider the interval immediately after a completed repacking leaving
N occupied cells and S=M−N free cells, up to and including the insertion
that triggers the next repacking. Count p insertions and q deletions in
this interval, including that triggering insertion. Its new occupancy
is N'=N+p−q≤N+p. For every operation in this interval the most recent
previous repacking is the one with occupancy N, even though the last
operation itself will perform a new repacking. Thus its alpha is N/M.

## 2. Exact reserve and why the insertion count exceeds S/(10n)

G distributes a real provisional reserve

    u_j=S/(10n)+(9S/(10 INC))D_j,   u_j≥S/(10n),
    sum u_j=S.

INC>0 at a genuine repacking, as fully proved in the basic recovery.
The allocated integer gap is floor(U_j)−floor(U_(j−1)), where
U_j=sum_(l≤j)u_l. The last gap also has this form because U_n=S
is an integer. For any real x and nonnegative u,

    floor(x+u)−floor(x)≥floor(u).

Consequently every gap after this repacking is at least floor(S/(10n)),
including the first and last stacks. No rounding assumption or average
over the gaps is needed.

Until the next repacking, bases and capacities stay fixed. If the next
overflow occurs in stack i, its insertions minus its deletions exceed
its initial free gap. Thus the number of insertions into that stack
is at least its initial gap plus1, and in particular

    p≥floor(S/(10n))+1>S/(10n).                      (1)

Arbitrary intervening deletions only increase the required insertions.
The overflow-triggering insertion must be counted in p: it has already
advanced TOP before G is called. This agrees with the alpha convention
in the question and makes(1) valid even when the reserve is below1.

## 3. Every term in the printed charging calculation

First suppose S>0. Charge every insertion in this interval

    A(N,S)=a+b+10c+10(b+c)nN/S,                       (2)

and every deletion d. The actual cost through the next repacking is
at most

    pa+qd+bN'+cn ≤ pa+qd+bN+bp+cn.                   (3)

The extra charge above p(a+b)+qd is, by(1), strictly greater than

    cS/n+(b+c)N.

The hypothesis M≥n² supplies exactly the missing table-scan term:

    S/n+N=M/n+N(1−1/n)≥n,
    cS/n+(b+c)N≥cn+bN.                              (4)

Combining these lines pays every term of(3), proving the displayed
answer's inequality without omitting its dependence on n. The role
of the M≥n² hypothesis is explicit in(4); it is not used to bound the
number of occupied words by n or to suppress an initialization cost.
Since N/S=alpha/(1−alpha), the insertion charge is
O(1+n alpha/(1−alpha)), with uniform constants a,b,c,d.

An unfinished final interval has no final repacking, so its ordinary
cost is bounded by the same nonnegative charges. An interval consisting
only of deletions cannot end at a new insertion overflow; its cost is
just qd. The last insertion may leave N'=M and SUM=0; the already
proved G/R steps still place every item legally and the present
interval, whose old S is positive, has paid for that call.

A subsequent interval whose old S=0 has alpha=1. The fraction in the
question then has no finite value. The finite theorem is stated for
all encountered old occupancies alpha<1; if one adopts the usual
extended upper-bound convention alpha/(1−alpha)=+infinity at1,
the remaining bound is vacuous. Deletions after such a full repacking
do not retrospectively change that alpha. No finite estimate is
silently obtained by setting0/0 or by replacing alpha with the current
rather than the last-repacked occupancy.

If a final insertion instead exceeds total capacity, G detects negative
SUM after its n-table scan and stops without R. With previous S>0,
N+p−q=M+1 implies p≥S+1, so(1) still holds; the scan is no more
than the repacking cost already allowed in(3). With previous S=0
the preceding infinite-bound qualification applies. The initial case
is handled separately in the next section.

Summing(2) over insertions and d over deletions gives

    O(m+n sum_(k=1)^m alpha_k/(1−alpha_k)),           (5)

once the first interval has been paid. Adding the same nonnegative
summand for deletions only increases the upper bound, which explains
why the question sums over all operations rather than only insertions.

## 4. Complete first-interval proof under(13)

The evenly spaced initial bases(13), together with BASE[n+1]=L_infinity,
allocate gaps floor(jM/n)−floor((j−1)M/n). Every such gap is at
least floor(M/n), hence also at least floor(M/(10n)). All stacks
start empty. Treat the initial state as a virtual repacking with N=0,
S=M only for purposes of the charge; no execution of G is assumed.
The reserve proof(1) and the cost comparison(3)–(4) then apply to the
first interval too. Its charge is just a+b+10c per insertion, exactly
consistent with alpha_k=0 before the first real repacking.

More explicitly, any first overflow needs at least floor(M/n)+1> M/n
insertions in its target stack after subtracting deletions. Since
M≥n², this exceeds n; its O(n) scan cost is therefore absorbed by
the number of earlier insertions. Its relocation copies no more than
the number inserted so far. If there is no overflow at all, each
operation has only ordinary cost. This proves(5) completely when
initialization(13) is required. The weaker initial condition that each
stack have at least floor(M/(10n)) cells also suffices by the first
version of the proof, provided a legal partition exists.

For n=1 the original initializations coincide and a successful insertion
cannot require repacking: all M cells belong to the single stack.
The ordinary O(m) bound and final O(1) full-memory check agree with the
same argument. For m=0 there is no operation cost; excluding setup
makes the asserted zero bound literal.

## 5. Complete general-initialization repair and the exact candidate

For an arbitrary legal empty initial allocation, before the first
repacking all operations cost only O(1). If it is reached after p
insertions and q deletions, N'=p−q≤p; its extra cost is at most
bp+cn. Charging b extra to each preceding insertion and a one-time
cn budget pays it. The same argument pays a first terminal full-memory
scan. After the first successful repacking, §§2–3 apply unchanged.
Thus the fully general corrected bound is

    O(n+m+n sum_(k=1)^m alpha_k/(1−alpha_k)).         (6)

The extra n is needed in general under uniform asymptotic constants.
Indeed, with initialization(11), n≥2,M=n², OLDTOP=TOP, and the
single operation I1, stack1 has initial capacity0. That operation
calls G and G1/G2 explicitly scan all n stacks. Its cost is Omega(n)
but m=1 and alpha1=0, so the literal right side of(5) is O(1).
The failure occurs inside the counted insertion, independently of
whether initial table creation is charged. The pending operation is
feasible because M≥n²≥4. No fullness or undefined fraction is used.

If n were held fixed and the hidden constant were allowed to depend
arbitrarily on it, this one-operation example would not contradict
O(1). The explicit n-dependence and the parenthetical O(n) guarantee
in the exercise are the uniform interpretation used here. The precise
conditional counterexample is already recorded in C0035.

The actual unresolved textual choice is on248: `Initially, the tables
are set as before, with OLDTOP[j]=TOP[j].` The preceding discussion
includes the original(11), the optional evenly spaced(13), and other
starting values chosen from experience. The sentence gives no formula
number. Reading it as an exclusive reference to(13) yields the complete
proof in §4; permitting(11) yields the counterexample above and requires
(6) or another first-interval provision. Neither the mathematics nor
the successful simulation chooses between those readings. C0035
therefore remains candidate and exercise18 remains partial for this
one explicit interpretation, with all conditional mathematics proved.

The advertised90-percent corollary itself follows in either case.
If all occupancies after repacking are at most0.9M, then every term
alpha/(1−alpha)≤9. Formula(5), or(6) for arbitrary initialization,
gives O(nm) for m≥1, since the extra n in(6) is then absorbed by nm.
Thus each operation costs O(n) amortized, with a constant independent
of M. This is an amortized statement over the sequence, not a claim
that every individual repacking takes O(n). For m=0 it is vacuous.
The empirical half-full and nearly-full remarks remain precisely
scoped in the experiment recovery note.

## 6. Errata, accepted checks and whole-section reconciliation

All four errata layers and current TeX were checked by248–251,254,544
and the exact amortization/OLDTOP/initialization terms. None supplies
a missing first-interval initialization convention. Known corrections
to the allocator's notation, the left-copy endpoint and neighboring
answers remain separated; no new candidate or confirmed item is added.
The old full-content tests and post-repacking reserve assertions were
accepted in earlier recovery blocks with their exact finite limits;
none was rerun and no new computation is required for this proof.

Every main-text mathematical statement of244–251 and every part of
all19 original exercises has now been evidence-reviewed. The complete
claim map consists of these eight2026-11-07 notes:

* `quality-recovery-section-2.2.2-basic`: all representations, G/R,
  invariants, copying, lifetime aliases, generalizations and1,2,6–8,16,19;
* `quality-recovery-section-2.2.2-addressing`: every part of3–5;
* `quality-recovery-section-2.2.2-counting`: every part of9–12;
* `quality-recovery-section-2.2.2-probability`: all of13 and every limit;
* `quality-recovery-section-2.2.2-multinomial`: all of14;
* `quality-recovery-section-2.2.2-experiment`: all of15 and empirical,
  policy and historical/source scope;
* `quality-recovery-section-2.2.2-initialization`: all of17 and the
  independently proved weaker248 bound;
* this note: all of18 and the exact remaining interpretation.

Known C0034 remains a proved counterexample, rather than an unexplained
checked label. C0035 remains the explicit mathematical interpretation
gap; it is not called solved. Source exceptions remain the full Yao1981
journal text, Wise–Watson1976, Fraenkel1979 and the specified historical
attribution/priority checks, including the piano anecdote in answer19.
Available earlier reports, exact saved source scopes and own proofs
cover the mathematical dependencies actually used. No old broad
reading or inventory entry is substituted for those proofs.

The section is evidence-reviewed with these limits; main_text_status
and exercise18 stay partial. This raises the full-section recovery map
to32 of51 sections, without changing the original exercise status
counts or claiming whole-volume completion. The next section is2.2.3.
