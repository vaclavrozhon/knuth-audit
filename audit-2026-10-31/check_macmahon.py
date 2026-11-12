#!/usr/bin/env python3
"""Independent triangular-lattice model and XCC generator for exercises 125–129."""
import argparse
import itertools as it
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/macmahon'
COLORS = 'abcd'

def name(t):
    x,y,z=t
    return f'{x}{y}'+("'" if z else '')

def edges(t):
    x,y,z=t
    return (('-',x,y+z), ('/',x+z,y), ('\\',x,y))

def vertices(t):
    x,y,z=t
    return ((x+1,y),(x,y+1),(x+z,y+z))

def piece(cs):
    return min(''.join(cs[i:]+cs[:i]) for i in range(3))

def opposite(t):
    x,y,z=t
    return 3-x,3-y,1-z

def complement(cs,involution='dcba'):
    return tuple(involution[COLORS.index(c)] for c in cs)

TRIANGLES = [(x,y,z) for x in range(4) for y in range(4) for z in range(2)
             if 2-z <= x+y <= 5-z]
HALF = [t for t in TRIANGLES if t[1]>=2]
PIECES = sorted({piece(c) for c in it.product(COLORS,repeat=3)})
EDGE_TRIANGLES=defaultdict(list)
for t in TRIANGLES:
    for e in edges(t): EDGE_TRIANGLES[e].append(t)

def scale(t,k,printed=False):
    x,y,z=t
    return {(k*x+p,k*(x if printed else y)+q,w)
            for p in range(k) for q in range(k) for w in (0,1)
            if (p+q < k-w) == (not z)}

def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def inside(p,vs):
    signs=[cross(vs[i],vs[(i+1)%3],p) for i in range(3)]
    return min(signs)>=0 or max(signs)<=0

def check_scaling():
    cases=0
    for x,y,z,k in it.product(range(-2,3),range(-2,3),(0,1),range(1,9)):
        t=(x,y,z); children=scale(t,k)
        vs=[(k*a,k*b) for a,b in vertices(t)]
        # Independent geometric selection: all three vertices must be inside.
        geometric={(a,b,w) for a in range(k*x-1,k*(x+1)+1)
                   for b in range(k*y-1,k*(y+1)+1) for w in (0,1)
                   if all(inside(v,vs) for v in vertices((a,b,w)))}
        assert children==geometric and len(children)==k*k
        cases+=1
    example=dict(triangle=[0,1,0],k=1,printed=sorted(scale((0,1,0),1,True)),
                 corrected=sorted(scale((0,1,0),1)))
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'scaling.json').write_text(json.dumps(dict(cases=cases,example=example),indent=2)+'\n')
    print('Scaling:',cases,'geometric cases passed;',example)

def edge_system(periodic=False):
    adj=defaultdict(list)
    # Each relation says color(f) = complement^flip(color(e)).
    for t in TRIANGLES:
        for e,f in zip(edges(t),edges(opposite(t))):
            adj[e].append((f,1)); adj[f].append((e,1))
    if periodic:
        pairs=[(('-',x,4),('-',x+2,0)) for x in (0,1)]
        pairs += [(('/',0,y),('/',4,y-2)) for y in (2,3)]
        pairs += [(('\\',x,1-x),('\\',x+2,3-x)) for x in (0,1)]
        for e,f in pairs:
            assert len(EDGE_TRIANGLES[e])==len(EDGE_TRIANGLES[f])==1
            adj[e].append((f,0));adj[f].append((e,0))
    mapping={}
    for e in sorted(EDGE_TRIANGLES):
        if e in mapping: continue
        mapping[e]=(e,0);stack=[e]
        while stack:
            v=stack.pop()
            for w,b in adj[v]:
                val=(e,mapping[v][1]^b)
                if w in mapping: assert mapping[w]==val
                else: mapping[w]=val;stack.append(w)
    return mapping

# (aaa location, permitted bbb locations, optional edge restricted to {a,c})
TYPES={
 1: ((0,2,0),[(0,3,0)],('/',1,2)),
 2: ((0,2,0),[(2,3,0)],None),
 3: ((0,2,0),[(1,3,1)],('\\',0,3)),
 4: ((0,2,0),[(1,2,0),(1,2,1),(2,2,0),(2,2,1),(1,3,0)],None),
 5: ((1,3,0),[(0,2,1)],('\\',1,2)),
 6: ((1,3,0),[(1,2,0)],None),
}

