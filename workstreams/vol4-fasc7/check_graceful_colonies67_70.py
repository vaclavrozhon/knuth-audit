#!/usr/bin/env python3
"""Finite certificates for Fig.105, (33)--(35), and exercises67--70.

No full graceful-labeling census. Searches have explicit small node/time
bounds and are either a fixed puzzle, a fixed rare longest edge, or just
one witness. General arguments are in the accompanying note.
"""
from fractions import Fraction as F
from itertools import permutations
import json
from pathlib import Path
import re
import time
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent
VERTICES = 'NH NY MA PA NJ CT RI MD DE VA NC GA SC'.split()
LABELS = dict(zip(VERTICES, [8, 0, 17, 18, 12, 15, 1, 10, 5, 6, 3, 13, 14]))
GRID = dict(zip(VERTICES, [(2,0),(1,1),(2,1),(0,2),(1,2),(2,2),
                         (3,2),(0,3),(1,3),(0,4),(1,4),(1,5),(2,5)]))
EDGES = [tuple(s.split('-')) for s in (
    'NH-MA NY-MA NY-PA NY-NJ NY-CT MA-CT MA-RI CT-RI PA-NJ '
    'PA-MD PA-DE NJ-DE MD-DE MD-VA VA-NC NC-GA NC-SC GA-SC').split()]


def labeling_certificate(labels):
    assert set(labels) == set(VERTICES)
    assert len(set(labels.values())) == 13
    assert all(0 <= x <= 18 for x in labels.values())
    out = [{'edge': list(e), 'values': [labels[u] for u in e],
            'difference': abs(labels[e[0]]-labels[e[1]])} for e in EDGES]
    assert sorted(r['difference'] for r in out) == list(range(1,19))
    return out


def native_graphs():
    paths = [x for x in ET.parse(ROOT/'sources/file-032.svg').iter()
             if x.tag.endswith('path') and x.get('stroke-width') == '0.48'
             and 'C' not in x.get('d','')]
    assert len(paths) == 48
    by_grid = {tuple(p):v for v,p in GRID.items()}
    out = []
    for panel in range(4):
        ox = F(['100.474','192.334','284.254','376.114'][panel])
        oy, sx, sy = F('67.87'), F('19.984'), F('12.99')
        edges, residuals = [], []
        for ordinal, path in enumerate(paths[12*panel:12*(panel+1)]):
            a,b,c,d,e,f = map(F,re.findall(r'-?\d+(?:\.\d+)?', path.get('transform')))
            words = path.get('d').split(); points = []
            while words:
                command,x,y,*words = words
                assert command in ('M','L')
                x,y = F(x),F(y); x,y = a*x+c*y+e,b*x+d*y+f
                gx,gy = round((x-ox)/sx),round((y-oy)/sy)
                residual = (x-ox-gx*sx)**2+(y-oy-gy*sy)**2
                assert residual < F(1,10000)
                residuals.append(str(residual)); points.append(by_grid[gx,gy])
            edges.extend(tuple(sorted(e)) for e in zip(points,points[1:]))
        assert len(edges) == 18 and len(set(edges)) == 18
        assert set(edges) == {tuple(sorted(e)) for e in EDGES}
        out.append({'panel':'abcd'[panel], 'straight_paths':12,
                    'edge_list':edges,'squared_residuals':residuals})
    return out


