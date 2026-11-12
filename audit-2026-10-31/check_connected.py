#!/usr/bin/env python3
"""Literal Algorithm R versus exhaustive subsets and polyomino growth.

TAOCP 4B, 7.2.2--75--78.  A is represented by an adjacency-list index;
len(adj[v]) represents Lambda.  Directed R4 implements exercise 77(d).
The weighted singleton fix is isolated by fix_singleton=False.
"""
import hashlib
import itertools as it
import json
from pathlib import Path
import random
import subprocess
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/connected'


def algorithm_r(adj, root, n=None, weights=None, low=0, high=1,
                fix_singleton=True, pretag=(), directed=False, tag=None,
                snapshots=None):
    N = len(adj)
    if tag is None:
        tag = [int(u in pretag) for u in range(N)]
    assert tag[root] == 0
    tag[root] = 1
    weighted = weights is not None
    w = weights[root] if weighted else 0
    solutions = []
    if weighted:
        if w >= high:
            return solutions, tag
        if not fix_singleton or w >= low:
            solutions.append((root,))
    elif n == 1:
        return [(root,)], tag
    vv = [None]*(N+1)
    ii = [None]*(N+1)
    aa = [None]*(N+1)
    vv[0], ii[0], aa[0] = root, 0, 0
    v, i, a, ell, step = root, 0, 0, 1, 4
    while True:
        if step == 2:
            assert i == ii[ell-1] and v == vv[i] and a == aa[ell-1]
            if weighted:
                assert w == sum(weights[u] for u in vv[:ell])
                if w >= low:
                    solutions.append(tuple(vv[:ell]))
            elif ell == n:
                solutions.append(tuple(vv[:ell]))
                if snapshots is not None:snapshots.append(tag.copy())
                ell = n-1
            step = 3
        elif step == 3:
            a += 1
            step = 4
        elif step == 4:
            if a != len(adj[v]):
                step = 5
            elif i == ell-1:
                step = 6
            else:
                i += 1
                v = vv[i]
                a = 0
                step = 4 if directed else 5
        elif step == 5:
            u = adj[v][a]
            tag[u] += 1
            if tag[u] > 1 or (weighted and w+weights[u] >= high):
                step = 3
            else:
                ii[ell], aa[ell], vv[ell] = i, a, u
                if weighted:
                    w += weights[u]
                ell += 1
                step = 2
        else:
            assert step == 6
            ell -= 1
            if ell == 0:
                break
            if weighted:
                w -= weights[vv[ell]]
            i = ii[ell]
            v = vv[i]
            for k in range(ell, i, -1):
                for u in adj[vv[k]]:
                    tag[u] -= 1
                    assert tag[u] >= 0
            for a in range(aa[ell]+1, len(adj[v])):
                tag[adj[v][a]] -= 1
                assert tag[adj[v][a]] >= 0
            a = aa[ell]
            step = 3
    return solutions, tag


def canonical(adj, subset, root):
    q = [root]
    seen = {root}
    for u in q:
        for v in adj[u]:
            if v in subset and v not in seen:
                seen.add(v)
                q.append(v)
    return tuple(q) if seen == subset else None


def brute(adj, root, n=None, weights=None, low=0, high=1, pretag=()):
    result = set()
    available = [u for u in range(len(adj)) if u != root and u not in pretag]
    for size in ([n] if n is not None else range(1, len(available)+2)):
        for rest in it.combinations(available, size-1):
            h = {root, *rest}
            if weights is not None and not low <= sum(weights[u] for u in h) < high:
                continue
            q = canonical(adj, h, root)
            if q is not None:
                result.add(q)
    return result


def graph(N, mask, directed=False):
    edges = list(it.permutations(range(N), 2) if directed
                 else it.combinations(range(N), 2))
    adj = [[] for _ in range(N)]
    for k, (u,v) in enumerate(edges):
        if mask >> k & 1:
            adj[u].append(v)
            if not directed:
                adj[v].append(u)
    return [sorted(row) for row in adj]


def grid(n, directed=False):
    adj = [[] for _ in range(n*n)]
    for y in range(n):
        for x in range(n):
            for dy,dx in ((0,1),(1,0)) if directed else ((-1,0),(0,-1),(0,1),(1,0)):
                if 0 <= y+dy < n and 0 <= x+dx < n:
                    adj[y*n+x].append((y+dy)*n+x+dx)
    return adj


