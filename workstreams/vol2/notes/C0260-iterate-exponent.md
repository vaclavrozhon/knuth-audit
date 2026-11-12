# V2-C0260: reversed exponent in the elementary iterate formula

Confirmed formula error, low impact. Third edition, first printing,
answer 4.7-15, printed 722/file 734. Original typesetting inspected on
10 November 2026; the question is on printed 534.

Here U^[n] denotes n successive compositions of U with itself. The
answer correctly integrates U'(z)/U(z)^k=1/z^k to obtain

    U(z)^(1-k) = z^(1-k) + c.

Consequently the nth iterate satisfies

    U^[n](z)^(1-k) = z^(1-k) + n*c,
    U^[n](z) = z / (1+n*c*z^(k-1))^(1/(k-1)).

The last displayed expression in the first paragraph instead has
z^(1-k) inside the parentheses. That exponent must be k-1; the
preceding integrated equation is correct and stays unchanged.

For a concrete check take k=2 and U(z)=z/(1+z). Then c=1 and
U'(z)/U(z)^2=1/z^2. At n=1 the printed formula returns
z/(1+z^(-1))=z^2/(1+z), whose linear coefficient is zero. It should
return U(z), whose linear coefficient is one. The corrected formula
z/(1+n*z) also verifies the iteration law directly.

All relevant third-edition errata and the older second-edition list
were screened; no correction of this exponent was found. The old
list introduces answer 15 on its page 658, rather than correcting
this defect. Targeted public searches for the exercise, page 722,
iteration and errata found the printed formula but no matching error
report. Absolute priority and later physical printings are unverified.
No report sent and no computation needed.
