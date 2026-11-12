#!/usr/bin/env python3
"""Trace corrected answer30 on its ring example and the fixed replacement29."""
from pathlib import Path
import json
from check_histoscape_local import boundary_geometry

ROOT = Path(__file__).resolve().parent
def canonical(cycle):
    cycle = [tuple(p) for p in cycle]
    return min(tuple(c[k:]+c[:k]) for c in (cycle,list(reversed(cycle))) for k in range(len(c)))

def extract(matrix):
    m,n = len(matrix),len(matrix[0]);t = max(map(max,matrix))+1
    bounds = (2*m,2*n,2*t-2)
    marked = {(2*i+1,2*j+1,2*k+1):1 for i,row in enumerate(matrix) for j,h in enumerate(row) for k in range(h)}
    phase_counts = {3:len(marked)}
    for dimension in (3,2,1):
        sources = [p for p,v in marked.items() if v == 1 and sum(x%2 for x in p) == dimension]
        for p in sources:
            for axis in range(3):
                if p[axis]%2 == 0:continue
                for direction in (-1,1):
                    neighbor = list(p);neighbor[axis] += 2*direction
                    if not marked.get(tuple(neighbor),0):
                        boundary = list(p);boundary[axis] += direction
                        assert all(0 <= x <= lim for x,lim in zip(boundary,bounds))
                        marked[tuple(boundary)] = 1
        phase_counts[dimension-1] = sum(sum(x%2 for x in p) == dimension-1 for p in marked)
    vertices2 = sorted(p for p in marked if not any(x%2 for x in p))
    polygons = []
    for fixed_axis in range(3):
        walk_marks = dict(marked)
        axes = [a for a in range(3) if a != fixed_axis]
        for start in vertices2:
            if walk_marks[start] != 1:continue
            point = start
            cycle = []
            while walk_marks[point] == 1:
                for axis in axes:
                    cycle.append(tuple(x//2 for x in point))
                    walk_marks[point] = 2
                    ahead = list(point);ahead[axis] += 1
                    delta = 2 if walk_marks.get(tuple(ahead),0) else -2
                    while True:
                        point = tuple(x+delta if a == axis else x for a,x in enumerate(point))
                        assert all(0 <= x <= lim for x,lim in zip(point,bounds))
                        if walk_marks.get(point,0):break
            assert point == start and len(cycle)%2 == 0
            polygons.append({'fixed_axis':fixed_axis,'fixed_coordinate':start[fixed_axis]//2,'vertices':cycle})
        assert all(walk_marks[p] == 2 for p in vertices2)
    return {'matrix':matrix,'allocated_shape':[x+1 for x in bounds],
            'phase_counts_by_cell_dimension':phase_counts,'vertices':[tuple(x//2 for x in p) for p in vertices2],
            'boundary_polygons':polygons}

ring = [[1,1,1],[1,0,1],[1,1,1]]
printed_vertices = '000 001 030 031 110 111 120 121 210 211 220 221 300 301 330 331'.split()
printed_cycles = ['000 030 031 001','110 120 121 111','210 220 221 211','300 330 331 301',
                  '000 001 301 300','030 031 331 330','110 111 211 210','120 121 221 220',
                  '000 300 330 030','001 301 331 031','110 210 220 120','111 211 221 121']
decode = lambda s:tuple(map(int,s))
r = extract(ring)
assert r['vertices'] == sorted(map(decode,printed_vertices))
assert {canonical(p['vertices']) for p in r['boundary_polygons']} == {canonical(list(map(decode,s.split()))) for s in printed_cycles}
geometry = boundary_geometry(ring)
assert {canonical(c) for f in geometry['faces'] for c in f['boundary_loops']} == {canonical(p['vertices']) for p in r['boundary_polygons']}
assert geometry['counts'] == {'vertices':16,'edges':24,'faces':10}
replacement = next(w for w in json.loads((ROOT/'results/histoscape-witnesses.json').read_text())['witnesses'] if w['source']=='public_replacement')['geometry']
s = extract(replacement['matrix'])
assert s['vertices'] == [tuple(v) for v in replacement['vertices']]
assert {canonical(p['vertices']) for p in s['boundary_polygons']} == {canonical(c) for f in replacement['faces'] for c in f['boundary_loops']}
empty = extract([[0]])
assert not empty['vertices'] and not empty['boundary_polygons']
(ROOT/'results/histoscape-extraction.json').write_text(json.dumps({
    'scope':'Every printed ring vertex and all twelve printed polygon cycles; corrected answer30 marking/tracing on that ring, one fixed8×8 witness, and empty input.',
    'proof':'notes/histoscape-extraction-and-exercise-030.md','ring':r,'ring_geometry':geometry,
    'replacement29':s,'empty':empty,
    'interpretation':'Each marking pass iterates over marked cells of the specified parity. Vertex visitation flags are reset for each of the three polygon orientations.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ring_vertices':len(r['vertices']),'ring_polygons':len(r['boundary_polygons']),
                  'replacement_vertices':len(s['vertices']),'replacement_polygons':len(s['boundary_polygons']),
                  'empty_polygons':len(empty['boundary_polygons'])}))
