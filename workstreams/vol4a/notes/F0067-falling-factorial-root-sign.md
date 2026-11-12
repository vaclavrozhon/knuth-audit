# Wrong sign in the falling-factorial root expansion

**Location.** Volume 4A, first edition, first printing (2011), last
paragraph of answer 7.2.1.3–17, printed page 727 / file page 744.

Let x falling t denote x(x-1)...(x-t+1). The forward expansion for
y=(x falling t)^(1/t) has the wrong sign on its 1/x term. For fixed
t, the correct beginning is

    y = x - (t-1)/2 - (t^2-1)/(24x) + O(x^-2).

The printed coefficient has a plus sign. Already for t=2,

    sqrt(x(x-1)) = x sqrt(1-1/x)
                 = x - 1/2 - 1/(8x) + O(x^-2),

so the sign cannot be positive. The following inverse expansion in
the book,

    x = y + (t-1)/2 + (t^2-1)/(24y) + O(y^-3),

is correct and needs no change. Neither the exact unranking algorithm
nor that final approximation is invalidated.

The original page was inspected. No matching correction appears in
the screened current/historical 4A and Fascicle 3 errata or targeted
public searches. Absolute priority is not established. See
sources/combination-basics-source-check.json. No code was needed.
