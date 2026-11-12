"""Independently decode all piece boundaries and chain interfaces in four figures."""
from collections import Counter
from datetime import datetime,timezone
import json
import chain150 as h
from extract_chain150 import paths,crossings,strips


def board(path,x0,y0):
    unit=10.175;rects,segs=paths(path);outlines=[]
    for a,b,c,d in rects:
        if x0-.01<=a<b<=x0+8*unit+.01 and y0-.01<=c<d<=y0+8*unit+.01:
            coords=[(a-x0)/unit,(b-x0)/unit,(c-y0)/unit,(d-y0)/unit]
            assert max(abs(q-round(q)) for q in coords)<.001;outlines.append(tuple(map(round,coords)))
    assert len(outlines)==18
    values={};raw={}
    for y in range(8):
        for x in range(8):
            for dx,dy in [(1,0),(0,1)]:
                q=(x+dx,y+dy)
                if q[0]>7 or q[1]>7:continue
                lo=(y0+(y+.1)*unit) if dx else (x0+(x+.1)*unit)
                hi=lo+.8*unit;axis=0 if dx else 1
                edge=(x0+(x+1)*unit) if dx else (y0+(y+1)*unit)
                both=[];details=[]
                for sign in [-1,1]:
                    pts=crossings(segs,axis,edge+sign*.07*unit,lo,hi)
                    kind=(2 if max(pts)-min(pts)<.3*unit else 1) if pts else 0
                    both.append(kind);details.append(pts)
                assert both[0]==both[1],(path,x,y,q,both,details)
                values[tuple(sorted(((x,y),q)))]=both[0];raw[str((x,y,q))]=details
    original,_=h.inventory();original_expected=Counter(h.canonical(p) for p in original)
    pieces,types=h.inventory(corrected=True);expected=Counter(h.canonical(p) for p in pieces)
    decoded=[];used=set();actual=Counter()
    for x1,x2,y1,y2 in outlines:
        cells={(x,y):[] for y in range(y1,y2) for x in range(x1,x2)}
        assert min(x2-x1,y2-y1)==1
        for (x,y),v in cells.items():
            assert (x,y) not in used;used.add((x,y))
            for dx,dy in h.DIRS:
                q=(x+dx,y+dy);c=values.get(tuple(sorted(((x,y),q))),0)
                v.append(int(bool(c)) if q in cells else c)
        cells={p:tuple(v) for p,v in cells.items()};actual[h.canonical(cells)]+=1;decoded.append(cells)
    assert used=={(x,y) for x in range(8) for y in range(8)}
    
    if actual!=expected:
        h.save(h.OUT/'figure-inventory-diagnostic.json',dict(path=str(path),outlines=outlines,decoded=[dict(bounds=bb,cells=h.key(pp),matches=[i for i,piece in enumerate(pieces) if h.canonical(piece)==h.canonical(pp)]) for bb,pp in zip(outlines,decoded)]))
    assert actual==expected,('Printed piece inventory mismatch',actual-expected,expected-actual)
    special=[p for p in decoded if any(2 in v for v in p.values())];assert len(special)==2
    superpiece={p:v for piece in special for p,v in piece.items()};assert len(superpiece)==11
    regular={h.canonical(t['cells']):t['name'] for t in types if t['name']!='sup'}
    placements=[dict(type=regular[h.canonical(p)],cells=p) for p in decoded if p not in special]+[dict(type='sup',cells=superpiece)]
    graph,components=h.validate(placements,corrected=True);assert components==[34]
    # Normalize the unique super-piece orientation by a global board rotation.
    target=h.key(types[-1]['cells']);normalized=None
    for k in range(4):
        ps=[]
        for p in placements:
            cells={}
            for (x,y),v in p['cells'].items():
                vv=[0]*4
                for i,c in enumerate(v):vv[(i+k)%4]=c
                for _ in range(k):x,y=7-y,x
                cells[x,y]=tuple(vv)
            ps.append(dict(type=p['type'],cells=cells))
        sup=next(p['cells'] for p in ps if p['type']=='sup');mx=min(x for x,y in sup);my=min(y for x,y in sup)
        if h.key({(x-mx,y-my):v for (x,y),v in sup.items()})==target:
            assert normalized is None;normalized=ps
    assert normalized is not None
    _,options=h.placements(corrected=True);lookup={(p['type'],h.key(p['cells'])):i for i,p in enumerate(options)}
    indexes=sorted(lookup[p['type'],h.key(p['cells'])] for p in normalized)
    return dict(outlines=outlines,visited_cells=len(graph),loop_components=components,path_key=h.path_key(graph),normalized_model=indexes,
        matches_corrected_inventory=True,matches_original_inventory=(actual==original_expected),
        extra_L_domino=actual[h.canonical(original[2])]-original_expected[h.canonical(original[2])],
        missing_S_domino=original_expected[h.canonical(original[9])]-actual[h.canonical(original[9])],
        all64_cells_covered=True,all112_grid_interfaces_checked=True,
        graph={str(p):sorted(ns) for p,ns in graph.items()},raw_crossings=raw)


def main():
    orig=h.ROOT/'results/bricks147/original-163.xml';draft=h.ROOT/'results/bricks147/draft-85.xml'
    a=strips(orig,350,380);b=strips(draft,460,490)
    assert [h.key(h.strip(r)) for r in a]==[h.key(h.strip(r)) for r in b]
    figs={};traces={str(p.relative_to(h.ROOT)):h.sha(p) for p in [orig,draft]}
    for name,filename,y0,xs in [('original','original-479.xml',85.645,[45.79,136.93,228.13,319.33]),
                              ('draft','draft-169.xml',194.23,[67.81,159.01,250.21,341.41])]:
        p=h.OUT/filename;traces[str(p.relative_to(h.ROOT))]=h.sha(p)
        for i,x0 in enumerate(xs):
            print('Checking',name,i,flush=True);figs[name+str(i)]=board(p,x0,y0)
    for i in range(4):
        for field in ['outlines','path_key','normalized_model']:assert figs['original'+str(i)][field]==figs['draft'+str(i)][field]
    assert all(p[0]<7 for p in [__import__('ast').literal_eval(v) for v in figs['original3']['graph']])
    h.save(h.OUT/'figures-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=h.sha(__file__),geometry_sha256=h.sha(h.__file__),
        extractor_sha256=h.sha(h.ROOT/'extract_chain150.py'),trace_sha256=traces,all18_question_strips_equal=True,literal_inventory_rejected_by_all_four_figures=True,
        question_pieces=a,figures=figs,all_original_and_draft_figures_equal=True))
    print('PASS150 figures:all four use corrected2L/1S inventory, not printed1L/2S. Original/draft agree; every figure has a single34-cell loop.')


if __name__=='__main__':main()
