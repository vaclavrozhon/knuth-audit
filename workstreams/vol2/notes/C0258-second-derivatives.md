# V2-C0258: the claimed bound for all second partial derivatives is false

Confirmed false complexity claim, medium impact. Third edition, first
printing, answer 4.6.4-71, printed 718/file 730, final sentence. The
question is on printed 524. Original typesetting inspected on
10 November 2026.

The answer claims that repeating the first-derivative construction
computes all second partial derivatives with at most 9m+3d chain
multiplications and 4d divisions, when the original scalar function
uses m chain multiplications and d divisions. A chain multiplication
multiplies two quantities that depend on the input variables;
multiplication by a fixed parameter is not counted.

Take the polynomial f(x1,...,x20)=x1*x2*...*x20 over the real numbers.
It can be computed with m=19 and d=0. For every pair i<j its mixed
second derivative is

    d²f/(dx_i dx_j) = product of x_k over k outside {i,j}.

These are 190 distinct monomials of degree 18. They are linearly
independent even after passing to the quotient by the vector space
of affine polynomials (constants and linear forms in the inputs).

Initially a polynomial chain contains only affine polynomials.
Addition, subtraction and multiplication by a constant do not enlarge
the linear span of the quantities already known. Each chain
multiplication introduces at most one new vector into that span.
Thus producing these 190 independent nonlinear outputs requires at
least 190 chain multiplications. The asserted limit is only

    9*19+3*0 = 171, with no divisions.

This contradiction uses exactly the book's cost model and ordinary
nonzero multivariate polynomials. It is independent of any numerical
rounding or derivative evaluation point. For a general product of n
variables the same lower bound is binom(n,2), which exceeds 9(n-1)
whenever n>18.

The reverse differentiation argument proves the requested bound for
the function and all its **first** derivatives. Applying that scalar
argument again to one selected first derivative gives a row of the
matrix of second derivatives, not all rows at once. The last sentence
should be removed or replaced by an appropriately qualified bound;
no sharp replacement complexity is claimed in this note.

There is also a local index typo in the first-derivative formula:
its initial term p1' * y_r should be p1' * y1. For example, with
g1=x1*x2 and g2=g1*x3=f, differentiating with respect to x1 requires
y1=x2*x3, whereas the printed y_r=y2 is x3. This is separate from
the false second-derivative conclusion.

All official current and historical third-edition lists were checked.
The older second-edition list introduces the same answer as new answer
68 on page 655, including both defective statements; it does not
identify or correct either error. Targeted public searches concerning
Knuth, exercise 4.6.4-71, Hessians and second derivatives found no
matching correction. Absolute priority and later physical printings
are unverified. No report sent; no computation is needed.
