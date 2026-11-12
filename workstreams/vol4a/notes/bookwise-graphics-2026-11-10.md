# Hyperbolic cells and bitmap geometry

Main pages 168–180, exercises 154–187, and answers 607–615 were read
together. Whole main pages 168–180, exercise pages 196–198, and answer
pages 607–614 are certified. Exercise page 199 and answer page 615
contain the next material and remain for its record.

Five new findings were documented against original page images and
historical/current errata: F0024 corrects the parabola curvature and
its numerical example; F0025 corrects an endpoint off the parabola;
F0026 supplies a missing child-pointer initialization; F0027 fixes a
null write during a component-tree splice; F0028 fixes the recorded
first-pixel column. Their separate notes give short hand calculations
or traces, impacts and source checks. No matching public report was
located; absolute novelty is not asserted.

The negative-Fibonacci digits, the predecessor/successor recurrences,
and the carry-based ten-operation construction were read together.
The ordinary Fibonacci decrement uses monus; its seven-operation
count and the conversion updates have known corrections. The odd
Fibonacci conversion, reversal obstruction, and pentagrid orientation
rules were followed as printed; the omitted case analyses are explicit
limits below. The upper-half-plane reflection formula is inversion
on the real endpoints of a semicircle. The 36/45/90 triangle and the
36/36/90 alternate pentagons agree with the angle descriptions.

The custerization formulas distinguish four and eight neighbors. The
maximum-density argument counts five contributions per black pixel
against at most four per interior cell. The Life implementation forms
neighbor counts with one half adder and three full adders, then tests
for exactly one high count bit and the low-bit survival condition.
The toroidal buffering algorithm retains two overlap bits and uses
the corrected zeroed auxiliary column before updating boundary bits.
The thinning network and its original configurations were inspected,
without regenerating its truth table or the empirical trajectories.

The cleaning operations are monotone closure/interior operations;
the inclusions and idempotence argument establish (XDL)DL=XDL.
The shrinking proof maps each surviving component through overlapping
local neighborhoods. Its known corrected part (b) was read in the
original errata PDF. The doubled row encoding makes black kingwise
and white rookwise overlaps use the same interval criterion. The
component-tree algorithm's four splice cases, dormant lists, absorption,
areas and traversal were followed; its pointer and coordinate defects
are F0026–F0028. The known next correction does not fix those defects.

For conics, the finite-difference updates preserve Q and its two
first derivatives. The four initializations use the appropriate
corner pixel and signed directional differences. The digitization
argument uses monotonicity and the no-two-roots premise; tie handling
is an infinitesimal positive perturbation. The ellipse and hyperbola
examples, the sign-reversal construction Q'=-1-Q, and the rational
line specialization were checked. The known derivative-coordinate
correction in answer 181 and the cross-reference correction in 185
are excluded from findings. The two parabola errors are new.
The quadratic Bezier recurrence is the displayed subdivision identity;
the implicit quadratic follows by eliminating t from 2*t*u+t^2*v.
The determinant sign selects the left side, and the known non-strict
monotonicity correction in answer 187 is incorporated.

No helper, general verifier, simulation, or census was run. Exact
external, empirical and proof-sketch limits are in the companion
exceptions file. Next: main page 181 / file 198, exercise 188 onward,
and answers from page 615.
