# F251 — A missing complemented string makes the UNSAT example satisfiable

Confirmed in Volume 4B, answer 504(d), printed 650/file 670; author draft 286.
Part (a) requires four strings w_j and all four complements. The last
boilerplate string in (d) repeats 00000011 instead of its complement
11111100. Replace that final string by 11111100.

The error is consequential: z=00000011 is within distance 4 of every
printed boilerplate string, with distances (4,4,4,0,4,4,4,0). It is also
within distance 5 of every printed clause string, including the optional
eighth clause: the distances are (5,3,3,3,5,3,3,3). Thus the displayed
closest-string instance for the unsatisfiable eight-clause formula R in
(6) is satisfiable. This z has 00 or 11 pairs, so it does not encode any
assignment of the required form (NOT x1),x1,...,(NOT x4),x4.

The corrected last boilerplate string is distance 8 from z and removes
this counterexample. Parts (a–c), including the NP-completeness reduction,
remain correct. Only this one fixed witness was checked computationally;
see results/bookwise-closest504-fixed-witness.json.

Original Volume 4B typesetting and the corresponding September 23, 2015
author draft were inspected. Relevant current/historical 4B and Fascicle 6
errata contain no matching correction. Focused public searches found no
matching report, without establishing absolute priority. Details are in
sources/bookwise-closest-tuning-source-check.json.
