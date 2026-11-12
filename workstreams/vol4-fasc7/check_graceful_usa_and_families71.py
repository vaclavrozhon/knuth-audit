#!/usr/bin/env python3
"""Exact, search-free checks of Fig.106 and the small complete graphs."""
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import combinations
import hashlib
import json
from pathlib import Path
import re
from xml.etree import ElementTree as ET

ROOT=Path(__file__).resolve().parent
ROWS=[
 [(4,'ND',58),(10,'VT',33),(11,'NH',83),(12,'ME',27)],
 [(1,'WA',59),(3,'MT',53),(4,'SD',6),(5,'MN',97),(6,'WI',93),(7,'MI',23),(10,'NY',64),(11,'MA',9)],
 [(1,'OR',41),(2,'ID',26),(3,'WY',106),(4,'NE',107),(5,'IA',48),(6,'IL',11),(7,'IN',55),(8,'OH',84),(9,'PA',62),(10,'NJ',90),(11,'CT',16),(12,'RI',78)],
 [(0,'CA',31),(1,'NV',98),(2,'UT',86),(3,'CO',0),(4,'KS',104),(5,'MO',2),(7,'KY',95),(8,'WV',19),(9,'MD',92),(10,'DE',24)],
 [(2,'AZ',15),(3,'NM',103),(4,'OK',25),(5,'AR',66),(7,'TN',101),(8,'VA',5),(9,'DC',56)],
 [(4,'TX',8),(5,'LA',100),(6,'MS',3),(7,'AL',88),(8,'GA',7),(9,'NC',82)],
 [(8,'FL',96),(9,'SC',28)],
]


