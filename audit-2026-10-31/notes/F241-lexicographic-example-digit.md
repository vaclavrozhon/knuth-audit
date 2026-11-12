# F241 — The illustrative lower binary bound is missing a zero

Confirmed in Volume4B, answer433, printed634/file654; author draft270.
For the printed partial word x=1***10**1, its minimum completion is
100010001, not the displayed 10010001. Replace the lower bound in the
example accordingly. The argument then reads, in binary,

    100010001 <= x <= y <= 100001111,

which is impossible because the endpoints are273 and271. The printed
eight-bit lower bound is only145 and therefore does not give the intended
contradiction. The subsequent unit-propagation trace and the general
forcing proof are unaffected.

Original typesetting and the corresponding September23,2015 author draft
were inspected. Relevant current/historical 4B and Fascicle6 errata, including
available TeX sources, contain no correction of this answer. Focused public
searches found no relevant report; absence is not a guarantee of priority.
See sources/bookwise-automata-source-check.json.
