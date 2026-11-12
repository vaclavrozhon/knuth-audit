# V4A-F0016: flipping the two extreme inputs can preserve decomposability

Confirmed, medium severity. Volume 4A, first edition, first printing
(2011), answer 7.1.2-75, second paragraph, printed page 576 /
file page 593. Original: `images/bookwise-p576.png`.

A nontrivial decomposition writes a Boolean function as g(Y,h(Z)),
where Y and Z partition its input variables, Y is nonempty, and Z has
at least two variables. The answer says that if f is decomposable,
then f XOR S_{0,n} is indecomposable. Here S_{0,n} is 1 precisely when
all n inputs are 0 or all n inputs are 1.

Take n=4 and f=x1 OR x2 OR x3 OR x4. Flipping its values at 0000 and
1111 gives

    f XOR S_{0,4} = NOT(x1 AND x2 AND x3 AND x4).

Both functions are decomposable with respect to the nontrivial
partition Y={x1,x2}, Z={x3,x4}. For f use h=x3 OR x4; for the changed
function use h=x3 AND x4 and g=NOT(x1 AND x2 AND h).

Thus the second paragraph's assertion of indecomposability needs a
qualification. Changing two truth-table entries can leave the result
decomposable. This does not refute the first paragraph about S_{0,n}
itself or the broader warning about approximately decomposable functions.

The current and historical Volume 4A errata and both Fascicle 0 layers
contain no matching correction. The nearby page-576 corrections apply
to answers 76 and 77. Two targeted public searches found no matching
report; absolute novelty is not established. See
`sources/extreme-flip-source-check.json`. No computation was needed.
