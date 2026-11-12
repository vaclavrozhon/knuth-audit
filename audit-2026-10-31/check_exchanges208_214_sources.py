"""Source geometry and short exchange witnesses; never run a tiling census."""
from collections import Counter,defaultdict
from datetime import datetime,timezone
from itertools import combinations,permutations,product
from pathlib import Path
import json,math,os,time,xml.etree.ElementTree as ET
from extract_chain150 import points
from extract_jigsaw import transform,inside
from check_focus202_207_sources import tree,immutable,options_from_text
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/exchanges208_214'
LABELS='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHI'
SHAPES=[['01','11','21','31','10'],['00','01','02','03','11'],
        ['00','10','20','30','21'],['10','11','12','13','02'],
        ['01','11','21','31','20'],['00','01','02','03','12'],
        ['00','10','20','30','11'],['10','11','12','13','01']]
SHAPES=[frozenset((int(s[0]),int(s[1])) for s in ss) for ss in SHAPES]

def norm(cells):
    r=min(x for x,y in cells);c=min(y for x,y in cells)
    return frozenset((x-r,y-c) for x,y in cells)

def polygon(t):
    out=[];first=prev=None
    for q in t:
        ps=points(t,q)
        if q.tag=='moveto':first=prev=ps[0];out.append(prev)
        elif q.tag=='lineto':prev=ps[0];out.append(prev)
        elif q.tag=='curveto':
            controls=[prev]+ps
            for k in range(1,13):
                z=k/12;work=controls[:]
                while len(work)>1:work=[tuple((1-z)*a+z*b for a,b in zip(u,v)) for u,v in zip(work,work[1:])]
                out.append(work[0])
            prev=ps[-1]
        elif q.tag=='closepath':out.append(first);prev=first
    return out

def figure(path,ymax):
    root=ET.parse(path);polys=[]
    for t in root.iter('stroke_path'):
        ps=[v for q in t for v in points(t,q)]
        if not ps or set(t.get('color','').split())!={'0'}:continue
        a,b,c,d=min(x for x,y in ps),max(x for x,y in ps),min(y for x,y in ps),max(y for x,y in ps)
        if a>250 and 15<b-a<33 and 15<d-c<33 and c<ymax:polys.append(polygon(t))
    assert len(polys)==45
    x0=min(x for p in polys for x,y in p)-.24;y0=min(y for p in polys for x,y in p)-.24
    unit=(max(x for p in polys for x,y in p)-x0+.24)/15
    assert abs(unit-7.9947)<.001
    tiles=[frozenset((r,c) for r in range(15) for c in range(15)
             if inside(x0+(c+.5)*unit,y0+(r+.5)*unit,p)) for p in polys]
    assert all(len(p)==5 and norm(p) in SHAPES for p in tiles)
    assert Counter(v for p in tiles for v in p)==Counter({(r,c):1 for r in range(15) for c in range(15)})
    anchors={};by_label={}
    for t in root.iter('fill_text'):
        for span in t:
            for g in span:
                ch=g.get('unicode','');x,y=transform(t,float(g.get('x')),float(g.get('y')))
                if len(ch)!=1 or ch not in LABELS or not(x0<x<x0+15*unit and y0<y<y0+15*unit):continue
                r,c=math.floor((y-y0)/unit),math.floor((x-x0)/unit)
                assert ch not in anchors;anchors[ch]=(r,c)
                found=[p for p in tiles if (r,c) in p];assert len(found)==1;by_label[ch]=found[0]
    assert set(anchors)==set(LABELS) and len(set(by_label.values()))==45
    return anchors,by_label

def options(center=True,center_orientation=0):
    out=[]
    for k,s in enumerate(SHAPES):
        for i,j in product(range(15),repeat=2):
            cells=frozenset((i+a,j+b) for a,b in s)
            if any(a>=15 or b>=15 for a,b in cells):continue
            if center and (7,7) in cells and k!=center_orientation:continue
            sec={4:('V',i,j),5:('H',i+1,j),6:('V',i,j+1),7:('H',i,j)}.get(k)
            out.append((cells,sec,k,(i,j)))
    return out

