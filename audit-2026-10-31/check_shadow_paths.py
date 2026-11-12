#!/usr/bin/env python3
"""Independent projected-cycle checks and orbit verification for exercises 522–524."""
import itertools as it
import json
import re
from collections import Counter
from functools import lru_cache
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/shadow_paths'
VERT=list(it.product(range(3),repeat=3))
ADJ={v:[w for w in VERT if sum(abs(a-b) for a,b in zip(v,w))==1] for v in VERT}
PLANES=list(it.combinations(range(3),2))

def cycle_normal(seq):
    s=tuple(seq);r=s[::-1]
    return min([s[i:]+s[:i] for i in range(len(s))]+[r[i:]+r[:i] for i in range(len(r))])

def canonical(path,cycle=False):
    images=[]
    for perm in it.permutations(range(3)):
        for flip in it.product((0,1),repeat=3):
            q=tuple(tuple(2-v[p] if f else v[p] for p,f in zip(perm,flip)) for v in path)
            images.append(cycle_normal(q) if cycle else min(q,q[::-1]))
    return min(images)

@lru_cache(None)
def acyclic(edges):
    # Leaf removal is independent of the C++ disjoint-set forest test.
    adj={}
    for a,b in edges:adj.setdefault(a,set()).add(b);adj.setdefault(b,set()).add(a)
    leaves=[v for v,n in adj.items() if len(n)<=1]
    while leaves:
        v=leaves.pop()
        if v not in adj:continue
        ns=adj.pop(v)
        for w in ns:
            adj[w].remove(v)
            if len(adj[w])<=1:leaves.append(w)
    return not adj

def shadows(path,cycle=False):
    result=[]
    steps=list(zip(path,path[1:]))+([(path[-1],path[0])] if cycle else [])
    for i,j in PLANES:
        edges=set()
        for a,b in steps:
            u=(a[i],a[j]);v=(b[i],b[j])
            if u!=v:edges.add(tuple(sorted((u,v))))
        result.append(frozenset(edges))
    return result

def valid(path,cycle=False):
    assert len(set(path))==len(path) and all(v in ADJ for v in path)
    assert all(b in ADJ[a] for a,b in zip(path,path[1:]))
    if cycle:assert path[0] in ADJ[path[-1]]
    assert all(acyclic(s) for s in shadows(path,cycle))

def plane_cycles():
    vs=list(it.product(range(3),repeat=2))
    adj={v:[w for w in vs if sum(abs(a-b) for a,b in zip(v,w))==1] for v in vs}
    cycles=set()
    for start in vs:
        def walk(path):
            for v in adj[path[-1]]:
                if v==start and len(path)>=4:cycles.add(cycle_normal(path))
                elif v>start and v not in path:walk(path+[v])
        walk([start])
    assert len(cycles)==13
    return cycles

def literal_sequences():
    text=(ROOT.parent/'text/vol4b.txt').read_text().split('\f')[654+19]
    tokens=re.findall(r'(?:[123]\u0304?\s*){20,}',text)
    assert len(tokens)==6,len(tokens)
    result=[]
    for n,token in enumerate(tokens):
        deltas=[(-1 if bar else 1)*int(d) for d,bar in re.findall(r'([123])(\u0304?)',token)]
        p=(0,0,0);path=[p]
        for d in deltas:
            q=list(p);q[abs(d)-1]+=1 if d>0 else -1;p=tuple(q);path.append(p)
        cycle=n<2
        if cycle:assert path[-1]==path[0];path.pop()
        valid(path,cycle)
        assert len(path)==(24 if cycle else 27)
        result.append(dict(deltas=deltas,path=path,canonical=canonical(path,cycle),end=tuple(x+1 for x in path[-1])))
    return result

def independent_enumeration(start,first=None,last=None,hamiltonian=False,domain=None):
    """No C++ viability pruning; each new shadow is checked by leaf removal."""
    domain=set(VERT if domain is None else domain)
    result=[];nodes=0
    path=[start] if first is None else [start,first]
    seen=set(path)
    initial=shadows(path)
    def walk(s):
        nonlocal nodes
        nodes+=1
        if hamiltonian and len(path)==27:result.append(tuple(path));return
        for v in ADJ[path[-1]]:
            if v not in domain:continue
            if v in seen and (hamiltonian or v!=start):continue
            if not hamiltonian and path[-1]==last and v!=start:continue
            if v==start and (len(path)<4 or (last is not None and path[-1]!=last)):continue
            new=[];a=path[-1]
            for old,(i,j) in zip(s,PLANES):
                u=(a[i],a[j]);w=(v[i],v[j])
                new.append(old if u==w else old|{tuple(sorted((u,w)))})
            if not all(acyclic(x) for x in new):continue
            if v==start:result.append(tuple(path));continue
            seen.add(v);path.append(v);walk(new);path.pop();seen.remove(v)
    walk(initial)
    return result,nodes

def main():
    pc=plane_cycles();literal=literal_sequences();data={}
    for label in ['corner-cycles','hamiltonian-corner','hamiltonian-face']:
        d=json.loads((OUT/f'{label}.json').read_text());assert d['complete']
        cyc=label=='corner-cycles';paths=[tuple(VERT[i] for i in p) for p in d['solutions']]
        for p in paths:valid(p,cyc)
        data[label]=set(canonical(p,cyc) for p in paths)
    assert len(data['corner-cycles'])==2
    assert len(data['hamiltonian-corner']|data['hamiltonian-face'])==4
    assert {tuple(map(tuple,d['canonical'])) for d in literal[:2]}==data['corner-cycles']
    assert {tuple(map(tuple,d['canonical'])) for d in literal[2:]}==data['hamiltonian-corner']|data['hamiltonian-face']
    independent={}
    jobs=[('cycles',(0,0,0),(0,0,1),(0,1,0),False),('ham-corner',(0,0,0),(0,0,1),None,True),
          ('ham-face-boundary',(0,1,1),(0,0,1),None,True),('ham-face-center',(0,1,1),(1,1,1),None,True)]
    for label,start,first,last,ham in jobs:
        paths,nodes=independent_enumeration(start,first,last,ham)
        c={canonical(p,not ham) for p in paths}
        assert c <= (data['hamiltonian-corner']|data['hamiltonian-face'] if ham else data['corner-cycles'])
        independent[label]=dict(paths=len(paths),nodes=nodes,orbits=len(c));print(label,independent[label],flush=True)
    domain={v for v in VERT if 1 in v};count=nodes=0
    for s in sorted(domain):
        paths,n=independent_enumeration(s,domain={v for v in domain if v>=s});count+=len(paths);nodes+=n
    assert count==0
    independent['cornerless']=dict(paths=count,nodes=nodes)
    result=dict(plane_cycles=[c for c in sorted(pc)],cycle_orbits=2,hamiltonian_orbits=4,literal_sequences=literal,independent=independent)
    (OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print('All six printed delta sequences and all orbit counts verified',flush=True)

if __name__=='__main__':main()