def array_certificate():
    lo = [None,13,15,3,6,5,12,5,10,8,3,3,0,5,1,0,1,0,0]
    first = [12,15,-1,6,-1,10,3,-1,17,-1,6,-1,18,14,13,17,-1,15,12]
    nl = [None,3,8,10,5,18,10,0,5,1,-1,-1,-1,0,0,-1,0,-1,-1]
    nh = [None,3,1,13,-1,12,5,18,-1,-1,14,-1,15,-1,17,17,-1,18,-1]
    name = ['NY','RI',None,'NC',None,'DE','VA',None,'NH',None,'MD',None,
            'NJ','GA','SC','CT',None,'MA','PA']
    def check(lab,lo,first,nl,nh,name):
        edges = {tuple(sorted([lab[u],lab[v]])) for u,v in EDGES}
        for d in range(1,19): assert (lo[d],lo[d]+d) in edges
        for v,w in permutations(range(19),2):
            if v<w: assert ((v,w) in edges) == (lo[w-v] == v)
        traversals = []
        for v in range(19):
            seen=[];w=first[v]
            while w >= 0:
                assert 0 <= w <= 18 and w != v and w not in seen
                seen.append(w);w=nl[v-w] if w<v else nh[w-v]
                assert len(seen) <= 18
            assert w == -1
            assert set(seen) == {b if a==v else a for a,b in edges if v in (a,b)}
            assert name[v] == next((u for u in VERTICES if lab[u]==v),None)
            traversals.append(seen)
        return traversals
    original = check(LABELS,lo,first,nl,nh,name)
    flip = lambda x: -1 if x==-1 else 18-x
    lop = [None]+[18-d-lo[d] for d in range(1,19)]
    firstp = [flip(first[18-v]) for v in range(19)]
    nlp = [None]+[flip(x) for x in nh[1:]]
    nhp = [None]+[flip(x) for x in nl[1:]]
    namep = list(reversed(name))
    complemented = check({u:18-x for u,x in LABELS.items()},lop,firstp,nlp,nhp,namep)
    assert all(complemented[18-v] == [18-w for w in original[v]] for v in range(19))
    return {'original':dict(LO=lo,FIRST=first,NEXTL=nl,NEXTH=nh,NAME=name,walks=original),
            'complemented':dict(LO=lop,FIRST=firstp,NEXTL=nlp,NEXTH=nhp,NAME=namep,walks=complemented),
            'ordered_adjacency_pairs_checked':19*18,'unused_LO_and_NEXT_indices':[0]}


class XCC:
    def __init__(self):
        self.rows=[];self.columns=[0]*36
        self.incident={u:0 for u in VERTICES}
        self.colored={(u,x):0 for u in VERTICES for x in range(19)}
        self.holders=[0]*19
        for e,(u,v) in enumerate(EDGES):
            for x in range(19):
                for y in range(19):
                    if x==y:continue
                    d=abs(x-y);r=len(self.rows);bit=1<<r
                    self.rows.append((e,d,u,x,v,y))
                    self.columns[e]|=bit;self.columns[18+d-1]|=bit
                    for a,z in ((u,x),(v,y)):
                        self.incident[a]|=bit;self.colored[a,z]|=bit;self.holders[z]|=bit
        assert len(self.rows)==6156
        self.conflicts=[]
        for e,d,u,x,v,y in self.rows:
            bad=self.columns[e]|self.columns[18+d-1]
            for a,z in ((u,x),(v,y)):
                bad|=self.incident[a]^self.colored[a,z]
                bad|=self.holders[z]^self.colored[a,z]
            self.conflicts.append(bad)
        self.all=(1<<len(self.rows))-1
        self.total_nodes=0;self.deadline=time.monotonic()+20

    def search(self,fixed,*,canonical=False,first_only=False,limit=5000,keep_tree=False):
        active=self.all
        assert len(set(fixed.values()))==len(fixed)
        for u,x in fixed.items():
            active &= ~(self.incident[u]^self.colored[u,x])
            active &= ~(self.holders[x]^self.colored[u,x])
        if canonical:
            for r,(e,d,u,x,v,y) in enumerate(self.rows):
                if (u,v) in [('NY','MA'),('GA','SC')] and x>y: active &= ~(1<<r)
        solutions=[];nodes=0;tree=[];aborted=None
        def dfs(mask,uncovered,chosen):
            nonlocal nodes,aborted
            nodes+=1;self.total_nodes+=1
            if nodes>limit or self.total_nodes>12000 or time.monotonic()>self.deadline:
                aborted='explicit small-search budget';return False
            index=len(tree);entry={}
            if keep_tree:tree.append(entry)
            if not uncovered:
                labels=dict(fixed)
                for r in chosen:
                    _,_,u,x,v,y=self.rows[r];labels[u]=x;labels[v]=y
                labeling_certificate(labels);solutions.append(labels)
                if keep_tree:entry['solution']=len(solutions)-1
                return first_only
            best=None;pending=uncovered
            while pending:
                bit=pending&-pending;c=bit.bit_length()-1;pending^=bit
                possible=mask&self.columns[c];n=possible.bit_count()
                if best is None or n<best[0]:best=(n,c,possible)
                if n==0:break
            _,c,possible=best
            if keep_tree:entry.update(column=c,children=[])
            while possible:
                bit=possible&-possible;r=bit.bit_length()-1;possible^=bit
                e,d,*_=self.rows[r]
                child=len(tree)
                if keep_tree:entry['children'].append([r,child])
                stop=dfs(mask&~self.conflicts[r],uncovered&~((1<<e)|(1<<(18+d-1))),chosen+[r])
                if stop or aborted:return stop
            return False
        dfs(active,(1<<36)-1,[])
        return {'fixed':fixed,'canonical':canonical,'nodes':nodes,'complete':aborted is None and not first_only,
                'first_witness_only':first_only,'aborted':aborted,'solutions':solutions,
                **({'tree':tree} if keep_tree else {})}


