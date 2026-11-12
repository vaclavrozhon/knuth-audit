# V3-C0078 — The conversion between the two R functions has the wrong sign

Confirmed in volume 3, second edition, first printing (1998), printed
p.544 (file p.555), the sentence following equation (60).

Equation (55) on p.543 defines R(alpha,n), a two-argument function.
At alpha=1 its series starts n/(n+1). The one-argument R(n) from
volume 1, §1.2.11.3 equation (3), starts with 1 followed by precisely
that series. Therefore

    R(n) = 1 + R(1,n),

where the left side denotes volume 1's function. Page 544 instead
prints R(n)=R(1,n)-1.

This also contradicts the equations locally: at alpha=1, equation
(58) contains the factor 2+R(1,b), whereas equation (60) contains
R(b)+1. They agree with the plus sign, not the printed minus.
For b=1, the literal printed conversion would give a successful-search
mean of 3/2-1/e instead of 3/2.

Change the minus to plus. Equation (60) and its asymptotic expansion
are consistent with the actual volume 1 definition. That specific
definition was checked on volume 1 p.116; the completed volume 1
audit was otherwise left closed.

Original pp.543–544 and the cited definition inspected. No matching
correction located in official errata or limited public searches;
see `sources/hashing-errata-review.json`.
