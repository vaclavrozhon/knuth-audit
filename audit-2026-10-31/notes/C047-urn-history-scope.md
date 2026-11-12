# C047 — Which history is intended in exercise73?

Status: candidate only. The harmonic classification is correct when
martingales are required to be relative to the complete urn history.
The phrase "for this model" may be intended to impose that requirement.
No confirmed erratum is asserted.

Location: Volume4B, Mathematical Preliminaries Redux, exercise73,
p19/file39. Answer73 on p381/file401 gives the correct formula for
the harmonic interpretation. The interpretive issue is the uniqueness
claim in the question, not an arithmetic error in that formula.

The book first defines a martingale by conditioning on its own history,
equation(26), and separately defines being a martingale with respect to
an auxiliary sequence in equation(28). These properties differ here.

Let R_n be the number of red balls in the original same-color urn,
initially R_0=1. Its possible values1,…,n+1 have equal probability1/(n+1).
Define Z_0=Z_1=0, and for n≥2 let

    Z_n=f(R_n,n),
    f(r,n)=n(n+1)/6 · ([r=n]−[r=n+1]).

Set f(r,0)=f(r,1)=0 on their domains. Every left boundary value
f(1,k) is0. Nonetheless f is not identically zero: at time2 it has
values0,1,−1, each with probability1/3.

This is an entire martingale relative to its own history. The first
step is constant; at the next step the past is still constant and
E Z_2=0. For n≥2 put c_n=n(n+1)/6. At any state r≤n−1 both
next values vanish. At r=n the conditional next mean is
n c_{n+1}/(n+2)=c_n. At r=n+1 it is
(−(n+1)c_{n+1}+c_{n+1})/(n+2)=−c_n.
Thus from time2 onward it is even a martingale relative to the
whole urn history. The tower property gives the own-history
condition; integrability follows from |Z_n|≤c_n at every finite time.

It is not a martingale relative to the urn history at time1:
given R_1=1 the conditional mean of Z_2 is1/3, while given
R_1=2 it is−1/3. Z_1=0 in both cases. Its own constant history
averages those equally likely cases to0.

Therefore both this nonzero state function and the identically zero
function meet equation(26) with the same entire boundary sequence a_k=0.
Under that literal interpretation, the claimed uniqueness is false.
Under the intended harmonic interpretation, this example is excluded
and the printed classification is valid.

The full classification, its finite recurrence, existence, uniqueness,
all three examples, and every boundary case are proved in
notes/sequential-mpr-ex073-076.md. The six errata layers and three
TeX sources have no applicable clarification in the saved snapshots;
see results/sequential/mpr-073-076-urn-errata.json.

Resolution options:
- If "for this model" supplies the complete-urn-history condition,
  dismiss this candidate as a context note.
- Otherwise explicitly require that condition in exercise73.

No new computation, physical-copy claim, priority claim, or independent
coordinator approval accompanies this candidate.

