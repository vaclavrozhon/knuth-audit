"""New bounded path and ZDD witnesses. Successful outputs are immutable."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
import json
import os
import re
import subprocess
import time
from puzzle_xcc import encode, native_text, save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/zdd261_264'
BIN = Path('/tmp/knuth-vol4b-zdd-qw7qwwga/dlx6')


def path_family(vertices, edges, sources, sinks, m, prescribed=False):
    outgoing = {v: [] for v in vertices}
    for u, v in edges:
        outgoing[u].append(v)
    def paths(v):
        if v in sinks:
            return [(v,)]
        return [(v,) + q for w in outgoing[v] for q in paths(w)]
    by_source = {s: [p for p in paths(s) if not prescribed or p[-1] == sinks[sources.index(s)]] for s in sources}
    found = set()
    def visit(chosen_sources, used, arcset):
        if not chosen_sources:
            found.add(tuple(sorted(arcset)))
            return
        for p in by_source[chosen_sources[0]]:
            if not used.intersection(p):
                visit(chosen_sources[1:], used | set(p), arcset + list(zip(p, p[1:])))
    for chosen in combinations(sources, m):
        visit(chosen, set(), [])
    return found


def path_xcc(vertices, edges, sources, sinks, m, prescribed=False):
    vi = {v: i for i, v in enumerate(vertices)}
    prim = [f'{vi[v]}{d}' for v in vertices for d in '-+' if v not in (sources if d == '-' else sinks)]
    sec = [f'v{vi[v]}' for v in vertices]
    rows, arcs = [], []
    def add(row, arc=None):
        # Integers 1,2,... encode literal colors '0','1',...; zero is blank.
        if prescribed:
            endpoints = dict(zip(sources, range(1, m+1))) | dict(zip(sinks, range(1, m+1)))
            for v, k in endpoints.items():
                if (f'v{vi[v]}' in dict(row) and dict(row)[f'v{vi[v]}'] != k+1):
                    return
        rows.append(row); arcs.append(arc)
    for u, v in edges:
        for k in range(1, m+1):
            add([(f'{vi[u]}+', 0), (f'{vi[v]}-', 0), (f'v{vi[u]}', k+1), (f'v{vi[v]}', k+1)], (u, v))
    for v in vertices:
        for d in '-+':
            if v not in (sources if d == '-' else sinks):
                add([(f'{vi[v]}{d}', 0), (f'v{vi[v]}', 1)])
    if not prescribed:
        for k, s in enumerate(sources, 1):
            prim.append(f'x{k}'); sec.append(f'y{k}')
            for j in range(k):
                for chosen in [False, True]:
                    level = j + chosen
                    if k == len(sources) and level != m:
                        continue
                    row = [(f'x{k}', 0), (f'v{vi[s]}', level+1 if chosen else 1), (f'y{k}', level+1)]
                    if k > 1:
                        row.append((f'y{k-1}', j+1))
                    add(row)
    return encode(prim, sec, rows), arcs


def native(label, enc):
    inp, log, zdd = [OUT / (label + suffix) for suffix in ['.xcc', '.log', '.zdd']]
    content = native_text(enc)
    cmd = [str(BIN), 'v1', 'm1', 'd0', 'T100000000']
    reused = inp.exists()
    elapsed = None
    if reused:
        assert inp.read_text() == content
    else:
        inp.write_text(content)
        start = time.monotonic()
        p = subprocess.run(cmd, input=content, text=True, capture_output=True, timeout=10)
        log.write_text(p.stderr); zdd.write_text(p.stdout)
        save(OUT/(label+'-terminal.json'), dict(command=cmd,returncode=p.returncode,elapsed_seconds=time.monotonic()-start,nice=os.getpriority(os.PRIO_PROCESS,0)))
        assert p.returncode == 0
        elapsed = time.monotonic()-start
    stderr, stdout = log.read_text(), zdd.read_text()
    assert 'Altogether ' in stderr and 'TIMEOUT' not in stderr and 'overflow' not in stderr.lower()
    nodes = {int(a,16): (int(b),int(c,16),int(d,16)) for a,b,c,d in re.findall(r'([0-9a-f]+): \(~(\d+)\?([0-9a-f]+):([0-9a-f]+)\)',stdout)}
    @lru_cache(None)
    def walk(i):
        if i == 0: return frozenset()
        if i == 1: return frozenset([()])
        v,l,h = nodes[i]
        if v == 0: return walk(h)
        return walk(l) | frozenset(tuple(sorted(q+(v-1,))) for q in walk(h))
    family = walk(max(nodes))
    count = int(re.search(r'Altogether (\d+) solution',stderr)[1])
    assert count == len(family)
    stats = dict(count=count,nodes=int(re.search(r'(\d+) ZDD node',stderr)[1]),
                 signatures=sum(map(int,re.search(r'(\d+)\+(\d+) signatures',stderr).groups())),elapsed_seconds=elapsed,reused_saved_terminal=reused)
    return stats,nodes,family


def triangle(n):
    v = [(i,j) for i in range(n+1) for j in range(i,n+1) if (i,j) not in [(0,0),(0,n),(n,n)]]
    e = [(u,w) for u in v for w in [(u[0]+1,u[1]),(u[0],u[1]-1)] if w in v]
    s = [(0,j) for j in range(1,n)] + [(i,n) for i in range(1,n)]
    t = [(i,i) for i in range(1,n)]
    # The named boundary vertices are sources: suppress incoming boundary arcs.
    # A literal reading retaining those arcs is audited separately.
    return v,[(u,w) for u,w in e if w not in s],s,t


def uncolored_model(enc, first=False):
    masks=[sum(1<<(i-1) for i,c in row) for row in enc['rows']]
    primary=(1<<enc['primary'])-1
    instructions={};memo={}
    def visit(s):
        if not s&primary:return 1,frozenset([()])
        active=[i for i,m in enumerate(masks) if m&s==m]
        relevant=primary
        for i in active:relevant|=masks[i]
        s &= relevant
        if s in memo:return memo[s]
        columns={j:[i for i in active if masks[i]>>j&1] for j in range(enc['primary']) if s>>j&1}
        pivot=min(columns) if first else min(columns,key=lambda j:(len(columns[j]),j))
        root=0;family=frozenset()
        for i in columns[pivot]:
            h,f=visit(s^masks[i])
            if h:
                new=len(instructions)+2;instructions[new]=(i+1,root,h);root=new
                family |= frozenset(tuple(sorted(q+(i,))) for q in f)
        memo[s]=(root,family)
        return memo[s]
    root,family=visit((1<<len(enc['names']))-1)
    return instructions,family,root


def pfaffian(a):
    a = [[Fraction(x) for x in row] for row in a]
    answer = Fraction(1)
    for k in range(0,len(a),2):
        j = next((j for j in range(k+1,len(a)) if a[k][j]),None)
        if j is None: return 0
        if j != k+1:
            a[j],a[k+1] = a[k+1],a[j]
            for row in a: row[j],row[k+1] = row[k+1],row[j]
            answer = -answer
        p = a[k][k+1]; answer *= p
        for i in range(k+2,len(a)):
            for j in range(i+1,len(a)):
                a[i][j] -= (a[k][i]*a[k+1][j]-a[k][j]*a[k+1][i])/p
                a[j][i] = -a[i][j]
    assert answer.denominator == 1
    return int(answer)


def path_pfaffian(n):
    v,e,s,t = triangle(n)
    out = {x: [] for x in v}
    for x,y in e: out[x].append(y)
    @lru_cache(None)
    def paths(x,y):
        if x == y: return 1
        return sum(paths(z,y) for z in out[x])
    a = [[paths(x,y) for y in t] for x in s]
    m = n-1; size = m + m%2
    q = [[0]*size for _ in range(size)]
    for i in range(m):
        for j in range(i+1,m):
            q[i][j] = sum(a[u][i]*a[w][j]-a[u][j]*a[w][i] for u in range(len(s)) for w in range(u+1,len(s)))
        if m%2: q[i][m] = sum(row[i] for row in a)
    for i in range(size):
        for j in range(i+1,size):q[j][i] = -q[i][j]
    return dict(n=n,single_path_matrix=a,skew_matrix=q,count=pfaffian(q))


def main():
    assert not (OUT/'cases-checked.json').exists()
    start = time.monotonic()
    cases=[]
    for n in range(2,6):
        v,e,s,t = triangle(n)
        expected = path_family(v,e,s,t,n-1)
        enc,arcs = path_xcc(v,e,s,t,n-1)
        stats,nodes,family = native(f'triangle261-{n}',enc)
        got = {tuple(sorted(arcs[i] for i in f if arcs[i] is not None)) for f in family}
        assert got == expected and len(got) == len(family)
        save(OUT/f'triangle261-{n}.json',dict(n=n,stats=stats,arc_families=sorted(got)))
        cases.append(dict(kind='triangle',n=n,stats=stats))
    # A branching acyclic network; several choices of number and endpoint pairings.
    vertices=list(range(6)); edges=[(0,2),(0,3),(1,2),(1,3),(2,3),(2,4),(2,5),(3,4),(3,5)]
    for m,prescribed,sinks in [(0,False,[4,5]),(1,False,[4,5]),(2,False,[4,5]),(2,True,[4,5]),(2,True,[5,4])]:
        expected=path_family(vertices,edges,[0,1],sinks,m,prescribed)
        enc,arcs=path_xcc(vertices,edges,[0,1],sinks,m,prescribed)
        label=f'network261-{m}-{int(prescribed)}-{sinks[0]}'
        stats,nodes,family=native(label,enc)
        got={tuple(sorted(arcs[i] for i in f if arcs[i] is not None)) for f in family}
        assert got==expected and len(got)==len(family)
        save(OUT/(label+'.json'),dict(stats=stats,arc_families=sorted(got)))
        cases.append(dict(kind=label,stats=stats))
    # The two actual printed counterexamples to uniqueness with secondary items.
    simple=[['p'],['p','r'],['p','s'],['q','r'],['q','s']]
    large=[['p']]+[['p',f'r{i}'] for i in range(1,4)]+[['p','s']]
    for x in ['q','r']:large += [[f'{x}{i}',f'{x}{j}'] for i,j in combinations(range(1,4),2)]
    large += [[f'q{i}',f'r{j}'] for i in range(1,4) for j in range(1,4)]
    large += [[f'q{i}','s'] for i in range(1,4)]
    assert len(large)==23
    for label,primary,rows,first in [('duplicates265-first',list('pqr'),simple,True),('duplicates265-mrv',['p','q1','q2','q3','r1','r2','r3'],large,False)]:
        enc=encode(primary,['s'],[[(i,0) for i in row] for row in rows])
        stats,native_nodes,family=native(label,enc)
        nodes,model_family,model_root=uncolored_model(enc,first)
        assert family==model_family
        duplicates=[(i,j) for i in nodes for j in nodes if i<j and nodes[i]==nodes[j]]
        assert duplicates
        if first:
            assert {i:v for i,v in nodes.items() if v[0]}=={2:(4,0,1),3:(1,0,2),4:(5,0,1),5:(2,3,4),6:(4,0,1),7:(3,5,6)}
            rank={i+1:(min(primary.index(x) for x in row if x in primary),-i) for i,row in enumerate(rows)}
            for k,(o,l,h) in nodes.items():
                if o:
                    for child in [l,h]:
                        if child>1:assert rank[o]<rank[nodes[child][0]]
        save(OUT/(label+'.json'),dict(stats=stats,instructions=nodes,native_instructions=native_nodes,model_root=model_root,duplicates=duplicates,solutions=sorted(family)))
        cases.append(dict(kind=label,stats=stats))
    matrices=[path_pfaffian(n) for n in [2,3,4,5,16,17]]
    for q,case in zip(matrices[:4],cases[:4]):assert q['count']==case['stats']['count']
    assert [q['count'] for q in matrices]==[2,5,16,66,10606175914819584,992340657705109416]
    save(OUT/'path-pfaffians.json',dict(cases=matrices,method='LGV and minor-summation Pfaffian; boundary sources in clockwise order, diagonal sinks in increasing order; dummy source/sink for odd count.'))
    files=[p for p in OUT.iterdir() if p.suffix in ['.xcc','.log','.zdd'] or p.name.startswith(('triangle261-','network261-','duplicates265-','path-pfaffians'))]
    result=dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),binary_sha256=sha(BIN),nice=os.getpriority(os.PRIO_PROCESS,0),elapsed_seconds=time.monotonic()-start,cases=cases,artifact_hashes={str(p.relative_to(ROOT)):sha(p) for p in files})
    save(OUT/'cases-checked.json',result)
    print(json.dumps(dict(elapsed_seconds=result['elapsed_seconds'],cases=[(c['kind'],c.get('n'),c['stats']['count']) for c in cases],pfaffian_counts=[(q['n'],q['count']) for q in matrices]),indent=2))


if __name__=='__main__':main()
