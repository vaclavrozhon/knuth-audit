# V4A-F0036: The clique restriction leaves necessary edges unset

Confirmed, low severity. Volume 4A, first edition, first printing
(2011), answer 7.1.4-130(b), printed page 642 / file 659.
Original: `images/bookwise-p642.png`.

Let C(m,r) mean that a graph on m vertices contains an r-clique,
where a clique is a set of pairwise adjacent vertices. The answer
restricts C(m,ceil(m/2)) by isolating vertices 1 through k and forcing
all edges between {k+1,...,ceil(m/2)} and {ceil(m/2)+1,...,m}.
It then identifies this restricted function with C(floor(m/2),k)
on the latter set of vertices. The identification also requires all
edges within the middle set {k+1,...,ceil(m/2)} to be present; the
printed restriction does not impose that condition.

For m=8 and k=2, isolate 1 and 2, join each of 3 and 4 to each of
5,6,7,8, and put only the edge 5--6 within the latter set. Leave
3--4 absent. All printed restrictions hold, and the latter four
vertices have a 2-clique. The full graph has no 4-clique: a clique
contains at most one of 3,4 and at most two of 5,6,7,8.

Repair: additionally make {k+1,...,ceil(m/2)} a clique. This restores
the intended equivalence. This is a missing condition in the printed
reduction, not a refutation of the lower bound. The known November
2011 correction to the bound in exercise 130(b) is separate and is
excluded from this finding.

Current and historical Volume 4A and Fascicle 1 errata were screened;
no matching correction or public report was located. See
`sources/bdd-size-source-check.json`. Absolute novelty is not
established. No computation was needed.
