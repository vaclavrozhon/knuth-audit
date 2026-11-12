#!/usr/bin/env python3
"""Exact, bounded certificate for all geometry in exercise 26; no search."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
names = '023 134 245 356 460 501 612 054 165 206 310 421 532 643'.split()
planes = [(0,0,1,0),(0,4,1,200),(2,0,1,-280),(5,-5,7,-700),
          (-5,5,7,-700),(-2,0,1,-280),(0,-4,1,200)]
printed = [(-140,0,0),(75,75,-100),(0,252,-280),(40,-100,-200),
           (90,-50,0),(140,50,0),(-240,0,200),(140,0,0),(240,0,200),
           (-140,-50,0),(-90,50,0),(-40,100,-200),(0,-252,-280),(-75,-75,-100)]

def det(a):
    return sum(a[0][j]*(a[1][(j+1)%3]*a[2][(j+2)%3]
                       -a[1][(j+2)%3]*a[2][(j+1)%3]) for j in range(3))

vertices, determinants = {}, {}
for name,want in zip(names,printed):
    ps = [planes[int(i)] for i in name]
    mat = [p[:3] for p in ps]
    denominator = det(mat)
    assert denominator
    point = tuple(F(det([[ps[i][3] if j == col else mat[i][j]
                          for j in range(3)] for i in range(3)]),denominator)
                  for col in range(3))
    assert point == want
    vertices[name] = point
    determinants[name] = denominator
assert len(set(vertices.values())) == 14

oriented_pairs = [(s[i],s[(i+1)%3]) for s in names for i in range(3)]
assert sorted(oriented_pairs) == [(str(i),str(j)) for i,j in product(range(7),repeat=2) if i != j]
edges = {(i,j):[s for s in names if str(i) in s and str(j) in s]
         for i,j in combinations(range(7),2)}
assert all(len(e) == 2 for e in edges.values())
faces = {}
for face in range(7):
    ns = [s for s in names if str(face) in s]
    assert len(ns) == 6
    adjacency = {s:[t for t in ns if s != t and len(set(s)&set(t)) == 2] for s in ns}
    assert all(len(v) == 2 for v in adjacency.values())
    cycle = [ns[0],adjacency[ns[0]][0]]
    while len(cycle) < 6:
        cycle.append(next(t for t in adjacency[cycle[-1]] if t != cycle[-2]))
    assert len(set(cycle)) == 6 and cycle[0] in adjacency[cycle[-1]]
    faces[face] = cycle

def matches_cycle(a,b):
    return any(a == c[k:]+c[:k] for c in (b,list(reversed(b))) for k in range(len(b)))
assert matches_cycle(faces[0],'023 310 501 054 460 206'.split())
assert matches_cycle(faces[1],'134 421 612 165 501 310'.split())
assert matches_cycle(faces[6],'612 206 460 643 356 165'.split())

def project(point,face):
    omit = next(i for i in range(3) if planes[face][i])
    return tuple(x for i,x in enumerate(point) if i != omit)
def orient(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def on_segment(p,a,b):
    return orient(a,b,p) == 0 and all(min(a[k],b[k]) <= p[k] <= max(a[k],b[k]) for k in range(2))
def segments_intersect(a,b,c,d):
    o1,o2,o3,o4 = orient(a,b,c),orient(a,b,d),orient(c,d,a),orient(c,d,b)
    if o1*o2 < 0 and o3*o4 < 0:return True
    return any(v == 0 and on_segment(p,u,w)
               for v,p,u,w in [(o1,c,a,b),(o2,d,a,b),(o3,a,c,d),(o4,b,c,d)])
def polygon_contains(point,polygon):
    if any(on_segment(point,a,b) for a,b in zip(polygon,polygon[1:]+polygon[:1])):return True
    inside = False
    x,y = point
    for a,b in zip(polygon,polygon[1:]+polygon[:1]):
        if (a[1] > y) != (b[1] > y):
            crossing = a[0]+(y-a[1])*(b[0]-a[0])/(b[1]-a[1])
            if crossing > x:inside = not inside
    return inside

face_checks = []
for face,cycle in faces.items():
    polygon = [project(vertices[s],face) for s in cycle]
    for k in range(6):assert orient(polygon[k-1],polygon[k],polygon[(k+1)%6]) != 0
    pairs_checked = []
    for a,b in combinations(range(6),2):
        if (a-b)%6 in (1,5):continue
        assert not segments_intersect(polygon[a],polygon[(a+1)%6],polygon[b],polygon[(b+1)%6])
        pairs_checked.append([a,b])
    face_checks.append({'face':face,'cycle':cycle,'nonadjacent_edge_pairs_disjoint':pairs_checked})

def merge(intervals):
    result = []
    for a,b in sorted(intervals):
        if result and a <= result[-1][1]:result[-1][1] = max(result[-1][1],b)
        else:result.append([a,b])
    return result
def line_in_face(face,other,base,direction,coordinate):
    polygon3 = [vertices[s] for s in faces[face]]
    polygon2 = [project(p,face) for p in polygon3]
    plane = planes[other]
    def value(p):return sum(a*x for a,x in zip(plane[:3],p))-plane[3]
    def parameter(p):return (p[coordinate]-base[coordinate])/direction[coordinate]
    crossings = set()
    for a,b in zip(polygon3,polygon3[1:]+polygon3[:1]):
        va,vb = value(a),value(b)
        if va == 0:crossings.add(parameter(a))
        if vb == 0:crossings.add(parameter(b))
        if va*vb < 0:
            u = va/(va-vb)
            crossings.add(parameter(tuple(x+u*(y-x) for x,y in zip(a,b))))
    points = sorted(crossings)
    assert len(points) >= 2
    intervals = [[t,t] for t in points]
    for a,b in zip(points,points[1:]):
        midpoint = tuple(x+(a+b)/2*d for x,d in zip(base,direction))
        if polygon_contains(project(midpoint,face),polygon2):intervals.append([a,b])
    return merge(intervals),points

intersections = []
for (i,j),edge in edges.items():
    a,b = map(vertices.__getitem__,edge)
    direction = tuple(y-x for x,y in zip(a,b))
    coordinate = next(k for k,d in enumerate(direction) if d)
    first,breaks_i = line_in_face(i,j,a,direction,coordinate)
    second,breaks_j = line_in_face(j,i,a,direction,coordinate)
    common = merge([[max(x,u),min(y,v)] for x,y in first for u,v in second if max(x,u) <= min(y,v)])
    assert common == [[0,1]], (i,j,common)
    intersections.append({'faces':[i,j],'shared_edge':edge,'line_parameter':'first endpoint + t(second−first)',
                          'first_face_breakpoints':breaks_i,'second_face_breakpoints':breaks_j,
                          'first_face_line_intervals':first,'second_face_line_intervals':second,
                          'intersection':common})

# A consistent choice of cyclic orientations is a separate combinatorial check.
def edge_direction(cycle,edge):
    a,b = edge
    if cycle[(cycle.index(a)+1)%6] == b:return 1
    assert cycle[(cycle.index(b)+1)%6] == a
    return -1
orientations = {0:1}
for j in range(1,7):
    edge = edges[0,j]
    orientations[j] = -edge_direction(faces[0],edge)*edge_direction(faces[j],edge)
for (i,j),edge in edges.items():
    assert orientations[i]*edge_direction(faces[i],edge) == -orientations[j]*edge_direction(faces[j],edge)
for s in names:
    incident = [e for e in edges.values() if s in e]
    assert len(incident) == 3
    assert len({t for e in incident for t in e if t != s}) == 3

def encode(x):
    if isinstance(x,F):return int(x) if x.denominator == 1 else str(x)
    raise TypeError(type(x).__name__)
result = {'scope':'All fourteen listed vertices; seven simple planar hexagons; all twenty-one face intersections exactly their common edges.',
          'proof':'notes/szilassi-and-exercise-026.md','planes_ax_by_cz_rhs':planes,
          'vertices':vertices,'triple_determinants':determinants,
          'oriented_pairs':oriented_pairs,'faces':face_checks,'face_intersections':intersections,
          'consistent_cycle_orientation_signs':orientations,'counts':{'vertices':14,'edges':21,'faces':7},
          'arithmetic':'Exact integer/Fraction arithmetic. No sampling, approximate geometry, or enumeration of possible realizations.'}
(ROOT/'results/szilassi-exact.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=encode)+'\n')
print(json.dumps({'vertices':len(vertices),'simple_hexagons':len(faces),'exact_shared_edge_intersections':len(intersections)}))
