#!/usr/bin/env python3
"""Finite local geometry certificates: all75 height order types, two zero conventions."""
from collections import Counter, defaultdict
from itertools import combinations, product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
directions = [(axis,sign) for axis in range(3) for sign in (-1,1)]

def local_link(matrix,x,y,z):
    m,n = len(matrix),len(matrix[0])
    def occupied(signs):
        i,j = x-(signs[0]<0),y-(signs[1]<0)
        h = matrix[i][j] if 0 <= i < m and 0 <= j < n else 0
        return z > 0 and h >= z if signs[2] < 0 else h > z
    edges = []
    for a,b in combinations(directions,2):
        if a[0] == b[0]:continue
        missing = 3-a[0]-b[0]
        signs = [0]*3
        signs[a[0]],signs[b[0]] = a[1],b[1]
        signs[missing] = -1
        minus = occupied(signs)
        signs[missing] = 1
        if minus != occupied(signs):edges.append((a,b))
    adjacency = defaultdict(list)
    for a,b in edges:adjacency[a].append(b);adjacency[b].append(a)
    if not edges:return {'kind':'interior_or_exterior','edge_rays':[]}
    edge_rays = [v for v,ns in adjacency.items() if len(ns) != 2 or ns[0][0] != ns[1][0]]
    if any(len(ns) != 2 for ns in adjacency.values()):
        return {'kind':'nonmanifold_edge','edge_rays':edge_rays,'link_edges':edges}
    reached = set()
    stack = [next(iter(adjacency))]
    while stack:
        v = stack.pop()
        if v in reached:continue
        reached.add(v);stack.extend(adjacency[v])
    if len(reached) != len(adjacency):return {'kind':'nonmanifold_point','edge_rays':edge_rays,'link_edges':edges}
    c = len(edge_rays)
    if c == 0:kind = 'face_interior'
    elif c == 2 and edge_rays[0][0] == edge_rays[1][0] and edge_rays[0][1] == -edge_rays[1][1]:kind = 'edge_interior'
    elif c == 3:kind = 'trihedral_vertex'
    else:kind = f'vertex_with_{c}_edges'
    return {'kind':kind,'edge_rays':edge_rays,'link_edges':edges}

def inspect(matrix):
    m,n = len(matrix),len(matrix[0])
    failures,vertices = [],[]
    for x,y in product(range(m+1),range(n+1)):
        heights = {0}
        heights.update(matrix[i][j] for i in (x-1,x) for j in (y-1,y) if 0 <= i < m and 0 <= j < n)
        for z in sorted(heights):
            link = local_link(matrix,x,y,z)
            if link['kind'] == 'trihedral_vertex':vertices.append((x,y,z))
            elif link['kind'] not in ('interior_or_exterior','face_interior','edge_interior'):
                failures.append({'point':[x,y,z],**link})
    return failures,vertices