def check_planarity(points,edges):
    def cross(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    checks=0
    for e,f in combinations(edges,2):
        shared=set(e)&set(f)
        if shared:
            u=next(iter(shared));v=next(v for v in e if v!=u);w=next(w for w in f if w!=u)
            a,b,c=points[u],points[v],points[w]
            if cross(a,b,c)==0:
                assert sum((b[k]-a[k])*(c[k]-a[k]) for k in (0,1))<0
        else:
            a,b,c,d=(points[u] for u in (*e,*f))
            box=all(max(min(a[k],b[k]),min(c[k],d[k]))<=min(max(a[k],b[k]),max(c[k],d[k])) for k in (0,1))
            intersect=box and cross(a,b,c)*cross(a,b,d)<=0 and cross(c,d,a)*cross(c,d,b)<=0
            assert not intersect
        checks+=1
    assert checks==5671
    return {'segment_pairs':checks,'no_improper_crossing_or_overlap':True}


def main():
    points={state:(x,y) for y,row in enumerate(ROWS) for x,state,value in row}
    labels={state:value for row in ROWS for x,state,value in row}
    reverse={p:s for s,p in points.items()}
    assert len(points)==len(set(labels.values()))==49
    assert all(0<=x<=107 for x in labels.values())
    elements=list(ET.parse(ROOT/'sources/file-033.svg').iter())
    paths=[x for x in elements if x.tag.endswith('path') and x.get('stroke-width')=='0.48' and 'C' not in x.get('d','')]
    ovals=[x for x in elements if x.tag.endswith('path') and x.get('stroke-width')=='0.48' and 'C' in x.get('d','')]
    assert len(paths)==106 and len(ovals)==49
    ox,oy,step=F('163.059'),F('278.105'),F('19.9954')
    edges=[];residuals=[]
    for ordinal,path in enumerate(paths):
        a,b,c,d,e,f=map(F,re.findall(r'-?\d+(?:\.\d+)?',path.get('transform')))
        words=path.get('d').split();vs=[]
        while words:
            command,x,y,*words=words;assert command in ('M','L')
            x,y=F(x),F(y);x,y=a*x+c*y+e,b*x+d*y+f
            gx,gy=round((x-ox)/step),round((y-oy)/step)
            residual=(x-ox-gx*step)**2+(y-oy-gy*step)**2
            assert residual<F(1,10000)
            residuals.append(str(residual));vs.append(reverse[gx,gy])
        edges.extend(tuple(sorted(e)) for e in zip(vs,vs[1:]))
    assert len(edges)==len(set(edges))==107
    official=ROOT/'sources/contiguous-usa-2026-11-07.dat'
    published={tuple(sorted(line.split())) for line in official.read_text().splitlines() if line.strip()}
    assert set(edges)==published
    # Every equality in the printed107-entry table, not just its totals.
    printed=[tuple(map(int,m)) for m in re.findall(r'(\d+)\s*[−-]\s*(\d+)\s*=\s*(\d+)',(ROOT/'sources/file-033.txt').read_text())]
    assert len(printed)==107 and sorted(z for x,y,z in printed)==list(range(1,108))
    assert all(x-y==d for x,y,d in printed)
    by_value={value:state for state,value in labels.items()}
    assert {tuple(sorted([by_value[x],by_value[y]])) for x,y,d in printed}==published
    exact=[{'edge':list(e),'labels':[labels[s] for s in e],
            'difference':abs(labels[e[0]]-labels[e[1]])} for e in sorted(published)]
    assert sorted(r['difference'] for r in exact)==list(range(1,108))
    from check_graceful_colonies67_70 import VERTICES,EDGES
    induced={e for e in published if all(s in VERTICES for s in e)}
    assert induced=={tuple(sorted(e)) for e in EDGES}
    # Exact cyclic order at vertices, followed by every directed face boundary.
    def cmp(a,b):
        ha=int(a[1]<0 or a[1]==0 and a[0]<0);hb=int(b[1]<0 or b[1]==0 and b[0]<0)
        if ha!=hb:return ha-hb
        cross=a[0]*b[1]-a[1]*b[0]
        return (cross<0)-(cross>0)
    def vector(u,v):return tuple(points[v][k]-points[u][k] for k in range(2))
    adj={s:[] for s in points}
    for u,v in published:adj[u].append(v);adj[v].append(u)
    for u in adj:adj[u].sort(key=cmp_to_key(lambda v,w:cmp(vector(u,v),vector(u,w))))
    seen=set();faces=[]
    for start in [(u,v) for u in adj for v in adj[u]]:
        if start in seen:continue
        edge=start;walk=[]
        while edge not in seen:
            seen.add(edge);u,v=edge;walk.append(u)
            edge=(v,adj[v][(adj[v].index(u)-1)%len(adj[v])])
        assert edge==start
        area=sum(points[u][0]*points[v][1]-points[u][1]*points[v][0] for u,v in zip(walk,walk[1:]+walk[:1]))
        faces.append({'walk':walk,'area_twice':area})
    assert len(faces)==60 and 49-107+len(faces)==2
    outer=max(faces,key=lambda f:abs(f['area_twice']))
    border='CA OR WA ID MT ND MN WI MI OH PA NY VT NH ME'.split()
    cyclic=outer['walk']+outer['walk']
    assert any(cyclic[k:k+15]==border or cyclic[k:k+15]==list(reversed(border)) for k in range(len(outer['walk'])))
    digits=''.join(f'{labels[s]:02}' for s in border)
    assert digits=='314159265358979323846264338327' and len(digits)==30
    # Alternating rational bounds, with a complete Machin identity proof in note.
    def atan_bounds(q,n):
        total=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),F(0))
        other=total+F((-1)**n,(2*n+1)*q**(2*n+1))
        return min(total,other),max(total,other)
    a,b=atan_bounds(5,25),atan_bounds(239,8)
    pi_low,pi_high=16*a[0]-4*b[1],16*a[1]-4*b[0]
    assert int(pi_low*10**29)==int(pi_high*10**29)==int(digits)
    complete=[]
    for n,S in [(1,[0]),(2,[0,1]),(3,[0,2,3]),(4,[0,2,5,6])]:
        m=n*(n-1)//2;diffs=sorted(abs(x-y) for x,y in combinations(S,2))
        assert diffs==list(range(1,m+1))
        complete.append({'n':n,'m':m,'labels':S,'differences':diffs})
    out={'source':'Original Fig.106/file33; original4A p15/file32 displayed for all49 state positions.',
         'official_data_url':'https://www-cs-faculty.stanford.edu/~knuth/contiguous-usa.dat',
         'official_data_sha256':hashlib.sha256(official.read_bytes()).hexdigest(),
         'positions':points,'labels':labels,'native_straight_paths':106,'native_ovals':49,
         'planarity':check_planarity(points,sorted(published)),
         'native_residuals_squared':residuals,'all107_edges':exact,'all107_printed_equalities':printed,
         'colonies_induced_edges':sorted(induced),'all_faces':faces,'outer_face':outer,
         'border_states':border,'pi_digits':digits,'pi_interval':[str(pi_low),str(pi_high)],
         'complete_graph_small_witnesses':complete,
         'scope':'No graceful search, no randomized restart, no census. The full general proofs and every71 exclusion are in the note.'}
    (ROOT/'results/graceful-usa-and-families71.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'vertices':49,'edges':107,'printed_equalities':len(printed),'induced_colonies_edges':len(induced),'faces':len(faces),'pi_prefix_digits':30,'complete_graph_witnesses':len(complete)}))


if __name__=='__main__':main()
