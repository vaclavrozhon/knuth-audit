# C048: The printed prime-number error exponent needs clarification

Candidate only. TAOCP4B p388/file408, notes following MPR113.
The original PDF and the author's Pre-Fascicle5A p45/file51 both
print ψ(n)=n+O(n exp(−C log n)) for a positive constant C.
There is no square root in either source.

For any fixed logarithm base, the printed expression is a fixed
power saving O(n^(1−δ)) for some δ>0. A change of logarithm base
cannot explain the difference from a square-root exponent.

The primary comparison source, Trudgian's arXiv:1401.2689v2,
Theorem1 on p3, bounds |ψ(x)−x| by
x sqrt(8/(17π)) X^(1/2) exp(−X), where
X=sqrt((ln x)/6.455), for x≥23. Its exponential scale is
exp(−c sqrt(ln x)); it does not establish the printed stronger bound.

This is not a counterexample to the stronger statement. No proof of
its falsehood is claimed, and no finite calculation can by itself
settle an asymptotic bound with unspecified constants. A missing
square root is a plausible intended correction, pending assessment
of the intended theorem and the cited historical source.

The six local errata layers and three TeX sources contain no
applicable correction. The historical1896 article has not been
fully assessed. The complete exercise remains partial specifically
for this mathematical note; its combinatorial parts, the Θ(n)
growth bounds and the exact LCM value are independently proved.

Evidence: `sequential-mpr-ex113.md`, original images `ref-408.png`,
`mpr113-notes-detail.png`, `fasc5a-51.png`, and the saved primary
paper `sources/trudgian-2014-pnt.pdf` with image `trudgian-2014-03.png`.