def strong_options(kind=0,periodic=False,involution='dcba'):
    mapping=edge_system(periodic)
    sec=sorted(set(v[0] for v in mapping.values()))
    secname={e:f'E{i}' for i,e in enumerate(sec)}
    header=PIECES+[name(t) for t in HALF]+['|']+list(secname.values())
    rows=[];metadata=[]
    for t in HALF:
        for cs in it.product(COLORS,repeat=3):
            tile=piece(cs); tile2=piece(complement(cs,involution))
            if kind:
                a,bs,edge=TYPES[kind]
                placements={t:tile,opposite(t):tile2}
                if any((pos==a)!=(p=='aaa') for pos,p in placements.items()): continue
                if any(p=='bbb' and pos not in bs for pos,p in placements.items()): continue
                if any(pos in bs and len(bs)==1 and p!='bbb' for pos,p in placements.items()): continue
            assignments={}
            good=True
            for e,c in zip(edges(t),cs):
                base,flip=mapping[e]
                c=complement((c,),involution)[0] if flip else c
                if base in assignments and assignments[base]!=c: good=False;break
                assignments[base]=c
            if not good: continue
            if kind and edge is not None:
                base,flip=mapping[edge]
                if base in assignments:
                    c=assignments[base]
                    if flip:c=complement((c,),involution)[0]
                    if c not in 'ac':continue
            row=[tile,tile2,name(t)]+[secname[e]+':'+c for e,c in assignments.items()]
            assert len(row)==len(set(r.split(':')[0] for r in row))
            rows.append(row);metadata.append(dict(triangle=t,colors=cs))
    return header,rows,metadata

def write_inputs():
    OUT.mkdir(parents=True,exist_ok=True)
    assert len(TRIANGLES)==24 and len(HALF)==12 and len(PIECES)==24
    assert len(EDGE_TRIANGLES)==42
    assert Counter(map(len,EDGE_TRIANGLES.values()))=={1:12,2:30}
    for periodic in (False,True):
        for kind in range(7):
            h,rs,meta=strong_options(kind,periodic)
            f=OUT/f'strong-{kind}{"-periodic" if periodic else ""}'
            f.with_suffix('.xcc').write_text(' '.join(h)+'\n'+'\n'.join(' '.join(r) for r in rs)+'\n')
            f.with_suffix('.options.json').write_text(json.dumps(meta)+'\n')
            print(f.name,len(rs),'options',len(h)-1,'items')
    assert len(strong_options()[1])==768

def weak_options(kind):
    """Full 24-triangle XCC; only the within-triangle equality pattern is paired."""
    all_edges=sorted(EDGE_TRIANGLES)
    secname={e:f'E{i}' for i,e in enumerate(all_edges)}
    patchname={t:f'B{i}' for i,t in enumerate(HALF)}
    patchname.update({opposite(t):v for t,v in list(patchname.items())})
    header=PIECES+[name(t) for t in TRIANGLES]+['|']+list(secname.values())+sorted(set(patchname.values()))
    a,bs,edge=TYPES[kind]
    allowed={'aaa':[a],'ddd':[opposite(a)],'bbb':bs,'ccc':[opposite(b) for b in bs]}
    rows=[]
    for t in TRIANGLES:
        for cs in it.product(COLORS,repeat=3):
            tile=piece(cs)
            if tile in allowed and t not in allowed[tile]:continue
            if any(len(loc)==1 and t in loc and tile!=p for p,loc in allowed.items()):continue
            assignments=dict(zip(edges(t),cs))
            if edge is not None and edge in assignments and assignments[edge] not in 'ac':continue
            # Equality of all three pairwise color comparisons is exactly equality
            # of color-patch boundaries inside a triangle.
            mask=sum((cs[i]!=cs[(i+1)%3])<<i for i in range(3))
            rows.append([tile,name(t)]+[secname[e]+':'+c for e,c in assignments.items()]+[patchname[t]+':'+str(mask)])
    return header,rows

def write_weak_inputs():
    for kind in range(1,7):
        h,rs=weak_options(kind)
        f=OUT/f'weak-{kind}.xcc'
        f.write_text(' '.join(h)+'\n'+'\n'.join(' '.join(r) for r in rs)+'\n')
        print(f.name,len(rs),'options')

def reflect(t,axis):
    x,y,z=t
    if axis=='tb':return x+y-2+z,3-y,1-z
    if axis=='lr':return 5-x-y-z,y,z
    raise ValueError(axis)

def patchmask(cs):
    return sum((cs[i]!=cs[(i+1)%3])<<i for i in range(3))

TB_TYPES={
 1: ((0,2,1),[(2,2,1)],('-',1,3)),
 2: ((0,2,1),[(1,2,1),(0,3,1),(1,3,0),(1,3,1),(2,3,0)],None),
 3: ((1,2,1),[(0,3,0),(0,3,1)],None),
 4: ((0,3,0),[(2,3,0)],('-',1,3)),
 5: ((0,3,0),[(1,3,0),(1,3,1)],None),
 6: ((0,3,1),[(1,3,1)],('-',1,3)),
}

