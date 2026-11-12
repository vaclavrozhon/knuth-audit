# Reversed arguments in the de Bruijn correspondence

Descriptive label: `feedback-argument-order`.

Status: candidate, evidence-backed mathematical correction; no global ID
assigned here. This concerns the stated bijection in answer 2.3.4.2-23,
not the final enumeration formula.

## Original statements

The original image of p. 380 specifies

```
X_(n+k+1) = f(X_(n+k), ..., X_(n+1)),   n >= 0.
```

Thus the most recent argument comes first. The answer on p. 584 uses arcs
`[x1,...,xk]` going from their length-(k-1) prefix to their suffix and says
that the correspondence is defined by

```
f(x1,...,xk) = x_(k+1)
```

when `[x1,...,xk]` is followed by `[x2,...,x_(k+1)]`.
This puts the oldest argument first, contrary to the recurrence.

Images inspected directly:

- `images/vol1-file395-p380.png`
- `images/vol1-file599-p584.png`

## Exact counterexample

Take m=k=2 and `f(u,v)=1-v`. The recurrence in the exercise produces

```
X1,X2,X3,... = 0,0,1,1,0,0,1,1,...
```

Its least period is 4=m^k, and its consecutive states run through
`00,01,11,10`. Therefore this is one of the functions to which the answer's
claimed correspondence applies.

The rule printed in the answer, applied to the same f, instead forces

```
00 -> 01 -> 10 -> 01 -> 10 -> ...
```

Here each arrow denotes consecutive arcs in G_2. In particular, the outgoing
arc after 01 is forced to be 10 because f(0,1)=0. The arcs 01 and 10 repeat
and 11 is never reached. This is not an Eulerian closed trail.

Equivalently, the actual maximum-period sequence needs 01 to be followed by
11, requiring `f(1,0)=1`, whereas the answer tests `f(0,1)=0`.
No numerical or asymptotic approximation is involved.

## Correction and scope

In the answer replace the displayed assignment by

```
f(xk,...,x1) = x_(k+1).
```

The ordered overlap of the arcs is then exactly the recurrence of the
exercise. Every maximal cycle determines f on all m^k argument tuples and
conversely. The enumeration `m^(-k) (m!)^(m^(k-1))` remains correct.

Alternatively, the recurrence in the exercise could be changed to put its
arguments in chronological order; that changes the convention for naming
the functions, but leaves their number unchanged. The answer-only edit is
the smaller correction.

## Errata comparison

All four supplied layers were searched by p. 380, p. 584, exercise 23,
period, argument, and reversal, and the corresponding original errata pages
were viewed:

- `all1-prepre`: pages 25-26 and 43-44;
- `all1-pre`: page 13;
- `all1`: page 10;
- `err1`: pages 8-9.

Relevant existing changes replace path/circuit terminology (2004/2008),
replace the proof of answer 21 (2001), remove a parenthesis on p. 584 (1997),
and correct arrows in its left figure (1997). None changes the argument
order in exercise or answer 23. The correction is absent from these four
layers as freshly checked by the root audit on 2026-11-01.

No claim of priority or physical-print verification is made.

## English ASCII draft

Page 584, answer to exercise 2.3.4.2-23: In the correspondence with Eulerian
closed trails, replace "f(x_1,...,x_k) = x_(k+1)" by
"f(x_k,...,x_1) = x_(k+1)". The recurrence on page 380 lists its arguments
from newest to oldest. For example, with m=k=2 and f(u,v)=1-v, the recurrence
has maximum period 0011, but the printed correspondence gives
00 -> 01 -> 10 -> 01 and does not produce an Eulerian trail. The final count
of functions is unchanged.