HVERT=frozenset([(r,c) for r in range(4) for c in [0,2]]+[(1,1),(2,1)])
HORZ=frozenset((c,r) for r,c in HVERT)

def h_pairs(tiles):
    result=[]
    for i,j in combinations(range(len(tiles)),2):
        union=tiles[i]|tiles[j]
        if len(union)==10 and norm(union) in [HVERT,HORZ]:result.append((i,j,union))
    assert len({i for i,j,u in result}|{j for i,j,u in result})==2*len(result)
    return result

def h_splits(union):
    singles=set()
    for s in SHAPES:
        for p in union:
            for a in s:
                translated=frozenset((x+p[0]-a[0],y+p[1]-a[1]) for x,y in s)
                if translated<=union:singles.add(translated)
    pairs={frozenset((a,union-a)) for a in singles if union-a in singles}
    assert len(pairs)==2
    return pairs

def canon(tiles):
    orbit=[]
    for flip in [False,True]:
        cur=[frozenset((r,14-c if flip else c) for r,c in p) for p in tiles]
        for k in range(4):
            orbit.append(tuple(sorted(tuple(sorted(p)) for p in cur)))
            cur=[frozenset((c,14-r) for r,c in p) for p in cur]
    assert len(set(orbit))==8
    return min(orbit)

def expand(tiles):
    hs=h_pairs(tiles);unions={u for i,j,u in hs};touched={i for i,j,u in hs for i in [i,j]}
    choices=[sorted(h_splits(u),key=lambda pair:sorted(sorted(p) for p in pair)) for i,j,u in hs]
    keys=set()
    for chosen in product(*choices):
        out=[p for i,p in enumerate(tiles) if i not in touched]+[p for pair in chosen for p in pair]
        assert len(out)==45 and len(set(out))==45
        assert Counter(v for p in out for v in p)==Counter({(r,c):1 for r in range(15) for c in range(15)})
        assert {u for i,j,u in h_pairs(out)}==unions
        keys.add(canon(out))
    assert len(keys)==2**len(hs)
    return keys,hs