def case_of(h):
    high = max(h)
    positions = [i for i,v in enumerate(h) if v == high]
    adjacent = lambda i,j: (i//2 == j//2) != (i%2 == j%2)
    if len(positions) >= 3:return 1
    if len(positions) == 2:return 2 if adjacent(*positions) else None
    others = [v for v in h if v != high]
    if len(set(others)) == 1:return 3
    second = max(others)
    second_positions = [i for i,v in enumerate(h) if v == second]
    if len(second_positions) == 1 and adjacent(positions[0],second_positions[0]):return 4
    return None

def order_certificate():
    records = []
    rank_counts = Counter()
    case_rank_counts = Counter()
    for k in range(1,5):
        for h in product(range(k),repeat=4):
            if set(h) != set(range(k)):continue
            case = case_of(h)
            for shift in (0,1):
                matrix = [[h[0]+shift,h[1]+shift],[h[2]+shift,h[3]+shift]]
                failures,vertices = inspect(matrix)
                assert bool(case) == (not failures), (matrix,case,failures)
                records.append({'rank_pattern':h,'minimum_height':shift,'case':case,'failures':failures,
                                'vertices':len(vertices)})
            if case:
                rank_counts[k] += 1
                case_rank_counts[case,k] += 1
    assert dict(rank_counts) == {1:1,2:12,3:16,4:16}
    assert len(records) == 150
    return records,rank_counts,case_rank_counts

def boundary_geometry(matrix):
    cubes = {(i,j,k) for i,row in enumerate(matrix) for j,h in enumerate(row) for k in range(h)}
    squares = []
    for cube in sorted(cubes):
        for axis,sign in directions:
            neighbor = list(cube);neighbor[axis] += sign
            if tuple(neighbor) in cubes:continue
            plane = cube[axis]+(sign>0)
            free = [a for a in range(3) if a != axis]
            corners = []
            for u,v in ((0,0),(1,0),(1,1),(0,1)):
                point = list(cube);point[axis] = plane
                point[free[0]] += u;point[free[1]] += v
                corners.append(tuple(point))
            squares.append({'plane':(axis,plane,sign),'corners':corners})
    edge_squares = defaultdict(list)
    for index,square in enumerate(squares):
        corners = square['corners']
        for a,b in zip(corners,corners[1:]+corners[:1]):edge_squares[tuple(sorted((a,b)))].append(index)
    parent = list(range(len(squares)))
    def representative(a):
        while parent[a] != a:a = parent[a]
        return a
    for es in edge_squares.values():
        assert len(es) == 2
        a,b = es
        if squares[a]['plane'] == squares[b]['plane']:parent[representative(a)] = representative(b)
    components = defaultdict(list)
    for i in range(len(squares)):components[representative(i)].append(i)
    face_ids = {root:index for index,root in enumerate(components)}
    boundary_edges = {}
    for edge,ss in edge_squares.items():
        fs = sorted({face_ids[representative(s)] for s in ss})
        if len(fs) == 2:boundary_edges[edge] = fs
    adjacency = defaultdict(list)
    for a,b in boundary_edges:adjacency[a].append(b);adjacency[b].append(a)
    vertices = {v for v,ns in adjacency.items() if len(ns) != 2}
    assert all(len(adjacency[v]) == 3 for v in vertices)
    for v,ns in adjacency.items():
        if v not in vertices:assert all(ns[0][k]+ns[1][k] == 2*v[k] for k in range(3))
    _,local_vertices = inspect(matrix)
    assert vertices == set(local_vertices)
    long_edges = set()
    for a in vertices:
        for b in adjacency[a]:
            prev,now = a,b
            while now not in vertices:
                nxt = next(v for v in adjacency[now] if v != prev)
                prev,now = now,nxt
            long_edges.add(tuple(sorted((a,now))))
    faces = []
    for root,square_ids in components.items():
        face = face_ids[root]
        segments = [edge for edge,fs in boundary_edges.items() if face in fs]
        badj = defaultdict(list)
        for a,b in segments:badj[a].append(b);badj[b].append(a)
        assert all(len(ns) == 2 for ns in badj.values())
        remaining = set(badj)
        loops = []
        while remaining:
            start = min(remaining);prev = None;now = start;loop = []
            while True:
                remaining.remove(now)
                if now in vertices:loop.append(now)
                nxt = next(v for v in badj[now] if v != prev)
                prev,now = now,nxt
                if now == start:break
            assert len(loop) >= 4
            loops.append(loop)
        faces.append({'face':face,'plane_axis_coordinate_normal':squares[root]['plane'],
                      'unit_squares':len(square_ids),'boundary_loops':loops})
    return {'matrix':matrix,'vertices':sorted(vertices),'edges':sorted(long_edges),'faces':faces,
            'counts':{'vertices':len(vertices),'edges':len(long_edges),'faces':len(faces)}}

if __name__ == '__main__':
    records,rank_counts,case_rank_counts = order_certificate()
    histoscape = boundary_geometry([[4,3],[1,2]])
    assert histoscape['counts'] == {'vertices':20,'edges':30,'faces':12}
    identity = local_link([[1,0],[0,1]],1,1,1)
    assert identity['kind'] == 'nonmanifold_edge' and len(identity['edge_rays']) == 5
    six_faces = local_link([[3,2],[2,1]],1,1,2)
    four_faces = local_link([[3,2],[1,2]],1,1,2)
    assert six_faces['kind'] == 'vertex_with_6_edges'
    assert four_faces['kind'] == 'vertex_with_4_edges'
    assert not inspect([[1,1],[0,1]])[0]
    assert inspect([[2,1],[0,1]])[0]
    result = {'scope':'Complete local geometry for75 ordered height types, with zero or positive minimum; explicit Fig.101(d) boundary geometry.',
              'proof':'notes/histoscapes-and-exercise-027.md',
              'criterion':'At each grid point, intersect local occupied octants with a small octahedron. Boundary link must be one cycle; after merging coplanar sectors it has zero, two opposite, or three corners.',
              'valid_rank_counts':dict(rank_counts),'case_rank_counts':{f'{c},{k}':v for (c,k),v in case_rank_counts.items()},
              'order_types':records,'identity_at_111':identity,'six_face_example':six_faces,'four_face_example':four_faces,
              'fig101d':histoscape,'arithmetic':'Integer incidence only.150 fixed order types; no enumeration of10000 matrices or8×8 census.'}
    (ROOT/'results/histoscape-local.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'order_type_checks':len(records),'valid_rank_counts':dict(rank_counts),'fig101d':histoscape['counts']}))