def verify(adj, root, **kwargs):
    actual, tags = algorithm_r(adj, root, **kwargs)
    oracle_kwargs = {k:v for k,v in kwargs.items() if k in
                     ('n','weights','low','high','pretag')}
    expected = brute(adj, root, **oracle_kwargs)
    assert len(set(actual)) == len(actual)
    assert set(actual) == expected, (adj,root,kwargs,actual,expected)
    # Exercise 76's shortcut, except its explicitly separate n=1 case
    # and weighted early termination before adjacency scanning.
    if kwargs.get('n') != 1 and not (
        'weights' in kwargs and kwargs['weights'][root] >= kwargs['high']):
        for u in adj[root]:
            tags[u] -= 1
        assert tags == [int(u==root or u in kwargs.get('pretag',()))
                        for u in range(len(adj))]
    return len(actual)


def figure():
    book = ROOT.parent/'books/taocp-vol4b-ed1-print2-2022.pdf'
    with tempfile.TemporaryDirectory(prefix='knuth-vol4b-connected-') as d:
        trace = Path(d)/'trace.xml'
        subprocess.run(['mutool','draw','-q','-F','trace','-o',str(trace),str(book),'82'],
                       check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        tree = ET.parse(trace)
    rows,origins = [],[]
    for fill in tree.iter('fill_text'):
        t = list(map(float,fill.attrib['transform'].split()))
        for span in fill:
            glyphs = list(span)
            if ''.join(g.get('unicode','') for g in glyphs) != '01234':
                continue
            points = []
            for g in glyphs:
                x,y = float(g.attrib['x']),float(g.attrib['y'])
                points.append((t[0]*x+t[2]*y+t[4],t[1]*x+t[3]*y+t[5]))
            if not 350 < points[0][1] < 440:
                continue
            x0,y0 = points[0]
            # Cell spacing and offset from digit 0's origin to its circle's
            # center, measured from original vector paths (not raster OCR).
            q = tuple(round((y-y0)/10.423)*3+round((x-x0)/10.423) for x,y in points)
            rows.append(q)
            origins.append((x0+1.8198,y0-1.9192))
    assert len(rows) == 21
    adj = grid(3)
    snapshots=[]
    actual,_ = algorithm_r(adj,0,n=5,snapshots=snapshots)
    assert rows == actual
    dots=[set() for _ in rows]
    for path in tree.iter('stroke_path'):
        if path.get('linewidth')!='.96':continue
        t=list(map(float,path.get('transform').split()))
        points=[]
        for cmd in path:
            if cmd.tag in ('moveto','lineto'):
                x,y=float(cmd.get('x')),float(cmd.get('y'))
                points.append((t[0]*x+t[2]*y+t[4],t[1]*x+t[3]*y+t[5]))
        if not points or len(set(points))!=1:continue
        x,y=points[0]
        if not 350<y<455:continue
        matches=[]
        for i,(x0,y0) in enumerate(origins):
            c,r=round((x-x0)/10.423),round((y-y0)/10.423)
            if 0<=c<3 and 0<=r<3 and abs(x-x0-10.423*c)<.02 and abs(y-y0-10.423*r)<.02:
                matches.append((i,r*3+c))
        assert len(matches)==1,(x,y,matches)
        i,u=matches[0];dots[i].add(u)
    for row,tags,excluded in zip(rows,snapshots,dots):
        assert excluded=={u for u in range(9) if tags[u]>0 and u not in row}
    assert sum(map(len,dots))==45
    good = [i+1 for i,q in enumerate(rows) if canonical(grid(3,True),set(q),0)]
    assert set(range(1,22))-set(good) == {13,18}
    return {'book_sha256':hashlib.sha256(book.read_bytes()).hexdigest(),
            'source':'printed 62, PDF ordinal 82; original positioned glyphs',
            'canonical_orderings':rows,'excluded_dot_vertices':[sorted(s) for s in dots],
            'directed_reachable':good}


def polyomino_growth(limit):
    # Independent method: add a boundary square, normalize translation,
    # and deduplicate whole shapes. Rotations/reflections remain distinct.
    shapes = {((0,0),)}
    out = []
    for n in range(1,limit+1):
        placements = sum((n-max(x for x,y in h))*(n-max(y for x,y in h)) for h in shapes)
        out.append({'n':n,'fixed_shapes':len(shapes),'placements':placements})
        nxt = set()
        if n < limit:
            for h in shapes:
                s = set(h)
                boundary = {(x+dx,y+dy) for x,y in h
                            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]}-s
                for p in boundary:
                    g = s|{p}
                    x0 = min(x for x,y in g)
                    y0 = min(y for x,y in g)
                    nxt.add(tuple(sorted((x-x0,y-y0) for x,y in g)))
            shapes = nxt
    return out


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    result = {'status':'running','fixed_graph_cases':{},'weighted_graph_cases':0}
    for directed,limit in [(False,5),(True,4)]:
        cases = 0
        for N in range(1,limit+1):
            edges = N*(N-1) if directed else N*(N-1)//2
            for mask in range(1<<edges):
                adj = graph(N,mask,directed)
                for root in range(N):
                    for n in range(1,N+1):
                        verify(adj,root,n=n,directed=directed)
                        cases += 1
        result['fixed_graph_cases']['directed' if directed else 'undirected'] = cases
        print('fixed',directed,cases,flush=True)
    # Exhaustive weighted small graphs and ternary weights, including zero.
    for directed in (False,True):
        for N in range(1,4):
            edges = N*(N-1) if directed else N*(N-1)//2
            for mask in range(1<<edges):
                adj = graph(N,mask,directed)
                for weights in it.product(range(3),repeat=N):
                    for root in range(N):
                        for low in (-1,0,1,2,3):
                            for high in range(max(0,low),5):
                                verify(adj,root,weights=weights,low=low,high=high,
                                       directed=directed)
                                result['weighted_graph_cases'] += 1
    print('weighted',result['weighted_graph_cases'],flush=True)
    rng = random.Random(750078)
    for case in range(2000):
        N = rng.randrange(2,9)
        directed = bool(case%2)
        edges = N*(N-1) if directed else N*(N-1)//2
        adj = graph(N,rng.getrandbits(edges),directed)
        for row in adj:
            rng.shuffle(row)
        root = rng.randrange(N)
        pretag = tuple(u for u in range(N) if u!=root and rng.randrange(4)==0)
        weights = tuple(rng.randrange(4) for _ in range(N))
        low = rng.randrange(8)
        verify(adj,root,weights=weights,low=low,high=low+rng.randrange(7),
               directed=directed,pretag=pretag)
        verify(adj,root,n=rng.randrange(1,N+1),directed=directed,pretag=pretag)
    result['random_graphs'] = 2000
    result['figure'] = figure()
    expected = [1,4,22,113,571,2816,13616,64678,302574]
    result['grid_counts'] = []
    for n in range(1,10):
        adj = grid(n)
        count = 0
        # Exercise 76's carried-tag shortcut, not fresh pretag initialization.
        tags = [0]*(n*n)
        for root in range(n*n):
            assert tags == [int(u<root) for u in range(n*n)]
            rows,tags = algorithm_r(adj,root,n=n,tag=tags)
            assert len(set(rows)) == len(rows)
            count += len(rows)
            if n>1:
                for u in adj[root]:tags[u] -= 1
        assert count == expected[n-1]
        result['grid_counts'].append(count)
        print('grid',n,count,flush=True)
    result['polyomino_growth'] = polyomino_growth(9)
    assert [r['placements'] for r in result['polyomino_growth']] == expected
    bad,_ = algorithm_r([[1],[0]],0,weights=[1,1],low=2,high=3,fix_singleton=False)
    good,_ = algorithm_r([[1],[0]],0,weights=[1,1],low=2,high=3)
    assert bad == [(0,),(0,1)] and good == [(0,1)]
    result['F098'] = {'adj':[[1],[0]],'root':0,'weights':[1,1],
                      'L':2,'U':3,'printed':bad,'corrected':good}
    result['status'] = 'pass'
    (OUT/'verified.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',flush=True)


if __name__ == '__main__':main()