def reflection_options(axis,allowed,edge=None,strong=False,involution='dcba'):
    rt={t:reflect(t,axis) for t in TRIANGLES}
    assert set(rt.values())==set(TRIANGLES)
    assert all(rt[rt[t]]==t for t in TRIANGLES)
    representatives=sorted({min(t,rt[t]) for t in TRIANGLES})
    pn={t:f'B{i}' for i,t in enumerate(representatives)}
    def patch(t,cs):
        if t==rt[t] and patchmask(cs)!=patchmask((cs[0],cs[2],cs[1])):return None
        c=patchmask(cs if t<=rt[t] else (cs[0],cs[2],cs[1]))
        return pn[min(t,rt[t])],str(c)
    def valid(t,cs):
        tile=piece(cs)
        if tile in allowed and t not in allowed[tile]:return False
        if any(len(loc)==1 and t in loc and tile!=p for p,loc in allowed.items()):return False
        d=dict(zip(edges(t),cs))
        return not(edge is not None and edge in d and d[edge] not in 'ac')
    if strong:
        header,source,meta=strong_options(involution=involution)
        header+=list(pn.values());rows=[]
        for row,m in zip(source,meta):
            t=m['triangle'];cs=m['colors'];u=opposite(t);ds=complement(cs,involution)
            if not valid(t,cs) or not valid(u,ds):continue
            a,b=patch(t,cs),patch(u,ds)
            if a is None or b is None or (a[0]==b[0] and a[1]!=b[1]):continue
            rows.append(row+[n+':'+c for n,c in sorted({a,b})])
    else:
        es={e:f'E{i}' for i,e in enumerate(sorted(EDGE_TRIANGLES))}
        header=PIECES+[name(t) for t in TRIANGLES]+['|']+list(es.values())+list(pn.values())
        rows=[]
        for t in TRIANGLES:
            for cs in it.product(COLORS,repeat=3):
                if not valid(t,cs):continue
                b=patch(t,cs)
                if b is None:continue
                rows.append([piece(cs),name(t)]+[es[e]+':'+c for e,c in zip(edges(t),cs)]+[b[0]+':'+b[1]])
    return header,rows

def write_reflection_inputs():
    for kind,(a,bs,edge) in TB_TYPES.items():
        allowed={'aaa':[a],'ddd':[reflect(a,'tb')],'bbb':bs,'ccc':[reflect(b,'tb') for b in bs]}
        for mode in ('weak','dcba','badc','cdab'):
            strong=mode!='weak'
            h,rs=reflection_options('tb',allowed,edge,strong,mode if strong else 'dcba')
            f=OUT/f'tb-{kind}{"-strong-"+mode if strong else ""}.xcc'
            f.write_text(' '.join(h)+'\n'+'\n'.join(' '.join(r) for r in rs)+'\n')
            print(f.name,len(rs),'options')

def mono_sets(axis):
    out=[]
    for mono in it.combinations(TRIANGLES,4):
        if {reflect(t,axis) for t in mono}!=set(mono):continue
        # Different monochrome pieces cannot meet along an edge.
        es=[e for t in mono for e in edges(t)]
        if len(es)!=len(set(es)):continue
        out.append(mono)
    return out

def write_lr_inputs():
    sets=mono_sets('lr');(OUT/'lr').mkdir(exist_ok=True)
    metadata=[]
    for i,mono in enumerate(sets):
        allowed={c*3:[t] for c,t in zip(COLORS,mono)}
        h,rs=reflection_options('lr',allowed)
        f=OUT/'lr'/f'{i:03d}.xcc'
        f.write_text(' '.join(h)+'\n'+'\n'.join(' '.join(r) for r in rs)+'\n')
        metadata.append(dict(index=i,mono=mono,fixed=sum(reflect(t,'lr')==t for t in mono),options=len(rs)))
        if {reflect(t,'tb') for t in mono}==set(mono):
            reps=sorted({min(t,reflect(t,'tb')) for t in TRIANGLES})
            pn={t:f'C{j}' for j,t in enumerate(reps)}
            h2=h+list(pn.values());r2=[];tn={name(t):t for t in TRIANGLES}
            for row in rs:
                t=tn[row[1]];cs=tuple(v.split(':')[1] for v in row[2:5])
                rt=reflect(t,'tb')
                if t>rt:cs=(cs[0],cs[2],cs[1])
                r2.append(row+[pn[min(t,rt)]+':'+str(patchmask(cs))])
            (OUT/'lr'/f'{i:03d}-both.xcc').write_text(' '.join(h2)+'\n'+'\n'.join(' '.join(r) for r in r2)+'\n')
            metadata[-1]['both']=True
    (OUT/'lr/metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print('LR mono sets:',len(sets),dict(Counter(d['fixed'] for d in metadata)))

if __name__=='__main__':
    check_scaling()
    write_inputs()
    write_weak_inputs()
    write_reflection_inputs()
    write_lr_inputs()
