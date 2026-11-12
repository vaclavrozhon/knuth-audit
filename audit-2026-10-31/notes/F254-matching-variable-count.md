# F254 — The matching encoding has 5n variables

**Location:** TAOCP 4B, first edition, second printing (2022), answer
7.2.2.2–525, printed p. 654 / PDF page 674, last line. Also in the
23 September 2015 fasc6a draft, printed p. 291.

**Correction:** Replace “3n variables” by “5n variables”.

The exact-cover instance has 3n items and 5n options; each option is a
triple containing one item in each of three classes of size n. The SAT
encoding uses one variable per option. At-most-one constraints for the
n items of one class give n*C(5,2)=10n binary clauses. At-least-one
constraints for the other two classes give 2n clauses of length five.
They force at least n selected options, while the first class allows at
most n; hence exactly n options cover every item once. Thus the printed
clause count and 30n literal occurrences are correct, but the number
of option variables is 5n. At n=40 it is 200, not 120.

This is a local size-description error, not a counterexample to the
reduction or its satisfiability equivalence. Original typesetting in
both editions was inspected. The known F6 erratum of 21 June 2022
rephrases rows and columns as options and items without changing this
incorrect variable count. No matching correction was found in the
checked current/historical errata or public searches.