def tiny_sources():
    out={}
    for ver,main,answer,dx,dy in [
        ('book','original-127','original-492',0,0),
        ('draft','draft-49','draft-182',22.08,108.60)]:
        original=ROOT/'sources/focus202_207'/('original-124.txt' if ver=='book' else 'draft-46.txt')
        opts={eq:options_from_text(original,eq) for eq in [90,92]}
        new90=[tuple(map(str,r))+tuple({'01':'A','02':'B','15':'B','24':'A'}.get(''.join(map(str,r)),'')) for r in opts[90]]
        new92=[tuple(map(str,r))+tuple({'01':'A','02':'B','145':'B','234':'A'}.get(''.join(map(str,r)),'')) for r in opts[92]]
        t100=tree(OUT/(main+'.xml'),(165+dx,280+dx,320+dy,357+dy))
        ax=0 if ver=='book' else 9.66
        t209=tree(ROOT/'results/focus202_207'/(answer+'.xml'),(355+ax,416+ax,500+dy,529+dy))
        assert t100['shape']==immutable(list('0123456'),new90)
        assert t209['shape']==immutable(list('012345'),new92)
        assert len(t100['nodes'])==14 and len(t209['nodes'])==7
        out[ver]=dict(tree100=t100,tree209=t209,options99=new90,options209=new92)
    opts101={'xX':'A','xY':'CD','xZ':'E','yX':'B','yY':'AE','yZ':'F','zX':'C','zY':'BF','zZ':'D'}
    six=[tuple(a+b for a,b in zip('xyz',p)) for p in permutations('XYZ')]
    rejected=[]
    for sol in six:
        conflict={c:n for c,n in Counter(c for p in sol for c in opts101[p]).items() if n>1}
        assert conflict;rejected.append(dict(solution=sol,conflicts=conflict))
    bipairs=[('xY','yX','xX','yY'),('yY','zX','yX','zY'),('zY','xX','zX','xY'),
             ('zY','xZ','zZ','xY'),('xY','yZ','xZ','yY'),('yY','zZ','yZ','zY')]
    for sec,(a,b,c,d) in zip('ABCDEF',bipairs):
        assert set(a).isdisjoint(b) and set(c).isdisjoint(d) and set(a+b)==set(c+d)
        assert {p for p,v in opts101.items() if sec in v}=={c,d}
    opts214={'xX','xY','yX','yY','yZ','zY','zZ'}
    sols=[frozenset(s) for s in six if set(s)<=opts214];assert len(sols)==3
    pairs=[('yX','xY','yY','xX'),('yZ','zY','yY','zZ')]
    choices=[]
    for use in [pairs,[pairs[0],('yY','zZ','yZ','zY')]]:
        edges=[]
        for s in sols:
            for a,b,c,d in use:
                if {c,d}<=s:edges.append((tuple(sorted(s)),tuple(sorted((s-{c,d})|{a,b}))))
        strong=[tuple(sorted(s)) for s in sols if not any(set([c,d])<=s for a,b,c,d in use)]
        # Exhibit a fixed order making both selected orientations canonical.
        order=next(o for o in permutations(sorted(opts214)) if all(o.index(a)<o.index(b) and o.index(a)<o.index(c)<o.index(d) for a,b,c,d in use))
        choices.append(dict(bipairs=use,strong=strong,reduction_edges=edges,order=order))
    assert len(choices[0]['strong'])==2 and len(choices[1]['strong'])==1
    assert len({a for a,b in choices[0]['reduction_edges']})==1
    # Exercise212(b): the otherwise unrestricted item3 can be put last.
    itemorder={a:i for i,a in enumerate('124053')}
    key=lambda a:tuple(sorted(itemorder[c] for c in a))
    assert min(['01','24','02','14'],key=key)=='14'
    assert min(['01','25','02','15'],key=key)=='01'
    out.update(example101=rejected,example214=choices,item_order212='124053')
    return out