def main():
    graphs=native_graphs()
    base=labeling_certificate(LABELS)
    complement=labeling_certificate({u:18-x for u,x in LABELS.items()})
    unused=set(range(19))-{x for u,x in LABELS.items() if u not in ('GA','SC')}
    pairs=[]
    for x,y in permutations(sorted(unused),2):
        if sorted([abs(x-3),abs(y-3),abs(x-y)])==[1,10,11]:
            labeling_certificate({**LABELS,'GA':x,'SC':y});pairs.append([x,y])
    assert pairs==[[2,13],[4,14],[13,2],[13,14],[14,4],[14,13]]
    changes=[{'VA':7},{'NJ':6,'VA':13,'GA':7},{'NH':6,'VA':7,'SC':4}]
    extra=[{'changes':c,'edge_checks':labeling_certificate({**LABELS,**c})} for c in changes]
    for x,y in pairs:labeling_certificate({**LABELS,'VA':7,'GA':x,'SC':y})
    xcc=XCC()
    assert sum(1 for e,d,u,x,v,y in xcc.rows if (u,v) not in [('NY','MA'),('GA','SC')] or x<y)==5814
    assert next(r for r in xcc.rows if r[2:] == ('PA',3,'DE',9))[:2] == (10,6)
    puzzle=xcc.search({'GA':0,'SC':18,'NJ':5},keep_tree=True)
    assert puzzle['complete'] and len(puzzle['solutions'])==1
    # This single rare-edge branch is a small census, not the full641952 run.
    rare=xcc.search({'GA':0,'SC':18},canonical=True,keep_tree=True)
    if rare['complete']:assert len(rare['solutions'])==24
    witnesses=[]
    for u,v in EDGES:
        if (u,v)==('GA','SC') and rare['solutions']:
            w={'edge':[u,v],'source':'rare-edge saved solution','labels':rare['solutions'][0]}
        else:
            r=xcc.search({u:0,v:18},first_only=True,limit=1000)
            w={'edge':[u,v],'nodes':r['nodes'],'aborted':r['aborted'],
               'labels':r['solutions'][0] if r['solutions'] else None}
        if w['labels'] is not None:labeling_certificate(w['labels'])
        witnesses.append(w)
    out={'native_graphs':graphs,'base_labels':LABELS,'base_edges':base,
         'complement_edges':complement,'exercise67_pairs':pairs,'exercise67_other_changes':extra,
         'arrays':array_certificate(),'XCC':{'options':6156,'canonical_options':5814,
         'primary_items':36,'colored_secondary_items':32},'puzzle':puzzle,'rare_edge':rare,
         'longest_edge_witnesses':witnesses,'total_search_nodes':xcc.total_nodes,
         'scope':'No full641952 census; no historical90/33gigamem or192/62/23-node reproduction.'}
    (ROOT/'results/graceful-colonies67-70.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'native_panels':len(graphs),'exercise67_pairs':len(pairs),
                      'puzzle_nodes':puzzle['nodes'],'puzzle_solutions':len(puzzle['solutions']),
                      'rare_nodes':rare['nodes'],'rare_complete':rare['complete'],
                      'rare_solutions':len(rare['solutions']),
                      'longest_edge_witnesses':sum(w['labels'] is not None for w in witnesses),
                      'total_search_nodes':xcc.total_nodes}))


if __name__=='__main__':main()