def main():
    assert not (OUT/'source-checked.json').exists();assert os.nice(0)>=15;start=time.monotonic()
    figures={};allopts=options();allcells=[q[0] for q in allopts]
    assert len(options(False))==1344 and len(allopts)==1309
    assert sum((7,7) in p for p,s,k,a in options(False))==40
    assert sum((7,7) in p for p,s,k,a in allopts)==5
    for name,ymax in [('original-126',200),('draft-48',300)]:
        anchors,tiles=figure(OUT/(name+'.xml'),ymax);remaining=set(product(range(15),repeat=2));path=[]
        central=next(p for p in tiles.values() if (7,7) in p)
        center_orientation=SHAPES.index(norm(central));assert center_orientation==4
        available=[p for p,s,k,a in options(center_orientation=center_orientation)]
        for ch in LABELS:
            degrees={v:sum(v in p for p in available) for v in remaining}
            mrv=min(remaining,key=lambda v:(degrees[v],v));assert mrv==anchors[ch],(name,ch,mrv,anchors[ch])
            chosen=tiles[ch];assert chosen in available and mrv in chosen
            path.append(dict(label=ch,item=mrv,degree=degrees[mrv],tile=sorted(chosen)))
            remaining-=chosen;available=[p for p in available if p.isdisjoint(chosen)]
        assert not remaining and not available
        assert [q['label'] for q in path if q['degree']==5]==list('8beghC')
        assert max(q['degree'] for q in path)==5
        keys,hs=expand([tiles[ch] for ch in LABELS]);assert len(hs)==4 and len(keys)==16
        assert any({LABELS[i],LABELS[j]}=={'8','b'} for i,j,u in hs)
        assert tiles['8']==frozenset([(1,12),(2,12),(3,12),(4,12),(3,11)])
        assert tiles['b']==frozenset([(1,10),(2,10),(3,10),(4,10),(2,11)])
        figures[name]=dict(branch_path=path,center_orientation=center_orientation,h_pairs=[dict(labels=[LABELS[i],LABELS[j]],cells=sorted(u)) for i,j,u in hs],local_incongruent_tilings=len(keys))
    assert figures['original-126']==figures['draft-48']
    # Every repeated secondary item excludes precisely the reflected H pair.
    groups=defaultdict(list)
    for p,s,k,a in allopts:
        if s:groups[s].append((p,k))
    conflicts=[];singleton=0
    for s,ps in groups.items():
        if len(ps)==1:singleton+=1;continue
        assert len(ps)==2
        (a,k),(b,l)=ps;assert a.isdisjoint(b) and norm(a|b) in [HVERT,HORZ]
        assert {k,l} in [{4,6},{5,7}]
        conflicts.append(dict(secondary=s,orientations=[k,l],cells=sorted(a|b)))
    # No Y can belong to two H unions: exhaust the possible local partner placements.
    partner=[]
    for s in SHAPES:
        ps=set()
        for h in [HVERT,HORZ]:
            for p in s:
                for v in h:
                    u=frozenset((x+p[0]-v[0],y+p[1]-v[1]) for x,y in h)
                    if s<=u and norm(u-s) in SHAPES:ps.add(u-s)
        assert len(ps)==1;partner.append(sorted(next(iter(ps))))
    bounded=json.loads((OUT/'y-bounded.json').read_text());assert bounded['status']=='time_limit' and not bounded['completed']
    canonical=set();weights=[];reports=[];secondary={p:s for p,s,k,a in allopts}
    for model in bounded['solutions']:
        tiles=[frozenset(map(tuple,q['cells'])) for q in model]
        assert all(p in secondary for p in tiles)
        assert max(Counter(secondary[p] for p in tiles if secondary[p]).values(),default=0)<=1
        keys,hs=expand(tiles);assert canonical.isdisjoint(keys);canonical|=keys
        assert not any((7,7) in u for i,j,u in hs)
        weights.append(len(hs));reports.append(dict(h_count=len(hs),expanded_count=len(keys),h_unions=[sorted(u) for i,j,u in hs]))
    expected=[2,4,5,2,3,2,5,3,5,3,2,4,3,4,2,4]
    assert len(reports)==16 and sorted(weights)==sorted(expected) and len(canonical)==sum(2**k for k in expected)==212
    small=tiny_sources()
    traces=sorted(OUT.glob('*.xml'))+list((ROOT/'results/focus202_207').glob('*.xml'))
    texts=sorted((ROOT/'sources/exchanges208_214').glob('*.txt'))+list((ROOT/'sources/focus202_207').glob('*.txt'))
    report=dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),nice=os.nice(0),
        wall_seconds=time.monotonic()-start,dependencies={p:sha(ROOT/p) for p in ['puzzle_xcc.py','extract_chain150.py','extract_jigsaw.py','check_focus202_207_sources.py']},
        source_hashes={str(p.relative_to(ROOT)):sha(p) for p in traces+texts+[OUT/'y-bounded.json']},
        figures=figures,secondary_conflicts=conflicts,irrelevant_singleton_secondary_items=singleton,
        unique_local_h_partners=partner,bounded_model_checks=reports,h_count_histogram=dict(Counter(weights)),
        independent_incongruent_tiling_lower_bound=212,upper_bound_verified=False,
        limitation='One20second run stopped after16 models without proving exhaustion.212 is independently validated as a lower bound only. Guided figure path does not establish first-search-solution status. No historical benchmark reproduced.',
        small_sources=small,accepted_partition_censuses_rerun=0,new_long_searches=0,status='PASS')
    save(OUT/'source-checked.json',report)
    print(json.dumps({k:v for k,v in report.items() if k in ['at_utc','nice','wall_seconds','independent_incongruent_tiling_lower_bound','upper_bound_verified','h_count_histogram','status']},ensure_ascii=False))

if __name__=='__main__':main()
